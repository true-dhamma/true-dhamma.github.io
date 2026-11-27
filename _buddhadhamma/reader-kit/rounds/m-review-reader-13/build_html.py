#!/usr/bin/env python3
import sys, subprocess, html, json, collections, os
sys.path.insert(0, '/workspace/bd-audit/tools')
from render_review_diff import render_pair, CSS, strip_generated

REPO = '/workspace/true-dhamma'
BASE = 'e0478db'
HEAD = sys.argv[2] if len(sys.argv) > 2 else subprocess.run(
    ['git', '-C', REPO, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True
).stdout.strip()
OUT = sys.argv[1]
L = json.load(open('/workspace/reader-work/m-review-reader-13/applied.json'))
PROMPT = open('/workspace/reader-work/m-review-reader-13/pt9u.txt', encoding='utf-8').read()
esc = html.escape

def git_show(rev, path):
    return subprocess.run(['git', '-C', REPO, 'show', f'{rev}:{path}'], capture_output=True, text=True).stdout

def read_new(path):
    return open(f'{REPO}/{path}', encoding='utf-8').read()

def para(lines, k):
    a = k
    while a > 0 and lines[a - 1].strip():
        a -= 1
    b = k
    while b < len(lines) - 1 and lines[b + 1].strip():
        b += 1
    return a, b

def cats_html(counter):
    return '、'.join(f'{k} {v}' for k, v in counter.most_common())

p1 = [e for e in L if e['pass'] == 'p1']
p2 = [e for e in L if e['pass'] == 'p2']
files = sorted({e['file'] for e in L})
arts = []
for fn in files:
    path = f'_buddhadhamma/{fn}'
    old = git_show(BASE, path).split('\n'); new = read_new(path).split('\n')
    assert len(old) == len(new)
    groups = collections.OrderedDict()
    for e in L:
        if e['file'] == fn:
            groups.setdefault(para(new, e['line'] - 1), []).append(e)
    for (a, b), es in groups.items():
        B = '\n'.join(old[a:b + 1]); A = '\n'.join(new[a:b + 1])
        x, y, meta = render_pair(B, A)
        assert strip_generated(x) == B and strip_generated(y) == A
        items = ''.join(
            f'<li><b>{esc(e["id"])} · {"第一遍" if e["pass"]=="p1" else "第二遍复读"} · {esc(e["cat"])}</b>：'
            f'<span class="o">{esc(e["old"])}</span> → <span class="n">{esc(e["new"])}</span>'
            f'<br><i>理由：</i>{esc(e["why"])}</li>' for e in es)
        arts.append(f'<article><h2>{esc(fn)}　第 {a+1}–{b+1} 行 · {len(es)} 条</h2><ul>{items}</ul>'
            f'<div class="pair"><div><b>改前（{BASE}）</b><div class="text">{x}</div></div>'
            f'<div><b>改后（{HEAD}）</b><div class="text">{y}</div></div></div></article>')

def table(title, rows, heads):
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    head = ''.join(f'<th>{esc(h)}</th>' for h in heads)
    return f'<section><h2>{esc(title)}</h2><table><tr>{head}</tr>{body}</table></section>'

c1 = collections.Counter(e['cat'] for e in p1); c2 = collections.Counter(e['cat'] for e in p2)
summary = f'''<h1>《佛法》读者润色 · m-review-reader-13</h1>
<section><p>基线 <code>{BASE}</code> → 本轮 <code>{HEAD}</code>（本地分支 m-review-reader-13，未推送）。</p>
<p><b>第一遍 {len(p1)} 条</b>（{cats_html(c1)}；law-of-kamma 1 条，第三章 11 条）。<b>第二遍复读 {len(p2)} 条</b>（{cats_html(c2)}；“二次翻译腔”0 条）。</p>
<p>校验：Kramdown 0 警告；脚注 2120/2120；AIPali 3300；内链 4325；硬换行 1540；列表项 2485；逐行拉丁词 0 违规（白名单 <code>latin-allow.json</code> 为空）；DOM 骨架两文件均不变；图片未动。</p>
<p>第三章计数（基线 → 本轮）：佛教 7 → 2（剩下 2 处都是“佛教徒”），佛法 30 → 36，哲学 11 → 11。</p>
<p>全书项目计划（21 批，待确认）：<code>_buddhadhamma/reader-kit/PROJECT-PLAN.md</code>，交付目录里另有一份。</p></section>
<details><summary>用户本轮原始 prompt（pt9u，点开查看）</summary><pre class="prompt">{esc(PROMPT)}</pre></details>'''

quotes = f'''<section><h2>用户待决意见的处理</h2>
<div class="rej"><div class="q">先解除拉丁语词冻结，按建议改K06和D03，改完复核后，恢复冻结。</div>
<p><b>K06 · 采纳（选项 A），格式有调整</b>：law-of-kamma 第 282 行 <code>nibbuta（涅槃）</code> → <code>nibbuta（寂灭）</code>。nibbuta 是过去分词“已寂灭的、清凉的”，不是 nibbāna。该行 11 个词头全部是“巴利（中文）：”格式；照字面改成“寂灭（nibbuta）”会让这一词头和其余 10 个不一致，所以只改括号里的中文，拉丁词不增不减。整行是否按 R12-6 改成中文在前，留给 law-of-kamma 批次（PROJECT-PLAN B04）一起处理。</p>
<p><b>D03 · 部分否定：拉丁词不改</b>。我对照了泰文注 165：正文的 สังสารทุกข์（saṁsāra-dukkha，出处 Vism. 531、VbhA. 145、149）是对的；误印只出现在泰文字母版《小义释》（Nd. II. 7 等处），那里把 saṅkhāra 印成了 saṁsāra。原建议的前提（正文应改作 saṅkhāra）不成立，所以第 527 行和注 53 的拉丁词都不动。改的是中文：第 527 行补了中文括注“（轮回之苦）”；注 53 原文“某些印本……系误印”说反了误印的位置，现在改成“见于 Vism. 531；VbhA. 145, 149 等。泰文字母版《小义释》有几处（如 Nd. II. 7）也作 saṁsāra-dukkha，那是传本讹误，应作 saṅkhāra-dukkha（行苦）。”</p>
<p><b>恢复冻结</b>：本轮没有任何拉丁词改动，白名单为空，冻结照旧。frozen_check 新增了 <code>--allow</code> 白名单机制，已测试：不在白名单的拉丁词改动会报错退出，登记在白名单的可以通过。</p></div>
<div class="rej"><div class="q">彻底解除R027冻结：全章计数 佛法 30、佛教 7、哲学 11 与基线一致。佛陀教法 佛法教义 佛教教义 佛教教法 佛教 等，遇到后参考TH，看是 佛教 还是 佛法 还是什么，在不违背TH真实含义的基础上，在佛法和佛教之间，优先倾向于 佛法 而不是 佛教--改后复核，并写入reader指南</div>
<p><b>采纳</b>：第三章逐处对照泰文，共改 9 处（见下方逐段对照）；规则已写进 reader-style-guide 的 R13-1，并同步到 revision-guide 和词表。R027 在 frozen_check 中改为只报告、不拦截。</p></div></section>'''

keep_rows = [
 ('K1', 'three-characteristics 第 1851、1853 行', '保留“佛教徒”', '泰文 ชาวพุทธ，指信众群体，属于 R13-1 允许用“佛教”的群体义。'),
 ('K2', 'three-characteristics 第 1006 行', '保留“整个教法体系”', '同一句里已有“佛法”，再改成“佛法体系”会在一句话里重复。'),
 ('K3', 'three-characteristics 第 567、758 行', '保留“教法／教义”', '指具体的教导内容，不是宗教名称，不属于佛法和佛教二选一的情况。'),
 ('K4', '第三章“哲学”11 处', '不改', '用户明确说“哲学”不动；R039 不重开。'),
 ('K5', '第 766–770 行“常见论、断灭论”等', '保留“论”', '这一段泰文 ทิฏฐิ／วาท 都有，reader-12 已定为“论”，本轮只把主语改成“这就否定了……”。'),
 ('K6', 'D03 拉丁词', '不改', '见上：泰文注 165 证明正文的 saṁsāra-dukkha 无误。'),
 ('K7', 'law-of-kamma 第 282 行整行格式', '暂不改', '留给 B04 批次，按 R12-6 整行统一。'),
]
rules = '''<section><h2>本轮新增或修订的规范与词表</h2><ul>
<li><b>R13-1 佛法／佛教</b>：逐处对照泰文；能用“佛法”的优先用“佛法”；“佛教”只用于宗教、历史、群体（佛教徒、佛教界、佛教国家）；不给泰文添加没有的意思（如“佛陀教法”→泰文只是“这就”）；拆开“佛教教义”一类叠词；“哲学”不动。原 R027（第 47 条）已废止。</li>
<li><b>R13-2 拉丁词白名单</b>：确实需要改拉丁词时，经用户批准后登记到 <code>reader-kit/tools/latin-allow.json</code>（文件、行、改前改后词形），frozen_check 用 <code>--allow</code> 校验；白名单之外仍然冻结。</li>
<li><b>R13-3</b>：nibbuta 译“寂灭”，不译“涅槃”。</li>
<li>词表 <code>glossary-final.csv</code> 新增 3 行：佛法优先规则；nibbuta 寂灭；saṁsāra-dukkha 轮回之苦（附误印说明）。</li>
<li>工具：<code>reader-kit/tools/frozen_check.py</code>（新增 --allow，R027 只报告）、<code>dom_skeleton.rb</code>、<code>latin-allow.json</code>。</li>
<li>reader-workflow、KICKOFF-PROMPT、revision-guide、reader-notes、README 已同步。</li></ul></section>'''
pend = '''<section><h2>待决与跨章</h2><p>本轮没有新的待决事项。law-of-kamma 第 282 行整行格式、第 583 行“牛虻”等跨章事项已列入 PROJECT-PLAN.md 的第八节，并指定了处理批次。仍然待决的有：Dhamma 大小写、说话人标记、R039、配图 G01。全书分批方案请看 PROJECT-PLAN.md 第九节的 5 个确认问题。</p></section>'''
style = (
    'body{background:#0f1115;color:#e6e6e6;font:15px/1.75 "Noto Sans CJK SC","PingFang SC",sans-serif;'
    'margin:0 auto;max-width:1400px;padding:24px}'
    'h1,h2,h3{color:#9cdcfe}h2{font-size:18px}h3{font-size:16px}'
    'article,section{border:1px solid #2d3340;border-radius:8px;margin:18px 0;padding:12px 16px;background:#161a22}'
    '.pair{display:grid;grid-template-columns:1fr 1fr;gap:12px}'
    '.text{white-space:pre-wrap;background:#0b0d12;border:1px solid #2a2f3a;border-radius:6px;padding:10px}'
    'ul{padding-left:20px}li{margin:6px 0}'
    '.o{color:#ff9aa8}.n{color:#8fe3b5}'
    'table{border-collapse:collapse;width:100%}td,th{border:1px solid #2d3340;padding:6px;vertical-align:top}th{background:#1d2330}'
    'code{color:#ce9178}'
    'details{border:1px solid #2d3340;border-radius:8px;padding:8px 16px;margin:18px 0;background:#161a22}'
    'summary{cursor:pointer;color:#9cdcfe;font-weight:600}'
    'pre.prompt{white-space:pre-wrap;background:#0b0d12;border:1px solid #2a2f3a;border-radius:6px;padding:12px;color:#c8c8c8}'
    '.rej{border-top:1px solid #2d3340;padding-top:8px;margin-top:12px}'
    '.q{background:#0b0d12;border-left:3px solid #ce9178;padding:8px 12px}'
    + CSS
)
doc = (f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>m-review-reader-13 润色对照</title><style>{style}</style></head><body>'
    + summary + quotes + table('不改／暂不改（缘由与依据）', keep_rows, ('编号', '位置', '决定', '缘由与依据')) + rules + pend
    + f'<section><h2>逐段修改（完整语境，最终文本对照基线 {BASE}）</h2><p>第二遍的回改已并入“改后”栏。</p></section>'
    + ''.join(arts) + '</body></html>')
open(OUT, 'w', encoding='utf-8').write(doc)
print('ok', 'arts', len(arts), 'head', HEAD, 'bytes', os.path.getsize(OUT))
