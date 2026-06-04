# 澄清记录 — REQ-00005(plan 阶段)

更新时间:2026-06-04 16:30
版本:V0.0.2

> 本文件记录**详细设计(code-plan)阶段**新增的澄清/确认项。
> 上游澄清(全部 2 处):
> 1. `require/REQ-00005/clarifications.md`(Q-1 ~ Q-8)— 需求阶段
> 2. `design/REQ-00005/clarifications.md`(Q-9 ~ Q-11 + 继承 Q-1~Q-8)— 概要设计阶段

## 2026-06-04 16:30(本轮)

### 状态总览
- **无新阻塞项**:本计划阶段无需新增澄清
- **无规范 vs 设计冲突**:13 个规范文件全部 100% 合规(继承 design 阶段 + 计划阶段无新增违反)
- **无设计 vs 实现冲突**:4 个任务的拆分粒度与概要设计 §13.3 预想任务列表一致

### plan 阶段对上游澄清的继承(完整链路)

| 阶段 | Q 编号 | 锁定/采纳 | 计划阶段继承 |
| --- | --- | --- | --- |
| require | Q-1(版本不一致时选哪个) | 锁定 A | ✅ 完整继承为步骤 0b(FR-2.AC-2.3) |
| require | Q-2(`git pull` 失败) | 锁定 A | ✅ 完整继承为 E-2/E-3/E-4 |
| require | Q-3(commit message 生成) | 锁定 A | ✅ 完整继承为步骤 N 弹窗(FR-3.AC-3.4) |
| require | Q-4(`code-it` 边界) | 锁定 B | ✅ 完整继承为 NFR-7 + 步骤 N 实现 |
| require | Q-5(`commit-conventions.md`) | 未采用 | ✅ 留 follow-up(本计划不填充) |
| require | Q-6(`.gitignore`) | 默认 | ✅ 完整继承(本计划不感知) |
| require | Q-7(CLAUDE.md 追加) | 未采用 | ✅ 留 follow-up(本计划不追加) |
| require | Q-8(commit 格式) | 默认 | ✅ 完整继承(`interface-specs.md §5 commit message 模板`) |
| design | Q-9(`commit-conventions.md` 填充) | 留 follow-up | ✅ 不阻塞本计划 |
| design | Q-10(CLAUDE.md "AI 工作约定") | 留 follow-up | ✅ 不阻塞本计划 |
| design | Q-11(README 同步) | 留 follow-up | ✅ 不阻塞本计划 |

### plan 阶段对上游"技术实现细节"的具体化

本计划**不**新增澄清,但对上游设计的"技术实现细节"做了**显式化**(非"新增决策",而是"明确已有决策的具体落地点"):

| 已有决策 | 计划阶段具体化 | 影响 |
| --- | --- | --- |
| **FR-2.AC-2.3 弹窗 3 选 1** | `interface-specs.md §步骤 0b` 给出完整弹窗 YAML(label / description / 数量 / 选项顺序) | 供 `code-it` 阶段直接落地 |
| **FR-3.AC-3.4 弹窗 3 选 1** | `interface-specs.md §步骤 N` 给出完整弹窗 YAML + preview 字段 | 供 `code-it` 阶段直接落地 |
| **NFR-3 硬中断** | `module-details.md §1.3.2 步骤 0b` 步骤 4 选 A → 调 `code-version` 后**退出** `code-require`(不续跑) | 显式化"退出"语义 |
| **NFR-8 拉取后状态** | `module-details.md §1.2.2 步骤 0a` 步骤 4 `Read .current-version` 显式列出"立即"字样 | 显式化"立即"语义 |
| **NFR-4 幂等** | `interface-specs.md §步骤 N` 步骤 1 → 步骤 2 转换条件显式列出 | 显式化"空跳过"语义 |
| **Q-4 锁定 B(并存)** | `module-details.md §1.4.2 步骤 N` 步骤 1 收集 `git status --porcelain` 输出,**不**特判"已 commit 文件" | 显式化"自然跳过"实现 |
| **任务编号 5+5 位** | `data-changes.md §4` + `module-details.md §4.3` 显式列出 4 个任务编号 | 显式化编号分配 |

### 计划阶段无新增冲突

- 规范 vs 设计:0(继承)
- 需求 vs 设计:0
- 设计 vs 设计(plan vs design):0
- 代码 vs 计划:0
- plan 阶段新引入的不确定项:0(已具体化的 7 个细节**不**算"不确定项",而是"显式化")

### 任务编号分配的明确性

| 维度 | 来源 | 计划阶段遵循 |
| --- | --- | --- |
| 格式 | `encoding-conventions.md §规则 1 + 3` | `TASK-REQ-NNNNN-NNNNN` |
| 父级 | 本需求 `REQ-00005` | ✅ |
| 序号 | 父级内独立递增 00001 ~ 00004 | ✅ |
| 不重用 | 已废弃编号不重新分配 | ✅(本计划首次拆分,无废弃编号) |
| 跨版本对照 | V0.0.1 `REQ-NNN` 3 位 → V0.0.2 `TASK-REQ-NNNNN-NNNNN` 5+5 位 | ✅ 严格遵循 V0.0.2 实践(`migration-mapping.md §规则 1` 2026-06-04 09:50 全量落地) |
