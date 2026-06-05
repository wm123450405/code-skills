# 规范遵循记录 — REQ-00016
更新时间:2026-06-05 16:10
版本:V0.0.2
需求编码:REQ-00016
设计标题:`code-design` / `code-plan` 增加"快模式"+ 末尾提交无需确认

---

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md` ✅ 强约束
- `./assistants/rules/module-conventions.md` ✅ 强约束(DEPRECATED 但仍引用 §规则 1 资源子目录)
- `./assistants/rules/dashboard-conventions.md` ✅ 强约束
- `./assistants/rules/encoding-conventions.md` ✅ 强约束(本设计**不**触发)
- `./assistants/rules/marketplace-protocol.md` ✅ 强约束(本设计**不**触发)
- `./assistants/rules/doc-conventions.md` ✅ 强约束(本设计**不**主动写 README)
- `./assistants/rules/migration-mapping.md` ✅ 强约束(本设计**不**触发)
- `./assistants/rules/framework-conventions.md` ⏸️ 占位(不触发)
- `./assistants/rules/naming-conventions.md` ⏸️ 占位(不触发)
- `./assistants/rules/coding-style.md` ⏸️ 占位(不触发)
- `./assistants/rules/commit-conventions.md` ⏸️ 占位(不触发)
- `./assistants/rules/dependency-conventions.md` ⏸️ 占位(不触发)
- `./assistants/rules/directory-conventions.md` ⏸️ 占位(不触发)

**总计**:13 个文件(7 有效 + 6 占位 + 1 DEPRECATED 仍引用 + 1 迁移不触发)

---

## 2. 规范 vs 现状偏离

**无**。本设计**严格遵循**所有有效约束:
- 既有 `code-design` / `code-plan` 技能已存在(无新增技能 → `skill-conventions §规则 1` 仅"保持 frontmatter 不变"约束,本设计**不**改 frontmatter)
- 既有资源(模板 + 清单)全部在 `templates/` / `checklists/` 固定子目录 → `module-conventions §规则 1` 不触
- 本设计**不扩展**看板字段(快模式仅追加 1 行,带"-快模式"后缀)→ `dashboard-conventions §规则 1` 3 处同步不触(状态枚举新增值**不**算字段约定扩展)
- 本设计**不**修改 `marketplace.json` / `plugin.json` / 其他 11 个 SKILL.md → `marketplace-protocol §规则 1` 不触
- 本设计**不**写 README(`code-rule` 沉淀,Q-7 采纳默认)→ `doc-conventions §规则 1-2` 不触

---

## 3. 规范 vs 需求冲突

**无冲突**。本需求是"`code-design` / `code-plan` 既有技能的优化扩展",无字段约定扩展 / 编码约定扩展 / 资源目录扩展。

---

## 4. 用户授权的偏离

**无**。本设计 100% 合规。

---

## 5. 规范变更响应(增量更新时填写)

> 本次为首次概要设计(v1),无规范变更触发。后续增量更新时,需重新 `Glob "./assistants/rules/**/*"` 与本表对比,识别新增/修改/删除的规范文件,任何触发的设计修订都需在本表追加记录。

---

## 6. 规范自检结论

- **完全合规的章节**:§1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §10 / §11 / §12 / §13 / §14(全部 14 个 RESULT.md 主章节)
- **经用户授权偏离的章节**:**0**
- **待澄清冲突**:**0**
- **建议派生(不影响本设计)**:
  - Q-P4:完整模式与快模式的"必生成过程文档清单"是否需要 `code-rule` 沉淀为 `mode-conventions.md`?(留作 follow-up)
  - Q-P5:快模式是否在 `code-auto` 默认走快模式?(留作 v2)
