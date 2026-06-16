# 工作目录布局参考 — code-plan(版本感知)

> `code-plan` 技能强制约定。所有路径以**当前工作目录(CWD)**为基准。
> 本技能受 `code-version` 管理,实际工作空间 = `./assistants/<版本号>/`(由 `./assistants/.current-version` 决定)。

## 整体布局
```
<项目根目录>/
├── assistants/
│ ├── rules/ ← 项目级规范(只读,跨版本共享)
│ │ ├── architecture.md
│ │ ├── module-conventions.md
│ │ ├── api-standards.md
│ │ ├── data-modeling.md
│ │ └── ...
│ ├── .current-version ← 当前激活版本标记
│ │ (内容示例:v1.0.0)
│ └── <版本号>/ ★ 版本工作空间
│ ├── RESULT.md ← 版本开发进度看板
│ ├── require/
│ │ └── REQ-00001/
│ │ ├── RESULT.md ← 上游需求,本技能只读
│ │ └── ...
│ ├── design/
│ │ └── REQ-00001/
│ │ ├── RESULT.md ← 上游概要设计,本技能只读
│ │ └── ...
│ └── plan/ ← 本技能产出,可写
│ └── REQ-00001/
│ ├── RESULT.md # 详细设计
│ ├── PLAN.md # 编码计划(任务列表 + 状态)
│ ├── materials-index.md
│ ├── design-notes.md
│ ├── module-details.md
│ ├── interface-specs.md
│ ├── data-changes.md
│ ├── risk-analysis.md
│ ├── rule-compliance.md
│ └── clarifications.md
├── src/ # 用户的项目源码(本技能只读,用于核对实现细节)
├── package.json / pyproject.toml / ... # 用户的项目配置
└── ...
```

## 上游三件套
本技能消费三个上游,均只读:
| 上游 | 路径 | 用途 |
| --- | --- | --- |
| 需求 | `./assistants/<版本号>/require/<需求编号>/RESULT.md` | FR / NFR / AC / 验收标准 |
| 概要设计 | `./assistants/<版本号>/design/<需求编号>/RESULT.md` | 模块拆分 / 接口概要 / 数据结构 / 决策 |
| 规范 | `./assistants/rules/` 下所有文件 | 硬约束(跨版本共享) |

**任一上游缺失**:本技能会拒绝继续,提示先去跑上游技能或补规范。

## 本技能双输出
- `<版本号>/plan/<需求编号>/RESULT.md`:详细设计,每个详细设计点都应有对应的 `PLAN.md` 任务
- `<版本号>/plan/<需求编号>/PLAN.md`:编码计划,每条任务都应能追溯回 `RESULT.md` 的设计点

**交叉验证是必需步骤**:技能结束前必须保证两个文件相互一致。

## 任务编号规范
- 格式:`TASK-(REQ|BUG)-NNNNN-NNNNN`,如 `TASK-REQ-00001-00001`
- 任务序号五位补零,自 00001 起递增
- **编号一经分配就稳定**,后续增量更新不会复用旧编号
- 已完成/已取消任务的编号也保留,作为历史

## 任务状态机
```
待开始 ──开始──→ 进行中 ──完成──→ 已完成(终态)
 │
 ├──阻塞──→ 阻塞 ──解除──→ 进行中
 │
 └──取消──→ 已取消(终态,不可恢复)
```
- `已完成` 与 `已取消` 都是终态,**不可修改**
- 终态任务如需重做,新增"修改类"任务并通过"关联任务"字段指向旧任务
- `待重新评估`:用于外部条件变化导致任务需要重新审视,可回到 `待开始` 或 `进行中`

## 任务双状态(开发 + 测试)
每条任务有**两个正交的状态字段**:
- **开发状态**:`待开始` / `进行中` / `已完成` / `已取消` / `阻塞` / `待重新评估`(由 `code-it` 推进)
- **测试状态**:`未编写` / `已编写` / `已运行-通过` / `已运行-失败` / `不适用` / `阻塞`(由 `code-unit` 推进)

**任务真正可发布 = 开发状态=已完成 ∧ 测试状态∈{已运行-通过, 不适用}**

## 任务触发/来源(每条任务)
13 个枚举值,决定 `code-it` 的输入源:
- 大多数 → `./assistants/<版本号>/plan/<需求编号>/RESULT.md`
- **`审查改修`** → `./assistants/<版本号>/review/<任务编码>/RESULT.md`(由 `code-check` 派生时使用)
- `需求撤回` → 任务标"已取消",无输入

## 用户 vs 技能产出
| 类别 | 写入方 | 修改方 |
| --- | --- | --- |
| `RESULT.md` | 技能 | 技能(增量更新) |
| `PLAN.md` | 技能 | 技能(增量更新 + 状态推进) |
| 任务开发状态 | 技能(根据用户告知) | `code-it` 主动推进 |
| 任务测试状态 | 技能(根据用户告知) | `code-unit` 主动推进 |
| 过程文档 | 技能 | 技能 |
| `<版本号>/RESULT.md`(看板) | code-version 初始化;本技能追加"详细设计与任务计划汇总" / "任务清单" / "里程碑" / "变更记录" | 只能追加,不能重写其他区段 |
| `./assistants/rules/` | 用户 | 用户(本技能不写) |
| `./assistants/<版本号>/require/<需求编号>/` | 用户 / code-require | 用户 / code-require(本技能只读) |
| `./assistants/<版本号>/design/<需求编号>/` | 用户 / code-design | 用户 / code-design(本技能只读) |
| CWD 下的项目源码 | 用户 | 用户 / 后续 code-it |

> 用户不应手动改 `RESULT.md` / `PLAN.md`。如有调整:
> - 改规范 → 改 `./assistants/rules/`,重跑 `code-design` → 重跑 `code-plan`
> - 改需求 → 改上游材料,重跑 `code-require` → 重跑 `code-design` → 重跑 `code-plan`
> - 改概要设计 → 改 `<版本号>/design/<编号>/RESULT.md`,重跑 `code-plan`
> - 改详细设计 → 直接重跑 `code-plan`,选增量更新分支
> - 推进任务状态 → 重跑 `code-plan`,告知哪些任务状态变化

## 多项目隔离
不同项目的 `assistants/` 完全独立。

## 跨计划检索
本技能会扫描 `./assistants/<版本号>/plan/*/PLAN.md` 寻找关联计划(同版本);
可选:跨版本扫描 `./assistants/*/plan/*/PLAN.md`(需用户授权)。
为保证检索质量:
- 关键模块名/接口名/数据结构名在 `PLAN.md` 与 `RESULT.md` 中保持一致命名
- 任务标题中包含动词 + 对象 + 关键限定,便于 grep
- 详细字段放在过程文档,`PLAN.md` 只放表格与任务详情
- 跨版本关联时注明"所在版本"
