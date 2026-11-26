# 《佛法》（Buddhadhamma）中文译本修订指南

版本：2026-11-25（G4基础及后续审定；最新m-review-notation-05集成验收完成；五批结束，idle）· 依据：英文版 buddhadhamma.github.io、中文版 true-dhamma `_buddhadhamma/`、术语审计（bd-audit/glossary.md、toc.md）以及用户的审定意见。
配套文件：`glossary-final.csv`（定稿词表，修订时逐条对照）。

> 语义审校既有状态（reader02历史记录，非本轮进度）：reader02已完成R007/R008/R012/R018/R020/R022/R043/R034八项限定词义复核。以下历史批次的“全书延伸待审”在这八项上由文末reader02规则及本阶段清单更新；R027/R039所涉佛教/佛法/哲学仍待审。编号02规则不恢复；其他已接受规范不变。


---

## 一、总体原则

### 1.1 标题格式
- 部/篇/章一律写成：`第一部：xxx`、`第二篇：xxx`、`第三章：xxx`（用中文数字，接全角冒号“：”，不留空格）。
- 附录写成 `附录一：xxx`、`附录二：xxx`；书末附录写成 `附录：心（Citta）、识（Viññāṇa）、意（Mano）`（G4 例外，见下条）。
- 非源标的编辑式 `#n` 须按语境重译：小节可用“一、二、”，既定题名如“二元论之一”可保留；修习/道的分阶段须说明其实际所指，不机械改“道之一”。原典卷章标识（如 Pariccheda #28）仍按冻结源标保留。详见 m-review-numbering-01。
- **目录和所有标题里都不放巴利文、英文**，只放准确的中文（正文首次出现时可以括注巴利文）。
  - **例外（G4）**：书末附录“心（Citta）、识（Viññāṇa）、意（Mano）”整篇都在解释这些巴利词，所以它的标题（h1、导航 yml、nav.md、页面 title）和小标题保留巴利括注，例如“识界（Viññāṇa-dhātu）与涅槃界（Nibbāna-dhātu）”“关于“知者”（Phoo Roo）的讨论”；正文中说明所讨论词语的巴利括注也保留。只适用于这一篇。
- 篇名保留问句风格（跟泰文原版一致），如 `第二篇：生命是怎样的？`。
- `nav.md` 的标题必须和各页 h1 逐字相同。
- **目录定稿不得改动（B8-r2，用户决定）**：第二节“定稿目录对照表”的“定稿”列（含所有“保留”项）是用户确认的最终标题；批次校对中一律不得改动这些标题（h1–h4、nav、yml），即使觉得译文可改，也只能列为“待定”请用户决定。每批交付前用 `b9/toccheck.py` 核对标题与定稿列一致。

### 1.2 巴利文括注
- 正文中术语**首次**出现时括注巴利文：`念（sati）`。括号用全角“（ ）”，巴利文小写，保留变音符号（ā ī ū ṁ ṅ ñ ṭ ḍ ṇ ḷ）。
- 同一章内后面再出现时，如果没有辨义的需要，就不再括注。
- 要统一成全角括号：现在混用了半角 `念 (sati)` 和全角 `念（sati）`。

### 1.3 人名、地名、称号
- 人名沿用既定传统汉译或音译（不按泰语读音）；既有必要首注以章/文件为基本单位，可作`舍利弗（Sāriputta）`。常见人名本来未注处不机械补注；独立定义/附注/脚注/表格/书目及拼写辨析可复注，普通连续行文的无辨义复注可删（notation04澄清）。
- **敬称放在名字前面**（同样适用于泰国和西方僧人：`尊者阿姜查雅萨罗`、`尊者帕·巴育陀`）：`尊者舍利弗`、`尊者阿难`、`尊者摩诃目犍连`。不写“舍利弗尊者”“阿难尊者”（现有 37 处左右）。“长老”同理：`长老 X`。
- **尊者名字一律译成中文（G4）**：巴利三藏中的人名（如 Ānanda、Anuruddha、Aṅgulimāla、Puṇṇa、Soṇa、Mahaka、Koṇḍadhāna、Piṇḍola）一律译出，不在正文里留拉丁原文，书中已有的译名照用（阿难、阿那律、鸯掘摩罗、富楼那、摩诃迦、宾头卢·颇罗堕、给孤独长者、婆迦梵天……），没有的采用汉译阿含或南传通行译名或音译（索那、军头波汉、尸利曼陀、瓦吉拉……）；敬称在前。按 1.3 首条，每章首次出现时可括注巴利原名。
- **后期论师与现代僧人（G4）**：义注时代人物（觉音、摩诃那伽长老等）以及泰国、缅甸、斯里兰卡、西方的现代僧人，译成或音译成中文，**在每个章节文件中第一次出现时**用全角括号附原名，之后只用中文。采用“按文件”而不是“按全书”，因为各章是分开阅读的。格式：`尊者那拉达（U Narada）`、`菩提比丘（Bhikkhu Bodhi）`、`髻智比丘（Bhikkhu Ñāṇamoli）`、`长老向智（Nyanaponika Thera）`、`帕·拉差瓦拉牟尼（Phra Rajavaramuni）`。书中已有的译名保留（阿姜查雅萨罗、帕·巴育陀、颂德·帕·菩陀构萨迦利雅、佛使比丘等）。“X比丘”是西方和泰国僧人的通行称法，保留在名字后面。括注里不加英文敬称（Ven.）。处于括注之内时，原名改用六角括号〔 〕，避免括号嵌套。在家人（学者、译者）的姓名属于书目信息，保留原文。作者讨论拼写本身的译注（如“作者使用拼写 Moggallīputta-Tissa Thera”）保留原文。
- **只有“阿姜”后面不加间隔号**：`阿姜查`、`阿姜查雅萨罗`。其他泰国僧衔或称号**保留原有间隔号**：`颂德·帕·菩陀构萨迦利雅`、`帕·巴育陀`、`隆波·查`。拿不准时保留原文写法。**（G5）“帕”“颂德”“隆波”作僧衔时后面一律有间隔号**，含连用的僧衔：`颂德·帕菩陀构萨迦利雅` ✗ → `颂德·帕·菩陀构萨迦利雅` ✓；`颂德·帕瓦纳拉特` ✗ → `颂德·帕·瓦纳拉特` ✓；`颂德·帕摩诃萨摩纳…` ✗ → `颂德·帕·摩诃萨摩纳…` ✓；`帕古·美提达玛沙恩` → `帕·古·美提达玛沙恩`（Phra Kru）。不属于僧衔的“帕”不加点：寺名（`帕那那查寺` Wat Pah Nanachat、`帕披仁寺`）、巴利词或人名音译中的“帕”（`帕拉玛萨` parāmāsa、`罗陀帕拉`、`迦库帕拉`）、爵衔整词“帕耶”（Phraya，`昭·功·帕耶`）。
- **巴利三藏人名、地名、天神名一律在正文中译出（G5）**：不只是“尊者X”，凡在中文行文中单独出现的经典人物、地名、天神、外道名（如 Vacchagotta、Māra、Sakka、Brahmā、Mettagū、Uruvelā、Cunda、Pāṭikaputta）都要译出；只有括注、出处（`MN 72 / M i 486-9`）和英文经名出处（`Vacchagotta Sutta`）里保留原文。不机械新增巴利括注；已有必要首注以章/文件为基本单位，普通连续行文的无辨义复注可删；独立附注/脚注、定义词目、表格、书目和拼写辨析可保留所需复注（notation04澄清）。G5 定名：Vacchagotta=**婆蹉衢多**（取代 G4 的“瓦恰葛达”；Aggivacchagotta Sutta=《婆蹉衢多火喻经》）、Mettagū=梅达古、Uruvelā=优楼频螺、Senānigama=斯那尼村、Cunda=纯陀、Pāṭikaputta=波梨子、Nandopananda=难陀优波难陀、Vajjiyamāhita=伐耆耶摩希达、Āḷāra Kālāma=阿罗罗·迦罗摩、Acela Kassapa=裸行者迦叶、Subhadda=须跋陀、Acela Seniya=裸行者塞尼耶、Māgaṇḍiya（游方者，MN 75）=摩犍提、Sedaka Sutta=《私达迦经》。
- 外国人的全名（非佛教称号）照常用间隔号：`阿尔伯特·爱因斯坦`。
- 统一用字：阿难（不用阿难陀/阿难达）、摩诃目犍连（不用大目犍连/目犍连单用）、给孤独长者、毗舍佉（不用维沙卡）、帝释天、魔罗（不用摩罗）、梵天、乔达摩（Gotama，属人名，保留）。
- **辟支佛一律改为“独觉佛”**（现有 15 处）。

### 1.4 经名、书名、引文出处
- 经名、论名加书名号：`《清净道论》`、`《法句经》`、`《卡拉玛经》`（不用“迦摩罗经”）、`《弥兰王问经》`。
- 部名之间用间隔号：`《增支部·三集》`、`《相应部·因缘品》`。
- 英文缩写的出处（如 `S. II. 28`）原样保留，不翻译。
- **（v6旧条，已由后期quotation/numbering及notation04规则取代）**：独立出处沿用当前已审定的VRI/PTS编号、卷页、巴利经名及AIPali链接，不补回普通出处的中文经名，也不按EN旧号重写现有源标；注释书/复注的内部章节原名按来源保留。正文书名规则不强加给出处。已批准的实质说明例外保留；任何数字、URL、ID及链接语法均冻结。
- 注释书、复注的章节名（如 `CompṬ.: Pakiṇṇakaparicchedavaṇṇanā`、`VismṬ.: …`、`Miln.: …`）按英文保留巴利原名，不译成中文。
- “Pali Canon”统一译作**巴利三藏**（专名“巴利圣典协会”Pali Text Society/PTS 保留不改）（现有“巴利圣典”210 处、“巴利经典”35 处，全部改掉）；Abhidhamma Piṭaka 译作“论藏”，Vinaya Piṭaka 译作“律藏”，Sutta Piṭaka 译作“经藏”。

### 1.5 标点与格式
- 一律用全角中文标点；引号嵌套用 “ ‘ ’ ”。
- 括号内再有括注（原名、巴利语、编号等）时，内层用六角括号〔〕，不写成（……（……）……）〔R3-r2〕；英文原书名本身带的半角括号保留。
- 原文的 `{{id_xxx}}`、`{123}`、脚注 `[\[1\]](#fn-fn1){:id="fr-fn1"}` 以及图片、Markdown 结构都**原样保留**，不改行、不并行。
- 中文与拉丁字母（英文、巴利文转写）之间加一个半角空格，两侧都加，如“有 attā 和 nirattā”“dukkha 一词”；紧邻全角标点或全角括号时不加，如“（attā）”；出处标识、链接目标、front matter、脚注标记语法内部不动。中文与阿拉伯数字 0–9 相邻时加一个 ASCII 空格，如“第 3 章”“2021 年”“M ii 174 中”。这是本书依 pt96u 采用的排版约定，不宣称是所有中文书的强制规范；本轮取代 G3 旧“数字不加空格”款。连续小数、千分组及范围不拆开。
- **（v6）不使用全角斜杠“／”**，一律用半角“/”（如 kamma/karma）。
- **（v6旧条，已由后续统一规则取代）**：旧版曾要求“译注：”；现行脚注及夹注标签一律为“译者注：”，对应英文的 “Trans.:”。需要交代中文/英文译者身份时写在注释正文中，不另造标签。
- （v6）脚注编号与英文版一一对应：标记、定义、英文脚注三者数量相等，按出现顺序从 1 连续编号；脚注定义只能有一段，不能在 `{: id="fn-fnN"}` 后面再接续文字。英文版的“Note”方框按“标题行 + 引用块（>）”的格式放在正文相应位置，不放进脚注。
- 删去残留字符 `↩`（nav.md）及非源标的编辑式“#n”编排；不删改冻结的原典卷章标识。

### 1.6 用语风格
- 用现代汉语白话、南传上座部通行用语；不用汉传特有的术语（但“三法印”按用户决定保留，见第三部分）。
- 避免带一神教色彩的词：恶（不用“罪”），信心（不用“信仰”，指其他宗教时除外）；God 译作“上帝”，deva 译作“天人”。
- “Dhamma”**从不**译作“达摩”。经核查，目前的“达摩”只出现在“阿毗达摩”“乔达摩”“苏达摩”中，属于正确用法；修订时要防止新出错。
- practical application 按所指用“实际运用”“落实于修行／实践”等；不硬译成“修行福祉方面的实践应用”，也不一律缩成“实修”。本批只落实已审语境，不扩展为全文替换。

---
## 二、定稿目录对照表

“现译”指中文仓库现在的标题；“定稿”是修订后应采用的标题；“说明”列：保留＝不改，修改＝需要改。h1＝页面主标题，h2–h4＝小标题。共 643 条，其中修改 128 条。


### titlepage

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Buddhadhamma | 佛法 中文版 | 佛法：自然法则及其对生命的利益 | **修改** |
| h2 | The Laws of Nature and Their Benefits to Life | （中文缺/未对齐） | 自然法则及其对生命的利益 | **修改** |
| h2 | Downloads | （中文缺/未对齐） | 下载 | **修改** |
| h3 | Buddhadhamma | （中文缺/未对齐） | 佛法 | **修改** |
| h2 | Order Hard Copies | （中文缺/未对齐） | 订购纸质版 | **修改** |
| h3 | Buddhadhamma, Section 1-7. | （中文缺/未对齐） | 佛法 | **修改** |

### anumodana

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Anumodanā | 随喜 | 随喜 | 保留 |

### abbreviations

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Abbreviations | 缩写 | 缩写 | 保留 |

### foreword-by-ajahn-jayasaro

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Foreword by Ven. Ajahn Jayasaro | 阿姜·查雅萨罗前言 | 尊者阿姜查雅萨罗前言 | **修改** |

### foreword-by-khun-yongyuth

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Foreword by the President of the Buddhadhamma Foundation | 佛法基金会主席前言 | 佛法基金会主席前言 | 保留 |

### foreword-by-translator

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Foreword by the Translator | （中文缺/未对齐） | 译者前言 | **修改** |

### introduction

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Introduction | 导论 | 导论 | 保留 |
| h2 | Primary Attributes of Buddha-Dhamma | 佛法的主要特征 | 佛法的主要特征 | 保留 |

### middle-teaching

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Part 1: Middle Teaching | 第一部：中道法义 | 第一部：中道法义 | 保留 |

### nature-of-human-life

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Section 1: Nature of Human Life | 第一篇：生命是什么？ | 第一篇：生命是什么？ | 保留 |

### five-aggregates

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Five Aggregates | （中文缺/未对齐） | 第一章：五蕴 | **修改** |
| h2 | Introduction | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h2 | Saññā and Sati: Memory, Recollection, and Mindfulness | （中文缺/未对齐） | “想”与“念”：记忆、辨识与忆持 | **本阶段修改**（m-review-reader-01） |
| h2 | Perception, Consciousness, and Wisdom | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h2 | Relationship between the Aggregates | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h2 | Human Life Entails the Functioning of the Five Aggregates | （中文缺/未对齐） | 人的生命即五蕴的运作 | **修改** |
| h3 | All Phenomena – Mind and Matter – Are Exclusively Made Up of the Five Aggregates | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | The Functioning of the Five Aggregates Constitutes Life | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | Vying for Happiness Leads to Increased Suffering for All | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | A Life Grounded in Wisdom Renders a Pursuit of Happiness Unnecessary | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | Nota Bene | （中文缺/未对齐） | 附注 | **修改** |
| h2 | The Five Aggregates and Clinging to the Five Aggregates | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h2 | Practical Application | （中文缺/未对齐） | 实践应用 | **修改** |
| h2 | Appendix 1: Additional Details in Regard to the Five Aggregates | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | Rūpa: body; physical form; materiality | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | Vedanā: feeling; sensation | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | Saññā: perception | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | Saṅkhāra: volitional formations | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h3 | Viññāṇa: consciousness | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |
| h2 | Appendix 2: Commentarial Explanation of Perception | （中文缺/未对齐） | （中文缺/未对齐） | 保留 |

### six-sense-spheres

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Six Sense Spheres | 第二章：六处 | 第二章：六处 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Nature of the Six Senses | 六处的性质 | 六处的性质 | 保留 |
| h3 | Nota Bene | 注意 | 附注 | **修改** |
| h2 | Buddhist Epistemology | 佛教的知见理论 | 佛法中的各种“知” | **本阶段修改**（m-review-reader-01） |
| h3 | Types of Knowledge | 知的种类 | 知的种类 | 保留 |
| h3 | Pathways of Cognition | 觉知的根门 | 认知的途径 | **修改** |
| h3 | Wisdom Development | 开发智慧 | 培育智慧 | **本阶段修改**（m-review-reader-01） |
| h3 | Human Activities and Accomplishments | 人类的意识活动与成就 | 人类的活动与成就 | **修改** |
| h2 | Accurate and Defective Knowledge | 正确的知见与错谬的知见 | 正确的知见与错谬的知见 | 保留 |
| h3 | Two Levels of Truth | 两种层次的真理 | 两种层次的真理 | 保留 |
| h3 | Three Aberrations of Knowledge | 三种颠倒知见 | 三种颠倒知见 | 保留 |
| h2 | The Buddha’s Words on the Sense Spheres | 佛陀关于六处的开示 | 佛陀关于六处的开示 | 保留 |
| h2 | Practical Application | 修行实践 | 实践应用 | 保留 |
| h2 | Appendix 1: Three Kinds of Wisdom | 附录一：三种智慧 | 附录一：三种智慧 | 保留 |
| h2 | Appendix 2: Commentarial Analysis of the Sense Spheres | 附录二：对六处的义注分析 | 附录二：对六处的义注分析 | 保留 |
| h2 | Appendix 3: The Six Sense Spheres and the Five Aggregates | 附录三：六处与五蕴 | 附录三：六处与五蕴 | 保留 |

### attributes-of-life

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Section 2: Attributes of Life | 第二篇：生命是怎样的？ | 第二篇：生命是怎样的？ | 保留 |

### three-characteristics

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Three Characteristics | 第三章：三法印 | 第三章：三法印 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Understanding the Terms Dhamma and Saṅkhāra | 理解“法”（Dhamma）和“行”（Saṅkhāra）这两个术语 | 理解“法”和“行”这两个术语 | **修改** |
| h3 | ’All Things’ and ’All Formations’ | “一切法”和“一切有为法” | “一切法”和“一切有为法” | 保留 |
| h3 | Saṅkhāra of the Five Aggregates and Saṅkhāra of the Three Characteristics | 五蕴之“行”与三法印之“行” | 五蕴之“行”与三法印之“行” | 保留 |
| h2 | Scriptural Definitions | 经论定义 | 经论定义 | 保留 |
| h3 | Impermanence | 无常 | 无常 | 保留 |
| h3 | Dukkha | 苦 | 苦 | 保留 |
| h4 | Introduction | 导论 | 导论 | 保留 |
| h4 | Dukkha in the Three Characteristics and Dukkha in the Four Noble Truths | 三法印中的苦与四圣谛中的苦 | 三法印中的苦与四圣谛中的苦 | 保留 |
| h3 | Nonself | 无我 | 无我 | 保留 |
| h4 | Scope | 范围 | 范围 | 保留 |
| h4 | Basic Definition | 基本定义 | 基本定义 | 保留 |
| h4 | Implied Definition | 隐含定义 | 无需另作阐释的含义 | **本阶段修改**（m-review-reader-01） |
| h4 | Scriptural Explanation | 经文解释 | 经文解释 | 保留 |
| h3 | Summary | 总结 | 总结 | 保留 |
| h2 | Concealers of the Three Characteristics | 遮蔽三法印之法 | 遮蔽三法印之法 | 保留 |
| h2 | Nonself and No-Self | “无我”与“非我” | “无我”与“非我” | 保留 |
| h2 | Ego and Conceit | “自我”与“我慢” | “自我”与“我慢” | 保留 |
| h2 | Practical Value | 实修价值 | 实践价值 | **本阶段修改**（m-review-reader-01） |
| h3 | The Spiritual Practice Leading to Liberation | 导向解脱的修行 | 导向解脱的修行 | 保留 |
| h3 | The Practice of Heedfulness | 不放逸的修行 | 不放逸的修行 | 保留 |
| h3 | Correlation Between the Practice of Liberation and the Practice of Heedfulness | 导向解脱的修行与不放逸的修行之间的关联 | 导向解脱的修行与不放逸的修行之间的关联 | 保留 |
| h3 | The Value of Liberation | 解脱的利益 | 解脱的利益 | 保留 |
| h2 | Practical Benefits of the Individual Characteristics | 单一法印的实际利益 | 各法印的实践价值 | **本阶段修改**（m-review-reader-01） |
| h3 | Impermanence | 无常 | 无常 | 保留 |
| h3 | Dukkha | 苦 | 苦 | 保留 |
| h3 | Anattā | 无我 | 无我 | 保留 |
| h2 | Buddha’s Words on the Three Characteristics | 佛陀关于三法印的教言 | 佛陀关于三法印的开示 | **修改** |
| h3 | Direct Knowledge of the Three Characteristics | 彻见三法印 | 彻见三法印 | 保留 |
| h3 | Practical Benefits of the Three Characteristics | 三法印的实修利益 | 三法印的实修利益 | 保留 |
| h4 | The Ephemeral Nature of Life and the Value of Time | 生命的短暂性和时间的价值 | 生命的短暂性和时间的价值 | 保留 |
| h4 | Developing a Sense of Urgency and Preparing for the Future | 培养紧迫感并为未来做准备 | 培养紧迫感并为未来做准备 | 保留 |
| h2 | Appendix 1: Abhidhamma Classification of Natural Laws | 附录一：阿毗达摩对自然法则的分类 | 附录一：阿毗达摩对自然法则的分类 | 保留 |
| h2 | Appendix 2: Commentarial Explanation of Designations (Paññatti) | 附录二：义注对概念（Paññatti）的解释 | 附录二：义注对概念的解释 | **修改**（G3：改回“概念”） |
| h2 | Appendix 3: Various Forms of Suffering | 附录三：各种形式的苦 | 附录三：各种形式的苦 | 保留 |
| h2 | Appendix 4: God | 附录四：神 | 附录四：上帝 | **修改** |

### process-of-life

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Part 2: Process of Life | 第三篇：生命如何运作？ | 第三篇：生命如何运作？ | 保留 |

### dependent-origination

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Dependent Origination | 第四章：缘起 | 第四章：缘起 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h3 | General Presentation | 总说 | 总说 | 保留 |
| h3 | Detailed (or ’Applied’) Presentation | 详说 | 详说 | 保留 |
| h2 | Significance of Dependent Origination | 缘起的意义 | 缘起的意义 | 保留 |
| h2 | Interpretations of Dependent Origination | 缘起的诠释 | 缘起的诠释 | 保留 |
| h2 | Relational Context of Dependent Origination | 缘起的关联脉络 | 缘起的关联脉络 | 保留 |
| h2 | Orthodox Explanation | 传统解释 | 传统解释 | 保留 |
| h3 | Factors of Dependent Origination | 缘起支 | 缘起支 | 保留 |
| h3 | Definitions | 定义 | 定义 | 保留 |
| h3 | General Explanations | 一般性解释 | 一般性解释 | 保留 |
| h2 | Application in Everyday Life | 在日常生活中的应用 | 在日常生活中的应用 | 保留 |
| h3 | Factors of Dependent Origination | 缘起支 | 缘起支 | 保留 |
| h3 | Preliminary Explanation of the Relationship between Factors | 各缘起支之间关系的初步解释 | 各缘起支之间关系的初步解释 | 保留 |
| h3 | Expanded Explanation of the Relationship between Factors | 各缘起支之间关系的详细解释 | 各缘起支之间关系的详细解释 | 保留 |
| h3 | Examples from Everyday Life | 日常生活中的例子 | 日常生活中的例子 | 保留 |
| h3 | Deeper Explanations | 更深入的解释 | 更深入的解释 | 保留 |
| h2 | Dependent Origination and the Middle Teaching | 缘起与中道教法 | 缘起与中道教法 | 保留 |
| h3 | Duality #1 | 二元论 #1 | 二元论之一 | **修改** |
| h3 | Duality #2 | 二元论 #2 | 二元论之二 | **修改** |
| h3 | Duality #3 | 二元论 #3 | 二元论之三 | **修改** |
| h3 | Duality #4 | 二元论 #4 | 二元论之四 | **修改** |
| h2 | Dependent Origination in a Social Context | 社会背景下的缘起 | 社会背景下的缘起 | 保留 |
| h2 | The Link Between the Middle Teaching and the Middle Way | 中道教法与中道的联系 | 中道教法与中道的关系 | **本阶段修改**（m-review-reader-01） |
| h2 | Breaking the Cycle | 打破循环 | 打破循环 | 保留 |
| h3 | Nutriment of Ignorance | 无明的滋养 | 无明的滋养 | 保留 |
| h3 | Nutriment of Knowledge and Liberation | 明与解脱的滋养 | 明与解脱的滋养 | 保留 |
| h4 | The Fulfilment of the Holy Life (brahmacariya) | 梵行的圆满 (brahmacariya) | 梵行的圆满 | **修改** |
| h4 | Seven Kinds of Purity | 七清净 | 七清净 | 保留 |
| h4 | Fifteen Modes of Conduct and the Three Kinds of Knowledge | 十五行与三明 | 十五行与三明 | 保留 |
| h4 | Righteous Ways of Conduct (dhamma-cariyā) | 正行 (dhamma-cariyā) | 法行（B3 改定） | **修改** |
| h2 | Appendix 1: Interpretations of Dependent Origination | 附录一：缘起法的阐释 | 附录一：缘起的诠释 | **修改** |
| h2 | Appendix 2: Laws of Nature (dhamma-niyāmatā) | 附录二：自然法则 | 附录二：自然法则 | 保留 |
| h3 | These Natural Laws Comprise Four Factors Linked to the Four Noble Truths | 这些自然法则包含与四圣谛相关的四个要素 | 这些自然法则包含与四圣谛相关的四个要素 | 保留 |
| h3 | Suchness (tathatā) | 如是性（tathatā） | 如是性 | **修改** |
| h3 | Terms Pertaining to the Three Characteristics (tilakkhaṇa) | 关于三法印的术语 | 关于三法印的术语 | 保留 |
| h3 | Terms Pertaining to Specific Conditionality (idappaccayatā) | 关于此缘性（idappaccayatā）的术语 | 关于此缘性的术语 | **修改** |
| h3 | All-encompassing Principles of Truth | 包罗万象的真理原则 | 包罗万象的真理原则 | 保留 |
| h2 | Appendix 3: ’Me and Mine’ | 附录三：“我”与“我的” | 附录三：“我”与“我的” | 保留 |
| h2 | Appendix 4: Birth and Death in the Present Moment | 附录四：当下的生与死 | 附录四：当下的生与死 | 保留 |
| h2 | Appendix 5: Abhidhamma Interpretation of Dependent Origination | 附录五：阿毗达摩对缘起的解释 | 附录五：阿毗达摩对缘起的解释 | 保留 |
| h3 | Twelve Unwholesome States of Mind (akusala-citta) | 不善心 | 十二不善心（B3 改定） | **修改** |
| h3 | Wholesome States of Mind | 善心 | 善心 | 保留 |
| h3 | Kamma-Resultant States of Mind and Functional States of Mind | 异熟心与唯作心 | 异熟心与唯作心 | 保留 |
| h3 | Transcendent States of Mind | 出世间心 | 出世间心 | 保留 |
| h2 | Appendix 6: Nirodha (’Cessation’) | 附录六：止息 (Nirodha) | 附录六：寂灭 | **修改** |
| h2 | Appendix 7: Concise Definitions for the Factors of Dependent Origination | 附录七：缘起支的简明定义 | 附录七：缘起支的简明定义 | 保留 |
| h2 | Appendix 8: Bhava-taṇhā and Vibhava-taṇhā | 附录八：有爱与无有爱 | 附录八：有爱与无有爱 | 保留 |
| h2 | Appendix 9: Detailed Description of Consciousness | 附录九：心识的详细描述 | 附录九：心识的详细描述 | 保留 |
| h2 | Appendix 10: Metaphysical Dilemmas | 附录十：形而上学的难题 | 附录十：形而上学的难题 | 保留 |

### law-of-kamma

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | The Law of Kamma | 第五章：业的法则 | 第五章：业的法则 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Basic Understanding of Kamma | 对业的基本理解 | 对业的基本理解 | 保留 |
| h3 | Kamma as a Law of Nature | 业作为自然法则 | 业作为自然法则 | 保留 |
| h3 | Definition of Kamma | 业的定义 | 业的定义 | 保留 |
| h3 | Kinds of Kamma | 业的种类 | 业的种类 | 保留 |
| h2 | Criteria for Good and Evil | 善恶的标准 | 善恶的标准 | 保留 |
| h3 | Good and Evil | 善与恶 | 善与恶 | 保留 |
| h3 | The Wholesome and the Unwholesome | 善与不善 | 善与不善 | 保留 |
| h3 | Special Points on Wholesomeness and Unwholesomeness | 关于善与不善的特别须知 | 关于善与不善的特别须知 | 保留 |
| h4 | The Wholesome and the Unwholesome Can Be Interconnected | 善与不善可相互关联 | 善与不善可相互关联 | 保留 |
| h4 | Good and Evil, and the Wholesome and the Unwholesome | 善与恶，以及善法与不善法 | 善与恶，以及善法与不善法 | 保留 |
| h3 | Criteria for Good and Bad Action | 善恶行为的准则 | 善恶行为的准则 | 保留 |
| h3 | Formal Criteria for Evaluation | 正式评估标准 | 形式上的评判标准 | **修改** |
| h2 | Fruition of Kamma | 业果 | 业果 | 保留 |
| h3 | Levels of Fruition | 果报的层次 | 果报的层次 | 保留 |
| h3 | Factors Promoting and Obstructing the Fruition of Kamma | 促进和阻碍业果成熟的因素 | 促进和阻碍业果成熟的因素 | 保留 |
| h4 | Pair #1 | 第一对 | 第一对 | 保留 |
| h4 | Pair #2 | 第二对 | 第二对 | 保留 |
| h4 | Pair #3 | 第三对 | 第三对 | 保留 |
| h4 | Pair #4 | 第四对 | 第四对 | 保留 |
| h3 | Longterm Effects of Kamma | 业的长期影响 | 业的长期影响 | 保留 |
| h3 | Rebirth | 再生 | 再生 | 保留 |
| h3 | Proper Relationship to the Next Life | 与来世的正确关系 | 与来世的正确关系 | 保留 |
| h3 | Fruits of Kamma According to the Cūḷakammavibhaṅga Sutta | 依《小业分别经》所说之业果 | 依《小业分别经》所说之业果 | 保留 |
| h2 | Additional Matters Pertaining to Kamma | 与业相关的其他事项 | 与业相关的其他事项 | 保留 |
| h3 | What is the Cause for Happiness and Suffering? | 苦与乐的因是什么？ | 苦与乐的因是什么？ | 保留 |
| h3 | Misinterpretations of Kamma | 对业的误解 | 对业的误解 | 保留 |
| h3 | Purifying Kamma | 净化业 | 净化业 | 保留 |
| h3 | Redeeming Kamma | 业的修正 | 业的补救 | **修改** |
| h3 | Kamma Leading to the End of Kamma | 导向业尽的业 | 导向业尽的业 | 保留 |
| h3 | Social or Collective Kamma | 社会业或共业 | 社会业或共业 | 保留 |
| h3 | Kamma in the Context of Conventional Laws | 世间法背景下的业 | 世俗规约中的业 | **本阶段修改**（m-review-reader-01） |
| h3 | Does the Law of Kamma Conflict with the Teaching on Nonself? | 业的法则与无我教义是否冲突？ | 业的法则与无我教义是否冲突？ | 保留 |
| h2 | Practical Value | 实修利益 | 实践价值 | **本阶段修改**（m-review-reader-01） |
| h3 | General Aspects of Kamma | 业的普适性 | 业的普适性 | 保留 |
| h3 | Kamma Grounded in Rational Belief | 基于理性信仰的业 | 基于理性信仰的业 | 保留 |
| h3 | Kamma as Active Engagement | 作为精进者的业 | 作为积极投入的业（B4 改定） | **修改** |
| h3 | Behaviour as the Benchmark for Gauging a Person’s Value | 行为是衡量个人价值的基准 | 行为是衡量个人价值的基准 | 保留 |
| h3 | Self-Reliance | 自依止 | 自依止 | 保留 |
| h3 | Exhortations for the Future | 对未来的劝诫 | 对未来的劝诫 | 保留 |
| h2 | Appendix: Twelve Kinds of Kamma | 附录：十二种业 | 附录：十二种业 | 保留 |
| h3 | Group no. 1 | 第一组 | 第一组 | 保留 |
| h3 | Group no. 2 | 第二组 | 第二组 | 保留 |
| h3 | Group no. 3 | 第三组 | 第三组 | 保留 |
| h3 | Group no. 4 | 第四组 | 第四组 | 保留 |
| h3 | Further Notes | 进一步说明 | 进一步说明 | 保留 |

### goal-of-life

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Part 3: Goal of Life | 第四篇：生命应成为怎样？ | 第四篇：生命应成为什么？ | **修改** |

### nibbana-supreme-peace

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Nibbāna | 第六章：涅槃：至上寂静 | 第六章：涅槃：至上寂静 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Cessation of Suffering | 苦的止息 | 苦的止息 | 保留 |
| h3 | Long Format | 详说 | 完整式 | **本阶段修改**（m-review-reader-01） |
| h3 | Short Format | 总说 | 简略式 | **本阶段修改**（m-review-reader-01） |
| h2 | State of Nibbāna | 涅槃的境界 | 涅槃的境界 | 保留 |
| h2 | Elements of Nibbāna | 涅槃的元素 | 涅槃界 | **修改** |
| h2 | Jhāna, Nirodha and Nibbāna | 禅那、寂灭和涅槃 | 禅那、寂灭与涅槃 | **修改** |
| h2 | Anattā and Nibbāna | 无我和涅槃 | 无我和涅槃 | 保留 |
| h2 | Value and Unique Attributes of Nibbāna | 涅槃的利益与特质 | 涅槃的利益与特质 | 保留 |
| h3 | Nibbāna is Attainable in this Lifetime | 涅槃此生可证 | 涅槃此生可证 | 保留 |
| h3 | Nibbāna Is Attainable By All | 涅槃一切皆可证得 | 涅槃一切皆可证得 | 保留 |
| h3 | Nibbāna Is the Highest Spiritual Attainment | 涅槃是最高的精神成就 | 涅槃是最高的精神成就 | 保留 |
| h2 | Common Misunderstandings about Nibbāna | 关于涅槃的常见误解 | 关于涅槃的常见误解 | 保留 |
| h3 | Attaching To Non-attachment | 执着于不执着 | 执着于不执着 | 保留 |
| h3 | Overestimation | 高估 | 增上慢 | **修改** |
| h3 | Happiness and Readiness for Happiness | 快乐与获得快乐的准备 | 安乐与获得安乐的准备 | R4-23：涅槃层面之乐→安乐 |
| h2 | Points of Controversy | 争议点 | 争议点 | 保留 |
| h3 | Nibbāna and the Self | 涅槃与自我 | 涅槃与自我 | 保留 |
| h3 | What Happens After an Arahant’s Death? | 阿罗汉般涅槃后会去哪里？ | 阿罗汉般涅槃后会去哪里？ | 保留 |
| h2 | Appendix 1: Sa-upādisesa and Anupādisesa | 附录一：有余依与无余依 | 附录一：有余依与无余依 | 保留 |
| h2 | Appendix 2: Diṭṭhadhammika and Samparāyika | 附录二：现世与后世 | 附录二：现世与来世 | **修改** |
| h2 | Appendix 3: Final Mind | 附录三：究竟心 | 附录三：最后心 | **修改** |
| h2 | Appendix 4: ’Attaining’ Nibbāna | 附录四：“证得”涅槃 | 附录四：“证得”涅槃 | 保留 |
| h2 | Appendix 5: Anupāda-parinibbāna | 附录五：无取般涅槃 | 附录五：无取般涅槃 | 保留 |

