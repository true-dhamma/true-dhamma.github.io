#!/usr/bin/env python3
"""Read-only, Unicode-aware PDF-excerpt locator for Markdown. Stdlib only."""
from __future__ import annotations
import argparse
from array import array
import bisect
from collections import defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
import html
import json
from pathlib import Path
import re
import sys
import unicodedata

FOOTNOTE = re.compile(r'\[\\\[\d+\\\]\]\(#fn-fn\d+\)\{:\s*id="fr-fn\d+"\}')
PATTERNS = [FOOTNOTE, re.compile(r'\[\^[^\]\n]+\]'),
            re.compile(r'\[&nbsp;↩&nbsp;\]\([^\n)]*\)'),
            re.compile(r'\{:[^}\n]*\}'), re.compile(r'<!--.*?-->', re.S),
            re.compile(r'<[^>\n]+>'),
            re.compile(r'^ {0,3}\[[^\]\n]+\]:\s*https?://[^\n]*', re.M)]
PDF_NOISE = re.compile(r'\[(?:\\\[)?\d{1,4}(?:\\\])?\]|【\d{1,4}】|[⁰¹²³⁴⁵⁶⁷⁸⁹]+')
ENTITY = re.compile(r'&(?:#\d+|#x[0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]+);')


def normalize(text: str, *, pdf_footnotes: bool = False) -> tuple[str, array]:
    """Return normalized visible text and per-character original character offsets.

    All whitespace/punctuation is ignored for retrieval, not for proposed edits.
    Literal digits remain unless pdf_footnotes explicitly removes bracket/super
    note forms. Markdown footnote syntax is always ignored. No files are written.
    """
    hidden = bytearray(len(text))
    def hide(a: int, b: int):
        hidden[a:b] = b'\x01' * (b-a)
    fm = re.match(r'\A\ufeff?---\s*\n.*?\n---[^\n]*(?:\n|$)', text, re.S)
    if fm:
        hide(*fm.span())
    for pattern in PATTERNS:
        for m in pattern.finditer(text):
            hide(*m.span())
    if pdf_footnotes:
        for m in PDF_NOISE.finditer(text):
            hide(*m.span())
    # Link labels stay visible; balanced destinations (including parentheses)
    # and optional titles are hidden. Never fetch a URL.
    for m in re.finditer(r'!?\[([^\]\n]*)\]\(', text):
        if hidden[m.start()]:
            continue
        i, depth = m.end(), 1
        while i < len(text) and depth:
            if text[i] == '\\':
                i += 2
                continue
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1
            i += 1
        if not depth:
            label_start = text.index('[', m.start()) + 1
            hide(m.start(), label_start)
            hide(m.end()-2, i)
    for m in re.finditer(r'\[([^\]\n]+)\]\[[^\]\n]*\]', text):
        if not hidden[m.start()]:
            hide(m.start(), m.start()+1)
            hide(m.start()+1+len(m[1]), m.end())
    entities = {m.start(): m for m in ENTITY.finditer(text)}
    chars: list[str] = []
    offsets = array('I')
    i = 0
    while i < len(text):
        if hidden[i]:
            i += 1
            continue
        start = i
        if i in entities:
            ent = entities[i]
            cluster = html.unescape(ent[0])
            i = ent.end()
        else:
            cluster = text[i]
            i += 1
            while i < len(text) and not hidden[i] and unicodedata.combining(text[i]):
                cluster += text[i]
                i += 1
        for ch in unicodedata.normalize('NFKC', cluster).casefold():
            if ch.isalnum() or unicodedata.category(ch).startswith('M'):
                chars.append(ch)
                offsets.append(start)
    return ''.join(chars), offsets


@dataclass
class Document:
    path: Path
    raw: str
    text: str
    offsets: array
    line_starts: list[int]

    @classmethod
    def load(cls, path: Path) -> Document:
        raw = path.read_text(encoding='utf-8')
        text, offsets = normalize(raw)
        return cls(path, raw, text, offsets,
                   [0] + [m.end() for m in re.finditer('\n', raw)])

    def result(self, a: int, b: int, score: float, context: int) -> dict:
        source_a = self.offsets[a]
        source_b = self.offsets[b-1]+1
        line_a = bisect.bisect_right(self.line_starts, source_a)
        line_b = bisect.bisect_right(self.line_starts, source_b)
        first = max(1, line_a-context)
        last = min(len(self.line_starts), line_b+context)
        lines = self.raw.splitlines()
        return {'file': str(self.path), 'line': line_a, 'end_line': line_b,
                'column': source_a-self.line_starts[line_a-1]+1,
                'score': round(score, 4), 'source_start': source_a,
                'source_end': source_b,
                'context': [{'line': n, 'text': lines[n-1]}
                            for n in range(first, min(last, len(lines))+1)]}


