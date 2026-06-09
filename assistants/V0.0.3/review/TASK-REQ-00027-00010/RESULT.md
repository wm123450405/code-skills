# TASK-REQ-00027-00010 — code-auto 步骤 2/3 适配 BUG 路径(`code-design` BUG 跳过 / `code-plan` BUG 路径入参)

- 任务编码:TASK-REQ-00027-00010
- 需求编码:REQ-00027
- 所属版本:V0.0.3
- 任务类型:修改
- **触发/来源:审查改修**
- 严重程度:必须改
- 触发时间:2026-06-08 17:30
- 触发者:code-review(Claude Opus 4.8)
- 关联原任务:TASK-REQ-00027-00002
- 关联评审报告:./assistants/V0.0.3/review/REQ-00027/REVIEW-REPORT.md §3.2 / F-7
- 状态:待开始
- 当前版本:v1

## 1. 任务概述

`code-auto/SKILL.md` 步骤 2 "code-design"(L325-333)+ 步骤 3 "code-plan"(L335-343)目前**只有** 1 个子分支(默认走需求路径:`Skill: code-design REQ-NNNNN` / `Skill: code-plan REQ-NNNNN`),未按模式分支。

BUG 路径下,`code-design` 应**跳过**(`code-design` 不接 BUG-NNN,需求 §2.4 决策 4 + 设计 §2.3 模式 C 状态机均无 code-design),`code-plan` 应接收 `<BUG-NNN>` 走缺陷分支(沿用 `code-plan` 既有缺陷分支)。

本任务为步骤 2 / 步骤 3 各加 1 个 BUG 路径子分支。

## 2. 问题清单

### 问题 F-7:步骤 1 子分支 1A-1D 仍按"需求路径"设计,缺 1E BUG 路径子分支
- **位置**:`plugins/code-skills/skills/code-auto/SKILL.md` L325-333(步骤 2 code-design)+ L335-343(步骤 3 code-plan)
- **类别**:设计符合度
- **严重程度**:必须改
- **依据**:
  - 设计:./assistants/V0.0.3/design/REQ-00027/RESULT.md §2.3 模式 C 状态机(无 code-design)
  - 详细设计:./assistants/V0.0.3/plan/REQ-00027/RESULT.md §2.2 + §7.3 子技能调用表
  - 需求:./assistants/V0.0.3/require/REQ-00027/RESULT.md §7.3 步骤 1-7(无 code-design)
- **现象**(L325-333):
  ```
  ### 步骤 2:code-design
  Skill: code-design
  Args: REQ-NNNNN
  - 期望产物:./assistants/<版本号>/design/REQ-NNNNN/RESULT.md
  - 失败处理:子技能退出码 ≠ 0 → 中断 + 报告(退出 1)
  ```
  与 L335-343:
  ```
  ### 步骤 3:code-plan
  Skill: code-plan
  Args: REQ-NNNNN
  - 期望产物:./assistants/<版本号>/plan/REQ-NNNNN/{RESULT,PLAN}.md
  - 失败处理:子技能退出码 ≠ 0 → 中断 + 报告(退出 1)
  ```
- **问题描述**:BUG 路径下,`code-design` **不**被调用(模式 C 状态机无 code-design),`code-plan` 接收 `<BUG-NNN>` 走缺陷分支。当前步骤 2 / 步骤 3 各自只有 1 个默认子分支,无法适配 BUG 路径——若用户在 BUG 路径下误走,会强行调 `code-design BUG-NNN`(`code-design` 不接受该格式,中断 + 报告退出 1)。
- **建议改修**:

1. **步骤 2 加 2A / 2B 子分支**:
   ```
   ### 步骤 2:code-design(条件化)

   #### 2A. 默认(需求路径:req-skip-require / req-run-require / req-content)
   Skill: code-design
   Args: REQ-NNNNN
   - 期望产物:./assistants/<版本号>/design/REQ-NNNNN/RESULT.md
   - 失败处理:子技能退出码 ≠ 0 → 中断 + 报告(退出 1)

   #### 2B. 跳过(BUG 路径:bug-skip-require / fix-skip-require)
   - 屏幕日志:
     [code-auto] 步骤 2/7:code-design(模式跳过,BUG 路径不调概要设计)
     [code-auto]   → 跳过依据:模式 C 不调概要设计
   - 不调任何子技能,直接进步骤 3
   ```