### awakened-beings

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Awakened Beings | 第七章：觉悟者 | 第七章：觉悟者 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Eight Noble Beings | 八种圣者 | 八种圣者 | 保留 |
| h2 | Attributes of an Arahant | 阿罗汉的特质 | 阿罗汉的特质 | 保留 |
| h3 | Physical Self-Mastery (bhāvita-kāya) | 身的修习圆满（bhāvita-kāya） | 身的修习圆满 | **修改** |
| h3 | Moral Self-Mastery (bhāvita-sīla) | 戒行的修习圆满（bhāvita-sīla） | 戒行的修习圆满 | **修改** |
| h3 | Mental Self-Mastery (bhāvita-citta) | 心的修习圆满（bhāvita-citta） | 心的修习圆满 | **修改** |
| h3 | Wisdom Self-Mastery (bhāvita-paññā) | 智慧的修习圆满（bhāvita-paññā） | 智慧的修习圆满 | **修改** |
| h2 | Additional Attributes of Arahants | 阿罗汉的其他特质 | 阿罗汉的其他特质 | 保留 |
| h3 | Outward Demeanour | 外在仪态 | 外在仪态 | 保留 |
| h3 | Happiness and Liberation | 安乐与解脱 | 安乐与解脱 | 保留 |
| h3 | Masters of the Heart, Rulers of Thought | 心的主宰者，意的主导者 | 心的主宰者，意的主导者 | 保留 |
| h3 | Loving All Creatures; Intimate with Death and Separation | 慈爱一切有情，坦然面对死亡与别离 | 慈爱一切有情，坦然面对死亡与别离 | 保留 |
| h2 | Seven Noble Beings | 七种圣者 | 七种圣者 | 保留 |
| h2 | Kinds of Arahants | 阿罗汉的种类 | 阿罗汉的种类 | 保留 |
| h2 | Distinctions between Different Levels of Noble Beings | 不同层次圣者的区别 | 不同层次圣者的区别 | 保留 |
| h3 | Trainees (sekha) and Arahants | 有学和无学 | 有学与阿罗汉 | **修改** |
| h3 | Those Practising for Stream-Entry and Stream-Enterers | 随法行者与须陀洹 | 须陀洹向与须陀洹 | **修改** |
| h3 | Stream-Enterers and Arahants | 须陀洹与阿罗汉 | 须陀洹与阿罗汉 | 保留 |
| h3 | Non-returners and Arahants | 阿那含与阿罗汉 | 阿那含与阿罗汉 | 保留 |
| h3 | Arahants Liberated by Wisdom and Arahants Liberated Both Ways | 慧解脱阿罗汉与俱解脱阿罗汉 | 慧解脱阿罗汉与俱解脱阿罗汉 | 保留 |
| h3 | The Buddha and Those Liberated by Wisdom | 佛陀与慧解脱者 | 佛陀与慧解脱者 | 保留 |
| h2 | Factors of Stream-Entry | 证得须陀洹的要素 | 证得须陀洹的要素 | 保留 |
| h3 | Active Qualities | 所具备的功德 | 所具备的功德 | 保留 |
| h3 | Abandoned Qualities | 已断除的烦恼 | 已断除的烦恼 | 保留 |
| h2 | Buddha’s Words on Stream-Enterers | 佛陀关于须陀洹的话语 | 佛陀关于须陀洹的开示 | **修改** |
| h3 | Epithets and Descriptions | 称号与描述 | 称号与描述 | 保留 |
| h3 | General Criteria | 一般准则 | 一般准则 | 保留 |
| h3 | Abandoned Qualities and Qualities of Fruition | 已断除的烦恼与证果的功德 | 已断除的烦恼与证果的功德 | 保留 |
| h3 | Attributes and Conduct before Attaining Stream-Entry | 证得须陀洹果前的特质与行为 | 证得须陀洹果前的特质与行为 | 保留 |
| h2 | Additional Points on the Attributes of Stream-Enterers | 关于入流者特性的补充要点 | 关于须陀洹特质的补充 | **修改** |
| h3 | Faith (saddhā) | 信心（saddhā） | 信心 | **修改** |
| h3 | Moral Conduct (sīla) | 戒行（sīla） | 戒行 | **修改** |
| h3 | Learning (suta) | 多闻（suta） | 多闻 | **修改** |
| h3 | Generosity (cāga) | 布施（cāga） | 布施 | **修改** |
| h3 | Wisdom (paññā) | 智慧（paññā） | 智慧 | **修改** |
| h2 | Appendix 1: Sīlabbata-parāmāsa | 附录一：戒禁取 | 附录一：戒禁取 | 保留 |
| h2 | Appendix 2: The Link Between the Fourfold Self-Mastery (bhāvita) and the Four Kinds of Development (bhāvanā) | 附录二：四种修习成就（bhāvita）与四种培育（bhāvanā）之间的联系 | 附录二：四种修习成就与四种修习的关联 | **修改** |
| h2 | Appendix 3: Learned Ones (sutavant), Noble Disciples (ariya-sāvaka), and Noble Dhamma (ariya-dhamma) | 附录三：多闻者（sutavant）、圣弟子（ariya-sāvaka）和圣法（ariya-dhamma） | 附录三：多闻者、圣弟子和圣法 | **修改** |
| h2 | Appendix 4: Incentives for Giving | 附录四：布施的动机 | 附录四：布施的动机 | 保留 |
| h2 | Appendix 5: Additional Scriptural Quotations | 附录五：额外的经文引述 | 附录五：额外的经文引述 | 保留 |
| h3 | Factors of Stream-entry – Abandoned Qualities | 入流支——已舍弃的特质 | 入流支——已断除的烦恼 | **修改** |
| h2 | Appendix 6: List of Foremost Disciples | 附录六：上首弟子名单 | 附录六：上首弟子名单 | 保留 |
| h2 | Appendix 7: Seven Noble Beings | 附录七：七圣者 | 附录七：七种圣者 | **修改** |

### calm-and-insight

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Calm and Insight | 第八章：止与观 | 第八章：止与观 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Liberation of Mind and Liberation by Wisdom | 心解脱与慧解脱 | 心解脱与慧解脱 | 保留 |
| h2 | Important Principles on the Realization of Nibbāna | 证悟涅槃的重要原则 | 证悟涅槃的重要原则 | 保留 |
| h3 | General Aspects of Realization | 证悟的一般方面 | 证悟的一般方面 | 保留 |
| h2 | Basic Principles of Tranquillity Meditation | 止禅的基本原则 | 修止的基本原则 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Outline #1 | 纲要 #1 | 纲要一 | **修改** |
| h3 | Outline #2 | 纲要 #2 | 纲要二 | **修改** |
| h2 | Basic Principles of Insight Practice | 毗婆舍那修行的基本原则 | 修观的基本原则 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Contemplations on the Five Aggregates | 对五蕴的观照 | 对五蕴的观照 | 保留 |
| h3 | Contemplations on the Sense Spheres | 对六处的观照 | 对六处的观照 | 保留 |
| h3 | General Inquiry | 一般审察 | 一般审察 | 保留 |
| h3 | All-Encompassing Contemplations | 全面观照 | 全面观照 | 保留 |
| h2 | Systematic Outlines of Meditation Practice | 禅修的系统纲要 | 禅修的系统纲要 | 保留 |
| h3 | Principles of Practice According to the Visuddhimagga | 根据《清净道论》的修习原则 | 根据《清净道论》的修习原则 | 保留 |
| h4 | Training in Higher Morality (adhisīla-sikkhā) | 增上戒学（adhisīla-sikkhā） | 增上戒学 | **修改** |
| h4 | Training in Higher Mind (adhicitta-sikkhā; concentration) | 增上心学（adhicitta-sikkhā；定） | 增上心学 | **修改** |
| h4 | Training in Higher Wisdom (adhipaññā-sikkhā) | 增上慧学（adhipaññā-sikkhā） | 增上慧学 | **修改** |
| h2 | Appendix 1: Jhāna | 附录一：禅那 | 附录一：禅那 | 保留 |
| h2 | Appendix 2: Is It Possible To Develop Insight or to Become Enlightened in Jhāna? | 附录二：能否在禅那中修观或证悟？ | 附录二：能否在禅那中修观或证悟？ | 保留 |
| h2 | Appendix 3: Is It Possible To Develop Insight While Dwelling In the Realm of Neither-Perception-Nor-Non-Perception? | 附录三：能否在非想非非想处定中修观？ | 附录三：能否在非想非非想处定中修观？ | 保留 |
| h2 | Appendix 4: The Mind-Moment at Realization of Path and Fruit | 附录四：证得道果时的心识刹那 | 附录四：证得道果时的心刹那 | **修改** |
| h2 | Appendix 5: Non-returners After Death | 附录五：不还者死后 | 附录五：阿那含死后 | **修改** |
| h2 | Appendix 6: Attainment of Cessation (nirodha-samāpatti) | 附录六：想受灭尽定 | 附录六：想受灭尽定 | 保留 |

### a-noble-life

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Section 5: A Noble Life | 第五篇：生命应如何存在？ | 第五篇：生命应如何度过？ | **修改** |

### the-supernatural-and-the-divine

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | The Supernatural and the Divine | 第九章：神通与天人 | 第九章：神通与天人 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Miracles and Psychic Powers | 神变与神通 | 神变与神通 | 保留 |
| h3 | Introduction | 导论 | 导论 | 保留 |
| h3 | Three Kinds of Miracles | 三种神变 | 三种神变 | 保留 |
| h3 | Psychic Powers Are Not Essential | 神通并非必要 | 神通并非必要 | 保留 |
| h3 | Noble Psychic Powers | 圣神通 | 圣神通 | 保留 |
| h3 | Dangers of Psychic Powers | 神通的危险 | 神通的危险 | 保留 |
| h3 | Proper Relationship to Psychic Powers | 与神通的正确关系 | 与神通的正确关系 | 保留 |
| h2 | Divine Beings | 天人 | 天人 | 保留 |
| h3 | Human Beings and Divine Beings | 人与天人 | 人与天人 | 保留 |
| h3 | Obsolete Form of Relating to the Divine | 与天人交往的过时方式 | 与天人交往的过时方式 | 保留 |
| h3 | Harmful Effects of Depending on Divine Beings | 依赖天人的有害影响 | 依赖天人的有害影响 | 保留 |
| h3 | Proper Relationship to the Divine | 与天人的正确关系 | 与天人的正确关系 | 保留 |
| h3 | Buddhist Relationship to the Divine | 佛教中的人天关系 | 佛教中的人天关系 | 保留 |
| h2 | Conclusion | 得出结论 | 结论 | **修改** |
| h3 | Three Stages of Development | 修行的三个阶段 | 修行的三个阶段 | 保留 |
| h3 | Stage of Freedom | 解脱的阶段 | 解脱的阶段 | 保留 |
| h3 | Proper Relationship to the Supernatural | 与神通的正确关系 | 与神通的正确关系 | 保留 |
| h3 | Unstinting Spiritual Development | 不懈的修行 | 不懈的修行 | 保留 |
| h2 | Appendix 1: Supernatural Phenomena Recorded in the Scriptures | 附录一：经典中记载的神通事迹 | 附录一：经典中记载的神通事迹 | 保留 |
| h2 | Appendix 2: Assistance and Provocation by Indra | 附录二：帝释天的协助与扰乱 | 附录二：帝释天的协助与扰乱 | 保留 |
| h2 | Appendix 3: Asseverations of Truth: a Viable Solution for People Dependent on Supernatural Powers | 附录三：谛语——为依赖神通者提供的一种可行方案 | 附录三：谛语——为依赖神通者提供的一种可行方案 | 保留 |
| h2 | Appendix 4: Was the Buddha Human or Divine? | 附录四：佛陀是人还是天人？ | 附录四：佛陀是人还是天人？ | 保留 |
| h2 | Appendix 5: Divine Higher Knowledge and Vision | 附录五：关于天人的殊胜知见 | 附录五：天人的证智与知见 | **修改** |
| h2 | Appendix 6: Offerings to Devas | 附录六：对天人的供养 | 附录六：对天人的供养 | 保留 |

### the-buddhist-teachings-on-desire

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | The Buddhist Teachings on Desire | 第十章：佛陀关于欲望的教导 | 第十章：佛陀关于欲望的教导 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Mechanisms of Human Activity | 人类活动的机制 | 人类活动的机制 | 保留 |
| h2 | Contrasting Aspects of Craving and Wholesome Desire | 渴爱与善法欲的对比 | 渴爱与善法欲的对比 | 保留 |
| h3 | Non-action as a Form of Action | 不行动也是一种行动 | 不行动也是一种行动 | 保留 |
| h3 | Means and Ends: Craving as a Motivating Force | 手段与目的：渴爱作为一种驱动力 | 手段与目的：渴爱作为一种驱动力 | 保留 |
| h2 | Formal Basis for the Principles of Desire | 欲的原则的正式基础 | 欲求原则的教理依据 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Linguistic Analysis of the Term Chanda | “Chanda”一词的语言分析 | 欲（chanda）的语义分析 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Chanda as the Root of Suffering and Chanda as the Source of Wholesome Qualities | 欲是苦的根源，与欲是善法的来源 | 欲是苦的根源，与欲是善法的来源 | 保留 |
| h3 | Definitive Definition for Chanda | Chanda的明确定义 | “欲”的明确定义 | **修改** |
| h2 | Craving and Wholesome Desire | 渴爱与善法欲 | 渴爱与善法欲 | 保留 |
| h3 | Motivation of Craving | 渴爱的动机 | 渴爱的动机 | 保留 |
| h3 | Motivation of Wholesome Desire | 善法欲的动机 | 善法欲的动机 | 保留 |
| h3 | Comparative Analysis | 比较分析 | 比较分析 | 保留 |
| h3 | Problems Arising from a Set of Preconditions | 由一系列先决条件引发的问题 | 附加条件引发的问题 | **修改〔concepts02〕** |
| h3 | Benefits of Wholesome Desire | 善法欲的益处 | 善法欲的益处 | 保留 |
| h3 | The Act of Eating Subject to Preconditions | 受条件制约的饮食行为 | 受条件制约的饮食行为 | 保留 |
| h3 | Procreation and Sensual Pleasure | 生育与感官享乐 | 生育与感官享乐 | R4-r3：恢复原译（现代生活语境标题，避免“欲乐”生硬） |
| h3 | Eating in Moderation | 适度进食 | 适度进食 | 保留 |
| h2 | Complex Relationship between Craving and Chanda | 渴爱与善法欲的复杂关系 | 渴爱与善法欲的复杂关系 | 保留 |
| h3 | Interplay between Wholesome and Unwholesome Desires | 善法欲与不善欲的相互作用 | 善法欲与不善欲的相互作用 | 保留 |
| h3 | Relying on Wholesome Desire | 依靠善法欲 | 依靠善法欲 | 保留 |
| h3 | Seeking Gratification, Escaping the Unpleasant, and Protecting the Sense of Self | 寻求满足，逃避不悦，以及保护自我感 | 寻求满足，逃避不悦，以及保护自我感 | 保留 |
| h3 | Wholesome Desire and Lovingkindness | 善法欲与慈心 | 善法欲与慈心 | 保留 |
| h3 | Continued Harassment by Craving | 渴爱的持续干扰 | 渴爱的持续干扰 | 保留 |
| h3 | Review of Wholesome Desire | 善法欲回顾 | 善法欲回顾 | 保留 |
| h3 | Can Chanda Wish for Unwholesome Things? | “欲”（chanda）可以欲求不善之事吗？ | 善法欲会指向不善之事吗？ | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Interference and Intrusion by Craving | 渴爱的干扰与侵入 | 渴爱的干扰与侵入 | 保留 |
| h3 | Desire for Nibbāna | 对涅槃的欲求 | 对涅槃的欲求 | 保留 |
| h3 | Abandonment of Desire | 舍离欲求 | 舍离欲求 | 保留 |
| h3 | Abandoning Craving by Way of Craving | 以渴爱舍离渴爱 | 以渴爱舍离渴爱 | 保留 |
| h2 | Conclusion | 得出结论 | 结论 | **修改** |
| h3 | Increasing One’s Inner Radiance by Generating Wholesome Desire | 通过培育善法欲来增长内在的光明 | 通过培育善法欲来增长内在的光明 | 保留 |
| h3 | Wholesome Desire Must Be Accompanied by Wisdom | 善法欲必须伴随智慧 | 善法欲必须伴随智慧 | 保留 |
| h3 | Consummate Wholesome Desire | 圆满的善法欲 | 圆满的善法欲 | 保留 |
| h3 | Great Beings are Guided by Wisdom and Compassion | 觉悟者以智慧和悲心为导向 | 觉悟者以智慧和悲心为导向 | 保留 |
| h3 | Summary of Craving and Wholesome Desire | 渴爱与善法欲总结 | 渴爱与善法欲总结 | 保留 |
| h3 | Cultivating Desire | 培养对真相的热爱 | 培养对真相的热爱 | 保留 |
| h2 | Appendix 1: Three Kinds of Craving | 附录一：三种渴爱 | 附录一：三种渴爱 | 保留 |
| h2 | Appendix 2: Harm of Craving | 附录二：渴爱的危害 | 附录二：渴爱的危害 | 保留 |
| h2 | Appendix 3: The Buddha’s Main Attributes | 附录三：佛陀的主要德行特质 | 附录三：佛陀的主要德行特质 | 保留 |

### happiness

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Happiness | 第十一章：安乐 | 第十一章：乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h3 | Buddhism is a Path of Developing Happiness | 佛法是培育安乐之道 | 佛法是培育乐之道 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Happiness Is Reached by Happiness | 以安乐证得安乐 | 以乐证乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h2 | Formal Teachings on Happiness | 关于安乐的正式教导 | 关于乐的正式教导 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | What is Happiness? | 什么是安乐？ | 什么是乐？ | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | The Nature and Importance of Desire | 欲的本质和重要性 | 欲的本质和重要性 | 保留 |
| h3 | Delight and Happiness | 喜与乐 | 喜与乐 | 保留 |
| h3 | Dual Pathways to Happiness | 通往安乐的两条途径 | 通往乐的两条途径 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Wholesome Desire in Relation to Others | 对他人的善法欲 | 对他人的善法欲 | 保留 |
| h2 | Wise Enjoyment of Sense Pleasure | 智慧地受用感官之乐 | 智慧地受用感官之乐 | 保留 |
| h3 | Diverse Grades of Happiness | 不同层次的乐 | 不同层次的乐 | 保留 |
| h3 | Sense Pleasure and Superior Forms of Happiness | 欲乐与更高层次的安乐 | 欲乐与更高层次的乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Dangers and Drawbacks of Sense Pleasure | 欲乐的过患 | 欲乐的过患 | 保留 |
| h4 | The individual | 个体 | 个体 | 保留 |
| h4 | Kāma itself | 欲 (kāma) 本身 | 欲本身 | **修改** |
| h4 | Social behaviour | 社会行为 | 社会行为 | 保留 |
| h3 | Happiness from Scratching an Itch and Happiness from the Itch Being Cured | 抓痒的欲乐与痊愈的安乐 | 抓痒的欲乐与痊愈的安乐 | 保留 |
| h3 | Enjoyment of Sense Pleasures without Affliction | 无过失地受用欲乐 | 无过失地受用欲乐 | 保留 |
| h3 | Liberated Enjoyment of Sense Pleasure | 解脱地受用欲乐 | 解脱地受用欲乐 | 保留 |
| h3 | Comparison of Different Kinds of Happiness | 不同种类安乐之比较 | 各种乐的比较 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Freedom to Choose from Various Forms of Happiness | 自在地选择各种乐 | 自在地选择各种乐 | 保留 |
| h2 | Advantages and Disadvantages of Happiness | 安乐的功德与过患 | 乐味与过患 | **修改（T1-r3）** |
| h2 | Nature Provides Happiness | 大自然带来安乐 | 大自然带来安乐 | 保留 |
| h2 | Higher Forms of Happiness | 更高层次的安乐 | 更高层次的乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Timeless Happiness | 恒常的安乐 | 不受时间限制的乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Ideal Happiness | 理想的安乐 | 理想的乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Supreme Happiness of the Buddha | 佛陀的究竟安乐 | 佛陀的究竟安乐 | 保留 |
| h2 | Path to Supreme Happiness | 通往至上安乐之道 | 通往至上安乐之道 | 保留 |
| h3 | Developing More Refined Forms of Happiness | 培育更微细的安乐 | 培育更微细的乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Happiness Beyond Sensation | 超越想和受的安乐 | 超越感受之乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Perfect Happiness | 圆满的安乐 | 圆满的安乐 | 保留 |
| h2 | Review of Different Forms of Happiness | 不同形式的安乐回顾 | 不同形式的乐回顾 | **本轮语境审改〔m-review-concepts-01〕** |
| h2 | Happiness and Ethics | 安乐与戒行 | 乐与戒行 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Human Regulations and a System of Preconditions | 人为规范与预设条件系统 | 人为规范与附加条件机制 | **修改〔concepts02〕** |
| h3 | System of Preconditions in Harmony with Natural Laws | 与自然法则和谐的先决条件系统 | 与自然法则相协调的附加条件机制 | **修改〔concepts02〕** |
| h3 | Deriving the Greatest Benefit from Systems of Preconditions | 从先决条件系统中获取最大利益 | 善用附加条件机制 | **修改〔concepts02〕** |
| h3 | Fun in Learning, Happiness in Training | 学中之乐，修中之乐 | 学中之乐，修中之乐 | 保留 |
| h3 | Joy in Learning and Joy from Learning | 学习中的喜悦与学习后的喜悦 | 学习中的喜悦与学习后的喜悦 | 保留 |
| h3 | Despite the Glut of Consumable Objects, Happiness is on the Wane | 物质丰裕，安乐感何以式微？ | 物质丰裕，快乐何以式微？ | **本轮语境审改〔m-review-concepts-01〕** |
| h2 | Practical Application | 实际应用 | 实际运用 | **本阶段修改**（m-review-reader-01） |
| h3 | Summon Wisdom to Deal With Suffering | 以智慧处理苦 | 以智慧处理苦 | 保留 |
| h3 | Practice Being Free From Suffering | 离苦的修行 | 离苦的修行 | 保留 |
| h3 | Happiness in the Household | 家庭中的安乐 | 家庭中的安乐 | 保留 |
| h3 | Developing Sense Desire: from Competition to Cooperation | 培育感官之欲：从竞争到合作 | 培育感官之欲：从竞争到合作 | 保留 |
| h3 | Joy Leads to Spiritual Growth | 喜悦导向修行成长 | 喜悦导向修行成长 | 保留 |
| h3 | A Cultivated Mind Is Easily Content | 已修习的心易于知足 | 已修习的心易于知足 | 保留 |
| h3 | Happiness of Giving Leads to Peace in Society | 布施之乐带来社会祥和 | 布施之乐带来社会祥和 | 保留 |
| h3 | Sharing of Material Gains within the Monastic Community | 僧团内的利养分享 | 僧团内的利养分享 | 保留 |
| h3 | Goodness in People’s Hearts Actively Supports Society | 内心的善是社会的积极因素 | 内心的善是社会的积极因素 | 保留 |
| h3 | Mutual Assistance Benefits Everyone | 互助互利 | 互助互利 | 保留 |
| h3 | The Wise Learn from Suffering | 智者于苦中学习 | 智者于苦中学习 | 保留 |
| h2 | Conclusion | 结论 | 结论 | 保留 |
| h3 | Happiness Is Reached by Happiness | 以安乐证得安乐 | 以乐证乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Proper Attitude Towards Happiness | 对安乐的正确态度 | 对乐的正确态度 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Spiritual Practice in Relation to Happiness | 与安乐相关的修行 | 与乐相关的修行 | **本轮语境审改〔m-review-concepts-01〕** |
| h4 | Enjoyment of Sense Pleasure | 受用欲乐 | 受用欲乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h4 | Abandonment of Sense Pleasure | 舍离欲乐 | 舍离欲乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h3 | Perfect Happiness | 圆满的安乐 | 圆满的安乐 | 保留 |
| h3 | Acting for the Happiness of All | 为众生的安乐而行 | 为众生的安乐而行 | 保留 |
| h2 | Appendix 1: Paired Sets of Happiness | 附录一：成对的乐分类 | 附录一：成对的乐分类 | 保留 |
| h2 | Appendix 2: Threefold Happiness (alternative model) | 附录二：三种安乐（另一种模式） | 附录二：三种乐（另一种模式） | **本轮语境审改〔m-review-concepts-01〕** |
| h2 | Appendix 3: Threefold Happiness: Sense Pleasure, Divine Happiness, and the Happiness of the Destruction of Craving | 附录三：三种安乐：欲乐、天人之乐与爱尽之乐 | 附录三：三种乐：欲乐、天人之乐与爱尽之乐 | **本轮语境审改〔m-review-concepts-01〕** |
| h2 | Appendix 4: Temporary Ordination | 附录四：短期出家 | 附录四：短期出家 | 保留 |

### middle-way

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Part 2: Middle Way | 第二部：中道 | 第二部：中道 | 保留 |

### a-worthy-life

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Section 6: A Worthy Life | 第六篇：美好的生命是怎样的？ | 第六篇：美好的生命是怎样的？ | 保留 |

### introduction-to-the-middle-way

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Introduction to the Middle Way | 第十二章：中道导论 | 第十二章：中道导论 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h3 | The Path as the Middle Way | 作为中道的道 | 作为中道的道 | 保留 |
| h3 | The Path as a Practice and Way of Life for both Monks and Laypeople | 作为比丘和居士修行与生活方式的道 | 作为比丘和居士修行与生活方式的道 | 保留 |
| h3 | The Path as a Spiritual Practice Connected to Society | 作为与社会连接的修行之道 | 作为与社会连接的修行之道 | 保留 |
| h3 | The Path as a Way to End Kamma | 作为业止息的之道 | 作为止息业之道 | **修改** |
| h3 | The Path as a Practical Tool | 作为交通工具的道 | 作为实用工具的道 | **修改** |
| h3 | The Path as the Holy Life | 作为梵行的道 | 作为梵行的道 | 保留 |
| h4 | Virtuous conduct | 有德行的行为 | 有德行的行为 | 保留 |
| h4 | Brahmacariya | 梵行（Brahmacariya） | 梵行 | **修改** |
| h4 | Cariya-dhamma | Cariya-dhamma | 行法 | **修改** |
| h3 | The Path as a Way of Achieving Life Objectives | 作为实现人生目标的道 | 作为实现人生目标的道 | 保留 |
| h3 | The Path as the Threefold Training or as the Practice for Generating Noble Beings | 作为三学或通往圣者的道 | 作为三学或通往圣者的道 | 保留 |
| h2 | The Noble Path and the Threefold Training | 圣道与三学 | 圣道与三学 | 保留 |
| h3 | From the Eightfold Path to the Threefold Training | 从八正道到三学 | 从八正道到三学 | 保留 |
| h3 | Householders Cultivate the Path by Developing Meritorious Actions | 居士通过功德行来实践道 | 居士通过修习福业事来实践道 | **修改** |
| h3 | The Eightfold Path and a System of Training | 八正道与修习体系 | 八正道与修习体系 | 保留 |
| h3 | Beginning and End of the Path | 道之始末 | 道之始末 | 保留 |
| h2 | Appendix 1: Traditional Definitions of the Threefold Training | 附录一：三学之传统定义 | 附录一：三学之传统定义 | 保留 |
| h2 | Appendix 2: Two Extremes | 附录二：两种极端 | 附录二：两种极端 | 保留 |

### virtuous-friendship

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Virtuous Friendship | 第十三章：善友 | 第十三章：善友 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Way of Faith and Confidence | 信心之道 | 信心之道 | 保留 |
| h2 | Importance of Good Companionship | 善友的重要性 | 善友的重要性 | 保留 |
| h2 | Attributes of a Virtuous Friend | 善友的特质 | 善友的特质 | 保留 |
| h2 | Responsibility of a Virtuous Friend | 善友的职责 | 善友的职责 | 保留 |
| h2 | Appendix 1: Four Bases of Social Solidarity (saṅgaha-vatthu) | 附录一：四摄事（saṅgaha-vatthu） | 附录一：四摄事 | **修改** |
| h2 | Appendix 2: Commentarial Analysis of Right View (sammā-diṭṭhi) | 附录二：正见（sammā-diṭṭhi）的义注分析 | 附录二：正见的义注分析 | **修改** |

### faith-and-confidence

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Faith and Confidence | 第十四章：信心 | 第十四章：信心 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | The Buddha’s Words on Faith | 佛陀关于信心的开示 | 佛陀关于信心的开示 | 保留 |
| h2 | Preparation for the Middle Way | 中道的准备 | 中道的准备 | 保留 |
| h2 | The Triple Gem as a Conduit to the Middle Way | 三宝作为通向中道的基石 | 三宝作为通向中道的基石 | 保留 |
| h2 | Appendix 1: Translating Pali Terms from the Kālāma Sutta | 附录一：巴利语词汇《迦摩罗经》译法探讨 | 附录一：《卡拉玛经》中巴利词语的翻译 | **修改** |
| h2 | Appendix 2: Four Kinds of Faith | 附录二：四种信心 | 附录二：四种信心 | 保留 |

### wise-reflection

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Wise Reflection | 第十五章：如理作意 | 第十五章：如理作意 | 保留 |
| h2 | The Role of Reflection in a Wholesome Way of Life | 作意在贤善生活方式中的作用 | 如理作意与健全人生的重要性 | **修改** |
| h2 | The Role of Reflection in Spiritual Training and Wisdom Development | 作意在修行和培育智慧中的作用 | 作意在修行和培育智慧中的作用 | 保留 |
| h3 | Commencement of Training | 修行的开始 | 修行的开始 | 保留 |
| h3 | Process of Training | 修行的过程 | 修行的过程 | 保留 |
| h3 | Basic Elements of Spiritual Training | 修行的基本要素 | 修行的基本要素 | 保留 |
| h3 | Thinking Conducive to Spiritual Training | 有助于修行的思惟 | 有助于修行的思惟 | 保留 |
| h2 | Importance of Wise Reflection | 如理作意的重要性 | 如理作意的重要性 | 保留 |
| h2 | Definition of Wise Reflection | 如理作意的定义 | 如理作意的定义 | 保留 |
| h2 | Ways of Reflecting Wisely | 如理作意的方法 | 如理作意的方法 | 保留 |
| h3 | Investigation of Causes and Conditions | 考察因缘法 | 探究因缘的作意 | **修改** |
| h3 | Analysis of Component Factors | 分析构成要素法 | 分析构成要素的作意 | **修改** |
| h3 | Reflection in Line with Universal Characteristics | 彻见三法印法 | 依共相的作意 | **修改** |
| h3 | Reflection in Line with the Four Noble Truths | 与四圣谛相应的作意 | 与四圣谛相应的作意 | 保留 |
| h3 | Reflection on Goals and Principles | 目标与原则的作意 | 目标与原则的作意 | 保留 |
| h3 | Reflection on Advantages, Disadvantages, and the Escape | 优点、缺点和出离的作意 | 思惟乐味、过患与出离的作意 | **修改** |
| h3 | Reflection on the True and Counterfeit Value of Things | 思惟事物的真实价值与附加价值 | 思惟事物真实价值与虚假价值的作意 | **修改** |
| h3 | Reflection Rousing Wholesome Qualities | 激发善法的作意 | 激发善法的作意 | 保留 |
| h3 | Reflection by Abiding in the Present Moment | 安住于当下的作意 | 安住于当下的作意 | 保留 |
| h3 | Reflection Corresponding to Analytic Discussion (vibhajja-vāda) | 与分别说 (vibhajja-vāda) 相应的作意 | 与分别说相应的作意 | **修改** |
| h3 | Reflecting on Perspectives of Truth | 思惟实相的视角 | 思惟实相的视角 | 保留 |
| h3 | Reflecting on Component Factors | 思惟组成部分 | 思惟组成部分 | 保留 |
| h3 | Reflecting on the Sequence of Momentary Events | 思惟刹那相续的顺序 | 思惟刹那相续的顺序 | 保留 |
| h3 | Reflecting on the Interrelationship of Causes and Conditions | 思惟因缘之间的相互关系 | 思惟因缘之间的相互关系 | 保留 |
| h3 | Reflecting on Prerequisites and Qualifications | 思惟先决条件和限定条件 | 思惟先决条件和限定条件 | 保留 |
| h3 | Reflecting on Alternatives and Other Possibilities | 思惟替代方案和其他可能性 | 思惟替代方案和其他可能性 | 保留 |
| h3 | Detailed Analysis as a Response to Questions | 以分别说回答问题 | 以分别说回答问题 | 保留 |
| h2 | Practical Application | 实践应用 | 实际运用 | **本阶段修改**（m-review-reader-01） |
| h2 | Appendix 1: Reflection in Accord with the Four Noble Truths and Reflection Based on Science | 附录一：依四圣谛的如理作意与科学方法 | 附录一：依四圣谛的如理作意与科学方法 | 保留 |
| h2 | Appendix 2: Dhammānudhamma-paṭipatti | 附录二：法随法行（Dhammānudhamma-paṭipatti） | 附录二：法随法行 | **修改** |

### path-factors

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Section 7: Path Factors | 第七篇：道支 | 第七篇：道支 | 保留 |

### path-factors-of-wisdom

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Path Factors of Wisdom | 第十六章：智慧道支 | 第十六章：智慧道支 | 保留 |
| h2 | The Role of Reflection in a Wholesome Way of Life | 如理作意与健全人生的重要性 | 如理作意与健全人生的重要性 | 保留 |
| h2 | Right View (sammā-diṭṭhi) | 正见（sammā-diṭṭhi） | 正见 | **修改** |
| h3 | Importance of Right View | 正见的重要性 | 正见的重要性 | 保留 |
| h3 | Definitions of Right View | 正见的定义 | 正见的定义 | 保留 |
| h3 | General Points | 一般要点 | 一般要点 | 保留 |
| h3 | Right View in the Context of Spiritual Study | 修行背景下的正见 | 修行背景下的正见 | 保留 |
| h2 | Right Thought (sammā-saṅkappa) | 正思惟（sammā-saṅkappa） | 正思惟 | **修改** |
| h2 | Appendix: Relationship between Internal Qualities and External Actions | 附录：内在品质与外在行为的关系 | 附录：内在品质与外在行为的关系 | 保留 |

