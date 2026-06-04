# 数据结构完整变更 — REQ-00006

更新时间:2026-06-04 17:01
版本:V0.0.2

## 1. 持久化数据结构

### 1.1 新增实体:无

本技能**不**新增任何持久化实体(无 DB、无 ORM)。所有"持久化"都是 Markdown 文件(由 ManualBuilder 写入 publish/),它们是"文档"不是"实体"。

### 1.2 修改实体:无

本技能**不**修改任何既有实体或文件(NFR-2 纯只读;FR-8 不修改其他 8 技能)。

### 1.3 数据迁移:无

## 2. 运行时数据结构(内存,SKILL 解释执行时)

详 design RESULT.md §9.1。本节简列字段总规格,供 `code-it` 阶段实现时参考。

### 2.1 PreflightResult

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| `passed` | bool | NOT NULL | — | 全部 3 区段均无未解决 → true |
| `reason` | string? | nullable | — | 失败原因(仅看板缺失/缺区段时填) |
| `undone` | list[UncompletedItem] | NOT NULL(可空) | — | 未完成项明细 |
| `stats.需求.总` | int | NOT NULL, >=0 | — | 需求清单总数 |
| `stats.需求.未完成` | int | NOT NULL, >=0, <=总 | — | 未完成需求数 |
| `stats.需求.状态分布` | dict[str, int] | NOT NULL | — | {`待开始`: N, `进行中`: M, ...} |
| `stats.任务.*` | 同上 | — | — | 任务清单统计 |
| `stats.缺陷.*` | 同上 | — | — | 缺陷清单统计 |

- 关系:无(单一聚合根)
- 存储选型:内存对象(Python dict / Claude 解释)
- 迁移脚本:不适用
- 依据规范:无

### 2.2 UncompletedItem

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `类型` | enum | NOT NULL, ∈{需求, 任务, 缺陷} | 区段名 |
| `编码` | string | NOT NULL | 看板编码列(REQ-NNNNN / TASK-REQ-NNNNN-NNNNN / BUG-NNNNN) |
| `标题` | string | nullable | 看板"标题"列(可能为空字符串) |
| `当前状态` | string | NOT NULL | 看板实际值(对任务,组合"开发=X 测试=Y") |
| `期望状态` | string | NOT NULL | 判定规则中要求的状态 |

### 2.3 BaselineResult

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `is_baseline` | bool | NOT NULL | 目标版本是否是基线 |
| `previous_version` | string? | nullable(基线时 null) | 字典序前一个版本号 |
| `all_versions_sorted` | list[string] | NOT NULL | 字典序排序的所有版本(调试用) |

### 2.4 ManualBuildResult

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `written` | list[string] | NOT NULL | 写入的文件路径列表 |
| `overwritten` | list[string] | NOT NULL | 覆盖的文件路径(written 的子集) |
| `skipped` | list[string] | NOT NULL | 跳过的文件(基线时的 UPDATE.md) |

### 2.5 QandaScaffoldResult

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `status` | enum | NOT NULL, ∈{已存在, 本次创建, 创建失败} | qanda 目录处理结果 |
| `error_msg` | string? | nullable | 失败原因(status=创建失败 时填) |

### 2.6 QandaAggregateResult(中间数据,供 ManualBuilder 消费)

| 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- |
| `content` | string | NOT NULL | 渲染后的 Q&A.md 字符串 |
| `source_files` | list[string] | NOT NULL | 聚合的文件路径(可空) |
| `warnings` | list[string] | NOT NULL | 读取警告列表 |

## 3. 读侧数据格式(看板表格的解析对象)

### 3.1 需求清单(主表) — 严格定义

锚点:`^## 需求清单$`

列(按 V0.0.1 与 V0.0.2 看板模板):
| 列名 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- |
| `需求编码` | string | ✓ | 格式 `REQ-NNNNN` |
| `标题` | string | ✓ | 简短 |
| `状态` | enum | ✓ | ∈{`待开始`, `进行中`, `已完成`, `已取消`, `阻塞`}(注:实际看板中观察到"已完成(需求分析)"等带后缀的值,本技能用 `startswith("已完成")` 容忍) |
| `创建时间` | datetime | ✓ | — |
| `完成时间` | datetime? | nullable | 未完成时为 `—` |
| `需求文档` | string(markdown link) | ✓ | — |
| `概要设计` | string(markdown link)? | nullable | — |
| `详细设计` | string(markdown link)? | nullable | — |

