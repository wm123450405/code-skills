# 材料登记 — REQ-00036

更新时间:2026-06-16 17:33
版本:V0.0.3

## 项目级规范
13 个规范文件,核心相关:

| 规范文件 | 类别 | 关键约束 |
| --- | --- | --- |
| `./assistants/rules/skill-conventions.md` §规则 1 | SKILL.md 元信息 | frontmatter 必含 `name` + `description` |
| `./assistants/rules/skill-conventions.md` §规则 2 | SKILL.md + templates/ 内容 | **不得包含 6 类开发痕迹**;4 类白名单例外(本设计的目标规范) |
| `./assistants/rules/encoding-conventions.md` §规则 1-4 | 编码格式 | REQ/BUG/TASK 命名;5 位纯数字;接收端宽松正则 |
| `./assistants/rules/dashboard-conventions.md` §规则 1 | 看板 | 字段扩展三方同步(本设计 0 触发) |
| `./assistants/rules/module-conventions.md` §规则 1 | 模块规划 | 资源放 `templates/` / `checklists/` / `guidelines/`(本设计只清 `templates/`) |

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00036/RESULT.md (v1)
- FR:FR-1 ~ FR-6(6 类清理) / FR-7(不动 checklists/guidelines) / FR-8(不动 assistants/)
- NFR:NFR-1 ~ NFR-10
- AC:AC-1 ~ AC-8

## 上游概要设计
- 来源:./assistants/V0.0.3/design/REQ-00036/RESULT.md (v1)
- 整体 = `--minimal`,功能性 = 中
- 6 条清理规则 R-1 ~ R-6
- 9 条硬约束 C-1 ~ C-9
- 6 项风险 R-1 ~ R-6
- 0 新增 / 0 调用外部接口

## 项目现状(实现细节)
- 仓库类型:Claude Code 插件市场仓库(纯 Markdown)
- 文件清单(本设计相关):
  - `plugins/code-skills/skills/<name>/SKILL.md` × 14
  - `plugins/code-skills/skills/<name>/templates/*.md` × 23
  - 合计 37 个目标文件
- 编码风格:Markdown + frontmatter + 章节编号 + 表格
- 无单测载体(纯文档)

## 本次变更源
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | (无 — 首次详细设计) | — |
| 概要设计侧 | (无 — 首次详细设计) | — |
| 规范侧 | Grep `./assistants/rules/` | 1 项变化:`skill-conventions.md §规则 2` 由 `code-rule` 阶段添加(本需求前) |
| 代码侧 | (无 — 详细设计阶段不探索代码细节) | — |
