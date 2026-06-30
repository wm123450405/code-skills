# 改修总结 — TASK-REQ-00044-00005 · 创建 code-fix 技能

## 1. 任务概述
- 所属需求:REQ-00044
- 任务类型:新增
- 涉及文件:2 个新建文件

## 2. 改动内容

| 文件 | 说明 |
| --- | --- |
| `code-fix/SKILL.md` | 缺陷修复全流程技能主文件。合并 code-fix+plan+it+check(缺陷路径)四技能能力,通过阶段执行器串行驱动,支持 --auto 静默模式和 PROCESS.md 断点续跑。DESIGN/PLAN/CODING/CHECK 阶段复用 code-req/references/ |
| `code-fix/references/fix-register.md` | 缺陷登记阶段详细流程。含缺陷编号分配、缺陷要素提取(缺陷描述/触发条件/可能成因/影响范围)、严重程度判定(P0-P3)、BUG.md 撰写原则、版本看板同步 |

## 3. 关键决策

- **阶段顺序差异**:code-fix 为 INIT → DESIGN → PLAN → CODING → CHECK → DONE,与 code-req 的 INIT → REQUIRE → ... 不同,INIT 阶段产出 BUG.md 而非 REQUIRE.md
- **复用 code-req references**:DESIGN/PLAN/CODING/CHECK 四个阶段的详细逻辑通过 `../code-req/references/` 相对路径引用,避免重复维护
- **严重程度判定**:在 INIT 阶段内置 P0-P3 判定标准(P0=系统不可用,P1=核心功能不可用,P2=部分不可用,P3=体验问题),默认 P2
- **与 code-req 的结构对齐**:SKILL.md 约 170 行,采用相同的渐进式加载模式,阶段执行器、PROCESS.md 断点续跑、--auto 静默模式均与 code-req 保持一致
- **fix-register.md 独立**:缺陷登记阶段逻辑独立成文件,与 code-req 的 require.md 平行,在缺陷要素提取(触发条件/可能成因/影响范围)上与需求分析(FR/NFR/AC)有本质差异

## 4. 验证结果

- 编译:不适用(纯文档产出)
- 运行:不适用
- 测试:不适用

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 17:00 | v1 | 初始创建 | code-fix SKILL.md + references/fix-register.md 创建完成 | wangmiao |