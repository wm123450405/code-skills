# 工程初始化报告 — V0.0.0

> 本报告由 `code-init` 技能生成,作为新成员(包括 AI Agent)快速理解本项目的入口。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`(项目当前状态)

## 项目概述

`code-skills` 是一套为 Claude Code 设计的技能(skill)集合,把软件开发的完整生命周期(版本管理 → 需求 → 概要设计 → 详细设计 → 编码 → 单元测试 → 评审 → 缺陷修复)标准化为可串接的 AI 工作流。插件以 Claude Code **marketplace** 协议打包,可通过 `claude plugin install code-skills@code-skills` 安装;所有技能以 `/code-skills:<name>` 形式调用。

## 技术栈

| 维度 | 选型 |
| --- | --- |
| 语言 | Markdown(技能描述)+ JSON(清单/元信息) |
| 框架 | Claude Code Skill SDK(技能 = 含 YAML frontmatter 的 `SKILL.md`) |
| 数据库 | 无 |
| 缓存 | 无 |
| 消息队列 | 无 |
| 构建/包管理 | 无(纯文档/配置项目,无源码编译) |
| 测试框架 | 无 |
| CI/CD | 无 |
| 部署形态 | 通过 GitHub 仓库发布,用户 `marketplace add` → `plugin install` 消费 |

> 项目本体**不包含**任何应用层源代码、构建系统、测试框架或包管理配置 —— 它本身是一个"教 AI 如何做事的文档/技能仓库"。

## 目录结构

```
code-skills/                                 ← marketplace 仓库根
├── .claude-plugin/
│   └── marketplace.json                     # marketplace 清单(plugins[] 数组)
├── plugins/
│   └── code-skills/                         # 插件本体(与插件名同名)
│       ├── .claude-plugin/
│       │   └── plugin.json                  # 插件自身元信息(name/version/keywords)
│       ├── README.md                        # 中文:工作流总览 + 10 个技能的命令参考
│       ├── README.en.md                     # 英文版 README
│       ├── CLAUDE.md                        # 给 Claude Code 用的开发指南
│       └── skills/
│           ├── code-init/                   # 工程初始化(项目级一次性引导)
│           ├── code-version/                # 版本管理(版本感知入口)
│           ├── code-rule/                   # 编码规范管理(项目级共享)
│           ├── code-require/                # 需求分析
│           ├── code-design/                 # 概要设计
│           ├── code-plan/                   # 详细设计 + 任务计划 / 缺陷修复方案(双路径)
│           ├── code-it/                     # 开发编码 + 缺陷修复实施(双路径)
│           ├── code-unit/                   # 单元测试
│           ├── code-fix/                    # 缺陷登记与跟踪
│           └── code-review/                 # 代码评审
└── .gitignore
```

> 每个技能目录下文件布局统一为:`SKILL.md` + `templates/`(技能产出的文档模板)+ 可选 `guidelines/` / `checklists/`(强制执行的规则/校验清单)。

## 核心模块与职责

| 模块 | 路径 | 职责 | 对外暴露的接口 |
| --- | --- | --- | --- |
| `code-init` | `skills/code-init/` | 项目接入的一次性引导,扫描现有代码,登记为 `EXISTING-NNN` 需求,创建基线版本 | `/code-skills:code-init [初始版本号]` |
| `code-version` | `skills/code-version/` | 切换/创建版本工作空间,所有主流程技能的前置门 | `/code-skills:code-version [版本号]` |
| `code-rule` | `skills/code-rule/` | 维护 `./assistants/rules/` 项目级共享规范 | `/code-skills:code-rule "<自然语言规范描述>"` |
| `code-require` | `skills/code-require/` | 需求分析(版本感知) | `/code-skills:code-require <REQ-YYYY-NNNN>` |
| `code-design` | `skills/code-design/` | 概要设计(版本感知) | `/code-skills:code-design <REQ-YYYY-NNNN>` |
| `code-plan` | `skills/code-plan/` | 详细设计 + 任务拆分;或缺陷修复方案(双路径) | `/code-skills:code-plan <REQ-YYYY-NNNN \| BUG-NNN>` |
| `code-it` | `skills/code-it/` | 任务路径:开发编码;缺陷路径:修复实施(双路径) | `/code-skills:code-it <REQ-YYYY-NNNN-NNN \| BUG-NNN>` |
| `code-unit` | `skills/code-unit/` | 单元测试(任务路径) | `/code-skills:code-unit <REQ-YYYY-NNNN-NNN>` |
| `code-fix` | `skills/code-fix/` | 缺陷登记与状态跟踪(支线入口) | `/code-skills:code-fix "<bug 描述>" \| <BUG-NNN>` |
| `code-review` | `skills/code-review/` | 整需求代码评审,派生"审查改修"任务 | `/code-skills:code-review <REQ-YYYY-NNNN>` |
| Marketplace 清单 | `.claude-plugin/marketplace.json` | 仓库根:声明本仓库是一个 marketplace,列出 `plugins[]` | (Claude Code 启动时读取) |
| 插件清单 | `plugins/code-skills/.claude-plugin/plugin.json` | 插件元信息(name/version/keywords) | (Claude Code 启动时读取) |

## 入口与主流程

### 主入口
- 文件:`plugins/code-skills/.claude-plugin/plugin.json`(插件元信息)+ `plugins/code-skills/skills/*/SKILL.md`(各技能定义)
- 启动方式:用户执行 `claude plugin marketplace add <repo>` → `claude plugin install code-skills@code-skills` → `/reload-plugins`,之后在 Claude Code 中输入 `/code-skills:<skill-name>`

### 主流程链路
1. 项目接入:`code-init` 扫源码、生成 `INIT-REPORT.md`、登记 `EXISTING-NNN`、创建基线版本 `V0.0.0`
2. 建立规范:`code-rule` 把自然语言规范沉淀到 `assistants/rules/`(跨版本共享)
3. 开新版本:`code-version <V0.1.0>` 创建新开发版本,`.current-version` 切到 `V0.1.0`
4. 主流程(按需触发):`code-require` → `code-design` → `code-plan` → `code-it`(逐任务)→ `code-unit` → `code-review`
5. 支线流程(发现 bug):`code-fix` 登记 → `code-plan BUG-NNN` 规划 → `code-it BUG-NNN` 实施 → `code-fix BUG-NNN` 推进状态到关闭
6. 跨版本:任意时刻 `code-version <旧版本号>` 回看,该版本工作空间完整保留

## 外部接口

### 技能(本项目对外暴露的"接口")

| 调用方式 | 用途 |
| --- | --- |
| `/code-skills:code-init` | 工程初始化 |
| `/code-skills:code-version` | 版本管理 |
| `/code-skills:code-rule` | 编码规范管理 |
| `/code-skills:code-require` | 需求分析 |
| `/code-skills:code-design` | 概要设计 |
| `/code-skills:code-plan` | 详细设计 / 缺陷修复方案 |
| `/code-skills:code-it` | 开发编码 / 缺陷修复 |
| `/code-skills:code-unit` | 单元测试 |
| `/code-skills:code-fix` | 缺陷登记与跟踪 |
| `/code-skills:code-review` | 代码评审 |

> 用户通过 Claude Code 的技能调用协议输入上述命令,AI Agent 按对应 `SKILL.md` 工作流执行。

### CLI 命令(用户侧,非项目自身)
- `claude plugin marketplace add <repo-url>` — 注册 marketplace
- `claude plugin install code-skills@code-skills` — 安装插件
- `/reload-plugins` — 激活刚安装的技能

## 数据模型

无显式数据模型。本项目是文档/配置仓库,不持久化业务数据。

运行时"数据"完全由 `assistants/` 目录的文件系统结构表示:
- `.current-version` 文件内容 = 当前激活版本号
- `<版本号>/RESULT.md` = 版本开发进度看板(Markdown 表)
- `<版本号>/require/EXISTING-NNN/RESULT.md` = 现有功能需求文档
- `<版本号>/plan/<需求编号>/PLAN.md` = 任务计划(其中"任务编号"格式 `REQ-YYYY-NNNN-NNN`,3 位数任务序号)

## 构建与运行

### 构建
无。本项目无需编译。

### 启动
无(用户通过 Claude Code 加载)。

### 配置
- **插件清单**:`plugins/code-skills/.claude-plugin/plugin.json`(version 字段需与 marketplace 同步)
- **市场清单**:`.claude-plugin/marketplace.json`(plugins[].version 字段需与子插件同步)
- **无环境变量**。

## 测试情况

| 维度 | 现状 |
| --- | --- |
| 是否有测试 | 否(纯文档/配置项目,无可执行代码) |
| 测试框架 | 无 |
| 覆盖率 | 不适用 |
| 测试组织 | 无 |
| CI 集成 | 无 |

> 质量保证手段:`README.md` 给出每个技能的调用方式与典型场景;`CLAUDE.md` 给出"如何编写技能"和"双状态任务模型"的开发规约;`code-review` 自带 `checklists/review-checklist.md` 作为评审清单。

## 可复用资产

| 资产 | 位置 | 用途 |
| --- | --- | --- |
| 双状态任务模型 | `plugins/code-skills/CLAUDE.md`(开发状态 × 测试状态) | 贯穿 `code-it` / `code-unit` / `code-review` 的状态机定义 |
| 看板字段约定 | `plugins/code-skills/skills/code-version/templates/version-RESULT.md` | 10 段固定区段(里程碑/需求清单/任务清单/缺陷清单/...),各技能按职责写入 |
| 触发/来源枚举 | `plugins/code-skills/CLAUDE.md`(13 个枚举值) | 决定 `code-it` 读 `plan/` 还是 `review/` 上游 |
| 需求模板 | `skills/code-require/templates/requirements.md` | 所有"需求类"产物的统一格式 |
| 评审清单 | `skills/code-review/checklists/review-checklist.md` | `code-review` 的强制校验项 |
| 编码风格约束 | `skills/code-it/guidelines/coding-style.md` | `code-it` 实施任务时强制遵守 |

## 已知问题/技术债

- **缺少自动化校验**:`SKILL.md` 的 YAML frontmatter(`name` + `description` 必填)目前靠人工目视检查,无 schema 校验脚本
- **版本号靠人工同步**:`marketplace.json` 与 `plugin.json` 的 `version` 字段需手动保持一致,易遗漏
- **无版本变更日志(CHANGELOG)**:发版历史只能从 git log 反推
- **`CLAUDE.md` 中"如何编写技能"是软约束**:目前没有 hook/lint 阻止不符合约定的 `SKILL.md` 被提交
- **中英文 README 重复维护**:`README.md` 与 `README.en.md` 内容结构对仗,改一边容易漏另一边
- **`assistants/` 工作空间约定**写在 `CLAUDE.md` 中,但没有显式的"创建助手项目骨架"的脚本(`code-init` 本身实现了一部分但只覆盖 `assistants/` 子树)

## 现有功能需求清单

> 详细的"现有功能"需求见 `./assistants/V0.0.0/require/EXISTING-NNN/RESULT.md`。
> 本节只列索引。

| 需求编码 | 标题 | 关键路径 | 需求文档 |
| --- | --- | --- | --- |
| EXISTING-001 | 工程初始化(`code-init`):把已有/新建项目纳入 `code-*` 体系,创建基线版本 | `plugins/code-skills/skills/code-init/` | [RESULT.md](require/EXISTING-001/RESULT.md) |
| EXISTING-002 | 版本管理(`code-version`):切换/创建版本工作空间,作为所有主流程技能的前置门 | `plugins/code-skills/skills/code-version/` | [RESULT.md](require/EXISTING-002/RESULT.md) |
| EXISTING-003 | 编码规范管理(`code-rule`):维护 `assistants/rules/` 项目级共享规范 | `plugins/code-skills/skills/code-rule/` | [RESULT.md](require/EXISTING-003/RESULT.md) |
| EXISTING-004 | 需求分析(`code-require`):版本感知的需求澄清与提示词文档生成 | `plugins/code-skills/skills/code-require/` | [RESULT.md](require/EXISTING-004/RESULT.md) |
| EXISTING-005 | 概要设计(`code-design`):版本感知的概要设计,基于需求+规范产出架构方案 | `plugins/code-skills/skills/code-design/` | [RESULT.md](require/EXISTING-005/RESULT.md) |
| EXISTING-006 | 详细设计与任务计划(`code-plan`):双路径,接收 `REQ-YYYY-NNNN` 或 `BUG-NNN` | `plugins/code-skills/skills/code-plan/` | [RESULT.md](require/EXISTING-006/RESULT.md) |
| EXISTING-007 | 开发编码(`code-it`):双路径,按 PLAN.md 单任务执行,或实施缺陷修复 | `plugins/code-skills/skills/code-it/` | [RESULT.md](require/EXISTING-007/RESULT.md) |
| EXISTING-008 | 单元测试(`code-unit`):补齐/编写任务的单元测试,推进测试状态 | `plugins/code-skills/skills/code-unit/` | [RESULT.md](require/EXISTING-008/RESULT.md) |
| EXISTING-009 | 缺陷登记与跟踪(`code-fix`):支线入口,登记 bug 并跟踪其状态机 | `plugins/code-skills/skills/code-fix/` | [RESULT.md](require/EXISTING-009/RESULT.md) |
| EXISTING-010 | 代码评审(`code-review`):整需求评审,派生"审查改修"任务回流到 `code-it` | `plugins/code-skills/skills/code-review/` | [RESULT.md](require/EXISTING-010/RESULT.md) |

## 报告元信息

| 字段 | 值 |
| --- | --- |
| 生成工具 | `code-init` |
| 生成时间 | 2026-06-03 18:10 |
| 适用版本 | `V0.0.0` |
| 覆盖的源文件数 | 10(每个技能 1 个 `SKILL.md`)+ 2(README/CLAUDE)+ 2(清单 JSON)= 14 |
| 现有功能数 | 10(对应 10 个 `code-*` 技能) |
| 项目类型 | Claude Code 技能(marketplace 插件) |
| 总体规模 | 10 个技能 × 平均约 416 行 `SKILL.md` = 约 4160 行 Markdown 文档 |
