# 偏离记录 — TASK-BUG-00004-00004

- 版本:V0.0.3
- 缺陷编号:BUG-00004
- 任务类型:文档
- 创建:2026-06-22 22:50

## 偏离 1:PLAN.md 标题写"6 个技能"但涉及文件模块列出 7 个

- **类别**:文档字面歧义
- **依据**:
 - PLAN.md §3 TASK-BUG-00004-00004 标题:`[文档] 其他 6 个技能旁路验证`
 - PLAN.md §3 TASK-BUG-00004-00004 目标:`对 code-require / code-design / code-check / code-plan / code-fix / code-init / code-rule 这 6 个技能的过程文档表做静态校验`
 - PLAN.md §3 TASK-BUG-00004-00004 涉及文件模块(列出 7 个):
 1. `plugins/code-skills/skills/code-require/SKILL.md`
 2. `plugins/code-skills/skills/code-design/SKILL.md`
 3. `plugins/code-skills/skills/code-check/SKILL.md`
 4. `plugins/code-skills/skills/code-plan/SKILL.md`
 5. `plugins/code-skills/skills/code-fix/SKILL.md`
 6. `plugins/code-skills/skills/code-init/SKILL.md`
 7. `plugins/code-skills/skills/code-rule/SKILL.md`
- **实际做法**:本任务**按"涉及文件模块"字面遍历 7 个技能**(而非标题"6 个"),产出 `side-skill-verification.md` 报告 7 行
- **偏离理由**:
 1. 标题"6 个"是 PLAN.md 字面歧义(可能漏数了)
 2. **"涉及文件模块"是 plan-conventions §规则 1 强约束**(文件级而非数字级),更具权威性
 3. BUG-00004 详细设计 §6 末"其他技能旁路验证结论" 也按 7 个技能列(本报告与详细设计字面 100% 一致,详见报告 §4)
- **影响**:
 - **正面**:覆盖更全(不漏 `code-rule` 技能);与详细设计字面一致
 - **负面**:与 PLAN.md 标题字面"6 个"不一致(但 PLAN.md "涉及文件模块"字面是 7 个,本报告以"涉及文件模块"为准)
- **授权**:用户口头确认(沿用 T-001 ~ T-003 末尾兜底提交模式)
- **时间**:2026-06-22 22:50

## 偏离 0:无偏离(NFR-3 零规范变更)

- T-004 严格按 PLAN.md §3 TASK-BUG-00004-00004 关键变更执行
- 全部产出物在 BUG-00004 详细设计 §4 模块 3 + §6 末"其他技能旁路验证结论"边界内
- 7 个技能全部**不**修改 SKILL.md(沿用"不动修改任何 6 个技能 SKILL.md"原则,扩展为 7 个,详 §偏离 1)