**判定规则**:解决 ⟺ `状态 startswith "已完成"`

### 3.2 任务清单(主表) — 严格定义

锚点:`^## 任务清单$`

列:
| 列名 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- |
| `任务编号` | string | ✓ | 格式 `TASK-REQ-NNNNN-NNNNN` 或旧 `REQ-NNNNN-NNN` 等;按字符串处理(E-9) |
| `需求` | string | ✓ | — |
| `类型` | enum | ✓ | — |
| `触发/来源` | enum | ✓ | — |
| `标题` | string | ✓ | — |
| `开发状态` | enum | ✓ | ∈{`待开始`, `进行中`, `已完成`, `已取消`, `阻塞`, `待重新评估`} |
| `测试状态` | enum | ✓ | ∈{`未编写`, `已编写`, `已运行-通过`, `已运行-失败`, `不适用`, `阻塞`} |
| `涉及文件` | string | ✓ | — |
| `完成时间` | datetime? | nullable | — |
| `提交哈希` | string? | nullable | — |
| `关联任务` | string? | nullable | — |

**判定规则**:解决 ⟺ `开发状态 == "已完成" ∧ 测试状态 ∈ {"已运行-通过", "不适用"}`

### 3.3 缺陷清单(主表) — 严格定义

锚点:`^## 缺陷清单$`

列:
| 列名 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- |
| `缺陷编号` | string | ✓ | 格式 `BUG-NNNNN` |
| `严重度` | enum | ✓ | ∈{`P0`, `P1`, `P2`, `P3`} |
| `标题` | string | ✓ | — |
| `状态` | enum | ✓ | ∈{`待修复`, `已修复`}(可能还有 `修复中` / `修复规划中` — `code-fix` 维护) |
| `报告时间` | datetime | ✓ | — |
| `修复时间` | datetime? | nullable | — |
| `关联任务` | string? | nullable | — |
| `修复提交` | string? | nullable | — |

**判定规则**:解决 ⟺ `状态 == "已修复"`

## 4. 写侧数据格式(publish/ 下 3 份手册)

详 needs §6.1 / §6.2 / §6.3 + design RESULT.md §7.2.8 / §7.2.9 / §7.2.10。

### 4.1 DEPLOY.md 字段(8 章节)

完整章节顺序:
1. 概述
2. 打包(含 2.1 软件包 / 2.2 目录 / 2.3 镜像 子节)
3. 获取成果物
4. 上传服务器
5. 初始化系统(含 5.1 / 5.2 / 5.3 / 5.4 子节)
6. 启动运行
7. 首次进入软件系统
8. 验证清单

**placeholder 集合**:
- 自动填充:`<本版本号>`
- 用户补全:`<打包方式>` / `<output>` / `<source_dir>` / `<image_name>` / `<version>` / `<environment dependency>` / `<DB 脚本路径>` / `<初始化数据脚本>` / `<配置文件路径>` / `<key>` / `<value>` / `<启动命令>` / `<首次访问 URL>` / `<默认账号>` / 等

### 4.2 UPDATE.md 字段(8 章节,§8 回滚为新增)

完整章节顺序:
1. 概述(含源/目标版本 / 升级方式)
2. 打包
3. 获取成果物
4. 上传服务器
5. 初始化系统(含 5.1 DB 升级 / 5.2 配置 diff)
6. 重新启动软件
7. 验证清单
8. 回滚方案(新增,DEPLOY.md 没有)

**placeholder**:
- 自动填充:`<本版本号>` / `<源版本>`
- 用户补全:其余同 DEPLOY.md + `<DB 回滚脚本>`

### 4.3 Q&A.md 字段

- 文首:`# 发布部署 Q&A — <本版本号>`(自动填充)
- 引言:`> 本手册聚合自 ...`
- 章节:N 个 `## <主题>(来源:qanda/<文件>)` 形式,内容为聚合的文件正文
- 末尾占位:`## 占位:常见问题(待补充)`

### 4.4 qanda/README.md 字段(本需求顺带创建)

- 文首:`# assistants/qanda/ — 项目级 Q&A 长期沉淀目录`
- `## 用途`:Q&A 长期沉淀
- `## 文件命名建议`:`<主题>.md`(如 `deploy-faq.md` / `db-init-faq.md`)
- `## 引用规范`:被 `code-publish` 聚合到 `Q&A.md`(自动排除 README.md)
- `## 维护方式`:暂时人工整理(Q-2 锁定)
