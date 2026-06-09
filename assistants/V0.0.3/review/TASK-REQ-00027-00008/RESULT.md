# TASK-REQ-00027-00008 — code-auto 步骤 1 新增"模式 C"识别(首段匹配 `^BUG-\d{5}$`),独立于 fix-skip-require

- 任务编码:TASK-REQ-00027-00008
- 需求编码:REQ-00027
- 所属版本:V0.0.3
- 任务类型:修改
- **触发/来源:审查改修**
- 严重程度:必须改
- 触发时间:2026-06-08 17:30
- 触发者:code-review(Claude Opus 4.8)
- 关联原任务:TASK-REQ-00027-00002
- 关联评审报告:./assistants/V0.0.3/review/REQ-00027/REVIEW-REPORT.md §3.2 / F-5
- 状态:待开始
- 当前版本:v1

## 1. 任务概述

`code-auto/SKILL.md` 步骤 4 "子技能调用表" 段新增的"BUG 路径子技能调用表"写"触发:`fix-skip-require` 模式"(L219),但需求 §7.2 / 设计 §2.3 / 详细设计 §2.2 明确要求新增独立的"模式 C"——首段匹配 `^BUG-\d{5}$` 触发,作为第 5 种模式,不是 `fix-skip-require` 模式的延伸。

`fix-skip-require` 模式是"缺陷已登记续跑"(基于目录检测 `fix/<input>/` 存在);模式 C 是"BUG 路径(本轮新增)"(基于正则匹配 `^BUG-\d{5}$`)。两者触发条件不同、行为不同:`fix-skip-require` 走"code-design 跳过 + code-plan 走缺陷分支"路径,模式 C 走"完全不调 code-design + code-plan 走缺陷分支"路径(模式 C 不调 `code-require` 也不调 `code-design`,直接 `code-plan`)。

本任务把 BUG 路径的触发条件改为"模式 C",并在 §"4 种路径感知模式"扩展为 5 种(详 T-009)。

## 2. 问题清单

### 问题 F-5:BUG 路径子技能调用表写"触发:`fix-skip-require` 模式",与设计不符
- **位置**:`plugins/code-skills/skills/code-auto/SKILL.md` L219
- **类别**:设计符合度
- **严重程度**:必须改
- **依据**:
  - 设计:./assistants/V0.0.3/design/REQ-00027/RESULT.md §2.3 模式 C + §2.4 决策 2
  - 详细设计:./assistants/V0.0.3/plan/REQ-00027/RESULT.md §2.2 模块 2 + §3.2 模式识别算法
  - 需求:./assistants/V0.0.3/require/REQ-00027/RESULT.md §7.2 模式识别表 + FR-2
- **现象**(L219):
  ```
  **BUG 路径子技能调用表**(本轮 REQ-00027 新增,触发:`fix-skip-require` 模式):
  ```
- **问题描述**:`fix-skip-require` 模式是"基于目录检测"(`fix/<input>/` 存在,见 L79);模式 C 是"基于正则匹配"(首段 `^BUG-\d{5}$`,见详细设计 §3.2)。两者是不同概念,不能混用。
- **建议改修**(L219 改写):
  ```
  **BUG 路径子技能调用表**(本轮 REQ-00027 新增,触发:模式 C,首段匹配 `^BUG-\d{5}$`):
  ```
  + 模式 C 的具体实现(目录检测 vs 正则匹配)详 T-009。
- **替代方案**:保留"触发:`fix-skip-require` 模式"措辞,在 §"4 种路径感知模式"加注释"模式 C 是 fix-skip-require 的 BUG 路径特例" — **不推荐**(混淆两个模式)

## 3. 应当改修的文件清单

### 文件 1:`plugins/code-skills/skills/code-auto/SKILL.md`
- **关联问题**:F-5
- **当前状态**:L219(BUG 路径子技能调用表标题)
- **应改为**:"触发:模式 C,首段匹配 `^BUG-\d{5}$`"
- **理由**:对齐详细设计 §2.2 + §3.2
- **改动范围**:仅改 L219 一行

## 4. 不需要做的(避免越界)

- **不**改 L73-80 "4 种路径感知模式" 表(由 T-009 扩展为 5 种)
- **不**改步骤 1 子分支 1A-1D(由 T-009 新增 1E)
- **不**改步骤 2/3(由 T-010 适配)
- **不**改 frontmatter
- **不**改其他章节

## 5. 验证手段

- **静态校验**:`git diff` 显示 L219 一行变更
- **字面校验**:`grep "触发:" code-auto/SKILL.md` 在 BUG 路径子技能调用表段应为"触发:模式 C,首段匹配 `^BUG-\d{5}$`"
- **回退方式**:`git revert <commit>`

## 6. 关联依据汇总

| 类型 | 路径 | 章节 |
| --- | --- | --- |
| 设计 | ./assistants/V0.0.3/design/REQ-00027/RESULT.md | §2.3 模式 C + §2.4 决策 2 |
| 详细设计 | ./assistants/V0.0.3/plan/REQ-00027/RESULT.md | §2.2 模块 2 + §3.2 |
| 需求 | ./assistants/V0.0.0/require/REQ-00027/RESULT.md | §7.2 + FR-2 |
| 评审报告 | ./assistants/V0.0.3/review/REQ-00027/REVIEW-REPORT.md | §3.2 / F-5 |

## 7. 完成定义(DoD)

- [ ] L219 改为"触发:模式 C,首段匹配 `^BUG-\d{5}$`"
- [ ] frontmatter 字节级一致
- [ ] 其他内容未改
- [ ] `git diff` 仅显示 code-auto/SKILL.md L219 变更

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-08 17:30 | v1 | 初始创建 | 由 code-review 派生,基于 T-002 BUG 路径触发模式偏离 | code-review(Claude Opus 4.8) |
