# 规范遵循记录 — REQ-00005

更新时间:2026-06-04 16:00
版本:V0.0.2

## 1. 本次参考的规范文件(13 个)

`./assistants/rules/` 下**全部 13 个**规范文件均已读取并归类(见 `materials-index.md` §"项目级规范"):

| # | 规范文件 | 类别 | 状态 |
| --- | --- | --- | --- |
| 1 | `skill-conventions.md` | 技能编写 | 强约束 |
| 2 | `dashboard-conventions.md` | 看板与模板 | 强约束(本需求不触发) |
| 3 | `doc-conventions.md` | 文档编写 | 强约束(本需求不触发) |
| 4 | `marketplace-protocol.md` | Marketplace 协议 | 强约束(本需求不触发) |
| 5 | `encoding-conventions.md` | 编码格式 | 强约束(本需求不触发) |
| 6 | `migration-mapping.md` | 编码迁移 | 强约束(本需求不触发) |
| 7 | `module-conventions.md` | 模块规划 | ⚠️ DEPRECATED(已迁 `directory-conventions.md`) |
| 8 | `directory-conventions.md` | 目录结构 | 占位(本需求不触发) |
| 9 | `coding-style.md` | 代码风格 | 占位(本需求不触发) |
| 10 | `commit-conventions.md` | 提交与合并 | 占位(NFR-6 显式不直接填充) |
| 11 | `dependency-conventions.md` | 三方依赖 | 占位(本需求不触发) |
| 12 | `framework-conventions.md` | 框架选型 | 占位(本需求不触发) |
| 13 | `naming-conventions.md` | 命名风格 | 占位(本需求不触发) |

## 2. 规范自检结论

### 2.1 强约束规范 — 完全合规

| 规范 | 条款 | 本设计满足度 | 验证方式 |
| --- | --- | --- | --- |
| `skill-conventions.md` | §规则 1 — SKILL.md frontmatter 含 `name`+`description`,`name` 与目录名一致;**不**改 frontmatter | ✅ 100% 合规 | 3 个 SKILL.md frontmatter 字节级保留(本设计 §module-breakdown §2.3 / §3.3 / §4.3 强约束) |
| `dashboard-conventions.md` | §规则 1 — 看板字段约定扩展需 `templates/version-RESULT.md` + `CLAUDE.md` + 本规范三方同步 | ✅ 不触发 | 本需求**不**扩展看板字段,只追加"概要设计清单"一行 + "变更记录"一条,走现有区段(责任划分内的常规追加) |
| `doc-conventions.md` | §规则 1 — README 中英同次提交 + 同步 | ✅ 不触发 | 本需求**不**写 README(FR-6.AC-6.3 留 follow-up) |
| `marketplace-protocol.md` | §规则 1 — `$schema` / `name` / `version` 必填;`source` 必须 `./` 开头;`skills` 必须是相对路径数组;不引入未知字段 | ✅ 不触发 | FR-6.AC-6.1 显式禁止修改 `marketplace.json` / `plugin.json` |
| `encoding-conventions.md` | §规则 1 — REQ/BUG 5 位纯数字;TASK 嵌套式 5+5 位 | ✅ 不触发 | 本需求**不**生成新 REQ/BUG/TASK 编码(0 新增) |
| `migration-mapping.md` | §规则 1-4 — 已落地/理论/通用公式/EXISTING-NNN 不追溯 | ✅ 不触发 | 本需求不触达历史编码;末尾 commit message 中引用的 `REQ-00005` 严格符合 5 位纯数字 |

### 2.2 占位规范 — 不触发

| 规范 | 占位状态 | 本需求处理 |
| --- | --- | --- |
| `directory-conventions.md` | §规则 1 占位 | 本需求**不**新增任何技能资源(模板 / 清单 / 指南),无内容可放,零状态 |
| `coding-style.md` | §规则 1 占位 | 本需求不写代码,无适用 |
| `commit-conventions.md` | §规则 1 占位 | NFR-6 显式不直接填充规则;末尾 commit 沿用 V0.0.1 实践 `chore(<scope>): <subject>` |
| `dependency-conventions.md` | §规则 1 占位 | NFR-1 零新增依赖,无适用 |
| `framework-conventions.md` | §规则 1 占位 | 本需求不涉及框架选型 |
| `naming-conventions.md` | §规则 1 占位 | 本需求不涉及命名风格决策 |

### 2.3 DEPRECATED 规范 — 不触达

| 规范 | 状态 | 本需求处理 |
| --- | --- | --- |
| `module-conventions.md` | ⚠️ DEPRECATED(2026-06-04),内容已迁 `directory-conventions.md` | 本设计 §module-breakdown §7 显式记录"本需求不新增任何技能资源,不触发该规范" |

