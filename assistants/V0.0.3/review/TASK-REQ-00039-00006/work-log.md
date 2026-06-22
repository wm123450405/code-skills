# 评审工作日志 — TASK-REQ-00039-00006

- 任务编码:TASK-REQ-00039-00006
- 所属版本:V0.0.3
- 评审时间:2026-06-22 16:35
- 评审者:wangmiao
- 当前版本:v1

## 本任务来源

本任务由 `code-check REQ-00039` 评审派生(2026-06-22 16:35),合并原任务 T-2 / T-3 / T-4 评审发现的 3 项字面问题:

| 原任务 | 发现 | 严重程度 | 类别 | 位置 |
| --- | --- | --- | --- | --- |
| T-4 | F-T4-1 | 必须改 | 正确性 | `code-it/templates/RESULT.md` line 124(模板标题末尾未闭合的半角逗号) |
| T-2 | F-T2-1 | 建议改 | 一致性 | `code-it/SKILL.md` line 762(步骤 8.6.3 E-3 字面与共享库 §函数 2 错误处理职责混淆) |
| T-3 | F-T3-1 | 建议改 | 一致性 | `code-check/SKILL.md` line 440(步骤 8.13 "总规模优先,新增次之" 字面与共享库 §函数 4 算法字面有出入) |

合并理由:3 项问题都涉及"字面残留 / 字面不一致"且都影响"调用方字面与共享库字面对齐"语义;虽跨 3 文件,但共同目标是"修正字面",合并为 1 个任务便于统一处理。

## 详细问题清单

详见 `./assistants/V0.0.3/review/REQ-00039/work-log.md §任务评审结果(T-2 / T-3 / T-4 详情)` + 本任务 `RESULT.md §2 问题清单(F-1 / F-2 / F-3)`。

## 应当改修的文件清单

### 文件 1:`plugins/code-skills/skills/code-it/templates/RESULT.md`

- **关联问题**:F-1(必须改)
- **当前状态**:line 124 标题为 `## 10. 逻辑行统计(由 code-it 内化,新增,`(末尾未闭合的半角逗号)
- **应改为**:`## 10. 逻辑行统计(由 code-it 内化,新增)`(末尾无逗号)
- **改动范围**:只改 line 124 标题末尾的半角逗号(删除 1 个字符)

### 文件 2:`plugins/code-skills/skills/code-it/SKILL.md`

- **关联问题**:F-2(建议改)
- **当前状态**:line 762 E-3 处理列写为 "跳过该文件 + 屏显警告"
- **应改为**:"`calcLogicLines` 返回 error 对象,任务级跳过该文件,继续下一文件 + 屏显警告"
- **改动范围**:只改 line 762 的 E-3 行处理列

### 文件 3:`plugins/code-skills/skills/code-check/SKILL.md`

- **关联问题**:F-3(建议改)
- **当前状态**:line 440 写为 "新增超标阈值级别同上(**总规模优先,新增次之**)"
- **应改为**:"新增超标阈值级别同上(先判 totalLoc,再判 newLoc,两个独立发现可同时触发)"
- **改动范围**:只改 line 440 的字面

## 验证手段

- **F-1 验证**:`grep -n "^## 10\. 逻辑行统计" plugins/code-skills/skills/code-it/templates/RESULT.md` — 确认 line 124 标题末尾**无**逗号
- **F-2 验证**:读 `code-it/SKILL.md` 步骤 8.6.3 E-3 行,确认处理列字面已更新
- **F-3 验证**:`grep -n "总规模优先" plugins/code-skills/skills/code-check/SKILL.md` — 确认**无**命中

## 关联评审报告

`./assistants/V0.0.3/review/REQ-00039/REVIEW-REPORT.md §5 派生的新任务列表`