### path-factors-of-virtuous-conduct

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Path Factors of Virtuous Conduct | 第十七章：戒行道支 | 第十七章：戒行道支 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Path Factors of Virtuous Conduct | 戒行道支 | 戒行道支 | 保留 |
| h2 | Universal Principles of Morality | 戒行的普遍原则 | 戒行的普遍原则 | 保留 |
| h2 | Theistic Morality vs a Doctrine of Natural Truth | 有神论的戒行与自然实相的教法 | 有神论道德与自然真理之教 | **修改** |
| h2 | Basic Moral Conduct | 基本戒行 | 基本戒行 | 保留 |
| h2 | Fundamental Principles of Morality | 道德的基本原则 | 戒行的基本原则 | **修改** |
| h2 | Virtuous Conduct for Enhancing One’s Life and Society | 增进生命与社会的德行 | 增进生命与社会的德行 | 保留 |
| h3 | First Section: freedom from the fourteen vices | 第一节：免于十四种恶行 | 第一节：免于十四种恶行 | 保留 |
| h3 | Second Section: preparing two assets for one’s life | 第二节：为生命准备两项资产 | 第二节：为生命准备两项资产 | 保留 |
| h3 | Third Section: to protect the six directions | 第三节：保护六方 | 第三节：保护六方 | 保留 |
| h2 | General Principles on Right Livelihood | 正命的一般原则 | 正命的一般原则 | 保留 |
| h2 | Moral Rectitude and a Healthy Economy | 德行正直与健康经济 | 德行正直与健康经济 | 保留 |
| h3 | Introduction | 导论 | 导论 | 保留 |
| h3 | The Search for and Protection of Wealth | 财富的寻求与保护 | 财富的寻求与保护 | 保留 |
| h3 | Happiness for Laypeople | 居士的快乐 | 居士之乐 | R4-r2：gihi-sukha 四种乐统一 |
| h3 | Spending of Wealth | 财富的开销 | 财富的开销 | 保留 |
| h3 | Retaining Freedom When Acquiring Wealth | 获取财富时保持自由 | 获取财富时保持自由 | 保留 |
| h3 | Dual Freedom of the Sangha | 僧伽的双重自由 | 僧伽的双重自由 | 保留 |
| h3 | Summary | 总结 | 总结 | 保留 |
| h2 | Virtuous Conduct and Moral Codes | 戒行与行为规范 | 戒行与行为规范 | 保留 |
| h3 | Important Terms Pertaining to Morality: Sīla, Vinaya, and Sikkhāpada | 与戒行相关的术语：Sīla、Vinaya 和 Sikkhāpada | 与戒行相关的重要术语：戒、律与学处 | **修改** |
| h3 | Sīla on the Level of Dhamma and Sīla on the Level of Vinaya | 法层面的 sīla 与律层面的 sīla | 法层面的戒与律层面的戒 | **修改** |
| h2 | The Bhikkhu Code of Discipline and Its Relationship to Society | 比丘戒律及其与社会的关系 | 比丘戒律及其与社会的关系 | 保留 |
| h2 | Means for Extolling the Dhamma and Enhancing Communal Welfare | 赞扬佛法与增进僧团福利的途径 | 弘扬佛法与增进社群福祉的方法 | **修改** |
| h3 | Bowing and Paying Respects | 顶礼与恭敬 | 顶礼与恭敬 | 保留 |
| h3 | The Prescription Forbidding Monks from Claiming Superhuman States | 禁止比丘宣称超人境界的戒规 | 禁止比丘宣称超人境界的戒规 | 保留 |
| h3 | Offerings to the Monastic Community | 供养僧团 | 供养僧团 | 保留 |
| h2 | Concluding Remarks on the Monastic Discipline | 关于僧团戒律的总结 | 关于僧团戒律的总结 | 保留 |
| h2 | Definition of Vinaya Beyond the Scope of Moral Precepts | 律的定义超出了戒条的范畴 | 超越戒条范畴的律之定义 | **修改** |
| h2 | Appendix 1: Teaching the Dhamma and Laying Down the Vinaya | 附录一：宣说法与制定律 | 附录一：宣说法与制定律 | 保留 |
| h2 | Appendix 2: Sīla, Vinaya, and Sīla-dhamma | 附录二：戒、律与戒法 | 附录二：戒、律与戒法 | 保留 |
| h2 | Appendix 3: The Five Precepts and the Ten Wholesome Courses of Action | 附录三：五戒和十善业道 | 附录三：五戒和十善业道 | 保留 |
| h2 | Appendix 4: Classifying the Ten Ways of Righteous Conduct into the Three Trainings | 附录四：将十善业道归类为三学 | 附录四：将十种法行归入三学 | **修改** |
| h2 | Appendix 5: Ill-Effects Resulting from Transgression of the Five Precepts | 附录五：违犯五戒所产生的恶果 | 附录五：违犯五戒所产生的恶果 | 保留 |
| h2 | Appendix 6: Variant Meanings of ’Vinaya’ | 附录六：“律”的其他含义 | 附录六：“律”的其他含义 | 保留 |
| h2 | Appendix 7: Practice for the Welfare of the Manyfolk | 附录七：为多数人利益而修行 | 附录七：为多数人利益而修行 | 保留 |
| h2 | Appendix 8: Honouring the Dhamma, Honouring the Vinaya | 附录八：恭敬法，恭敬律 | 附录八：恭敬法，恭敬律 | 保留 |
| h2 | Appendix 9: Showing Respect According to Seniority | 附录九：依戒腊显示恭敬 | 附录九：依戒腊显示恭敬 | 保留 |
| h2 | Appendix 10: Is Buddhism a Pessimistic Religion? | 附录十：佛教是一种悲观的宗教吗？ | 附录十：佛教是一种悲观的宗教吗？ | 保留 |
| h2 | Appendix 11: Moral Precepts (sīla) and Religious Practices (vata) | 附录十一：戒律（sīla）与宗教实践（vata） | 附录十一：戒行与禁行 | **修改** |

### path-factors-of-concentration

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Path Factors of Concentration | 第十八章：禅定道支 | 第十八章：禅定道支 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Right Effort | 正精进 | 正精进 | 保留 |
| h2 | 3. Right Mindfulness | 正念 | 正念 | 保留 |
| h3 | Definition | 定义 | 定义 | 保留 |
| h3 | Mindfulness as Heedfulness | 作为“不放逸”的念 | 作为“不放逸”的念 | 保留 |
| h3 | Social Value of Mindfulness | “念”的社会价值 | “念”的社会价值 | 保留 |
| h3 | Mindfulness for Wisdom Development and the Removal of Mental Impurity | 用于开发智慧和消除内心杂染的“念” | 用于培育智慧和消除内心杂染的“念” | **本阶段修改**（m-review-reader-01） |
| h3 | Right Mindfulness in the Context of the Four Foundations of Mindfulness | 四念住语境下的正念 | 四念住语境下的正念 | 保留 |
| h3 | Gist of the Foundations of Mindfulness | 念住的要旨 | 念住的要旨 | 保留 |
| h3 | Four Foundations of Mindfulness: Way of Practice | 四念住：修习之道 | 四念住：修习之道 | 保留 |
| h3 | Fruits of Mindfulness Practice | 正念修习的成果 | 正念修习的成果 | 保留 |
| h3 | Momentary Awareness Is Essential for Insight Meditation | 对观禅而言，刹那的觉知至关重要 | 刹那的觉知对修观至关重要 | **修改〔m-review-concepts-01更新〕** |
| h3 | The Foundations of Mindfulness Nourish the Enlightenment Factors | 念住滋养觉支 | 念住滋养觉支 | 保留 |
| h2 | Right Concentration (sammā-samādhi) | 正定 | 正定 | 保留 |
| h3 | Definition of Samādhi | 定的定义 | 定的定义 | 保留 |
| h3 | Levels of Concentration | 禅定的层次 | 禅定的层次 | 保留 |
| h3 | Adversaries to Concentration | 禅定之敌 | 禅定之敌 | 保留 |
| h3 | Attributes of a Concentrated Mind | 专注之心的特质 | 专注之心的特质 | 保留 |
| h3 | General Objectives and Benefits of Concentration | 禅定的总体目标和益处 | 禅定的总体目标和益处 | 保留 |
| h3 | Aims and Benefits of Different Kinds of Concentrative Meditation | 不同种类禅定的目标和益处 | 不同种类禅定的目标和益处 | 保留 |
| h3 | Preventing Misunderstandings about the Aims and Benefits of Concentration | 防止对禅定目标和益处的误解 | 防止对禅定目标和益处的误解 | 保留 |
| h2 | The Highest Fruit of Concentration and the Spiritual Accomplishment Transcending Concentration | 禅定的最高果报与超越禅定的修行成就 | 禅定的最高果报与超越禅定的修行成就 | 保留 |
| h3 | Important Results and Limitations of Concentration | 禅定的重要成果与局限 | 禅定的重要成果与局限 | 保留 |
| h3 | Supporting Factors for Concentration | 禅定的辅助因素 | 禅定的辅助因素 | 保留 |
| h3 | The Basis, Proximate Cause, and Goal of Concentration | 禅定的基础、近因和目标 | 禅定的基础、近因和目标 | 保留 |
| h3 | Accompanying Factors of Concentration | 禅定的伴生因素 | 禅定的伴生因素 | 保留 |
| h3 | Criteria for Preparedness | 准备就绪的标准 | 准备就绪的标准 | 保留 |
| h3 | Wisdom’s Task Force | 智慧运作的“团队” | 智慧运作的“团队” | 保留 |
| h3 | Unity and Harmony of the Path Factors | 诸道支的和谐齐备 | 诸道支的和谐齐备 | 保留 |
| h2 | Ways of Developing Concentration | 培育定的方式 | 培育定的方式 | 保留 |
| h3 | Natural Development of Concentration | 定的自然培育 | 定的自然培育 | 保留 |
| h3 | Development of Concentration in Line with the Paths to Success | 依四神足培育禅定 | 依四神足培育禅定 | 保留 |
| h4 | Enthusiasm (chanda) | 欲（chanda） | 欲神足 | **concepts03：明确所释神足分支，正文保留基础因素词义** |
| h4 | Energy (viriya) | 精进 (viriya) | 精进神足 | **concepts03：明确所释神足分支，正文保留基础因素词义** |
| h4 | Focused attention (citta) | 专注 (citta) | 心神足 | **concepts03：明确所释神足分支，正文保留基础因素词义** |
| h4 | Investigation (vimaṁsā) | 审察 (vimaṁsā) | 审察神足 | **concepts03：明确所释神足分支，正文保留基础因素词义** |
| h3 | Standard Development of Concentration: Meditation Guided by Mindfulness | 定的标准修习：由正念引导的禅修 | 定的标准修习：由正念引导的禅修 | 保留 |
| h3 | Systematic Development of Concentration | 禅定的系统修习 | 禅定的系统修习 | 保留 |
| h3 | Eliminating the Ten Impediments | 消除十种障碍 | 消除十种障碍 | 保留 |
| h3 | Seeking a Virtuous Friend | 寻求善友 | 寻求善友 | 保留 |
| h3 | Receiving a Meditation Technique Suitable to One’s Disposition | 接受适合自己性情的业处 | 接受适合自己性情的业处 | 保留 |
| h3 | Finding a Fixed Abode | 寻找固定住所 | 寻找固定住所 | 保留 |
| h3 | General Practice of Meditation | 修习禅定的普遍原则 | 修习禅定的普遍原则 | 保留 |
| h3 | Mindfulness of Breathing As an Example of Meditation Practice | 安般念作为禅修实践的例子 | 安般念作为禅修实践的例子 | 保留 |
| h4 | Special Attributes of Mindfulness of Breathing | 安般念的特殊特质 | 安般念的特殊特质 | 保留 |
| h4 | Buddha’s Words Describing Mindfulness of Breathing | 佛陀描述安般念的话语 | 佛陀描述安般念的话语 | 保留 |
| h4 | Method of Practice in the Context of Tranquillity Meditation (Samatha) | 在奢摩他（samatha）背景下的修习方法 | 修止的方法 | **本轮语境审改〔m-review-concepts-01〕** |
| h2 | Appendix 1: Developing the Four Foundations of Mindfulness: a Life Free from Suffering | 附录一：培育四念住——离苦的生活 | 附录一：培育四念住——离苦的生活 | 保留 |
| h2 | Appendix 2: The Five Hindrances and the Seven Factors of Enlightenment | 附录二：五盖与七觉支 | 附录二：五盖与七觉支 | 保留 |

### four-noble-truths

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Four Noble Truths | 第十九章：四圣谛 | 第十九章：四圣谛 | 保留 |
| h2 | Introduction | 导论 | 导论 | 保留 |
| h2 | Role and Significance of the Four Noble Truths | 四圣谛的作用与意义 | 四圣谛的作用与意义 | 保留 |
| h2 | The Meaning of the Four Noble Truths | 四圣谛的含义 | 四圣谛的含义 | 保留 |
| h2 | The Four Noble Truths and Dependent Origination | 四圣谛与缘起 | 四圣谛与缘起 | 保留 |
| h2 | Actions to Be Performed in Relation to the Four Noble Truths | 关于四圣谛应履行的职责 | 关于四圣谛应履行的职责 | 保留 |
| h2 | Summary of the Four Noble Truths | 四圣谛总结 | 四圣谛总结 | 保留 |
| h3 | Dukkha | 苦：应遍知 | 苦：应遍知 | 保留 |
| h3 | Samudaya: the Source of Suffering | 苦集：苦的根源 | 集：苦的根源 | **修改** |
| h3 | Nirodha: the Cessation of Suffering | 灭：苦的止息 | 灭：苦的止息 | 保留 |
| h3 | Magga: the Path Leading to the Cessation of Suffering | 道：导向苦灭之道 | 道：导向苦灭之道 | 保留 |
| h3 | Path of the Noble Ones: Self-Mastery and Mutual Assistance | 圣者之道：自律与互助 | 圣者之道：自律与互助 | 保留 |
| h3 | Confidence in the Triple Gem Leads to the Threefold Training | 对三宝的信心导向三学 | 对三宝的信心导向三学 | 保留 |
| h2 | Buddhist Way of Solving Problems | 佛教解决问题的方式 | 佛教解决问题的方式 | 保留 |
| h3 | The constancy of human nature | 人性的恒常不变 | 人性的恒常不变 | 保留 |
| h3 | Prioritization and unique understanding | 优先次序和独特理解 | 优先次序和独特理解 | 保留 |
| h3 | Profundity, complexity, and true importance | 深奥性、复杂性和重要性 | 深奥性、复杂性和重要性 | 保留 |
| h3 | The interconnectedness of all facets of life | 生命各方面的相互关联 | 生命各方面的相互关联 | 保留 |
| h3 | Different levels of conducting one’s life | 不同层次的生活方式 | 不同层次的生活方式 | 保留 |
| h3 | The nature of all sentient beings | 一切有情众生的本质 | 一切有情众生的本质 | 保留 |
| h3 | Summary | 总结 | 总结 | 保留 |
| h2 | Outstanding Benefits of the Four Noble Truths | 四圣谛的卓越利益 | 四圣谛的殊胜利益 | **修改〔concepts02〕** |
| h2 | Distilling Buddhadhamma into The Four Noble Truths | 将佛陀教法精炼为四圣谛 | 将《佛法》浓缩为四圣谛 | m-review-language-02 M026：此处指本书 |
| h2 | Appendix 1: Observations on the Study of Buddha-Dhamma | 附录一：对佛法学习的观察 | 附录一：对佛法学习的观察 | 保留 |
| h3 | Middle Teaching (majjhena-dhammadesanā): the Dynamics of Nature | 中道法义：自然的运作机制 | 中道法义：自然的运作 | **修改** |
| h3 | Middle Path (majjhimā-paṭipadā): Methods for Practical Application | 中道：实际应用的方法 | 中道：实践方法 | **本阶段修改**（m-review-reader-01） |
| h2 | Appendix 2: Order of Chapters in the Thai Edition of Buddhadhamma | 附录二：泰文《佛法》扩展版的章节顺序 | 附录二：《佛法》泰文版的章节顺序 | **修改〔concepts03〕** |

### appendix-citta-vinnana-mano

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Special Appendix: Citta, Viññāṇa, Mano | 附录：心（Citta）、识（Viññāṇa）、意（Mano） | 附录：心（Citta）、识（Viññāṇa）、意（Mano） | 保留（G4 更正：恢复原题，例外保留巴利） |
| h2 | Definition of the term Citta | Citta一词的定义 | “心”（Citta）一词的定义 | **修改**（G4） |
| h2 | Distinction Between Citta, Viññāṇa, and Mano | Citta、Viññāṇa和Mano之间的区别 | 心（Citta）、识（Viññāṇa）、意（Mano）的区别 | **修改**（G4） |
| h2 | A Citta Over and Above the Five Aggregates | 超越五蕴的心（Citta） | 超越五蕴的心（Citta） | 保留（G4） |
| h2 | Viññāṇa-dhātu and Nibbāna-dhātu | Viññāṇa-dhātu和Nibbāna-dhātu | 识界（Viññāṇa-dhātu）与涅槃界（Nibbāna-dhātu） | **修改**（G4） |
| h2 | Discussion of the ’Knower’ (Phoo Roo) | 关于“知者”（Phoo Roo）的讨论 | 关于“知者”（Phoo Roo）的讨论 | 保留（G4） |

### authors-postscript

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Author’s Postscript | 作者后记 | 作者后记 | 保留 |

### bibliography

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Bibliography | 参考书目 | 参考书目 | 保留 |
| h3 | Pali Canon | 巴利圣典 | 巴利三藏 | **修改** |
| h4 | Vinaya Piṭaka | 律藏 | 律藏 | 保留 |
| h4 | Sutta Piṭaka | 经藏 | 经藏 | 保留 |
| h4 | Abhidhamma Piṭaka | 阿毗达磨藏 | 论藏 | **修改** |
| h3 | Pre-commentarial Texts | 前期义注文本 | 义注前文献 | **修改** |
| h3 | Commentaries, Sub-commentaries, and Other Non-Canonical Texts | 义注、复注及其他非经藏文本 | 义注、复注及其他藏外文献 | **修改** |
| h4 | Outstanding Scripture and Associated Text | 杰出经文及相关文本 | 重要典籍及相关文献 | **修改** |
| h4 | Vinaya Piṭaka | 律藏 | 律藏 | 保留 |
| h4 | Sutta Piṭaka | 经藏 | 经藏 | 保留 |
| h4 | Abhidhamma Piṭaka | 阿毗达磨藏 | 论藏 | **修改** |
| h4 | Grammar | 语法书 | 语法书 | 保留 |

### p-a-payutto

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | P. A. Payutto (Somdet Phra Buddhaghosacariya) | 巴育陀 (P. A. Payutto) | 巴育陀 | **修改** |
| h2 | Life and Work | 生活与工作 | 生活与工作 | 保留 |
| h3 | Primary Education | 初等教育 | 初等教育 | 保留 |
| h3 | Monastic Education | 僧侣教育 | 僧侣教育 | 保留 |
| h3 | Ecclesiastical titles | 法号 | 僧衔 | **修改** |
| h3 | Religious Activities | 弘法活动 | 弘法活动 | 保留 |
| h2 | Honours Received | 所获荣誉 | 所获荣誉 | 保留 |
| h3 | Honorary Positions | 荣誉职位 | 荣誉职位 | 保留 |
| h3 | Decorations of Honour and Awards | 荣誉勋章与奖项 | 荣誉勋章与奖项 | 保留 |
| h3 | Honorary Doctorate Degrees | 荣誉博士学位 | 荣誉博士学位 | 保留 |

### president-of-the-buddhadhamma-foundation

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | President of the Buddhadhamma Foundation | 佛法基金会主席 | 佛法基金会主席 | 保留 |
| h3 | Education | 教育经历 | 教育经历 | 保留 |
| h4 | Activities During Study at University | 大学期间活动 | 大学期间活动 | 保留 |
| h3 | Life and Work | 生活与工作 | 生活与工作 | 保留 |

### copyright

| 级 | 英文 | 现译 | 定稿 | 说明 |
|---|---|---|---|---|
| h1 | Copyright | 版权 | 版权 | 保留 |

---
## 三、核心词表（定稿译法）

下表给出语境规范，先辨概念、语法角色及所指再选主称，不把允许的语境分用误当任意混称；本轮止观/chanda及乐的规则见m-review-concepts-01节。完整表（含自动抽取的巴利词约 725 条）见 `glossary-final.csv`。“现有译法”中的次数是子串计数，仅供参考。

| 英文 | 巴利 | 定稿译法 | 现有译法（次数） |
|---|---|---|---|
| insight meditation/insight | vipassanā | 观（普通论述）；修观（动作）；观禅（明确方法，与止禅对应）。音译与内观可用于首释、语词分析及特定译名引述；vipassanā-ñāṇa=观智，不泛化到所有ñāṇa〔m-review-concepts-01〕 | 毗婆舍那×118; 观禅×103; 内观×57; 观智×36; 修观×5 |
| tranquillity meditation/calm | samatha | 止（普通论述）；修止（动作）；止禅（明确方法，与观禅对应）；首现可注音译奢摩他〔m-review-concepts-01〕 | 奢摩他×34; 止禅×42; 止观×10; 寂止×10 |
| Abhidhamma | abhidhamma | 阿毗达摩（Abhidhamma Piṭaka=论藏） | 阿毗达磨×34; 阿毗达摩×131 |
| hatred/aversion | dosa | 嗔（G3：统一用“嗔”，不再用“瞋”） | （G3 前）瞋×168; 嗔×101 |
| mindfulness | sati | 念（sati）：作为心所/道支名称或括注巴利时作“念（sati）”；修习语境（建立/维持/滋养/运用 mindfulness，正念正知）作“正念”〔T1 修订，见 T1 确认事项〕 | 正念×301; 念×1317; 觉知×197; 忆念×44 |
| clear comprehension | sampajañña | 正知 | 正知×78; 明觉×1 |
| Commentaries/commentarial | aṭṭhakathā | 义注；Sub-commentary=复注 | 义注×633; 注释×52 |
| sub-commentary | ṭīkā | 复注 | 复注×68; 疏钞×11 |
| Pali Canon/Tipiṭaka | tipiṭaka | 《巴利三藏》（Pali Canon；作书名时加书名号，R3/D3）；Tipiṭaka＝三藏；Abhidhamma/Sutta/Vinaya Piṭaka＝论藏/经藏/律藏；不用巴利圣典、巴利经典；专名“巴利圣典协会”（Pali Text Society）保留〔D10〕 | 巴利三藏×233; 巴利圣典×51; 巴利经典×0; 三藏×288 |
| Pali |  | 巴利语 | 巴利语×201; 巴利文×26 |
| happiness | sukha | 按语境区分，见 4.1 | 安乐×674; 快乐×595; 幸福×185; 乐×3200 |
| suffering | dukkha | 苦（dukkha）；physical pain=痛 | 苦×2585; 痛苦×569; 苦难×33 |
| virtuous friend/good friend | kalyāṇamitta | 善友（章名与正文统一，不用“善知识”） | 善知识×1; 善友×194; 良师益友×1 |
| faith/confidence | saddhā | 信（saddhā）/信心；不用“信仰”除非指他宗教 | 信心×562; 信仰×152; 信×1554 |
| wise reflection/wise attention | yoniso-manasikāra | 如理作意（如理思惟只作为释义或一般“如理地思惟法义”，见 T1） | 如理作意×468; 如理思惟×7 |
| heedfulness | appamāda | 不放逸 | 不放逸×136; 精勤×29; 警觉×33 |
| wholesome desire | kusala-chanda | 善法欲 | 善法欲×294; 善欲×43; 正当欲求×1 |
| craving | taṇhā | 渴爱（taṇhā）为默认；缘起支、三爱名、戏论三法等紧凑列举中作“爱”；世间语境用“贪爱”或“贪欲”（见指南 G3-1） | 渴爱×673; 贪爱×263; 爱×1626 |
| clinging/attachment | upādāna | 取（缘起支）/执取；attachment（一般）=执着 | 执取×249; 取×894; 执着×402 |
| defilement | kilesa | 烦恼 | 烦恼×467; 杂染×29; 染污×80 |
| mental impurity/taint | āsava | 漏（āsava） | 漏×239; 诸漏×60; 烦恼漏×1 |
| concentration | samādhi | 定；同层对举可用戒、定、慧或戒行、禅定、智慧。禅定在此是广义samādhi，不限jhāna；心的功能可称专注，增上心学不机械缩成禅那学〔m-review-concepts-02〕 | 定×3850; 禅定×390; 专注×347; 三摩地×6 |
| absorption | jhāna | 禅那（jhāna） | 禅那×492; 禅定×390; 入定×9 |
| meditation | bhāvanā | 禅修；bhāvanā=修习；避免“冥想” | 禅修×258; 修习×723; 打坐×2 |
| meditation object/meditation technique | kammaṭṭhāna | 业处（kammaṭṭhāna） | 业处×35; 禅修所缘×20 |
| Path Factors/path factor | maggaṅga | 道支 | 道支×171; 八正道支×12; 道分×4 |
| Noble Eightfold Path/Eightfold Path | ariya aṭṭhaṅgika magga | 八正道（首次可注“八圣道”） | 八正道×149 |
| Threefold Training | tisso sikkhā | 三学 | 三学×139 |
| Four Noble Truths | ariya-sacca | 四圣谛 | 四圣谛×189; 四谛×1 |
| Dependent Origination | paṭiccasamuppāda | 缘起 | 缘起×430; 缘起法×51; 十二缘起×5; 依缘共起×1 |
| specific conditionality | idappaccayatā | 此缘性 | 此缘性×9; 特定缘起性×8; 具体缘起法×1 |
| Three Characteristics | tilakkhaṇa | 三法印；单项可用 无常法印/苦法印/无我法印（指南 4.6） | 三法印×172; 三相×2 |
| nonself/not-self | anattā | 无我 | 无我×296; 非我×19 |
| impermanence | anicca | 无常 | 无常×375 |
| formations/volitional formations | saṅkhāra | 按语境区分，见 4.2 与 G3-4：与无为法/涅槃/一切法对举及解释性语境作“有为法”（可作“行法”）；行蕴、缘起支、身语意行作“行” | 行×6356; 行蕴×108; 有为法×221; 诸行×17; 造作×177 |
| Five Aggregates | pañcakkhandha | 五蕴 | 五蕴×232 |
| sense spheres/sense bases | āyatana | 六处（āyatana）；internal sense bases=六内处 | 六处×94; 六入×2; 六根×28; 感官基础×11 |
| perception | saññā | 想 | 想×1257; 认知×154; 知觉×20 |
| feeling | vedanā | 受（vedanā） | 受×2372; 感受×301 |
| consciousness | viññāṇa | 识（viññāṇa） | 识×1632; 心识×127; 意识×135 |
| volition/intention | cetanā | 技术主称思（cetanā），可释心的意向作用；同一技术定义及连续回指用思。普通目的、打算与意图可自然保留；英语 intention 的词义讨论、saṅkappa/adhippāya 等其他术语不能据字面强套思 | 思×1630; 意图×174; 意志×33 |
| mental factor | cetasika | 心所 | 心所×158; 心所法×9 |
| Nibbāna | nibbāna | 涅槃 | 涅槃×803 |
| arahant | arahant | 阿罗汉；修行人用阿罗汉向，道本身用阿罗汉道，果用阿罗汉果。不把所有magga一律改向〔m-review-concepts-02〕 | 阿罗汉×554 |
| stream-enterer/stream-entry | sotāpanna | 须陀洹；修行人用须陀洹向，道本身用须陀洹道，果用须陀洹果。首次或有解释需要可括注入流者；词源讨论及入流支保留意译。不把所有magga一律改向〔m-review-concepts-02〕 | 须陀洹×122; 入流者×57; 入流×121; 预流×25 |
| once-returner | sakadāgāmī | 斯陀含；修行人用斯陀含向，道本身用斯陀含道，果用斯陀含果。首次或有解释需要可括注一来者；词源讨论及入流支保留意译。不把所有magga一律改向〔m-review-concepts-02〕 | 斯陀含×27; 一来者×9; 一来×24 |
| non-returner | anāgāmī | 阿那含；修行人用阿那含向，道本身用阿那含道，果用阿那含果。首次或有解释需要可括注不还者；词源讨论及入流支保留意译。不把所有magga一律改向〔m-review-concepts-02〕 | 阿那含×29; 不还者×37 |
| noble disciple | ariya-sāvaka | 圣弟子 | 圣弟子×163; 圣者弟子×2 |
| noble being/noble one | ariya-puggala | 圣者 | 圣者×195; 圣人×1; 圣贤×1 |
| trainee | sekha | 有学 | 有学×57; 学人×18; 受训者×4 |
| monk/bhikkhu | bhikkhu | 比丘；monastic=出家人 | 比丘×1406; 僧侣×28; 僧人×4; 和尚×2 |
| layperson/householder | gahapati | 居士/在家人 | 居士×306; 在家人×9; 在家众×19 |
| Sangha/monastic community | saṅgha | 僧团（Saṅgha 作专名可用“僧伽”） | 僧伽×143; 僧团×269; 僧众×4 |
| Triple Gem | tiratana | 三宝；并列主称佛、法、僧。若法明确指佛陀教法，也可佛陀、佛法、僧伽；法还包括真理与证悟，不为字数一律扩为佛法〔m-review-concepts-02〕 | 三宝×44; 三宝×44 |
| Buddha-Dhamma/Dhamma | dhamma | Dhamma=法；Buddha-Dhamma=佛法；绝不译作“达摩” | 佛法×740; 法×5649; 达摩×175; 正法×104 |
| holy life | brahmacariya | 梵行；义释可用崇高的行为/生活。广义包含整个道或中道，不仅是戒行；狭义独身依语境说明〔m-review-concepts-02〕 | 梵行×147; 圣洁生活×3 |
| psychic powers/supernormal powers | iddhi | 神通（iddhi）；miracle（pāṭihāriya）=神变；六神通中 iddhividhā=神足通（G3-8） | 神通×341; 神变×54 |
| higher knowledge/direct knowledge | abhiññā | 证智（abhiññā 总称）；指六种/五种具体能力时作“神通”（六神通）；见 4.5 | 神通×341; 胜智×27; 殊胜智×22; 证智×3 |
| devas/divine beings/gods | deva | 天人（deva）；God（一神教）=上帝/神 | 天人×303; 天神×66; 诸天×3; 神明×3; 神×957 |
| Indra/Sakka | sakka | 帝释天 | 帝释天×22; 帝释×23; 因陀罗×2 |
| Brahma | brahmā | 梵天 | 梵天×103; 大梵天×14 |
| Mara | māra | 魔罗 | 魔罗×36; 摩罗×21 |
| lovingkindness/loving-kindness | mettā | 慈（mettā）/慈心 | 慈心×82; 慈爱×75; 慈×291 |
| compassion | karuṇā | 悲（karuṇā）/悲心 | 悲心×55; 悲悯×55; 慈悲×66; 悲×356 |
| sympathetic joy/appreciative joy | muditā | 喜（muditā）/随喜 | 随喜×24; 喜心×1 |
| equanimity | upekkhā | 舍（upekkhā） | 舍×778; 平等心×1; 平静×146; 舍心×30 |
| Divine Abidings/sublime states | brahmavihāra | 四梵住（B10-r2 用户决定；四无量心仅用于 appamaññā） | 四梵住×24; 四无量心×14; 梵住×46 |
| rapture/joy/delight | pīti | 喜（pīti） | 喜×700; 喜悦×247; 欢喜×55 |
| tranquillity | passaddhi | 轻安（passaddhi） | 轻安×49; 宁静×28; 平静×146 |
| one-pointedness | ekaggatā | 心一境性（技术名相；谓语可作专注于一境） | 一境性×41; 心一境性×13; 一心×50 |
| initial application/applied thought | vitakka | 寻 | 寻×527; 觉×1138 |
| sustained application/sustained thought | vicāra | 伺 | 伺×47; 观×1043 |
| hindrances | nīvaraṇa | 盖/五盖 | 五盖×68; 盖×261; 障碍×106 |
| Factors of Enlightenment/enlightenment factors | bojjhaṅga | 觉支/七觉支 | 七觉支×64; 觉支×153 |
| Foundations of Mindfulness | satipaṭṭhāna | 四念住（南传通行） | 四念住×80; 念住×137 |
| mindfulness of breathing | ānāpānasati | 安般念（入出息念） | 安般念×40; 入出息念×8; 观呼吸×1 |
| Paths to Success/Bases of Success | iddhipāda | 四神足 | 四神足×27; 四如意足×1 |
| access concentration | upacāra-samādhi | 近行定 | 近行定×38 |
| attainment concentration | appanā-samādhi | 安止定 | 安止定×49; 根本定×8 |
| attainment of cessation | nirodha-samāpatti | 灭尽定（全称想受灭尽定） | 灭尽定×68; 想受灭尽定×43; 想受灭定×3 |
| merit | puñña | **福德**（T1 用户决定，取代 B10-r2“功德”）；make merit 按语境作积累福德/行善积福/修福/行福德之事/做功德（口语、经文俗语）；fruit of merit＝福报；固定词保留：福业、福业事、福行、福田、福尽死、非福；“功德”只用于 guṇa、回向功德/随喜功德、做功德等习语及 Q4 布施功德等标签 | 功德×227; 福德×15; 福×548 |
| Bases of Merit/meritorious action | puññakiriyāvatthu | 福业事（十福业事；不用“十种功德业处”）〔T1 全书核对〕 | 福业事×5; 功德行×21 |
| generosity/giving | dāna | 布施 | 布施×282; 慷慨×45; 施舍×2 |
| moral conduct/virtue/morality | sīla | 戒行（sīla）；具体条目、五戒、戒学作“戒”；泛论伦理、与他宗教比较时用“道德”；人品用“德行”（指南 4.4） | 戒×1332; 戒行×364; 德行×355; 道德×340; 持戒×36 |
| precepts | sikkhāpada | sikkhāpada=学处；precepts（五戒）=戒 | 戒条×19; 学处×44; 戒律×276 |
| discipline/Vinaya | vinaya | 律（Vinaya）；Vinaya Piṭaka=律藏 | 律×775; 戒律×276; 律藏×122 |
| Ten Wholesome Courses of Action | kusala-kammapatha | 十善业道 | 十善业道×31 |
| Right Livelihood | sammā-ājīva | 正命 | 正命×70 |
| Right Thought/Right Intention | sammā-saṅkappa | 正思惟 | 正思惟×83; 正思维×1 |
| thinking/thought |  | 按语义：佛法修习的 reflection/contemplation、saṅkappa、cintā＝思惟；一般 thinking/thought process/way of thinking＝思维/思考；manasikāra＝作意〔T1 用户确认〕；paccavekkhaṇa＝省察，yoniso paṭisaṅkhā＝如理省察〔T1〕 | 思惟×682; 思维×152 |
| wholesome | kusala | 善（kusala）/善法 | 善法×784; 善的×291; 健全×18 |
| unwholesome | akusala | 不善 | 不善法×176; 不善×461 |
| evil/bad | pāpa | 恶（pāpa）；避免“罪”（有基督教色彩） | 罪×55; 恶×762; 恶业×48 |
| kamma/karma | kamma | 业（kamma）；perform kamma / volitional action（动词）＝造业；不用“思业”“意图行为”泛称一切业〔T2〕 | 业×1552; 业力×10; 因果×204 |
| result of kamma/kamma-result | vipāka | 异熟/果报；vipāka-citta=异熟心 | 果报×181; 业果×63; 异熟×11; 业报×13 |
| rebirth | punabbhava | 再生/投生（避免“转世”） | 再生×65; 转世×3; 投生×104 |
| round of rebirth/cycle | saṁsāra | 轮回 | 轮回×101; 生死轮回×7; 轮回流转×13 |
| ignorance | avijjā | 无明 | 无明×366; 愚痴×25 |
| delusion | moha | 痴 | 痴×201; 愚痴×25 |
| greed | lobha | 贪 | 贪×764; 贪婪×74; 贪欲×143 |
| sensual desire/sense desire | kāmacchanda | 欲贪（kāmacchanda） | 欲贪×41; 贪欲×143; 感官欲望×46 |
| sense pleasure/sensual pleasure | kāma-sukha | 欲乐 | 欲乐×354; 感官之乐×107; 感官享乐×129 |
| conceit | māna | 慢（māna）；“我是”慢=我慢 | 我慢×45; 慢×151 |
| identity view/personality view | sakkāya-diṭṭhi | 身见（有身见） | 身见×20; 有身见×11; 我见×33 |
| wrong view | micchā-diṭṭhi | 邪见 | 邪见×111; 错误见解×3 |
| Right View | sammā-diṭṭhi | 正见 | 正见×394 |
| Middle Way/Middle Path | majjhimā-paṭipadā | 中道 | 中道×174; 中道修行×6 |
| Middle Teaching | majjhena-dhammadesanā | 中道法义 | 中道法义×17; 中道教法×12; 中说×6 |
| virtuous/wholesome way of life |  | 见 toc.md | 贤善生活×5; 健全人生×1 |
| liberation of mind | cetovimutti | 心解脱 | 心解脱×133 |
| liberation by wisdom | paññāvimutti | 慧解脱 | 慧解脱×101 |
| liberated both ways | ubhatobhāga-vimutta | 俱解脱（者） | 俱解脱×38; 俱分解脱×1 |
| dry-insight practitioner | sukkha-vipassaka | 纯观行者 | 纯观行者×20; 纯观者×3 |
| wisdom | paññā | 慧（paññā）/智慧；术语组合用“慧” | 智慧×1515; 慧×1925 |
| knowledge | ñāṇa | 智（ñāṇa） | 智×2183; 知识×425; 智慧×1515 |
| true knowledge | vijjā | 明（vijjā） | 明×1251; 真知×14; 三明×29 |
| Supreme Peace |  | 至上寂静 | 至上寂静×7 |
| designation/concept | paññatti | 概念／概念法；首现可加“（又译“施设”）”（G3-6，取消 B1-r2 的“施设”规则）；书名《人施设论》照旧 | 施设×15; 概念×159; 假名×1 |
| ultimate truth/ultimate reality | paramattha | 胜义谛/究竟法 | 胜义×30; 究竟实相×3; 究竟义×7 |
| conventional truth | sammuti-sacca | 世俗谛 | 世俗谛×14 |
| Laws of Nature/natural laws | niyāma | 自然法则（niyāma）；五种 niyāma=五定律 | 自然法则×170; 尼夜摩×8; 定律×10 |
| suchness | tathatā | 如是性（名称）／如是（形容）；亦可翻译为“如性”〔R3-r2〕 | 如是性×4 |
| life-continuum | bhavaṅga | 有分（bhavaṅga） | 有分×18; 有分心×7; 有分识×1; 潜意识×6 |
| mind-moment | cittakkhaṇa | 心刹那 | 心识刹那×21; 心刹那×16 |
| mind and matter/mentality-materiality | nāma-rūpa | 名色 | 名色×89; 心物×3 |
| object/sense object | ārammaṇa | 所缘 | 所缘×450; 对象×287; 目标×530; 六尘×25 |
| Discourse/Sutta | sutta | 经；具体经名用《……经》 | 经×1588; 经文×311 |
| verse | gāthā | 偈 | 偈×140; 偈颂×70; 诗偈×7 |
| Bodhisatta | bodhisatta | 菩萨 | 菩萨×28 |
| Tathāgata | tathāgata | 如来 | 如来×119 |
| Blessed One | bhagavā | 世尊 | 世尊×216 |
| Venerable | āyasmā | 尊者（放在名字前面：尊者舍利弗）；括注不加 Ven.；巴利三藏人名一律译出（G4-1） | 尊者×356; 长老×85; 大德×11 |
| Sāriputta |  | 尊者舍利弗（Sāriputta） | 舍利弗×92 |
| Ānanda |  | 尊者阿难（Ānanda）；不用阿难陀/阿难达 | 阿难陀×18; 阿难达×2; 阿难×84 |
| Moggallāna |  | 尊者摩诃目犍连（Mahā Moggallāna） | 目犍连×14; 摩诃目犍连×9; 大目犍连×2 |
| Anāthapiṇḍika |  | 给孤独长者（Anāthapiṇḍika） | 给孤独长者×7; 给孤独×7 |
| Visākhā |  | 毗舍佉（Visākhā） | 毗舍佉×2; 维沙卡×2 |
| Devadatta |  | 提婆达多 | 提婆达多×8; 提婆达多×8 |
| Visuddhimagga |  | 《清净道论》 | 清净道论×104 |
| Milindapañhā/Milinda |  | 《弥兰王问经》 | 弥兰王问经×1; 弥兰陀王问经×2; 弥兰王问×1 |
| Kālāma Sutta |  | 《卡拉玛经》（Kālāma Sutta）；族人 Kālāma＝卡拉玛人（G10 定；G8“伽蓝”已取代）；目录“迦摩罗经”有误（已改） | 迦摩罗经×0 |
| refuge / go for refuge | saraṇa | 皈依（全书统一，“归依”已改；B14 D4）；attasaraṇa / attadīpa＝自归依（保留） | 皈依×32; 自归依×1; 自皈依×1（six-sense-spheres 426，待统一） |
| Dhammapada |  | 《法句经》 | 法句经×25; 法句×25 |
| Payutto |  | 帕·巴育陀／巴育陀比丘（P. A. Payutto）；僧衔 颂德·帕·菩陀构萨迦利雅 | 巴育陀×26 |
| Ajahn Jayasaro |  | 阿姜查雅萨罗（Ajahn Jayasaro），不加间隔号 | 阿姜·查雅萨罗×11 |
| Thai |  | 语言=泰语，版本=泰文版 | 泰文×34; 泰语×72; 泰国×80 |
| spiritual practice/practice | paṭipatti | 修行；practical application（作标题或指实际运用）=实践应用（指南 1.6）；spiritual（修行义）＝修行〔R1/R2〕 | 修行×1408; 修持×7; 实修×14; 修习×812 |
| development/cultivation | bhāvanā | bhāvanā=修习；develop wisdom=培育智慧（不用“开发”，指南 4.7） | 培育×587; 开发×53; 培养×288; 修习×723; 发展×341 |
| Introduction |  | 导论 | 导论×35; 引言×3; 介绍×17; 前言×11 |
| Appendix |  | 附录一/附录二… | 附录×172 |
| Paccekabuddha/Silent Buddha | paccekabuddha | 独觉佛（不用“辟支佛”） | 辟支佛×15 |
| gratification/advantage (of) | assāda | 乐味（assāda）；与过患、出离成组：乐味、过患、出离；happiness 标题已改为“乐味与过患”（T1-r3）；呼应句同步 | 优点×4; 功德×2; 乐味×1; 满足×1 |
| danger/drawback/disadvantage | ādīnava | 过患（ādīnava）；与乐味、出离成组 | 缺点×6; 过患×4; 危险×1 |
| escape/release | nissaraṇa | 出离（nissaraṇa）；与乐味、过患成组 | 出离×8; 解脱×2; 摆脱×1 |
| cessation | nirodha | 一般用“寂灭”；缘起“此灭故彼灭”与灭谛等固定术语用“灭”（灭谛、苦灭、灭尽定、想受灭尽定），见 4.3；不用“尼罗陀” | 灭×10; 苦灭×7; 止息×5; 尼罗陀×3 |
| supernatural |  | 神通（标题与正文统一）；世间语境用“超自然”（G3-8） | 神通; 超自然 |
| Gotama | gotama | 乔达摩（人名，保留） | 乔达摩 |
| Somdet Phra Buddhaghosacariya |  | 颂德·帕·菩陀构萨迦利雅（Somdet Phra Buddhaghosacariya） |  |
| recollection of past lives | pubbenivāsānussati-ñāṇa | 宿命智（六神通中作“宿命通”） | 宿命智×4; 宿命通×2 |
| destruction of the taints | āsavakkhaya-ñāṇa | 漏尽智（六神通中作“漏尽通”） | 漏尽智×4; 漏尽通×2 |
| vayadhammā saṅkhārā, appamādena sampādetha |  | 一切有为法皆是坏灭法，当不放逸以成道业（G4-2，全角逗号） |  |
| Sāriputta (name) |  | 尊者舍利弗（不留拉丁原名；G3-9/G4-1） |  |
| Anuruddha |  | 尊者阿那律（Anuruddha） |  |
| Aṅgulimāla |  | 尊者鸯掘摩罗（Aṅgulimāla） |  |
| Puṇṇa |  | 尊者富楼那（Puṇṇa） |  |
| Soṇa (Koḷivisa) |  | 尊者索那（Soṇa） |  |
| Mahaka |  | 尊者摩诃迦（Mahaka） |  |
| Koṇḍadhāna |  | 尊者军头波汉（Koṇḍadhāna） |  |
| Piṇḍola Bhāradvāja |  | 尊者宾头卢·颇罗堕（Piṇḍola Bhāradvāja） |  |
| Sirimaṇḍa |  | 尊者尸利曼陀（Sirimaṇḍa） |  |
| Vacchagotta |  | 婆蹉衢多（Vacchagotta）；Aggivacchagotta Sutta=《婆蹉衢多火喻经》（G5，取代“瓦恰葛达”） | 瓦恰葛达×8 |
| Vajirā (nun) |  | 比丘尼瓦吉拉（Vajirā） |  |
| Baka Brahmā |  | 婆迦梵天（Baka） |  |
| Citta (householder) |  | 质多居士（Citta） |  |
| Mahānāga Thera |  | 尊者摩诃那伽长老（Mahānāga Thera） |  |
| Pabbhāravāsī-Tissa |  | 长老山窟住帝须（Pabbhāravāsī-Tissa） |  |
| Bhikkhu Bodhi |  | 菩提比丘（Bhikkhu Bodhi） |  |
| Bhikkhu Ñāṇamoli |  | 髻智比丘（Bhikkhu Ñāṇamoli） |  |
| Nyanaponika Thera |  | 长老向智（Nyanaponika Thera） |  |
| Narada Thera |  | 长老那烂陀（Narada Thera） |  |
| U Narada |  | 尊者那拉达（U Narada） |  |
| U Thittila |  | 尊者帝提拉（U Thittila） |  |
| Thanissaro Bhikkhu |  | 坦尼沙罗比丘（Thanissaro Bhikkhu） |  |
| Buddhadāsa Bhikkhu |  | 佛使比丘（Buddhadāsa） |  |
| Parivāra |  | 《附随》（Parivāra） |  |
| Special Appendix: Citta, Viññāṇa, Mano |  | 附录：心（Citta）、识（Viññāṇa）、意（Mano）（标题例外保留巴利） |  |
| loka-paññatti (sutta phrase) |  | 世间施设（经文原译保留） |  |
| pāṭihāriya |  | 神变 |  |
| aniccā vata saṅkhārā |  | 确实，一切有为法无常，是生灭法。既已生起，便会止息；其止息是究竟之乐。 |  |

