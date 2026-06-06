# 材料登记 — REQ-00019
更新时间:2026-06-06 14:30
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | SKILL 编写 | frontmatter 字节级保留;`name` 字段不可改 |
| `./assistants/rules/module-conventions.md` | 模块摆放 | SKILL.md 在技能根目录;`templates/` 子目录只放模板 |
| `./assistants/rules/dashboard-conventions.md` | 看板规范 | §规则 1 三同步(模板 + CLAUDE.md + 规范自身) |
| `./assistants/rules/encoding-conventions.md` | 任务编号 | 5+5 位嵌套式 `TASK-REQ-NNNNN-NNNNN` |
| `./assistants/rules/dependency-conventions.md` | 依赖 | 0 新增依赖强约束 |
| `./assistants/rules/marketplace-protocol.md` | 协议 | 0 改 `marketplace.json` / `plugin.json` |
| `./assistants/rules/commit-conventions.md` | 提交消息 | `chore(<scope>): <subject>` |
| `./assistants/rules/doc-conventions.md` | 文档 | 中英 README 同次提交 + 章节对仗 |
| `./assistants/rules/naming-conventions.md` | 命名 | kebab-case + 沿用既有前缀 |
| `./assistants/rules/directory-conventions.md` | 目录 | 过程文档摆放规则 |
| `./assistants/rules/coding-style.md` | 编码风格 | 沿用既有 SKILL.md 风格 |
| `./assistants/rules/framework-conventions.md` | 框架 | 不涉及(本需求纯文档重构) |
| `./assistants/rules/migration-mapping.md` | 迁移 | 不涉及(本需求纯文档重构) |

## 上游需求
- 来源:无(本需求是元技能自身优化,无用户上游需求材料)
- 用户原始输入:`优化技能 /code-plan,在修复缺陷模式下的产出物与正常模式下的保持一致。区别只有参考来源,需求模式下来源需求和概设;缺陷模式下来源于登记的缺陷。`

## 上游概要设计
- 来源:无(本需求是元技能自身优化,无 design 阶段)

## 项目现状(实现细节)
- `code-plan/SKILL.md` 第 588-735 行"缺陷分支"明确产出单文件 `fix-plan.md`;`code-it/SKILL.md` 第 638-800 行 BUG 路径硬编码消费 `fix-plan.md`
- 既有 12 份过程文档已在 REQ 路径使用;`templates/plan.md` + `templates/task-plan.md` + `templates/fix-plan.md` 3 份模板均存在
- BUG-00001 已有 `fix-plan.md`(624 行)+ 5 份 `fix-` 前缀过程文档;本需求不迁移
- 版本看板 `assistants/V0.0.2/RESULT.md` "任务清单" 区段现有 45 个 REQ 任务行(沿用既有);本需求**新增** BUG 任务行

## 本次变更源(增量更新时)
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 无(本需求是元技能自身) | — |
| 概要设计 | 无 | — |
| 规范侧 | `./assistants/rules/` 13 份 0 冲突 | — |
| 代码侧 | `code-plan/SKILL.md` 步骤 19-28A + `code-it/SKILL.md` 步骤 17-25 全部需要联动改造 | 2 个 SKILL.md 修改 |
