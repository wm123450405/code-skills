# REQ-00028 — 新增 code-answer 技能(概要设计)

- 需求编码:REQ-00028
- 所属版本:V0.0.3
- 设计状态:已完成
- 创建:2026-06-10
- 最近更新:2026-06-10
- 当前版本:v1
- 上游:`./assistants/V0.0.3/require/REQ-00028/RESULT.md`
- 遵循规范:`./assistants/rules/` 下 13 个文件(已逐条对照)

## 1. 设计目标

> `--balanced` — code-auto 上下文自动采纳(沿用 REQ-00011 + REQ-00020 简化为 1 维度)

- **整体设计目标**:`--balanced`(平衡型,不强扩展也不极简)

## 2. 设计概述

REQ-00028 的本质是**新增一个"只读查询型"技能元数据**。`code-answer` 不创造新模块、不引入新依赖、不改既有 11 个技能;它通过 1 个新文件 `plugins/code-skills/skills/code-answer/SKILL.md` 提供"按关键字或编号查询功能逻辑"的能力。架构上完全沿用 `code-dashboard` 的"只读 + 屏显"范式,工具集限定 `Read` / `Glob` / `Grep`,**严禁** `Write` / `Edit` / `Bash`。

## 3. 关键决策与不变量

### 3.1 决策(D-1 ~ D-5)

| ID | 决策 | 依据 |
| --- | --- | --- |
| **D-1** | `code-answer` 是**单文件技能**(仅 1 个 `SKILL.md`,不放子目录) | 技能无模板/无清单/无指南;沿用 `module-conventions §规则 1` 反面示例(本需求不触发该规则,因为无资源文件) |
| **D-2** | 工具集严格 `{Read, Glob, Grep}` | 沿用 `code-dashboard` 范式;`NFR-3.AC-1` 严守;FR-6 强约束 |
| **D-3** | 扫描范围 = `./assistants/*/require/*/RESULT.md`(全版本) | 用户澄清记录 2026-06-10 §问题 1 |
| **D-4** | 源码目录候选列表 = `src/` `lib/` `app/` `pkg/` `cmd/` `internal/` `packages/` `modules/` `core/` | 用户澄清记录 2026-06-10 §问题 2 |
| **D-5** | 报告**仅屏显**,**不**落盘任何文件(无 `auto-report.md`、无 `RESULT.md` 类产出) | 用户澄清记录 2026-06-10 §问题 3 |

### 3.2 不变量(INV-1 ~ INV-5)

- **INV-1**:**不**修改 `plugins/code-skills/skills/` 下其他 11 个 `code-*` 技能的 `SKILL.md`(`code-dashboard` 范式零修改,沿用 `code-design` 既有契约)
- **INV-2**:**不**修改 `marketplace.json` / `plugin.json`(走 Claude Code 技能自动发现协议,新增技能目录后 Claude Code 自动发现)
- **INV-3**:**不**修改 `./assistants/rules/` 下任何文件(项目级规范,`code-rule` 责任)
- **INV-4**:**不**产生任何结果文件(无 `RESULT.md` / `auto-report.md` / `require/<REQ>/...`)— 本技能的"产物"仅是屏显 stdout
- **INV-5**:**不**产生任何过程文件(无 `materials-index.md` / `analysis-notes.md` / `clarifications.md` 等) — 屏显即终态

## 4. 模块拆分

### 4.1 新增模块

| 模块 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| `code-answer` 技能 | `plugins/code-skills/skills/code-answer/SKILL.md` | 新增 | 定义"只读功能查询"技能的目标 / 输入 / 输出 / 工作流 / 边界 | 无(无资源子目录,无三方依赖) |

### 4.2 复用既有模块

无 — 本技能是**纯只读查询**,不调用任何其他子技能,不读取 `.current-version` 之外的运行期状态。

### 4.3 模块边界自检(`module-conventions §规则 1` 沿用)

- ✅ 技能目录名 `code-answer` = `SKILL.md` `name: code-answer`(`skill-conventions §规则 1`)
- ✅ 技能根目录只放 `SKILL.md`,无散落的资源文件(`module-conventions §规则 1` 反面示例全无)
- ✅ 无资源子目录 — 本技能无 `templates/` / `checklists/` / `guidelines/`
- ✅ 依赖方向:本技能 → 既有需求清单 + 既有源代码(只读),不形成反向依赖

## 5. 接口

### 5.1 用户接口

