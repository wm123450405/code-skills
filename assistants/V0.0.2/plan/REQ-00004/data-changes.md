# 数据结构完整变更 — REQ-00004

更新时间:2026-06-04 16:10
版本:V0.0.2

> 本需求**不**新增任何持久化数据(无 DB / 无文件 schema / 无第三方存储)。
> 本节定义"技能内部使用的内存数据结构",由 Claude Code 读取 `SKILL.md` 后在单次调用中实例化。

---

## D-1:Suggestion(下一步建议条目,对应 FR-4 / 算法 3)

### 字段
| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| `command` | string | NOT NULL, 严格匹配既有 `code-*` SKILL.md 的真实语法 | — | 例如 `"/code-it TASK-REQ-00004-001"` |
| `reason` | string | NOT NULL, 一句话 | — | 例如 `"任务 ... 开发状态=待开始,排在本版本所有待开始任务的最前"` |
| `priority` | enum | `高` / `中` / `低` / `—` | — | 与 AC-4.1 三字段对应 |

### 关系
- 1 个 `Suggestion` 属于 1 个 "调用上下文"(总览模式 / 需求模式)
- 多个 `Suggestion` 构成 1 个"建议列表"(最多 5 条,按优先级降序)

### 存储选型
**无**(内存对象)

### 迁移脚本
**无**

### 依据规范
- FR-4 + AC-4.1/4.2/4.3:字段 + 数量 + 格式三约束

---

## D-2:TaskId(任务编号解析结果,对应 NFR-3 / 算法 4)

### 字段
| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| `format` | enum | `new` / `old` | — | 字面格式标识 |
| `type` | enum | `REQ` / `BUG` | — | 父级类型 |
| `parentNum` | string | 5 位纯数字,前导补零 | — | 父级数字段 |
| `taskNum` | string | 5 位纯数字,前导补零 | — | 任务序号 |
| `displayId` | string | NOT NULL, 字面原样 | — | 用于展示;`format=new` 时为 `TASK-REQ-NNNNN-NNNNN`,`format=old` 时为 `REQ-NNNNN-NNNNN` |

### 关系
- 1 个 `TaskId` 来自 1 个"看板任务行"
- 多条 `TaskId` 聚合为 1 个 `TaskRow`(见 D-4)

### 存储选型
**无**(内存对象)

### 迁移脚本
**无**

### 依据规范
- `encoding-conventions.md §规则 1/3`:`REQ-NNNNN` / `TASK-(REQ|BUG)-NNNNN-NNNNN` 权威源
- NFR-3:双格式兼容,`format` 字段区分

### 边界与回退
- 解析失败:`format` 字段缺失 → 该行在渲染时按字面显示(`REQ-00001-001`),不参与"路径解析"

---

## D-3:ParseResult(步骤 3 解析结果,对应 I-3)

### 字段
| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `mode` | enum | `总览` / `需求` / `错误` | 调用模式 |
| `version` | string | `^V\d+\.\d+\.\d+$` | 当前激活版本号 |
| `reqNum` | string \| null | `^REQ-\d{5}$` 或 null | 需求模式时 = `REQ-00001`;否则 null |
| `requirements` | `RequirementRow[]` | 总览模式必填;数组可空 | 见 D-5 |
| `tasks` | `TaskRow[]` | 总览模式必填;数组可空 | 见 D-4 |
| `bugs` | `BugRow[]` | 总览 + 需求模式;数组可空 | 见 D-6 |
| `targetReq` | `RequirementDetail \| null` | 需求模式必填;否则 null | 见 D-7 |
| `error` | `ErrorInfo \| null` | 错误模式必填;否则 null | 见 D-8 |

### 关系
- 1 个 `ParseResult` 来自 1 次 `parseDashboard()` 或 `parseRequirementMode()` 调用
- 1 个 `ParseResult` 流向 1 次 `aggregate()` + `renderBar()` + `generateSuggestions()` 调用

### 存储选型
**无**

### 迁移脚本
**无**

### 依据规范
- `dashboard-conventions.md §规则 1`:看板字段约定扩展需 3 文件同步;本数据结构**不**扩展看板字段(只是内部)

---

## D-4:TaskRow(任务行,对应需求模式任务清单渲染)

### 字段
| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `taskId` | `TaskId` | 必填 | 见 D-2 |
| `title` | string | 可能为空 → 显示 `?` | 任务标题(看板"任务清单"列) |
| `devStatus` | enum | `待开始` / `进行中` / `已完成` / `已取消` / `阻塞` / `待重新评估` | 与看板枚举一致 |
| `testStatus` | enum | `未编写` / `已编写` / `已运行-通过` / `已运行-失败` / `不适用` / `阻塞` | 与看板枚举一致 |

### 关系
- 1 个 `TaskRow` 对应 1 行看板"任务清单"
- 1 个 `RequirementDetail` 含 0..N 个 `TaskRow`

### 存储选型
**无**

### 依据规范
- `dashboard-conventions.md §规则 1`:字段枚举值由看板"任务清单"列定义,本技能**不**新增枚举

---

## D-5:RequirementRow(需求行,对应总览模式需求进度段)

