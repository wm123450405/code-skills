# 偏离记录 — REQ-00002-001
版本:V0.0.1

## 无偏离

- 本任务**未做任何设计偏离**。所有替换均按 PLAN.md §2.1 + REQU §FR-1/FR-2 编码映射表执行。
- 5 个 SKILL.md 全部为"只改正文,不动 frontmatter"(`skill-conventions.md` §规则 1 严格遵循)。
- 范围严格限定在 10 个 SKILL.md 内,未触及 templates/ 目录(由 T-002 单独处理)。
- 未触及任何其他文件(marketplace.json / plugin.json / 其他 9 个 SKILL.md frontmatter 等 INV 边界保持)。

## 范围外但被识别的事项(留给后续任务)
- **范围外文件清单**(不在 T-001 内,由后续任务处理):
  - `code-design/templates/assistants-layout.md`(T-002)
  - `code-version/templates/assistants-layout.md` + `version-RESULT.md`(T-002)
  - `code-plan/templates/assistants-layout.md`(T-002)
  - `code-require/templates/assistants-layout.md` + `requirements.md`(T-002)
  - `code-it/templates/assistants-layout.md`(T-002)
  - `code-unit/templates/assistants-layout.md`(T-002)
  - `code-fix/templates/bug.md` + `fix-registry.md` + `assistants-layout.md`(T-002)
- 这些命中**正常**,因为本任务边界明确仅限 SKILL.md。

## 时间
2026-06-04 09:50
