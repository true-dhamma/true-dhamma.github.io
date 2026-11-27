#!/usr/bin/env python3
import sys, subprocess, html, json, collections, os
sys.path.insert(0, '/workspace/bd-audit/tools')
from render_review_diff import render_pair, CSS, strip_generated

REPO = '/workspace/true-dhamma'
BASE = '7fdc4e3'
HEAD = sys.argv[2] if len(sys.argv) > 2 else subprocess.run(
    ['git', '-C', REPO, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True
).stdout.strip()
OUT = sys.argv[1]
L = json.load(open('/workspace/reader-work/m-review-reader-12/applied.json'))
PROMPT = open('/workspace/reader-work/m-review-reader-12/pt8u.txt', encoding='utf-8').read()
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
p1_ch3 = [e for e in p1 if e['file'] == 'three-characteristics.md']
p2_ch3 = [e for e in p2 if e['file'] == 'three-characteristics.md']

# ---- articles: all non-vocative-only edits, complete context ----
files = sorted({e['file'] for e in L})
arts = []
st = 0
voc_rows = []
for fn in files:
    path = f'_buddhadhamma/{fn}'
    old = git_show(BASE, path).split('\n')
    new = read_new(path).split('\n')
    if old[-1] == '':
        old = old[:-1]
    if new[-1] == '':
        new = new[:-1]
    assert len(old) == len(new), (fn, len(old), len(new))
    groups = collections.OrderedDict()
    voc_e = None
    for e in L:
        if e['file'] != fn:
            continue
        if e['cat'] == '概念统一' and e['old'] == '诸比丘，':
            voc_e = e
            continue
        groups.setdefault(para(new, e['line'] - 1), []).append(e)
    if voc_e:
        voc_rows.append((fn, voc_e['count']))
    for (a, b), es in groups.items():
        B = '\n'.join(old[a:b + 1])
        A = '\n'.join(new[a:b + 1])
        x, y, meta = render_pair(B, A)
        assert strip_generated(x) == B and strip_generated(y) == A
        st += 1
        items = []
        for e in es:
            tag = '第一遍' if e['pass'] == 'p1' else '第二遍复读'
            cnt = f'（同改 {e["count"]} 处）' if e['count'] > 1 else ''
            items.append(
                f'<li><b>{esc(e["id"])} · {tag} · {esc(e["cat"])}</b>{cnt}：'
                f'<span class="o">{esc(e["old"])}</span> → <span class="n">{esc(e["new"])}</span>'
                f'<br><i>理由：</i>{esc(e["why"])}</li>'
            )
        arts.append(
            f'<article><h2>{esc(fn)}　第 {a+1}–{b+1} 行 · {len(es)} 条</h2>'
            f'<ul>{"".join(items)}</ul>'
            f'<div class="pair"><div><b>改前（{BASE}）</b><div class="text">{x}</div></div>'
            f'<div><b>改后（{HEAD}）</b><div class="text">{y}</div></div></div></article>'
        )

def table(title, rows, heads):
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    head = ''.join(f'<th>{esc(h)}</th>' for h in heads)
    return f'<section><h2>{esc(title)}</h2><table><tr>{head}</tr>{body}</table></section>'

# ---- rejection / partial ----
rej = [
    (
        '部分采纳',
        '我慢（māna）：骄傲和自我评判；渴望显赫和控制他人；对权力的追求。<br>--这三条是否适合改成 爱 慢 见？',
        '词头仍用「渴爱、我慢、见」，不改成单字「爱、慢、见」。在 L1191 补出「（汉译习称“爱、慢、见”）」。',
        '用户本轮自己定的规则（易与普通词混淆的术语加后缀；规则现为 R12-5）：单字「爱」易读成爱情，「慢」易读成缓慢。词表核心条目 taṇhā 作「渴爱」，māna 作「我慢」。列表词头与这两条一致，同时把汉译习称写在首次出现处，便于对照。'
    ),
    (
        '不采纳',
        '另外增加一个任务，看看全书中，尤其三法印那一章:苦 和 三法印中的苦/苦相/苦的法印，是否适合统一成“苦的法印？',
        '不统一成「苦的法印」。沿用总指南 4.6。',
        '三法印作为一组称「三法印」；其中单项称「无常法印／苦法印／无我法印」。一般陈述事物的性质仍用「无常、苦、无我」。某物的特相（dukkhatā、dukkha-lakkhaṇa）用「苦相」。英语 characteristic 若指「相」则用「相」（如有为相）。「苦的法印」既不像单项专名「苦法印」，也不像特相「苦相」，会把三种用法搅在一起。第三章现有用法已按 4.6 区分，无需再改。'
    ),
    (
        '不统一（两种都保留）',
        '不再受生<br>不受后有<br>--全书这两种都有（经文中之前统一为后者），看看巴利，这个到底是生，还是有？然后看看是否有必要统一？',
        '不统一。两个套语按巴利分用，全书现有用法已符合，本轮未改。',
        '「不受后有」对译 nāparaṃ itthattāya，是套语「生已尽，梵行已立，所作已办，不受后有」里的一句（itthattāya，此有、此状态），见于第三章 363 行、止观章、信仰章、涅槃章等。「不再受生」对译 natthi dāni punabbhavo（punabbhava，再生、再有）及 anabhinibbatti，英文作 no more renewed existence，泰文 ภพใหม่，套语是「这是我的最后一生，从此不再受生」，见于止观章、涅槃章、欲望章。两者不是同一个巴利词，不必强行合一。reader-style-guide 原已有此条，本轮写入词表。'
    ),
    (
        '部分采纳（保留“实体”，补清所指）',
        '但这种变化也可能反而强化他们对实体的信念：<br>--实有 vs 实体？',
        '保留「实体」，改成「强化他们“事物有实体”的观念」。',
        '全书分工：「实有」作谓语、形容词（真正存在的）；「实体」作名词（entity / substance）。这里说的是“事物是一个实体”这种观念，是名词用法，不宜改成「实有」。加上引号，把观念的内容说清楚。'
    ),
]

rej_html = '<section><h2>否定或部分否定的用户条目（原文照录）</h2>'
for i, (dec, q, do, why) in enumerate(rej, 1):
    rej_html += (
        f'<div class="rej"><h3>N{i:02d}　{esc(dec)}</h3>'
        f'<p class="q"><b>用户条目原文：</b><br>{q}</p>'
        f'<p><b>本轮处理：</b>{esc(do)}</p>'
        f'<p><b>理由与依据：</b>{why}</p></div>'
    )
rej_html += '</section>'

keep = [
    ('D01', 'three-characteristics.md 第 810、814 行「逼迫性的还是安稳的」', '按用户决定不改',
     '同一部经（SN 22.59）第 62 行作「苦还是乐」，巴利同为 dukkhaṃ vā sukhaṃ vā。用户明确答复「D01不改」，本轮不动。'),
    ('D03', 'three-characteristics.md 第 527 行及注 53 saṁsāra-dukkha', '仍待决（需改拉丁词）',
     '注 53 指出泰文版 Nd. II. 7 的 saṁsāra-dukkha 是误印，应作 saṅkhāra-dukkha，但正文举例仍用 saṁsāra-dukkha。改动会增减该行拉丁词，等有权改拉丁词的一轮再定。说明见下文「K04／D03 说明」。'),
    ('K06', 'nibbuta 词义（law-of-kamma.md 第 282 行等）', '仍待决，本轮不动',
     '记号批次以来一直待决。本轮只说明问题、给出选项，见下文「待决事项」。'),
    ('说话人标记', 'introduction-to-the-middle-way.md 第 149 行「〔诸比丘回答……〕」', '不改',
     '属说话人标记待决项。全书呼格「诸比丘，」155 处已改「比丘们，」，这一处不在呼格范围内，不动。'),
    ('冻结小标题', 'three-characteristics.md 第 1406 行「三法印的实修利益」及第 1223 行呼应句', '保留「实修」',
     '标题属冻结项。按本轮「实修」规则，这里是与理论相对的「实际修持利益」，用语本身也合适，故正文呼应句一并保留。同章「佛法实修」3 处已改为「佛法修行」。'),
    ('社区余例', '全书仍余 31 处「社区」', '本轮不改，交各章 Agent 复核',
     '已改 21 处（僧团、佛教界、团体／群体、邻里等）。剩下的多半是现代居住或一般社会生活意义上的地方社会、社群，暂保留，由各章按同一规则个案审定。清单见「跨章未了事项」。'),
    ('R027／冻结项', '逐行拉丁词、脚注、链接、硬换行、列表、标题、Dhamma 大小写、图片', '全部未动',
     'K04 那一行把拉丁经名改成中文时，原拉丁词放进括注，该行拉丁词不增不减。第三章「佛法／佛教／哲学」仍为 30／7／11，全书 767／778／46 不变。'),
]
keep_rows = [[esc(a), esc(b), esc(c), esc(d)] for a, b, c, d in keep]

pend = [
    ['K06 nibbuta 词义',
     'law-of-kamma.md 第 282 行「nibbuta（涅槃）：清凉、平息」；three-characteristics.md 第 1388 行「寂灭（tadaṅga-nibbuta）」；awakened-beings.md 第 751 行「寂灭（sītibhūta；nibbuta）」；nibbana-supreme-peace.md 中出现在 URL 和经名里。',
     '建议 A：改作「寂灭（nibbuta）」，与第三章、觉悟者章一致。<br>'
     '选项 B：改作「已涅槃」。<br>'
     '选项 C：不改。<br>'
     '<b>建议选 A。</b>nibbuta 是过去分词，意为已寂灭的、清凉的、平息的，不是名词 nibbāna（涅槃）。law-of-kamma 第 282 行把两者写成「nibbuta（涅槃）」，把词义混在一起。同段相邻词头已用「清凉（sītabhūta）」「安稳（khema）」这类「中文（巴利）」格式，改成「寂灭（nibbuta）：清凉、平息」即可，无须动拉丁词。此条自记号批次起一直待决。'],
    ['D03 saṁsāra-dukkha／saṅkhāra-dukkha',
     'three-characteristics.md 第 527 行及注 53。',
     '注 53 说泰文版 Nd. II. 7 作 saṁsāra-dukkha 是误印，应作 saṅkhāra-dukkha（诸行之苦），但正文举例仍写 saṁsāra-dukkha。改正须改拉丁词，等有权改拉丁词的一轮再定。'],
]
pend_rows = [[esc(a), esc(b), c] for a, b, c in pend]

k04 = '''<section><h2>K04 与 D03 的说明（用户问「那个巴利语是怎么回事」）</h2>
<p><b>K04（已改）。</b>原文「Mahā- 和 Cūḷadukkhakkhandha 经」是巴利经名的省写：Mahā＝大，Cūḷa＝小，dukkhakkhandha＝苦蕴（mass of suffering）。两部经是《中部》第 13 经《大苦蕴经》（Mahādukkhakkhandha Sutta, MN 13）和第 14 经《小苦蕴经》（Cūḷadukkhakkhandha Sutta, MN 14）。「Mahā-」后面的连字符表示与下一词共用同一个后缀（都是 -dukkhakkhandha），不是两个残缺的词。本轮改成「《大苦蕴经》《小苦蕴经》〔Mahā- 和 Cūḷadukkhakkhandha〕」：中文经名在前，原拉丁词全部保留在括注里，该行拉丁词一个不增不减。</p>
<p><b>D03（未改，待决）。</b>同一句后面举了 saṁsāra-dukkha。注 53 说明：泰文版所引《大义释》（Nd. II. 7）作 saṁsāra-dukkha（轮回之苦），作者认为这是误印，应作 saṅkhāra-dukkha（诸行之苦）。正文却仍按误印的形式举例。要改正文或注释里的拉丁词，须等有权改拉丁词的一轮。</p>
</section>'''

rules = '''<section><h2>本轮新增或修订的规范与词表</h2>
<h3>读者规范（reader-style-guide.md）</h3>
<p>旧规则 13、23、25、39、41 已标明废止或修订。新增 R12-1 至 R12-10（全书适用）：</p>
<ol>
<li><b>R12-1 不用古译、文言：</b>现代读者难懂的改白话（如救头燃、为得未得、多众利益）；已经懂的古译可留（此有故彼有；不受后有套语；当不放逸以成道业）。</li>
<li><b>R12-2 引号：</b>该加的加（特定说法、观念内容、括注所注的句中成分），该去的去（一般陈述、已有巴利括注的中文术语）。</li>
<li><b>R12-3 读不懂的必须改到读得懂：</b>直译谚语、文言外壳、生僻说法，改写或加简短说明。</li>
<li><b>R12-4 英文近义双词合并：</b>cause or motive 等只写一个中文词。</li>
<li><b>R12-5 易混淆术语加后缀：</b>相续相、威仪相、密集相；列表词头用渴爱、我慢、见，不单写爱、慢。</li>
<li><b>R12-6 括注巴利的范围：</b>只注紧挨在前的那个中文词；嵌在句中时加引号；列表「中文（巴利）：」；括号里只放巴利；拉丁经名改中文时原词进括注，该行拉丁词不增不减；不用「和/或」。</li>
<li><b>R12-7 标点（加强）：</b>分号只用于本身含逗号的长并列分句，或行文中的「有时……；有时……」。解释、转折、因果、短句不用分号。并列短语用顿号，与外层逗号、分号分层。</li>
<li><b>R12-8 二次翻译腔：</b>自己润色时写出的英语句式同样要改。工作流程见 reader-workflow.md。</li>
<li><b>R12-9 对仗与搭配：</b>前后对举用同一个词；同组标题句式统一。</li>
<li><b>R12-10 全书用词：</b>比丘们、恒常、彻见三法印、常见／断见与常见论／断灭论、不再受生与不受后有分用、执取／执着、修行／修习／实修、不用心灵、社区按语境、实有／实体、思考者、道德水准。</li>
</ol>
<h3>工作流程（新建 reader-workflow.md）</h3>
<p>两遍法（第一遍按规范改并复查上一轮；第一遍只发消息、不发文件；第二遍忘掉改前改后，只复读改过的地方及其上下文；交付第二遍结果）。交付 HTML 必备：两遍分类计数、否定条目须引用户原文、原始 prompt 默认收起、本轮规范变化、待决事项。</p>
<h3>全书体例（revision-guide.md 新增 m-review-reader-12 一节，15 条）</h3>
<p>呼格「比丘们」；「恒常」；常见／断见 vs 常见论／断灭论（按 -diṭṭhi／-vāda，vibhava-diṭṭhi 作无有见）；不再受生／不受后有；不用「心灵」；「社区」个案；「彻见三法印」；苦／苦相／苦法印沿用 4.6；相续相／威仪相／密集相；执取／执着；修行／修习／实修；实有／实体；括注只放巴利；神意因论；K04 拉丁经名处理。</p>
<h3>词表（glossary-final.csv）</h3>
<p>修订 8 行：santati→相续相，iriyāpatha→威仪相，ghana→密集相，sassata-diṭṭhi→常见，uccheda-diṭṭhi→断见，sassata-vāda→常见论，uccheda-vāda→断灭论，vibhava-diṭṭhi→无有见。</p>
<p>再次确认 3 行：kicca＝职责，nirāmisa-sukha＝非物质之乐，sāmisa-sukha＝物质之乐。</p>
<p>新增 13 行（reader-12）：比丘们；不再受生；不受后有；执取／执着；修行／修习／实修；恒常；不用心灵；社区分用；彻见三法印；神意因论；不放逸／放逸（中文在前）；贤善凡夫；渴爱／我慢／见（词头）。</p>
</section>'''

cross = '''<section><h2>跨章未了事项（留给各章 Agent）</h2>
<ul>
<li><b>「（巴利；中文）：」括注格式</b>：第三章已改（忧愁、绝望）。其他章仍有约 30 处同类格式（如 five-aggregates、four-noble-truths、path-factors-of-concentration／wisdom、wise-reflection 等），按 R12-6 改为「中文（巴利）：即……」。两个巴利异名并列（pubbekatahetu-vāda；pubbekata-vāda）可保留。</li>
<li><b>执取／执着／执着于</b>：规则已写入词表。第三章已逐条核对（只改 1 处：见的词头「执取于」→「执着于」）。各章现存量（执取／执着／执着于）：awakened-beings 34/42/16，calm-and-insight 8/21/4，dependent-origination 102/64/10，faith 1/8/0，five-aggregates 12/1/1，four-noble-truths 4/5/1，happiness 6/30/11，introduction-to-the-middle-way 7/10/5，law-of-kamma 2/20/9，nibbana 85/39/10，path-factors-of-concentration 13/21/9，path-factors-of-virtuous-conduct 0/16/2，path-factors-of-wisdom 2/16/6，six-sense-spheres 6/20/12，desire 8/18/3，three-characteristics 70/80/29，virtuous-friendship 1/6/0，wise-reflection 5/25/10。</li>
<li><b>修行／修习／实修</b>：规则已写入词表。第三章「佛法实修」3 处已改，「实修利益」标题保留。各章现存量（修行／修习／实修）较高者：awakened-beings 145/222/0，happiness 185/48/1，wise-reflection 153/38/0，path-factors-of-concentration 141/140/0，path-factors-of-virtuous-conduct 126/10/0，introduction-to-the-middle-way 101/73/0，calm-and-insight 71/69/0，four-noble-truths 53/74/0。请各章按规则个案处理，不要整章替换。</li>
<li><b>「社区」余 31 处</b>（本轮已改 21 处）：awakened-beings 1396、1521、1832；four-noble-truths 649；happiness 688、698、732、754、993、1883；introduction-to-the-middle-way 246、279、330、376、499、501（2 次）、505；law-of-kamma 832、1362、1370、1418、1489、1491、1493；path-factors-of-virtuous-conduct 1054；path-factors-of-wisdom 235、429；desire 649、782；virtuous-friendship 584。请按「现代居住／一般社会生活可留；僧团、佛教界、团体／群体、邻里按语境」复核。</li>
<li><b>注 102（three-characteristics.md 第 2162 行）</b>仍作「爱（taṇhā）、慢（māna）和见（diṭṭhi）」，与正文词头「渴爱、我慢、见」及「汉译习称」可以并存（注是在列举习称），各章若改相关注释，与 R12-5 对齐即可。</li>
</ul>
</section>'''

fig = '''<section><h2>配图（本轮未改图）</h2>
<p>G01　ch-3-temple-trade.jpg（第三章配图）：图中「云石寺」应作「大理石寺」；Benchamaborphit 应作 Benchamabophit。仍交回主 Agent，本轮未改任何图片或 SVG。</p>
</section>'''

voc_table = '<table><tr><th>章节</th><th>处数</th></tr>' + ''.join(
    f'<tr><td>{esc(f)}</td><td>{n}</td></tr>' for f, n in voc_rows
) + f'<tr><th>合计</th><th>{sum(n for _, n in voc_rows)}</th></tr></table>'

summary = f'''<h1>《佛法》读者润色 · m-review-reader-12</h1>
<p>基线 <code>{BASE}</code> → 本轮提交 <code>{HEAD}</code>（分支 m-review-reader-12，仅本地，未推送）。本轮是<b>中文润色</b>：按用户 pt8u 处理第三章条目、落实 D02／D04／D05／D06／K04，并作若干全书用词统一。泰文、英文、巴利只作参照。最终文本是<b>第二遍复读之后</b>的结果。</p>

<h2>两遍计数</h2>
<table>
<tr><th></th><th>条数</th><th>处数</th><th>按类型</th></tr>
<tr><td>第一遍</td><td>{len(p1)}</td><td>{sum(e["count"] for e in p1)}</td><td>第三章 {len(p1_ch3)} 条／{sum(e["count"] for e in p1_ch3)} 处；其他章 {len(p1)-len(p1_ch3)} 条／{sum(e["count"] for e in p1)-sum(e["count"] for e in p1_ch3)} 处。<br>类型：{esc(cats_html(collections.Counter(e["cat"] for e in p1)))}。</td></tr>
<tr><td>第二遍复读回改</td><td>{len(p2)}</td><td>{sum(e["count"] for e in p2)}</td><td>第三章 {len(p2_ch3)} 条，path-factors-of-virtuous-conduct.md 3 条。<br>类型：{esc(cats_html(collections.Counter(e["cat"] for e in p2)))}（含二次翻译腔 {sum(1 for e in p2 if e["cat"]=="二次翻译腔")}）。</td></tr>
<tr><td>合计（交付）</td><td>{len(L)}</td><td>{sum(e["count"] for e in L)}</td><td>对照段落 {len(arts)} 个（不含纯「诸比丘」机械替换的段落，那些见下表）。</td></tr>
</table>
<p>第一遍还复查了 reader-11 的 524 条旧改动，其中 40 条在本轮第一遍里作了后续修正（分号、文言、二次翻译腔、双词、括注）。第二遍忘掉改前改后，只把改过的地方放回上下文重读。</p>

<h2>验证</h2>
<p>43 份 MD Kramdown 零警告，脚注 2120/2120；AIPali 3300、内链 4325、硬换行 1540、列表项 2485 与冻结基线一致；frozen_check 无违规（逐行拉丁词一致）；各章 DOM 骨架与基线相同；第三章「佛法／佛教／哲学」30／7／11，全书 767／778／46 不变；nibbuta、说话人标记未动；{st} 段对照均通过剥离标签往返自检。未改任何图片。</p>

<details><summary>本轮用户原始 prompt（pt8u，点击展开）</summary>
<pre class="prompt">{esc(PROMPT)}</pre>
</details>
'''

voc_sec = f'''<section><h2>全书呼格「诸比丘，」→「比丘们，」（D05）</h2>
<p>共 {sum(n for _, n in voc_rows)} 处，按文件如下。这是纯中文替换，不改拉丁词、不改说话人标记。示例见各章若与其他改动同段的对照；其余从略，避免大量重复。</p>
{voc_table}
</section>'''

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

doc = (
    f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
    f'<title>m-review-reader-12 润色对照</title><style>{style}</style></head><body>'
    + summary + rej_html + k04
    + table('待决事项（下一批发给用户）', pend_rows, ('编号', '位置', '选项与建议'))
    + table('不改／暂不改（缘由与依据）', keep_rows, ('编号', '位置', '决定', '缘由与依据'))
    + rules + voc_sec + cross + fig
    + '<section><h2>逐段修改（完整语境，最终文本对照基线 7fdc4e3）</h2>'
    '<p>每段先列第一遍、第二遍的逐条改动，再给出整段改前／改后对照。第二遍回改已并入「改后」栏。</p></section>'
    + ''.join(arts) + '</body></html>'
)
open(OUT, 'w', encoding='utf-8').write(doc)
print('ok', 'arts', len(arts), 'st', st, 'head', HEAD, 'bytes', os.path.getsize(OUT))
