# 规范遵循 — BUG-00004

更新时间:2026-06-22 20:30
版本:V0.0.3

## 适用的规范文件

- `./assistants/rules/skill-conventions.md`(SKILL.md 编写规范)
- `./assistants/rules/dashboard-conventions.md`(看板/模板扩展规范)
- `./assistants/rules/doc-conventions.md`(文档编写规范)
- `./assistants/rules/module-conventions.md`(技能资源摆放规范)
- `./assistants/rules/encoding-conventions.md`(编号格式规范)
- `./assistants/rules/naming-conventions.md`(命名规范)
- `./assistants/rules/dependency-conventions.md`(依赖规范)
- `./assistants/rules/coding-style.md`(代码风格规范)
- `./assistants/rules/commit-conventions.md`(提交规范)
- `./assistants/rules/directory-conventions.md`(目录布局规范)
- `./assistants/rules/framework-conventions.md`(框架规范)
- `./assistants/rules/marketplace-protocol.md`(marketplace 协议规范)
- `./assistants/rules/migration-mapping.md`(迁移映射规范)

## 自检结论

| 规范文件 | 条款 | 自检结论 | 备注 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 规则 1:frontmatter L1-3 字节级保留 | ✅ 完全合规 | 本需求**不**修改 `code-it/SKILL.md` frontmatter(第 1-3 行 `name: code-it` + `description: ...` 字节级保留) |
| `skill-conventions.md` | 规则 2:SKILL.md / templates/ 不含 6 类开发痕迹 | ✅ 完全合规 | 本需求**不**写"(本需求 BUG-00004 新增)" / "原 code-it 步骤 X" / "Q-N 锁定" / "YYYY-MM-DD 起生效" / 退场文件名引用 等 6 类字面;所有新增段不含"变更人:<具体自然人名>" |
| `dashboard-conventions.md` | 规则 1:看板字段扩展需 templates/version-RESULT.md + CLAUDE.md + 本规范三方同步 | ✅ 不触发 | 本需求**不**改看板字段(只改 `code-it/SKILL.md` 内部章节 + `code-it/templates/RESULT.md` 模板);`code-it/templates/RESULT.md` 是 skill 内部模板,**不**触发三方同步 |
| `doc-conventions.md` | 规则 1:README 多语言对仗 | ✅ 不触发 | 本需求**不**改 README |
| `module-conventions.md` | 规则 1:资源放 templates/ / checklists/ / guidelines/ 子目录 | ✅ 不触发 | 本需求**不**新增资源子目录 |
| `encoding-conventions.md` | 规则 1/3:BUG-NNNNN 接收端放宽 | ✅ 完全合规 | 本需求任务编号 `TASK-BUG-00004-00001` ~ `TASK-BUG-00004-00004` 严格遵循 5+5 位嵌套式 |
| `naming-conventions.md` | 规则 1:kebab-case | ✅ 完全合规 | 本需求**不**新增文件;既有 `process-doc-decisions.md` / `code-it/SKILL.md` 命名沿用 |
| `dependency-conventions.md` | 规则 1:沿用既有 tokei/cloc | ✅ 完全合规 | 本需求**不**新增依赖 |
| `coding-style.md` | 代码风格 | ✅ 不触发 | 本需求改 SKILL.md(非代码) |
| `commit-conventions.md` | 提交格式 | ✅ 完全合规 | 本需求末尾兜底 commit 沿用 `chore(code-it): BUG-00004 <title>` 格式 |
| `directory-conventions.md` | 目录布局 | ✅ 不触发 | 本需求**不**改 marketplace 协议布局 |
| `framework-conventions.md` | 框架 | ✅ 不触发 | 本需求**不**改框架代码 |
| `marketplace-protocol.md` | marketplace 协议 | ✅ 不触发 | 本需求**不**改 marketplace.json / plugin.json |
| `migration-mapping.md` | 迁移映射 | ✅ 不触发 | 本需求**不**做迁移 |

## 用户授权的偏离

无(本需求**完全合规**,0 授权偏离)。

## 待澄清的冲突

无(本需求**完全合规**,0 待澄清)。

## 总结

- **完全合规**:13 / 13 条规范
- **授权偏离**:0
- **待澄清**:0
- **总体结论**:本需求合规,可直接进入实施阶段
