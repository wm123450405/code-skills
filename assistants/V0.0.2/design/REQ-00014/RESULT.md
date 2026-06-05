# REQ-00014 — 概要设计:优化技能 `/code-plan` 的任务拆分维度

- 需求编码:`REQ-00014`
- 所属版本:`V0.0.2`
- 上游需求:`./assistants/V0.0.2/require/REQ-00014/RESULT.md`(v1,已锁定,4 FR / 6 NFR / 13 AC)
- 遵循规范:`./assistants/rules/` 下 13 个文件(7 强约束 + 6 占位 + 1 DEPRECATED;详见 §3 与 `rule-compliance.md`)
- 状态:已完成(首次概要设计)
- 责任人:wangmiao
- 创建:2026-06-05
- 最近更新:2026-06-05 13:05
- 当前版本:v1

---

## 1. 概要设计概述

在概要设计的基础上,本详细设计把"系统长什么样"细化为"系统怎么写"。核心决策:**修改 1 个 `code-plan` SKILL.md 的 1 个章节**(§10A `任务拆分原则`,L195-199,共 4 行文字),**完全替换**为新原则(Q-D1 锁定):**核心原则:按"功能点"拆分**(1 个任务 = 1 个用户完整可用的能力 = 展示效果 + 功能逻辑 + 使用说明)+ **架构任务作为首个任务**(条件触发:较高扩展性/可维护性/可配置性 + 较高复杂度,或涉及未来不同实现方式,或对接不同三方组件)。生效范围 = V0.0.2 未来所有需求(REQ-00008+);既有 7 个 PLAN **不**追溯重拆(Q-A3 锁定 A)。**0** 模块新增,**0** 三方依赖新增,**0** 规范违反,**0** 其他 12 个 `code-*` 技能 SKILL.md 修改,**0** 看板字段修改(故**不**触发 `dashboard-conventions §规则 1` 三同步)。

## 2. 需求回顾

引用上游 `./assistants/V0.0.2/require/REQ-00014/RESULT.md`(v1):

- **FR-1** 按"功能点"拆分任务(Q-A1 锁定:按用户可见能力)→ §4.1 详细化
- **FR-2** 架构任务作为首个任务(条件触发)→ §4.2 详细化
- **FR-3** 仅未来需求生效(Q-A3 锁定 A)→ §4.3 详细化
- **FR-4** 不破坏其他 12 个 `code-*` 技能 → §4.4 详细化
- **NFR-1** 零新增依赖 → §6 依赖评估 = 0
- **NFR-2** SKILL.md 修改行数 ≤ 50 → §5 修改范围 = 4 行删除 + ~25 行新增 = ~20 行净增(满足 ≤ 50)
- **NFR-3** 不触发 `dashboard-conventions §规则 1` 三同步 → §3 规范遵循 = 0 触发
- **NFR-4** 不触发 `code-design` 联动修改 → §7 影响范围 = 0
- **NFR-5** 不触发 `code-it` 联动修改 → §7 影响范围 = 0
- **NFR-6** 对 V0.0.2 未来所有需求立即生效 → §5 生效范围

## 3. 规范遵循(总账)

### 3.1 适用的规范文件

| 规范文件 | 类别 | 关键约束 | 本概要设计对应章节 |
| --- | --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | 技能编写 | §规则 1:frontmatter 必含 name+description | (不触达,沿用既有) |
| `./assistants/rules/module-conventions.md` | 模块规划(DEPRECATED) | §规则 1:资源放固定子目录 | (不触达,无资源新增) |
| `./assistants/rules/dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:字段约定扩展需 3 处同步 | **不触发**(本设计**不**改字段) |
| `./assistants/rules/doc-conventions.md` | 文档编写 | §规则 1:中英同次;§规则 2:持续维护 | (不触达) |
| `./assistants/rules/marketplace-protocol.md` | Marketplace 协议 | §规则 1:skills 数组以 `./` 开头 | (不触达) |
| `./assistants/rules/encoding-conventions.md` | 编码格式 | §规则 1-4:任务编号 5+5 位嵌套 | §5 修改范围(沿用既有) |
| `./assistants/rules/migration-mapping.md` | 编码迁移 | §规则 1-4:EXISTING-NNN 不追溯 | §5 生效范围(仅未来需求) |

**占位规范(6 个,不影响)**:`directory-conventions.md` / `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `naming-conventions.md`