## 3. 规范 vs 现状偏离

**无任何现状偏离**。本需求修改的 3 个 SKILL.md 的 frontmatter 字节级保留;新增工作流步骤严格遵循 `skill-conventions.md §规则 1`(YAML frontmatter 不可变);不触达其他 4 个 SKILL.md / 协议清单 / README / 规范文件。

| 规范条款 | 项目现状 | 规范要求 | 偏离? |
| --- | --- | --- | --- |
| `skill-conventions.md §规则 1` | 10 个 SKILL.md frontmatter 完整 | frontmatter 含 `name`+`description` | 无偏离 |
| `marketplace-protocol.md §规则 1.3` | `marketplace.json.plugins[0].version` = `plugin.json.version` = `1.0.0` | 两边 `version` 同步 | 无偏离 |
| `doc-conventions.md §规则 1` | `README.md` 与 `README.en.md` 章节对仗 | 中英结构对仗 + 同步 | 无偏离 |
| `dashboard-conventions.md §规则 1` | V0.0.2/RESULT.md 字段约定与 `templates/version-RESULT.md` + `CLAUDE.md` 一致 | 三方同步 | 无偏离(本需求不扩展字段) |

## 4. 规范 vs 需求冲突

**无冲突**。13 个规范文件中,**无任何一条**与本需求"末尾 commit 模板"或"步骤 0a/0b 工作流"直接冲突。理由:

| 维度 | 结论 |
| --- | --- |
| `commit-conventions.md` | 占位文件,无规则约束;NFR-6 显式不直接填充 |
| `skill-conventions.md` | 仅约束 frontmatter(不可变);NFR-2 严格遵守 |
| `marketplace-protocol.md` | 仅约束协议清单;FR-6 显式禁止修改 |
| `doc-conventions.md` | 仅约束 README;本需求不写 README |
| `dashboard-conventions.md` | 仅约束字段扩展;本需求不扩展字段 |
| 其他占位规范 | 0 规则可触发冲突 |

## 5. 用户授权的偏离

**无任何偏离**。本设计 100% 合规,无需用户授权任何偏离。

## 6. 规范变更响应(增量更新时填写)

> 本节为预留,本次为首次设计,无历史规范变更需要响应。
> 若后续 `code-rule` 技能填充了 `commit-conventions.md §规则 1` 或 `directory-conventions.md §规则 1` 等占位文件,**可能**需要回退修订本设计;届时按 `code-design §步骤 7B / 8B / 9B` 增量更新。

### 6.1 历史规范变更时间线(本设计视角)
- **2026-06-04 10:45**:`coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `directory-conventions.md` / `framework-conventions.md` / `naming-conventions.md` 等 6 个占位文件创建(由 `code-it` 在 REQ-00003-002 中)
- **2026-06-04 10:08**:`migration-mapping.md` 创建(由 `code-it` 在 REQ-00002-006 中)
- **2026-06-04**:`module-conventions.md` 标记 DEPRECATED(由 `code-it` 在 REQ-00003 H2 决策)

> 上述 3 条变更**均早于**本需求 REQ-00005(2026-06-04 13:33),本设计已在 `materials-index.md §项目级规范` 反映最新状态。

### 6.2 未来可能触发的规范修订(留 follow-up)
- **`commit-conventions.md §规则 1` 填充**:由 `code-rule` 实施(派生任务);若填充,本设计 §RESULT.md §"接口与数据结构" 中"commit message 模板"小节应**升级**为引用 `commit-conventions.md` 权威源,而不是直接硬编码格式
- **`plugins/code-skills/CLAUDE.md` "AI 工作约定"小节追加**:由 `code-rule` 实施(类型 B,触发 `dashboard-conventions §规则 1` 三方同步);若追加,本设计 §RESULT.md 看板"索引"区段应新增"AI 工作约定"链接
- **`plugins/code-skills/README.md` / `README.en.md` 同步"3 个技能步骤变化"**:由 `code-rule` 实施(触发 `doc-conventions §规则 1` 中英同次提交)

> 上述 3 条**均不阻塞**本设计;**均不阻塞** `code-plan` 阶段。

## 7. 规范自检结论汇总

| 维度 | 结论 |
| --- | --- |
| 强约束规范遵循度 | 100%(6/6 完全合规或不触发) |
| 占位规范触发数 | 0(本需求不引入新规则适用对象) |
| 规范 vs 现状偏离 | 0 |
| 规范 vs 需求冲突 | 0 |
| 用户授权的偏离 | 0 |
| 规范变更触发的设计修订 | 0(本次为首次设计) |

**总评**:**本设计 100% 合规**,无需任何授权偏离或冲突解决。
