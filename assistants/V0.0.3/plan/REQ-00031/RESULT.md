# 详细设计 — REQ-00031 优化 /code-plan 任务粒度(内化编译/运行,外移单元测试)

- 需求编码:REQ-00031
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00031/RESULT.md
- 上游概要设计:./assistants/V0.0.3/design/REQ-00031/RESULT.md
- 遵循规范:./assistants/rules/ 下 7 个文件(已逐条对照,无冲突)
- 状态:草稿
- 责任人:wangmiao
- 创建:2026-06-12
- 最近更新:2026-06-12 15:35

## 设计目标

| 维度 | 优先级 |
| --- | --- |
| 整体设计目标 | `--balanced`(`code-auto` 上下文默认,沿用 design) |
| 功能性 | 中 |
| 扩展性 | 低 |
| 健壮性 | 低 |
| 可维护性 | 中 |
| 封装性 | 不适用(本仓库 Markdown 自然语言) |
| 可复用性 | 不适用(本仓库 Markdown 自然语言) |
| 可读性 | 不适用(本仓库 Markdown 自然语言) |

## 1. 概述

本详细设计对 `code-plan` / `code-it` / `code-unit` / `code-auto` 4 个 SKILL.md + `templates/plan.md` 1 个模板的**精确修改点**给出可直接编码的细节;不含伪代码(本需求是 Markdown 文字修订,无算法逻辑)。

**与概要设计的关系**:本详细设计是 `design/REQ-00031/RESULT.md` §5(架构总览)+ §6(功能架构)的展开;每条 FR 都映射到 1 个具体任务的"关键变更"。

**任务粒度**:5 个任务(T-001 ~ T-005),每任务 1 文件,**不**单列"编译运行检测"任务(每任务自身"修改后 Read + INV 字节级校验"已内化为"运行成功"语义);**不**规划"单元测试"任务(本需求主动外移)。

## 2. 上游引用

| 上游 FR | 本详设对应章节 | 对应任务 | 过程文档 |
| --- | --- | --- | --- |
| FR-1 任务完成定义内化"编译/运行成功" | §3.1 | T-001 | module-details.md §模块 1 |
| FR-2 任务类型移除 `测试` | §3.1 | T-001 | data-changes.md §修改实体 1 |
| FR-3 任务"测试状态"枚举收窄 | §3.1 | T-001 | data-changes.md §修改实体 2 |
| FR-4 code-it 职责文档声明 | §3.2 | T-002 | module-details.md §模块 2;interface-specs.md §接口 3 |
| FR-5 code-unit 职责文档声明 | §3.3 | T-003 | module-details.md §模块 3;interface-specs.md §接口 4 |
| FR-6 code-auto 任务循环步骤 4.b 修订 | §3.4 | T-004 | module-details.md §模块 4;interface-specs.md §接口 2 |
| FR-7 templates/plan.md 同步收窄 | §3.5 | T-005 | module-details.md §模块 5;interface-specs.md §接口 5 |

## 3. 变更模块概述(每模块 1 段,**详细化见过程文档**)

### 3.1 模块 1:`code-plan` 任务粒度原则修订(T-001)

**修改文件**:`plugins/code-skills/skills/code-plan/SKILL.md §步骤 10A`

**结构化语义锚点**:
- 锚点 1:`§步骤 10A` 子标题
- 锚点 2:`"任务拆分原则"` 子段(以"**任务拆分原则"开头)
- 锚点 3:`"任务类型"` 子段(列表 6 类)
- 锚点 4:`"任务双状态字段"` 子段
- 锚点 5:`"双状态语义"` 子段

**修改要点**:
1. 锚点 2 末尾**追加** 1 段"#### 任务完成定义内化编译/运行"(FR-1,4 行)
2. 锚点 3 列表**移除** `测试` + 列表后**追加** 1 段引用说明(FR-2,3 行)
3. 锚点 4 修订"测试状态"枚举为 2 个(FR-3,3 行)+ 追加 1 段说明(4 行)
4. 锚点 5"双状态语义"**简化** 1 句(FR-3 副作用,2 行)

**详细化**:`module-details.md §模块 1` + `data-changes.md §修改实体 1 / §修改实体 2`

**符合的规范**:`skill-conventions.md` INV-1/2/3

### 3.2 模块 2:`code-it` 职责文档声明(T-002)

**修改文件**:`plugins/code-skills/skills/code-it/SKILL.md ## 目标`

**结构化语义锚点**:
- 锚点 1:`## 目标` 小节(本节末尾**追加** 1 段)
- 锚点 2:`## 工作流程` 小节(本需求**不**修改)

