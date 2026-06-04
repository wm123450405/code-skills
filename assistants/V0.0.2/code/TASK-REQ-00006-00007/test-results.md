# 测试结果 — TASK-REQ-00006-00007

版本:V0.0.2
时间:2026-06-04 18:03
任务:T-007 `[文档] 不变量自检 + 同步 V0.0.2 看板 + 偏差日志`

## 测试命令

**N/A** — 本仓库无 test 命令,纯文档型。
本任务的"测试"= 8 项不变量 + 9 项 NFR 自检(详 `compile-and-run.md`)。

## 不适用说明

本任务**测试状态 = 不适用**的理由(沿用 PLAN.md §3):

1. 本仓库无传统单元测试
2. T-007 是**自检任务**,不引入新代码
3. 测试 = "8 项不变量自检"已在 `compile-and-run.md` 完成

## 端到端验证场景(将由用户实际调用 code-publish 时验证 — 本任务未执行)

| 场景 | 输入 | 预期(待用户实际调用时验证) |
| --- | --- | --- |
| 1. V0.0.2(预期有未完成任务) | `/code-publish` | 不通过报告 + 阻塞统计 + 不生成手册(因为需求/任务/缺陷有未解决) |
| 2. V0.0.0(预期可发布基线) | `/code-publish V0.0.0` | 通过 + 基线模板 + 仅 2 份手册生成(DEPLOY + Q&A,无 UPDATE) |
| 3. qanda/ 删除后 | `/code-publish` | 通过 + qanda/ 自动重建 + Q&A.md 占位提示 |

**说明**:本任务**未实际执行**这 3 场景,因为:
- V0.0.2 当前需求/任务/缺陷**有未完成项** — 调 `code-publish` 不会进入 Step 2(场景 1 实际可跑,但仅验证"不通过"路径)
- 场景 2 / 3 需要"可发布版本" — 当前无
- T-007 是"自检任务"而非"运行任务";端到端 3 场景的**完整验证**属于**用户实际使用** `code-publish` 时的范畴

**本任务已完成的"端到端前置"**:
- ✓ SKILL.md frontmatter 严格遵循 `skill-conventions §规则 1`
- ✓ 5 份模板在 `templates/` 子目录(严格遵循 `module-conventions §规则 1`)
- ✓ SKILL.md 的 7 工作流步骤完整 + 每步骤工具调用显式
- ✓ PreflightChecker 的判定逻辑(全检查最严)与 code-dashboard "真正可发布" 对齐(NFR-8)
- ✓ BaselineDetector 字典序最小(NFR-7)
- ✓ ManualBuilder 3 份手册生成逻辑
- ✓ QandaScaffolder + QandaAggregator + ReportFormatter
- ✓ 4 种报告模板(通过/不通过/基线/qanda 空)

## 失败用例详情

无(本任务无失败用例;8 项不变量 + 9 项 NFR 全部通过)
