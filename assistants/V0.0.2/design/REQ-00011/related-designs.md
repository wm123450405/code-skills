# 关联设计 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 同版本关联设计

| 关联设计编码 | 关联点 | 对本设计的影响 | 链接 |
| --- | --- | --- | --- |
| **REQ-00017**(V0.0.2)— `code-plan` 拆分任务逻辑:更新看板下沉至 `code-it` | `code-plan` 步骤 4A 拆任务 + `code-it` 末尾兜底 P-1 推进看板 | 本需求在 `code-plan` SKILL.md 中"步骤 0a"后**再**追加"步骤 0b",与其现有"步骤 4A 拆任务"位置不重叠;任务粒度调整段(FR-4)叠加在"步骤 4A"前/后均可,需在 `code-it` 实施时协调位置 | [RESULT](../REQ-00017/RESULT.md) |
| **REQ-00016**(V0.0.2)— 看板字段约定 / `code-auto` 步骤 0a 守卫 | 看板字段约束;`code-auto` 步骤 0a 拉取 | 本需求**不**触发 `dashboard-conventions §规则 1` 3 处同步;`code-auto` 沿用"总选推荐项"(NFR-5) | [RESULT](../REQ-00016/RESULT.md) |
| **REQ-00014**(V0.0.2)— `code-auto` v2 增量 | `code-auto` 现行 FR-3 / FR-4.AC-4.1 / FR-4.AC-4.3 在"全自动"场景下会"总选推荐项"绕过用户确认 | 本需求**不**触发 `code-auto` 升级;沿用现行"总选推荐项"行为 | [RESULT](../REQ-00014/RESULT.md) |
| **REQ-00009**(V0.0.2)— `code-unit` 项目可测性守卫(步骤 0a 模式) | 守卫模式 | 与本需求"步骤 0b"模式同位叠加;`code-unit` 不变 | [RESULT](../REQ-00009/RESULT.md) |
| **REQ-00010**(V0.0.2)— `code-it` 前置任务守卫(步骤 0a 模式) | 守卫模式 | 与本需求"步骤 0b"模式同位叠加;`code-it` 不变 | [RESULT](../REQ-00010/RESULT.md) |
| **REQ-00008**(V0.0.2)— `code-review` 整版本模式 | 评审 | `code-review` 不感知"设计目标"概念;FR-7.AC-7.3 强约束"不改 code-review" | [RESULT](../REQ-00008/RESULT.md) |
| **REQ-00007**(V0.0.2)— `code-auto` 自动开发技能 | `code-auto` 调 `code-design` / `code-plan` 各 1 次 | NFR-5:`code-auto` 选"推荐项";**不**触发 `code-auto` 升级 | [RESULT](../REQ-00007/RESULT.md) |
| **REQ-00006**(V0.0.2)— `code-publish` 发布部署技能 | 发布 | `code-publish` 不感知"设计目标"概念;**不**触发升级 | [RESULT](../REQ-00006/RESULT.md) |
| **REQ-00005**(V0.0.2)— 优化 3 技能,加首步拉取与末步提交 | "首步拉取"位置 = 步骤 0a | NFR-6 锁定:本需求"步骤 0b"叠加在 REQ-00005 之上;首步拉取**仍**为步骤 0a | [RESULT](../REQ-00005/RESULT.md) |
| **REQ-00004**(V0.0.2)— `code-dashboard` 开发看板技能 | 看板展示 | `code-dashboard` 不感知"设计目标"概念;**不**触发升级 | [RESULT](../REQ-00004/RESULT.md) |

## 跨版本关联设计(参考)

| 关联设计编码 | 关联点 | 对本设计的影响 | 链接 |
| --- | --- | --- | --- |
| **REQ-00003**(V0.0.1)— 优化 `code-rule` 技能 | "用户确认"模式参考(FR-7 自动+显式模式) | 本需求可借鉴 REQ-00003 FR-7 的"自动推断 + 显式追问"模式;**不**直接引用 | `./assistants/V0.0.1/require/REQ-00003/RESULT.md` |
| **REQ-00002**(V0.0.1)— 编码格式统一 | 编码权威源 | 本需求**不**直接产生新编码;不涉及 | `./assistants/V0.0.1/require/REQ-00002/RESULT.md` |
| **REQ-00001**(V0.0.1)— 看板模板 | 看板字段约定 | 本需求**不**修改看板;**不**触发 `dashboard-conventions §规则 1` | `./assistants/V0.0.1/require/REQ-00001/RESULT.md` |

## 关键事实

- V0.0.0 基线版本由 `code-init` 批量生成 10 个 `EXISTING-NNN`,**不**追溯重命名(`migration-mapping.md §规则 4`)
- V0.0.1 中所有概要设计 / 详细设计产物均**无**"设计目标"小节;V0.0.2 之后由本需求支持(增量追加,不动历史)
- V0.0.2 既有 11 个 `code-*` 技能:`code-init` / `code-version` / `code-rule` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-fix` / `code-review` / `code-publish` / `code-auto`(12 个,含本需求前 9 + 后 3)
- 本需求**只**改 `code-design` / `code-plan` 2 个技能,FR-7.AC-7.1 强约束

## 跨需求聚合(本需求对"步骤 0b"模式的协同)

| 需求 | "步骤 X"模式 | 本需求关系 |
| --- | --- | --- |
| REQ-00005 | "步骤 0a 拉取" + "末尾兜底" | 本需求"步骤 0b"叠加在 REQ-00005 "步骤 0a"之后;**不**改 REQ-00005 既有边界 |
| REQ-00009 | "步骤 0a 守卫"(`code-unit`) | 本需求"步骤 0b"模式协同;**不**改 `code-unit` |
| REQ-00010 | "步骤 0a 守卫"(`code-it`) | 本需求"步骤 0b"模式协同;**不**改 `code-it` |
| REQ-00016 | "步骤 0a 守卫"(`code-auto`) | 本需求"步骤 0b"模式协同;**不**改 `code-auto` |
| REQ-00017 | `code-plan` 步骤 4A 拆任务 + `code-it` 末尾兜底 P-1 推进看板 | 本需求"步骤 0b"与 REQ-00017"步骤 4A"位置不重叠;任务粒度调整段(FR-4)需在 `code-it` 实施时协调位置 |
