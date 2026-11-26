# Reader Agent 交接套件

本目录是给**并行 Reader Agent** 的交接套件，用于按中文母语读者视角审校 Buddhadhamma 中文正文。

## 文档分类维护（t126u）——必须遵守

Reader 批次可以、也应当更新规范文档，但必须**分门别类、同步更新、互不混杂**：

1. **术语词表** `glossary-final.csv`  
   只维护术语、译名、词义边界和不宜混用的近义。不要把长篇句式规则写进词表。

2. **全书总修订指南** `revision-guide.md`  
   只维护全书各批次总原则、冻结项、体例和待决议。需要指向 reader 规范时写一条索引即可，不要把本套件的行文细则整段搬进去。

3. **Reader 专有行文／读者体验规范** `reader-style-guide.md`  
   只维护面向中文读者的行文、节奏、自然度与出版可读性。随真实问题递增追加，不预先堆砌理论条文。

某条决定既改译名又改句子时：词表写译名，本规范写如何入句，总指南只作索引。三份文档都要在同一轮里更新到彼此不矛盾的状态。

## 职责边界（t125u）

- Reader Agent **只审校和修改文字**：Markdown 正文，以及上述三类规范／词表。
- **不要修改任何配图、图表、SVG 或图片生成脚本。**
- 审读中若发现某张配图或图表需要修改：记下图号、所在文件与大致位置、建议改动点，在汇报里**单列「图像问题」**，由用户发专门指令交回主 Agent（Buddhadhamma）处理。
- 本套件与面向用户的交付包 **一律不含图片**，也不含图片生成或 SVG 处理脚本、工具。

## 套件内容（无图）

- `README.md`（本文件）
- `KICKOFF-PROMPT.md`（启动提示）
- `reader-style-guide.md`
- `glossary-final.csv`、`revision-guide.md`、`manual-review-standing-rules.md`、`delivery-policy-current.md` 的副本
- `tools/`：仅文字／Markdown 校验与定位工具（kramdown 检查、模糊定位、差异渲染等）。**不含**绘圆、SVG、位图处理脚本。
- `sources/`：与本轮条目相关的英、泰拆段，供对勘；不是全书源稿。

书稿正本在仓库 `_buddhadhamma/*.md`（43 个权威章节）。本套件若被放在 `_buddhadhamma/reader-kit/`，`_config.yml` 已将其列入 `exclude:`，不作为书籍章节发布。

## 工作原则（摘要）

- 目标是可出版的中文佛教文本：自然、顺畅、准确；以泰语原文、巴利、英译为意义依据，经文以巴利为准。
- 有特别理想且有依据的写法就改；没有把握就写入本轮差异 HTML 和汇报，提出建议，不牵强。
- 改、不改或只改一部分，都必须在 HTML 里写依据。
- 冻结项：引文 6275、AIPali 3300、注释 2120、内部链接 4240、硬换行 4131、列表 695，以及 URL、ID、CSS、图片字节。记号批次保护的 141 处／11 组大小写交界、`nibbuta`、P432、未核说话人标记，不得擅自落定。不重开 R027/R039。
- 本地提交使用既有技术身份：`git -c user.name=bd -c user.email=bd@local`，不改全局配置，不 push。
- 面向用户的交付：最新完整 43 个书籍 MD 的 zip（仓库相对路径，仅 MD），外加本轮暗色完整语境差异 HTML。不交累计包，不交图片。

## 启动

先读 `KICKOFF-PROMPT.md`，再读 `reader-style-guide.md`、`revision-guide.md` 的分类原则与冻结项，以及 `glossary-final.csv` 中与本轮相关的条目。不要从零发明另一套总指南。
