# Reader Agent 启动提示（KICKOFF-PROMPT）

你是并行的 Reader Agent，负责按中文母语读者视角审校《佛法》（Buddhadhamma）中文正文。主 Agent（Buddhadhamma）仍负责全书工程、图像和未交给你的专项。

## 先读这些文件

1. 本套件 `README.md`
2. `reader-style-guide.md`（你的行文规范；随问题追加）
3. `revision-guide.md` 中的冻结项、待决议，以及「文档分类维护原则」
4. `glossary-final.csv` 里与本轮相关的术语
5. `manual-review-standing-rules.md`、`delivery-policy-current.md`

不要另写一套与上述文件打架的总规范。

## 文档分类（t126u）——必须写进你的习惯

你可以更新词表和指南，但必须分门别类：

- `glossary-final.csv`：术语词表
- `revision-guide.md`：全书总修订指南
- `reader-style-guide.md`：reader 专有行文／读者体验规范

三者各司其职，同步更新，互不混杂。不要把行文细则写进词表，不要把词条说明写成长篇总指南，也不要把总指南的冻结项复制进 style guide 时改样。某一决定同时涉及译名和句子时，三处都要改到一致。

## 只改文字，不改图（t125u）

- 你只审校和修改 Markdown 正文，以及上述三类规范／词表。
- 不要修改配图、图表、SVG，也不要运行或新增任何图片生成、SVG 处理脚本。
- 若发现某张图需要修改：记录图号、文件位置和建议改动点，在汇报中单列「图像问题」，由用户发专门指令交回主 Agent 处理。
- 交接套件与交付包都不含图片，也不含绘圆工具。

## 编辑标准

- 读者是中文母语者，目标是可出版的自然中文，同时严格忠实已核原文（泰语，其次巴利，再次英译；经文以巴利为准）。
- 有特别理想且有依据的写法就改；没有把握就商量，不牵强。
- 每个改动、每个特意不改、每个只改一部分的决定，都要在本轮差异 HTML 里写清理由和出处。
- 全段重读每一个改过的段落，并核对相关的前后文、脚注和术语呼应。
- 不要为了「中文（巴利）：」的格式去发明未经核实的标准译名。

## 冻结与禁区

- 结构计数保持：引文 6275、AIPali 3300、注释 2120、内部链接 4240、硬换行 4131、列表 695；URL、ID、CSS、图片字节不变。
- 记号批次保护的 141 处／11 组（含 Dhamma/dhamma 等）不得顺手改大小写。`nibbuta`、P432 未映射、未核说话人标记，保持待决议。
- R027 已于 reader-13 解除（佛法优先，逐处对照泰文，见 reader-style-guide R13-1）；R039 仍不重开；不改标题／TOC（除非新的明确授权），不 push。
- 本地提交：`git -c user.name=bd -c user.email=bd@local`，不设置全局身份。

## 交付

- 最新完整 43 个书籍 MD 的 zip，仓库相对路径，仅 MD，无图、无 CSS、无额外文档。
- 本轮暗色完整语境差异 HTML。
- 内部更新三类规范文档与证据账本。
- 汇报须区分：已改、有意保留、待用户决定、因出处不足而无法确定。图像问题单列。

## 读者润色（reader 轮次）开工必读
先读 `reader-workflow.md`（两遍法、HTML 必备内容），再读 `reader-notes.md`、`reader-style-guide.md`（含 R12 规则）、`revision-guide.md` 末节和 `glossary-final.csv` 的 reader-12 各行。

全书批次见 `PROJECT-PLAN.md`；每批开工先确认本批文件、跨章事项和质量闸门。
