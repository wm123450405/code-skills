# 关联需求 — REQ-00031

## REQ-00030(同版本 V0.0.3)— 优化 /code-design 与 /code-plan 职责分离
- **关联点**:本需求是 REQ-00030 的"姐妹需求",共同收敛"任务粒度 / 职责边界"
- **影响**:沿用 REQ-00030 的 INV-1~INV-9 字节级保留约束 + §8.10/8.11/8.12 三新校验点
- **来源**:`./assistants/V0.0.3/require/REQ-00030/RESULT.md` + `design/REQ-00030/RESULT.md` + `plan/REQ-00030/PLAN.md`

## REQ-00020(V0.0.2)— code-design / code-plan 步骤 0b 7 维度问路
- **关联点**:"设计目标"小节机制
- **影响**:本需求**沿用**其"`design/.../RESULT.md` 顶部 ## 设计目标"小节 + `code-plan` 步骤 0b 自适应问题数"机制
- **来源**:`./assistants/V0.0.2/plan/REQ-00020/PLAN.md`

## REQ-00014(V0.0.2)— 架构骨架作为首个任务(条件性)
- **关联点**:`code-plan/SKILL.md §步骤 10A "架构任务作为首个任务(条件性)"` 子段
- **影响**:本需求**字节级保留**此子段;不重写
- **来源**:`./assistants/V0.0.2/plan/REQ-00014/PLAN.md`

## REQ-00017(V0.0.2)— 拆任务约束(实际产出候选集)
- **关联点**:`{代码改写, 测试编写, 文档改写, 数据迁移, 配置变更, 部署脚本}` 候选集
- **影响**:本需求"移除 `测试` 类型"是 REQ-00017 候选集的具体子项修正;`测试编写`作为候选**仍有效**,但**不**由 `code-plan` 任务清单承担(由 `code-unit` 承担)
- **来源**:`./assistants/V0.0.2/require/REQ-00017/RESULT.md` + `code-plan/SKILL.md §步骤 10A "拆任务约束"`

## REQ-00007(V0.0.2)— code-auto 任务循环步骤 4.b 原"code-unit 是否调用"逻辑
- **关联点**:`code-auto/SKILL.md §步骤 4` 任务循环步骤 4.b
- **影响**:本需求**改写**为"永不再调 code-unit"(原逻辑变"恒等跳过")
- **来源**:`./assistants/V0.0.2/plan/REQ-00007/PLAN.md`

## REQ-00027(V0.0.3)— code-auto BUG 路径子技能调用表
- **关联点**:BUG 路径步骤 1-7 子技能调用表
- **影响**:**字节级保留**;BUG 路径不涉及本需求
- **来源**:`./assistants/V0.0.3/plan/REQ-00027/PLAN.md`

## BUG-00001(V0.0.3)— 脏标记文件方案 A3
- **关联点**:`./assistants/.code-auto-running` 标记文件
- **影响**:**字节级沿用**;`code-auto` 步骤 0b 设置 + 步骤 7 清理
- **来源**:`./assistants/V0.0.3/fix/BUG-00001/RESULT.md` + 4 个被改 SKILL.md 步骤 0b.0
