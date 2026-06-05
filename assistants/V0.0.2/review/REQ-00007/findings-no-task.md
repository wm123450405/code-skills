# 未派生任务的发现 — REQ-00007

版本:V0.0.2
需求:REQ-00007
时间:2026-06-05 11:45
评审:wangmiao

## 总结

本次评审发现 **0 必须改 + 4 建议改 + 0 可选**。

**决策:4 条建议改全部归类为"可选"**,**不派生"审查改修"任务**。

**理由**:
1. 4 条都是"SKILL.md 缺规范/澄清 token 引用" — 文档级微调,无功能/安全/设计影响
2. 派生任务会消耗看板 1 行 + 派生 1 个新任务,投入产出比低
3. 由用户后续手动追加或在 V0.0.3 集中处理
4. 依据:`code-review` SKILL.md §9 "建议改" → 询问用户:派生 / 留作 follow-up → 本次选择"留作 follow-up"

## 类别:可选(原"建议改"降级)

### T-001:OPT-001 — SKILL.md 缺 Q-4 引用

- **位置**:`plugins/code-skills/skills/code-auto/SKILL.md`(全文搜索)
- **类别**:可维护性 / 文档可追溯
- **描述**:SKILL.md 中未显式引用澄清项 `Q-4`(所有 `AskUserQuestion` 自动选推荐项)。Q-4 已在 `require/clarifications.md` 锁定 A,但 SKILL.md 中应保留引用以便读者追溯。
- **建议**:在 §"## 工具使用约定"或 §"## 工作流步骤" 增加引用:
  > "Q-4 锁定(上游 `require/clarifications.md`):所有 `AskUserQuestion` 自动选推荐项"
- **影响**:0;读者体验略改善
- **授权**:N/A(归类为"可选"不派生)
- **状态**:留作 follow-up

### T-001:OPT-002 — SKILL.md 缺 Q-5 引用

- **位置**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **类别**:可维护性 / 文档可追溯
- **描述**:SKILL.md 未显式引用 Q-5(不引入批量模式)。Q-5 已在 `require/clarifications.md` 锁定 A。
- **建议**:在 §"## 不要做的事" 增加引用:
  > "Q-5 锁定:不引入批量模式,子技能按原设计运行"
- **影响**:0
- **状态**:留作 follow-up

### T-001:OPT-003 — SKILL.md 缺 `doc-conventions.md` 引用

- **位置**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **类别**:可维护性 / 规范可追溯
- **描述**:SKILL.md 在 §"## 关联需求"未引用 `doc-conventions.md` 规范(虽然 T-003 实施时已严格遵循)。
- **建议**:在 §"## 关联需求" 增加:
  > "`doc-conventions.md §规则 1`:README 中英同次提交 + 结构对仗(本技能不触达,仅作为'已通过此规范'的引用)"
- **影响**:0
- **状态**:留作 follow-up

### T-001:OPT-004 — SKILL.md 缺 `marketplace-protocol.md` 引用

- **位置**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **类别**:可维护性 / 规范可追溯
- **描述**:SKILL.md 在 §"## 工具使用约定"未引用 `marketplace-protocol.md` 规范(虽然 T-002 实施时已严格遵循)。
- **建议**:在 §"## 工具使用约定" 增加:
  > "`marketplace-protocol.md §规则 1`:`$schema` / `name` / `version` 必填,`source` 必须 `./` 开头,`skills` 必须是 `./` 开头的相对路径数组(本技能不触达,仅作为'已通过此规范'的引用)"
- **影响**:0
- **状态**:留作 follow-up

## 整体结论

- **0 必须改** = 无阻塞
- **4 可选** = 4 条 token 引用缺失(归类为可选,无功能影响)
- **0 派生"审查改修"任务**
- **评审结论:⚠️ 条件通过 — 可合并**

## 后续

由用户在后续手动追加 OPT-001 ~ OPT-004,或集中到 V0.0.3 修复。