**修改要点**:锚点 1 末尾**追加** 1 段"本技能职责范围"(FR-4,3 行)

**详细化**:`module-details.md §模块 2` + `interface-specs.md §接口 3`

**符合的规范**:INV-1/2/3

### 3.3 模块 3:`code-unit` 职责文档声明(T-003)

**修改文件**:`plugins/code-skills/skills/code-unit/SKILL.md ## 目标`

**结构化语义锚点**:
- 锚点 1:`## 目标` 小节
- 锚点 2:`## 工作流程` 小节(本需求**不**修改)

**修改要点**:锚点 1 末尾**追加** 1 段"本技能职责范围"(FR-5,3 行)

**详细化**:`module-details.md §模块 3` + `interface-specs.md §接口 4`

**符合的规范**:INV-1/2/3

### 3.4 模块 4:`code-auto` 任务循环步骤 4.b 修订(T-004)

**修改文件**:`plugins/code-skills/skills/code-auto/SKILL.md §步骤 4 任务循环 步骤 4.b`

**结构化语义锚点**:
- 锚点 1:`§步骤 4 任务循环` 子节
- 锚点 2:子步 b(既有"若 code-it 输出含'测试需要=Y'")

**修改要点**:
1. 锚点 2**改写**为"恒等跳过"(FR-6,5-7 行)
2. 锚点 2 末尾**追加** 1 段"还原指引"注释(本需求 INV-10,3-4 行)

**详细化**:`module-details.md §模块 4` + `interface-specs.md §接口 2`

**符合的规范**:INV-1/2/3/10

### 3.5 模块 5:`templates/plan.md` 同步收窄(T-005)

**修改文件**:`plugins/code-skills/skills/code-plan/templates/plan.md`

**结构化语义锚点**:
- 锚点 1:`## 任务总览` 表格
- 锚点 2:模板顶部(以"---"分隔线为锚点)

**修改要点**:
1. 锚点 1"任务类型"列**移除** `测试`(FR-7,1 行)
2. 锚点 2**追加** 1 段"任务粒度约束"(FR-7 副作用,3 行)

**详细化**:`module-details.md §模块 5` + `interface-specs.md §接口 5`

**符合的规范**:`module-conventions.md`

## 4. 算法与逻辑

本需求**不**涉及新算法或逻辑,**不**绘制流程图 / Mermaid 图。

(每任务实施逻辑:**Read 最新文件 → 定位结构化语义锚点 → Edit/Write 修订内容 → INV 字节级校验 → 提交 commit**,是 `code-it` 步骤 5-8 的标准流程,本详设**不**重复。)

## 5. 数据结构完整变更(概述,详细化见 `data-changes.md`)

### 5.1 新增实体(无)

### 5.2 修改实体

| 实体 / 字段 | 形式 | 修改前 | 修改后 | 详细化 |
| --- | --- | --- | --- | --- |
| `PLAN.md 任务总览.任务类型` | 字段 | `{新增, 修改, 重构, 修复, 测试, 文档}`(6 类) | `{新增, 修改, 重构, 修复, 文档}`(5 类) | `data-changes.md §修改实体 1` |
| `PLAN.md 任务总览.测试状态` | 字段 | `{未编写, 已编写, 已运行-通过, 已运行-失败, 不适用, 阻塞}`(6 枚举) | `{已运行-通过, 不适用}`(2 枚举) | `data-changes.md §修改实体 2` |

### 5.3 删除实体(无)

## 6. 接口细节(概述,详细化见 `interface-specs.md`)

| 接口 | 形式 | 路径 | 详细化 |
| --- | --- | --- | --- |
| `code-plan` 任务粒度接口 | 文档子节 | `code-plan/SKILL.md §步骤 10A` | `interface-specs.md §接口 1` |
| `code-auto` 任务循环步骤 4.b | 文档子节 | `code-auto/SKILL.md §步骤 4` | `interface-specs.md §接口 2` |
| `code-it` 文档头声明 | 文档头 | `code-it/SKILL.md ## 目标` | `interface-specs.md §接口 3` |
| `code-unit` 文档头声明 | 文档头 | `code-unit/SKILL.md ## 目标` | `interface-specs.md §接口 4` |
| `templates/plan.md` 任务类型字段 | 模板字段 | `templates/plan.md ## 任务总览` | `interface-specs.md §接口 5` |

## 7. 异常处理

本需求**不**引入新的失败场景 / 异常路径。

