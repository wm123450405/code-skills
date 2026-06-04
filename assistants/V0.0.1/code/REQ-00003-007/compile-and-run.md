# 编译与启动验证 — REQ-00003-007
版本:V0.0.1

## 构建
- 命令:N/A(纯审计任务,无构建)
- 结论:N/A

## 启动
- 命令:N/A
- 结论:N/A

## 验证(11+ 项不变量自检)

| # | 不变量 | 验证命令 | 结果 |
| --- | --- | --- | --- |
| INV-1 | SKILL.md/模板/README 0 旧 REQ 格式 | `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/` | 0 命中 ✅ |
| INV-1.1 | 0 旧 BUG 格式 | `Grep "BUG-\d{3}\b" plugins/code-skills/` | 0 命中 ✅ |
| INV-1.2 | 0 旧 TASK 格式 | `Grep "TASK-\d{4}-\d{4}-\d{3}" plugins/code-skills/` | 0 命中 ✅ |
| INV-2 | 6 个新文件占位 | `Grep "## 规则 1: \(待添加\)" assistants/rules/*.md` | 6/6 = 6 命中 ✅ |
| INV-3 | CLAUDE.md 仅追加 | `git diff plugins/code-skills/CLAUDE.md` | clean(已 commit)✅ |
| INV-3.1 | CLAUDE.md 含 "## AI 工作约定" 小节 | `Grep` | L129 ✅ |
| INV-4 | SKILL.md frontmatter 0 变更 | `git diff` | clean ✅ |
| INV-5 | marketplace.json + plugin.json 0 变更 | `git status` | clean ✅ |
| INV-6 | 5 保留 rules/ 0 变更 | `git diff` | 5/5 = 0 变更 ✅ |
| INV-6.1 | 2 REQ-00002 新 rules/ 0 变更 | `git diff` | 0 变更 ✅ |
| INV-7 | module-conventions.md 仅 DEPRECATED | `Grep "DEPRECATED" module-conventions.md` | L7 ✅ |
| INV-8/9/10 | TASK 编码格式严格 | `Grep "TASK-(REQ|BUG)-\d{5}-\d{5}"` | 0 命中 ✅ |
| INV-11 | 看板/工作文件保留旧串(预期) | `Grep` | 多处历史字面值(预期)✅ |
| INV-12 | 2 个新规范文件存在 | `ls` | 2 文件 ✅ |
| INV-13 | 5 commit 顺序正确 | `git log` | 顺序正确 ✅ |

## 全仓库 Grep(排除 V0.0.1)

| 模式 | 命中 |
| --- | --- |
| `REQ-\d{4}-\d{4}` | 0 |
| `BUG-\d{3}\b` | 0 |
| `TASK-\d{4}-\d{4}-\d{3}` | 0 |

## 5 commit 顺序

```
086890d feat(code-rule): add 3 target types + 6 classification categories    ← T-001
bec5f13 feat(rules): add 6 placeholder classification files                    ← T-002
695c029 chore(rules): deprecate module-conventions.md (REQ-00003 H2)         ← T-003
2f41bb0 feat(code-rule): extend templates/rule.md with placeholder/bootstrap    ← T-004
35bc26b feat(CLAUDE.md): add AI 工作约定 section                            ← T-005
```

## 修复记录
- 无(无错误)