### 3.2 自检结论

- **完全合规**的章节:§1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §10
- **经用户授权偏离**的章节:**0**
- **待澄清冲突**:**0**

> 详细规范遵循记录见 `rule-compliance.md`(本目录)。

## 4. 模块详细化

### 4.1 模块 M-1:`code-plan/SKILL.md` §10A 修改(对应概要设计 §7.2)

#### 关键"组件"(SKILL.md 的工作流视角)

| 组件 | 形式 | 职责 |
| --- | --- | --- |
| 任务拆分原则子节(原 4 行) | 文字 | 原"按层拆分"原则(**完全替换**) |
| 任务拆分原则子节(新 2 子节) | 文字 | "按功能点拆分" + "架构任务作为首个"(**新增**) |
| 任务类型 | 文字 | 6 种类型(沿用既有) |
| 任务编号 | 文字 | `TASK-(REQ|BUG)-NNNNN-NNNNN`(沿用既有) |
| 任务双状态 | 文字 | 开发 + 测试(沿用既有) |
| 任务触发/来源 | 文字 | 13 个枚举值(沿用既有) |

#### 关键"调用顺序"(对应 `code-plan` 步骤 10A)

```
code-plan 步骤 10A 任务拆分(优化后)
  ├─ 10A.0 评估需求(满足架构任务触发条件?)
  │   ├─ 是 → 首个任务 = 架构设计开发任务(FR-2)
  │   │       └─ 后续任务 = 各个功能点(FR-1)
  │   └─ 否 → 直接按功能点拆分(FR-1)
  ├─ 10A.1 识别功能点(用户可见能力,1 个 = 1 个任务)
  ├─ 10A.2 对每个功能点,1 个任务 = 1 个完整一套
  │   ├─ 展示效果(UI / 截图 / 界面描述 / 示例)
  │   ├─ 功能逻辑(算法 / 接口 / 数据结构)
  │   └─ 使用说明(README / 入门文档 / API 文档)
  └─ 10A.3 任务编号 + 双状态 + 触发/来源(沿用既有)
       └─ 首个任务若是架构任务,占 TASK-XXX-00001
```

#### 内部状态

- **不维护内存状态**:`code-plan` 是无状态工作流定义
- **不写代码 / 配置 / 数据库**
- **不持有任何凭据**

#### 并发模型
- **N/A**(无运行时)

#### 资源管理
- **N/A**(无连接 / 锁 / 缓存)

#### 错误处理范式
- **不修改既有错误处理**:本需求**不**改错误处理范式
- 沿用 `code-plan` 既有的步骤 8A"澄清冲突与不确定项"机制(用户已在 REQ-00014 require 阶段使用)

#### 日志埋点
- **N/A**:本需求**不**改日志

#### 依据规范
- `skill-conventions §规则 1`:**不**触达(沿用既有 frontmatter)
- `module-conventions §规则 1`:**不**触达(无资源新增)
- `dashboard-conventions §规则 1`:**不**触发(本优化**不**改字段)
- `encoding-conventions §规则 1-4`:**不**触达(任务编号格式沿用既有)

### 4.2 模块 M-2:无(本需求不产生新模块)

## 5. 算法与逻辑(可直接编码)

### 算法 1:`code-plan` 步骤 10A 拆分任务(优化后)

