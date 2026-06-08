# 模块拆分 — REQ-00027

## 修改 1:`plugins/code-skills/skills/code-fix/SKILL.md`(纯登记型重写)

- **路径**:`plugins/code-skills/skills/code-fix/SKILL.md`
- **状态**:修改既有
- **职责**:缺陷登记 + 跟踪(纯登记型)
- **关键变更**:
  - §"目标":新增"本技能仅产出 `fix/<BUG-NNN>/RESULT.md`,不实施代码改动、不产出 `fix-plan.md`、不推进'修复规划中'及之后状态"
  - §"适用场景":补"修复流程入口"——用户调 `code-fix` 登记 BUG 后,需调 `code-plan` / `code-it` / `code-check` 推进后续
  - §"工作目录约定":删除"fix-plan.md" / "fix-work-log.md" / "fix-test-results.md" 等下游文件目录结构(本技能不产出)
  - §"工作流程 步骤 4":候选目标状态缩减为"报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞"
  - §"工作流程 步骤 5":删除"→ 修复规划中"等推进提示;改为"若需推进,请先调 `code-plan` / `code-it` / `code-check`"
  - §"工作流程 步骤 6":保留"修复日志 + 变更记录"区段(状态变更仍记录)
  - §"工作流程 步骤 9":引导改为"调 `code-plan` / `code-it` / `code-check` 推进后续状态"
  - §"不要做的事":新增"不产出 `fix-plan.md`"(沿用 `code-require` 模式)
- **对外暴露的接口**:无新增
- **依赖**:无
- **关键决策**:沿用 `code-require` 纯登记型模式;不再产出 `fix-plan.md`(由 `code-plan` 产出)
- **符合的规范**:`skill-conventions.md` §规则 1 满足(frontmatter 0 改)

## 修改 2:`plugins/code-skills/skills/code-auto/SKILL.md`(模式 C 增加 + BUG 路径子技能调用表)

- **路径**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **状态**:修改既有
- **职责**:自动开发编排(扩展)
- **关键变更**:
  - §"输入" 步骤 1 "模式识别":增加"模式 C"(`^BUG-\d{5}$` 首段匹配 → BUG 路径)
  - §"子技能调用表" 步骤 4:扩展 BUG 路径子技能表
    - 步骤 1:`code-plan <BUG-NNN>` → 产出 `fix-plan.md`
    - 步骤 2:`code-it <BUG-NNN>` → 产出 `fix-work-log.md` 等
    - 步骤 3:`code-unit <BUG-NNN>`(条件触发) → 产出 `fix-test-results.md`
    - 步骤 4:`code-check <BUG-NNN>` → 产出 `REVIEW-REPORT.md`
    - 步骤 5:解析"必须改"列表
    - 步骤 6:派生任务循环
    - 步骤 7:写 `fix/<BUG-NNN>/auto-report.md`
  - §"附加约束":沿用 REQ 路径的"自动选推荐项"
  - §"边界与异常":新增 E-18 "BUG 路径模式 C 错配"等
- **对外暴露的接口**:无新增
- **依赖**:`code-plan` / `code-it` / `code-unit` / `code-check`(本轮不修改)
- **关键决策**:模式识别表扩展与现有 A / B 模式正则互不冲突
- **符合的规范**:`module-conventions.md`(沿用既有子技能编排模式)

## 复用

- `code-plan/SKILL.md` 缺陷分支(步骤 19-28):沿用既有
- `code-it/SKILL.md` 缺陷分支(步骤 17-25):沿用既有
- `code-unit/SKILL.md` 任务分支(守卫"项目可测性"):沿用既有
- `code-check/SKILL.md` 任务分支(沿用 `code-review` 能力):沿用既有

## 新增

- 无
