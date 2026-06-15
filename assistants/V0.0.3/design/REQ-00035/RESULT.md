# 设计目标

> 本节由 `code-design` 步骤 0b 自动生成(code-auto 上下文,沿用 --balanced 默认)

- 整体设计目标:`--balanced`
- 功能性:中
- 扩展性:不触发
- 触发条件:本需求属"过程文档生成逻辑改造",5 个主流程技能 + 1 编排 + 1 dashboard = 7 个改写点;无新增三方依赖;无对外接口变更(仅改内部过程文档生成约定)
- code-auto 上下文:0 问(沿用 REQ-00020 步骤 0b.0 强约束)

---

# REQ-00035 — 概要设计

- 需求编码:REQ-00035
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00035/RESULT.md (v1)
- 遵循规范:./assistants/rules/{encoding-conventions,dashboard-conventions,migration-mapping,doc-conventions,skill-conventions,module-conventions,marketplace-protocol}.md(共 7 个)
- 状态:已完成
- 创建:2026-06-15
- 最近更新:2026-06-15

## 1. 概要设计概述

本概要设计回答"5 个主流程技能 + 1 编排 + 1 dashboard 的过程文档生成逻辑改造后,系统长什么样"。

核心设计:
- **统一判定器**:为每类过程文档建立"不涉及判定准则"(`process-doc-decisions` 数据结构),AI 在每个技能启动时按准则自适应判定
- **决策记录文件**:`process-doc-decisions.md` 仅当有"不生成"判定时才生成,反向节省 token
- **步骤 0a 注入**:每个主流程 SKILL.md 加 1 个新步骤(0a 或 0b),执行判定 + 决策写入
- **8.13 评审维度**:`code-check` 新增 8.13 评审过程文档适配性(派生"建议改"任务,不阻断)
- **看板变更记录策略**:幂等空跑 / 用户取消提交 / 子技能判定失败场景下不追加

不展开的字段(下沉到 `code-plan` 阶段):
- 详设级 SKILL.md 步骤文本(由 `code-plan` 步骤 9A 写)
- 任务粒度拆分(由 `code-plan` 步骤 10A 写)
- 三方依赖 / 数据结构 / 接口细节(本需求**不**涉及,沿用 NFR-8 / NFR-9)

## 2. 上游引用

- **需求**:`./assistants/V0.0.3/require/REQ-00035/RESULT.md` 关键摘录
  - FR-1~FR-8:8 条功能需求
  - NFR-1~NFR-9:9 条非功能需求
  - AC-1~AC-7:22 条验收标准
  - §6 过程文档"不涉及/不适用"判定准则(本设计直接引用)
- **规范**:本设计引用 7 个规范文件(详见 §3 规范遵循)
- **项目现状**:本仓库项目结构无外部代码改动(纯元技能改);既有 9 个 SKILL.md 全部需要评估是否改造

## 3. 规范遵循

### 3.1 引用的规范

| 规范文件 | 引用理由 | 本设计中的体现 |
| --- | --- | --- |
| `encoding-conventions.md` | 编码格式 / 命名 | 沿用 TASK / REQ / BUG 编码格式 |
| `dashboard-conventions.md` | 看板解析 | NFR-7 强约束(不扩展字段) |
| `skill-conventions.md` | 技能 SKILL.md 编写 | 锚点 / 不修改 frontmatter / 不修改既有章节 |
| `module-conventions.md` | 模块边界 | 不改模块边界;仅改技能内部步骤 |
| `doc-conventions.md` | 文档约定 | 沿用变更记录 / 模板规范 |
| `marketplace-protocol.md` | marketplace 协议 | 不改 marketplace.json(本需求 NFR-5) |
| `migration-mapping.md` | 旧→新映射 | 沿用既有迁移;不改 |

### 3.2 自检结论

- **完全合规**:0 偏离
- **授权偏离**:0 条
- **待澄清冲突**:0 条(本设计不引入新规范冲突)

## 4. 模块拆分

详见 `module-breakdown.md`(本设计 §4 仅列模块名,具体职责/路径/依赖见该文件)。

模块总览:
- M1: 5 个主流程技能 SKILL.md(code-require / code-design / code-plan / code-it / code-check)
- M2: 1 个编排技能 SKILL.md(code-auto)
- M3: 1 个看板技能 SKILL.md(code-dashboard)
- M4: 5 个模板新增(`process-doc-decisions.md` × 5 技能)

## 5. 接口与数据结构(概要)

### 5.1 接口(本设计不引入新外部接口)

- **不**新增外部接口(本需求为内部过程文档生成约定改造)
- **不**修改既有 SKILL.md 的 CLI 接口(NFR-3 强约束)
- 5 个主流程技能的"过程文档生成"由 SKILL.md 步骤约定,无对外暴露

### 5.2 数据结构

#### 实体:`ProcessDocDecision`(本设计核心数据结构)

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `type` | string | 是 | 过程文档类型(如 `clarifications.md` / `work-log.md`) |
| `decision` | enum | 是 | `生成` / `不生成` |
| `reason` | string | 是 | 判定理由,引用 §6 准则编号 |
| `alternatives` | string[] | 否 | 备选方案(若 AI 犹豫时可记录) |