---
## 四、需按语境处理的术语（判定规则）

### 4.1 sukha / happiness / pleasure（重点）
**现状清点**（中文全书子串计数）：安乐 674、快乐 595、幸福 185、乐（单字，含复合词）约 3200、欲乐 354、享乐 167、感官享乐 129、感官之乐 107、乐受 116、喜乐 41、禅悦 40、乐住 25（其中现法乐住 17）、涅槃之乐 15、天人之乐 15、物质之乐 19、非物质之乐 9。英文：happiness 1809、pleasure 826、sense pleasure 233、sensual pleasure 145、bliss 119、happy 204、welfare 122。
巴利文括注里的 sukha 复合词约 90 种，大多已经用“X之乐”格式（如 nekkhamma-sukha＝出离之乐，vimutti-sukha＝解脱之乐），格式基本一致；主要问题出在没有括注的英文 happiness 上，安乐、快乐、幸福三种译法混用。

**判定规则**
| 语境 | 英文常见形式 | 定稿 | 例 |
|---|---|---|---|
| 作为教理术语的 sukha（与 dukkha 相对，三受之一以外） | happiness, sukha | **乐** | “苦与乐”“乐的层次” |
| 受蕴中的乐受 | pleasant feeling, sukha-vedanā | **乐受**（苦受、不苦不乐受） | — |
| 类别总称及各层次比较 | happiness / ความสุข / sukha，不限善乐或乐受 | **乐** | 第十一章：乐；以乐证乐；乐的例子可含欲乐〔m-review-concepts-01〕 |
| 安稳喜乐的自然状态及惯用表达 | 依全段具体含义判断，不因spiritual/true就一概套用 | **安乐**（可用） | 身心安乐；安乐地住；愿众生安乐 |
| 感官五欲之乐 | sense pleasure, sensual pleasure, kāma-sukha | **欲乐**（不用“感官享乐/感官之乐”，除非句子太拗口） | “欲乐的过患” |
| 依赖物质 / 不依赖物质 | sāmisa / nirāmisa-sukha | **物质之乐 / 非物质之乐**（用户已定） | — |
| 巴利复合词 X-sukha | jhāna-sukha 等 | **X之乐**：禅那之乐（jhāna-sukha；“禅悦”只在不括注的修辞句中用）、涅槃之乐、解脱之乐、出离之乐、天人之乐、爱尽之乐 | — |
| 固定术语 | diṭṭhadhamma-sukhavihāra | **现法乐住** | — |
| 日常口语、凡夫的心情 | happy, be happy, joy（非 pīti） | **快乐**、开心 | “他感到快乐” |
| 社会、众生的福祉 | welfare, well-being of the many, bahujana-sukha | **利益安乐**（hita-sukha）/福祉 | “为多众的利益安乐” |
| 最高之乐 | supreme / perfect happiness, parama-sukha | **至上安乐**（Ch.11 小标题“圆满的安乐”保留） | “涅槃是至上安乐” |
| bliss | bliss | 一般作“妙乐”，涅槃语境作“至乐” | — |
| pleasure（贬义、享乐主义） | pleasure-seeking, indulgence | **享乐** | “沉溺享乐” |
| pīti、delight、joy（禅支） | rapture, joy | **喜**（不译成“乐”） | “喜与乐” |

**R4 补充（2026-11-04，乐词族全书核对）**
| 语境 | 英文 | 定稿 |
|---|---|---|
| sensuality, sense desire（kāma） | sensuality, sense desire | **欲**（如“对欲的渴爱”“迷恋于欲”） |
| 初禅定型句 | secluded/apart from sensual pleasures | **远离欲**、远离不善法 |
| 五欲 | five cords of sensual pleasure（kāma-guṇa） | **五欲** |
| 乐味 | gratification（assāda） | **乐味**（“欲乐的乐味”） |
| nandi / abhinandita / delight in | delight | **喜 / 喜好**；delightful feelings＝**可喜的感受** |
| 喜乐 | — | **只用于 pīti-sukha**（离生喜乐、定生喜乐） |
| pāmojja（作术语、在悦→喜→轻安→乐→定链中） | joy, gladness | **悦**；pīti＝**喜**；描述性行文中 EN joy 可作“喜悦” |
| 经文中的 pleasant/painful feeling | pleasant feeling | **乐受 / 苦受**；论述性行文的 pleasant sensations 可作“愉悦的感受” |
| X-sukha 复合词 | bliss/happiness of X | **X之乐**：涅槃之乐、解脱之乐、禅那之乐（不作禅悦/禅乐）、观智之乐、爱尽之乐、拥有之乐、无过之乐、出世间之乐、灭尽定之乐 |
| bliss（非 pīti、非 X-sukha） | profound bliss 等 | **妙乐**；end in bliss＝至乐（不用“极乐”） |
| 同段同指 | happiness | 同一段落同一层次的所指用同一主称；层次比较优先用欲乐、禅那之乐等明确对象。不能只凭凡夫/圣者身份把同一sukha自动分配成快乐/安乐〔m-review-concepts-01〕 |
| 幸福 | times of happiness, pursuit of happiness, blissful hour | 可用于日常、世俗语境与引语；不作教理 sukha 的译法 |

**R4-r2 补充（2026-11-04，乐字族逐段复核，4451 处全覆盖）**
| 语境 | 英文 | 定稿 |
|---|---|---|
| 社会层面的乐 | social happiness | ~~社会层面的快乐~~ → **社会层面的安乐**（R4-r3 改定，见 R4-13）〔R4-07〕 |
| 福祉与乐 | welfare and happiness, wellbeing and happiness | **福祉和安乐**；diṭṭhadhamma/samparāya 的 hita-sukha（今生、来世）＝**利益安乐**〔R4-08〕 |
| 修行次第链 | joy(pāmojja) → delight/rapture(pīti) → tranquillity → happiness(sukha) → concentration | **悦 → 喜 → 轻安 → 乐 → 定**，经文与论述一律如此（含 Vin/AN 无悔链）；“有乐者心定”〔R4-09〕 |
| 居士四乐（AN 4.62） | gihi-sukha: atthi/bhoga/anaṇa/anavajja | **居士之乐**：拥有之乐、受用之乐、无债之乐、无过之乐；“四种乐”〔R4-10〕 |
| 章名交叉引用 | Chapter 11 on Happiness | **第十一章“安乐”**（与章标题一致）〔R4-11〕 |
| 精致/内在/完整之乐 | refined / inner / complete happiness | 同段与“X之乐”系列一致时作**乐**（更精致之乐、内在之乐） |

**R4-r3 单字/双字标准（2026-11-04，用户 [pt47u] 第8点；取代 R4/R4-r2 中与之冲突的表述）**

总原则：单字是“术语、对举、成组”的形式；双字是“行文”的形式。拿不准时读出声：前后是双字词就用双字，前后是单字就用单字。

| 场合 | 用单字（乐/苦/悦/喜） | 用双字（安乐/快乐/痛苦/愉悦/喜悦） |
|---|---|---|
| 术语、次第链、列举的因素 | 戒→无悔→**悦**→**喜**→轻安→**乐**→定；禅支“喜、乐、心一境性”；乐受、苦受；“四种乐”“三种乐” | — |
| X-sukha 复合词 | **X之乐**（四字最佳：拥有之乐、受用之乐、无债之乐、无过之乐、涅槃之乐、内在之乐、更高之乐） | — |
| 与单字对举 | 乐与苦、苦乐、得乐离苦、“如何对待乐，也关乎如何对待苦” | — |
| 偈颂、经文定型句 | 保留原有节奏（“这种乐是可以预料的”） | — |
| 修饰语＋的＋乐 | ✗ 不用（“内在的乐”“更高的乐”“人类低级的乐”） | 改为“X之乐”（修饰语为单/双字形容词）或“X的安乐/快乐”（修饰语为层次/形式/种类/所有/其他等） |
| 与双字词并列 | ✗（“乐或满足”“喜悦和乐”“乐和舒适”） | 安乐与满足、喜悦和安乐、安逸和舒适 |
| 作“概念”的主语/宾语 | 可用：“乐是欲望的满足”“培育乐”“体验到乐”（本章教理定义处） | 与双字动词/宾语成组时改双字（“培育安乐与改善生活”） |

安乐 vs 快乐：**安乐**＝善的、更深的、修行与教理层面的乐与福祉（含社会层面的安乐、圣者的个人安乐与社会安乐）；**快乐**＝日常、世俗、情绪性的乐（happy、凡夫/国王的快乐、涵盖欲乐在内的泛称“各种快乐的乐味与过患”、他人的“其他形式的快乐”）。

悦 vs 愉悦 vs 喜悦（pāmojja）：次第链或作为列举因素/术语时作**悦**；pāmojja 在行文中作名词/品质（EN joy）时作**愉悦**（“愉悦是一种至关重要的内在品质”）；一般英文 joy 作**喜悦**；pleasant/pleasing 作**愉悦/令人愉悦**；经偈“比丘悦多”保留。

**R4-r3 其他决定**

| 项目 | 规则 | 编号 |
|---|---|---|
| welfare and happiness（hita-sukha） | 作者行文、AN/MN“导向福祉和安乐”＝**福祉和安乐**；“福利”一律不用（福利和安乐→福祉和安乐；福利、利益和安乐→福祉、利益和安乐）；bahujana-hitāya bahujana-sukhāya 定型句＝**（为了）许多人/多数人的利益和安乐**；今生/来世 hita-sukha＝利益安乐（R4-08 不变） | R4-14 |
| 社会层面的乐 | **社会层面的安乐**；个人安乐与社会安乐（推翻 R4-07“社会层面的快乐”） | R4-13 |
| 无过之乐 | anavajja-sukha＝**无过之乐**（四字，与拥有/受用/无债之乐一致；推翻 R4-10 的“无过失之乐”）；标题“无过失地受用欲乐”不在此列 | R4-15 |
| 章节交叉引用 | 本书章节一律作 **第N章“章名”**（中文数字；章名取 h1 冒号后全名，如 第六章“涅槃：至上寂静”、第十章“佛陀关于欲望的教导”）；不写号时作 **“章名”一章**；不用“论”“关于X的第N章”“第N章关于X的内容/章节”；附录作 第N章“章名”附录二；泰文版/英文版章号（他版对照）不改 | R4-16 |
| 欲乐 | kāma-sukha 在经文、教理处仍作**欲乐**；与“欲/欲望/欲求”紧邻（“对欲乐的欲”）或现代生活语境标题时作**感官享乐**（生育与感官享乐、对感官享乐的欲求） | R4-17 |
| abhinandita / anabhinandita | **贪恋 / 不被贪恋**（不作喜好）；“喜好和厌恶”（anurodha-virodha、likes and dislikes）＝**好恶**；dhamma-rāga＝对法的贪恋；ālaya-rāmā＝乐于执着；attachment or delight＝执着或迷恋；个人喜好（likes, preferences）保留 | R4-18 |
| taṇhā 定型句 | tatra-tatrābhinandinī＝**处处寻求欢愉**（复原原译；nandi-rāga 仍作喜与贪） | R4-19 |
| 妙乐 | 避免“妙…妙”：最精致的妙乐 | R4-20 |

**禁用（R4 修订）**：“幸福”不作为教理 sukha 的译法；日常、世俗语境与引语可用〔R4-02〕。原文：*：除非引用别人的说法，“幸福”不作为 sukha 的译法（现有 185 处要逐条改成 乐/安乐/快乐）。

### 4.2 saṅkhāra 及相关词
**现状清点**：“行”（含复合词）约 6356 处、行蕴 108、有为法 221、造作 177、诸行 17、一切行 7、身行 26、语行（口行 2）、意行 62、心行 29、福行 9、非福行 4、不动行 3；巴利括注中 saṅkhāra 被译作 行 65 / 行蕴 19 / 法 20 / 其他 4。

| 语境 | 定稿 | 说明、例 |
|---|---|---|
| 五蕴中的第四蕴 | **行蕴**（saṅkhāra-khandha）；在五蕴并列时单用“行” | “色、受、想、行、识” |
| 缘起支“无明缘行” | **行** | 不改 |
| 三种行：kāya-/vacī-/citta-saṅkhāra（缘起语境） | **身行、语行、意行** | 安般念语境中的 citta-saṅkhāra 作“心行”（现在“意行/心行”混用） |
| abhisaṅkhāra 三种 | **福行、非福行、不动行** | — |
| 三法印语境（sabbe saṅkhārā aniccā） | **有为法**（“一切有为法（saṅkhāra）无常”）；三法印条目名可作“一切行无常（Sabbe saṅkhārā aniccā）：所有有为法都是无常的” | G3 规则 4：与无为法/涅槃/一切法对举时必须作“有为法”；经文固定句（如“诸行寂灭，究竟安乐”）可保留“诸行” |
| 有为法、条件所成之物（saṅkhata、conditioned things） | **有为法**；形容词作“有为的” | 与 asaṅkhata＝无为 / 无为法 相对 |
| 动词或过程义（fabricate、form、concoct） | **造作** | 只在非术语的叙述中用 |
| saṅkhāra-dukkha | **行苦** | — |
| 括注 saṅkhāra 却译作“法”的 20 处 | 逐条复核：指一切法时，英文多为“dhamma”，应改成“有为法” | 不要把 saṅkhāra 和 dhamma 都译作“法” |
| visaṅkhāra | **离行**（即涅槃） | 现在误作“法” |

### 4.3 nirodha
- 一般叙述、指“熄灭/止灭”的状态：**寂灭**（例：“禅那、寂灭与涅槃”）。
- 固定术语一律用**灭**：灭谛、苦灭、苦灭圣谛、灭尽定、想受灭尽定、缘起的“灭”的方向（“此灭故彼灭”）。
- 四圣谛小标题：`灭：苦的止息`。
- 不用音译“尼罗陀”（现有 3 处）。

### 4.4 sīla / morality / virtue
- 默认用 **戒行**（sīla、virtuous conduct、moral conduct）。
- **戒**：指具体的条目或数目（五戒、八戒、持戒），以及三学中的“戒学”。
- **律**：Vinaya；**学处**：sikkhāpada；**戒条**：泛称条文。
- **道德**：只在泛论人类伦理、与有神论道德或哲学比较时使用（“有神论道德”）。
- **德行**：只在指人的品德时使用（virtue as a personal quality），不作术语。

### 4.5 abhiññā（定稿：**证智**/**神通**，按语境）
- 总称、指“通过修行亲身证知的超常智慧”：**证智**。理由：①字面就是“证得之智”，一般读者不必解释也能懂；②南传汉译（如元亨寺本、庄春江译本）的“证智/通智”都有先例；③“胜智”语义含糊（用户反映难懂），“殊胜智”同样如此。
  （用户之前提到的“书圣制”应是语音输入的误识别，可能是“殊胜智”或“证智”，此处按“证智”定稿。）
- 列举具体的六种或五种能力：**神通**（六神通、五神通；天眼通、宿命通、漏尽通）。
- 与 iddhi（神变的能力）同时出现时：iddhi＝神通/神变，abhiññā＝证智，两者要区分。
- 动词“abhijānāti / directly know”：**亲证、证知**。

### 4.6 三法印（tilakkhaṇa）
- 总称一律用**三法印**（按用户决定）。
- 单独一项：说明“三法印中的某一项”时用 **无常法印 / 苦法印 / 无我法印**（例：小标题“单一法印的实际利益”下的三个小节）；描述事物性质的一般句子仍用“无常、苦、无我”（例：“一切有为法无常”不改成“无常法印”）。
- 英文“characteristic”单指“相”的场合（如 saṅkhata-lakkhaṇa）用“有为相”。

### 4.7 其他易混词
| 词 | 规则 |
|---|---|
| sati / mindfulness | sati 作名称、括注时作 **念**；修习语境（建立/维持正念、正念正知）作 **正念**〔T1〕；sammā-sati 作 **正念**；satipaṭṭhāna 作 **念住/四念住**；动词 be mindful 作“保持正念”可以接受 |
| samādhi / jhāna | samādhi＝**定**（泛称可作“禅定”）；jhāna＝**禅那**；concentration 作心理作用（专注力）时可用“专注” |
| vipassanā | 普通论述用**观**，动作**修观**，明确方法用**观禅**；与止/修止/止禅同层对应。首现可释内观、音译毗婆舍那；语词分析和特定译法引述可保留旧称。vipassanā-ñāṇa＝**观智**，vipassanā-paññā＝**观慧**；一般insight另据句义，不把ñāṇa一概当观智〔m-review-concepts-01〕 |
| samatha | 普通论述**止**，动作**修止**，明确方法**止禅**；首次可释音译奢摩他；与观的对应项同层，技术乘名保留止乘或以止为乘〔m-review-concepts-01〕 |
| taṇhā / upādāna | taṇhā＝**渴爱**（默认）；缘起支、三爱名（欲爱、有爱、无有爱）、戏论三法“爱、慢、见”等紧凑列举中作“爱”；世间语境作“贪爱”或“贪欲”（G3-1）；upādāna＝**取**（缘起支）/**执取**；一般 attachment＝**执着** |
| paññā / ñāṇa / vijjā | **慧/智慧**、**智**、**明** |
| bhāvanā / development | 术语作 **修习**；develop wisdom 作“培育智慧”（不用“开发”） |
| chanda | 广义用**意欲/欲求**，不预设善恶；与渴爱对举、由理解向善的狭义用**善法欲**；四神足、心所等法数保留**欲**并随需要释义；语词分析保留原词。不能把所有chanda判成善或不善〔m-review-concepts-01〕 |
| kattukamyatā-chanda | 定义、解释处作 **欲求行动**（如“欲求行动（kattukamyatā-chanda）”“被定义为欲求行动”）；行文中紧凑处作 **行欲**（如“行欲就是善法欲”“求知欲和行欲”）；不用“行动欲”“作事欲”（B8-r2） |
| bhojane-mattaññutā | **食知节量**（全书统一；人作“食知节量者”）；不用“饮食知量”“食知量”“饮食适量”（B8-r2） |
| kalyāṇamitta | **善友**（不用“善知识”） |
| saddhā | **信**/**信心**；不用“信仰” |
| paramattha | 指真理时作“胜义”（胜义谛）；指利益（paramattha 三利之一）时作“究竟利益” |
| deva / God | **天人**；God＝**上帝** |
| sekha / asekha | **有学 / 无学**；“trainee”不译“学人/受训者” |
| Thai | 指语言＝泰语，指版本＝泰文版 |
| 思惟 / 思维 | 见 T1 确认事项“思惟 / 思维 语义原则” |

---

## 五、已知结构问题（修订时处理）

1. **第一章缺一整节**：中文 `five-aggregates.md` 缺英文的 “Human Life Entails the Functioning of the Five Aggregates” 一节及其 5 个小节（All Phenomena… / The Functioning… Constitutes Life / Vying for Happiness… / A Life Grounded in Wisdom… / Nota Bene），约 67 段，位置在“蕴之间的关系”与“五蕴与五取蕴”之间。需要按英文补译，定稿标题见第二部分。
2. **nav.md**：几乎每个条目都带残留字符“↩”（连标题“目录↩”也有），要全部删除；第二篇误作“生命的怎样的？”；第九、十、十三章的 nav 写法与 h1 不一致。修订后 nav 必须逐字等于各页 h1。
3. **英文源本身的错误**（中文不跟着错）：process-of-life 页 h1 写作 “Part 2”，goal-of-life 页写作 “Part 3”，实为 Section 3、Section 4；Ch.18 “3. Right Mindfulness” 多出编号。
4. **书名副标题不一致**：buddhadhamma.md 的 title 作“自然法则及其对生命的利益”，封面 alt 作“自然的法则与对生活的价值”。定稿统一为 **《佛法：自然法则及其对生命的利益》**。
5. **标题页**：中文 titlepage 只有“佛法 中文版”；英文还有副标题、Downloads、Order Hard Copies 等。是否补齐由用户决定（中文版可以不放订购信息）。
6. **译者前言**：中文多出“英文译者前言/中文译者前言”两小节，属中文版新增，保留。
7. **段落数不一致**：几乎每章中英文的段落块数都不同（例如 law-of-kamma 英文 1128 / 中文 993，nibbana 722/579，calm-and-insight 726/601，faith-and-confidence 360/244，appendix-citta 62/40）。差距一部分来自列表或表格的拆分方式，但也可能有漏译。修订每章时都要逐段对齐检查（见第六部分）。
8. **括号与格式**：半角、全角括号混用；巴利文大小写不统一（Paññatti / paññatti）。

---

## 六、修订流程与检查清单

**每章流程**
1. 用英文 HTML 的段落与中文 md 的段落逐段对齐（脚本可以复用 `bd-audit/blocks.json` 的抽取方法），列出缺失或多出的段落，先补齐。
2. 把标题改成第二部分的“定稿”，同步修改 nav.md。
3. 用 `glossary-final.csv` 的核心词（source=core）做全文替换前的**逐条检索**：每个“现有译法”都要看上下文再改，不要盲目全局替换（尤其是 乐、行、法、定、念、戒 这些单字）。
4. 按第四部分的规则处理语境词：sukha、saṅkhāra、nirodha、sīla、abhiññā、三法印。
5. 检查人名与敬称：尊者在前、称号不加间隔号、辟支佛改为独觉佛、首次出现括注拉丁转写。
6. 检查巴利文括注：只在首次出现时括注，用全角括号，小写，保留变音符号；标题中不出现巴利文。
7. 检查格式：脚注标签、`{{id}}`、图片链接原样保留；行数和空行与修改前一致，除非是在补译。
8. 通读一遍中文，看是否自然流畅；把新发现的术语补进 glossary-final.csv。

**快速检查清单（每章提交前）**
- [ ] 标题格式为“第X部/篇/章：”，与 nav.md 一致，没有巴利文（“心、识、意”附录除外）、没有“↩”和“#”
- [ ] 正文没有未译的尊者名（巴利三藏人名一律译出；现代僧人每章首现“中文（原名）”）
- [ ] 没有：巴利圣典、巴利经典、阿毗达磨、瞋、施设（书名除外）、诸行皆是坏灭法、辟支佛、阿姜·、“X尊者”（敬称后置）、幸福（作 sukha）、观禅、善知识、胜智、尼罗陀、迦摩罗经、实际应用（作标题）
- [ ] sukha、saṅkhāra 的每一处都符合 4.1、4.2
- [ ] 须陀洹、斯陀含、阿那含采用主称；首次或确有说明需要时括注入流者/一来者/不还者。词源/入流概念专论、原典标题等保留意译，不把“首次”误解成此后绝不许解释〔concepts02〕
- [ ] 括号全角，脚注编号连续
- [ ] 中英段落对齐，没有漏译

---

## 七、已决定事项（2026-10-17）
1. sāmisa / nirāmisa-sukha 沿用 **物质之乐 / 非物质之乐**。
2. 第一章缺失的一节需要补译；在修订稿中先插入暂定小标题和“待补译”标记（见 change-log.md）。
3. 中文标题页**不**加英文副标题和下载、订购信息。
4. 编号小标题：Duality/Dualism #1 译作“二元论之一”，其余同类标题依此处理（纲要一 等）。

## v3 确认事项（用户已确认）
- aññā = 究竟智（abhiññā = 证智，二者区分）。
- nirodha：在缘起（此灭故彼灭）和灭谛语境中用“灭”；其他地方一般用“寂灭”。
- 业的果报语境中，“安乐和幸福”类的叠词可作“安乐和快乐”（law-of-kamma.md）。
- issā/macchariya 在心所列表中作“嫉/悭”（按用户第一章译稿）。

## v6 确认事项
- 四神足（iddhipāda）中的 citta 通名作“心”，释为“专心投入”，其所生定称“心定”；五蕴章脚注23与戒行章脚注37采用相同说明（m-review-language-02 M017，取代旧“专注意念”规则）。普通 citta 的其他语境不受此简释限定。
- issā/macchariya 作“嫉/悭”（斜杠改为半角）。

## v7 确认事项

- **Ps. I. 159**：中文保留 `Ps. I. 159`。英文原书此处误作 “Ps. 1. 159”，中文直接采用正确写法（静默更正），不加译注。这是全书唯一与英文引文不逐字一致的已知例外。
- **不加英文括注**：中文正文与脚注中不再用括号附注英文释义，例如“有学者（learners）”“正定（right concentration）”，一律删去括号及英文。英文是写给英文读者的；中文读者需要的是巴利语原词。
  - 巴利语括注保留，例如（sati）（kamma）（Dhammavinaya）。巴利专名后附的英文中心词（ceremony、grove、heaven、meditation、King、Ven. 等）删去，只留巴利语，例如“迦絺那衣仪式（Kaṭhina）”。
  - 以下情况保留英文：（1）现代人名、泰国人名与称号（Tahn Chao Khun、Ajahn 等）；（2）地名、寺院、机构、出版社；（3）英文书名、章名等书目信息；（4）正文讨论的对象就是英文词语本身时，例如 “evil” 的词源、英文 “me/mine” 的局限、美国《独立宣言》的 “pursuit of happiness”。
  - 图片的 alt 文本不属于正文括注，不在本规则范围内。
