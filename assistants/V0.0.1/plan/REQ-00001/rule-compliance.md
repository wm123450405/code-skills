# 规范遵循记录 — REQ-00001(code-plan 阶段)
更新时间:2026-06-03 20:30
版本:V0.0.1

## 1. 本次参考的规范文件

| 规范文件 | 关联强度 | 适用条款 |
| --- | --- | --- |
| `./assistants/rules/marketplace-protocol.md` | **强** | §规则 1(协议字段约束) |
| `./assistants/rules/doc-conventions.md` | **强** | §规则 1(README 中英同次提交);§规则 2(命令反映实际状态) |
| `./assistants/rules/dashboard-conventions.md` | 弱(不触发) | §规则 1(本需求不改看板字段约定) |
| `./assistants/rules/module-conventions.md` | 弱(不触发) | §规则 1(本需求不改技能资源) |
| `./assistants/rules/skill-conventions.md` | 弱(不触发) | §规则 1(本需求不改 SKILL.md) |

## 2. 规范 vs 现状偏离

**无偏离**。本仓库所有现有结构均符合规范(本仓库本身就是按规范构建的基线),本需求在规范框架内执行。

## 3. 规范 vs 需求冲突

**无冲突**。本需求的 7 条 FR 全部在规范允许的范围内,继承 `code-design` 阶段 `rule-compliance.md` 的全部结论。

## 4. 用户授权的偏离

**无**。本计划无任何对规范的偏离。

## 5. 规范触发的关键工作流约束(本计划采纳清单)

| 规范条款 | 触发的工作流约束 | 本计划的实现 |
| --- | --- | --- |
| `marketplace-protocol.md §规则 1.1`(`$schema` 必填) | Edit 不可误删 `$schema` | T-001 Edit 锁定仅改 1 行,前 Read 全文 |
| `marketplace-protocol.md §规则 1.2`(`name` kebab-case) | 改后仍为 kebab-case | `code-skills-marketplace` ✅ |
| `marketplace-protocol.md §规则 1.3`(plugin 同步) | plugin name 与 version 保持 | T-001 显式禁止修改;`plugin.json` 严禁修改 |
| `marketplace-protocol.md §规则 1.4`(`source` 以 `./` 开头) | 保持 | 不改 |
| `marketplace-protocol.md §规则 1.5`(`skills` 相对路径数组) | 保持 | 不改 |
| `marketplace-protocol.md §规则 1.6`(不引入未知字段) | 不增字段 | Edit 工具仅改值,不动结构 |
| `doc-conventions.md §规则 1`(README 中英同次提交) | 1 个 commit 内同步 | T-002 同时改 2 文件;`design-notes.md` §D-4 选定单 commit |
| `doc-conventions.md §规则 2`(命令反映实际状态) | README 命令必须可用 | T-002 替换为新 install 命令 |

## 6. 待澄清项的处理(本计划采用概要设计默认值)

继承概要设计 `clarifications.md` 的 3 项 Q 决策(Q-3 / Q-4 / Q-5,均采用 REQU 文档默认,无规范违反)。详见本计划 `clarifications.md`。

## 7. 规范变更响应(本计划无新增响应)

继承概要设计 `rule-compliance.md §7`,N/A(无新增规范变化)。
