# 偏离记录 — TASK-REQ-00004-00001

版本:V0.0.2
时间:2026-06-04 16:40

---

## 本任务**无**代码偏离

本任务是"新增 1 个 Markdown 技能定义文件",无编程语言运行时,无"代码 vs 设计"的偏离语义。设计阶段已识别的 3 项用户授权偏离(本任务不新增子目录 A-1 / 不改 marketplace.json A-2 / 不实现"切历史版本" A-3)已**完整落地**于 SKILL.md:
- A-1:SKILL.md 全文未出现 `templates/` / `checklists/` / `guidelines/` 子目录创建指令
- A-2:SKILL.md 行 51 + 行 311 显式声明"不修改 marketplace.json / plugin.json"
- A-3:SKILL.md `## 不适用` 节明示"想切到历史版本 → 走 code-version"

本阶段新增的 3 项偏离(P-A1 / P-A2 / P-A3)也已**完整落地**:
- P-A1:SKILL.md 段 1 渲染段显式注明"状态字面严格按看板列定义:`待开始` / `进行中` / `已完成` / `已完成(需求分析)` / `已取消` / `阻塞`(V0.0.2 引入'已完成(需求分析)'子状态,**不归一化**到'已完成')"
- P-A2:PLAN.md §6.2 测试状态 = `不适用`;SKILL.md 无单元测试章节(由 `code-plan` 阶段确认,本任务**不**添加)
- P-A3:SKILL.md `## 不适用` 节明确"想看'里程碑'段 → 走 `code-dashboard` 总览模式(本技能需求模式不显示)"

---

## 验证

- ✅ 静态自检 9/9 项通过(详见 `compile-and-run.md`)
- ✅ git status 净度:NFR-6 边界未破(`marketplace.json` / `plugin.json` / 其他 10 SKILL.md 全部未改)
- ✅ 任务编号双格式正则严格按 `encoding-conventions §规则 1/3` 落地
- ✅ 3 项 design 阶段授权偏离 + 3 项 plan 阶段新增偏离**全部落地**

**本任务的"无偏离"是项目规范与设计严格执行的体现**;无任何需要用户授权的偏离需要补记录。
