# 规范遵循记录 — REQ-00007

更新时间:2026-06-05 09:35
版本:V0.0.2

## 1. 本次参考的规范文件(13 个,均已读)

`./assistants/rules/` 下**全部 13 个**规范文件均已读取并归类(详见 `materials-index.md` §"项目级规范"):

| # | 规范文件 | 类别 | 状态 |
| --- | --- | --- | --- |
| 1 | `skill-conventions.md` | 技能编写 | **强约束**(本设计触发 — 新建 1 个技能) |
| 2 | `dashboard-conventions.md` | 看板与模板 | **强约束**(本设计触发 — 追加"概要设计清单"行 + "变更记录"行) |
| 3 | `doc-conventions.md` | 文档编写 | **强约束**(本设计触发 — 中英 README 同次提交追加 1 行) |
| 4 | `marketplace-protocol.md` | Marketplace 协议 | **强约束**(本设计部分触发 — `code-it` 任务需更新 `plugins[].skills`) |
| 5 | `encoding-conventions.md` | 编码格式 | **强约束**(本设计触发 — 解析任务编码时遵循) |
| 6 | `migration-mapping.md` | 编码迁移 | **强约束**(不触发 — 不触达历史编码) |
| 7 | `module-conventions.md` | 模块规划 | ⚠️ DEPRECATED(已迁 `directory-conventions.md`);§规则 1 仍引用 |
| 8 | `directory-conventions.md` | 目录与模块 | 占位(本设计不触发) |
| 9 | `coding-style.md` | 代码风格 | 占位(本设计不触发) |
| 10 | `commit-conventions.md` | 提交与合并 | 占位(NFR-3 显式不直接填充) |
| 11 | `dependency-conventions.md` | 三方依赖 | 占位(NFR-1 显式零新增依赖) |
| 12 | `framework-conventions.md` | 框架选型 | 占位(本设计不涉及) |
| 13 | `naming-conventions.md` | 命名风格 | 占位(本设计不涉及) |

## 2. 规范自检结论

### 2.1 强约束规范 — 完全合规