#### 实体:`ProcessDocDecisionsFile`(顶层结构)

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `version` | string | 是 | 格式 `V<n.n.n>` |
| `requirement` | string | 是 | 关联需求编码(如 `REQ-00035`) |
| `skill` | string | 是 | 关联技能名(`code-require` / `code-design` / `code-plan` / `code-it` / `code-check`) |
| `decisions` | `ProcessDocDecision[]` | 是 | 决策列表(包含"不生成"和"生成"两类) |
| `generated` | string[] | 是 | 实际已生成的过程文档列表 |
| `changelog` | `ChangeLog[]` | 是 | 变更记录(沿用既有约定) |

> 注:此为"决策记录"文件的数据结构,**仅当有"不生成"判定时**才生成。

## 6. 三方依赖评估(本设计不新增)

- **不**新增任何第三方依赖(本需求为内部元技能改)
- **不**修改任何 package.json / requirements.txt / Cargo.toml
- 既有依赖完全沿用

> 详见 §6 准则(本设计 §4 中 `dependencies.md` 因"无外部依赖"被判定不生成,详见 `process-doc-decisions.md`)

## 7. 关键设计决策

### D-1:判定器位置 — 在 SKILL.md 步骤 0a/0b(选定 A)

**候选方案**:
- A. 在每个技能的 SKILL.md 步骤 0a(版本检测后)新增"过程文档判定"步骤 ← **选定**
- B. 抽出一个 `process-doc-decision.sh` / 共享库
- C. 在 code-rule 中维护一份共享规则文件

**选定理由**:
- A 方案让"判定"与"使用"在同一文件,易于维护(沿用 REQ-00020 自含原则)
- B 方案在 markdown-as-skill 范式下不适用(子技能是 markdown,无 shell 库)
- C 方案违反"code-rule 跨版本共享,主流程技能只读"的约束(项目级规范**不**参与过程文档生成判定,NFR-9 强约束)

### D-2:`process-doc-decisions.md` 文件的"有时无"语义(选定 A:有时无)

**候选方案**:
- A. 仅当有"不生成"判定时才生成 ← **选定**
- B. 始终生成(记录所有决策)
- C. 始终生成(仅记录"不生成"的,精简版)

**选定理由**:
- A 方案反向节省 token(若所有过程文档都生成,无判定可记录)
- B 方案违反 NFR-1(可能产生只 1-2 行的空骨架文件)
- C 方案与 A 等价但需要"空文件占位"标记,增加复杂度

### D-3:看板"变更记录"不追加的判定(选定 A:严格语义)

**候选方案**:
- A. 严格语义:仅当"有变更"才追加 ← **选定**
- B. 宽松语义:始终追加"无变更"行

**选定理由**:
- A 符合"看板是状态总览,不是日志"的语义(沿用既有约定)
- B 方案产生大量 "无变更 YYYY-MM-DD HH:mm" 的噪声行,违背 NFR-1

### D-4:8.13 评审维度派生任务级别(选定 A:建议改,不必须改)

**候选方案**:
- A. 派生"建议改"(不阻断)← **选定**
- B. 派生"必须改"(阻断)
- C. 不派生任务,仅记录到 findings-no-task.md

**选定理由**:
- AI 自适应判定本身有合理自由度(沿用 §E-2 边界:倾向生成)
- "必须改"会反向增加 token(派生任务本身是过程文档)
- "不派生"则失去评审的纠错能力
- 折中:派生"建议改",给用户决策空间

## 8. 关联设计

详见 `related-designs.md`(本设计 §8 引用 5 个关联设计的关键决策)。

## 9. 架构图

```mermaid
graph TB
    subgraph 主流程技能
        R[code-require] -->|读需求材料| J[步骤 0a 过程文档判定]
        D[code-design] -->|读规范 + 上游| J
        P[code-plan] -->|读上游| J
        I[code-it] -->|读任务| J
        C[code-check] -->|读任务 + 测试| J
    end

    J -->|§6 准则| Decide{每类过程文档}
    Decide -->|生成| Write1[Write 过程文档]
    Decide -->|不生成| Write2[Write process-doc-decisions.md]

    J -.->|code-auto 上下文| Auto[--balanced 默认值]
    Auto --> J

    C -->|8.13 评审维度| Review[派生"建议改"任务]
    Review -.->|NFR-2| NoBlock[不阻断]
```

## 10. 变更记录

| 时间 | 事件 | 摘要 |
| --- | --- | --- |
| 2026-06-15 19:05 | 设计完成 | REQ-00035 概要设计完成(4 决策 / 0 不变量 / 0 新增模块(纯改既有)/ 0 新增接口 / 0 数据结构 / 0 依赖) |

## 11. 报告元信息

- **创建人**:code-design (AI 自动化)
- **输入材料**:REQ-00035 需求 + 7 个项目级规范 + V0.0.3 现有 9 个 SKILL.md
- **下一步**:`/code-plan REQ-00035` 详细设计 + 任务拆分
