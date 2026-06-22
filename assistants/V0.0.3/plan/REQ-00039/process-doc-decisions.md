# 过程文档生成判定 — REQ-00039

更新时间:2026-06-22 15:00
版本:V0.0.3

## 判定依据

| 过程文档 | 准则 | 判定 | 理由 |
| --- | --- | --- | --- |
| `materials-index.md` | 始终生成 | **生成** | 上游引用 + 规范登记是核心(13 规范文件全部存在) |
| `design-notes.md` | 始终生成 | **生成** | 详细设计权衡笔记是核心(7 个关键设计问题 + 候选方案对比) |
| `module-details.md` | 模块数 ≥ 2 → 生成 | **生成** | 本详细化模块数 = 5(共享库 ×2 + SKILL.md ×2 + 模板 ×1)≥ 2 |
| `interface-specs.md` | 接口数 ≥ 2 → 生成 | **生成** | 本详细化接口数 = 4(`detectLocTool` / `calcLogicLines` / `heuristicLoc` / `code-check-exceed`)≥ 2 |
| `data-changes.md` | 涉及数据库/缓存/状态字段变更 → 生成 | **不生成** | 本需求是 Markdown 自然语言改造,**不**涉及数据库/缓存/状态字段变更 |
| `risk-analysis.md` | 任务数 ≥ 3 → 生成 | **生成** | 本详细化任务数 = 5(共享库 + code-it + code-check + 模板 + 端到端验证)≥ 3 |
| `rule-compliance.md` | 规范存在且有内容 → 生成 | **生成** | 13 规范文件全部存在,自检 15 条全部满足 |
| `clarifications.md` | 本轮有用户问路 → 生成 | **不生成** | code-auto 上下文,1 轮 `AskUserQuestion` 全部跳过(采纳 `--balanced` 默认) |
| 看板"变更记录" | 本轮有追加 → 生成 | **生成** | 本轮需在 `<版本号>/RESULT.md` §"详细设计与任务计划汇总"追加本条 + §"任务清单"追加 5 行 + §"变更记录"追加 1 条 |

## 决策结果

存在"不生成"判定 2 项(`data-changes.md` / `clarifications.md`),按 `code-plan` SKILL.md §"过程文档自适应判定"小节规则,需写本文件记录决策理由。

**"不生成"详情**:

1. **`data-changes.md`**:**不**生成 — 本需求是 Markdown 自然语言改造,**不**涉及数据库表 / 缓存键 / 状态字段的变更。逻辑行 metadata 存储在 `code/<task>/RESULT.md` 的"## 逻辑行统计"小节(Markdown 文本),**不**是数据库/缓存/状态字段变更。既有 `code-it` / `code-check` 的数据模型保持不变。
2. **`clarifications.md`**:**不**生成 — code-auto 上下文已检测(`./assistants/.code-auto-running` 存在),`code-plan` 步骤 0b.0 自动采纳 `--balanced` 默认(沿用 `design/REQ-00039/RESULT.md` 的设计目标),**不**触发 `AskUserQuestion`(沿用 REQ-00020 + BUG-00001 D-5 修订)。

## 不变量(NFR)

- **不**修改 `code-plan` frontmatter(L1-3 字节级保留)
- **不**修改既有"## 工作流程"小节
- **不**修改"## 不要做的事"小节