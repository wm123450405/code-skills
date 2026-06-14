# 材料登记 — REQ-00026
更新时间:2026-06-08 12:45
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能元信息 | SKILL.md frontmatter 必含 `name` + `description`,`name` 与目录名一致 |
| doc-conventions.md | 文档编写 | README 中英对仗;主语言 README 必须含完整小节 |
| encoding-conventions.md | 编码格式 | REQ/BUG/TASK 3 类编码权威源;生成端 5 位纯数字;接收端宽松正则 |
| module-conventions.md | 模块 | 技能目录结构约定 |
| marketplace-protocol.md | 市场协议 | marketplace.json + plugin.json 路径/关键词/description 一致性 |
| dependency-conventions.md | 依赖 | 不新增依赖 |
| coding-style.md | 代码风格 | 编码风格 |
| commit-conventions.md | 版本控制 | commit 格式 / 分支策略 / PR / merge |
| naming-conventions.md | 命名 | 命名约定 |
| directory-conventions.md | 目录 | 目录约定 |
| framework-conventions.md | 框架 | 框架约定 |
| dashboard-conventions.md | 看板 | 看板 3 区段解析锚点 |
| migration-mapping.md | 迁移映射 | 新旧编码追溯表 |

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00026/RESULT.md (v1,2026-06-08 11:55)
- FR:5 / NFR:4 / AC:3 类共 12 条
- 关键交叉点:
  - FR-1 → 10 SKILL.md 描述段去专属化
  - FR-2 → 10 SKILL.md 描述段指代泛化
  - FR-3 → ./assistants/ 路径保持原样
  - FR-4 → 3 templates + 1 INIT-REPORT 字面替换
  - FR-5 → code-rule/SKILL.md L336/363/370 CLAUDE.md 字面替换

## 上游概要设计
- 来源:./assistants/V0.0.3/design/REQ-00026/RESULT.md (v1,2026-06-08 12:30)
- 模块拆分:13 个目标文件
- 关键决策:占位符 `<本仓库>` + 每个被改 SKILL.md 概述段显式声明
- 9 条 INV

## 项目现状(实现细节)
- 项目类型:Claude Code 技能库(Markdown 文档,无源代码)
- 命名风格:全小写 kebab-case(目录名) + PascalCase(章节标题)
- 既有功能实现风格:10 个 SKILL.md 各自有 H1 标题 + YAML frontmatter + 章节结构(适用场景 / 工具使用约定 / 工作流步骤 / 过程文档格式 / 衔接 / 不要做的事)
- 既有"工具引用"惯例:各 SKILL.md 中以 `Bash:` / `Read:` / `Write:` / `Edit:` / `Glob:` / `Grep:` / `Skill:` 形式标注工具调用
- **本仓库不写代码**:无 package.json / 测试框架 / 构建工具
- 可复用工具函数/中间件:**N/A**

## 关键交叉点(FR ↔ 概要设计 ↔ 本详细设计)
| FR | 上游设计章节 | 本详细设计章节 |
| --- | --- | --- |
| FR-1 | §2 架构方案 / §3 组件拆分 | module-details.md §1-10 |
| FR-2 | 同上 | module-details.md §11(各 SKILL.md "本项目"指代扫描) |
| FR-3 | §3 INV-8 | data-changes.md(无变更,0 diff) |
| FR-4 | §3 module-breakdown L21-25 | module-details.md §11-14 |
| FR-5 | §3 module-breakdown L19 | module-details.md §10 |
