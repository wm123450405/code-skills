# 规范遵循记录 — REQ-00005(plan 阶段)

更新时间:2026-06-04 16:30
版本:V0.0.2

> 本文件是 `code-plan` 阶段的规范遵循记录。**完全继承** `code-design` 阶段的 `rule-compliance.md`,本阶段**无新增**违反 / 偏离 / 冲突。

---

## 1. 本次参考的规范文件(13 个,与 design 阶段一致)

`./assistants/rules/` 下**全部 13 个**规范文件均已读取并归类(详见 `materials-index.md §项目级规范`):

| # | 规范文件 | 类别 | 状态 |
| --- | --- | --- | --- |
| 1 | `skill-conventions.md` | 技能编写 | 强约束 |
| 2 | `dashboard-conventions.md` | 看板与模板 | 强约束(本计划不触发) |
| 3 | `doc-conventions.md` | 文档编写 | 强约束(本计划不触发) |
| 4 | `marketplace-protocol.md` | Marketplace 协议 | 强约束(本计划不触发) |
| 5 | `encoding-conventions.md` | 编码格式 | **强约束**(本计划强约束用于分配任务编号) |
| 6 | `migration-mapping.md` | 编码迁移 | 强约束(本计划不触发) |
| 7 | `module-conventions.md` | 模块规划 | ⚠️ DEPRECATED(不触发) |
| 8 | `directory-conventions.md` | 目录结构 | 占位(不触发) |
| 9 | `coding-style.md` | 代码风格 | 占位(不触发) |
| 10 | `commit-conventions.md` | 提交与合并 | 占位(NFR-6 显式不直接填充);本计划沿用 V0.0.1 实践 |
| 11 | `dependency-conventions.md` | 三方依赖 | 占位(不触发) |
| 12 | `framework-conventions.md` | 框架选型 | 占位(不触发) |
| 13 | `naming-conventions.md` | 命名风格 | 占位(不触发) |

## 2. 规范自检结论(继承 + plan 阶段增量)

### 2.1 强约束规范 — 完全合规(继承 design 阶段)

| 规范 | 条款 | 本计划满足度 | plan 阶段增量 |
| --- | --- | --- | --- |
| `skill-conventions.md §规则 1` | SKILL.md frontmatter 字节级保留 | ✅ 100% 合规 | `module-details.md §1.1 / §2.1 / §3.1` 显式列出 frontmatter 原文,严守 |
| `dashboard-conventions.md §规则 1` | 看板字段约定扩展需三同步 | ✅ 不触发 | 本计划步骤 16A 同步仅在现有"详细设计与任务计划汇总" / "任务清单" / "里程碑" / "变更记录" 区段追加,**不**扩展新字段 |
| `doc-conventions.md §规则 1` | README 中英同次提交 | ✅ 不触发 | 本计划**不**写 README(FR-6.AC-6.3 + Q-11 留 follow-up) |
| `marketplace-protocol.md §规则 1` | `$schema` / `name` / `version` 必填;不引入未知字段 | ✅ 不触发 | T-001 ~ T-003 严禁修改 `marketplace.json` / `plugin.json` |
| `encoding-conventions.md §规则 1 + 3` | REQ/BUG 5 位纯数字;TASK 嵌套式 5+5 位 | ✅ 100% 合规 | **本计划强约束**:`module-details.md §4.3` + `data-changes.md §4` 显式列出 `TASK-REQ-00005-00001 ~ 00004` 5+5 位格式,严格遵循 |
| `migration-mapping.md §规则 1-4` | 已落地/理论/通用公式/EXISTING-NNN 不追溯 | ✅ 不触发 | 本计划任务编号严格 5+5 位(不混用 V0.0.1 旧 3 位格式) |

### 2.2 占位规范 — 不触发(继承 design 阶段)

| 规范 | 占位状态 | 本计划处理 |
| --- | --- | --- |
| `directory-conventions.md` | §规则 1 占位 | 本计划**不**新增任何技能资源,无内容可放 |
| `coding-style.md` | §规则 1 占位 | 本计划不写代码,无适用 |
| `commit-conventions.md` | §规则 1 占位 | NFR-6 显式不直接填充规则;commit message 沿用 V0.0.1 实践 `chore(<scope>): <subject>` |
| `dependency-conventions.md` | §规则 1 占位 | NFR-1 零新增依赖,无适用 |
| `framework-conventions.md` | §规则 1 占位 | 本计划不涉及框架选型 |
| `naming-conventions.md` | §规则 1 占位 | 本计划不涉及命名风格决策 |

### 2.3 DEPRECATED 规范 — 不触达(继承 design 阶段)

| 规范 | 状态 | 本计划处理 |
| --- | --- | --- |
| `module-conventions.md` | ⚠️ DEPRECATED | 本计划不新增任何技能资源,不触发 |

## 3. 规范 vs 现状偏离(继承 design 阶段)

**无任何现状偏离**。

| 规范条款 | 项目现状 | 规范要求 | 偏离? |
| --- | --- | --- | --- |
| `skill-conventions.md §规则 1` | 10 个 SKILL.md frontmatter 完整 | frontmatter 含 `name`+`description` | 无偏离 |
| `marketplace-protocol.md §规则 1.3` | `marketplace.json.plugins[0].version` = `plugin.json.version` = `1.0.0` | 两边 `version` 同步 | 无偏离 |
| `doc-conventions.md §规则 1` | `README.md` 与 `README.en.md` 章节对仗 | 中英结构对仗 + 同步 | 无偏离 |
| `dashboard-conventions.md §规则 1` | V0.0.2/RESULT.md 字段约定与 `templates/version-RESULT.md` + `CLAUDE.md` 一致 | 三方同步 | 无偏离(本计划不扩展字段) |

## 4. 规范 vs 需求冲突(继承 design 阶段)

**无冲突**。13 个规范文件中,**无任何一条**与本计划"末尾 commit 模板"或"步骤 0a/0b 工作流"或"任务编号 5+5 位"直接冲突。

## 5. 用户授权的偏离(继承 design 阶段)

**无任何偏离**。本计划 100% 合规。

## 6. 规范变更响应(增量更新时填写)

> 本节为预留,本次为首次 plan,无历史规范变更需要响应。
> 完整历史规范变更时间线见 `design/.../rule-compliance.md §6`。

### 6.1 plan 阶段 vs design 阶段的规范视角差异

| 维度 | design 阶段 | plan 阶段 |
| --- | --- | --- |
| 关注点 | 架构决策 / 模块拆分 / 接口契约 | 实现细节 / 任务拆分 / 数据结构 / 风险分析 |
| 新增的规范引用 | 全部 13 个规范文件 | 重点强化 `encoding-conventions.md`(任务编号)+ `skill-conventions.md`(frontmatter 字节级) |
| 规范 vs 现状偏离 | 0 | 0(继承) |
| 规范 vs 需求冲突 | 0 | 0(继承) |
| 用户授权的偏离 | 0 | 0(继承) |

## 7. 规范自检结论汇总

| 维度 | 结论 |
| --- | --- |
| 强约束规范遵循度 | 100%(6/6 完全合规或不触发) |
| 占位规范触发数 | 0 |
| 规范 vs 现状偏离 | 0 |
| 规范 vs 需求冲突 | 0 |
| 用户授权的偏离 | 0 |
| 规范变更触发的设计/计划修订 | 0(本次为首次 plan) |

**总评**:**本计划 100% 合规**,完全继承 design 阶段规范遵循记录,无需任何授权偏离或冲突解决。
