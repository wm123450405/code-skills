# 缺陷详情 — BUG-00001

- 缺陷编号:BUG-00001
- 所属版本:V0.0.2
- 严重度:**P0**
- 报告人:wangmiao
- 报告时间:2026-06-06 13:45
- 状态:**报告**
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
```

## 变更记录

```
2026-06-06 13:45  缺陷登记  code-fix 创建缺陷 BUG-00001(严重度 P0)  BUG-00001
```

## 根因分析(待调查)

详见 `investigation.md`(本轮尚未调查,根因待定)

**初步假设**:
- `code-auto` 自身**不**传任何特殊参数给子技能(D-8 零修改契约保持)
- 子技能的 `AskUserQuestion` 没有"上下文感知"机制,无法区分"用户在用 `code-auto` 跑"vs"用户手动调子技能"
- 用户回答 Q1:子技能自动检测(推荐) — 需在子技能中增加"调用上下文检测"逻辑
- 可能方案:检查 `process.env` / 父进程 argv / `code-auto` 留下的脏标记文件

## 修复方案(待规划)

详见 `fix-plan.md`(由 `code-plan BUG-00001` 产出)

## 修复实施(待实施)

详见 `fix-work-log.md`(由 `code-it BUG-00001` 产出)

## 验证结果

待修复后填写