### 字段
| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `id` | string | `^REQ-\d{5}$` | 需求编码 |
| `title` | string | 可能为空 → 显示 `?` | 需求标题 |
| `status` | enum | `待开始` / `进行中` / `已完成` / `已完成(需求分析)` / `已取消` / `阻塞` | 与看板枚举一致(V0.0.2 引入了"已完成(需求分析)"子状态) |
| `design` | enum | `已完成` / `未开始` / `—` | 概要设计状态(由看板"概要设计"列推断) |
| `plan` | enum | `已完成` / `未开始` / `—` | 详细设计状态(由看板"详细设计"列推断) |

### 关系
- 1 个 `RequirementRow` 对应 1 行看板"需求清单"

### 依据规范
- `dashboard-conventions.md §规则 1`:字段枚举由看板列定义;本技能**不**新增枚举

### V0.0.2 状态枚举差异注意
- 看板"需求清单"列的"状态"字段在 V0.0.2 实际使用了 `已完成(需求分析)` 这种"阶段化"子状态
- 本技能 `status` 字段接受该字面,**不**在内部做归一化
- 计数时:**严格按字面匹配**(避免误把"已完成(需求分析)"归到"已完成"桶,导致后续"code-plan / code-it"看不到)

---

## D-6:BugRow(缺陷行,对应总览模式缺陷段 + 需求模式关联缺陷筛)

### 字段
| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `bugId` | string | `^BUG-\d{5}$` | 缺陷编码 |
| `severity` | enum | `P0` / `P1` / `P2` / `P3` | 严重度 |
| `title` | string | 可能为空 | 缺陷标题 |
| `status` | enum | `待修复` / `修复中` / `已修复` / `已关闭` | 缺陷状态(具体枚举由看板"缺陷清单"列定义) |
| `relatedTask` | string \| null | `^TASK-(REQ\|BUG)-\d{5}-\d{5}$` 或 `^TASK-(REQ\|BUG)-…\|^REQ-\d{5}-\d{5}$` 或 `^REQ-\d{5}-\d{5}$`(透传) | 关联任务 |

### 关系
- 1 个 `BugRow` 对应 1 行看板"缺陷清单"
- 1 个 `RequirementDetail` 关联 0..N 个 `BugRow`(`relatedTask` 字段匹配 `REQ-NNNNN-` 前缀)

### 依据规范
- `dashboard-conventions.md §规则 1`:字段枚举由看板列定义
- `encoding-conventions.md §规则 1`:`BUG-NNNNN` 严格按权威源

---

## D-7:RequirementDetail(需求详情,对应需求模式)

### 字段
| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `id` | string | `^REQ-\d{5}$` | 需求编码 |
| `title` | string | 可能为空 | 需求标题 |
| `status` | enum | 同 D-5 | 需求状态 |
| `design` | enum | `已完成` / `未开始` / `—` | 概要设计状态 |
| `plan` | enum | `已完成` / `未开始` / `—` | 详细设计状态 |
| `tasks` | `TaskRow[]` | 来自 `plan/<REQ>/PLAN.md` "任务总览" 表格 | 任务清单 |

### 关系
- 1 个 `RequirementDetail` 对应 1 个 `require/<REQ>/RESULT.md` + 1 个 `plan/<REQ>/PLAN.md`
- 1 个 `RequirementDetail` 关联 0..N 个 `BugRow`

### 依据规范
- `dashboard-conventions.md §规则 1`:字段枚举由看板列定义

---

## D-8:ErrorInfo(错误信息,对应错误模式)

### 字段
| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `code` | enum | `E-1` ~ `E-10` | 错误码(本技能自定,与 FR-5/6/7 边界一致) |
| `message` | string | NOT NULL | 错误消息(屏幕显示用) |
| `guide` | string \| null | 错误模式时 = 用户引导 | 用户引导(例:`"请先执行: /code-version <版本号>"`) |

### 关系
- 1 个 `ErrorInfo` 由 1 次 `parseArgs()` / `readCurrentVersion()` 等步骤产生
- 错误模式:不进入步骤 3/4/5,直接 `printOutput(segments)` + 退出

### 依据规范
- NFR-2:任何错误不崩溃;L1 退出 / L2 退化 / L3 兜底

---

## 数据迁移

### 6.3 迁移需求
**无**(本技能无持久化数据,所有数据结构为内存对象,生命周期 ≤ 1 次调用)

### 灰度策略
**无**

### 回滚方案
**无需回滚**(本技能为只读型,无副作用);若发现问题,删除 `plugins/code-skills/skills/code-dashboard/SKILL.md` 即可

---

## 总结

| 维度 | 结论 |
| --- | --- |
| 新增持久化实体 | **0** |
| 新增内存数据结构 | **8**(`Suggestion` / `TaskId` / `ParseResult` / `TaskRow` / `RequirementRow` / `BugRow` / `RequirementDetail` / `ErrorInfo`) |
| 既有数据修改 | **0** |
| 迁移脚本 | **0** |
| 触发 `dashboard-conventions §规则 1` | **否**(不扩展看板字段) |
