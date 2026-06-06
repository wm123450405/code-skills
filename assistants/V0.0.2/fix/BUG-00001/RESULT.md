# 缺陷详情 — BUG-00001

- 缺陷编号:BUG-00001
- 所属版本:V0.0.2
- 严重度:**P0**
- 报告人:wangmiao
- 报告时间:2026-06-06 13:45
- 状态:**修复规划中**
- 当前负责人:wangmiao
- 关联需求:—
- 修复时间:—
- 修复提交:—

## 缺陷标题

code-auto 调用子技能时子技能仍会手...

## 缺陷描述

### 用户原始报告

修复 `/code-auto` 执行时会让手动选择架构设计目标(可维护性、可扩展性等)的问题,应该自动分析并使用推荐选项,无需人工介入。

### 复现步骤

1. 用户输入 `/code-auto "<新需求>"`
2. `code-auto` 步骤 2 调用 `code-design`
3. `code-design` 步骤 0b 触发 `AskUserQuestion`(1-5 问,设计目标 / 功能性 / 扩展性 / 健壮性 / 可维护性)
4. `code-auto` 的"完全无人确认"约束被破坏 — 用户被迫手动选 1-5 个选项
5. `code-auto` 流程**中断**,退出码 ≠ 0

### 期望行为

`code-auto` 调用 `code-design` 时,子技能应**自动**选推荐项,无 `AskUserQuestion` 触发,保持"完全无人确认"约束。

### 实际行为

`code-design` 步骤 0b 触发 `AskUserQuestion`,违反 `code-auto` "完全无人确认"约束,`code-auto` 中断。

## 涉及文件/模块

- `plugins/code-skills/skills/code-design/SKILL.md`(步骤 0b 设计目标确认)
- `plugins/code-skills/skills/code-plan/SKILL.md`(步骤 0b 设计目标确认)
- `plugins/code-skills/skills/code-require/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-fix/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-review/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-merge/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-publish/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-dashboard/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-unit/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-init/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-version/SKILL.md`(其他可能问路场景)
- `plugins/code-skills/skills/code-auto/SKILL.md`(**不**修改 — D-8 零修改契约保持)

## 修复日志

```
2026-06-06 13:45  登记  wangmiao 报告缺陷:code-auto 调用子技能时子技能仍会手动选择架构设计目标
2026-06-06 14:00  修复规划  code-plan 已产出 fix-plan.md(选定方案 A3 脏标记文件 + 4 步修复 + 5 项 R-1~R-5 回归用例 + 13 份规范严守 + 0 待澄清)
```

## 变更记录

```
2026-06-06 13:45  缺陷登记  code-fix 创建缺陷 BUG-00001(严重度 P0)  BUG-00001
2026-06-06 14:00  状态推进  BUG-00001 状态"报告"→"修复规划中"  BUG-00001
```

## 根因分析(已调查)

详 `investigation.md`(本轮已细化根因)

**根因(精准定位)**:
- `code-auto` 的"自动选推荐项"约束**只在 `code-auto` 自己的 prompt 模板中声明**(子技能 prompt 模板注入),但子技能**本身**在执行 `AskUserQuestion` 时没有"我在被 `code-auto` 调用吗?"的检测逻辑
- `./assistants/` 目录下**没有**任何"调用上下文标记"文件,子技能**无法** Read 任何状态以判断"是否在 `code-auto` 上下文中"

## 修复方案(已规划)

详见 [fix-plan.md](fix-plan.md)

**选定方案 A3**(脏标记文件 `./assistants/.code-auto-running`):
- `code-auto` 步骤 0b 设置标记 + 步骤 7 收尾清理标记(用 `try-finally` 模式)
- 子技能(`code-design` / `code-plan` / `code-require` 可选)在触发 `AskUserQuestion` **前**先 Read 标记,存在即跳过
- D-8 修订:从"不传任何特殊参数"→"不传 prompt 参数(状态文件除外)"

## 修复实施(待实施)

详见 `fix-work-log.md`(由 `code-it BUG-00001` 产出)

## 验证结果

待修复后填写