既有异常处理字节级保留:
- `code-plan` 步骤 8A"澄清冲突"路径
- `code-it` 步骤 12"错误修复循环"路径
- `code-auto` 步骤 5"子技能失败"路径
- `code-check` 步骤 8.7"测试质量"维度"`不适用` 不派生任务"语义

## 8. 安全要求

本需求**不**涉及安全改动(INV-8 沿用):
- 不新增鉴权 / 加密 / 审计
- 不修改敏感数据处理
- 不引入新依赖

## 9. 状态机 / 流程

### 9.1 本需求状态机(简化)

```
START → Read upstream(require/design) → Apply 5 modifications → 5 commits → END
```

### 9.2 任务状态机(沿用 code-it 既有)

- `待开始` → `进行中` → `已完成`
- `不适用`:`code-check` 评审时任务"测试状态"=`不适用` 不派生任务

### 9.3 code-auto 任务循环状态机(由 T-004 修订)

- 既有"code-it → (code-unit?)"→ 修订为"code-it → (code-unit, 恒等跳过)"
- 屏幕日志格式字节级保留 INV-10

## 10. 性能与资源

本需求**不**涉及性能改动。预估总耗时 5 分钟(5 任务 × 每任务 ~1 分钟纯 markdown 编辑)。

## 11. 测试要点(详细化见 `risk-analysis.md` §测试要点)

### 11.1 单元测试范围

**0 项**(本需求主动外移单元测试职责,FR-5;任务"测试状态"统一 `不适用`)

### 11.2 集成测试范围

**0 项**

### 11.3 端到端测试范围

由 `code-check` 评审承担,8 大类 AC(AC-1 ~ AC-8,详 `risk-analysis.md §端到端测试`)

### 11.4 性能/安全测试

不适用。

## 12. 规范遵循

7 个项目级规范**全部满足**(INV-5):
- `skill-conventions.md` — INV-1 / INV-2 / INV-3
- `module-conventions.md` — 资源文件放 templates/
- `doc-conventions.md` — 不适用
- `dashboard-conventions.md` — 看板字段三方同步 0 触发
- `commit-conventions.md` — `chore(<skill>):` 前缀
- `encoding-conventions.md` — 5 位纯数字生成端
- `naming-conventions.md` — kebab-case / 中英混排

**2 项用户授权偏离**:`rule-compliance.md §4 用户授权的偏离`:
- NFR-2(不追溯重写既有 11 个 REQ 的 `plan/PLAN.md`)
- INV-10(屏幕日志格式字节级保留)

## 13. 待澄清 / 未决项

| 编号 | 问题 | 状态 | 备注 |
| --- | --- | --- | --- |
| Q-1 | 5 个 Q(FR-1~FR-7 职责边界) | **已澄清** | `require/REQ-00031/clarifications.md` |
| Q-2 | T-006 是否独立任务 | **留作 follow-up** | 本需求不设 T-006,5 任务已足够 |

## 14. 关联需求

| 关联需求 | 关联点 | 沿用方式 |
| --- | --- | --- |
| REQ-00030(同版本) | INV-1~INV-9 + §8.10/8.11/8.12 校验点 | **字节级沿用** |
| REQ-00020(V0.0.2) | "设计目标"小节机制 | **字节级沿用** |
| REQ-00014(V0.0.2) | `code-plan §步骤 10A "架构任务作为首个任务"` | **字节级保留** |
| REQ-00017(V0.0.2) | 拆任务约束候选集 | **修正**:本需求"移除 `测试` 类型"是候选集的具体子项修正 |
| REQ-00007(V0.0.2) | `code-auto §步骤 4 任务循环` | **改写**:由"按需调用"改为"恒等跳过" |
| REQ-00027(V0.0.3) | BUG 路径步骤 1-7 | **字节级保留** |
| BUG-00001(V0.0.3) | `./assistants/.code-auto-running` | **字节级沿用** |

## 15. 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-12 15:30 | 设计新增 | REQ-00031 详细设计完成(14 章节 + 5 任务 + 10 INV);整体=--balanced + 功能性=中;架构骨架**不**触发;2 数据结构变更;0 派生"更新看板"任务;0 单元测试(主动外移) | REQ-00031 |
| 2026-06-12 15:35 | 设计精简 | 详设 RESULT.md §3-§6 详细化下放到过程文档(module-details / interface-specs / data-changes),§3 改为"变更模块概述";目的是让详设 RESULT.md 主体行数收敛(避免 ratio > 1.2 违反 §8.12 校验点) | REQ-00031 |