```
function algorithm_1_split_tasks(requirement):
    # 1. 评估需求(满足架构任务触发条件?)
    architecture_needed = False
    if (requirement.has_high_scalability or requirement.has_high_maintainability or requirement.has_high_configurability) and requirement.has_high_complexity:
        architecture_needed = True
    elif requirement.involves_future_alternate_implementations:
        architecture_needed = True
    elif requirement.involves_third_party_components:
        architecture_needed = True
    
    tasks = []
    task_counter = 1
    
    # 2. 若是 → 首个任务 = 架构设计开发任务
    if architecture_needed:
        tasks.append({
            "id": f"TASK-{requirement.id}-{task_counter:05d}",
            "title": "[新增] 架构设计 + 架构骨架",
            "type": "新增",
            "content": "抽象层 + 接口契约 + 扩展点(不实现具体业务)"
        })
        task_counter += 1
    
    # 3. 识别功能点(用户可见能力,1 个 = 1 个任务)
    feature_points = identify_feature_points(requirement)
    
    # 4. 对每个功能点,1 个任务 = 1 个完整一套
    for fp in feature_points:
        tasks.append({
            "id": f"TASK-{requirement.id}-{task_counter:05d}",
            "title": f"[{fp.type}] {fp.name}",
            "type": fp.type,
            "content": {
                "展示效果": fp.ui_or_display,
                "功能逻辑": fp.algorithm_or_interface,
                "使用说明": fp.readme_or_docs
            }
        })
        task_counter += 1
    
    # 5. 任务编号 + 双状态 + 触发/来源(沿用既有)
    for t in tasks:
        t["dev_status"] = "待开始"
        t["test_status"] = "未编写" if t["type"] != "文档" else "不适用"
        t["source"] = "需求新增"
    
    return tasks
```

- **输入**:`requirement`(requirement 对象,含特性/复杂度/扩展性等元数据)
- **输出**:`tasks` 列表(每个任务含 id/title/type/content/dev_status/test_status/source)
- **复杂度**:O(N_feature_points)
- **依赖**:无
- **关键决策**:**完全替换**原"按层拆分"算法(Q-D1 锁定)
- **边界条件**:无功能点的需求 → 仅返回架构任务(若触发)或空列表
- **对应任务**:T-001 写 `code-plan` SKILL.md §10A 改写

## 6. 数据结构完整变更(概要,详见 `data-changes.md`)

### 6.1 新增实体(0)
- 无

### 6.2 修改实体(1)

| 实体 | 变更字段 | 索引 | 兼容策略 | 对应任务 |
| --- | --- | --- | --- | --- |
| `plugins/code-skills/skills/code-plan/SKILL.md` | §10A L195-199(4 行) | 无 | 完全替换(Q-D1 锁定) | T-001 |

### 6.3 数据迁移(N/A)
- 本需求**不涉及**数据迁移

## 7. 接口细节(概要,详见 `interface-specs.md`)

### 7.1 接口总览

| 接口名 | 形式 | 状态 | 对应任务 | 依据规范 |
| --- | --- | --- | --- | --- |
| `code-plan` 任务拆分工作流 | 文字描述(SKILL.md §10A) | 修改 | T-001 | `skill-conventions §规则 1` |
| `code-plan` 步骤 10A 调用顺序 | 文字描述 | 修改 | T-001 | `module-conventions §规则 1`(沿用) |

### 7.2 关键决策

- **修改范围**:`code-plan` SKILL.md §10A 的 5 行(L195-199) → **完全替换**为 ~25 行新内容
- **生效范围**:V0.0.2 未来所有需求(REQ-00008+);既有 7 个 PLAN **不**追溯
- **触发 `dashboard-conventions §规则 1` 三同步**:**否**(本优化**不**改字段)
- **触发其他 12 个 `code-*` 技能 SKILL.md 联动修改**:**否**
- **既有 7 个 PLAN 追溯重拆**:**否**

## 8. 异常处理

按 E-1 ~ E-5 组织(沿用需求文档):

- **E-1** 需求边界模糊(无法判断是否需要架构任务)→ 由 `code-plan` 步骤 8A 与用户澄清
- **E-2** 用户要求修改 `code-plan` 其他章节(非 §10A)→ 拒绝,引导用户另起需求
- **E-3** 既有 7 个 PLAN 用户要求重拆→ 拒绝,引用 Q-A3 锁定 A
- **E-4** 未来需求拆分时 `code-plan` 应用新规则失败→ 退回"分层拆分"(沿用既有)
- **E-5** `code-plan` SKILL.md 修改后与 `code-design` 冲突→ 暂停,询问用户

