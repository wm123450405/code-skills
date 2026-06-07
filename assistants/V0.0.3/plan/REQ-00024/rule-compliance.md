# 规范遵循 — REQ-00024
更新时间:2026-06-07
版本:V0.0.3

> 本文档是 `code-plan BUG-00001` 阶段的辅助过程文档。核心内容已并入 `plan/REQ-00024/RESULT.md §规范遵循(13 份规范自检)`,本文档为索引。

## 13 份规范自检结论

| 规范 | 触发? | 结论 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | ✅ 强 | code-auto frontmatter 字节级保留(INV 严守) |
| `module-conventions.md` | ❌ | DEPRECATED,本修复不引用 |
| `directory-conventions.md` | ❌ | 占位待填,本修复不触发 |
| `encoding-conventions.md §规则 1-4` | ❌ | 0 触发新编码生成 |
| `dashboard-conventions.md §规则 1` | ❌ | 0 字段扩展,0 三同步 |
| `doc-conventions.md §规则 1-2` | ❌ | 本修复不涉及 README |
| `coding-style.md` | ❌ | 占位,SKILL.md 是自然语言不涉及代码风格 |
| `commit-conventions.md` | ⚠️ 软 | 沿用既有 `chore(code-it):` 格式 |
| `dependency-conventions.md` | ❌ | 0 新依赖 |
| `framework-conventions.md` | ❌ | 0 架构变更 |
| `naming-conventions.md` | ❌ | 0 新增命名实体 |
| `migration-mapping.md` | ❌ | 0 编码重命名 |
| `marketplace-protocol.md` | ❌ | 0 JSON 字段变更 |

## 冲突解决记录
- **0 冲突**(本修复不与任何现有规范产生冲突)

## 不需澄清冲突
本修复不修改任何规范文件;0 触发 `code-rule`。

## 自检结论
- **0 违反强约束**
- **1 项软约束沿用既有**(commit message 格式)
- **0 需 `code-rule` 介入**
- 详 `plan/REQ-00024/RESULT.md §规范遵循(13 份规范自检)`