2. **步骤 3 加 3A / 3B 子分支**:
   ```
   ### 步骤 3:code-plan(条件化)

   #### 3A. 默认(需求路径:req-skip-require / req-run-require / req-content)
   Skill: code-plan
   Args: REQ-NNNNN
   - 期望产物:./assistants/<版本号>/plan/REQ-NNNNN/{RESULT,PLAN}.md
   - 失败处理:子技能退出码 ≠ 0 → 中断 + 报告(退出 1)

   #### 3B. 缺陷分支(BUG 路径:bug-skip-require / fix-skip-require)
   Skill: code-plan
   Args: <BUG-NNN>
   - 期望产物:./assistants/<版本号>/fix/<BUG-NNN>/fix-plan.md
   - 失败处理:子技能退出码 ≠ 0 → 中断 + 报告(退出 1)
   ```
- **替代方案**:在步骤 2 顶部加"若 BUG 路径 → 跳过"if 块 — 部分缓解,但缺少 3A / 3B 显式分支,不利于阅读,**不推荐**

## 3. 应当改修的文件清单

### 文件 1:`plugins/code-skills/skills/code-auto/SKILL.md`
- **关联问题**:F-7
- **当前状态**:L325-333(步骤 2)+ L335-343(步骤 3)
- **应改为**:步骤 2 拆为 2A / 2B;步骤 3 拆为 3A / 3B
- **理由**:对齐需求 §7.3 步骤 1-7 + 设计 §2.3 模式 C
- **改动范围**:2 段(步骤 2 / 步骤 3)

## 4. 不需要做的(避免越界)

- **不**改 frontmatter
- **不**改步骤 4-7(既有子分支已正确;详 T-008/T-009 适配触发模式措辞)
- **不**改 `code-design` / `code-plan` 自身
- **不**改其他 `code-*` SKILL.md
- **不**改 README / CLAUDE.md

## 5. 验证手段

- **静态校验**:`git diff` 显示 L325-333 + L335-343 变更
- **字面校验**:`grep "^#### 2A" code-auto/SKILL.md` 应有 1 处
- **字面校验**:`grep "^#### 3A" code-auto/SKILL.md` 应有 1 处
- **回退方式**:`git revert <commit>`

## 6. 关联依据汇总

| 类型 | 路径 | 章节 |
| --- | --- | --- |
| 设计 | ./assistants/V0.0.3/design/REQ-00027/RESULT.md | §2.3 模式 C 状态机 |
| 详细设计 | ./assistants/V0.0.3/plan/REQ-00027/RESULT.md | §2.2 + §7.3 |
| 需求 | ./assistants/V0.0.3/require/REQ-00027/RESULT.md | §7.3 步骤 1-7 + FR-2 |
| 评审报告 | ./assistants/V0.0.3/review/REQ-00027/REVIEW-REPORT.md | §3.2 / F-7 |

## 7. 完成定义(DoD)

- [ ] L325-333 拆为 2A (默认) / 2B (BUG 跳过)
- [ ] L335-343 拆为 3A (默认) / 3B (缺陷分支)
- [ ] 2B 屏幕日志:code-design 模式跳过
- [ ] 3B 入参为 `<BUG-NNN>`,期望产物为 `fix/<BUG-NNN>/fix-plan.md`
- [ ] frontmatter 字节级一致
- [ ] 步骤 4-7 未改
- [ ] `git diff` 仅显示 code-auto/SKILL.md 步骤 2/3 变更

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-08 17:30 | v1 | 初始创建 | 由 code-review 派生,基于 T-002 步骤 2/3 未适配 BUG 路径 | code-review(Claude Opus 4.8) |
