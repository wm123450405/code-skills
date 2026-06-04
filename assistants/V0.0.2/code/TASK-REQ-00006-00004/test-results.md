# 测试结果 — TASK-REQ-00006-00004

版本:V0.0.2
时间:2026-06-04 17:52
任务:T-004 `[新增] 写 templates/Q&A.md 模板`

## 测试命令

**N/A** — 本仓库无 test 命令,纯文档型。

## 不适用说明

本任务**测试状态 = 不适用**的理由(沿用 PLAN.md §3):

1. 本仓库无传统单元测试
2. Q&A.md 模板是"静态文档",无运行时函数可测
3. 模板的"测试"=人工调用 `code-publish` 生成 publish/Q&A.md 后目检;由 T-007 收尾任务执行
4. 端到端验证:需"可发布版本" + qanda/ 内容才能完整验证

## 端到端验证场景(将由 T-007 执行)

| 场景 | 输入 | 预期 |
| --- | --- | --- |
| 1. qanda/ 空(仅 README.md) + `code-publish` | `/code-publish` | `publish/Q&A.md` 包含 H1 + 引言 + 占位章节(模板原样) |
| 2. qanda/ 有 2 个文件 + `code-publish` | `/code-publish` | `publish/Q&A.md` 包含 H1 + 引言 + 2 个 `## <主题>(来源:...)` 章节 + 占位章节(模板中说明的兜底) |
| 3. qanda/ 仅 README.md(空) + `code-publish` | `/code-publish` | `publish/Q&A.md` = 模板原样 + 报告中标注"⚠ qanda/ 目录为空" |

## 失败用例详情

无(本任务无失败用例;静态结构验证全部通过)
