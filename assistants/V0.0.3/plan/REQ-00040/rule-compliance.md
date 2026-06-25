# 规范遵循记录 — REQ-00040

更新时间:2026-06-25
版本:V0.0.3

## 1. 本次参考的规范文件

13 份项目级规范(`./assistants/rules/`),全部沿用,**不**新增任何规范文件:

1. `coding-style.md`
2. `commit-conventions.md`
3. `dashboard-conventions.md`
4. `dependency-conventions.md`
5. `directory-conventions.md`
6. `doc-conventions.md`
7. `encoding-conventions.md`
8. `framework-conventions.md`
9. `marketplace-protocol.md`
10. `migration-mapping.md`
11. `module-conventions.md`(已 DEPRECATED,沿用历史)
12. `naming-conventions.md`
13. `skill-conventions.md`

## 2. 规范 vs 现状偏离

**0 项偏离**。本需求的所有设计均符合 13 份项目级规范。

| 规范条款 | 现状 | 本设计是否偏离 |
| --- | --- | --- |
| `dashboard-conventions §规则 1`(看板字段扩展三同步) | 当前看板 7 列 | **不偏离** — 本设计**不**新增看板列(产物放 `fix/<BUG-NNN>/reproduce/` 子目录,**不**进总览 / 看板) |
| `skill-conventions §规则 1`(SKILL.md frontmatter) | `code-fix/SKILL.md` frontmatter 已含 | **不偏离** — 本设计**不**改 frontmatter(L1-3 字节级保留) |
| `skill-conventions §规则 2`(不得含开发痕迹) | `code-fix/SKILL.md` 与 `bug.md` 当前**不**含 | **不偏离** — 本设计**不**在产物 SKILL.md / 模板中写"本需求 REQ-00040 新增" 等字面 |
| `encoding-conventions §规则 1-4`(3 类编码格式) | 既有 5 位纯数字 | **不偏离** — 本设计**不**新增编码格式;沿用 `BUG-NNNNN` 5 位纯数字 |
| `module-conventions §规则 1`(资源放 `templates/` / `checklists/` / `guidelines/`) | `code-fix` 既有 `templates/` 子目录 | **不偏离** — 本设计仅修改 `templates/bug.md` 与 `templates/assistants-layout.md`,**不**新增子目录 |
| `directory-conventions`(目录与模块规范) | §规则 1 占位;既有 `code-fix/templates/` 布局 | **不偏离** — 本设计**不**新增项目级目录,`reproduce/` 是运行时子目录 |

## 3. 规范 vs 需求冲突

**0 项冲突**。本需求的所有设计均与 13 份项目级规范兼容,**不**触发任何冲突。

## 4. 用户授权的偏离

**0 项偏离**。本需求严守 13 份项目级规范,**不**存在"用户授权的偏离"。

## 5. 规范变更响应(增量更新时填写)

本轮为**首次设计**,无规范变更。

## 6. 13 份规范自检结论(详设 vs 概设 同构)

| 规范 | 触发? | 结论 |
| --- | --- | --- |
| `skill-conventions §规则 1` | ✅ 强 | `code-fix/SKILL.md` frontmatter(L1-3)字节级保留 — INV 严守 |
| `skill-conventions §规则 2` | ✅ 强 | 本设计**不**在 SKILL.md / 模板中写"本需求 REQ-00040 新增" 等开发痕迹字面 |
| `module-conventions §规则 1` | ⚠️ 软(DEPRECATED) | 本设计**不**新增 `code-fix` 子目录;`reproduce/` 是运行时子目录 |
| `directory-conventions` | ⚠️ 软(规则 1 占位) | 本设计**不**新增项目级目录 |
| `dashboard-conventions §规则 1` | ❌ 0 触发 | 本设计**不**新增看板列 |
| `encoding-conventions §规则 1-4` | ❌ 0 触发 | 本设计**不**新增编码格式 |
| `coding-style.md` | ❌ 0 触发 | SKILL.md 是自然语言,无代码风格约束 |
| `commit-conventions.md` | ⚠️ 软(规则 1 占位) | 沿用既有 `chore(code-it):` / `chore(code-design):` / `chore(code-plan):` 前缀 |
| `dependency-conventions.md` | ❌ 0 触发 | 本设计**0 新增三方依赖** |
| `framework-conventions.md` | ❌ 0 触发 | 本设计**不**涉及项目架构 |
| `naming-conventions.md` | ⚠️ 软(规则 1 占位) | `reproduce/` 命名遵循"小写 + 复数"风格 |
| `doc-conventions.md` | ❌ 0 触发 | 本设计**不**涉及 README |
| `marketplace-protocol.md` | ❌ 0 触发 | 本设计**不**涉及插件清单 |
| `migration-mapping.md` | ❌ 0 触发 | 本设计**不**涉及编码迁移 |

**自检结论**:0 违反强约束,0 触发 `dashboard-conventions §规则 1` 三同步,0 新增 `code-rule` 介入。

## 7. 与上游规范对比(详设沿用概设结论)

本详设严格沿用 `design/REQ-00040/rule-compliance.md §6` 的自检结论(13 份规范全部 0 触发冲突 / 0 触发三同步),无新增。
