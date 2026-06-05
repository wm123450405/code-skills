# 三方依赖 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 复用既有依赖

**无**。本项目(`code-skills`)是 Claude Code 技能集合,**不**包含任何运行时技术栈(`plugins/code-skills/CLAUDE.md` §需与用户确认的约定)。

本需求**仅**使用既有工具:
- `Bash`(无新增 — 步骤 0a 拉取沿用 REQ-00005)
- `Read` / `Write` / `Edit`(无新增 — 步骤 0b 写入"## 设计目标"小节)
- `AskUserQuestion`(既有 — 步骤 0b 触发用户确认)
- `Glob` / `Grep`(辅助定位,无新增)

## 新增依赖

**无**(NFR-1 强约束)。

## 拒绝引入的依赖及理由

- **任何 npm/pip/cargo 包** — 拒绝理由:本项目**无**运行时技术栈,引入包管理器会破坏"Claude Code 技能集合"定位
- **任何运行时框架** — 拒绝理由:`plugins/code-skills/CLAUDE.md` 明确"不包含任何源代码、构建系统、测试框架、Lint 工具或包管理配置"
- **任何 Lint / 测试工具** — 拒绝理由:同上
- **任何第三方 CLI 工具** — 拒绝理由:Claude Code 工具集(`Bash` / `Read` / `Write` / `Edit` / `AskUserQuestion`)已足够覆盖本需求
- **`code-rule` 沉淀"设计目标"字段约定(派生建议)** — 拒绝理由:本需求**不**触发 `code-rule` 调用,仅在 Q-6 / Q-9 建议派生(由用户决定)
- **`code-auto` 升级(派生建议)** — 拒绝理由:NFR-5 强约束"`code-auto` 现行'总选推荐项'**不**变";`code-auto` 已能"总选推荐项"覆盖本需求

## 维护说明

- 本需求**无**新增依赖,故无维护责任
- 若未来衍生需求需引入依赖,需在 `dependency-conventions.md §规则 1`(待添加)落地后,按其条款评估
