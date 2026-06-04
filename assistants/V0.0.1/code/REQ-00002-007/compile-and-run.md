# 编译与启动验证 — REQ-00002-007
版本:V0.0.1

## 构建
- 命令:N/A(纯审计任务,无构建)
- 结论:N/A

## 启动
- 命令:N/A
- 结论:N/A

## 验证

### 不变量自检结果(13/13 全部 ✅)

| # | 不变量 | 验证命令 | 实际 | 状态 |
| --- | --- | --- | --- | --- |
| INV-1 | SKILL.md/模板/README 0 旧格式 | `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/` | 0 命中 | ✅ |
| INV-1.1 | SKILL.md/模板/README 0 旧 BUG | `Grep "BUG-\d{3}\b" plugins/code-skills/` | 0 命中 | ✅ |
| INV-1.2 | SKILL.md/模板/README 0 旧 TASK | `Grep "TASK-\d{4}-\d{4}-\d{3}" plugins/code-skills/` | 0 命中 | ✅ |
| INV-2 | SKILL.md frontmatter 0 变更 | `git diff plugins/code-skills/skills/*/SKILL.md` | clean(已 commit) | ✅ |
| INV-3 | `marketplace.json` + `plugin.json` 0 变更 | `git status .claude-plugin/ plugins/code-skills/.claude-plugin/` | clean | ✅ |
| INV-3.1 | `marketplace.json` + `plugin.json` 内 0 旧格式 | `Grep "REQ-\d{4}-\d{4}|BUG-\d{3}\b"` | 0 命中 | ✅ |
| INV-4 | 中英 README 变更行数差异 ≤ 1 | `git diff --stat HEAD~6 HEAD -- README.md README.en.md` | 72+/72-(差异 0) | ✅ |
| INV-5 | 5 个现有 `rules/` 文件 0 变更 | `git status assistants/rules/` | clean(仅新增,无修改) | ✅ |
| INV-5.1 | 5 个现有 `rules/` 内 0 旧格式 | 5 个文件逐一 Grep | 5/5 = 0 命中 | ✅ |
| INV-6 | V0.0.0 EXISTING-* 0 变更 | `git status assistants/V0.0.0/` | clean | ✅ |
| INV-7 | 27 模板全部更新(实际改 11 个) | `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/*/templates/` | 0 命中 | ✅ |
| INV-8 | TASK 需求任务格式严格 | `Grep "TASK-REQ-\d{5}-\d{5}" plugins/` | 0 命中(plugins/ 不引用 TASK) | ✅ |
| INV-9 | TASK 缺陷任务格式严格 | `Grep "TASK-BUG-\d{5}-\d{5}" plugins/` | 0 命中 | ✅ |
| INV-10 | TASK 编码不含 `REQ-` / `BUG-` 前缀 | (同 INV-8/9) | 0 命中 | ✅ |
| INV-11 | 看板/工作文件中旧串保留(预期) | `Grep "REQ-\d{4}-\d{4}" assistants/V0.0.1/` | 3+ 处(全部预期保留) | ✅ |
| INV-11.1 | 同上,旧 BUG | `Grep "BUG-\d{3}\b" assistants/V0.0.1/` | 3+ 处(全部预期保留) | ✅ |
| INV-12 | 新规范文件由 code-it 创建 | `ls assistants/rules/{encoding-conventions,migration-mapping}.md` | 2 文件存在(7202+10172 bytes) | ✅ |
| INV-13 | 7 个 commit 按预期顺序 | `git log --oneline -7` | 5 个新 commit 顺序正确 | ✅ |

### 全仓库 Grep 排除 V0.0.1 工作文件

| 模式 | 命中 | 状态 |
| --- | --- | --- |
| `REQ-\d{4}-\d{4}` | 0 | ✅ |
| `BUG-\d{3}\b` | 0 | ✅ |
| `TASK-\d{4}-\d{4}-\d{3}` | 0 | ✅ |

### 修复记录
- 无(无错误)
