# 数据结构完整变更 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 新增数据结构(内存中传递,无持久化)

### DesignGoals

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| `writeTime` | `string` | NOT NULL, 格式 `YYYY-MM-DD HH:mm` | — | 回写时间 |
| `writeTrigger` | `"code-design" \| "code-plan"` | NOT NULL, 枚举 | — | 回写触发方 |
| `overallGoal` | `"--minimal" \| "--extensible" \| "--balanced"` | NOT NULL, 枚举 | — | 整体设计目标 |
| `dimensionPriority` | `DimensionPriority` | NOT NULL, 对象 | — | 4 维度优先级 |
| `dimensionPriority.functionality` | `"高" \| "中" \| "低"` | NOT NULL, 枚举 | — | 功能性优先级 |
| `dimensionPriority.extensibility` | `"高" \| "中" \| "低"` | NOT NULL, 枚举 | — | 扩展性优先级 |
| `dimensionPriority.robustness` | `"高" \| "中" \| "低"` | NOT NULL, 枚举 | — | 健壮性优先级 |
| `dimensionPriority.maintainability` | `"高" \| "中" \| "低"` | NOT NULL, 枚举 | — | 可维护性优先级 |

- **关系**:**无**(纯数据对象,无关联)
- **存储选型**:**无持久化**(在 `code-design` / `code-plan` 步骤 0b 内部传递,写入 `RESULT.md` 后即被释放)
- **迁移脚本**:**无**
- **依据规范**:FR-5 + REQ-00011 §8.1

### NeedContext(辅助,code-design 步骤 0b 内部用)

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `size` | `"small" \| "medium" \| "large"` | NOT NULL, 枚举 | 需求规模(用于自适应问题数) |
| `subFeatures` | `string[]` | 可空 | 大需求时的子功能列表(AC-6.3 拆分提问) |

- **存储选型**:**无持久化**
- **依据规范**:FR-6 + AC-6.3

## 修改文档结构(Markdown)

### "## 设计目标"小节 Markdown 模板

- **位置**:
  - `design/.../RESULT.md` 顶部(在"## 文档头"之后,"## 1. 设计概述"之前)
  - `plan/.../RESULT.md` 顶部(在"## 文档头"之后,"## 1. ..."之前)
- **模板**:
  ```markdown
  ## 设计目标

  > 本小节由 `code-design` / `code-plan` 步骤 0b 自动生成,记录用户确认的设计目标。

  - **回写时间**:2026-06-05 19:50
  - **回写触发**:code-design

  ### 整体设计目标
  `--balanced`

  ### 维度优先级

  | 维度 | 优先级 |
  | --- | --- |
  | 功能性 | 中 |
  | 扩展性 | 中 |
  | 健壮性 | 中 |
  | 可维护性 | 中 |
  ```
- **字段映射**:
  - `回写时间` ↔ `DesignGoals.writeTime`
  - `回写触发` ↔ `DesignGoals.writeTrigger`
  - `整体设计目标` ↔ `DesignGoals.overallGoal`
  - `维度优先级` 表 ↔ `DesignGoals.dimensionPriority`
- **兼容策略**:
  - 多次执行 → 覆盖前次内容(NFR-3)
  - 历史 `RESULT.md`(V0.0.1 / V0.0.2 早于本需求的版本)**无**该小节 — 由 `code-plan` 步骤 0b 退化路径兼容

## 修改既有 SKILL.md 正文(锚点定位,无语义层数据结构变化)

### `code-design/SKILL.md` §步骤 0a L107
- **变更**:删除"code-design **不**含步骤 0b(FR-2 显式仅 `code-require` 专属)"整句
- **插入**:"步骤 0a 成功后,`code-design` 进入'步骤 0b 设计目标确认'(本需求 REQ-00011 新增,FR-1)"
- **结构**:步骤 0a 既有锚点(L106-117)字节级保留(L107 小注更新除外)

### `code-plan/SKILL.md` §步骤 0a L118
- **变更**:同 code-design,删除"code-plan **不**含步骤 0b"整句
- **插入**:"步骤 0a 成功后,`code-plan` 进入'步骤 0b 设计目标确认'(本需求 REQ-00011 新增,FR-2)"

## 数据迁移

- **无**(本需求不涉及数据迁移;新增"## 设计目标"小节是 Markdown 文本,无需数据库迁移)
