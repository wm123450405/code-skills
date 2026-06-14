# 材料登记 — REQ-00026
更新时间:2026-06-08 12:30
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能元信息 | SKILL.md frontmatter 必含 `name` + `description`,`name` 与目录名一致 |
| doc-conventions.md | 文档编写 | README 中英版本结构对仗;主语言 README 必须含完整小节 |
| encoding-conventions.md | 编码格式 | REQ/BUG/TASK 三类编码权威源;5 位纯数字(生成端);宽松正则(接收端) |
| commit-conventions.md | 版本控制 | 占位(待填充) |
| naming-conventions.md | 命名 | 占位(待填充) |
| module-conventions.md | 模块 | 技能目录结构约定 |
| directory-conventions.md | 目录 | 目录约定 |
| coding-style.md | 代码风格 | 编码风格 |
| dependency-conventions.md | 依赖 | 依赖管理 |
| dashboard-conventions.md | 看板 | 看板 3 区段解析锚点 |
| marketplace-protocol.md | 市场协议 | marketplace.json + plugin.json 路径 / 关键词 / description 一致性 |
| framework-conventions.md | 框架 | 框架约定 |
| migration-mapping.md | 迁移映射 | 新旧编码追溯表 |

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00026/RESULT.md
- 版本:V0.0.3(2026-06-08 11:55)
- FR:5 / NFR:4 / AC:3 类共 12 条

## 项目现状
### 项目类型
- Claude Code 技能库 / Marketplace 协议 / 纯文档
### 目录结构
- 仓库根(本仓库):`.claude-plugin/marketplace.json` + `plugins/code-skills/`
- 插件根:`.claude-plugin/plugin.json` + `CLAUDE.md` + `README*.md` + `skills/`
- skills/ 下共 14 个 `code-*` 目录(本需求目标 10 个)
### 已有模块
- 14 个 SKILL.md(本需求目标 10 个,本需求范围外:`code-version` / `code-dashboard` / `code-auto` / `code-merge`)
- 13 个 `templates/*.md`(本需求目标 4 个,本需求范围外:9 个)
### 编码与构建约定
- 本仓库**不**包含任何源代码、构建系统、测试框架、Lint 工具或包管理配置(`CLAUDE.md` 显式)
