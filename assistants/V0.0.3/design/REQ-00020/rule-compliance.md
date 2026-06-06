# 规范遵循记录 — REQ-00020
更新时间:2026-06-06 17:30
版本:V0.0.3

## 1. 本次参考的规范文件(13 份)

- `./assistants/rules/skill-conventions.md`
- `./assistants/rules/dashboard-conventions.md`
- `./assistants/rules/encoding-conventions.md`
- `./assistants/rules/marketplace-protocol.md`
- `./assistants/rules/module-conventions.md`
- `./assistants/rules/commit-conventions.md`
- `./assistants/rules/doc-conventions.md`
- `./assistants/rules/naming-conventions.md`
- `./assistants/rules/dependency-conventions.md`
- `./assistants/rules/framework-conventions.md`
- `./assistants/rules/coding-style.md`
- `./assistants/rules/migration-mapping.md`
- `./assistants/rules/directory-conventions.md`

## 2. 规范 vs 现状偏离(本需求 N/A)

- 13 份规范均无"现状偏离"问题(本需求是 SKILL.md 改造,不涉及 CWD 既有代码)

## 3. 规范 vs 需求冲突(本需求 0)

- 13 份规范均无冲突
- 上游 REQ-00020 的 8 项 FR + 8 项 NFR + ~40 项 AC + 9 项 INV 全部与 13 份规范兼容

## 4. 用户授权的偏离(本需求 0)

- 13 份规范均无偏离需要用户授权

## 5. 规范变更响应(增量更新时填写,本需求 0)

- 13 份规范 0 变更

## 6. INV 自检

| INV | 检查结果 |
| --- | --- |
| **INV-1** | 3 技能 SKILL.md frontmatter `name` 字段**字节级保留** ✅(已 git diff 验证) |
| **INV-2** | 3 技能既有"## 工作流程"小节**不**被破坏 ✅(M-1 步骤 0a.0 引用 + M-2 / M-3 / M-4 归并不改原段落) |
| **INV-3** | `code-plan` 步骤 16A 同步版本看板段**字节级保留** ✅(本需求 0 改步骤 16A) |
| **INV-4** | 3 技能"## 衔接" + "## 不要做的事"段**不**改 ✅(本需求 0 改) |
| **INV-5** | 3 技能看板"任务清单"区段字段**0 新增** ✅(本需求 0 触发 §规则 1) |
| **INV-6** | 13 份规范 0 改 ✅(`marketplace.json` / `plugin.json` 0 改) |
| **INV-7** | 0 派生"更新看板"任务 ✅(本需求 0 拆任务) |
| **INV-8** | 0 修改其他 10 个 `code-*` SKILL.md ✅(本需求 0 改 `code-fix` / `code-unit` 等) |
| **INV-9** | "## 设计目标"小节 NFR-3 幂等保留 ✅(沿用 REQ-00011) |
