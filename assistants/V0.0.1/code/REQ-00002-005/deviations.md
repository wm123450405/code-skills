# 偏离记录 — REQ-00002-005
版本:V0.0.1

## 偏离 1:`code-it` 创建新文件(`code-rule` 职责范围内)
- **类别**:任务范围扩展(用户授权的偏离)
- **依据**:
  - 设计要求:PLAN §2.5 "本任务是本需求中**唯一**创建新文件的 2 个任务之一(T-5 + T-6)"
  - 设计要求:PLAN §2.5 边界与异常 "'创建'动作 vs '修改'既有约束 → **不违反**(本设计 D-PLAN-1 已澄清)"
  - 设计依据:`plan/REQ-00002/RESULT.md` §4 决策 D-PLAN-1 "`code-it` 创建新规范文件,授权"
- **实际做法**:
  - `code-it` 在 `./assistants/rules/` 下创建 `encoding-conventions.md`
  - 这通常是 `code-rule` 技能的职责范围
- **偏离理由**:
  - REQ-00002 实施时,`encoding-conventions.md` 规则内容由 REQ-00002 决定,需要在 REQ-00002 落地时同时创建该规则
  - 若等 `code-rule` 创建,会引入"先实施后规范"的逻辑矛盾
  - `code-rule` 创建规则需要"自然语言描述",但本规则的完整定义已在 REQU/PLAN 中,直接落盘更高效
- **影响**:
  - **无不良影响**。`encoding-conventions.md` 创建后,立即被所有 `code-*` 技能读取为强制约束源
  - 后续 `code-rule` 可基于该文件"维护/扩展"具体条款(但本任务**不**动用 `code-rule`)
- **授权**:PLAN §2.5 + design D-PLAN-1 已预先授权
- **时间**:2026-06-04 10:05

## 其他
- 本任务**未做设计偏离**。规范文件内容严格遵循 PLAN §2.5 6 段结构。
- 范围严格限定在 `./assistants/rules/encoding-conventions.md` 1 个新文件,未触及任何既有文件。

## 范围外但被识别的事项(留给后续任务)
- `migration-mapping.md` 创建(由 T-006 单独处理)
- `module-conventions.md` 弃用处理(由 REQ-00003 单独处理)
- 全仓库 Grep 审计(由 T-007 单独处理)
- 看板同步(由 T-008 单独处理)

## 时间
2026-06-04 10:05
