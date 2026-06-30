# 改修总结 — TASK-REQ-00044-00004 · 创建 code-req 技能

## 1. 任务概述
- 所属需求:REQ-00044
- 任务类型:新增
- 涉及文件:1 个新建文件

## 2. 改动内容

| 文件 | 说明 |
| --- | --- |
| `code-req/SKILL.md` | 需求开发全流程技能主文件。合并 code-require+design+plan+it+check(需求路径)五技能能力,通过阶段执行器串行驱动,支持 --auto 静默模式和 PROCESS.md 断点续跑 |

## 3. 关键决策

- **阶段执行器模式**:每个阶段(REQUIRE/DESIGN/PLAN/CODING/CHECK)按统一模式执行:追加 PROCESS.md → 执行阶段逻辑 → 追加 PROCESS.md → 交互确认。非 --auto 模式每阶段 AskUserQuestion 确认
- **渐进式加载**:SKILL.md 精简为 ~170 行,详细逻辑在 `references/`(6 个阶段文档 + 1 个公共流程),按需加载
- **合并五技能**:code-require + code-design + code-plan + code-it + code-check → code-req,单一入口覆盖从需求到代码审查全流程
- **--auto 静默模式**:所有 AskUserQuestion 自动选推荐项,屏幕输出 `[code-req --auto]` 前缀,适用于 CI/无人值守场景
- **PROCESS.md 断点续跑**:追加式记录每阶段进度,中断后重跑从最后记录的阶段继续
- **复用已创建的 references/templates**:TASK-00001(8 个模板)和 TASK-00002(6 个 references)已就绪,本任务仅创建 SKILL.md 编排层

## 4. 验证结果

- 编译:不适用(纯文档产出)
- 运行:不适用
- 测试:不适用

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 16:00 | v1 | 初始创建 | code-req SKILL.md 创建完成 | wangmiao |