# 澄清记录 — REQ-00002
更新时间:2026-06-03 20:55
版本:V0.0.1

> 本需求 **5 项待澄清 + 1 项已锁定**(在 REQU 阶段记录)。
> design 阶段**未追加**澄清(所有 Q 采用 REQU 文档默认)。
> plan 阶段**未追加**澄清(沿用 design 决策)。
> 本文件用于**追溯** REQU → design → plan 三阶段对各项 Q 的处理。

## REQU 阶段记录的待澄清项(继承自 REQU RESULT.md)

### Q-6:EXISTING-* 是否同步
- **REQU 默认**:(a) 保留默认 — 范围外
- **本设计采纳**:是
- **影响章节**:不变量 §5(INV-5);module-details §T-7
- **处理时间**:2026-06-03 20:14(REQU 阶段)

### Q-7:TASK 编码格式
- **REQU 默认**:**已锁定** v2 G4 新嵌套式(`TASK-REQ-<父级>-NNNNN` / `TASK-BUG-<父级>-NNNNN`)
- **本设计采纳**:是
- **影响章节**:data-changes §"修改实体:TASK 编码格式";不变量 §8 / §9
- **处理时间**:2026-06-03 20:18(REQU v2)

### Q-8:encoding-conventions.md 是否新建
- **REQU 默认**:(a) 新建默认
- **本设计采纳**:是(由 `code-it` 在 T-5 创建)
- **影响章节**:module-details §T-5;data-changes §"新增实体:encoding-conventions.md"
- **处理时间**:2026-06-03 20:14(REQU 阶段)

### Q-9:migration-mapping.md 是否新建
- **REQU 默认**:(a) 持久化默认
- **本设计采纳**:是(由 `code-it` 在 T-6 创建)
- **影响章节**:module-details §T-6;data-changes §"新增实体:migration-mapping.md"
- **处理时间**:2026-06-03 20:14(REQU 阶段)

### Q-10:cache README 提示
- **REQU 默认**:(b) 不加默认
- **本设计采纳**:是(本需求不涉及 cache 改造)
- **影响章节**:无
- **处理时间**:2026-06-03 20:14(REQU 阶段)

### Q-11:实施顺序
- **REQU 默认**:(a) SKILL.md → 模板 → README → 看板 → 新规范 → 迁移 → Grep
- **本设计采纳**:是(design 与 REQU 一致)
- **影响章节**:module-details §T-1 ~ T-7 顺序
- **处理时间**:2026-06-03 20:14(REQU 阶段)

### Q-12:TASK 编码"父级段"是否含 `REQ-` 前缀
- **REQU 默认**:(a) 仅数字段(不含 `REQ-`)
- **本设计采纳**:是
- **影响章节**:不变量 §10;data-changes §"TASK 编码格式"
- **处理时间**:2026-06-03 20:14(REQU 阶段)

## design 阶段无新增澄清

- **理由**:design v1 已采纳所有 REQU 默认;11 子任务预想与 Q-1 ~ Q-12 无冲突
- **时间**:2026-06-03 20:25

## plan 阶段澄清(本阶段新发现/决策 1 项)

### 决策 D-PLAN-1:`code-it` 是否可创建新规范文件
- **问题**:既有事实"`code-it` 不可修改 `rules/`"是否包含"创建"?
- **分析**:
  - "修改" = 改变既有文件内容(Edit 既有文件)
  - "创建" = 写入新文件(Write 新文件)
  - 既有约束描述:"不可修改"
  - 字面解释:"创建" ≠ "修改"
- **本设计决策**:**可创建**(不违反既有约束)
- **授权**:本设计阶段(2026-06-03 20:55)显式授权
- **影响章节**:module-details §T-5 / §T-6;rule-compliance §4
- **后续**:`code-rule` 接管维护新文件
- **记录位置**:`code/REQ-00002-00005/deviations.md` + `code/REQ-00002-00006/deviations.md`

## 待用户后续确认(无)

本设计阶段**无遗留待用户确认项**。所有 REQU 待澄清(Q-1 ~ Q-12)已采纳默认;design 阶段无新增;plan 阶段澄清 1 项已在本设计内决策。
