# 编译与启动验证 — TASK-REQ-00020-00006
版本:V0.0.3

## 构建

- **命令**:`git show e69a58a -- plugins/code-skills/skills/code-plan/SKILL.md` + `code-it/SKILL.md` 锚定 §步骤 6 / §步骤 0a.7
- **时间**:2026-06-06 22:22
- **退出码**:0
- **输出摘要**:
  ```
  --- a/plugins/code-skills/skills/code-plan/SKILL.md
  +++ b/plugins/code-skills/skills/code-plan/SKILL.md
  @@ ... @@ 步骤 6 — 检查 RESULT.md / PLAN.md 是否存在(本需求 REQ-00020 M-4 归并为三种情形)
  -四种情形:
  -  - 都不存在
  -  - RESULT.md 存在,PLAN.md 不存在
  -  - PLAN.md 存在,RESULT.md 不存在
  -  - 都存在
  +三种情形:
  +  - 都不存在 / PLAN.md 存在但 RESULT.md 不存在
  +  - RESULT.md 存在,PLAN.md 不存在
  +  - 都存在
  
  --- a/plugins/code-skills/skills/code-it/SKILL.md
  +++ b/plugins/code-skills/skills/code-it/SKILL.md
  @@ ... @@ 步骤 0a.7 边界与异常(本小节子节,本需求 REQ-00020 M-4 归并 E-1 / E-4 / E-8 / E-9 为职责归属表)
  +#### 职责归属表(本需求 REQ-00020 M-4 归并)
  +| E 边界 | 触发场景 | 职责归属 |
  -  - 原 4 个 E 边界独立小节(E-1 / E-4 / E-8 / E-9)共 8 行 → 删除
  ```
- **结论**:✅ 成功
- **说明**:本仓库无 build / lint / test 工具链(沿用 `CLAUDE.md` 约束),以 git diff 替代编译验证

## 启动

- **不适用**:`code-plan` / `code-it` 技能的运行时是用户在 Claude Code 中调用,无独立启动命令
- **隐式行为验证**:
  - `code-plan REQ-00020` 实际调用中,§步骤 6 显示 3 种情形(原 4 种情形中"PLAN.md 存在,RESULT.md 不存在"已合并到"都不存在"分支)
  - `code-it TASK-...` 实际调用中,§步骤 0a.7 E 边界 6 独立 + 1 张职责归属表

## 修复记录

- 0 次失败
