"""Unit and actual-book integration tests. Read-only; no book writes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from md_fuzzy_locator import normalize, Document, locate

ROOT = Path('/workspace/bd-thai-all/_buddhadhamma')
HERE = Path(__file__).resolve().parent


class NormalizationTests(unittest.TestCase):
    def test_markdown_visible_text_and_balanced_url(self):
        s = '**正见**与[如理作意](https://example.test/a_(b) "标题"){: target="_blank"}。'
        n, offsets = normalize(s)
        self.assertEqual(n, '正见与如理作意')
        self.assertEqual(s[offsets[n.index('如')]], '如')
        self.assertNotIn('example', n)

    def test_custom_footnotes_and_backlinks(self):
        s = '正见[\\[73\\]](#fn-fn73){:id="fr-fn73"}与智慧[^x]。[&nbsp;↩&nbsp;](#fr-fn73)\n{: id="fn-fn73"}'
        self.assertEqual(normalize(s)[0], '正见与智慧')

    def test_pdf_noise_requires_opt_in(self):
        s = '正见[73]，如理【12】作意⁴；DN 16，2026 年，P10'
        self.assertIn('73', normalize(s)[0])
        self.assertEqual(normalize(s, pdf_footnotes=True)[0], '正见如理作意dn162026年p10')

    def test_unicode_and_mapping(self):
        s = 'ＡＢＣ　Cafe\u0301\n智慧'
        n, offsets = normalize(s)
        self.assertEqual(n, 'abccafé智慧')
        self.assertEqual(s[offsets[n.index('é')]], 'e')
        self.assertEqual(s[offsets[n.index('智')]], '智')

    def test_frontmatter_html_entities_reference_links(self):
        s = '\ufeff---\ntitle: 不应检索\n---\n[智慧][w]&nbsp;与<em>正见</em>\n[w]: https://example.test'
        self.assertEqual(normalize(s)[0], '智慧与正见')

    def test_too_short_query_rejected(self):
        with self.assertRaises(ValueError):
            locate('正见', [])


@unittest.skipUnless(ROOT.exists(), 'requires actual book checkout')
class ActualBookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hashes = {p: hashlib.sha256(p.read_bytes()).digest() for p in ROOT.glob('*.md')}

    @classmethod
    def tearDownClass(cls):
        assert all(hashlib.sha256(p.read_bytes()).digest() == h for p, h in cls.hashes.items()), 'BOOK WAS MODIFIED'

    def assert_hit(self, query, file, line, **kw):
        rs = locate(query, [ROOT/file], **kw)
        self.assertTrue(rs)
        self.assertEqual(rs[0]['file'], str(ROOT/file))
        self.assertEqual(rs[0]['line'], line)
        self.assertTrue(any(c['line'] == line for c in rs[0]['context']))
        return rs[0]

    def test_pdf_broken_lines_and_note_artifact(self):
        q = '真理并不局限于婆罗门与《吠陀》（Veda）[4]\n\n的教条，而是客观\n和普遍的。'
        r = self.assert_hit(q, 'awakened-beings.md', 36, pdf_footnotes=True)
        self.assertEqual(r['score'], 1.)
        self.assertIn('《吠陀》', next(c['text'] for c in r['context'] if c['line']==36))

    def test_ch15_final_title(self):
        self.assertEqual(self.assert_hit('中道先导：正见\n生起的内在因缘', 'wise-reflection.md', 7)['score'], 1.)

    def test_actual_footnote_location_survives_noise(self):
        q = '这些品质是梵行（brahmacariya）的重要目标；【73】\n它们是比丘的行为和修行的标准；[74]'
        self.assertEqual(self.assert_hit(q, 'awakened-beings.md', 651, pdf_footnotes=True)['score'], 1.)

    def test_approximate_typo_ranked_with_original_context(self):
        # PDF/OCR-like one-character error: 客观 -> 客覌.
        q = '真理并不局限于婆罗门与《吠陀》（Veda）的教条，而是客覌和普遍的'
        r = self.assert_hit(q, 'awakened-beings.md', 36)
        self.assertGreater(r['score'], .90)
        self.assertLess(r['score'], 1.)

    def test_real_aipali_link_and_pdf_line_breaks(self):
        import re
        path = ROOT/'awakened-beings.md'
        chosen = None
        for line_no, line in enumerate(path.read_text().splitlines(), 1):
            if 'https://aipali.' in line and len(line) > 180 and '↩' not in line:
                # Independent display-only approximation, not normalize().
                visible = re.sub(r'\[([^\]]+)\]\(https?://[^)]+\)', r'\1', line)
                visible = re.sub(r'\{:[^}]+\}', '', visible)
                visible = re.sub(r'\[\\\[\d+\\\]\]\(#fn-fn\d+\)', '', visible)
                chosen = (line_no, visible[:160]); break
        self.assertIsNotNone(chosen)
        no, text = chosen
        q = '\n\n'.join(text[i:i+17] for i in range(0, len(text), 17))
        self.assertEqual(self.assert_hit(q, path.name, no)['score'], 1.)

    def test_approximate_ranked_against_whole_book(self):
        q = '真理并不局限于婆罗门与《吠陀》（Veda）的教条，而是客覌和普遍的'
        matches = locate(q, sorted(ROOT.glob('*.md')), top=4)
        self.assertTrue(matches)
        self.assertEqual(Path(matches[0]['file']).name, 'awakened-beings.md')
        self.assertEqual(matches[0]['line'], 36)
        self.assertGreater(matches[0]['score'], .90)
        self.assertEqual([r['score'] for r in matches], sorted((r['score'] for r in matches), reverse=True))

    def test_cli_full_book_json_labels(self):
        run = subprocess.run([sys.executable, str(HERE/'md_fuzzy_locator.py'),
                              '中道先导：正见\n生起的内在因缘', '--label', 'P10', '--id',
                              'M-LOC-01', '--top', '3', '--json'], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        report = json.loads(run.stdout)
        self.assertTrue(report['read_only'])
        self.assertEqual((report['label'], report['id']), ('P10', 'M-LOC-01'))
        self.assertEqual(Path(report['matches'][0]['file']).name, 'wise-reflection.md')
        self.assertEqual(report['matches'][0]['line'], 7)

    def test_line_mapping_custom_marker_boundary(self):
        doc = Document.load(ROOT/'awakened-beings.md')
        q = '这些品质是梵行'
        start = doc.text.index(q)
        r = doc.result(start, start+len(q), 1., 0)
        self.assertEqual(r['line'], 651)
        self.assertEqual(doc.raw[r['source_start']:r['source_end']], q)


if __name__ == '__main__':
    unittest.main(verbosity=2)
