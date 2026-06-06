# 材料登记 — REQ-00019
更新时间:2026-06-06 15:30
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | SKILL 编写 | frontmatter `name` 字段字节级保留;L5 description 段可改 |
| `./assistants/rules/module-conventions.md` | 模块摆放 | SKILL.md 在技能根目录;`templates/` 子目录只放模板 |
| `./assistants/rules/dashboard-conventions.md` | 看板规范 | §规则 1:新增/删除/重命名区段/列/枚举值/字段语义需三同步 |
| `./assistants/rules/encoding-conventions.md` | 任务编号 | 5+5 位嵌套式 `TASK-REQ-NNNNN-NNNNN`;`TASK-BUG-NNNNN-NNNNN` 沿用 |
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
- 来源:./assistants/V0.0.2/require/REQ-00019/RESULT.md (v1)
- 提取的 FR / NFR / AC 数量:8 FR / 11 NFR / ~30 AC / 11 INV
- 关键交叉点:
  - FR-1 / FR-2 / FR-3 → §4 模块 1(`code-plan` 步骤 19-28A+1)
  - FR-4 / FR-5 / FR-6 / FR-7 → §4 模块 2(`code-it` 步骤 17-25)
  - FR-8 → §3 非目标(0 修改 `code-fix`)

## 上游概要设计
- 来源:./assistants/V0.0.2/design/REQ-00019/RESULT.md (v1)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - 模块拆分:2 个核心模块(`code-plan` + `code-it`)+ 3 复用模板(`templates/plan.md` / `templates/task-plan.md` / `templates/fix-plan.md`)
  - 接口概要:1 个新增(步骤 28A+1)+ 2 个修改(步骤 17 / frontmatter L5)
  - 数据结构:1 个新增实体(`TASK-BUG-NNNNN-NNNNN`)+ 1 个修改实体(看板"任务清单"区段行字段扩展填法)
  - 关键决策:5 项 D-1~D-5 全部锁定(整体设计目标 `--minimal`)

## 项目现状(实现细节)
- `code-plan/SKILL.md` L588-735 现有 9 步骤(19/20/21/22/23/24A/25A/26A/27A/28A/29),既有"关键简化"列表 4 条(沿用既有),frontmatter 1-7 行
- `code-it/SKILL.md` L638-800 现有 9 步骤(17/18/19/20/21/22/23/24/25),既有"关键简化"列表 3 条(沿用既有),frontmatter 1-7 行
- `templates/plan.md` 14 章节(详细设计模板,BUG 路径复用)
- `templates/task-plan.md` 8 章节(任务计划模板,BUG 路径复用)
- `templates/fix-plan.md` 10 章节(旧 BUG 路径模板,留作历史,不再被引用)
- 命名风格:沿用既有 kebab-case + 大写前缀(`TASK-` / `BUG-`)
- 错误处理:沿用既有"屏显 + 退出码 ≠ 0"模式
- 日志格式:沿用既有"⚠ / ✓ / ✗" + 中点 `·` 标题格式(REQ-00013)
- 既有过程文档清单:`fix/<BUG-NNN>/fix-plan.md` + 5 份 `fix-` 前缀过程文档(本需求后不再使用)

## 本次变更源(增量更新时)
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | `./assistants/V0.0.2/require/REQ-00019/RESULT.md` 变更记录 | 0(本详细设计是首批) |
| 概要设计 | `./assistants/V0.0.2/design/REQ-00019/RESULT.md` 变更记录 | 0(本详细设计是首批) |
| 规范侧 | `./assistants/rules/` 13 份 0 冲突 | 0 |
| 代码侧 | 重读 `code-plan/SKILL.md` L588-735 + `code-it/SKILL.md` L638-800 | 0(本详细设计是首批) |