- **附录4（布施动机）**：三组经文按英文结构分为三个编号列表，每组之后附出处行。“为庄严心、提升心（的品质）而施”是 cittālaṅkāra/cittaparikkhāra 的统一译法。

## B1-r2 确认事项

- **taṇhā：渴爱／爱**，不机械统一，逐处按语境判断：
  - 默认作“渴爱”（一般叙述、单独出现的 craving）。
  - 作“爱”：（1）缘起支及其链式表述，如“缘受有爱”“爱缘取”“受 → 爱 → 取”、经文中缘起逆观问答“……爱才生起？”；（2）三爱名：欲爱、有爱、无有爱（统称可作“三种爱”；附录标题“三种渴爱”保留）；（3）带巴利括注的紧凑列举，尤其戏论三法：爱（taṇhā）、慢（māna）、见（diṭṭhi）；成对术语“爱（taṇhā）和见（diṭṭhi）”（爱依止、见依止）；（4）与固定说法呼应处，如“依爱而断爱”（AN 4.159）。
  - 世间（lokiya）语境中的“贪爱”可以接受：日常欲望、社会与经济讨论等，若“贪爱”读起来更自然，可保留或使用；佛法教义、出世间（lokuttara）语境中优先用“渴爱”或“爱”。不做批量回改；校对中遇到世间语境且“贪爱”明显更好的个案，作为普通编号条目修改。
  - 原译中的“贪爱”，若对应 taṇhā，按上述规则改为“渴爱”或“爱”；若对应 rāga、chanda-rāga、kāma-rāga 或 attachment/liking（常与“嗔恚／嗔恨”成对），保留“贪爱”。
- **paññatti：概念／施设**，选择现代读者最易理解的译法：
  - 一般语境（conventional designations、concepts、labels，如“猫”“桌子”）作“概念”，必要时作“世俗概念”。
  - 阿毗达摩/义注的技术语境与二谛（世俗谛/胜义谛）讨论中作“施设”，并在该处首次出现时释义：施设（paññatti，即概念、名称）。附录二标题“义注对施设的解释”保留。
  - 律学用法（vinaya-paññatti、paññatti-vinaya 等“制定”义）与经名、书名（世间施设、《人施设论》）不在此规则内，维持原译。
- （G3 注：上面 taṇhā、paññatti 两条已由“G3 确认事项”规则 1、6 修订，以 G3 为准。）


## G3 确认事项（第三轮指南，2026-10-18）

以下规则取代前文相应条目，已全书（目录/导航 yml、正文、脚注）逐处按语境执行。

1. **taṇhā：渴爱／爱／贪爱／贪欲**。佛法、出世间（lokuttara）语境优先用“渴爱”或“爱”（缘起支、三爱名、紧凑列举照 B1-r2 用“爱”）；世间语境（日常欲望、教育与育儿、消费与经济、娱乐、性欲等社会讨论）可用“贪爱”或“贪欲”，以原译为准。做法：依据 v1–B2 全部改动记录，先把每一处改成或改离“渴爱/爱/贪爱”的地方恢复原译，再逐处重新决定。例：“仿佛它被贪欲所掩盖或隐藏”用原译“贪欲”。原译“贪爱”对应 rāga、chanda-rāga 等的地方保留。
2. **标准偈**（G4 已改，见下）：vayadhammā saṅkhārā, appamādena sampādetha 原定作“一切有为法皆是坏灭法；当勤精进以证目标。”（经文中的呼格“诸比丘/比丘们”保留，分行偈保留分行）。相关偈 aniccā vata saṅkhārā 同用“有为法”：“确实，一切有为法无常，是生灭法。既已生起，便会止息；其止息是究竟之乐。”
3. **嗔**：dosa 等一律用“嗔”（嗔恚、嗔恨、嗔心、无嗔、嗔行……），取代旧规则“统一用瞋”；已出版作品的书名内照原样（本书目前没有这种情况）。注：用户写的“睹”指“瞋”；“目睹”的“睹”不受影响。
4. **saṅkhāra**：在世间或解释性语境中，可用“有为法”或“行法”（可括注“行”或 saṅkhāra）帮助现代读者理解，但不能歪曲法义。与无为法（asaṅkhata）、涅槃、“一切法”对举时，必须用“有为法”，例如“一切有为法（saṅkhāra）都是无常的……一切法（dhamma）都是无我”“所有有为法……所有法，无论是有为法还是无为法”。以下情况保留“行”：五蕴的行蕴（五蕴并列时作“行”）、缘起支“行”、身行/语行/意行、福行/非福行/不动行；经文固定句（如“诸行寂灭，究竟安乐”“我是针对诸行无常而说的”、Vajirā 偈“诸行的聚合”）也保留。脚注和括注的用词必须与正文一致（如三法印章脚注8“saṅkhāra（有为法）”）。
5. **中文与拉丁字母之间的空格**：见“一、总体原则”。数字的处理〔pt96u 更新，取代 G3 旧款〕：可见中文与数字 0–9 相邻时插入一个 ASCII 空格；已有间隔不重复添加。连续数值如 3.5、1,000、102–103 不拆，年份/序数/计量/金额同样处理。链接显示文字可处理，但目标、紧邻 IAL 属性、锚点/ID、脚注引用/定义标签、front matter、代码、数学和图片语法均保护；出处的实际标识字符不动，只在标识与外部中文的交界加空格。须以实际 Kramdown 文本/结构/属性对等、冻结引用和可逆清单检验，不能只靠原始 Markdown 正则。
6. **paññatti**：更正为“概念”或“概念法”（原译的意思），取消 B1-r2 的“施设”规则；首次出现时可加“（又译“施设”）”（在引号内时写作‘施设’）。B1-r2 和 B2 改成“施设”的地方全部改回，包括标题“附录二：义注对概念的解释”。书名《人施设论》（Puggalapaññatti）与经文“世间施设”（loka-paññatti，原译）不在此规则内。
7. **papañca-saññā**：统一作“戏论想”。描述性译法（“源于不善心戏论的想”）后面补“即戏论想”；“戏论之想”“心想”等改为“戏论想”。
8. **神通／神变／超自然**：iddhi、abhiññā（具体能力）用“神通”；pāṭihāriya（包括 iddhi-pāṭihāriya）用“神变”（“神通神变”照旧）；六神通列举中的 iddhividhā 用“神足通”，指“展现神变”这一行为时可用“神变（iddhi-vidhā）”；“超自然”只用于世间语境（依赖超自然力量、超自然实体或现象、神力干预），保留。现状（G3 后）：神通 335、神变 56、超自然 21（全部为世间语境）。
9. **人名**：Sāriputta 一律作“（尊者）舍利弗”，不留拉丁转写的原文名（首次出现时的括注除外）。

**B2 待定事项的决定**：书名页不补“下载/订购”两节；补译版权与联系信息（措辞与 copyright.md 一致）；缩写表不加 SC 栏，但补入律藏细分 10 行（Pj、Ss、Ay、Np、Pc、Pd、Sk、Bi Pc、Kd、Pvr）；“中文译者前言”和 B2-244～248 增译保留不动；书名页 h1 与作者行、塔纳普拉／坤·斯里詹·比罗姆巴克迪、“梵”、“圣者之律”已获认可。

## G4 确认事项（第四轮指南，2026-10-18）

1. **尊者名字**：见 1.3 新增两条。巴利三藏人名一律译出；后期论师与现代僧人在每个章节文件第一次出现时写成“中文（原名）”，敬称在前（`尊者那拉达（U Narada）`）。“只有阿姜不加间隔号”的规则不变。G4 全书已执行（正文、脚注、书目、前后附文）。目录和导航中没有未译的人名。
2. **标准偈（取代 G3-2）**：vayadhammā saṅkhārā, appamādena sampādetha 统一作“**一切有为法皆是坏灭法，当不放逸以成道业**”（中间是全角逗号，不是分号）；经文中的呼格（诸比丘/比丘们）和分行偈的分行保留。aniccā vata saṅkhārā 偈不含这句，维持 G3 的写法。
3. **“心、识、意”附录**：标题恢复原形“附录：心（Citta）、识（Viññāṇa）、意（Mano）”（h1、页面 title、nav.md、导航 yml 一致）；小标题对照英文恢复或补上巴利括注；属于“标题不放巴利文”规则的例外（见 1.1）。正文核对后，没有发现前几轮删去的巴利括注；也没有漏译（中英比例低，是因为英文把引文拆成 20 多个单独段落，并有巴利原文行）。
4. **词表**：glossary-final.csv 与指南全部决定同步（见 G4 审阅表“词表变更”一节）。
5. **书目**：《附件》（Parivāra）→《附随》。

## G5 确认事项（第五轮指南，2026-10-18，用户已确认）
- 规则1：“帕”“颂德”“隆波”作僧衔时后面保留间隔号（见 1.3）；颂德·帕·菩陀构萨迦利雅等 13 处修正。帕古→帕·古（Phra Kru）为判断项。
- 规则2：巴利三藏人名、地名、天神名在中文行文中一律译出（见 1.3）；Vacchagotta 定为“婆蹉衢多”，全书统一（含 G4 已改的 8 处）。
- 遗留待定：Āḷāra Kālāma 书中有“阿罗罗·迦罗摩”（3 处）与“阿罗逻·迦蓝”（happiness 1 处）两种写法；Māgaṇḍiya 有“摩犍提”（happiness，游方者）与“玛干帝亚”（virtuous-friendship，《经集》婆罗门）两种写法（可能不是同一人）。本轮未统一。

## G6 确认事项（第六轮指南，2026-10-18，用户已确认）
- 书名统一（义注、复注、论书）：以参考文献（bibliography.md）的译名为标准，参考文献本身明显误译的一并改正；全书正文、脚注、缩写表、参考文献一致。正文中单独出现的拉丁书名（Visuddhimagga、Paṭisambhidāmagga、Cūḷaniddesa 等）译成中文，出处缩写和纯引文标签（如 Saṅganī Mūlaṭīkā、Maṅgalatthadīpanī [1/210-19]）保留原文。书名后的原名括注一律用全角括号。

| 巴利书名 | 标准译名 | 已替换的异译 |
|---|---|---|
| Abhidhammatthasaṅgaha（Comp.） | 《摄阿毗达摩义论》 | 阿毗达摩义广释（书目误）、阿毗达摩义集、阿毗达摩义摄论、阿毗达摩概要、摄阿毗达摩义；复注 CompṬ.＝《摄阿毗达摩义论复注》 |
| Abhidhammatthavibhāvinī | 《阿毗达摩义广释》 | 阿毗达摩义灯、阿毗达摩义广释复注（另一部书，不并入 Saṅgaha） |
| Pañcikā (Abhidhammatthavibhāvinī-atthayojanā) | 《阿毗达摩义广释注解》 | 五部义注（书目误） |
| Paramatthadīpanī（Ud/It/Vv/Pv/Th/Thī/Cp 义注、五部论注） | 《胜义灯》 | 胜义显露 |
| Paramatthamañjūsā（VismṬ.） | 《胜义宝函》；描述性名称《清净道论大复注》 | 最胜义灯大疏钞（书目误）、究竟义要义、究竟义疏、胜义谛精义注、胜义灯（误）、清净道论大疏钞 |
| Sammohavinodanī（VbhA.） | 《破除痴迷》 | 迷惑根除论、困惑破除、迷惑断 |
| Saddhammappakāsinī（PsA.） | 《正法显明》 | 显正法论、正法开示 |
| Manorathapūraṇī（AA.） | 《满足希望》 | 满足希求论、满足希望者 |
| Papañcasūdanī（MA.） | 《破除障碍》 | 满足希求论（误）、中部注 |
| Paramatthajotikā（KhA./SnA.） | 《胜义之光》 | 胜义光明 |
| Atthasālinī（DhsA.） | 《显义》 | 法集论释 |
| Nettipakaraṇa | 《导论》 | 摄义论（书目）、奈迪巴加拉那、义释（误）；Nettivibhāvinī＝《导论广释》 |
| Peṭakopadesa | 《藏释》 | 彼得哥巴德萨、巴利藏指南 |
| Maṅgalatthadīpanī | 《吉祥义灯》 | 吉祥经义注 |
| Abhidhānappadīpikā | 《名义灯》 | 阿毗达摩论典释（误）、词典 |
| Milindapañha | 《弥兰王问经》（G7 改定） | 弥兰陀问经、弥兰陀王问经 |
| Dhātukathā / Yamaka | 《界论》/《双论》 | 界说论 / 双对论 |
| Samantapāsādikā | 《善见律毗婆沙》 | 善见律注 |
| Vimativinodanī | 《除疑律疏》 | （正文原名未译） |
| Mahāniddesa / Cūḷaniddesa | 《大义释》/《小义释》 | （正文原名未译）；Cūḷaniddesa Aṭṭhakathā＝《小义释义注》，不作“小部义注” |
| 描述性义注名 | “X义注”“X复注”：《长部义注》《法句经义注》《分别论义注》《经集义注》《增支部义注》《无碍解道义注》《律藏义注复注》 | 长部注、法句经注、分别论注、经集注、增支部注、无碍解道释、律藏复注 |

- 例外（用户决定）：Abhidhammatthasaṅgaha 一律《摄阿毗达摩义论》；参考文献原作《阿毗达摩义广释》是把 Abhidhammatthavibhāvinī 的译名套错了，“义广释”专指 Vibhāvinī。
- Nettipakaraṇa 不从参考文献的《摄义论》（易与《摄阿毗达摩义论》混淆），改从缩写表与正文通用的《导论》。
- 人名：Subha＝须婆（保留）；Puṇṇa Koliyaputta（MN 57）＝富楼那·拘利子，在首次称呼处标出全名，与说法第一的富楼那（Mantāniputta）区别；Āḷāra Kālāma＝阿罗罗·迦罗摩；Māgaṇḍiya＝摩犍提（经名《摩犍提经》，取代“玛干帝亚”“摩犍提耶经”）；Udāyī＝优陀夷（取代“乌陀夷”）；Kālāma（族人）＝卡拉玛人，经名《卡拉玛经》（取代“迦拉玛人”“伽蓝人”）；Sedaka Sutta＝《私达迦经》；Phra Kru＝帕·古。
- Pali Canon＝《巴利三藏》，Tipiṭaka＝三藏（“巴利语圣典”不再使用）；“巴利圣典协会”（Pali Text Society）保留。
- 小标题 Kamma in the Context of Conventional Laws＝“世俗法中的业”。
- 待以后批次：参考文献中“觉音阿阇梨尊者”（16 处）未在 G6 改动，留给参考文献批次按 G4 人名规则处理。


## G7 确认事项（第七轮指南，2026-10-18，用户已确认）
- B5 决定（用户已确认）：Vessantara＝维桑塔拉；Dabba Mallaputta＝尊者陀骠·摩罗子（含 awakened-beings）；Kesaputta＝羁舍子（取代“拘萨城”）；Nettipakaraṇa＝《导论》、Abhidhānappadīpikā＝《名义灯》保留；英文单独成段的“**”在中文中也单独成行；goal-of-life 偈注“须陀洹果”保留；“比丘们/诸比丘”不统一。
- **无余依涅槃 / 无取般涅槃**：anupādisesa-nibbāna（-dhātu）＝无余依涅槃（界），anupādisesa-puggala＝无余依者；anupādā-parinibbāna（MN 24“为无取般涅槃而修梵行”、Pvr 14，英文 final, absolute Nibbāna / final Nibbāna without fuel）＝**无取般涅槃**。两者是不同的词，不互换。不改作“无执取般涅槃”：附录五（英文 Appendix 5）明说有些老师把它解作“无执取（upādāna）的般涅槃”，而义注驳斥此说、把 upādā 解作“燃料、缘”（appaccaya-parinibbāna）；“无取”保留了 upādā 的两义，“无执取”会让附录五的论述自相矛盾。英文只写 final, absolute Nibbāna 而括注 anupādā-parinibbāna 时，译“究竟、绝对的涅槃——无取般涅槃（anupādā-parinibbāna）”。
- **最后心 / 临终心 / 死心**：carima-citta、carimaka-citta（阿罗汉般涅槃时的最后之心，英文 final mind / last mind）＝**最后心**，carima-viññāṇa＝**最后识**；maraṇāsanna-citta（临死时的心）＝临终心；cuti-citta＝死心。按每处的巴利/英文判定。本书英文中的 final mind 全部是 carima-citta（附录三及其引文），没有 maraṇāsanna-citta；一般叙述的 at the moment / time of death 仍作“临终时”。
- **Milindapañha＝《弥兰王问经》**（用户决定，与 1.1 一致，取代 G6 表中的《弥兰陀问经》）；国王名 Milinda＝弥兰陀王。
- **篇名问句体**（沿用泰文版）：第一篇：生命是什么？／第二篇：生命是怎样的？／第三篇：生命如何运作？／第四篇：生命应成为什么？／第五篇：生命应如何度过？／第六篇：美好的生命是怎样的？／第七篇：道支（英文 Path Factors 非问句，指南标题表已定，保留）。正文中提到篇名（如第十九章的两份目录、六处章脚注）一律用这些篇名；英文 A Noble Life＝“生命应如何度过？”，A Worthy Life＝“美好的生命是怎样的？”。各章章名英文都不是问句，照标题表。页面 title、h1、nav.md、导航 yml 四处必须逐字相同（nav.md 标题页条目“佛法”沿用英文导航的短名，见待定）。

## G8 确认事项（第八轮指南，2026-10-19；人名、地名凡与下文 G10/G11“人名与地名译名表”冲突者，以该表为准）
- B6 建议（用户已确认）：附录二 bhāvita-kāya / -sīla / -citta / -paññā＝身的修习圆满 / 戒的修习圆满 / 心的修习圆满 / 慧的修习圆满（正文作“戒行的修习圆满”“智慧的修习圆满”）；bhāvitindriya＝已修习诸根；diṭṭhi-sampanna＝具足正见者；附录一 sīla / vata / parāmāsa＝戒 / 禁 / 取（不用尸罗、瓦塔、帕拉玛萨音译）；Khemaka＝差摩迦；Vassakāra＝雨行；Lakuṇṭaka Bhaddiya＝罗婆那跋提。B6-198：awakened-beings“有描述涅槃为安乐的术语”（总括语，一般 sukha），“至上安乐”只用于 paramaṁ sukhaṁ。
- **人名规则（新）**：经典中的人名、地名、天神、族姓及含人名的经名，凡现用现代音译者，一律改用传统通行的汉译名。依据次序：汉译《阿含》《律》《论》→ 元亨寺《汉译南传大藏经》→ 萧式球、庄春江译本 → 叶均译本 → 《佛光大辞典》《丁福保佛学大辞典》。只有找不到传统译名时才保留现代音译。现代人物（泰、缅、西方）不受此规则影响。
- G8 译名表（巴利 → 定译；不用：旧译）：
  - Aggivessana（萨遮迦的族姓）＝火种（不用：阿吉维萨那）
  - Aggivessana（萨遮迦的族姓）＝火种（不用：阿耆毗舍那）
  - Pārāsariya＝婆罗门波罗奢那（不用：婆罗门波罗萨利耶）
  - Pārāsariya＝波罗奢那（不用：波罗萨利耶）
  - Uttara（波罗奢那的弟子）＝郁多罗（不用：优陀罗）
  - Byagghapajja＝虎路（不用：彪伽帕阇）
  - Dīghajāṇu＝长膝（不用：迪迦阇努）
  - Dīghajāṇu＝长膝（不用：帝伽贾努）
  - Koliya＝拘利人（不用：伽梨人）
  - Bāhiya Dārucīriya＝木皮衣婆醯迦（不用：跋希亚·达鲁契利耶） ⚑
  - Cakkhupāla＝护眼（不用：迦库帕拉） ⚑
  - Ciñcā-māṇavikā＝旃遮摩那祇（不用：差摩那维迦）
  - Cunda＝银匠纯陀（Cunda）（不用：银匠准达（Cunda））
  - Cunda＝纯陀（不用：准达）
  - Dhanapāla(ka)＝护财（不用：达那巴拉）
  - Isidatta＝梨师达多（不用：伊西达塔）
  - Purāṇa＝富兰那（不用：富拉那）
  - Kevaddha Sutta（DN 11）＝《坚固经》（不用：《哥伐陀经》） ⚑
  - Kevaddha＝坚固（不用：哥伐陀） ⚑
  - Khujjuttarā＝久寿多罗（不用：库珠塔拉）
  - Kosiya＝憍尸迦（Kosiya）（不用：高沙（Kosiya））
  - Macchariya Kosiya＝悭吝憍尸迦（不用：麻沙利亚·高西雅）
  - Kuṇḍadhāna＝军头波汉（不用：昆达达那）
  - Kālāma Sutta＝《伽蓝经》（不用：《卡拉玛经》） ⚑ 〔已被 G10 取代：卡拉玛人、《卡拉玛经》〕
  - Kālāma＝伽蓝人（不用：卡拉玛人） ⚑ 〔已被 G10 取代：卡拉玛人、《卡拉玛经》〕
  - Mahānāma＝摩诃男（不用：马哈那马）
  - Mahākappina＝大劫宾那（不用：摩诃迦毗那）
  - Mahākassapa＝大迦叶（不用：摩诃迦叶）
  - Māluṅkyaputta＝鬘童子（不用：马鲁迦子）
  - Māluṅkyaputta＝鬘童子（不用：摩伦迦弗达）
  - Meghiya＝弥醯（不用：弥希亚）
  - Migasālā＝鹿住（不用：弥迦萨拉） ⚑
  - Nakulamātā＝那拘罗母（不用：纳库拉玛塔）
  - Nakulapitā＝那拘罗父（不用：纳库拉比达）
  - Narada＝那罗陀长老（Narada Thera）（不用：长老那烂陀（Narada Thera））
  - Piṇḍola Bhāradvāja＝宾头卢·颇罗堕（不用：宾度罗跋啰堕阇）
  - Piṇḍola Bhāradvāja＝宾头卢·颇罗堕（不用：宾度拉·巴拉度瓦迦）
  - Pilindavaccha＝毕陵伽婆蹉（不用：毕陵伽·婆蹉）
  - Potaliputta＝哺罗陀子（不用：波多利布达）
  - Pāvā＝波婆（Pāvā）（不用：波伐（Pāvā））
  - Rohaṇa（那先的师父）＝楼汉（不用：罗哈那）
  - Rohitassa＝赤马（不用：卢奚多萨）
  - Samiddhi＝三弥提（不用：萨密提）
  - Samiddhi＝三弥提（Samiddhi）（不用：沙弥（Samiddhi））
  - Selā＝尸罗比丘尼（不用：舍拉比丘尼）
  - Seniya＝先尼（不用：塞尼耶） ⚑
  - Siṁsapā＝申恕（不用：辛沙巴）
  - Soṇa＝二十亿耳（不用：索那）
  - Soṇa Koḷivisa＝二十亿耳（不用：娑那·拘利维萨）
  - Soṇa Kuṭikaṇṇa＝亿耳（不用：娑那·拘帝迦那）
  - Subha＝须婆（不用：苏跋）
  - Sudhamma（质多长者故事中的比丘）＝善法（不用：苏达摩） ⚑
  - Moḷiya Sīvaka＝尸婆（不用：西瓦卡）
  - Moḷiya Sīvaka＝尸婆（不用：西瓦迦）
  - Tapussa＝帝梨富娑（不用：塔普萨） ⚑
  - Vajirā＝金刚比丘尼（Vajirā）（不用：比丘尼瓦吉拉（Vajirā））
  - Vakkali＝跋迦梨（不用：瓦卡利）
  - Vakkali＝跋迦梨（不用：跋伽利）
  - Vakkali＝跋迦梨（不用：跋迦利）
  - Vassakāra＝雨行（不用：跋沙迦罗）
  - Vassakāra＝雨行（不用：婆悉迦罗）
  - Khemaka＝差摩迦（不用：奢摩迦）
  - Kakusandha＝拘留孙（不用：迦俱散陀）
  - Kakusandha＝拘留孙（不用：迦俱孙陀）
  - Bimbisāra＝频婆娑罗（不用：频毗娑罗）
  - Nigaṇṭha Nātaputta＝尼乾陀·若提子（不用：尼干陀·那陀子）
  - Nigaṇṭha＝尼乾陀（不用：尼干陀）
  - Nigaṇṭha＝尼乾子（不用：尼干子）
  - Baka＝婆迦（Baka）（不用：婆伽（Baka））
  - Baka＝婆迦（Baka）（不用：跋迦（Baka））
  - Susima＝须深（不用：须深摩）
  - Susima＝《须深经》（不用：《须西马经》）
  - Mahāpanthaka＝摩诃槃陀伽（不用：大盘特迦）
  - Cūḷapanthaka＝周利槃陀伽（不用：周利盘特迦）
  - Hatthaka of Āḷavī＝阿罗毗的手长者（不用：哈达卡·阿拉瓦卡居士）
  - Hatthaka of Āḷavī＝手长者（不用：哈达卡居士）
  - Lakuṇṭaka Bhaddiya＝罗婆那跋提（不用：拉孔塔卡·巴迪亚）
  - Saviṭṭha＝殊胜（不用：萨威陀）
  - Kakutthā＝拘孙河（不用：伽窟他河）
  - Dīghāvu＝长生（不用：迪伽乌）
  - Suvaṇṇasāma＝睒子（不用：苏梵纳萨马）
  - Abhayarājakumāra＝无畏（Abhaya）王子（不用：阿跋耶（Abhaya）王子）
  - Saṅkicca＝僧吉蔗（不用：僧吉迦）
  - Bhaddiya Sutta＝《跋提经》（不用：《巴蒂亚经》）
  - —＝Kesaputta Sutta、Kesaputti Sutta、Kesaputtiya Sutta 或 Kesamutti Sutta（不用：《揭沙弗经》、《揭沙普提经》、《揭沙普提雅经》或《揭萨穆蒂经》）
  - Pāsarāsi Sutta＝《圣求经》（Pāsarāsi Sutta）（不用：《帕沙拉西经》（Pāsarāsi Sutta））
  - Kīṭāgiri Sutta＝《翅吒山经》（不用：《基塔吉利经》）
  - Kūṭadanta Sutta＝《究罗檀头经》（不用：《瞿昙达那经》）
  - Gosiṅgasāla Sutta＝《牛角娑罗林经》（不用：《高辛萨拉经》）
  - Mandhātu＝《顶生王本生经》（不用：《曼陀度罗阇本生经》）
  - Siṅgālaka Sutta＝《善生经》（不用：《施伽罗经》）
  - Saṅgīti Sutta＝《众集经》（不用：《僧伽提经》）
  - Anupada Sutta＝《无间经》（不用：《阿那巴经》）
- 保留现代音译（无传统通行译名或待决定）：
  - Jāli / Kaṇhājinā / Maddī：贾利 / 甘哈 / 玛迪——保留（待决定）：传统《太子须大拏经》作 耶利 / 罽拏延 / 曼坻，但用户已定 Vessantara＝维桑塔拉，三名需与之配套
  - Mettagū：梅达古——保留⚑：《经集·彼岸道品》学童名，未找到通行古译
  - Senānigāma：斯那尼村——保留⚑：古译“斯那尼”与音译相同；《方广大庄严经》作“斯那耶那”不通行
  - Vajjiyamāhita：伐耆耶摩希达——保留⚑：《杂阿含》对应经未见
  - Sirimaṇḍa：尸利曼陀——保留⚑：“尸利”为传统音节，无更通行古译
  - Kakkarapatta：喀卡拉巴塔——保留⚑：庄春江意译未核实
  - Upasena Vaṅgantaputta / Sobhita：优波先那·瓦刚塔普塔 / 娑比塔——保留⚑：古译对应不确定
  - Kusa / Maṇḍavya：古萨 / 曼达维亚——保留⚑：本生故事人物，无通行古译
  - Sāḷha Sutta / Sedaka：《萨拉经》/《私达迦经》——保留⚑
  - MN 7 河名 Bāhukā 等：巴胡卡、阿地卡卡、巴胡马提、跋亚迦、萨拉萨提、孙陀利卡——保留：《中阿含·水净梵志经》河名与巴利本不对应
  - Dhammadinnā：法施——保留：已是传统译名（《增一阿含》“法施比丘尼”）
  - 现代人物（泰/缅/西方）：———不受本规则影响

## B9 确认事项（第十一章 安乐，2026-10-19，用户已确认；brahmavihāra 一项见 B10-r2：四梵住）
- 术语（按 4.1 执行到第十一章全章）：sense pleasure / sensual pleasure＝**欲乐**（不用感官之乐、感官享乐、感官欲乐；定稿标题“智慧地受用感官之乐”保留）；kāma-guṇa＝**五欲**／**五欲乐味**（按语境；T1-r2 不再保留“五欲功德”）；sensuality / sense desire＝**欲**；初禅定型句 secluded from sensual pleasures＝**远离欲**。
- happiness of jhāna / jhāna-sukha＝**禅那之乐**；“禅悦”只保留在不带括注的修辞句（全章仅 1 处）。supreme happiness＝**至上安乐**；perfect happiness＝**圆满安乐**；“究竟安乐”只保留在定稿标题“佛陀的究竟安乐”和法句偈译文中。
- 喜悦五支：pāmojja＝**悦**、pīti＝**喜**、passaddhi＝**轻安**、sukha＝**乐**、samādhi＝**定**（全章一致）。
- brahmavihāra（四者合称）＝**四梵住**（B9 原译；B9-r2 曾改为“四无量心”，B10-r2 用户决定恢复“四梵住”），列举作“慈、悲、喜、舍”；muditā＝喜／喜心；非列举的 lovingkindness／compassion＝慈心／悲心。saṅgaha-vatthu＝**四摄法**（布施、爱语、利行、同事）；sārāṇīya-dhamma＝“六和敬法”。
- upadhi-sukha／nirupadhi-sukha＝**有依之乐／无依之乐**（“有漏／无漏之乐”专用于 sāsava／anāsava）。
- āsava＝漏；assāda＝乐味；craving＝渴爱（不用贪爱）；stream-enterer＝须陀洹（不用入流者）；wholesome enthusiasm＝善法欲；非修行语境 development＝发展。
- 中文多出的“法喜”（英文为 happiness／joy／rapture）一律按英文改回，列为增译。

## B9-r2 确认事项（2026-10-19；brahmavihāra 一项已被 B10-r2 取代，以下第一、二条作废）
- brahmavihāra（慈、悲、喜、舍四者合称）全书一律作**四无量心**；“四梵住”不用（已全书替换）。指称其中若干项作“无量心”（如“其他三种无量心”“前三种无量心”“这些无量心”）；单项作“X无量心”（如舍无量心 upekkhā-brahmavihāra、慈无量心）。巴利括注一律保留。
- 例外（保留“梵住”）：（1）经文中把某种定称为 brahma-vihāra 的固定说法（如 SN 54.11 安般念定“是圣者之住、是梵住、是如来之住”）；（2）原文专门区分 appamaññā 与 brahmavihāra 两个巴利名的地方，“梵住”是名称本身，加引号作四“梵住”（path-factors-of-concentration 1404、1531、2272、注 173）。
- B9 中“有依之乐／无依之乐”、pāmojja＝悦、删“法喜”、七宝译名、“禅悦”只用于修辞句、kāma-guṇa 作“五欲／五欲乐味”（T1-r2 取代“保留五欲功德”），其余均已确认。B9 遗留排版项（726 行偈颂合并、1603–1604 行硬换行）移入 plan.md 遗留清单的排版轮处理。

## B10 确认事项（中道导论、善友、信心，2026-10-19，用户已确认；puñña 一项见 B10-r2）
- puñña-kiriyā / puññakiriyā-vatthu＝**福业 / 福业事**（三福业事、十福业事）；不用“功德行”“功德善业”“功德行处”“十种功德基础”。章节标题“居士通过修习福业事来实践道”。单独的 puñña 仍作“功德”（未改，待定）。
- pattidāna / pattānumodanā＝分享功德 / 随喜功德（“回向”为备选，待定）。〔T1 已定：pattidāna＝回向功德〕
- mind＝**心**（不用“心识”，viññāṇa 除外）；strength＝力量（不用“精进”）；spiritual faculties（indriya）＝根器 / 诸根；kamma 在正文中作“业”。
- training（sikkhā）＝**学**（三学、增上戒学等；“学处”专指 sikkhāpada）；gihi-vinaya＝居士律。
- sammā-ñāṇa＝正智；knowledge and vision（ñāṇadassana）＝智见；“解脱知见”（vimuttiñāṇadassana）沿用传统译名不改。
- sammatta＝十正性；asekha-dhamma＝十无学法；nāthakaraṇa-dhamma＝带来保护的美德；sotāpattiyaṅga＝（四）入流支。
- sorrow, lamentation, pain, grief, despair＝愁、悲、苦、忧、恼（全书标准）。
- boundless mind（vimariyādikatena cetasā）＝无限心（与 happiness 一致；不用“无量心”，以免与 appamaññā“四无量心”混淆）。
- wise reflection＝如理作意（包括附注标题“三种如理作意”；不用“智慧反思”）。
- transcendent right view＝出世间正见；mundane＝世间（不用“世俗”“超越的”）。
- Paṭisambhidāmagga＝《无碍解道》（不用《分别道论》）。
- 《卡拉玛经》十项：“Do not believe on the basis of …”＝“不要因……而相信”（原译“不要被……所引导”与紧接的附注讨论“不相信”一词矛盾）；附录一的“Be not led by”仍作“不要被……引导”。
- 附注引用格式统一为（参见附注“…”）；Pali 括注一律小写；脚注中文句内出处分隔用全角“；”。
- saṅgaha-vatthu＝**四摄事**（B10-r2 全书统一，见下）。

## B10-r2 确认事项（2026-10-19，用户决定）
- **brahmavihāra＝四梵住 / 梵住**（用户决定恢复 B9 译法，取代 B9-r2 的“四无量心”）。四者合称作“四梵住”；泛指或复数作“梵住”“这些梵住”“前三种梵住”“其他三种梵住”；单项作“慈梵住”“舍梵住”（巴利为 mettā-/upekkhā-brahmavihāra 时）。经文固定说法（如安般念定“是梵住”）照旧。
- **appamaññā＝四无量心**（英文 unbounded states of mind）：只用于巴利为 appamaññā 的地方；两名对举时作“四无量心（appamaññā）——亦即四梵住（brahmavihāra）”，或先列“四无量心（appamaññā）”再说“这些境界最常被称为四梵住（brahmavihāra）”。不用引号。
- boundless mind（vimariyādikatena cetasā）＝无限心，不作“无量心”。
- **saṅgaha-vatthu＝四摄事**（全书统一，不用“四摄法”）；四项为布施（dāna）、爱语（piyavācā / piya-vācā）、利行（atthacariyā）、同事（samānattatā）。
- **puñña** 单独出现作“功德”；“福”只用于福业 / 福业事（三福业事、十福业事）。pattidāna＝分享功德；pattānumodanā＝随喜功德。〔已被 T1 取代：puñña＝福德〕
- B10-r2b 补正（2026-10-21）：law-of-kamma 中 puñña 的定义部分（原作“福（puñña）”“福德”“非福”“福尽死”“福法”）全部改作“功德”；非 puñña 的 blessings / fruit 不再用“福德”“福报”，按英文作利益、福祉、果报、美好、恩赐。固定复合词“福行／非福行”（puññābhisaṅkhāra / apuññābhisaṅkhāra）与“福田”（puññakkhetta）为传统译名，暂保留，待用户决定。〔puñña 部分已被 T1 取代〕
- B10 全部建议已确认；排版遗留项推迟到排版轮（见 plan.md 九）。

