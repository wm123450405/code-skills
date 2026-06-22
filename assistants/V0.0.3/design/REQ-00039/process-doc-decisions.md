# 过程文档生成判定 — REQ-00039

更新时间:2026-06-22 14:30
版本:V0.0.3

## 判定依据

| 过程文档 | 准则 | 判定 | 理由 |
| --- | --- | --- | --- |
| `materials-index.md` | 始终生成 | **生成** | 项目级规范登记是核心(13 规范文件全部存在) |
| `design-notes.md` | 始终生成 | **生成** | 设计权衡笔记是核心(7 个关键设计问题 + 候选方案对比) |
| `module-breakdown.md` | 模块数 ≥ 2 → 生成 | **生成** | 本设计模块数 = 5(共享库 ×2 + SKILL.md ×2 + 模板 ×1)≥ 2 |
| `dependencies.md` | 依赖 ≥ 1 → 生成 | **不生成** | 本需求**不**新增三方依赖(沿用既有 tokei/cloc 系统命令);**不**修改 `code-it` / `code-check` 既有依赖 |
| `related-designs.md` | 关联设计 ≥ 1 → 生成 | **生成** | 关联 REQ-00038 / REQ-00037 / REQ-00034 / REQ-00022 共 4 个同版本设计 |
| `rule-compliance.md` | 规范存在且有内容 → 生成 | **生成** | 13 规范文件全部存在,自检 14 条全部满足 |
| `clarifications.md` | 本轮有用户问路 → 生成 | **不生成** | code-auto 上下文,1 轮 `AskUserQuestion` 全部跳过(采纳 `--balanced` 默认) |
| 看板"变更记录" | 本轮有追加 → 生成 | **生成** | 本轮需在 `<版本号>/RESULT.md` §"概要设计清单"追加本条 + §"变更记录"追加 1 条 |

## 决策结果

存在"不生成"判定 2 项(`dependencies.md` / `clarifications.md`),按 `code-design` SKILL.md §"过程文档自适应判定"小节规则,需写本文件记录决策理由。

**"不生成"详情**:

1. **`dependencies.md`**:**不**生成 — 本需求是 Markdown 自然语言改造,**不**新增 Python / Rust / JS 等运行时依赖(沿用既有 tokei/cloc 系统命令,本仓库不安装)。既有 `code-it` / `code-check` 的依赖(无外部 Python 包 / Node 模块)保持不变。
2. **`clarifications.md`**:**不**生成 — code-auto 上下文已检测(`./assistants/.code-auto-running` 存在),`code-design` 步骤 0b.0 自动采纳 `--balanced` 默认,**不**触发 `AskUserQuestion`(沿用 REQ-00020 + BUG-00001 D-5 修订)。

## 不变量(NFR)

- **不**修改 `code-design` frontmatter(L1-3 字节级保留)
- **不**修改既有"## 工作流程"小节
- **不**修改"## 不要做的事"小节