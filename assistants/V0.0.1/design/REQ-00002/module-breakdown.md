# 模块拆分 — REQ-00002
更新时间:2026-06-03 20:25
版本:V0.0.1

## 总览

本需求**不新增、不修改任何应用模块**(本仓库无应用代码)。变更仅限于**协议文本 / 模板示例 / 文档示例**的字符串替换,以及(条件)2 个新文件。

变更按"文件类型"分组(详见 design-notes.md §Q-4 选定方案):

| 状态 | 文件 / 模块分组 | 文件数 | 职责 | 变更类型 |
| --- | --- | --- | --- | --- |
| **修改** | 10 个 SKILL.md | 10 | 各技能正文中的编码格式说明 / regex / 示例 | 字符串多处替换(不动 frontmatter) |
| **修改** | 20+ 模板(占位符 + 示例值) | 20+ | 各技能产出的文档模板 | 字符串多处替换 |
| **修改** | README.md + README.en.md(中英同次提交) | 2 | 用户面向的使用说明 | 字符串多处替换 |
| **修改** | CLAUDE.md | 1 | AI 工作指引 | 字符串多处替换 |
| **修改** | version-RESULT.md 模板 | 1 | 看板模板示例值 | 字符串多处替换(**不改字段语义,不触发 dashboard-conventions §规则 1**) |
| **可能修改** | (Q-6=H2)V0.0.0/EXISTING-* 文件**内**文本 | 10 | 基线文档内的示例字符串 | 若 Q-6=H1(默认)→ 不改;若 H2 → 批量替换 |
| **可能新增** | (Q-8=a)`./assistants/rules/encoding-conventions.md` | 1 | 编码格式权威约束源 | **本需求不直接操作**;由 `code-rule` 在实施阶段创建 |
| **可能新增** | (Q-9=a)`./assistants/V0.0.1/require/REQ-00002/migration-mapping.md` | 1 | 新旧编码映射表 | 新建 |
| **不动** | `marketplace.json` | 1 | marketplace 协议清单 | FR-10 严禁修改 |
| **不动** | `plugin.json` | 1 | 插件元信息 | FR-10 严禁修改 |
| **不动** | `plugins/code-skills/` 目录 | 1 | 插件根 | FR-10 严禁修改 |
| **不动** | git 远端仓库名 | — | 远端 | FR-10 严禁修改 |
| **不动** | 10 个 SKILL.md frontmatter | 10 | `name` + `description` | `skill-conventions §规则 1`;本需求只改正文 |
| **不动** | `./assistants/rules/` 下 5 个现有规范 | 5 | 项目级规范 | 严禁修改(本需求范围) |
| **不动** | (Q-6=H1)V0.0.0 EXISTING- 目录名 | 10 | 基线目录 | REQU FR-10;基线特例保持 |
| **不动** | `./assistants/V0.0.1/require/REQ-00001/` 已重命名内容 | — | 已落地的追溯重命名 | ✅ 已于 2026-06-03 20:20 完成 |

## 模块清单(逐项)

### 1. 10 个 SKILL.md — 编码格式正文

| 项 | 值 |
| --- | --- |
| 模块名 | 10 个技能的入口文档 |
| 路径 | `plugins/code-skills/skills/<code-init|code-version|code-rule|code-require|code-design|code-plan|code-it|code-unit|code-fix|code-review>/SKILL.md` |
| 状态 | **修改既有**(字符串替换,非结构性变更) |
| 职责 | 各技能的入口文档;含 YAML frontmatter + Markdown 正文 |
| 本次变更 | 把"编码格式"相关描述(占位符、示例值、regex、编号分配逻辑)统一替换为新格式;**frontmatter 保持不变** |
| 关键决策 | 用 `Edit` 工具,逐处精确替换;**不修改** frontmatter(`skill-conventions.md §规则 1`) |
| 规范遵循 | `skill-conventions.md §规则 1`(frontmatter 必含且不破坏) |