## B11 确认事项（第十五章 如理作意，2026-10-21，用户 2026-10-25 确认，T1 复审修订）
- **think / thinking / thought（一般意义）＝思惟／思考／思维，不译“作意”**；“作意”只对应 manasikāra（yoniso-manasikāra＝如理作意，ayoniso-manasikāra＝不如理作意）。本章原译常把 think 译成“作意”（32 处已改）。〔T1 复审：凡英文 reflection 指本章的 manasikāra 方法（“作意的善巧”“这种作意”“第九种作意”）仍作“作意”，部分 B11 改动已回退〕
- yoniso paṭisaṅkhā / paccavekkhaṇa＝**如理省察**〔T1 修订，取代“以智慧思惟”〕；注 47 区分它与 yoniso-manasikāra（如理作意）。
- 本章十种作意的小标题保持定稿措辞（目录保留清单）；正文中各类作意与小标题一致：依共相的作意（sāmañña-lakkhaṇa＝共相）、思惟乐味（assāda）、过患（ādīnava）与出离（nissaraṇa）的作意、真实价值与虚假价值（true and counterfeit value）、激发善法的作意、分别说（vibhajja-vāda）等。
- 正文中英文用英文术语加巴利括注的地方，中文要译出术语（如渴爱（taṇhā）、无明、缘起、禅定成就），不留拉丁原文（9 处）。
- reflection on the repulsive（paṭikkūla-manasikāra）＝厌逆作意；rag-robes＝粪扫衣；dhutaṅga＝头陀支；divine abiding of lovingkindness＝慈梵住（B10-r2）。
- 继续沿用：sati＝念/正念（按语境，见 T1）；sense pleasure＝欲乐；faith＝信心；idappaccayatā＝此缘性；sappurisa＝正人；sotāpattiyaṅga＝四入流支；vimuttiñāṇadassana＝解脱知见；mind＝心。

## T1 确认事项（puñña / manasikāra 全书修订，2026-10-25，用户已确认）

**原则**：逐条按上下文和英文、巴利原义选词，不做机械替换。下表为各词的用法与例句。

| 词 | 用于 | 例句（书中） | 不用于 |
|---|---|---|---|
| 福德 | puñña 本身（世间善及其力量）；术语讨论 | 福德（puñña）；“福德是安乐之名”；有依福德；福德之海 | guṇa（品质） |
| 积累福德 | accumulate / make merit（书面） | 还俗以便花费财富和积累福德；积累福德或获得祝福 | — |
| 行善积福 | perform meritorious deeds（口语、劝导） | 布施、行善积福、持戒；将行善积福视为一种牟利形式 | — |
| 修福 | 偈颂、精炼语 | 智者赞扬精勤修福 | — |
| 行福德之事 / 福德善事 / 福德善行 | meritorious deed(s) | ‘让我行福德之事’，他却行了非福之事 | — |
| 做功德 | 经文/泰国习俗口语的引述 | “做功德”（书中原引述）；为已故者做功德 | 术语定义 |
| 福报 | fruit / result of merit（自然处） | 供养佛陀的布施在两次场合下福报特别大 | 一般 benefit |
| 福业 / 福业事 / 福行 / 福尽死 / 非福 / 福德法 | 固定术语 | 十福业事；福行（puññābhisaṅkhāra）；“非福”（apuñña） | — |
| 回向功德 / 功德回向 | pattidāna；向天人/亡者回向 | 回向功德（pattidāna）；向天人回向功德 | — |
| 分享 | 实为“分享”义处 | 他会与他们分享这份功德 | 名称 pattidāna |
| 随喜功德 | pattānumodanā | — | — |
| 布施功德、持戒功德 … （Q4=b） | 十福业事标签保留 | 布施功德（dāna-maya）：通过给予获得的福德 | “获得的功德”→“获得的福德” |
| 属于福德分 | puññabhāgiya（bhāga＝分） | 属于福德分、在五取蕴方面结果 | “有福分的”（口语义偏“幸运”） |
| 功德 | guṇa：佛、三宝、圣者的功德；入定、成就的功德；anisaṁsa 固定标题 | 佛的功德；所具备的功德；出离的功德 | puñña |
| 品质 | 可培育的一般 qualities（信戒闻施慧、领导者应有） | 这五种品质——闻、信、戒、施、慧 | 佛、圣者的功德 |
| 德行 | 个人 virtue | 对自己德行和努力的信心 | — |
| 恩德 | 父母之恩 | 父母恩德 | — |
| 利益 / 好处 / 优点 | benefits / merits(=advantages) | 称赞独居的好处；优点和害处 | — |
| 乐味 | assāda（经文三支） | 乐味、过患和出离 | 已定稿标题 |
| 五欲 / 五欲乐味 | kāma-guṇa：列举五境用“五欲”；强调其乐味用“五欲乐味”；不再保留“五欲功德”（T1-r2） | 享受五欲（kāma-guṇa）；依赖这五欲而生起的乐……乐味 | 五欲功德 |
| 思惟 | 佛法修习的 reflect / contemplate；saṅkappa；cintā；“X 的思惟方式/形式”指本章的省思方法 | 正思惟；思惟（cintā）；如理思惟法义 | 一般 thinking |
| 思维 | 一般认知：thinking / thought process / way of thinking；逻辑、批判、抽象思维 | 迎合渴爱的思维过程；思维方式 | 佛法术语 |
| 思考 | 一般 think（动词） | 善于思考 | — |
| 作意 | manasikāra；本章 reflection 指作意方法 | 作意的善巧；第九种作意；如理作意 | 一般 think |
| 省思 | 一般佛法语境的 reflect（非术语） | 省思、思量和洞察 | — |
| 省察 | paccavekkhaṇa；yoniso paṭisaṅkhā＝如理省察 | 如理省察，使用袈裟；省察智 | — |
| 审察 | atthupaparikkhā | 审察其义 | — |
| 寻 | vitakka | 寻（vitakka） | — |
| 念 / 正念 | 名称、括注作“念（sati）”；修习语境作“正念” | 建立正念；正念和正知 | — |

- **思惟 / 思维 语义原则**：看英文和所指——指佛法修习中的思惟、观察（reflection / contemplation，以及 saṅkappa、cintā）用“思惟”；指一般心理活动（thinking、thought process、way of thinking、思维能力）用“思维”。“思惟”是汉传佛典的写法，“思维”是现代通用写法；以“是否为修习方法或佛法术语”为界。全书已据此重扫（T1 改 21 处，其余原用法符合原则）。
- 目录保留清单中的“所具备的功德”“已断除的烦恼与证果的功德”“有助于修行的思惟”不改。“安乐的功德与过患”已于 T1-r3 改为“乐味与过患”，呼应句同步；其余保留清单标题不改。
- Q4＝b：布施功德等标签保留，释义中“获得的功德”改“获得的福德”。
- B11 复审：sati 修习语境回退为“正念”；本章 reflection（manasikāra 方法）回退为“作意”；一般 thinking 的 B11 改动保留。
- **T1-r2（2026-10-27，用户确认剩余项）**：
  - 标题“安乐的功德与过患”→**乐味与过患**（T1-r3；用户认定“安乐的乐味与过患”不顺）；正文呼应句同步为乐味与过患；目录对照表已改。
  - kāma-guṇa：列举五境＝**五欲**；强调乐味＝**五欲乐味**；happiness 600/602/2438 的“五欲功德”已改“五欲”。
  - faith-and-confidence 291/316 保留“如理思惟”；经文/口语“做功德”保留。
  - wise-reflection 253 图题“两种思惟”→“两种思维方式”。
  - “戒功德”→**持戒功德**（introduction-to-the-middle-way 526）。

## 人名与地名译名表（G10/G11，2026-10-19，用户已确认；取代 G9 版）

**适用范围**：正文、脚注、参考文献、目录/导航中的经典人名（含族姓、天神、动物名）、地名及含人名/地名的经名；现代人物、现代地名不在此列。

**取名优先级**（用户 2026-10-19 规定，取代 G9 规则）：
1. 公认常用的巴利三藏译名（如《卡拉玛经》）；
2. 原翻译——如与全书风格一致且无误，则保留（“原翻译”指 G9 之前书中已有的译名，即底本译名或经用户确认的 G5–G8 修订形）；
3. 萧式球译（志莲净苑《巴利文佛典翻译》长部/中部/相应部/增支部，https://www.chilin.org/culture/Current/current_detail1.html?child=202&id=86 ；中部网页版 https://nanda.online-dhamma.net/tipitaka/sutta/majjhima/mnNNN-siu-sk/ ）；
4. 汉译《阿含》（CBETA）；
5. 元亨寺《汉译南传大藏经》（CBETA N 部）；
6. 庄春江译（agama.buddhason.org）。
用户逐条指定者（表中“用户指定”）为最终决定。

**执行要点**：名字同时是普通词语的逐处按上下文判断；首次出现保留巴利括注；敬称前置；同一人、同一偈中的名字须一致；含人名的经名随人名。

**表中编号**沿用 review-G9.html 译名表的“#”列（用户所指行号即此列）。

| # | 巴利 | 类型 | 定译 | 级别 | 依据 | G9 译名 |
|---|---|---|---|---|---|---|
| 1 | Kālāma | 族 | 卡拉玛（卡拉玛人、《卡拉玛经》） | 1 公认常用 | 用户举例的公认译名；良稹译《卡拉玛经》等通行（萧 AN 3.65 作“迦蓝磨”） | 卡拉玛（卡拉玛人、《卡拉玛经》） |
| 2 | Bāhiya Dārucīriya | 人 | 木皮衣婆醯迦 | 2 原译 | G9 前原译（G8 已确认），无误；萧 AN 1.216 作“树皮衣．波希耶” https://www.chilin.org/upload/culture/doc/1666608406.pdf | 树皮衣婆醯 |
| 3 | Cakkhupāla | 人 | 护眼 | 1 公认常用 | 法句义注通行（文喜比丘译、佛门网） | 护眼 |
| 4 | Kevaṭṭa (Kevaddha) | 人/经名 | 坚固（《坚固经》） | 1 公认常用 | 《长阿含·坚固经》、元亨寺 DN 11《坚固经》通行（G8 已确认）；萧 DN 11 作《羇婆多经》 https://www.chilin.org/upload/culture/doc/1666608275.pdf | 坚固（《坚固经》） |
| 5 | Migasālā | 人 | 鹿住 | 2 原译 | G9 前原译（G8 已确认），义译无误（萧、阿含未见） | 鹿屋 |
| 6 | Seniya | 人 | 先尼 | 2 原译 | G9 前原译（G8 已确认）；萧 MN 57 作“舍尼耶” https://nanda.online-dhamma.net/tipitaka/sutta/majjhima/mn057-siu-sk/ | 斯尼耶 |
| 7 | Sudhamma | 人 | 善法 | 2 原译 | 原译（G8，律藏“善法比丘”） | 善法 |
| 8 | Tapussa | 人 | 帝梨富娑 | 2 原译 | G9 前原译（G8 已确认）；各巴利译本不一（萧 AN 1（第一优婆塞）“达波须”、元亨寺“多梨富沙”、庄“桃普沙”），无公认译名 | 提谓 |
| 9 | Mettagū | 人 | 梅达古 | 2 原译 | 原译（底本即如此），无误 | 弥勒固 |
| 10 | Dhotaka | 人 | 多达迦 | 用户指定 | 用户：改回之前的翻译 | 都达葛 |
| 11 | Senānigama | 地 | 斯那尼村 | 2 原译 | G9 前原译，无误（萧 MN 26 作“舍那镇”） | 谢那镇 |
| 12 | Vajjiyamāhita | 人 | 伐耆耶摩希达 | 用户指定 | 用户：改回之前的翻译 | 威基亚玛西达 |
| 13 | Sirimaṇḍa | 人 | 尸利曼陀 | 2 原译 | 现代长老，原译 | 尸利曼陀 |
| 14 | Kakkarapatta | 地 | 喀卡拉巴塔 | 2 原译 | G9 前原译，无误 | 鹧鸪羽 |
| 15 | Upasena Vaṅgantaputta | 人 | 优波先那·瓦刚塔普塔 | 2 原译 | 原译（底本），无误（萧 AN 1.215“优波舍那．鹏紧多子”） | 瓦额达之子优波先那 |
| 16 | Sobhita | 人 | 娑比塔 | 用户指定 | 用户：改回之前的翻译 | 寿逼桃 |
| 17 | Kusa (Jātaka 531) | 人 | 古萨 | 2 原译 | G9 前原译，无误（元亨寺作“姑尸”） | 姑尸 |
| 18 | Maṇḍavya (Jātaka 444) | 人 | 曼达维亚 | 2 原译 | G9 前原译，无误（元亨寺作“曼达宇耶”） | 曼达宇耶 |
| 19 | Suvaṇṇasāma | 人 | 睒子 | 1 公认常用 | 《睒子经》通行 | 睒子 |
| 20 | Sāḷha Sutta (AN 3.66) | 经名 | 《萨拉经》 | 2 原译 | G9 前原译，无误 | 《萨哈经》 |
| 21 | Sedaka Sutta | 经名 | 《私达迦经》 | 2 原译 | 原译 | 《私达迦经》 |
| 22 | Bāhukā | 地 | 巴乎迦河 | 用户指定 | 用户 G11 指定“巴乎迦河”（取代 G10 的萧译“婆睺迦河”） | 巴乎葛
| 23 | Adhikakkā | 地 | 阿提迦（渡口） | 用户指定 | 用户：阿提迦 / 阿提迦渡口（萧 MN 7“阿提迦渡口”）；巴利 Adhikakkā 为浴场 | 阿地葛 |
| 24 | Gayā | 地 | 伽耶 | 1 公认常用 | 通行 | 伽耶 |
| 25 | Sundarikā | 地 | 孙陀利迦 | 用户指定 | 用户指定（=萧 MN 7） | 孙陀利葛河 |
| 26 | Sarassatī | 地 | 舍罗舍提 | 用户指定 | 用户指定（=萧 MN 7） | 色乐色地河 |
| 27 | Payāga | 地 | 波耶迦 | 用户指定 | 用户指定（=萧 MN 7） | 波亚家 |
| 28 | Bahumatī | 地 | 婆睺摩提 | 用户指定 | 用户指定（=萧 MN 7） | 巴乎马地河 |
| 29 | Vessantara | 人 | 须大拏 | 用户指定 | 用户指定；《太子须大拏经》 https://cbetaonline.dila.edu.tw/zh/T0171_001 | 维桑塔拉 |
| 30 | Jāli | 人 | 耶利 | 用户指定 | 用户指定（G9 预改）；《太子须大拏经》 | 耶利 |
| 31 | Kaṇhājinā | 人 | 罽拏延 | 用户指定 | 用户指定（G9 预改）；《太子须大拏经》 | 罽拏延 |
| 32 | Maddī | 人 | 曼坻 | 用户指定 | 用户指定（G9 预改）；《太子须大拏经》 | 曼坻 |
| 33 | Mahāvessantara Jātaka | 经名 | 《须大拏本生经》 | 用户指定 | 用户：与第 29 行一致 | 《大本生经》 |
| 34 | Nālāgiri | 动物 | 护财 | 用户指定 | 用户指定（G9 预改） | 护财 |
| 35 | Mayhakasakuṇa Jātaka | 经名 | 《我有鸟本生经》 | 5 元亨寺 | 原译《麻雀本生经》不确（mayhaka 为叫“我的”之鸟，非麻雀）；萧、阿含无；元亨寺 J 390“我有鸟本生谭” https://cbetaonline.dila.edu.tw/zh/N0018_008 | 《我有鸟本生经》 |
| 36 | Sudhābhojana Jātaka | 经名 | 《天食本生经》 | 5 元亨寺 | 原译《须达饭本生经》易误为须达多（Sudatta）；萧、阿含无；元亨寺 J 535“天食本生谭” https://cbetaonline.dila.edu.tw/zh/N0018_023 | 《天食本生经》 |
| 37 | Illīsa Jātaka | 经名 | 《夷利沙本生经》 | 2 原译 | G9 前原译，无误 | 《伊利萨本生经》 |
| 38 | Apaṇṇaka Jātaka | 经名 | 《无误本生经》 | 2 原译 | G9 前原译，无误 | 《无戏论本生经》 |
| 39 | Mandhātu | 人 | 顶生王 | 1 公认常用 | 通行 | 顶生王 |
| 40 | Mahājanaka | 人 | 摩诃迦那迦 | 2 原译 | 原译 | 摩诃迦那迦 |
| 41 | Sarabhaṅga | 人 | 萨拉邦伽 | 2 原译 | G9 前原译，无误 | 娑罗槃迦 |
| 42 | Sāriputta | 人 | 舍利弗 | 1 公认常用 | 公认；“萨利子”与全书不一致 | 舍利弗 |
| 43 | Mahānāma (Sakka) | 人 | 摩诃那摩 | 用户指定 | 用户：改回（全书释迦族 Mahānāma 统一） | 摩诃男 |
| 44 | Nandiya | 人 | 难提 | 1 公认常用 | 萧、庄、阿含一致（萧 AN 11.13）；“南帝亚”与全书传统名风格不一 | 难提 |
| 45 | Saviṭṭha | 人 | 殊胜 | 1 公认常用 | 萧 SN 12.68、庄、杂阿含一致 https://www.chilin.org/upload/culture/doc/1666608353.pdf | 殊胜 |
| 46 | Musīla | 人 | 茂师罗 | 1 公认常用 | 萧 SN 12.68、庄、杂阿含一致 | 茂师罗 |
| 47 | Nigaṇṭha | 族 | 尼乾陀 | 1 公认常用 | 萧、阿含通用，全书统一 | 尼乾陀 |
| 48 | Uruvela Kassapa | 人 | 优楼频螺迦叶 | 2 原译 | 原译（去间隔号，全书统一） | 优楼频螺迦叶 |
| 49 | Hatthaka Āḷavaka | 人 | 阿罗毗的手长者 | 2 原译 | 全书已用（G8 已确认） | 阿罗毗的手长者 |
| 50 | Gotama | 人 | 乔达摩 | 1 公认常用 | 通行，全书统一 | 乔达摩 |
| 51 | Upāli | 人 | 优波离 | 1 公认常用 | 萧、庄通用，全书统一 | 优波离 |
| 52 | Godhika | 人 | 瞿提迦 | 2 原译 | G9 前原译，与萧 SN 4.23 同 https://www.chilin.org/upload/culture/doc/1666608343.pdf | 瞿低迦 |
| 53 | Khemaka | 人 | 差摩迦 | 2 原译 | G9 前原译（G6 已确认），无误（萧 SN 22.89 作“羇摩迦”） | 差摩 |
| 54 | Sunakkhatta | 人 | 善星 | 1 公认常用 | 萧 MN 105、庄、阿含一致 https://nanda.online-dhamma.net/tipitaka/sutta/majjhima/mn105-siu-sk/ | 善星 |
| 55 | Pāṭikaputta | 人 | 波梨子 | 2 原译 | 原译 | 波梨子 |
| 56 | Poṭṭhapāda | 人 | 布吒婆楼 | 用户指定 | 用户指定（长阿含、元亨寺） | 布吒婆楼 |
| 57 | Pārāsariya | 人 | 波罗奢那 | 用户指定 | 用户：改回之前的翻译（G8 已确认形） | 波罗奢耶 |
| 58 | Uttara | 人 | 郁多罗 | 2 原译 | 原译（G8 已确认） | 郁多罗 |
| 59 | Kajaṅgala | 地 | 迦阇伽罗 | 用户指定 | 用户：改回之前的翻译 | 迦徵伽罗 |
| 60 | Esukārī | 人/经名 | 郁瘦歌罗（《郁瘦歌罗经》） | 用户指定 | 用户：改回之前的翻译 | 耶苏葛力（《耶苏葛力经》） |
| 61 | Subha | 人/经名 | 须跋（《须跋经》） | 用户指定 | 用户指定（=萧 MN 99、135） | 苏玻（《苏玻经》） |
| 62 | Potaliputta | 人 | 哺罗陀子 | 用户指定 | 用户指定 | 迫大哩之子 |
| 63 | Bhaddāli | 人 | 跋达离 | 用户指定 | 用户：改回之前的翻译 | 跋大哩 |
| 64 | Kuṇḍaliya | 人 | 昆达利耶 | 用户指定 | 用户：改回之前的翻译 | 库达利亚 |
| 65 | Añjanavana | 地 | 安阇那林 | 用户指定 | 用户：改回之前的翻译 | 漆黑林 |
| 66 | Bhadraka | 人 | 跋陀迦 | 用户指定 | 用户：改回之前的翻译 | 薄罗葛 |
| 67 | Dārukammika | 人 | 达卢卡摩 | 用户指定 | 用户：看萧用什么——萧 AN 6.59“达卢卡摩” https://www.chilin.org/upload/culture/doc/1666608464.pdf | 达鲁葛咪葛 |
| 68 | Yasoja | 人 | 耶输阇 | 用户指定 | 用户：改回之前的翻译 | 亚受若 |
| 69 | Sopāka | 人 | 索帕迦 | 2 原译 | 原译，无误 | 苏波迦 |
| 70 | Adhimutta | 人 | 阿地目多 | 2 原译 | G9 前原译，无误 | 阿提目多 |
| 71 | Migajāla | 人 | 弥伽阇罗 | 2 原译 | G9 前原译，无误（萧 SN 35.63 作“鹿网”） | 鹿网 |
| 72 | Ujjaya | 人 | 优阇耶 | 用户指定 | 用户：改回之前的翻译 | 优惹雅 |
| 73 | Saṅgārava | 人 | 僧伽罗婆 | 2 原译 | 原译，与萧同 | 伤歌逻 |
| 74 | Ātumā | 地 | 阿图玛 | 2 原译 | 原译，无误 | 阿都玛 |
| 75 | Sudassana (māṇava) | 人 | 苏达萨那 | 2 原译 | G9 前原译，无误 | 善见 |
| 76 | Vacchagotta | 人 | 婆蹉衢多 | 2 原译 | G9 前原译（G5 已确认），无误（萧作“婆蹉种”） | 婆蹉种 |
| 77 | Aggi-Vacchagotta Sutta | 经名 | 《婆蹉衢多火经》 | 2 原译 | G9 前原译，与第 76 行一致 | 《婆蹉火经》 |
| 78 | Caṅkī Sutta | 经名 | 《旃奇经》 | 用户指定 | 用户指定 | 《郑计经》 |
| 79 | Kīṭāgiri Sutta | 经名 | 《翅吒山经》 | 2 原译 | 用户：再看看——保留原译（G8 已确认）；现代巴利译本“往見”MN 70 亦作《翅吒山经》 https://ehipassa.org/majjhima/070/ ；萧作《基多山经》 https://nanda.online-dhamma.net/tipitaka/sutta/majjhima/mn070-siu-sk/ | 《记大其哩经》 |
| 80 | Doṇapāka Sutta | 经名 | 《多那帕卡经》 | 2 原译 | 用户：再看看——保留原译（音译无误）；萧 SN 3.13 作“一多那食物”，庄作《一桶煮好的经》 | 《一桶煮好的经》 |
| 81 | Sālā | 地 | 萨拉 | 2 原译 | 原译，无误 | 沙拉 |
| 82 | Acela Kassapa | 人 | 迦叶波（裸行者迦叶波） | 用户指定 | 用户：改回之前的翻译（= review-G9“已替换旧译”栏）；G11 全书统一（含 path-factors-of-concentration 脚注 146，Acela 按 G5 作“裸行者”） | 迦叶 |
| 83 | Samiddhi | 人 | 三弥提 | 2 原译 | 全书统一（G8 已确认） | 三弥提 |
| 84 | Mahākoṭṭhita | 人 | 大拘絺罗 | 用户指定 | 用户：改回之前的翻译（= review-G9“已替换旧译”栏）；G11 全书统一（含 calm-and-insight；对称“友拘絺罗”不变） | 摩诃拘絺罗 |
| 85 | Kosala | 地 | 拘萨罗 | 1 公认常用 | 萧通用，全书统一 | 拘萨罗 |
| 86 | Gijjhakūṭa | 地 | 灵鹫山 | 1 公认常用 | 萧通用、公认 | 灵鹫山 |
| 87 | Gosiṅgasālavana | 地 | 牛角娑罗林 | 2 原译 | 全书已用《牛角娑罗林经》（G8 已确认，中阿含 184）；原译“高辛萨拉”与之不一致（萧 MN 32 作《大牛角经》） | 牛角娑罗林 |
| 88 | Bārāṇasī | 地 | 波罗奈 | 1 公认常用 | 萧、庄通用，全书统一 | 波罗奈 |
| 89 | Jambudīpa | 地 | 阎浮提 | 1 公认常用 | 萧通用，全书统一 | 阎浮提 |
| 90 | Jetavana | 地 | 祇树给孤独园 | 用户指定 | 用户指定（=萧通用） | 祇陀林（寺院：祇园精舍） |
| 91 | Vāseṭṭha Sutta | 经名 | 《婆悉吒经》（对告者 Vāseṭṭha 作“婆悉吒”） | 用户指定 | 用户：改回之前的翻译（= review-G9“已替换旧译”栏）；G11 全书统一（含 law-of-kamma 经名 ×3、对告者 ×3） | 《婆私吒经》 |
| 92 | Kuṇḍadhāna | 人 | 军头波汉 | 1 公认常用 | G9 前已用译名，保留；《增一阿含·弟子品》 https://cbetaonline.dila.edu.tw/zh/T0125_003；元亨寺 AN 1.14“军头波漠”（庄“古达达那”） | 军头波汉 |
| 93 | Sīvali | 人 | 尸婆罗 | 1 公认常用 | G9 前已用译名，保留；《增一阿含》；元亨寺 AN 1.14“尸拔罗” | 尸婆罗 |
| 94 | Bakkula | 人 | 薄拘罗 | 1 公认常用 | G9 前已用译名，保留；《阿弥陀经》；元亨寺“薄俱罗” | 薄拘罗 |
| 95 | Sāti | 人 | 嗏帝 | 1 公认常用 | G9 前已用译名，保留；《中阿含·嗏帝经》（萧“沙提”、庄“沙低”） | 嗏帝 |
| 96 | Māgandiya | 人 | 摩犍提 | 1 公认常用 | G9 前已用译名，保留；法句譬喻诸本通行（萧“摩紧提耶”、庄“马更地亚”） | 摩犍提 |
| 97 | Selā | 人 | 尸罗 | 1 公认常用 | G9 前已用译名，保留；《杂阿含》1203；《别译杂阿含》（庄“谢勒”） | 尸罗 |
| 98 | Puṇṇa Koliyaputta | 人 | 富楼那·拘利子 | 2 原译 | G9 前已用译名，保留；萧 MN 57“富那．拘利子”；庄“拘利族人之子富楼那” | 富楼那·拘利子 |
| 99 | Sītavana | 地 | 尸陀林 | 1 公认常用 | G9 前已用译名，保留；古译通行（庄“寒林”） | 尸陀林 |
| 100 | Sāketa | 地 | 娑祇多 | 1 公认常用 | G9 前已用译名，保留；萧（5 处）、阿含（庄“娑鸡多”） | 娑祇多 |
| 101 | Sunāparanta | 地 | 输卢那 | 1 公认常用 | G9 前已用译名，保留；萧；《杂阿含》311 | 输卢那 |
| 102 | Kakudhā/Kakutthā | 地 | 拘孙河 | 1 公认常用 | G9 前已用译名，保留；《长阿含·游行经》 | 拘孙河 |
| 103 | Veḷuvana | 地 | 竹林精舍 | 1 公认常用 | G9 前已用译名，保留；通行名 | 竹林精舍 |
| 104 | Isipatana | 地 | 仙人住处鹿野苑 | 1 公认常用 | G9 前已用译名，保留；通行名 | 仙人住处鹿野苑 |
| 105 | Brahmāyu | 人 | 梵寿 | 1 公认常用 | G9 前已用译名，保留；庄、萧 MN 91 | 梵寿 |
| 106 | Byagghapajja / Dīghajāṇu | 人 | 虎路 / 长膝 | 2 原译 | G9 前已用译名，保留；庄 AN 8.54 | 虎路 / 长膝 |
| 107 | Sīvaka | 人 | 尸婆 | 1 公认常用 | G9 前已用译名，保留；庄 SN 36.21；杂阿含 | 尸婆 |
| 108 | Isidatta / Purāṇa | 人 | 梨师达多 / 富兰那 | 1 公认常用 | G9 前已用译名，保留；庄、杂阿含 | 梨师达多 / 富兰那 |
| 109 | Dabba Mallaputta | 人 | 陀骠·摩罗子 | 1 公认常用 | G9 前已用译名，保留；阿含、律通用 | 陀骠·摩罗子 |
| 110 | Āḷavaka | 天 | 阿罗婆 | 1 公认常用 | G9 前已用译名，保留；《杂阿含》1326 | 阿罗婆 |
| 111 | Sundara-samudda | 人 | 孙陀罗·三慕陀 | 2 原译 | G9 前已用译名，保留；法句义注；书内统一 | 孙陀罗·三慕陀 |
| 112 | Raṭṭhapāla | 人 | 赖吒和罗 | 1 公认常用 | G9 前已用译名，保留；《中阿含·赖吒和罗经》；萧 MN 82 | 赖吒和罗 |
| 113 | Kumārakassapa | 人 | 鸠摩罗迦叶 | 1 公认常用 | G9 前已用译名，保留；庄、元亨寺 | 鸠摩罗迦叶 |
| 114 | Vaṅgīsa | 人 | 婆耆舍 | 1 公认常用 | G9 前已用译名，保留；庄、杂阿含 | 婆耆舍 |
| 115 | Sāgata | 人 | 娑伽陀 | 1 公认常用 | G9 前已用译名，保留；《四分律》；元亨寺“娑竭陀” | 娑伽陀 |
| 116 | Mogharāja | 人 | 莫伽罗阇 | 2 原译 | G9 前已用译名，保留；（庄“空虚王”，增一“面王”） | 莫伽罗阇 |
| 117 | Selected well-known | 人/地 | 舍利弗、阿难、目犍连、大迦叶、优楼频螺、纯陀、优陀夷、离婆多、跋迦梨、法施、耆婆、大劫宾那、波婆、那烂陀、拘利、天臂、菩提王子、无畏王子、长爪 | 1 公认常用 | G9 前已用译名，保留；庄、萧共用 | 舍利弗、阿难、目犍连、大迦叶、优楼频螺、纯陀、优陀夷、离婆多、跋迦梨、法施、耆婆、大劫宾那、波婆、那烂陀、拘利、天臂、菩提王子、无畏王子、长爪 |

**G11 说明（2026-10-19，用户确认）**：
- “改回”＝ review-G9 译名表“已替换旧译”栏的内容；编号＝ review-G9 译名表左侧“#”列。G11 已逐行核对。
- 第 22 行由用户改定为“巴乎迦河”。
- 本表其余行维持 G10：第 2 级“原译”仍指 G9 之前书中已有的译名；木皮衣婆醯迦、阿提迦渡口、须跋，以及与萧式球不同的 G8 定译，一律保留。
- 遗留扫描：凡在任何一轮出现过、现已被取代的译名，全书不得再出现（引文出处标签、参考文献原题、巴利语括注除外）。

> 来源：萧式球 PDF 各册见上；CBETA https://cbetaonline.dila.edu.tw/zh/ ；庄春江 https://agama.buddhason.org/ 。

---

## 附：插图（diagram）校对规律〔IMG3〕

原则：按英文原图的**意思**校对，而不是照搬它的版式。英文图版式凌乱、不规范的地方，改画成清楚、规范、美观的版本。

1. **对齐**：同一列的元素要垂直对齐，同一行的元素要水平对齐。表头和下面内容的列起点要一致；分组编号和它所属的列左对齐；连线的落点要对准相应的行（例如“2/3 对准左侧的信/慧行”）。
2. **居中与留白**：整幅内容要水平居中，上下左右的留白要均衡，右侧不能留出过大的空白（渲染时自动居中，顶部和底部各留 20px）。
3. **框内文字**：框内文字水平、垂直都居中，框的上下内边距相等；框高按内容来定，不留多余的空白。
4. **连线对称**：成对的分支（汇合、分叉）要镜像对称，线型（实线/虚线）的语义要清楚。
5. **箭头**：样式统一。几条线汇向同一目标时，先合并成一条再画一个箭头，不画多个错位的箭头。回环箭头用直角圆角折线，箭头垂直指向目标。
6. **括号（brace）**：括号的范围必须正好覆盖它所概括的项（从第一项的左/上边缘到最后一项的右/下边缘）；从括号尖端引出的线要从尖端出发，不能穿过括号。
7. **巴利文**：巴利文一律放在中文下方，用灰色小号斜体；同一幅图里要么每个术语都标，要么都不标。不写成“中文（巴利）”同行括注（正文句子里的引用除外）。
8. **译全**：图中的巴利词组都要附中文译名，优先用正文已有的译名（如 mamaṅkāra＝我所作、ahaṅkāra＝我作、mānānusaya＝慢随眠）。
9. **措辞统一**：同类项目用同一个句式（例如都用“对 X 的执着”）；圣者用“须陀洹向/斯陀含向/阿那含向/阿罗汉向”；禅那写“初禅、二禅、三禅、四禅”。
10. **去括号、不折行**：说明文字不加括号，直接作为灰色副行，与上一行文字左对齐。能放在一行的就不折行；脚注类小字要缩小字号，排成一整行。
11. **列表符号**：同一张表里的列表符号要统一（全用圆点，或全用编号）。表格中的勾选用 ✓，不用 ×。
12. **出处**：图中引用的出处按正文规范写作“DN 33 / D iii 248-9”，不用 PTS 旧式写法“D. III. 248-9”。
13. **字形**：巴利变音字母用拉丁字体（Source Sans 3）渲染，避免 CJK 字体里的 ṅ、ṁ 显示错位；中文标点（“”……、）仍用 CJK 字体。
14. **源文件**：SVG 源文件（表格类为 HTML）放在 batches/IMGn/src，文件名与 JPG 相同，宽 800 逻辑像素，按 2 倍输出 1600px。

---

## 附：术语补充〔IMG4 用户确认〕

- **色界四禅**：标准写法是“初禅、二禅、三禅、四禅”，不加“那”，“第一禅”统一改为“初禅”。语境需要突出序数时（例如与阿毗达摩五禅体系对照）可以保留“第X禅”。无色禅仍写“第X无色禅”。网址、锚点、经名链接里的“第X禅”一律不改。
- **X向**（指修道者，如 maggaṭṭha；sotāpatti-magga 指道本身时为须陀洹道）：一般直接写“须陀洹向、斯陀含向、阿那含向、阿罗汉向”。首次出现或需要说明的地方，可以加括注“（为证得X果而修行的人）”。

## 附：SVG 输出规范〔IMG4〕

每张图输出三个文件：`name.svg`（文字已转曲，主力版本）、`name_text.svg`（保留文字，供编辑）、`name.jpg`（兼容备份，宽 1600px）。

