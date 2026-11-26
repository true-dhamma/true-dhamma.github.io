# Markdown 模糊定位器（只读）

`md_fuzzy_locator.py`：将 PDF 粘贴片段定位到原 Markdown 文件及行号，返回按相似度排序的候选和**未经修改的原始 MD 上下文**。Python 3.10+，仅标准库，无需安装依赖。**没有编辑功能，也绝不把命中结果自动应用到书稿。**

## CLI

```bash
python3 /workspace/bd-audit/tools/md_fuzzy_locator.py \
  '中道先导：正见
生起的内在因缘' --label P10 --id M-LOC-01

# 多行片段建议先存为 UTF-8 文件，也可通过标准输入传入
python3 /workspace/bd-audit/tools/md_fuzzy_locator.py \
  --query-file /workspace/excerpt.txt --pdf-footnotes \
  --label P10 --id M-LOC-02 --top 5 --context 2

# 缩小到某章；JSON 包含原文字符偏移、起止行号、起始列、原始上下文
python3 /workspace/bd-audit/tools/md_fuzzy_locator.py \
  '真理并不局限于婆罗门与《吠陀》（Veda）的教条，而是客覌和普遍的' \
  --glob awakened-beings.md --json
```

- 默认目录 `/workspace/bd-thai-all/_buddhadhamma`；`--root` 可更换目录，`--glob '**/*.md'` 可递归。
- `--label P10` 保留用户 PDF 页号，`--id` 保留人工问题/解决编号；两者原样回显，不进入匹配。不要把页码直接混入正文查询。
- `--top` 默认 5；`--context` 默认前后各 1 个原文行；`--min-score` 默认 0.45。
- 退出码：0 找到候选；1 无候选；2 参数或读文件错误。

## 归一化与安全边界

- 合并 PDF 换行、空白影响；使用 Unicode NFKC、casefold，兼容全角及组合附标；忽略标点，保留汉字、字母、数字及组合附标。
- 去掉常见 Markdown 语法、链接 URL/属性，**保留链接显示文字**；兼容目标 URL 内平衡括号，HTML 标签与实体，参考链接和 front matter。
- 自动去掉本书自定义注码、`[^name]` 注码和脚注回链/属性 ID。**脚注的实际说明文字仍可检索**，不会整段删除。
- PDF 粘贴的 `[73]`、`【12】`、上标数字，只有显式 `--pdf-footnotes` 才去掉，避免默认误删有效数字；启用后也不删除普通年份、DN 16 等数字。若方括号数字本来就是正文，请不要启用。
- 每个规范化字符保留原文字符偏移映射，支持原始文件/行/列及上下文回溯；JSON 偏移从 0 开始、末端不含，行列从 1 开始。
- 先找归一化精确命中；否则用分布式字符锚点提出候选窗口，再以局部 `SequenceMatcher` 对齐并按相似度降序排序，重叠候选去重。

**相似度不是正确概率。** 忽略标点可能合并不同结构，常见短语可能多处出现；精确命中只表示归一化文本相同。推荐查询 15–200 字连续正文，必须阅读完整原文上下文核对。工具是保守的常见 Markdown 处理器，不是完整渲染器；不能还原 PDF 阅读顺序、复杂表格/嵌套链接或严重 OCR 错字。近似候选每个锚点每文件最多 80 次、总计精排 180 个窗口，极常见片段可能漏召回；换更独特的片段或缩小范围。少于 4 字或超过 4000 字的归一化查询会被拒绝。不访问网络，不写书稿，不产生自动修正。

## 测试

```bash
cd /workspace/bd-audit/tools
python3 -m unittest -v test_md_fuzzy_locator.py
```

2026-11-18（Asia/Shanghai）实测 **14/14 通过**，详见 `test-results.txt`。包含本书《吠陀》段落、梵行段落、ch15 定稿标题、真实 AIPali 显示文本的 PDF 断行/注码噪声、模拟 OCR 错字、Unicode 映射与全书 CLI 排序；测试前后对所有书稿文件做 SHA-256 核对，确保未改动。实际书稿集成测试依赖当前本地书稿；未来行号改变时应人工核实并更新测试锚点，不自动改书。