def locate(query: str, paths: list[Path], *, top: int = 5,
           pdf_footnotes: bool = False, context: int = 1,
           min_score: float = .45) -> list[dict]:
    q, _ = normalize(query, pdf_footnotes=pdf_footnotes)
    if len(q) < 4:
        raise ValueError('规范化后至少需 4 个字符；建议粘贴 15–200 字的连续正文。')
    if len(q) > 4000:
        raise ValueError('单次规范化查询最多 4000 字；请分段定位。')
    docs = [Document.load(p) for p in paths]
    exact = []
    for doc in docs:
        start = 0
        while len(exact) < top * 10:
            start = doc.text.find(q, start)
            if start < 0:
                break
            exact.append(doc.result(start, start+len(q), 1., context))
            start += 1
    if exact:
        return sorted(exact, key=lambda r: (r['file'], r['line']))[:top]
    # Distributed anchors nominate windows. SequenceMatcher supplies local
    # alignment and ranks only the best nominees; never apply the result.
    seed_len = max(2, min(9, len(q)//6))
    positions = sorted({round(i*(len(q)-seed_len)/15) for i in range(16)})
    bucket_size = max(4, len(q)//8)
    nominations = defaultdict(list)
    for di, doc in enumerate(docs):
        for qp in positions:
            seed = q[qp:qp+seed_len]
            pos = -1
            for _ in range(80):
                pos = doc.text.find(seed, pos+1)
                if pos < 0:
                    break
                start = max(0, pos-qp)
                nominations[(di, start//bucket_size)].append(start)
    ranked = sorted(nominations.items(), key=lambda kv: -len(kv[1]))[:180]
    candidates = []
    for (di, _), starts in ranked:
        doc = docs[di]
        start = sorted(starts)[len(starts)//2]
        slack = max(15, len(q)//3)
        lo, hi = max(0, start-slack), min(len(doc.text), start+len(q)+slack)
        window = doc.text[lo:hi]
        blocks = [b for b in SequenceMatcher(None, q, window, autojunk=False).get_matching_blocks() if b.size]
        if not blocks:
            continue
        a, b = lo+blocks[0].b, lo+blocks[-1].b+blocks[-1].size
        # Include missing/mistyped query edges in the comparison window.
        a = max(lo, a-blocks[0].a)
        b = min(hi, b+len(q)-(blocks[-1].a+blocks[-1].size))
        score = SequenceMatcher(None, q, doc.text[a:b], autojunk=False).ratio()
        if score >= min_score:
            candidates.append((score, di, a, b))
    chosen = []
    for score, di, a, b in sorted(candidates, reverse=True):
        if any(di == odi and min(b, ob)-max(a, oa) > .5*min(b-a, ob-oa)
               for _, odi, oa, ob in chosen):
            continue
        chosen.append((score, di, a, b))
        if len(chosen) >= top:
            break
    return [docs[di].result(a, b, score, context) for score, di, a, b in chosen]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('query', nargs='?', help='PDF 粘贴文本；也可用 --query-file 或标准输入')
    p.add_argument('--query-file', type=Path)
    p.add_argument('--root', type=Path, default=Path('/workspace/bd-thai-all/_buddhadhamma'))
    p.add_argument('--glob', default='*.md', help='root 内检索范围，如 **/*.md')
    p.add_argument('--top', type=int, default=5)
    p.add_argument('--context', type=int, default=1)
    p.add_argument('--min-score', type=float, default=.45)
    p.add_argument('--pdf-footnotes', action='store_true', help='显式移除 PDF [12]、【12】、上标数字；可能误删真实数字')
    p.add_argument('--label', help='原用户 PDF 页号，如 P10，仅作报告标签，不进入匹配')
    p.add_argument('--id', dest='issue_id', help='人工校对问题编号，仅作报告标签')
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    if args.top < 1 or args.context < 0 or not 0 <= args.min_score <= 1:
        p.error('top >= 1、context >= 0、min-score 在 0..1 之间')
    query = args.query_file.read_text(encoding='utf-8') if args.query_file else args.query
    if query is None:
        if sys.stdin.isatty():
            p.error('请提供 query、--query-file 或标准输入')
        query = sys.stdin.read()
    paths = sorted(args.root.glob(args.glob))
    if not paths:
        p.error('root/glob 下没有 Markdown 文件')
    try:
        matches = locate(query, paths, top=args.top, context=args.context,
                         pdf_footnotes=args.pdf_footnotes, min_score=args.min_score)
    except (ValueError, OSError) as e:
        p.error(str(e))
    payload = {'label': args.label, 'id': args.issue_id, 'read_only': True,
               'notice': '相似度不是置信概率；必须核对原文上下文，严禁自动据此编辑。',
               'matches': matches}
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(' / '.join(x for x in (args.label, args.issue_id) if x) or '只读模糊定位')
        print(payload['notice'])
        for n, r in enumerate(matches, 1):
            print(f"\n{n}. {r['file']}:{r['line']}:{r['column']}–{r['end_line']}  score={r['score']:.4f}")
            for ln in r['context']:
                print(f"{ln['line']:>5} | {ln['text']}")
        if not matches:
            print('未找到候选；请换一段较长正文、缩小文件范围，或明确开启 --pdf-footnotes。')
    return 0 if matches else 1

if __name__ == '__main__':
    sys.exit(main())
