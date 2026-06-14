# 材料登记 — REQ-00027
更新时间:2026-06-08 15:30
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能元信息 | SKILL.md frontmatter 必含 `name` + `description`,`name` 与目录名一致 |
| doc-conventions.md | 文档编写 | README 多语言对仗;主语言 README 必须含完整小节 |
| encoding-conventions.md | 编码格式 | REQ/BUG/TASK 3 类编码权威源;生成端 5 位纯数字 |
| module-conventions.md | 模块 | 技能目录结构约定 |
| marketplace-protocol.md | 市场协议 | marketplace.json + plugin.json 路径/关键词/description 一致性 |
| commit-conventions.md | 版本控制 | commit 格式 / 分支策略 / PR / merge |
| coding-style.md | 代码风格 | 编码风格 |
| directory-conventions.md | 目录 | 目录约定 |
| framework-conventions.md | 框架 | 框架约定 |
| dashboard-conventions.md | 看板 | 看板 3 区段解析锚点 |
| dependency-conventions.md | 依赖 | 依赖管理 |
| naming-conventions.md | 命名 | 命名约定(占位) |
| migration-mapping.md | 迁移映射 | 新旧编码追溯表(占位) |

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00027/RESULT.md
- 版本:V0.0.3(2026-06-08 15:20)
- 提取的 FR / NFR / AC 数量:4 FR / 4 NFR / 4 类 AC(共 12 条 AC)
- 关键交叉点:
  - FR-1 → §2.2 状态机收敛 / §2.4 决策 1
  - FR-2 → §2.3 模式 C 状态机 / §2.4 决策 2 / 3
  - FR-3 → §2.2 状态机收敛
  - FR-4 → §2.4 决策 4(自动选推荐项)

## 项目现状(本次扫描)
### 项目类型
- Claude Code 技能库 / Markdown 文档 / 0 代码
- 已重命名:`code-review` → `code-check`(REQ-00022,目录已建,SKILL.md 改名未完成 100% 覆盖)
- 现有 BUG:BUG-00001(修复编码中) / BUG-00002(已修复-待验证) / BUG-00003(修复编码中)

### 目录结构(相关)
- `plugins/code-skills/skills/code-fix/SKILL.md` ← 本轮修改 1
- `plugins/code-skills/skills/code-auto/SKILL.md` ← 本轮修改 2
- `plugins/code-skills/skills/code-plan/SKILL.md` ← 复用(不动)
- `plugins/code-skills/skills/code-it/SKILL.md` ← 复用
- `plugins/code-skills/skills/code-unit/SKILL.md` ← 复用
- `plugins/code-skills/skills/code-check/SKILL.md` ← 复用(已改名)

### 已有模块
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| code-fix | 缺陷登记与跟踪 | 是(本轮重写为纯登记型) |
| code-plan | 详细设计 + 编码计划 | 是(沿用缺陷分支) |
| code-it | 开发编码 | 是(沿用缺陷分支) |
| code-unit | 单元测试 | 是(沿用缺陷分支) |
| code-check | 代码评审 | 是(本仓库 V0.0.3 已重命名) |
| code-auto | 自动开发编排 | 是(本轮增加模式 C) |

### 已有接口
- BUG 路径输入:BUG-NNN 字符串
- BUG 路径输出:`fix/<BUG-NNN>/` 目录下 5-7 份文档(RESULT.md / fix-plan.md / fix-work-log.md / fix-test-results.md / deviations.md / auto-report.md)
- 状态推进:8 态(报告/调查中/修复规划中/修复编码中/已修复-待验证/已修复-已验证/已关闭-*/已取消/阻塞)

### 已有数据模型
- 缺陷元信息:BUG-NNN / 严重度 / 报告人 / 报告时间 / 状态 / 当前负责人 / 修复时间 / 修复人 / 修复提交
- 变更记录:时间 + 类型 + 摘要 + 关联项

### 已有第三方依赖
- 无

### 编码与构建约定
- commit 沿用 `chore(code-XXX):` 前缀
- SKILL.md frontmatter `name` 与目录名一致
- 0 改 frontmatter / 0 改 marketplace.json / 0 改 4 个 README / 0 改 CLAUDE.md(本仓库既有约定)
