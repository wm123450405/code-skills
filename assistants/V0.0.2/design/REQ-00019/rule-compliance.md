# 规范遵循记录 — REQ-00019
更新时间:2026-06-06 15:00
版本:V0.0.2

## 1. 本次参考的规范文件
- `./assistants/rules/skill-conventions.md`
- `./assistants/rules/module-conventions.md`
- `./assistants/rules/dashboard-conventions.md`
- `./assistants/rules/encoding-conventions.md`
- `./assistants/rules/dependency-conventions.md`
- `./assistants/rules/marketplace-protocol.md`
- `./assistants/rules/commit-conventions.md`
- `./assistants/rules/doc-conventions.md`
- `./assistants/rules/naming-conventions.md`
- `./assistants/rules/directory-conventions.md`
- `./assistants/rules/coding-style.md`
- `./assistants/rules/framework-conventions.md`
- `./assistants/rules/migration-mapping.md`

## 2. 规范 vs 现状偏离
- 无(本需求 0 现状偏离)

## 3. 规范 vs 需求冲突
- 无(本需求 0 规范冲突;详 `require/REQ-00019/clarifications.md` 7 轮 Q-locked)

## 4. 用户授权的偏离
- 无

## 5. 规范变更响应(增量更新时填写)
- 暂无(本设计是首批)

## 6. 自检结论

| 规范 | 自检 | 影响章节 | 备注 |
| --- | --- | --- | --- |
| `skill-conventions §规则 1` | ✅ | §7 / §8 | `code-plan/SKILL.md` + `code-it/SKILL.md` frontmatter `name` 字段**字节级保留**;L5 description 段可改(本需求改 `code-it` L5) |
| `module-conventions §规则 1` | ✅ | §7 / §10 | SKILL.md 在技能根目录;`templates/` 子目录只放模板;**不**新增资源文件;`templates/fix-plan.md` 留作历史不删 |
| `dashboard-conventions §规则 1` | ✅ | §2.5.2 / §9 | 0 触发:不新增/删除/重命名区段;不新增/删除/重命名表格列;不新增枚举值(沿用既有 6 类型 + 13 触发/来源);不改字段语义 |
| `encoding-conventions §规则 1/3` | ✅ | §9 / §6 | 5+5 位嵌套式沿用;`TASK-BUG-NNNNN-NNNNN` 与 `TASK-REQ-NNNNN-NNNNN` 风格一致 |
| `dependency-conventions` | ✅ | §10 | 0 新增依赖 |
| `marketplace-protocol` | ✅ | §2.5.2 | 0 改 `marketplace.json` / `plugin.json` |
| `commit-conventions` | ✅ | §16(变更记录) | 沿用 `chore(<scope>): <subject>` |
| `doc-conventions` | ✅ | §2.5.2 | 0 改中英 README |
| `naming-conventions` | ✅ | §9 | 0 新增文件名前缀规则;`TASK-BUG-` 沿用 `TASK-` 已有规则 |
| `directory-conventions` | ✅ | §9 | 过程文档摆放在 `fix/<BUG-NNN>/` 根目录(沿用既有目录约定) |
| `coding-style` | ✅ | §7 / §16 | 沿用既有 SKILL.md 风格;2 处锚点替换 + 1 处 frontmatter 修订 |
| `framework-conventions` | — | — | 不涉及(本需求纯文档重构) |
| `migration-mapping` | — | — | 不涉及(本需求纯文档重构) |

**总览**:13 份规范全部严守;0 冲突 0 偏离 0 授权。
