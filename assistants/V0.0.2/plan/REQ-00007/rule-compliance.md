# 规范遵循记录 — REQ-00007(详细设计阶段)

更新时间:2026-06-05 10:20
版本:V0.0.2

## 1. 本次参考的规范文件(13 个)

`./assistants/rules/` 下**全部 13 个**规范文件均已读取并归类(详见 `materials-index.md §项目级规范`):

| # | 规范文件 | 类别 | 状态 |
| --- | --- | --- | --- |
| 1 | `skill-conventions.md` | 技能编写 | **强约束** |
| 2 | `module-conventions.md` | 模块规划 | **强约束**(DEPRECATED 但沿用) |
| 3 | `dashboard-conventions.md` | 看板与版本工作空间 | **强约束** |
| 4 | `doc-conventions.md` | 文档编写 | **强约束** |
| 5 | `marketplace-protocol.md` | Marketplace 协议 | **强约束** |
| 6 | `encoding-conventions.md` | 编码格式 | **强约束** |
| 7 | `migration-mapping.md` | 编码迁移 | **强约束** |
| 8 | `directory-conventions.md` | 目录与模块 | 占位 |
| 9 | `coding-style.md` | 代码风格 | 占位 |
| 10 | `commit-conventions.md` | 提交与合并 | 占位 |
| 11 | `dependency-conventions.md` | 三方依赖 | 占位 |
| 12 | `framework-conventions.md` | 框架选型 | 占位 |
| 13 | `naming-conventions.md` | 命名风格 | 占位 |

## 2. 强约束规范 — 完全合规

| 规范 | 条款 | 本详细设计满足度 | 验证方式 |
| --- | --- | --- | --- |
| `skill-conventions.md §规则 1` | SKILL.md frontmatter 含 `name`+`description`,`name` 与目录名 kebab-case 一致;**不**改 frontmatter | ✅ 100% 合规 | T-001 显式定义 frontmatter schema(`module-details.md §6.2`)+ T-005 字节级校验 |
| `module-conventions.md §规则 1` | 资源须放 `templates/` / `checklists/` / `guidelines/` 固定子目录;`SKILL.md` 本身在根 | ✅ 100% 合规 | `code-auto/` **无**子目录(`module-details.md §模块 M-1`)+ T-005 自检 |
| `dashboard-conventions.md §规则 1` | 字段约定扩展需 `templates/version-RESULT.md` + `CLAUDE.md` + 本规范三同步 | ✅ 不触发 | 本设计**不**扩展看板字段,只在 4 区段**追加行**(`data-changes.md §5`)+ T-004 一次性同步 |
| `doc-conventions.md §规则 1` | README 中英同次提交 + 结构对仗 | ✅ 触发(同次提交) | T-003 严格按"`Add 1 行 + 2 文件同次 commit`"执行,中英 H2/列/行数对仗 |
| `doc-conventions.md §规则 2` | README 必须存在并持续维护 | ✅ 不触发 | 本设计**不**修改 README 主体,仅追加 1 行 |
| `marketplace-protocol.md §规则 1` | `$schema` / `name` / `version` 必填;`source` 必须 `./` 开头;`skills` 必须是 `./` 开头的相对路径数组;不引入未知字段 | ✅ 触发(由 T-002) | T-002 严格按"末尾追加 1 项 `./skills/code-auto`"执行 + T-005 JSON Schema 校验 |
| `encoding-conventions.md §规则 1-4` | REQ/BUG `^REQ-\d{5}$` / `^BUG-\d{5}$`;TASK 嵌套式 `^TASK-(REQ\|BUG)-\d{5}-\d{5}$`;§规则 4 实施流程 | ✅ 部分触发 | T-001 显式定义任务编码双格式正则(本设计**不**产生新编码,仅消费) |
| `migration-mapping.md §规则 1-4` | 已落地/理论/通用公式/EXISTING-NNN 不追溯 | ✅ 不触发 | 本设计**不**触达历史编码;V0.0.0 EXISTING-NNN 保持原样 |

## 3. 占位规范 — 不触发