**正式仓库** `_uploads/buddhadhamma/images/diagrams/` 中每张图放三个文件：name.jpg、name.svg（转曲）、name_text.svg（留档备用）。正文目前仍引用 JPG。

**name.svg（发布用）**

1. **文字全部转曲**：不出现 `<text>`。字形一律转成 `<path>`，同一颜色连续的字形合并为一条 path。
2. **白色背景**：第一个图形元素是覆盖整个 viewBox 的 `<rect width="W" height="H" fill="#FFFFFF"/>`，不留透明区域，保证深色或夜间模式下线条依然可见。
3. **尺寸与留白**〔IMG6 修订〕：画布统一宽 800（JPG 为 1600px），内容水平居中；上下留白统一为 20px，各图高度随内容而定。根元素写 `width="800" height="H" viewBox="0 0 800 H"`，三者一致。preserveAspectRatio 不写。
4. **元素白名单**：只允许 `<svg>`、`<title>`、`<rect>`（仅背景）和 `<path>`。禁止滤镜、阴影、模糊、渐变、混合模式、opacity、`<mask>`、`<clipPath>`、`<use>`/`<symbol>`、`<marker>`（箭头头部改为实心 path）、`<image>`/内嵌位图、`<foreignObject>`、`<style>`、class、CSS、@font-face、`<script>`、vector-effect、注释、编辑器元数据和命名空间。
5. **样式写法**：只用行内表现属性（fill、stroke、stroke-width、stroke-dasharray、stroke-linecap、stroke-linejoin、fill-rule）。允许描边，线宽随缩放等比变化。
6. **颜色**：保留设计原色（墨色 #2c3e50、线条 #4a5866、灰字 #6b7785、底色 #f6f1e7/#eef3f8），不强制改为纯黑。底色已经是白色，灰字对白底的对比度约 4.6:1。
7. **坐标**：只用绝对命令 M/L/C/Z，数值保留 2 位小数。
8. **文件头**：`<?xml version="1.0" encoding="UTF-8"?>`，不写 DOCTYPE，只声明 SVG 命名空间（不用 xlink）。
9. **无障碍**：根元素写 `role="img"` 和 `aria-label="<正文图注>"`，第一个子元素是 `<title>` 图注，图注与正文 `![图注]` 一致。
10. **验收**：
    - `xmllint --noout` 检查格式正确；
    - 用规范检查脚本扫描禁用元素和属性；
    - 分别用 rsvg-convert、cairosvg、Chrome 栅格化到 1600px，与 JPG 逐像素比较，指标为平均灰度差和“差值大于 64 的像素占比”，要求接近 0；
    - 记录文件大小。
11. **JPG 生成方式**：JPG 由转曲 SVG 经 Chrome 按 2 倍栅格化得到（quality 92），两者的版式和留白因此完全一致。转曲时以页面背景矩形校准坐标，抵消 Chrome 打印约 0.03% 的缩放。〔IMG5〕全部 30 张都由转曲 SVG 生成 JPG，包括内容不变的 past-present-future-cycles 和 destruction-of-defilements，三种格式完全一致。

**name_text.svg（编辑用，不用于发布）**：保留 `<text>`，可以有 `<style>` 中的 @font-face（Source Sans 3 负责拉丁和巴利字母，Noto Sans CJK SC 负责中文）和 `<marker>`。需要本机装有上述字体；在 Chrome 中的渲染与发布版一致。rsvg 不支持 unicode-range，巴利字母会回退到 CJK 字体，字宽会略有不同。列表圆点（::marker）不是文字节点，转换时按 Chrome 的画法补成圆形；viewBox 与发布版相同的裁切范围（可带偏移）。表格类的图由 HTML 版面（按 2 倍设备像素排版，与截图一致）换算成 rect、line 和 text，每行文字单独定位，换行位置与原图相同；转曲版也由这份 _text.svg 生成，避免打印排版改变换行。

**EPUB 和网站嵌入**〔IMG6 修订〕：正文引用转曲 SVG，写法为 `![描述性 alt](./images/diagrams/name.svg){: width="800" height="H" loading="lazy"}`，图上方加图题段落 `图 X.Y：标题` 并加 `{: style="text-align:center"}`；站点 CSS 已有 `img{max-width:100%;height:auto}`。原写法〔IMG5〕：`<img src="images/diagrams/name.svg" alt="图注" style="max-width:100%;height:auto">`，按原尺寸显示，屏幕较窄时等比缩小；各图宽度不同，不要统一拉伸到 100%。EPUB3 清单里写 `media-type="image/svg+xml"`，JPG 保留作后备。不要给插图加深色模式的反色滤镜，白底就是为此准备的。

## IMG7 / ILL1 补充（2026-11-05）
- 图表 img 统一写法：`![alt](./images/diagrams/name.svg){: width="800" height="H" loading="lazy" style="max-width:100%;height:auto"}`，路径保持 `./images/`。
- 图题改名：图4.3 三世二重因果；图7.1 禅修成就的次第；图12.1 三学的运用（正文引用同步）。
- 插图图注：Noto Sans CJK SC 11px、行距16px；寺名、佛像名、人名后括注英文原名；街道层小地名保留拉丁拼写。


## m-review-language-01 人工语言校对补充（2026-11-18，Asia/Shanghai）

以下是有语境边界的判断，不是全局替换表；同一巴利词可因句法、法义层次与读者需求有不同自然译法。与旧的自动最高频建议冲突时，以此处及更新后的 glossary-final.csv 为准。

- Sīvaka=尸婆迦；Sīvali=尸婆罗，不能按汉字前缀连改。Dasuttara Sutta=《十上经》。所有冻结经号、AIPali URL和图片路径不因显示名称改变而改动。
- 呼语āvuso通常译贤友并在人名前；普通朋友、善友、恶友不改，bho注释的吾友保留其语用分析。并非所有友都是同一源词，也不以是否比丘机械决定礼貌程度。
- nirāsa技术义用无所期待/无所希求，说明字面反常双关时可保留无望；凡夫的失望、绝望与阿罗汉的圆满无求必须区别，正面慈悲善愿等希望不强行改词。
- sekha技术义统一有学，普通学僧/学生不套用。sīlabbata-parāmāsa作为saṃyojana称结缚；cetaso vinibandha为心缚；普通心理纠结可用心结。
- Nigaṇṭha泛指离系者，Nigaṇṭhā为复数教徒：教团用尼乾陀派/耆那教，成员用尼乾陀派教徒；Nigaṇṭha Nātaputta人名用尼乾陀·若提子。不按陀/子词尾简单分配教主与成员。
- nimitta宽义为相；技术禅修可用心相/禅相；具体心理影像可用心像，不是字形错误，不要把所有相限制为视觉表象。三相沿用遍作相、取相、似相。
- vaṭṭa/vivaṭṭa在缘起两过程对举时可用流转/还灭，不把还灭说成另一循环；解脱结果的脱离轮回/出离轮回可依语境保留。
- nirodha在缘起灭支与灭谛等用灭；本轮附录六止息是讨论英语cessation的译词，不建立nirodha只能译止息的规则。缘不具足而不生，不等同毁灭一个已生实体。
- 干观说明避免用证悟枯燥；可解释为修观前未证禅那，纯观行者与干观行者是本处别称。心解脱/慧解脱的释义应说明含义，避免重复中文词的翻译腔。
- P601命终叙事依TH+EN改般涅槃，注意出四禅后；不把全部final/ultimate Nibbāna机械改无余依涅槃。P999的泰文是生活方式，不是人格；两章英文原有同名标题，不删章、不改目录。
- P987 Thera在SN21.10是人名，不能把每一处Thera都按长老敬称替换。P1086附注17.9用善巧能干，与标题及正文回指相同。
- PDF中重复译偈先对照前文：只删巴利原句后重复的第二份中文译文，保留清楚的主译与巴利；术语释义、校勘、源目说明不删。
- P235作者示意可用清晰并列列表，不因英文HTML转换产生的孤立项目而照搬；经文引语仍用blockquote。不改CSS；引文出处可调整外围括号/分隔，不能改经号/链接。

本轮记录：/workspace/bd-audit/batches/m-review-language-01/。用户P页号与L编号同时保留；R1未获授权，当前历史位置不动，待确认。


## m-review-language-02 补充（2026-11-18 Asia/Shanghai）

- **M010 P1157**：ekaggatā、cittassa ekaggatā、cittassekaggatā在禅支、心所名和术语定义处统一为“心一境性”，中文在前。自然述谓可说“心专注于一境”。普通“一心一意”、单一心识刹那等不机械改。心一境性本身未必都是正定，须保留善恶语境。
- **M011 P1157**：本处sampasāda明确释为saddhā，作“净信”；整句传统的“内等净”等译法不排斥，切勿由单词译名反推所有二禅经句须统一改写。jhānaṅga统一“禅支”，附注18.5标题、回指一致。
- **M014–M017 P1178/P1180**：四神足通名欲、精进、心、审察；本节向善、求圆满的欲明释善法欲，不全书替换欲或热情。四种定分别为欲定、精进定、心定、审察定，名字与后文作用相对应。审察包括因果探究、实验和反思，不局限为省察自我；“心”在此指专心投入，不新增专注意念名相。勤行指起支持、推动作用的精进，与四正勤相联。
- **M021 P1229**：nirodha可用“灭”作名相、“止息”作释义和动词；不是所有句子必须用同一个单字。五灭各有范围，保留复合名；samuccheda-nirodha用“正断灭”，表示断除烦恼，不是断灭见。
- **M022 P1236**：bhāvita是已修习的完成态，与bhāvanā修习过程不同；解释例“身的修习圆满者”与既定词表相联，经文短式“身已修习”可依语境保留。
- **M025 P1238**：Pāṭimokkha及其复合名称统一“波罗提木叉”，不用省略的波提木叉；巴利、出处和不同律学概念不改。
- **M026 P1241**：重组本书篇章的小节标题采用“将《佛法》浓缩为四圣谛”；不是对一般佛陀教法一概加书名号。此为用户本轮明确要求核定的标题。
- **M028 P1279**：双空格硬换行通常生成br，不生成独立段落。需要Word每一段首行缩进时用空行分段，并在Word段落样式设首行缩进2字符；只对用户指定原名与出生资料处改动，其余硬换行保持。
- **R1**：用户pt92u已选A，保留“梵行……的重要目标；”后注码；本轮不再列待定。

- **M003 P1150**：同一游行训诫全书五处，共同部分统一为“比丘们，为了多数人的利益，为了多数人的安乐，为了悲悯世间，你们要游行。”两处长引文保留“为了诸天和人类的利益、福祉和安乐”，不删不同引文的额外范围；其它游行叙述不套用。

## m-review-format-language-01：中文读者取向与出处指引〔pt94u〕

以下为语境性编辑原则，不是全书无条件替换表；与v7“普通术语不加英文释义、必要英语分析除外”的原则相衔接。

- **英语词是分析对象时**：保留实际英语词，但先使中文释义独立可读；词源、多义、英译选择须明确属于英语或英译者，不把英语词源说成汉字词源，也不把几个英文别译伪称通行中文译名。只需转述含义时，可直接给中文释义并标明其为英译之意，不必增加一串英文。巴利语、梵语和泰语转写、人名、书名、出处缩写与网址不按英语赘词清理。
- **引导词不机械合一**：精确出处、页码、注号及局部定位通常用“参见”；需比照异说或相关材料时，cf.可用“参照”或依句法保留“比较”；引导通读章节、附录或较长解释时可用“参阅”。“参考”仍用于借鉴、参考框架、参考资料、参考书目等实义。英文reference须先分辨是出处、引文、论述还是参考资料，不逐字硬译。简短“见上文”“见下文”可保留；正见、邪见、看见、亦见于等绝不据字形替换。
- **异译与词形**：已有中文异译可用“又译”；解释性可选表达可用“也可译为”。另一种拉丁转写词形应说“另一词形”，不能冒称另一中文译法。不限定每个巴利语词只有一个死译名。
- **虚构金额例子**：确属说明问题的假例，可改用自然的“元”及合理数量，并保持原有比例、比较及推理；不声称作汇率换算。真实历史币种、金额、引文事实须保留或另行研判，不套用假例本土化。
- **括注与引用边界**：独立译者括注和作者术语说明通常不伪装成经文引用框；原框若承载公式、图解或另一层作者附注，则按实际功能保留。经文结语与出处应核原经及英文结构，不以视觉换行就断言漏了引用符。调整时保护注码、锚点、既有硬换行与加粗附注题。


## m-review-concepts-01：语境规范与可检验标准

本轮以用户新的同层对举与中文阅读要求更新上文对应条目，旧稿中“禁用观禅”及chanda自动最高频映射不再适用。A/B及C009全章概念用词审读已完成。泰英对读以全章主题、分类和上下文对应为依据；逐次中文候选判断见本轮库存与段落判定表。D1的concepts01处理记录保留；最新pt97u决定及原经核查见concepts02，仍不得为视觉顺序擅改第10项或总结。

### 先辨概念，再选同层主称
1. 止观：普通止/观；动作修止/修观；明确方法止禅/观禅。引用音译时奢摩他/毗婆舍那同层；乘名止乘/观乘或以止/观为乘。内观若指普通内省、向内观察，不硬改；律藏Samathakkhandhaka、书目、原泰文目录、特定译名引述各保留其本来对象。毗婆舍那定等既有技术复合名不为凑字数新造含混的观定；四神足第四种定用审察定，避免和vipassanā混淆。
2. chanda：先问是词义范围、伦理属性、法数名，还是普通动词。广义不恒善；kattukamyatā为欲求行动，可随善/不善；与渴爱对举且依理解向善时为善法欲。ch10从前部广义分析转入约定的狭义论述，P676应读作善法欲会否趋向不善，不能抹平为一切chanda恒善。引文和关于同一欲字不同解释的争论保留。完成某项任务后相应欲求平息，不等于断灭阿罗汉全部善法欲。
3. 乐：THความสุข/สุข、EN happiness为总称，可包欲乐、禅那之乐与超越乐受的乐。中文总称用乐，不把它误当一切都是感官乐受。安乐可表示安稳喜乐的具体状态、祝愿和惯用句；欲乐、禅那之乐、观智之乐、至上安乐、利益安乐等先辨对象，不按善/恶一刀切。多数人的安乐等已核定经句不改。

### 检验而非机械禁词
- 每个候选有原文、位置、范围判断、保留/修改理由；机器只能找疑点，不能凭词形替语义决定。
- 成对比较不得止或内观、止禅和毗婆舍那无说明地跨层；单独保留音译或一般内省需有语境理由。
- 修改后读完整段及前后过渡，确认代词、简称、引文限制和法数未改变；不以同字强行统一不同概念。
- 章名、小标题同步导航与回指；保持固定锚点，检测已有链接是否新增失效。
- ch11已完整核TH两章及EN合并顺序。P807第6依pt97u改为非圣/圣；pt98u又决定第10也改为无定/定。concepts03已应用，保留原总结，D2关闭。

### C009完稿补充：自然中文与源语边界

- 分类、层次及总题用“乐”；日常教育、体验和分享可用“快乐”。明确安稳自在、祝愿与惯用经句可用“安乐”，善法欲带来的所有乐不自动改叫安乐。不可机械造出音乐义“乐感”“乐章”或缺助词的“精致乐”“乐形式”。
- TH ทุกเวลา、ประจำตลอดเวลา及EN ever-present、constantly present在三类简明分类中作“恒常具有的乐”，不另立永恒实体。TH22:1807–1827的nirāmisatara-sukha用“超非物质之乐”，此处为阿罗汉省察智所生，仍属受；不要与非受的灭尽定之乐混为一谈。
- 英译者对happiness与pleasure的选择是英语说明；注的标签统一为“译者注”，不另分英译者注/中译者注/中译说明；内容中用“英文译本”“此处中文”等客观句式交代语言归属。不得把原英译说明写成安乐/快乐的固定二选一。
- 可检验例：全章的分类含欲乐→乐；四种居士乐条名及复述→乐；孩子健康安乐、痊愈的安乐、众生利益安乐→可保留；学习获得快乐→自然叙述。不同语法角色不是不同法义概念。
- 本轮用户明确授权止观、chanda、乐的标题与层级审改，以下目录表定稿列已同步；一般冻结标题规则仍对未经后续明确授权的轮次有效。

## m-review-format-language-02：反馈后当前有效规则〔pt96u〕

- **评价层次**：一般评价好/坏，道德评价善/恶；kusala/akusala 的技术名善/不善。讨论英语 good 的广义时，可以说明其涵盖美学、用途与经济价值；不得异层拼成好/恶，也不能把所有 good/bad 硬等于善/不善。
- **思与意图**：术语主称思（cetanā），即心的意向作用。概念定义、法数/复合名及同节回指优先同称；普通计划、动机、打算可用意图。英语 intention 本身的词义讨论不可删，saṅkappa/adhippāya/adhimokkha 等不能因英译或汉语相近就等同 cetanā。javana-cetanā 作速行思，指速行心中的思，不把心与心所直接当作同一物。
- **数字空格**：依本轮明确偏好施行，是本书编辑约定，不说成普遍强制标准。只处理可见汉字与 0–9 的交界，一个 ASCII 空格；已有间隔不重复加。小数、范围、千位分组的数字内部不拆。实际语法、引用标识、元数据与路径保护，链接/强调容器外沿放空格，不能隔开链接与其紧邻 IAL 属性。
- **金额**：现代假例及说明性寓言中的确定金额采用阿拉伯数字，与原数额和比例一致；英文既有 $300 也有 three/fifty dollars，中文不必逐例追随英文数字字形。不扩大到所有中文数字。原典引文/诗句与固定说法依原语体保留，如八百万金币的经文叙事、一枚硬币的譬喻/件数，不冒充现代金额例子。货币单位及历史事实不按汇率本土化。
- **括注层级**：独立说明用外层（），已有圆括注内的再括注用〔〕；双引号不构成圆括号层级。六角括号不是所有英文释义的专用括号。引文中明确标出叙述性编者插语的〔〕不等同词义括注，书名号也不改。上轮错误是把已有内层规则误套到外层，并非另有标准要求。
- **译者注统一标签**：只用译者注。需要区别语言或叙述者时在正文说“英文译本较少使用…”“此处中文以…”，不把原英译者第一人称冒充当前中文译者。真实译者身份的历史说明与原作者的注不因此抹去。
- **D1/P807历史记录**：format-language02当时未获顺序决定而不改；pt97u后来明确只改6、不改10，pt98u又批准改10，当前结果见concepts03。其余概念成果保留。

## m-review-concepts-02：语境规范〔pt97u；斜线与D1条已由concepts03取代〕

1. **四向四果**：人/阶段主称须陀洹、斯陀含、阿那含、阿罗汉。修行人用X向；道本身X道，果X果，不能把所有magga都改成向。首次或解释确有需要可括注意义；入流的词源专论、四入流支、原经标题等保留。随法行者/随信行者是独立类别，法随法行另为实践术语。P1161按所引SN48.12–24分列须陀洹与两类随行者。第7章附录七明确说明经本异文，其不同版本解释不在名词统一时悄悄改写。
2. **条件**：第10/11章以人为奖酬约定驱动行为的 systems of preconditions / provisional system 用“附加条件机制”，首次说明先完成行为才获报酬/奖励。不把它泛化成所有conditioning。自然因缘、有为法、一般必要条件、修行前提、为了感官享受而采取手段等分别表达；四个相关标题定稿列已同步。
3. **技术**：technical term依语境为专门术语、佛法中称、按佛法分类、严格说来；实际操作为方法/实际修习等。科技、技术进步、技术人员、技术官僚等实义保留。不得用一张替换表消除所有技术。
4. **卓越**：梵行构词及崇高人生用崇高/高尚；殊胜品质、圆满修养、最高成就分别按义表达。梵行广义仍是整个道/中道，不缩为道德行为；出众能力与工作成果的卓越可保留。
5. **戒定慧**：同层并列可戒、定、慧，或戒行、禅定、智慧；三学正式名称遵增上戒学、增上心学、增上慧学，不把心/智慧作用一律当作定慧标签。禅定是广义samādhi，不限jhāna。因果链、不同功能的连续叙述、心身与四修习等不是强行凑字的同层三学标签。P223三项标签按实际英文PDF第417页/书页345加粗。
6. **佛法僧**：真正同层三宝默认佛、法、僧，P910三项标签如此。佛陀、佛法、僧伽只在法明确为佛陀教法且读来准确时可用。Dhamma包含真理/德行/证悟，不为双字而缩成仅教法；叙述中的佛陀、经句中的声闻僧伽与历史专名不机械改。
7. **斜线历史记录**：本轮曾按编辑约定添加42处空格；pt98u及concepts03已撤回这一约定与42处新增空格，当前规则见concepts03，不动既存源出处空格。
8. **D1/P807与D2历史记录**：本轮只改6而保留10与总结；pt98u后来明确也改10，concepts03已改为无定乐/定乐，两处低到高与原总结一致，D2不再需要。
9. **回读与保护**：每个检索候选须有判断，所有修改处带最终上下文回读。保留既有外层（）/内层〔〕、译者注标签、数字与汉字一个ASCII空格规则；引用、注码、URL、固定锚点、图像、硬换行均不得搭便车变动。

## m-review-concepts-03：当前新增/覆盖规则〔pt98u〕

- **D1已解决**：第6非圣/圣、第10无定/定均低到高，原“后一种更胜”总结保留，不采用D2中性改写。原经AN2.74为定乐胜，来源标识未改。
- **最小编辑**：真实世俗技术/技能本来可读就保留；不为避“技术”而改写。上轮57处技术编辑仅限其清单回查，船夫恢复“技术娴熟”；术语/定义/分类义的自然化仍有效。旧B009简化“修行成就程度”为“修行成就”。
- **斜线紧排**：半角/作汉语并列或替代分隔时紧排，不用全角斜线。GB/T15834—2011第4.17例示和/或、杜婧/于洋，第5.1.9规定半字位；这支持中文紧排习惯，不等于另有禁止所有混排外文ASCII空格的绝对条款。撤回concepts02的42处新增空格；经号/PTS来源格式、URL、编号、路径及其他未授权旧空格不扩大改动。
- **书名与语言/文字版本**：一般《书名》中文版/英文版/泰文版；有无“的”依长限定可读性，正式书目标题与资料专名不改。泰文译本指译成泰文；泰文字母版可仍是巴利语原典，对比罗马字母版的校勘情形必须区分。没有明确书名的本书英文版、泰文原版等自然回指保留；泰语版在口语音视频等语境不是错误词。
- **四神足**：具体分支主称欲神足、精进神足、心神足、审察神足（传统称观神足），列表、小标题与明确回指用全称。欲/精进/心/审察作为基础心理因素和词义分析保留；欲定/精进定/心定/审察定是相应的定，不改成神足。区别神足通这一神通类别。
- **四念住**：经句于身随观身、于受随观受、于心随观心、于法随观法；内外限定置于对应宾语前，名词身随观/身念住等依语法保留。已核TH16:542–564，不是把所有身受心法词组套成同一句。附注18.2与回指同步，固定锚点不变。
- **五盖**：作为该法数独立分支用贪欲盖、嗔恚盖、昏沉睡眠盖、掉举恶作盖、疑盖；P1144经引、P1166滋养、注释和十盖细分均逐义处理。普通恶意、贪欲、睡眠、疑，其他心所类别、以及复合盖的解释性子因素不一律加盖。
- **七觉支**：具体分支念觉支、择法觉支、精进觉支、喜觉支、轻安觉支、定觉支、舍觉支。七项名录、滋养主语、义注所说使该觉支生起的品质和十四觉支细分用全称。生起条件中的身心轻安、念的基础、定相、与有定者交往及普通心理品质不扩成觉支；不与五根、禅支或四梵住混同。
- **交付HTML**：完整原段/最终段通过工具render_review_diff.py用difflib自动生成红删绿增，所有文本先转义；不得人工/LLM圈定差异span。大块超过阈值可仅展示完整原后段，标明未细比。剥离生成标签须逐字恢复原文/新文，含HTML转义和Unicode测试。
- **DQ历史状态（concepts03）**：当轮断灭/自性仅研究、未应用。此待决状态已由用户 pt99u 在 concepts04 授权取代：正断灭选定，自性逐义酌改；具体现行规则见下节。此前交付报告不回写。

### concepts03版本语义的补充实证
TH04:3184、TH07:1520/1529明确使用“อักษรไทย”（泰文字母）；TH24:211–215明确“以泰文字母印行”。书目总注英文虽写translated into Thai，该处以泰文原文为准，指版本文字而非翻译语言。书目总注与相应脚注已据此统一，不扩增出版年代；真正泰文译本（例如faith所讨论的皇家版译文）仍区别处理。


## m-review-concepts-04：正断灭与自性（pt99u 已授权）

### A．按概念分层，不按“断灭”字串替换
- samuccheda-nirodha 名相用**正断灭**：相应出世间道智永久断除该阶段应断的烦恼；四道次第不同，不能写成须陀洹道已断尽所有烦恼。
- samuccheda-vimutti 用**正断解脱**；samuccheda-pahāna 用**正断**，必要时释为“以道智彻底断除相应烦恼”，不造“正断灭断”；samuccheda-parinibbāna 在本书该义注分类处用**正断般涅槃**。
- 一般 nirodha 仍依既定规则为“灭／止息”，不得全体加正断。解释性“完全根除／断除／摧毁烦恼”若义已准确、句子自然，可保留，不把普通谓语全改成术语。
- uccheda-diṭṭhi、ucchedavāda 的断灭见／断灭论，以及无有爱、害怕自我消失、被批评的“我被断灭”等确指的欲求或见解，保留“断灭”；不得让批评对象变成正断灭。

### B．“自性”按原词及句义灵活处理，不实行零字政策
- sabhāva 讨论事物如何呈现、运行时，多用“性质／特性／实际情形”；不一律译成“实相”，更不可把所有相关句子改成“皆依因缘生”——有些总说同时包括无为法。
- 与共相（sāmañña-lakkhaṇa）相对的 sabhāva-lakkhaṇa 用“特相”；原文给出的简称“自相”（salakkhaṇa）保留。paramattha-dhamma 在该句中为“胜义法”，不是 paramattha-sacca 的“胜义谛”。
- 否定固定自我、实体或主宰的“无自性”可以保留（pt100u明确确认）；并非正面肯定实体自性。不实行禁字；必要时才解释为“无固定实体”，不可写成“无性质”，不可抹掉否定范围。
- kammassakatā-ñāṇa 为“知业为己有之智”，它不是 sabhāva。自性苦（sabhāva-dukkha）作为必要的原有分类名保留，并以“有为法固有的苦，即生、老、死”解释；不等同苦苦。
- P1123 四圣谛句依泰文“คืออะไร เป็นอย่างไร”释为“如实了知四圣谛各自是什么、是怎样的”，不硬译本体化的自性；不借此扩张出原文没有的本体理论。

### 本轮范围边界
本节记载concepts04当时的研究边界：专注/sati/忆念当时待商议。后续pt100u已批准推荐的C-A方案，concepts05按下节正式实施；C-B未选择。T1念/正念等名称规则继续保留。glossary的current列仍为历史采样，非本轮精确词频。


## m-review-concepts-05 当前执行规范（pt100u，2026-11-19 Asia/Shanghai）

规则先行，但以具体句义与法义层次为边界；以下不是全局替换表。完整候选判读、未改理由、EN/指定TH证据与修改后回读见 batches/m-review-concepts-05。

- **A001 无自性**：允许否定实体性的无自性；恢复上一轮不必要的否定语回避，同时保留对正面自性按性质、特相、实际情形等所做的改进。自性苦等必要分类并未禁用。
- **A002 C-A已批准**：念是忆持与不忘失，不限回忆过去；操作依句说持续留意、不忘失所缘、忆持对象/任务，正知负责如实了知。P1116警惕将念局限于“回忆过去”；P1127批评围绕行为者“我”的自我形象来误读念与正知，不是否认忆念这个译词；P1126主动作用与被作用的对象以相对齐的三组表达。upaṭṭhāna于此解释照护心。不把每个专注改念住/安住，定、禅那、止及普通工作语境的专注仍可用；观也须定，止也有念，不能宣称一有注意就必然变成止。
- **B001/B002 三苦与苦**：正文标签苦苦、坏苦、行苦；保留原有脚注及其编号，脚注补充说明而非只在那里给中文名。坏苦为标准主标签，变易苦可作解释，单称变苦不取。四谛总名苦，不缩成情绪痛苦或生理疼痛；具体疼痛、苦受、悲伤和日常困境仍可自然说痛苦。说dukkha-vatthu为苦的所依，不把三法印总义定义成引起疼痛。
- **B003 见解**：diṭṭhi名称见，说明时见解；顽固执见不用意见来弱化术语。普通建议、学者意见和讨论者未证实的意见仍可保留。
- **B004 时节**：utu-niyāma主名时节法则，解释温度等物质变化，不限四季；亦称物理法则是传统分类的释义，不以此宣称等同整套现代物理学。
- **B005 生起/止息**：samudaya-vāra/nirodha-vāra对举生起过程/止息过程，正文列表、跨章回指同步；通向解脱的善法相续不是另一个封闭苦循环。经典此灭故彼灭、无明灭→行灭、苦灭/灭谛等保留灭；三相现象生起/灭去与vaṭṭa/vivaṭṭa流转/还灭另按本义处理，不为凑双字改法数。
- **B006/B007 世间/世界/世俗**：有情生命经验、业偈、悲悯众生与经典分类一般世间；物质世界、宇宙系统、国际社会、专名、世界观等依句世界。MN98主译世间随业而转；注明的异译保留其译义与归属，只协调世间称谓。lokānukampāya译悲悯世间，不把帮助无源并入原经引语。lokiya世间、lokuttara出世间；sammuti/sammati人为约定及vohāra世俗语言，不强改世间法。人间之乐与天界之乐对举时不用含天界在内的整个世间替代人间。
- **B008 念住与随观**：satipaṭṭhāna类别身念住/受念住/心念住/法念住；anupassanā是身随观等随观动作，完整句于身随观身等。kāyānupassanā本身不硬改身念住，也不把vedanā这个受字括注到整项受念住名下。
- **B009 四双八辈**：唱诵固定名统一四双八辈，即四道四果；解释性的八种圣者标题及其他圣者分类按含义保留，不把七种人类别等混入。
- **B010 三利益**：现法利益、后世利益、究竟利益。samparāyikattha依本书解释也含当前人生较深层的利益，不机械限制死后；paramattha在此为究竟利益，在paramattha-sacca/dhamma等仍按胜义谛、胜义法/究竟法解释。
- **B011 我所**：分析名相用我所，首处释为认作我的/归我所有。直接引语这是我的、这不是我的及普通领属语保留。ahaṁ与asmīti/asmimāna不可统归所有权；我是之慢不同于我所执。mamāyita按作者偶兼我执的特殊解释保留弹性。附录标题与正文回指同步，不改变图片标识及既有表格。
- **B012 凡夫**：puthujjana及清楚的凡圣阶段对举用凡夫；ทั่วไป等一般人群及一般学习者不套用。P76泰文为一般人相对于能独立自证者，不改凡夫。uttarimanussa超越常人的殊胜法亦非一律超越凡夫。
- **B013 非我公式**：统一这不是我的、这不是我、这不是我的自我。泰文确也有相当于我不是那个的语序，不能由旧中文主宾顺序就推论作者暗立一个实体我；采用这不是我是自然、易与全式对齐的汉译。
- **B014 内外缘**：先明确善友及其言教、引导为外缘，如理作意为内缘；之后自然用善友、良好教导、外在助缘或内外因缘配合，不反复堆叠社会因素/个人心力因素。明确人物和言教时不一律稀释为社会环境；真正的制度、文化等语境保留社会环境/社会影响。自证者不依他人引导，不等于不依任何外在因缘。
- **B015 福德**：十福业事十项用布施之福德等X之福德，与后文通过X获得的福德对齐；相关puñña回向/积累用福德，动作可说修福。正在讨论旧口语做功德的句子保留被讨论用语；guṇa、三宝/僧伽功德、ānisaṁsa与kāmaguṇa等不误改成福德。
- **B016/B017 已正确项不重改**：vipassanā-ñāṇa=观智；P853基线已经正确。dhammānusārī/saddhānusārī=随法行者/随信行者，非另一术语法随法行，也不能都说已获入流果。P1161基线已正确。SN25.1核实未获初果的限度；MN70另明说其部分漏尽，不能凭记忆去删改原经这项叙述。

排版及冻结底线不变：外层（）、内层〔〕；正文斜杠不加空格、不用全角斜杠；中文与阿拉伯数字边界一ASCII空格但标识/引文/链接等保护；不改书稿CSS、不改注号、经号、AIPali目标、图像路径与既有硬换行。HTML色差一律由可复现脚本产生。

本轮保护复核补记：完整图片Markdown（含替代说明）按冻结边界保留；four-noble-truths.md的图示替代说明原有“来世利益”作为图片保护例外原样恢复。正文和脚注三利益主标签已统一，不能用概念统一越过图片保护范围。


## m-review-quotation-01：引用体例与念的后续措辞（已实施）

concepts05 的措辞反馈，独立于引用专项
- 念（sati）不忘失所缘的作用可说“忆持对象”“持续留意”；避免“念所保持对象”“保持所缘”等生硬的及物构造。“保持正念/保持警觉”等维持状态之语本来通顺，不禁用“保持”。
- “具念”用于具有念而不忘失；并非凡 sati 都改成正念。正知是如实了解、洞察，不与定混为一谈。
- 止禅说明中，以“专注于”描述对稳定所缘的注意可以成立；该句仍说念在止禅中的作用，不将念定义成定，不反过来宣称观中不能有注意或定。

## Q/G：引用体例、出处归属及容器
- 通常的独立出处：现有经号/卷页在前，继以巴利经名。源标编号与全部URL不改。中文经名的取舍已由下文m-review-quotation-02按pt104u修订：纯粹多一层汉译经名的普通出处省去该汉译名；正文/附注题名不随之删除，带实质限定语的特殊出处按语境保留。
- 行文中自然提及某经、推荐阅读条目、章节对照可按语法题名在前；不是把所有题名都搬到编号后。章节/小节不能误用为两部独立书名。
- e.g.→例如；See→参见；cf./Compare 的出处关系→对照；cf.,e.g.→例如可对照。不同限定语不抹平。独立出处中的“例如”不是佛陀话语，不能悬在引文正文句末。
- “cited at / referred to at”说明该处也引用/提及，并非说主要原典“引自”后出论书。Vism与原始经引的两层源别保留；节译、前文已引、解释等有效说明保留。
- verse/verses 是“偈”的语言标签，可译“第 … 偈”；经号、页码、偈号原样保持，包括冻结版本与EN的差别。不得因EN另种编号而更正现有编号或URL。
- 短引可逐段同行括注来源，不必强排成统一的长出处段，更不能把各句出处合并后失去归属。
- 附注外层是容器，不等于整段经典原话；内层实际引录与其来源归在一起。已正确二级的正文不重复嵌套。作者依源整理的资料提要可以分层，须以“内容提要”等明确性质，不能变造为逐字佛说；其正常出处不必再冠“所据：”（pt105u，附注18.9）。
- 相邻且独立的经引或附注明确分界；仅加非可视HTML注释，不改CSS。基线Kramdown已独立的附注如实报告，不能声称原DOM合并。
- 实际检查渲染DOM列表；分成两个ol时，仅把第二个Markdown序号写成2不足以让Kramdown显示2，本轮P371通过把各条出处缩进相应li来恢复一个ol/两个li，实测显示1、2；不添加多余start属性。此例序号为作者的示例编排，不冒充原经固有编号。
- “同上”若只指来源，应明示指代且独立列出。现有引用标识计数冻结，不能擅增一份完整编号/链接。