## 9. 安全要求

- **鉴权**:N/A(纯文档型)
- **授权**:N/A
- **输入校验**:`code-plan` 拆分任务的输入是设计文档,**不涉及**外部输入
- **敏感数据处理**:**不**读任何凭据 / secrets
- **防注入**:N/A
- **审计**:N/A
- **依据规范**:`dashboard-conventions §规则 1`(本需求**不**改字段,沿用既有)

## 10. 状态机 / 流程(对应概要设计 §5.1)

### 10.1 主状态机

```
[code-plan 步骤 10A 启动]
  ↓
[10A.0 评估需求]
  ├─ 满足架构触发条件? → 首个任务 = 架构设计开发任务
  └─ 不满足 → 跳过架构任务
  ↓
[10A.1 识别功能点]
  ├─ 用户可见能力(1 个 = 1 个任务)
  └─ 0 个功能点 → 仅返回架构任务(若触发)或空列表
  ↓
[10A.2 完整一套拆分]
  ├─ 展示效果 + 功能逻辑 + 使用说明
  └─ 必须在同一个任务中
  ↓
[10A.3 任务编号 + 双状态 + 触发/来源]
  ├─ 任务编号:自 00001 起递增
  └─ 双状态:待开始 + 未编写/不适用
  ↓
[返回 tasks 列表] → [code-plan 步骤 11A-18A 继续]
```

### 10.2 内部状态

`code-plan` 是**无状态工作流定义**,**不**维护内存状态。

## 11. 性能与资源

- **关键路径耗时**:`code-plan` 整体执行由子步骤决定;§10A 拆分任务耗时 = O(N_feature_points)
- **并发上限**:N/A
- **资源限制**:N/A
- **缓存策略**:N/A
- **批量/异步**:N/A
- **降级策略**:N/A

## 12. 测试要点(概要,详见 `risk-analysis.md`)

- **单元测试**:N/A(纯文档型,本仓库无测试框架)
- **集成测试**:**回归** — V0.0.2 既有 7 个 PLAN 拆分结果**不**因新规则而破坏(由 `code-review` 验证)
- **端到端测试**:**新规则应用** — V0.0.2 未来需求(REQ-00008+)按新规则拆分,由 `code-it` / `code-review` 验证
- **性能/安全测试**:N/A
- **回归测试**:**0** 既有 PLAN 追溯重拆(Q-A3 锁定 A)
- **静态自检**:8 项不变量(由 `code-it` T-005 实施,与 V0.0.2 既有 PLANS 一致)

## 13. 关联编码计划

- `PLAN.md` 中本详细设计对应 **2 个任务**(T-001 写 `code-plan` SKILL.md §10A + T-005 8 项不变量自检 + 收尾)
- 关键任务对应:
  - **T-001** ↔ 本设计 §4.1(M-1 模块详细化)+ §5(算法 1)
  - **T-005** ↔ 本设计 §12(测试要点)

## 14. 待澄清 / 未决项(本轮已全部澄清)

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 | 状态 |
| --- | --- | --- | --- | --- | --- |
| Q-D1 | §10A 改写范围 | §4.1 / §5 | (本轮已锁定) | 已锁定 A | N/A |

## 15. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-05 13:05 | v1 | 初始创建:1 个模块 M-1 修改(§10A 4 行删除 + ~25 行新增)+ 1 个算法(可编码)+ 4 接口契约;100% 规范合规,0 偏离 0 冲突 0 授权;**不**触发 `dashboard-conventions §规则 1` 三同步(本优化**不**改字段);**不**修改其他 12 个 `code-*` SKILL.md;**不**追溯重拆既有 7 个 PLAN(Q-A3 锁定 A);生效范围 = V0.0.2 未来所有需求(REQ-00008+);Q-D1 锁定 A(§10A 改写 = 完全替换原 4 行原则) | wangmiao |