| 规范 | 条款 | 本设计满足度 | 验证方式 |
| --- | --- | --- | --- |
| `skill-conventions.md §规则 1` | SKILL.md frontmatter 含 `name`+`description`,`name` 与目录名 kebab-case 严格一致 | ✅ 100% 合规 | `code-auto/SKILL.md` frontmatter 显式 `name: code-auto` + 完整 description(见 `module-breakdown.md §2.2`) |
| `module-conventions.md §规则 1`(DEPRECATED 但沿用) | 资源须放 `templates/` / `checklists/` / `guidelines/` 固定子目录 | ✅ 100% 合规 | `code-auto/` **无**任何子目录(无模板/清单/规则资源) — 见 `module-breakdown.md §4` |
| `dashboard-conventions.md §规则 1` | 字段约定扩展需 `templates/version-RESULT.md` + `CLAUDE.md` + 本规范三方同步 | ✅ 不触发 | 本设计**不**扩展看板字段;只在现有"概要设计清单"区段追加 1 行 + "变更记录"区段追加 1 行(责任划分内的常规追加) |
| `doc-conventions.md §规则 1` | README 中英同次提交 + 结构对仗 | ✅ 触发(同次提交) | `plugins/code-skills/README.md` + `README.en.md` "主要能力"段同次追加 1 行 `code-auto`(由 `code-it` 任务 T-1 执行;不在 `code-design` 阶段写) |
| `doc-conventions.md §规则 2` | README 必须存在并持续维护 | ✅ 不触发 | 本设计**不**修改 README 主体,仅追加 1 行 |
| `marketplace-protocol.md §规则 1` | `$schema` / `name` / `version` 必填;`source` 必须 `./` 开头;`skills` 必须是 `./` 开头的相对路径数组;不引入未知字段 | ✅ 触发(由 `code-it` 任务) | `code-design` 阶段**不**修改 `marketplace.json` / `plugin.json`;由 `code-it` 任务 T-N 在落地时按规范同次提交追加 `./skills/code-auto` 到 `plugins[].skills` 数组 |
| `encoding-conventions.md §规则 1-4` | REQ/BUG 5 位纯数字;TASK 嵌套式 5+5 位;新编码实施流程 | ✅ 部分触发 | 本设计**不**产生新编码,仅在 §2.5 任务编码解析时遵循新格式正则 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` + 旧格式正则 `^(REQ|BUG)-\d{5}-\d{5}$` 透传 |
| `migration-mapping.md §规则 1-4` | 已落地/理论/通用公式/EXISTING-NNN 不追溯 | ✅ 不触发 | 本设计不触达历史编码;`auto-report.md` 报告内容中的 `REQ-NNNNN` 引用严格 5 位纯数字 |

### 2.2 占位规范 — 不触发

| 规范 | 占位状态 | 本设计处理 |
| --- | --- | --- |
| `directory-conventions.md §规则 1` | 占位 | 本设计**不**新增任何技能资源(模板/清单/指南),无内容可放 |
| `coding-style.md §规则 1` | 占位 | 本设计不写代码,无适用 |
| `commit-conventions.md §规则 1` | 占位 | NFR-3 显式不直接填充规则(`code-auto` 自身不 commit);`code-it` 子技能内部 commit 沿用 V0.0.1 实践 |
| `dependency-conventions.md §规则 1` | 占位 | NFR-1 零新增依赖,无适用 |
| `framework-conventions.md §规则 1` | 占位 | 本设计不涉及框架选型 |
| `naming-conventions.md §规则 1` | 占位 | 本设计不涉及命名风格决策 |

### 2.3 DEPRECATED 规范 — 不触达

| 规范 | 状态 | 本设计处理 |
| --- | --- | --- |
| `module-conventions.md` | ⚠️ DEPRECATED(2026-06-04),内容已迁 `directory-conventions.md` | 本设计 §module-breakdown §4 显式记录"`code-auto/` 无子目录"满足 §规则 1(规则 1 仍引用) |

## 3. 规范 vs 现状偏离

**无任何现状偏离**。本设计新建 1 个 `SKILL.md` 的 frontmatter 严格遵循 `skill-conventions.md §规则 1`;`code-auto/` 目录无子目录,符合 `module-conventions.md §规则 1`;不修改其他 9 个子技能 SKILL.md / 协议清单 / 现有 README 主体;不触达 V0.0.0 基线(`migration-mapping.md §规则 4`)。

| 规范条款 | 项目现状 | 规范要求 | 偏离? |
| --- | --- | --- | --- |
| `skill-conventions §规则 1` | 11 个子技能全部 frontmatter 合规 | 新建技能需同样合规 | ❌ 无偏离 |
| `module-conventions §规则 1` | 7 个子技能用 `templates/`,2 个用 `checklists/`,1 个用 `guidelines/`,4 个无子目录 | 资源放固定子目录 | ❌ 无偏离(本设计无资源) |
| `marketplace-protocol §规则 1` | marketplace.json / plugin.json 合规 | 字段不引入未知 | ❌ 无偏离(本设计不修改) |
| `dashboard-conventions §规则 1` | 看板扩展已三同步 | 字段扩展需三同步 | ❌ 无偏离(本设计不扩展字段) |
| `doc-conventions §规则 1` | 2 个 README 结构对仗 | 中英同次提交 | ❌ 无偏离(本设计同次提交追加 1 行) |
| `encoding-conventions §规则 1-4` | V0.0.1 REQ-00002 已落地 | 5 位纯数字 + 嵌套式 5+5 位 | ❌ 无偏离(本设计不产生新编码) |

## 4. 规范 vs 需求冲突

**无任何规范 vs 需求冲突**。REQ-00007 NFR-1/3/4/8/9 与既有规范均无冲突;Q-1 ~ Q-12 全部锁定或采纳默认;Q-13 派生任务预警属"建议"不阻塞。

| 需求条款 | 规范条款 | 冲突? | 处理 |
| --- | --- | --- | --- |
| NFR-1 零新增依赖 | `dependency-conventions §规则 1`(占位) | ❌ | 显式合规 |
| NFR-2 串行而非并发 | 无相关规范 | ❌ | 强约束 |
| NFR-3 不自动 commit | `commit-conventions §规则 1`(占位) | ❌ | 显式不沉淀规则 |
| NFR-4 不引入批量模式 | `module-conventions §规则 1` | ❌ | 子技能零修改 |
| FR-6 选推荐项 | 无相关规范 | ❌ | 子技能零修改(约束自身 SKILL.md 写法) |
| FR-8.AC-8.1 子技能零修改 | `skill-conventions §规则 1` | ❌ | 强约束 |

## 5. 用户授权的偏离

**无**。本设计 100% 合规。

## 6. 规范变更响应(增量更新时填写)

> 本节为增量更新阶段的占位;首次设计时无需填写。

- 规范文件:N/A
- 变更:N/A
- 时间:N/A
- 对 RESULT.md 的影响:N/A
- 处理动作:N/A
