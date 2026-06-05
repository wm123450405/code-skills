# 规范遵循记录 — REQ-00014

更新时间:2026-06-05 13:40
版本:V0.0.2
需求:REQ-00014(优化技能 `/code-plan` 的任务拆分维度)

## 1. 本次参考的规范文件(13 个)

`./assistants/rules/` 下**全部 13 个**规范文件均已读取并归类(详见 `materials-index.md` §项目级规范):

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

| 规范 | 条款 | 本设计满足度 | 验证方式 |
| --- | --- | --- | --- |
| `skill-conventions.md §规则 1` | SKILL.md frontmatter 含 `name`+`description`,`name` 与目录名 kebab-case 严格一致 | ✅ 100% | 本需求**不**改 frontmatter(只改 §10A 工作流文字) |
| `module-conventions.md §规则 1` | 资源须放 `templates/` / `checklists/` / `guidelines/` 固定子目录;`SKILL.md` 本身在根 | ✅ 100% | `code-plan/SKILL.md` 已在根目录,本需求**不**新增资源 |
| `dashboard-conventions.md §规则 1` | 字段约定扩展需 `templates/version-RESULT.md` + `CLAUDE.md` + 本规范三方同步 | ✅ **不触发** | 本需求**不**改看板字段(任务编号/双状态/触发来源沿用既有) |
| `doc-conventions.md §规则 1` | README 多语言版本必须保持结构对仗 | ✅ 不触达 | 本需求**不**改 README |
| `marketplace-protocol.md §规则 1` | `$schema` / `name` / `version` 必填,`source` 必须 `./` 开头,`skills` 必须是 `./` 开头的相对路径数组 | ✅ 不触达 | 本需求**不**改 marketplace.json |
| `encoding-conventions.md §规则 1-4` | REQ/BUG `^REQ-\d{5}$` / `^BUG-\d{5}$`;TASK 嵌套式 `^TASK-(REQ\|BUG)-\d{5}-\d{5}$`;§规则 4 实施流程 | ✅ 100% | 任务编号格式**不**修改(沿用既有) |
| `migration-mapping.md §规则 1-4` | 已落地映射;EXISTING-NNN 不追溯 | ✅ **不触达** | 本需求**不**触达历史编码 |

## 3. 占位规范 — 不触发

| 规范 | 占位状态 | 本设计处理 |
| --- | --- | --- |
| `directory-conventions.md §规则 1` | 占位 | 本需求**不**新增任何技能资源,无内容可放 |
| `coding-style.md §规则 1` | 占位 | 本需求不写代码,无适用 |
| `commit-conventions.md §规则 1` | 占位 | NFR-1 显式零新增依赖,无适用 |
| `dependency-conventions.md §规则 1` | 占位 | NFR-1 显式零新增依赖,无适用 |
| `framework-conventions.md §规则 1` | 占位 | 本需求不涉及框架选型 |
| `naming-conventions.md §规则 1` | 占位 | 本需求不涉及命名风格决策 |

## 4. DEPRECATED 规范 — 仍沿用

| 规范 | 状态 | 本设计处理 |
| --- | --- | --- |
| `module-conventions.md` | ⚠️ DEPRECATED | 本需求**不**新增任何资源,满足"无子目录" |

## 5. 规范 vs 现状偏离

**无任何现状偏离**。本设计:
- 修改 1 个 `code-plan` SKILL.md 的 §10A 共 4 行文字
- **不修改**任何其他 18 个章节
- **不修改**任何 `.claude-plugin/marketplace.json` / `README.md` / 看板 / 既有 PLAN
- **不修改**任何 `./assistants/rules/` 下规范文件

| 规范条款 | 项目现状 | 规范要求 | 偏离? |
| --- | --- | --- | --- |
| `skill-conventions §规则 1` | 12 个 `code-*` 技能 SKILL.md frontmatter 全部合规 | 沿用 | ❌ 无偏离 |
| `module-conventions §规则 1` | `code-plan/` 无子目录 | 沿用 | ❌ 无偏离(本需求**不**触发) |
| `dashboard-conventions §规则 1` | 看板字段定义已落地 | 沿用 | ❌ 无偏离(本需求**不**改字段) |
| `encoding-conventions §规则 1-4` | 任务编号格式已落地 | 沿用 | ❌ 无偏离(本需求**不**改格式) |

## 6. 规范 vs 需求冲突

**无任何冲突**。本设计继承上游需求(REQ-00014 require/RESULT.md)的全部约束。

| 需求条款 | 规范条款 | 冲突? | 处理 |
| --- | --- | --- | --- |
| FR-1 按功能点拆分 | 全部 7 强约束 | ❌ | 显式合规 |
| FR-2 架构任务作为首个 | 全部 7 强约束 | ❌ | 显式合规 |
| FR-3 仅未来生效 | 全部 7 强约束 | ❌ | 显式合规 |
| FR-4 不破坏其他 12 个技能 | 全部 7 强约束 | ❌ | 显式合规 |
| NFR-1 零新增依赖 | `dependency-conventions §规则 1`(占位) | ❌ | 显式合规 |
| NFR-2 SKILL.md 修改 ≤ 50 行 | (无强约束) | ❌ | 显式合规(+20 行净增) |
| NFR-3 不触发三同步 | `dashboard-conventions §规则 1` | ❌ | 显式合规(本需求**不**改字段) |
| NFR-4 不触发联动 | 全部 7 强约束 | ❌ | 显式合规 |
| NFR-5 不追踪既有 PLANS | (无强约束) | ❌ | 显式合规(Q-A3 锁定 A) |
| NFR-6 未来需求立即生效 | (无强约束) | ❌ | 显式合规 |

## 7. 用户授权的偏离

**无**。本设计 100% 合规。

## 8. 待澄清的规范冲突

**无**。

## 9. 规范变更响应(增量更新时填写)

> 本节为增量更新阶段的占位;首次详细设计时无需填写。

- 规范文件:N/A
- 变更:N/A
- 时间:N/A
- 对 RESULT.md 的影响:N/A
- 处理动作:N/A