### 2. 20+ 模板 — 编码示例值与占位符

| 项 | 值 |
| --- | --- |
| 模块名 | 各技能产出的文档模板 |
| 路径 | `plugins/code-skills/skills/*/templates/*.md`(20+ 文件,含 `assistants-layout.md` 的 10 个副本) |
| 状态 | **修改既有** |
| 职责 | 各技能在 `code-plan` / `code-design` / `code-it` / `code-review` 等阶段产出的文档样板 |
| 本次变更 | 把示例值 `REQ-2026-0001` → `REQ-00001`、`BUG-001` → `BUG-00001`、`REQ-2026-0001-001` → `TASK-REQ-00001-00001`;占位符 `<REQ-YYYY-NNNN>` → `<REQ-NNNNN>`、`<BUG-NNN>` → `<BUG-NNNNN>`、`<任务编码>`(旧嵌套)→ `<TASK-REQ-NNNNN-NNNNN>` 或 `<TASK-BUG-NNNNN-NNNNN>` |
| 关键决策 | 用 `Edit` 工具,逐处精确替换;**不修改**模板的章节结构 / 表格列 / 字段名 |
| 规范遵循 | `module-conventions.md §规则 1`(资源在 `templates/` 子目录) |

### 3. README.md + README.en.md(中英同次提交)

| 项 | 值 |
| --- | --- |
| 模块名 | 仓库使用说明(中/英) |
| 路径 | `plugins/code-skills/README.md` / `plugins/code-skills/README.en.md` |
| 状态 | **修改既有**(与中文版**同次提交**同步) |
| 职责 | 用户面向的工作流管道说明、命令示例、状态机、典型流程 |
| 本次变更 | 把所有 `REQ-YYYY-NNNN` / `BUG-NNN` / `REQ-2026-0001` / `code-it <REQ-YYYY-NNNN-001>` 等示例替换为新格式 |
| 关键决策 | 用 `Edit` 工具,逐处精确替换;**中英同次提交**(`doc-conventions.md §规则 1`) |
| 规范遵循 | `doc-conventions.md §规则 1`(结构对仗 + 同次提交同步);`§规则 2`(命令反映实际) |

### 4. CLAUDE.md — AI 工作指引

| 项 | 值 |
| --- | --- |
| 模块名 | Claude Code 在本仓库的工作指引 |
| 路径 | `plugins/code-skills/CLAUDE.md` |
| 状态 | **修改既有** |
| 职责 | 供 Claude Code 读取的工作约定 |
| 本次变更 | 把第 24/88/99/100 行等含 `BUG-NNN`、`REQ-YYYY-NNNN` 引用的文字替换为新格式 |
| 关键决策 | 用 `Edit` 工具,逐处精确替换 |
| 规范遵循 | `doc-conventions.md §规则 2`(命令与实际状态一致) |

### 5. version-RESULT.md 模板 — 看板模板示例值

| 项 | 值 |
| --- | --- |
| 模块名 | 版本看板样板 |
| 路径 | `plugins/code-skills/skills/code-version/templates/version-RESULT.md` |
| 状态 | **修改既有**(只改示例值) |
| 职责 | 各版本 `RESULT.md` 的实际样板 |
| 本次变更 | 把所有 `REQ-YYYY-NNNN` / `BUG-001` / `T-001` / `REQ-2026-0001-001` 等示例值替换为新格式 |
| 关键决策 | **不触发** `dashboard-conventions.md §规则 1` 三处同步(本需求只改示例值,不改字段语义 / 区段结构 / 表格列);`doc-conventions §规则 2` 仍要求示例值反映新格式 |
| 规范遵循 | `dashboard-conventions.md §规则 1`(纯排版/示例值调整不触发本规则) |

### 6. (条件 Q-8 = a)`./assistants/rules/encoding-conventions.md` — 编码格式权威源