- Comp.是《摄阿毗达摩义论》的缩写，不是Compare；Vīthimuttaparicchedo章下列Paṭisandhicatukkaṁ节，不能把章、节都套成独立书名。
- 经名校正须有实际源证：本轮SN3.18题名据既有冻结链接原典改为Kalyāṇamitta Sutta；不机械复制EN误题，也不因此改动编号。真实异名/简称可保留，不把所有原典题名强造为唯一译名。


验证提示：附注原DOM已独立时，只称显式分界；不把非可视注释误报成修复原DOM合并。P960同一出处行的一处硬换行为本轮特许删除，4132→4131，其余保持。


## m-review-quotation-02：普通出处省去汉译经名（pt104u）

仅多汉译经名的独立出处按多数格式“现有编号/卷页，巴利经名”呈现，删该处汉译经名及仅用于中巴配对的外括号；不改行文、附注标题、交叉回指或冻结编号/URL。
带实质说明的特殊出处不强拆：本轮《须跋经》有EN明确的abbreviated translation（节译）；《婆蹉衢多火经》有especially the concluding sections（尤指结尾部分），均按必要信息例外整行保留。后续 pt105u 已明确要求撤销《婆蹉衢多火经》此项例外，删该处中文经名及“尤指结尾部分”，保留正常编号/卷页、巴利名及全部URL；《须跋经》的“节译”及中文名仍原样保留。上述两项整行保留是quotation-02当时的保守处理，不另立“凡有说明均永久需要中文经名”的机械规则。词表译名本身不变，本轮不更新glossary。


## m-review-numbering-01：编号与语义层级（pt105u）

1. **先判节点，后定样式**：逐章核对EN实际HTML的heading、ol、ul、独立标记段落和段内枚举；不凭PDF视觉缩进或“有两种”推断有序。正文heading层级、既有锚点不为改编号而改变。
2. **段落纲目**：EN独立A./1\.等扩展段落用“一、二、”；同一纲目内再分组用“（一）（二）”。六方1/A–6/B解释为六个方位纲目，各含相互对应的两组职责。不用甲乙丙，不把六组拆成十二个无层级项目。
3. **真实列表**：有序项目用原生Markdown `1.  `，子项及续段按标记实际内容列悬挂缩进；两位序号加两空格时续段需五列。可用空父项 `4. ` 后接缩进的子ol，不编造引导文字。无序项目仍用`*`；EN原生ul里已经印有1./A.的伪编号，按实际数字/字母的有序语义修复，不保留双标记。
4. **续号和分界须实测**：被纲目、共用说明或学科标题隔开的同一编号组，用Kramdown实测支持的前置 `{:start="6"}` 等保留实际续号；不得假设原稿写6就会显示6。相邻而独立的同类列表会合并时，用最少的`<!-- numbering-boundary -->`分开，不改CSS。
5. **段内枚举**：同级用（1）（2），已在圆括号内时相应内层用〔1〕〔2〕。不把段内五法则或十二支箭头链强拆为段落；不改经号、卷页、偈号、URL或已冻结图片内编号。
6. **回指按意义同步**：2A/2B说明对应的跨生/当下解释，方法A–D按实际四种方法回指；“道#1–3”为道的三个子阶段，不是三条道。正文和远处脚注一并检查。无可查先行项的EN A/B/C不照搬为中文悬空回指，保留完整释义；可明确命名者优先用内容说明。
7. **附注容器不等于经典原话**：附注6.2四种缘起箭头概述为作者纲要，保留外层附注quote、撤去多余内层quote；已有真实经文/义注引录的层级不随编号轮泛改。
8. **保留判断实例**：P133三种应苦方式、P134四种活动、P294两个类比、P657两种渴爱、P936两种思维力量均有EN原生ul依据，保留无序；P794“第一/第二”也为EN无序成果条目。P842特殊要素贯穿其他要素，不编为第十一福业事。
9. **EN转换异常不硬抄**：四遍净戒B/C/D误吞在A项、缘起法行图中因“+”产生的孤立ul，都按实际并列义判断；逐项证据见本批DOM清单。
10. **P1221小范围释名**：首次完整定义对应“真理智（sacca-ñāṇa，亦称谛智）”“职责智（kicca-ñāṇa，亦称作智）”，已作智（kata-ñāṇa）原称保留。是有据的常见对应译名，不宣称唯一古译，也不把示/劝/证转或证智混成唯一命名。四谛所应履行的职责标签用应遍知、应断除、应现证、应修习；知遍知、审察遍知等智名和一般名词不机械加应。冻结的三智图片不改。

验收：43MD实测Kramdown零警告；逐列表核对父子深度、直接li数量、连续序号与续段归属；全部经号/URL/图片/注ID冻结、硬换行不变、内部链接零坏链。审计目录：`/workspace/bd-audit/batches/m-review-numbering-01/`。


## pt109u：编号02选择回退与结束

已按用户列明U项及必要关联恢复，其余已改项维持。撤回编号02“明确数量清单可推广为ol”的新增规范；后续不再以该议题发起调整，也不另立冻结/例外系统。基本段落纲目、语义层级、真实悬挂缩进、续号与既有回指检查等编号01规范仍有效。编号01第8条仅为当轮历史决定，不用于覆盖pt109u保留的02改项。具体回退见m-review-terms-diagrams-01/rollback-decisions.json。


## m-review-terms-diagrams-01：他人教导、性行与行者、相关图（pt109u/pt110u）

1. **paratoghosa柔性统一**：技术主名用“他人教导”，普通句法可用“他人的教导”；“听闻他人教导”描述接受过程，不与名词标签硬凑字面。字面“他人的言说”只在词义解释处使用。原文指有益/善法教导时保留限定，不把词本身定义成必然善法，也不以“诱导”概括全部。一般社会影响可按本句保留，不能把明确人及其教导统统改成环境。
2. **内外缘**：与如理作意成对说明修习/正见条件时用“外缘/内缘”；外缘说明可保留“社会影响”。普通外部环境、社会制度、物理因素及其他心理因素不是遇字就换。
3. **性行/人分开**：抽象cariya/carita是“性行（即性情与惯常倾向）”；具有这种倾向的人用“X行者”。本章ordinary behaviour是惯常行为，不是凡夫或一般人的果位身份。比较习惯、选择业处、教师判断对象、图表列头等人物位用行者；抽象性行的定义/成因不机械加者。
4. **六类人物规范**：rāga-carita贪行者；dosa-carita嗔行者；moha-carita痴行者；saddhā-carita信行者；buddhi-carita觉行者；vitakka-carita寻行者。本书同列ñāṇa-carita作为buddhi-carita同义名时也用觉行者。觉指智慧倾向，不表示已觉悟的果位；寻指思考倾向，不把所有普通思考语改成术语。依据叶均《清净道论》第三品及《摄阿毗达摩义论》第九品，并非凭字面把智/思随意替换。
5. **另一个二分体系**：本书缘起讨论的taṇhā-carita/diṭṭhi-carita用爱行者/见行者，不能用六类中的贪行者吞并爱行者。随信行者、随法行者等圣者名，善行、梵行、利行、ācariya及cetana等同形字都不机械改。
6. **图书一致**：本轮只授权outline-spiritual-training、training-and-development、techniques-characters三套图内容调整。保留路径与原尺寸；可编辑_text.svg保留真实文字，生产.svg采用既有Chrome→PDF→pdftocairo流程真路径化，不含text/tspan；同步JPG与实际PNG目验。图表六列与正文同名，保留近行定等非人物标签不变。其余图字节保持。

来源与逐段保留理由：本轮source-evidence/decisions-and-urls.md、83条paratoghosa及175条性行全书候选判断、57段修改后回读。来源经号不同版本编号不一致不据此改本书冻结编号。编号事项仅执行用户指定选择性回退，不扩展，也不重启数量清单推进。

## m-review-reader-01：t113u有限验收与阶段交付

本节只记录已经落稿、已完成回读与结构验证的修订；不是宣称t111u全书语义审校完工。新累计基线为d13a2ab，旧批次不重新包入。逐题完成状态及未审范围见随附completion-status.md、original-issue-status.md与pending-brief.md。本文旧版历史记录与本节冲突时，就本阶段已修订的语境以本节为准；不得据本节对未审候选执行批量替换。

- **各种“知”**：第二章按觉知、辨识/想、见解、智与智慧的不同作用分层。knowledge可指广义认识，不必是书本知识，更不自动等同观智。学问、传授的信息仍可称知识。标题“佛法中的各种‘知’”及“想”与“念”：记忆、辨识与忆持按实际书稿写法同步。
- **念、根与根门**：念忆持所缘，使所缘呈现于心而不忘失；可说持续留意，不倒说成单纯转移注意力。中性念不一律称正念；处、根与门不机械等同。
- **三法印与行**：三法印呈现共同特征，可释共相；特定法的自相/特相不删。行蕴、思主导的心理造作与泛称一切有为法须区分，不将所有行都改成造作。dhātu在第三章的自然规律语境不译成稳定实体；yogakkhema不是离开瑜伽。
- **生起/止息**：samudaya-vāra/nirodha-vāra对举生起过程/止息过程；vaṭṭa/vivaṭṭa对举轮回流转/轮回止息，必要时保留还灭这一传统名称。第六章Long/Short Format用完整式/简略式，避免与第四章总说/详说混淆。图2.4与此同步。
- **五类自然法则**：时节法则、种子法则、心的法则、业的法则、法的法则；依第五章与第三、四、十九章相关位置互校。法的法则在总义中说明普遍自然规律，不变成与其余四类互不相关的独立领域。
- **社会规约**：saṅgama-niyāma社会规约、saṅgama-niyamana社会规制、sammati-niyāma世俗规约、paññatti-niyāma人为规约。均属人为约定/制定的规范，不混同自然定律，不把世俗规约当成与出世间相对的世间法。
- **读者表达**：动态按实际所指化为运作、相续变化、因缘过程等；苦的生灭逼迫不同于伤害他人的恼害与社会压迫。真实物理物体、液体流动、宇宙论问题及转述常见等按原义保留。名称不一律升格名相，普通执着不一律换成技术术语执取，佛教/佛法/哲学全书延伸判断尚未完成。
- **智慧培育与标题**：已审“开发智慧”语境采用培育智慧；不是禁止一切开发或发展。当前目录表仅同步本批实际改动标题，其他标题不重审。
- **第五章好坏**：相关英语good/bad辨义段落面向中文读者改写，分清日常好坏与佛法善/不善；保留原脚注位置，并说明中文适配，不假称泰文作者采用中文例子。没有扩展成全书删英语。
- **仍有效的既有决定**：保留pt109u指定的编号回退与其余接受项；不重启编号02推广，不建立新的编号冻结。此前经号、URL、脚注及非指定图均不变。

本阶段交付的是可审阅、可上传的已验证增量版本；待审候选保持原状，之后不自动恢复全书审校。


## reader02：用户指定八项的完成规则（2026-11-25，Asia/Shanghai）

本节是已实际应用并回读的规则，不是未应用建议。范围限八项的全书检索与相关表达；实际改段逐段完整回读，未进行新的全书语义审计。逐处改/留、源行、来源限定见m-review-reader-02/review-ledger.json及edits.jsonl。

1. **R007 行/造作**：诸行、诸行无常、广义有为法，与行蕴及心的造作分开；十二缘起固定行支可保留行，首次解释或容易误读处直说心理造作。五蕴章思代表的是相关心理造作，不是思等同所有有为法。阿罗汉止息生业造作，并非在世时没有思或行蕴。
2. **R008 共相/特相**：共相可解释为共同特征；三法印不用技术意义的特相代称。自相/特相只在特定法的独有特征分析中保留；一般人的品质可用特征，不能把全部特性一律术语化。
3. **R012 名称**：名称、称谓、标签本来就是约定命名，按句意保留，不一律名相。六处章DN9引文两处使用称谓；不是对名色之名另作命名。
4. **R018 流动**：物理水流、清楚标明的比喻保留；生命、心念、正念等因缘过程按所指用相续/运作/迁流。不添加持久实体或独立的流。
5. **R020 知识**：学问信息可称知识；基本了解用认识/理解；亲自通达用了知；ñāṇa用智或对应智名，paññā为慧/智慧；并非所有ñāṇa都是观智。saññā在似相等技术语境为想，不泛作知觉。沿用如实知见、解脱知见等既定复合语，不把所有知见硬改成另一字样。明达者（vedagū）前后一致。法智（dhamma-ñāṇa）/类智（anvaya-ñāṇa）不与随顺真理之智（saccānulomika-ñāṇa）混同；知业为己有之智（kammassakatā-ñāṇa）保留世间基本认识的层次，不全抬成出世间智。
6. **R022 执着/执取**：技术取支upādāna及四取用取/执取；普通执着、贪染rāga等依上下文保留，不作全词替换。念住“不执取世间任何事物”的经句、解说、总结联动。uggaha取相用摄取影像，不把它等同烦恼之取。upādāniya是可被执取，不是执取本身；未加取限定的五蕴不等于一概无漏、不能被执取的五蕴。
7. **R043 培育智慧**：主动修习一般用培育智慧，也容许培养智慧、修慧等自然搭配；发展过程、智慧增长及一般智力能力发展并非禁词。标题及复合表达均已检索；本轮未改既定标题，不需生成新锚点或目录。
8. **R034 人天众生**：合举宣法受益者/受害者时可用人天众生；区别人和天人的比较、诸天与人等范围枚举保留，不压成一种主体。宣法训诫两处同引文联动。

### 来源与限度
- 以本地英文同章完整段落作主要对读，并核本地泰文第一章心所分类、第十二章901–942行、第十四章203/273行等相关段。来源摘录与文件哈希随本阶段参考包保存。未虚构PDF页码。
- 五蕴章E140–141关于阿罗汉的段落，本地泰文版本没有逐句对应；不能宣称逐句由泰文证实。本轮用上下文关于生业与唯作的对比、泰文第一章通一切心心所仍列思的分类，限定为“不再受生业造作束缚”；这是一处有记录的语境释明，不是另造泰文引文。
- 名称等词大多经判断保留；保留不是未做。匹配数/字面频数不是错误数，也不是全书逐字审读量。
- 所有URL、原典标识、脚注、ID、硬换行、列表、CSS及图像均按冻结要求验证；本轮未改图2.4或任何其他图像，累计包承接已验收图2.4。
- 仍待R027/R039的佛教/佛法/哲学全书延伸判断；本轮未处理这些未选维度，不能称原全书任务全部完成。


## m-review-notation-01：第一批大小写与语言分类（2026-11-25，Asia/Shanghai）

仅处理中文解释、括注、定义项、脚注中的普通巴利词形首字母；不是全书重新译注。依据当前 CN（起点458ab9c）、本地 EN HTML 的实际结构与同章 E 源段；不把旧 Z@ 中文当作现行书稿。

## 已知事实与推断分开

- P257：dependent-origination.md:1919–1934。EN E914 的 blockquote 内是带 br 的英文句群，`Saṅkhāra condition viññāṇa.`、`Viññāṇa conditions nāma.`；同一个词处于句首时大写、宾语位置时小写。括句以 `Kusala-mūlā` 起首。本轮中文括注 avijjā、saṅkhāra 等是词形，而非英文句首。
- P259：同章1957–1979；EN E925–936 实际为 ol 的12个 li，词头 Avijjā…Jarāmaraṇa 首字母大写。这是列表位置事实，不能证明十二词都是专名。
- P442：awakened-beings.md:296；EN E133 原文为 `The term bhāvita…`、`The term bhāvanā…`，两词实际不在英文句首。中文省去 The term 后仍可小写，原有这两词不改。
- P583：calm-and-insight.md:1411–1420 的 EN E647–650；Suta、Nimitta、Abhiññā 位于脚注起首，pariññā 在分号后。此轮前三者小写；pariññā 本已小写，保留。完整巴利句 `Sabbe dhammā nālaṁ abhinivesāya` 保留原式。
- 上述位置解释是由实际句法/DOM支持的体例推断，不是查得英译者逐项声明“因句首所以大写”，更不是巴利语必须一概小写的普遍断言。

## 可执行的低歧义规范

1. 普通巴利词形在中文句首、词头列表、脚注开头及中文括注中均用小写；不能将英文 sentence-initial/list-initial capitalization 机械移入中文词汇括注。保留原有长短音、附标、词尾、单复数、连字符与顺序；只改首字母大小写。
2. 人名、地名、天界名、典籍/正式篇名、自然书目引文与缩写、整句巴利引文或完整引用表达保留实际原式。词形相同不等于功能相同：citta 普通词与 Citta 居士、asoka 无忧与 Asoka 王、brahma 构词义与 Brahma 神名分别判定。既有冻结标题及其文字引用不在本轮擅改。
3. 拉丁字母不等于巴利语：梵语 Śūdra、Kṣatriyaḥ、Vaishya、Ashvamedha；泰语转写 Luang Por、Phra Jao；英语及书目名称、引用缩写、URL/ID 各自保护。不以一条 lowercase 正则处理所有语言。
4. Dhamma/dhamma 不按“宗教一定大写，普通一定小写”绝对二分。英译本可能以大写标示教法、称谓或语境义；《三法印》E20 明说 Three Characteristics 作为教导名才大写；《戒道支》E1052/FN160 明辨 sangha 僧团与 Sangha 圣弟子。其余 Buddha/Nibbāna/Sangha/Dhammavinaya 等本轮保留、列待议，绝不由英文宗教大写反推中文词形必须大写，也不据小写抹掉语义差异。
5. 注释标记自然文字与 Markdown 脚注语法、出处标识分开。统一标签仍是“译者注：”；本轮不改标签，不删注、不调序、不重译。中文可见方括号和说话人增补归第三批，不提前落实。

## 覆盖及限度

43MD 的正文、脚注及相关标题均纳入大写可见词扫描；已有冻结标题保留。14,030 是大写可见 Latin token 出现次数，不是错误数。逐语境选审993处，改657处（428种词形、624个改动源行〔当前AST去重586块〕、19MD），明确保留336处；141处/11组宗教称谓或英巴交界语境保护待议；其余12,896处作为姓名、标题、英语、缩写等排除类保留，未宣称逐个完成全书语义审计。

每组有实际 EN 词形证据和逐处决定。`lexical attestation` 类证明词形实际见于该章 EN；算法建议的段落对齐不冒充唯一逐句对应。手工核实的十二缘起链另标。Upapīḷaka-kamma 的英文原式用 en dash（Upapīḷaka–kamma），中文现有连字符故意不改；不是拼写修订。


## m-review-notation-02：第二批巴利语使用、中文主次及首注复注（2026-11-25，Asia/Shanghai）

本轮从 aa332f1 承接，只处理读者呈现和必要注释，不重译佛教概念。以现行中文整段、本地英文同章源段与既有中文规范为据；旧 Z@ 仅帮助定位，不冒充当前书稿。算法对齐不是唯一逐句对应证明；短词目和链条的邻段误配另已定位实际英文词头/整链。

1. **普通叙述与教学清单**采用“中文（巴利）：释义”，或依句法让中文先行；释义中的同义、替代形式与语境限定完整保留。词头不是专名，不凭字母外观判语言；沿用第一批词形/大小写保护，绝不把所有 Latin 统一处理。
2. **首注按章/文件，不按全书只注一次。**独立脚注、表格、定义、意义辨析、词源/语法单元可以重新标巴利。只在同段/同单元没有辨义或查找功能时删去重复括注；论述巴利词本身、比较不同义项、引用完整句子或重复因果节点时，不因重复而删。
3. **按实际功能判断语言单元例外（pt120u补查更正）。**仅真正以原词为研究对象的异名索引、同义/译法比较、词源、构词或语法分析，以及完整原文引句，可巴利先行。业的十六类、来源的先后分类及禅修五环节是普通解释性清单，不因像词目或位于附注/后记而豁免；中文定义另占下一段也不豁免。可前置忠实简释或名词短语，不强造唯一传统定译，不删屈折、别名、条件或词源。arūpa项仍保持无rūpa（色）的否定范围。
4. **同一因果链内部一致。**中文节点后附完整原词，保留节点、先后、箭头、省略、编号与硬换行；整句原文另行引用时内部原式保留。悦/喜/轻安/乐/定不互换，轻安/乐原有说明不删；buddhi-carita 仍为觉行者，ñāṇa-carita 别名保留。
5. **补中文优先用确证的既有术语；无既定短名可前置忠实、透明的描述性短释，不能假称传统定译。**第二章应遍知法、应断除法、应修习法与第十九章现行职责分类一致；既有自然句法“应培育之法/应修习的法”等不强替换。不得将自动最高频猜词当作最终汉译；下列本批 manual 条目高于旧 pali-auto 建议，但不抹掉历史记录或既有专名。
6. **严格分批。**统一注释标签仍是“译者注：”。本轮不启动全书引号/方括号/说话人增补审查或专名书名统一；已有外（）内〔〕只用于本轮新增括注所需的嵌套，不预定第三批编辑括号规则。第一批141处/11组英巴交界称谓继续原式保护。

覆盖和限度：43MD作可见词/候选结构扫描；985个重叠类别候选源段并非985处错误，15,398是词表/EN词形匹配 token，不是全书所有Latin或人工逐字审读量。222个改动源行的完整语境逐处回读〔当前AST去重217块〕；保留的词目、语法、整句引文、独立意义比较及重复注另列证据层级。其余候选保留但不伪称全段语义核证；逐处清单明确区分完整语境决定、词头/摘要筛读与扫描保留。本轮不为无充分来源的疑似翻译问题强制改义。


## m-review-notation-03：第三批引号、括注、译者注与经文增补（2026-11-25，Asia/Shanghai）

以下为本批实际规则，先前各批“第三批未启动”的句子记录其当时状态，并非本节后的当前状态。

1. **依据不夸大。**GB/T15834—2011的4.9.3.1说普通注释/补加一般用圆括号，4.9.3.6要求尽量避免同形嵌套；4.8允许真实引语、着重论述和特殊义引号。因此〔〕作为中文引文/正文已有编辑增补、说话人补接、译者夹注的区分，是本书体例，不声称国标强制。商务印书馆有明确说明六角括号标示特定修订者增补的译本实例。〔〕、［］、【】三种形状不混称。
2. **按功能，不按“有中文就换”。**普通词形/说明用（），嵌套用外（）内〔〕；已有编辑补语可用〔〕，保留词语边界，不把〔心〕身扩大为〔心身〕。二者外形相同但功能分别登记。真正英文/巴利原文、书目/版本装置、异读校勘及Markdown/注码等按原功能保留。三处Latin书目装置中的中文ASCII本批保留，书名全局体例归第四批。
3. **译者注标签唯一。**用“译者注：”，不另造译注/中文译者注/英译者注。必要的中文/英文译者身份在注释正文说明。独立脚注整则译者注不再套冗余外括号；作者注中或正文/引文中的译者插注可用〔译者注：……〕。内部已有〔〕的两处外圆保留，避免同形嵌套。作者回应译者的提示不改叫译者注。
4. **来源与范围。**不以“EN用了[]”推断泰作者/英译者谁最先加，也不推断原巴利无对应。MN136有阿难转报及佛陀etadavoca，P983压缩叙事桥既有〔〕保留；SN3.17有波斯匿王etadavoca，P1118对话不造新括号。SN38.16的已有整标签沿用〔游方沙门：〕。P1178法义体会前件在AN5.26有据，沿用EN摘引补接，逗号随补入的中文条件从句界定；MN36同型条件从句同步。“然后〔在后来的场合〕，我……”的逗号属于“然后，我……”而不机械移入。整标签/仅人物姓名的范围不抹平，冒号按真实补入单位判断。
5. **引号与相邻括注。**已核实的普通中文词头/译义可去冗余引号；直接话语、词语本身的讨论、特殊义、自我概念“我/我的”、黑白业等比喻保留。不把英语所有强调引号一概判错。相邻括号只在同一所指、同一作者层中以分号合并；独立出处、自然编号、不同注者层不合并。第六章两表原词、词形、词序与“黑白”语义功能保留。
6. **冻结与覆盖。**本批未增删任何Latin/泰语词形，大小写、附标、屈折、顺序完全不动；未改标题、URL/ID、脚注语法、列表/硬换行、CSS/图。全部209改段完整回读；4862个候选块只代表全书可见AST扫描，未逐段审过的保留项不能冒称“均正确”。第一批141处/11组交界、R027/R039及第二批语义疑点仍保护；“第四/五批未启动”为第三批完成时的历史阶段状态，不是当前进度。

来源：上海交大医学院语言文字网所载GB/T15834—2011全文（https://www.shsmu.edu.cn/yywz/info/1026/1526.htm）；北师大出版科学研究院编校文章（https://pub.bnu.edu.cn/jzyg1/06b4e9434c104517bbda817da9d2eac7.html）；商务印书馆《罗马帝国社会经济史》前言/翻译体例（https://www.cp.com.cn/book/7-100-02037-9_42.html）。实际EN HTML与四处原经的路径、摘录和SHA256随notation03参考包，不把搜索摘要当已读全文。


## m-review-notation-04 · 书名、专名及出处边界（已实施，仅本批确认）

1. **首注是阅读单元规则，不是字符计数。**章/文件内已有必要首注保留；连续行文、同一故事/对话里无辨义功能的重复原名可去。常见阿难、舍利弗等不为统一而到处补原名。少见人物既有首注不删光；独立附注/脚注、人物能力词目、表格、每个书目版本/作品的作者信息以及词源/同名/拼写讨论可复注。书目不是正文的长版累赘。
2. **三种载体分流。**普通正文沿用已定中文《书名》，必要首处原名可留；已有中文经名不要求每个都加巴利。紧接DN/AN等明确代码时，《长部》等中文名+冻结代码链接足以辨识，冗余Nikāya原名可省。缩写表保留完整中巴/代码，书目保留作品/版本/译者/出版社身份。脚注不一概等于出处：其中说明性汉语句的书名可中文为主（如《分别论义注》），带卷页/内部章名的来源串仍保留。普通独立出处保持当前编号/卷页+巴利经名，不恢复中文经名，不改链接/ID/数字。
3. **作品、部类与内部层级。**《佛法》一书与佛法教义分开；阿毗达摩等有学说/藏别等含义，不能凭斜体或大写判书名。国标书名号可用于书、篇等作品，本书内部章/节叙述按既有层级辨清，不谎称篇名一律不得用《》。已确认Mahākhandhaka=大犍度，即《大品》（Mahāvagga）的第1犍度；附注19.3据当前EN及既有缩写表96行纠正层级标示，不改变出处的Mahākhandhaka原文或MV1源标。
4. **人名不借机重译。**现有中文拼法沿用，完整名/简称、泰僧衔号和真实异名不无据抹平。菩提比丘为既定姓名形式，不作比丘菩提；明确姓名后的尊者按现行敬称前置。Citta的人名质多与心、Thera的特拉人名与长老敬称、Kassapa等同形不同所指逐语境区分；本轮不把所有长老/诗偈名称或组合敬称机械搬动。
5. **保护和限度。**保留原名全部大小写、附标、词形和真实异体；不把Cūḷapanthaka/Cullapanthaka、Khun Yongyut Thanapura/Dhanapura等当拼写统一任务。三处中文ASCII书目/版本/异名装置保留。Sīlakkhandhavagga在本文仍保留实际原名；本批未核定新增中文篇名，不臆造。统一标签仍译者注，注者归属不抹平。前批141处/11组交界与nibbuta/R027/R039保持保护；标题、目录、图像、CSS和全部冻结结构不改；“第五批未启动”为第四批完成时的历史阶段状态，当前见notation05验收。

依据：当前CN/EN源段及缩写表/书目，详见notation04逐项账本。英文对应采用真实HTML的名字及上下文证据，未将非唯一的自动匹配冒充逐段唯一对齐；GB/T15834—2011书名号条用于区分作品名称，不作为强制所有内部层级同式的理由。面向用户交付仅最新完整43MD，遵循t118u，不推断用户已上传。


## m-review-notation-05：前四批集成验收完成（2026-11-25，Asia/Shanghai）

1. 五批计划已完成。本批正文新增改动0，不为验收制造空提交；不重开未批准的全书词义审计。现行规则仍为notation01–04已确认条款；前文“某批未启动/未来讨论”属于当时阶段记录，不恢复旧规则或另索取已经批准的执行许可。
2. 四批内存逐行重放均与各自43MD提交字节一致。657处大小写变化只在第一批；第二批仅删16个登记冗余Latin token、未新增，第三批Latin序列不动，第四批仅132次登记整原名括注删除，其余Latin词形、变音、屈折及顺序保留。四批合计去重1029改动源行、986个当前AST源块；不是各批段数相加，也不表示第五批又逐字审读986块。
3. 最终人工全文回读146个跨批交叉源块，另56个不重复的用户示例/定义/脚注/书目边界源块，共202块；71个目标样本与交叉块重叠15个。全43MD作结构及可见AST验收，不冒称每章每字语义审读。保留Pali固定引句Gambhīrañca kathaṁ kattā / No caṭṭhāne niyojaye的来源大小写；人名＋能力的独立双括注并非同层赘注；arūpa中的无 rūpa（色）仍属词形辨析，不回滚第二批。
4. P257/P259英文句首及列表首的大写是实际位置事实；中文词形不照搬。P442英文实际有The term前导。P583的真实整句是Sabbe dhammā nālaṁ abhinivesāya。P983/P1118/P1178沿用第三批来源及补语范围判断，未因统一括号造新增补；三处含中文的ASCII书目装置及数字卷页装置保留。
5. 来源验收补记：notation03存档SN3-17-Pali.html实际是HTTP200校验等待页，不能作为经文正文证据；原存档不改。本批据https://www.wordsofthebuddha.org/sn3.17的公开当前页面重新核验rājā pasenadi kosalo bhagavantaṁ etadavoca；P1118保留结论不变。MN136、AN5.26、SN38.16其余存档已检查实际正文。英语[]不能单独证明最早由泰作者还是英译者添加；未宣称全书逐条泰巴溯源。
6. 141处/11组宗教称谓及英巴交界继续原式保护，不是141个错误。law-of-kamma.md:282 nibbuta（涅槃）：清凉、平息仍待另作词义核查；Sīlakkhandhavagga不臆造新增中文篇名，真实异体及R027/R039不重开。本轮没有新的强制规范或新定经典译名，因此词表1124行逐字保留，未添加伪装术语的验收条目。
7. t118u要求最新完整43MD.zip；pt122u随后明确仍须随每轮交付本轮差异审校HTML，不需累计HTML。不再交MD差分/累计多版本包；ZIP只含权威43个仓库相对路径MD，不含图、CSS、配置或内部审计文档。词表/指南/账本内部维护，不假设用户已手工上传，不重置历史基线。完成后idle，无自动续改。


## m-review-notation-02-followup-01：pt120u漏改纠正及t121冒号复查

- 实际根因：两项paṭicchanna/appaṭicchanna旧库N02-0864/0865已检出；draft-heads.py的短中文/逗号后限定词过滤未产提案，apply-reviewed.py又以过宽词目筛读理由保留。此前业十六类、来源次第及禅修五环节的整类豁免亦过宽，现撤回，不能借深度标签为漏改辩解。
- 中文优先是读者呈现，不是每个巴利词都要硬造名词：可用现有汉译或准确简短的说明性词头，保留原有例子、别名和限定。隐而不显、旁人不易察觉的苦/明显的痛苦为本处原释前置，不声称隐性苦/显性苦等是已核实传统定译；不与行苦、坏苦混同。
- 定义单元的中文词头（巴利）后接释义，用冒号；怀孕之苦所在七小类已同组复核。完整断言、真正引语、独立新论述不机械替换）。；新移位的词头也按功能放置冒号。新增注释只作本次词序所需最小调整；外（）内〔〕与已有编辑增补功能分别判断。
- 不能以词表成员资格、首字母大写、单一列表前缀、中文短释长度或是否与中文同段作为唯一检索/完成条件。独立AST与原始结构双证、Unicode组合附标/连字符/多词、双破折号/等号、独占词头下一段续定义均检查。所有残余起首词头必须有明确功能理由；无决定项保持待议，不写成正确。
- 真正语言例外保留：涅槃异名原词索引；sīla/vinaya/sikkhāpada的集合名词与单复数讨论；bhāvanā/bhāvita、词根/构词比较；Mā开头及其他完整巴利原句；独立词义译法脚注与自然出处。不能扩张为所有脚注/所有词目表免改。
- 同一职责家族沿用第十九章现行遍知、断除、现证、修习。sacchikiriyā的职责主标签为现证；普通说明中的亲证/证得等动词和同义说明不借此删去。
- 全部43MD扫描不等于全书所有Latin已逐词重新译审；本补查的结构候选与完整语境判断、原句号宽筛/精审数量见同目录issue-summary.json。nibbuta所在law282整段11词头按既定保护保留，不冒充合规词典例外；141处/11组大小写交界亦不判为错误。R027/R039和图像均未开启。
- 对外仅最新完整43MD ZIP＋相对50483f1的本轮暗色完整语境差异HTML，不交累计HTML；指南、词表、账本为内部维护。


## m-review-notation-06：残差体例与待决议（pt123u）

- 本轮只处理有把握的体例与已核实的具体条目，不把141处/11组大小写交界、nibbuta词义、P432页段映射或未经核验的说话人标记擅自落定。
- 定义清单：中文词头（巴利）后接本项解释用冒号。行文中的同位说明，在“即”前用逗号，如昏沉（thīna），即……。完整断言或另起论述不机械改冒号。
- 编辑增补〔〕若本身在引出后文或引文，冒号属于增补，写作〔清楚地知道：〕，去掉括号后不应留下外置冒号。作为完整标题的〔回应译者评论：……〕之后，引出作者答复的冒号属于外围句法，可留在括号外。外（）内〔〕仍用于嵌套括注；普通原名/释义对应用（），不得把〔〕当成所有括注的默认形式，也不得把经文编辑增补与普通对等词混为一谈。
- 已核实后加的说话人标记用〔佛陀：〕〔舍利弗：〕；巴利常有 etadavoca 叙事，但不等于每轮对话都有“xx：”。未核原文的对话标记本轮保留并列入待核。
- 认识/认知：认识多指理解、所知或见解；认知多指认知过程或机能。不把所有认识改成认知，也不把知识一律升级为观智。

## 文档分类维护原则与 m-review-reader-03（t126u）

术语词表（`glossary-final.csv`）、全书总修订指南（本文件 `revision-guide.md`）与 reader 专有行文/读者体验规范（`reader-style-guide.md`）各司其职，同步更新，互不混杂：

- `glossary-final.csv`：只收术语、译名与词义边界，不写长篇行文规则。
- `revision-guide.md`：全书各批次总修订原则、冻结项、体例与待决议，不把 reader 的句式品味细则整段搬进来。
- `reader-style-guide.md`：面向中文读者的行文、节奏、自然度与出版可读性规范，随 reader 批次按实际问题追加。

本轮 reader-03 的具体行文决定见 `reader-style-guide.md`；本文件只记录：在有把握处已按读者视角修订可见中文，不改冻结结构计数，不改图，不把记号批次的待决议（Dhamma/dhamma、nibbuta、P432、未核说话人标记等）擅自落定。R027/R039 仍不重开。
