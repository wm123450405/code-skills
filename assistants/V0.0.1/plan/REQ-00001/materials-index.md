# 材料登记 — REQ-00001
更新时间:2026-06-03 20:30
版本:V0.0.1

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `dashboard-conventions.md` | 看板/版本工作空间 | §规则 1:看板字段约定扩展需三处同步;本需求不触发 |
| `doc-conventions.md` | 文档编写 | §规则 1:README 中英版本必须结构对仗,**同次提交**同步;§规则 2:README 中命令/路径必须反映仓库实际状态 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`$schema`/`name`/`version` 必填;`plugins[].name` 必须与 `plugin.json` name 同步;`name` 改后仍为 kebab-case |
| `module-conventions.md` | 技能资源摆放 | §规则 1:技能资源放 `templates/` / `checklists/` / `guidelines/` 子目录;本需求不创建/修改资源 |
| `skill-conventions.md` | 技能元信息 | §规则 1:SKILL.md frontmatter 必含 `name` + `description`;本需求不触发 |

> 规范层面对本需求的强约束:**doc-conventions.md §规则 1**(README 中英同次提交)+ **marketplace-protocol.md §规则 1**(协议字段约束)。

## 上游需求
- 来源:`./assistants/V0.0.1/require/REQ-00001/RESULT.md`
- 版本:v2(2026-06-03 20:20)
- 提取的 FR / NFR / AC 数量:7 FR / 7 NFR / 9 AC
- 待澄清:3 项(Q-3 / Q-4 / Q-5,均非阻塞,本设计采用 REQU 文档默认值)

## 上游概要设计
- 来源:`./assistants/V0.0.1/design/REQ-00001/RESULT.md`
- 版本:v1(2026-06-03 20:25)
- 7 个过程文档已就绪(`clarifications` / `design-notes` / `module-breakdown` / `dependencies` / `related-designs` / `rule-compliance` / `materials-index`)
- 4 文件变更集(1 JSON + 2 README + 1 CLAUDE?)
- 11 条关键不变量

## 项目现状(实现细节)
- **语言/框架**:N/A(本仓库是 Claude Code 技能定义集合,无应用代码)
- **构建系统**:N/A
- **测试框架**:N/A
- **依赖管理**:N/A
- **命名约定**:kebab-case 文件名与目录名
- **关键工具**:Claude Code 内置工具集(Edit / Write / Grep / Read)
- **既有相似功能实现风格**:N/A(无应用代码)
- **既有测试用例**:N/A
- **可复用工具函数**:N/A

## 本次变更源(增量更新时)
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | (无变化,v2 已锁定 FR) | — |
| 概要设计侧 | (无变化,v1 已锁定 4 文件集) | — |
| 规范侧 | (无变化) | — |
| 代码侧 | `Grep "code-skills@code-skills"` 全仓库 → 4 处命中(2 README + 2 V0.0.1 工作空间文档) | 与设计预期一致 |