| 项 | 值 |
| --- | --- |
| 模块名 | 编码格式权威约束源 |
| 路径 | `./assistants/rules/encoding-conventions.md` |
| 状态 | **可能新增**(取决于 Q-8) |
| 职责 | 编码格式的"单一事实源";10 个 SKILL.md 引用本规则,不硬编码 |
| 本次变更 | 若 Q-8 = a(本设计默认):**本需求不直接写入**;由用户在 `code-it` 阶段调 `code-rule` 技能创建 |
| 关键决策 | REQU FR-7 显式说明"本需求不直接写入 rules/";由 `code-rule` 维护边界 |
| 规范遵循 | `./assistants/rules/` 是 `code-rule` 唯一写入位置(CLAUDE.md §"版本感知工作空间约定") |

### 7. (条件 Q-9 = a)`./assistants/V0.0.1/require/REQ-00002/migration-mapping.md` — 新旧编码映射

| 项 | 值 |
| --- | --- |
| 模块名 | 新旧编码映射表 |
| 路径 | `./assistants/V0.0.1/require/REQ-00002/migration-mapping.md` |
| 状态 | **可能新增**(取决于 Q-9) |
| 职责 | 记录旧编码 → 新编码、改名时间、涉及文件清单 |
| 本次变更 | 若 Q-9 = a(本设计默认):新建文件,含 `REQ-2026-0001 → REQ-00001` 一行(及已知变更) |
| 关键决策 | 由 `code-it` 阶段实施;在 FR-6 部分已提前落地的基础上,补充完整映射 |
| 规范遵循 | (无直接规范) |

### 8. (条件 Q-6 = H2)V0.0.0 EXISTING-001~010 文档**内**文本

| 项 | 值 |
| --- | --- |
| 模块名 | 基线版本(10 个需求)的文档内示例字符串 |
| 路径 | `./assistants/V0.0.0/require/EXISTING-001~010/RESULT.md` 等 |
| 状态 | **可能修改**(取决于 Q-6) |
| 职责 | 基线版本的"代码现状"快照,语义独立 |
| 本次变更 | 若 Q-6 = H1(本设计默认):**不改** EXISTING- 任何文件;若 H2:批量替换文档内 `REQ-2026-0001` 等旧编码字符串 |
| 关键决策 | Q-6 待澄清,本设计采用默认 H1;回退路径已记录 |
| 规范遵循 | REQU FR-10(严禁修改 V0.0.0,除非 Q-6 = H2) |

## 不变更项的强约束理由

| 项 | 约束来源 |
| --- | --- |
| `marketplace.json` 任何字段 | `marketplace-protocol.md §规则 1`;REQU FR-10 |
| `plugin.json` 任何字段 | 同上 |
| `plugins/code-skills/` 目录 | NFR-2(协议合规);REQU FR-10 |
| git 远端仓库名 | NFR-2;REQU FR-10 |
| 10 个 SKILL.md frontmatter | `skill-conventions.md §规则 1`(本需求只改正文) |
| 5 个 `./assistants/rules/` 现有规范 | FR-7 严禁修改 |
| V0.0.0 EXISTING- 目录名(Q-6=H1) | REQU FR-10 |
| `.claude/` 本地配置 | 不在 `git` 跟踪范围 |
| 模板的章节结构 / 表格列 / 字段名 | `module-conventions.md §规则 1`;`doc-conventions.md §规则 1` |

## 自检清单(对照 `module-conventions.md §规则 1`)

- [x] 无资源散落到技能根目录(本需求不改任何技能资源)
- [x] 无资源放在仓库其它位置(本需求仅改原位置文本)
- [x] 子目录命名遵循约定(本需求不创建新子目录)
- [x] (Q-8=a)新建的 `encoding-conventions.md` 放在 `./assistants/rules/`,由 `code-rule` 维护
- [x] (Q-9=a)新建的 `migration-mapping.md` 放在本需求工作目录(REQU 显式指定)
