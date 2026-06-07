# 规范遵循 — BUG-00001
更新时间:2026-06-07
版本:V0.0.3

> 本文档是 `code-plan BUG-00001` 阶段的辅助过程文档。核心内容已并入 `RESULT.md §7.3 规范遵循(13 份规范自检)`,本文档为索引。

## 13 份规范自检结论

| 规范 | 触发? | 结论 | 自检依据 |
| --- | --- | --- | --- |
| `skill-conventions.md §规则 1` | ✅ 强 | 通过 | SKILL.md frontmatter(`name` + `description`)字节级保留 — INV-16 静态校验 |
| `module-conventions.md` | ❌ | 不适用 | DEPRECATED,本修复不引用 |
| `directory-conventions.md` | ❌ | 不适用 | 占位待填,本修复不触发 |
| `encoding-conventions.md §规则 1-4` | ✅ 强 | 通过 | BUG 任务编号 5+5 位嵌套式 `TASK-BUG-00001-NNNNN` |
| `dashboard-conventions.md §规则 1` | ❌ | 不适用 | 0 字段扩展,0 三同步 |
| `doc-conventions.md §规则 1-2` | ❌ | 不适用 | 本修复不涉及 README |
| `coding-style.md` | ❌ | 不适用 | 占位,SKILL.md 是自然语言不涉及代码风格 |
| `commit-conventions.md` | ⚠️ 软 | 通过(沿用) | 本修复产物为 6 段 SKILL.md 文本追加,commit message 沿用 `chore(code-it): BUG-00001 ...` |
| `dependency-conventions.md` | ❌ | 不适用 | 0 新依赖 |
| `framework-conventions.md` | ❌ | 不适用 | 0 架构变更 |
| `naming-conventions.md` | ❌ | 不适用 | 0 新增命名实体 |
| `migration-mapping.md` | ❌ | 不适用 | 0 编码重命名(BUG-00001 已是新格式) |
| `marketplace-protocol.md` | ❌ | 不适用 | 0 JSON 字段变更 |

## 冲突解决记录

**0 冲突**。本修复不与任何现有规范产生冲突。

## 不需澄清冲突

本修复不修改任何规范文件;新增 `rules/skill-responsibility.md` 留作后续可能需求(本轮 Q-1 锁定"否")。

## 自检结论

- **0 违反强约束**
- **2 项软约束已通过**(frontmatter 保留 + 任务编号新格式)
- **0 需 `code-rule` 介入**
- 详 `RESULT.md §7.3 规范遵循(13 份规范自检)`
