# 模块拆分 — REQ-00001
更新时间:2026-06-03 20:25
版本:V0.0.1

## 总览

本需求**不新增、不修改任何应用模块**(本仓库无应用代码)。变更仅限于:

| 状态 | 文件 / 模块 | 职责 | 变更类型 |
| --- | --- | --- | --- |
| **修改** | `.claude-plugin/marketplace.json` | marketplace 协议清单根 `name` | 字符串 1 行替换 |
| **修改** | `plugins/code-skills/README.md` | 中文版使用说明 | 字符串多处替换(命令 + 解释) |
| **修改** | `plugins/code-skills/README.en.md` | 英文版使用说明 | 字符串多处替换,与中文版**同次提交** |
| **可能修改** | `plugins/code-skills/CLAUDE.md` | AI 工作指引 | `code-it` 阶段 Grep 后决定;若 0 命中,记录"已核查,无需修改" |
| **不动** | `plugins/code-skills/.claude-plugin/plugin.json` | 插件元信息 | 严禁修改(`marketplace-protocol.md §规则 1.3`) |
| **不动** | `plugins/code-skills/`(目录本身) | 插件根目录 | 严禁修改 |
| **不动** | `plugins/code-skills/skills/*` | 10 个技能 | 严禁修改(FR-7) |
| **不动** | `plugins/code-skills/skills/*/templates/*` | 技能模板 | 严禁修改(FR-7) |
| **不动** | `./assistants/rules/*` | 项目级规范 | 严禁修改(FR-7) |
| **不动** | `./assistants/V0.0.0/*` | 基线版本 | 严禁修改(FR-7) |

## 模块清单(逐项)

### 1. `.claude-plugin/marketplace.json` — 根 `name` 字段

| 项 | 值 |
| --- | --- |
| 模块名 | marketplace 根协议清单 |
| 路径 | `.claude-plugin/marketplace.json`(相对仓库根) |
| 状态 | **修改既有**(字符串替换,非结构性变更) |
| 职责 | 描述本仓库作为 Claude Code marketplace 暴露给 Claude Code 安装器的"市场名称"与所含 plugin 列表 |
| 对外接口 | `name`(根);`version`(根);`owner`;`plugins[].(name, version, source, skills, keywords)` |
| 本次变更 | 仅根 `name`:`"code-skills"` → `"code-skills-marketplace"` |
| 依赖 | 无(纯 JSON 文件) |
| 关键决策 | 用 `Edit` 工具,精确定位"`"name": "code-skills"`"行(避免误改 `plugins[].name` / `owner.name`) |
| 规范遵循 | `marketplace-protocol.md §规则 1.1`(`$schema` 保持);`§规则 1.2`(`name` 改后仍 kebab-case);`§规则 1.3`(`plugins[].name` 与 plugin.json 同步保持);`§规则 1.6`(不引入未知字段) |

### 2. `plugins/code-skills/README.md` — 中文版使用说明

| 项 | 值 |
| --- | --- |
| 模块名 | 中文版使用说明 |
| 路径 | `plugins/code-skills/README.md` |
| 状态 | **修改既有** |
| 职责 | 介绍本插件、含安装命令、用法说明、技能清单等 |
| 本次变更 | 把所有 `code-skills@code-skills` 形式的 install 命令替换为 `code-skills@code-skills-marketplace`;所有显式表述"marketplace name 是 `code-skills`"或类似含义的文字调整 |
| 关键决策 | 用 `Edit` 工具,逐处精确替换;**不修改**与本次改名无关的章节 |
| 规范遵循 | `doc-conventions.md §规则 2`(命令与实际状态一致);`§规则 1`(与英文版同次提交) |

### 3. `plugins/code-skills/README.en.md` — 英文版使用说明

| 项 | 值 |
| --- | --- |
| 模块名 | 英文版使用说明 |
| 路径 | `plugins/code-skills/README.en.md` |
| 状态 | **修改既有**(与中文版**同次提交**同步) |
| 职责 | 中文版的英文对仗版,供英文用户阅读 |
| 本次变更 | 与中文版**逐项对应**:install 命令 / marketplace name 解释 / 任何相关字面量引用 |
| 关键决策 | 对照中文版改动逐项同步;由 `code-review` 阶段并列对比两个文件 |
| 规范遵循 | `doc-conventions.md §规则 1`(结构对仗 + 同次提交同步) |

### 4. `plugins/code-skills/CLAUDE.md` — AI 工作指引(可选)

| 项 | 值 |
| --- | --- |
| 模块名 | Claude Code 在本仓库工作时的工作指引 |
| 路径 | `plugins/code-skills/CLAUDE.md` |
| 状态 | **可能修改**(取决于 Grep 命中) |
| 职责 | 供 Claude Code 读取的"工作约定" |
| 本次变更 | 仅当 Grep `code-skills@code-skills` 或 `marketplace name` 命中时才修改;若 0 命中,在偏差日志记录"已核查,无需修改" |
| 关键决策 | 不主动扩大范围;遵守 FR-7 反向约束(不修改与本需求无关的章节) |
| 规范遵循 | `doc-conventions.md §规则 2`(保持 README 实际状态一致) |

## 不变更项的强约束理由

| 项 | 约束来源 |
| --- | --- |
| `plugin.json` 任何字段 | `marketplace-protocol.md §规则 1.3`(marketplace 与 plugin 的 `name` 必须保持一致,本需求改的是 marketplace 根,plugin 标识保持) |
| `plugins/code-skills/` 目录 | NFR-2(协议合规);FR-2 显式禁止 |
| `git` 远端仓库名 | NFR-2(协议合规);FR-2 显式禁止 |
| 10 个 SKILL.md / 模板 | FR-7(本需求严禁修改);`skill-conventions.md §规则 1` |
| 5 个规范文件 | FR-7(本需求严禁修改) |
| V0.0.0 基线 | FR-7(本需求严禁修改) |
| `.claude/` 本地配置 | 不在 `git` 跟踪范围 |

## 自检清单(对照 `module-conventions.md §规则 1`)

- [x] 无资源散落到技能根目录(本需求不改任何技能资源)
- [x] 无资源放在仓库其它位置(本需求仅动根清单 + 文档)
- [x] 子目录命名遵循约定(本需求不创建新子目录)
