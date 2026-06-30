# 改修总结 — TASK-REQ-00044-00002 · 创建 code-req references

## 1. 任务概述
- 所属需求:REQ-00044
- 任务类型:新增
- 涉及文件:6 个新建文件

## 2. 改动内容

| 文件 | 说明 |
| --- | --- |
| `code-req/references/common.md` | 公共流程:版本检测、PROCESS.md 恢复、追加写入、阶段执行器、目录结构、看板同步、交互确认、通用边界 |
| `code-req/references/require.md` | 需求分析阶段:编号分配、材料收集、需求提取、关联检索、用户澄清、REQUIRE.md 撰写、技术选型过滤 |
| `code-req/references/design.md` | 软件设计阶段:需求读取、项目探索、架构构思、模块拆分、接口设计、数据结构、关键流程、方案选型、DESIGN.md 撰写 |
| `code-req/references/plan.md` | 任务排期阶段:任务拆分原则、编号规则、依赖分析、里程碑划分、依赖图绘制、PLAN.md 撰写、双状态模型 |
| `code-req/references/coding.md` | 编码执行阶段:任务解析、前置守卫、任务循环、单任务执行(编码/编译/运行/测试)、TASK-N.md 撰写、错误修复循环、追踪编号禁用规则 |
| `code-req/references/check.md` | 代码审查阶段:材料收集、逐维度审查(8 维度)、发现分类(必须改/建议改/可选)、必须改处理、CHECK.md 撰写、评审结论判定 |

## 3. 关键决策

- **渐进式加载**:每个 reference 文件独立,code-req SKILL.md 按阶段加载对应文件,减少 token 消耗
- **复用设计**:code-fix 将通过相对路径引用 `code-req/references/design.md`、`plan.md`、`coding.md`、`check.md`
- **编码规范继承**:coding.md 中继承了追踪编号禁用规则(来自 REQ-00042)
- **技术选型过滤**:require.md 中明确技术选型类关键词过滤,留待 DESIGN 阶段处理

## 4. 验证结果

- 编译:不适用(纯文档产出)
- 运行:不适用
- 测试:不适用

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 00:00 | v1 | 初始创建 | 6 个 reference 文件创建完成 | wangmiao |