- **调用形式**:`/code-answer <查询>`(单参数,空格分隔多 token 拼为单一字符串)
- **参数**:`<查询>` = 任意自然语言关键字 / `REQ-NNNNN` / `EXISTING-NNN`
- **返回值**:屏显报告(详见上游 RESULT.md §FR-5)
- **退出码**:成功 0 / 用法错误 1 / 内部错误 1(无副作用可污染)

### 5.2 工具接口(子技能内部使用)

| 工具 | 用途 | 引用规范 |
| --- | --- | --- |
| `Read "./assistants/.current-version"` | 可选版本上下文检测(FR-2) | `code-require` 既有契约 |
| `Read "<路径>"` | 读需求清单 / 源代码段 | — |
| `Glob "./assistants/*/require/*/RESULT.md"` | 列出全版本需求清单 | — |
| `Glob "./src/**/*"` 等常见源码目录 | 定位代码根 | D-4 |
| `Grep "<关键字>" --type <ext>` | 跨文件检索 | — |

### 5.3 严禁接口

| 工具 | 状态 | 依据 |
| --- | --- | --- |
| `Write` | **禁用** | INV-4, FR-6 |
| `Edit` | **禁用** | INV-4, FR-6 |
| `Bash` | **禁用** | FR-6 |
| `WebFetch` / `WebSearch` | **禁用** | FR-6 |
| `Task` / `Agent` | **禁用** | FR-6 |
| `cron` / `ScheduleWakeup` | **禁用** | FR-6 |

## 6. 数据结构

无新增数据结构 — 本技能不维护任何持久化状态;运行期临时变量(扫描结果数组)在函数返回时自动释放。

## 7. 三方依赖

无 — 本技能不引入任何新三方依赖(不写 `package.json` / `requirements.txt` / `go.mod` 等)。

## 8. 关联概要设计

| 关联设计 | 关联点 | 影响 | 链接 |
| --- | --- | --- | --- |
| `code-dashboard` (V0.0.2 REQ-00023) | 工具集范式 / 屏显契约 | 沿用 | `./assistants/V0.0.2/design/REQ-00023/RESULT.md` |
| `code-require` (V0.0.1 REQ-00001) | 输入源格式 | 需求清单主输入 | `./assistants/V0.0.1/design/REQ-00001/RESULT.md` |
| `code-init` (V0.0.0) | `EXISTING-NNN` 编号 | 基线需求主输入 | `./plugins/code-skills/skills/code-init/SKILL.md` |

## 9. 规范遵循

| 规范文件 | 条款 | 本设计状态 |
| --- | --- | --- |
| `skill-conventions §规则 1` | SKILL.md 必含 name + description, name = 目录名 | ✅ `name: code-answer` + 完整 description |
| `module-conventions §规则 1` | 资源文件必须放固定子目录 | ✅ 不适用(无资源文件) |
| `dashboard-conventions §规则 1` | 看板/模板扩展时同步 | ✅ 不适用(不涉及看板字段扩展) |
| `doc-conventions` | 文档编写风格 | ✅ 沿用既有 10 个技能的章节布局 |
| `coding-style` | 编码风格 | ✅ 不适用(本技能无代码) |
| `naming-conventions` | 命名风格 | ✅ 技能名 `code-answer` 沿用 kebab-case |
| `directory-conventions` | 目录结构 | ✅ 技能目录零子目录结构 |
| `framework-conventions` | 框架约定 | ✅ 不适用(本仓库无框架) |
| `dependency-conventions` | 依赖管理 | ✅ 不适用(无新增依赖) |
| `commit-conventions` | 提交规范 | ✅ 由 `code-it` 实施时遵循 |
| `migration-mapping` | 迁移映射 | ✅ 不适用(无旧版本映射) |
| `encoding-conventions` | 编号编码 | ✅ 沿用 `^REQ-\d{5}$` / `^EXISTING-\d{3}$` 接收端正则 |

### 用户授权的偏离

无 — 本设计完全符合既有规范。

### 规范 vs 需求冲突

无冲突 — 上游 RESULT.md 中 7 FR / 6 AC 均不触发规范冲突。

## 10. 待澄清 / 未决项

- **Q-1**(沿用上游):是否需要支持"反向查询"(从代码反向定位需求)? — 不影响本设计,留作 v2
- **Q-2**(沿用上游):关键字匹配是否需要支持正则表达式? — 不影响本设计,留作 v2
- **Q-3**(沿用上游):报告是否需要"导出为 Markdown"按钮? — 不影响本设计,留作 v2

## 11. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-10 11:00 | v1 | 初始创建 | 完成首次概要设计(5 决策 / 5 不变量 / 1 新增模块) | wangmiao |
