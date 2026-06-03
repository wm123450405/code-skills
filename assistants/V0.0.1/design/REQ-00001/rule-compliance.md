# 规范遵循记录 — REQ-00001
更新时间:2026-06-03 20:25
版本:V0.0.1

## 1. 本次参考的规范文件

| 规范文件 | 关联强度 | 适用条款 |
| --- | --- | --- |
| `./assistants/rules/marketplace-protocol.md` | 强 | §规则 1(协议字段约束) |
| `./assistants/rules/doc-conventions.md` | 强 | §规则 1(README 中英同次提交);§规则 2(命令反映实际状态) |
| `./assistants/rules/dashboard-conventions.md` | 弱(不触发) | §规则 1(本需求不改看板字段约定) |
| `./assistants/rules/module-conventions.md` | 弱(不触发) | §规则 1(本需求不改技能资源) |
| `./assistants/rules/skill-conventions.md` | 弱(不触发) | §规则 1(本需求不改 SKILL.md) |

## 2. 规范 vs 现状偏离

**无偏离**。本仓库所有现有结构均符合规范(本仓库本身就是按规范构建的基线),本需求在规范框架内执行。

## 3. 规范 vs 需求冲突

**无冲突**。本需求的 7 条 FR 全部在规范允许的范围内:
- FR-1(改 marketplace.json 根 name):`marketplace-protocol.md §规则 1.2` 允许(`name` 仍为 kebab-case)
- FR-2(不修改其它项):`marketplace-protocol.md §规则 1.3` 要求保持(plugin 标识不变)
- FR-3/FR-4(同步 README):`doc-conventions.md §规则 1` 要求(中英同次提交)
- FR-5(CLAUDE.md Grep):`doc-conventions.md §规则 2` 要求(命令与实际一致)
- FR-6(全仓库 Grep):本仓库无 lint 工具,纯靠人工 + AI 遵守
- FR-7(不改 SKILL.md / 模板 / 规范):`skill-conventions.md` / `module-conventions.md` 间接保障

## 4. 用户授权的偏离

**无**。本设计无任何对规范的偏离。

## 5. 规范触发的工作流约束(本设计采纳清单)

| 规范条款 | 触发的工作流约束 | 本设计的实现 |
| --- | --- | --- |
| `marketplace-protocol.md §规则 1.1`(`$schema` 必填) | 改根 name 时不可误删 `$schema` 字段 | `code-it` 阶段 Edit 前 Read 全文,锁定仅改 1 行 |
| `marketplace-protocol.md §规则 1.2`(name kebab-case) | 改后仍为 kebab-case | `code-skills-marketplace` ✅ |
| `marketplace-protocol.md §规则 1.3`(plugin 同步) | plugin `name` 与 `version` 保持 | FR-2 显式禁止修改 |
| `marketplace-protocol.md §规则 1.4`(`source` 以 `./` 开头) | 保持 | 不改 |
| `marketplace-protocol.md §规则 1.5`(`skills` 相对路径数组) | 保持 | 不改 |
| `marketplace-protocol.md §规则 1.6`(不引入未知字段) | 不增字段 | Edit 工具仅改值,不动结构 |
| `doc-conventions.md §规则 1`(README 中英同次提交) | 1 个 commit 内同步 | `design-notes.md` §Q-4 选定 B |
| `doc-conventions.md §规则 2`(命令反映实际状态) | README 命令必须可用 | 本需求的目标就是让命令反映新 name |

## 6. 待澄清项的处理(本设计采用默认值的依据)

REQU 文档中 Q-3 / Q-4 / Q-5 三项未答复,本设计采用默认值。详细记录见 `clarifications.md`。这些默认值的选择**未触发**任何规范违反:

| Q | 默认值 | 规范层面是否合规 |
| --- | --- | --- |
| Q-3(marketplace.json `description` 是否改) | 不改(沿用现状) | ✅ 符合 `marketplace-protocol.md §规则 1.6`(不引入未知字段;description 字段已存在) |
| Q-4(README 是否加迁移指引) | 不加 | ✅ 符合 `doc-conventions.md §规则 1`(不增加就无需同步);`§规则 2` 仍满足(命令反映实际) |
| Q-5(marketplace.json `version` 是否升 1.1.0) | 保持 1.0.0 | ✅ 符合 `marketplace-protocol.md §规则 1.3`(plugin 同步约束,本仓库 plugin 仍是 1.0.0) |

## 7. 规范变更响应(本设计为首次,无历史)

N/A(首次设计,无既有规范变更需要响应)
