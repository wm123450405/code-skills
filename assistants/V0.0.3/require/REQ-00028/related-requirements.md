# 关联需求 — REQ-00028

更新时间:2026-06-10

## 关联项 1:本仓库已有 10 个 `code-*` 技能(全版本)

- **来源**:`./plugins/code-skills/skills/*/SKILL.md`
- **关联点**:`code-answer` 的工具集(只读)、屏显契约、与 `code-require` 的输入/输出差异
- **影响**:本需求必须**沿用**既有 `code-dashboard`(只读型)的范式,工具集限定 `Read` / `Glob` / `Grep`,**不**调用 `Write` / `Edit` / `Bash`
- **影响**:`code-require` 走"版本感知 + 写入 RESULT.md"路径;`code-answer` 走"只读查询 + 屏显报告"路径,二者职责不重叠
- **正交性**:与 `code-dashboard`(状态查询)横向正交 — 一个查"做了什么",一个查"功能是什么"

## 关联项 2:`code-init` 创建的基线需求(`require/EXISTING-NNN/RESULT.md`)

- **来源**:`./assistants/V0.0.0/require/EXISTING-001/` ~ `EXISTING-010/RESULT.md`
- **关联点**:`code-answer` 的**主输入源之一**(用户 args 明确要求)
- **影响**:`code-answer` 必须能够按"功能名 / 关键字"匹配到对应的 `EXISTING-NNN/RESULT.md`,并以引用形式呈现
- **路径约束**:跨版本扫描,涵盖 `./assistants/*/require/EXISTING-*/RESULT.md`

## 关联项 3:`code-require` 登记的开发需求(`require/REQ-NNNN/RESULT.md`)

- **来源**:`./assistants/V0.0.1` / `V0.0.2` / `V0.0.3` 下全部 `require/REQ-*/RESULT.md`
- **关联点**:`code-answer` 的**主输入源之一**(用户 args 明确要求)
- **影响**:扫描时需覆盖**所有历史版本**(V0.0.1 ~ V0.0.3),不限于当前激活版本
- **关联字段**:`RESULT.md` 内 §1 需求概述 / §4 功能需求 / §13 变更记录,均是回答的引用素材

## 关联项 4:`code-dashboard` 技能(最接近的范式)

- **来源**:`./plugins/code-skills/skills/code-dashboard/SKILL.md`
- **关联点**:工具集、屏显契约、版本上下文检测、幂等性
- **影响**:`code-answer` **沿用** `code-dashboard` 的以下契约:
  - **不**调用 `Write` / `Edit` / `Bash`
  - 多次执行幂等
  - 屏显报告总行数有限(用户友好)
  - 错误信息统一前缀(`✗` / `⚠`)
- **差异**:`code-dashboard` 按"需求编号"查询状态,`code-answer` 按"功能关键字"查询功能逻辑