| 规范 | 占位状态 | 本详细设计处理 |
| --- | --- | --- |
| `directory-conventions.md §规则 1` | 占位 | 本设计**不**新增任何技能资源,无内容可放 |
| `coding-style.md §规则 1` | 占位 | 本设计不写代码,无适用 |
| `commit-conventions.md §规则 1` | 占位 | NFR-3 显式不直接填充规则;`code-auto` 自身不 commit;子技能按各自规则 commit |
| `dependency-conventions.md §规则 1` | 占位 | NFR-1 零新增依赖,无适用 |
| `framework-conventions.md §规则 1` | 占位 | 本设计不涉及框架选型 |
| `naming-conventions.md §规则 1` | 占位 | 本设计不涉及命名风格决策 |

## 4. DEPRECATED 规范 — 仍沿用

| 规范 | 状态 | 本设计处理 |
| --- | --- | --- |
| `module-conventions.md` | ⚠️ DEPRECATED(2026-06-04),内容已迁 `directory-conventions.md` | 本设计 `module-details.md §模块 M-1` + `T-005 自检` 显式记录"`code-auto/` 无子目录"满足 §规则 1(规则 1 仍引用) |

## 5. 规范 vs 现状偏离

**无任何现状偏离**。本详细设计:
- T-001 新建 1 个 `SKILL.md`,frontmatter 严格遵循 `skill-conventions §规则 1`
- T-001 显式约束"不修改其他 11 个子技能 SKILL.md"(FR-8.AC-8.1)
- T-002 修改 1 个 `marketplace.json`,仅追加 1 项(不修改其他字段)
- T-003 修改 2 个 README,各追加 1 行(不修改其他行)
- T-004 修改 1 个 `V0.0.2/RESULT.md`,在 4 区段追加行(责任划分内的常规追加)
- T-005 静态自检 8 项不变量

| 规范条款 | 项目现状 | 规范要求 | 偏离? |
| --- | --- | --- | --- |
| `skill-conventions §规则 1` | 11 个子技能全部 frontmatter 合规 | 新建技能需同样合规 | ❌ 无偏离 |
| `module-conventions §规则 1` | 7 个子技能用 `templates/`,2 个用 `checklists/`,1 个用 `guidelines/`,4 个无子目录 | 资源放固定子目录 | ❌ 无偏离(本设计无资源) |
| `marketplace-protocol §规则 1` | marketplace.json / plugin.json 合规 | 字段不引入未知 | ❌ 无偏离(本设计仅追加 1 项) |
| `dashboard-conventions §规则 1` | 看板扩展已三同步 | 字段扩展需三同步 | ❌ 无偏离(本设计不扩展字段) |
| `doc-conventions §规则 1` | 2 个 README 结构对仗 | 中英同次提交 | ❌ 无偏离(本设计同次提交追加 1 行) |
| `encoding-conventions §规则 1-4` | V0.0.1 REQ-00002 已落地 | 5 位纯数字 + 嵌套式 5+5 位 | ❌ 无偏离(本设计不产生新编码) |

## 6. 规范 vs 需求 / 设计冲突

**无任何冲突**。本详细设计继承概要设计 + 上游需求,无新增冲突。

| 需求条款 | 规范条款 | 冲突? | 处理 |
| --- | --- | --- | --- |
| NFR-1 零新增依赖 | `dependency-conventions §规则 1`(占位) | ❌ | 显式合规 |
| NFR-3 `code-auto` 不 commit | `commit-conventions §规则 1`(占位) | ❌ | 显式不沉淀规则 |
| NFR-4 不引入批量模式 | `module-conventions §规则 1` | ❌ | 子技能零修改 |
| FR-6 选推荐项 | 无相关规范 | ❌ | 子技能零修改(约束自身 SKILL.md 写法) |
| FR-8 子技能零修改 | `skill-conventions §规则 1` | ❌ | 强约束 |

## 7. 用户授权的偏离

**无**。本详细设计 100% 合规。

## 8. 待澄清的规范冲突

**无**。

## 9. 规范变更响应(增量更新时填写)

> 本节为增量更新阶段的占位;首次详细设计时无需填写。

- 规范文件:N/A
- 变更:N/A
- 时间:N/A
- 对 RESULT.md 的影响:N/A
- 处理动作:N/A
