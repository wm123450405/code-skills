# 改修总结 — TASK-REQ-00044-00007 · 适配 code-rule/code-merge/code-dashboard 到新结构

## 1. 任务概述
- 所属需求:REQ-00044
- 任务类型:修改
- 涉及文件:3 个修改文件

## 2. 改动内容

| 文件 | 说明 |
| --- | --- |
| `code-rule/SKILL.md` | 更新技能名引用(code-design→code-req, code-version→code-ver, code-require→code-req);更新工作目录图(新增 req/fix);更新衔接章节 |
| `code-merge/SKILL.md` | 更新工作目录(5目录→2目录 req/fix);更新FR-4.1冲突文件模式(新路径);更新FR-6看板自检(5区段→2区段);更新技能名引用(code-version→code-ver, code-publish→code-ver --publish, code-auto→code-req --auto);更新变更记录 |
| `code-dashboard/SKILL.md` | 大幅重构:更新工作目录(require/plan/design→req/fix);更新步骤2数据加载(require/RESULT.md→req/REQUIRE.md, 新增PROCESS.md);更新步骤3区段解析(5区段→2区段);更新段1进度计算(PROCESS.md阶段追踪);更新段2状态分类(5类状态→PROCESS.md阶段);更新段4建议映射(新技能名);更新段5需求模式(任务清单→阶段进度);更新边界/衔接/工具约定/不要做 |

## 3. 关键决策

- **code-rule**: 最小改动 — 仅更新技能名引用和工作目录图,核心逻辑(Type A/B/C, AskUserQuestion)不变
- **code-merge**: 看板自检从5区段简化为2区段(需求清单+缺陷清单),与简化版RESULT.md对齐;冲突文件模式更新为新的req/fix路径
- **code-dashboard**: 最大改动 — 进度计算从"6步模型"改为PROCESS.md阶段追踪(INIT→REQUIRE→DESIGN→PLAN→CODING→CHECK→DONE);状态分类从看板列派生改为PROCESS.md解析;建议命令从旧技能名更新为新技能名(code-req/code-fix/code-ver)

## 4. 验证结果

- 编译:不适用(纯文档产出)
- 运行:不适用
- 测试:不适用

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 18:00 | v1 | 初始创建 | code-rule/code-merge/code-dashboard 三个 SKILL.md 适配新结构完成 | wangmiao |