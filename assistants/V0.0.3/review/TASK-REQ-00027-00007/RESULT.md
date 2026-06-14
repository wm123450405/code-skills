# TASK-REQ-00027-00007 — code-fix 全局清理 investigation.md 引用(纯登记型不再创建该文件)

- 任务编码:TASK-REQ-00027-00007
- 需求编码:REQ-00027
- 所属版本:V0.0.3
- 任务类型:修改
- **触发/来源:审查改修**
- 严重程度:必须改
- 触发时间:2026-06-08 17:30
- 触发者:code-review(Claude Opus 4.8)
- 关联原任务:TASK-REQ-00027-00001
- 关联评审报告:./assistants/V0.0.3/review/REQ-00027/REVIEW-REPORT.md §3.1 / F-4
- 状态:待开始
- 当前版本:v1

## 1. 任务概述

`code-fix/SKILL.md` 在多处仍把 `investigation.md` 列为本技能可写文件(L237, L279, L381, L400-406),但"工作目录约定"段(纯登记型声明本技能**不**产出 `fix-plan.md` / `fix-work-log.md` 等下游文件)+ "过程文档格式(纯登记型)" 段(本技能不产出 `fix-plan.md` / `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` / `deviations.md`)已明确不产出该文件;但 `investigation.md` 不在该"不产出"清单中,导致角色模糊——本技能**既声明**纯登记型不写文件,**又**在多处提及可写 `investigation.md`。

本任务把 `investigation.md` 角色明确划归 `code-it`(沿用 `code-it` BUG 路径的"调查笔记"功能),`code-fix` 仅**读取**(若有)该文件,不创建/更新。

## 2. 问题清单

### 问题 F-4:investigation.md 角色在多节中残留
- **位置**:`plugins/code-skills/skills/code-fix/SKILL.md` L237 / L279 / L381 / L400-406
- **类别**:一致性 / 可维护性
- **严重程度**:必须改
- **依据**:
  - 设计:./assistants/V0.0.3/design/REQ-00027/RESULT.md §2.2(纯登记型不写代码)
  - 详细设计:./assistants/V0.0.3/plan/REQ-00027/RESULT.md §2.1 过程文档格式 + §3 过程文档
  - 需求:./assistants/V0.0.3/require/REQ-00027/RESULT.md FR-1
- **现象**:
  - L237 步骤 3:`investigation.md`:调查笔记
  - L279 步骤 5:`→ 调查中`:询问"初步根因假设是什么?涉及哪些文件?"(可写 `investigation.md`)
  - L381 步骤 10:- 收尾 `investigation.md`(若有)
  - L400-406 过程文档格式段:独立小节"### investigation.md(可选)" 自由形式
- **问题描述**:`investigation.md` 在 T-001(2026-06-08 15:40 commit)前后未在"不产出"清单中明确划出;步骤 3 / 步骤 5 / 步骤 10 仍把该文件作为本技能可写文件,违反"纯登记型"语义。`investigation.md` 应由 `code-it` 在 BUG 路径下产出(类似 `fix-work-log.md` / `deviations.md` 的角色);`code-fix` 仅在复跑时**读取**该文件,获取调查进度。
- **建议改修**(4 处修改):
  - L237 步骤 3:把 `investigation.md`:调查笔记 改为 `investigation.md`:调查笔记(由 `code-it` 写入,本技能只读)
  - L279 步骤 5:`→ 调查中`:把"(可写 `investigation.md`)" 改为"(可由 `code-it` 写 `investigation.md`,本技能不写)"
  - L381 步骤 10:把"- 收尾 `investigation.md`(若有)" 改为"- 读 `investigation.md`(若有,本技能不创建)"
  - L400-406 过程文档格式段:把"### investigation.md(可选)" 改为"### investigation.md(由 `code-it` 写入,本技能只读)",并把该小节移出"过程文档格式(纯登记型)"段(该段专讲本技能产出的文件)
- **替代方案**:在"不产出"清单中加 "investigation.md" 一行 — 部分缓解,但 L237 / L279 / L381 三处仍提及该文件,**不推荐**

## 3. 应当改修的文件清单

### 文件 1:`plugins/code-skills/skills/code-fix/SKILL.md`
- **关联问题**:F-4
- **当前状态**:L237 / L279 / L381 / L400-406(4 处)
- **应改为**:把 4 处 `investigation.md` 角色统一为"由 `code-it` 写入,本技能只读"
- **理由**:对齐详细设计 §2.1 过程文档格式
- **改动范围**:仅改这 4 处

## 4. 不需要做的(避免越界)

- **不**改 `code-it/SKILL.md` 自身的 BUG 路径(本任务不动 `code-it` 行为)
- **不**改 frontmatter
- **不**改"过程文档格式"段对 `fix-plan.md` / `fix-work-log.md` 等的描述
- **不**改 README / CLAUDE.md

## 5. 验证手段

- **静态校验**:`git diff` 显示 L237 / L279 / L381 / L400-406 变更
- **字面校验**:`grep "investigation.md" code-fix/SKILL.md` 应仅 4 处(原 5 处,合并后 4 处)
- **回退方式**:`git revert <commit>`

## 6. 关联依据汇总

| 类型 | 路径 | 章节 |
| --- | --- | --- |
| 设计 | ./assistants/V0.0.3/design/REQ-00027/RESULT.md | §2.2 状态机收敛 |
| 详细设计 | ./assistants/V0.0.3/plan/REQ-00027/RESULT.md | §2.1 过程文档格式 + §3 |
| 需求 | ./assistants/V0.0.3/require/REQ-00027/RESULT.md | FR-1 |
| 评审报告 | ./assistants/V0.0.3/review/REQ-00027/REVIEW-REPORT.md | §3.1 / F-4 |

## 7. 完成定义(DoD)

- [ ] L237 / L279 / L381 / L400-406 共 4 处全部加 "由 code-it 写入,本技能只读" 说明
- [ ] "过程文档格式" 段不再有 "investigation.md(可选)" 小节
- [ ] frontmatter 字节级一致
- [ ] `git diff` 仅显示 code-fix/SKILL.md 4 处变更

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-08 17:30 | v1 | 初始创建 | 由 code-review 派生,基于 T-001 investigation.md 角色残留 | code-review(Claude Opus 4.8) |
