# TASK-REQ-00027-00009 — code-auto §"路径感知模式"扩展为 5 种(新增"模式 C"),§"步骤 1 子分支"扩展为 1A-1E

- 任务编码:TASK-REQ-00027-00009
- 需求编码:REQ-00027
- 所属版本:V0.0.3
- 任务类型:修改
- **触发/来源:审查改修**
- 严重程度:必须改
- 触发时间:2026-06-08 17:30
- 触发者:code-review(Claude Opus 4.8)
- 关联原任务:TASK-REQ-00027-00002
- 关联评审报告:./assistants/V0.0.3/review/REQ-00027/REVIEW-REPORT.md §3.2 / F-6
- 状态:待开始
- 当前版本:v1

## 1. 任务概述

`code-auto/SKILL.md` §"路径感知模式"表(L73-80)只有 4 种模式(req-skip-require / req-run-require / fix-skip-require / req-content);但需求 §7.2 / 设计 §2.3 / 详细设计 §2.2 要求新增第 5 种"模式 C"(BUG 路径)。

`code-auto/SKILL.md` §"步骤 1 子分支"也只有 4 个(1A/1B/1C/1D),缺 1E 子分支覆盖 BUG 路径。

异常表 E-20(BUG 路径模式 C 错配)已经引用"模式 C"概念(L735),但 §"4 种路径感知模式"无该模式,出现"概念引用但未实现"的悬空。

本任务把"4 种"扩为"5 种",把"1A-1D"扩为"1A-1E"。

## 2. 问题清单

### 问题 F-6:异常表 E-20 引用"模式 C",但 §"4 种路径感知模式"无该模式
- **位置**:`plugins/code-skills/skills/code-auto/SKILL.md` L73-80(模式表)+ L273-323(步骤 1 子分支)+ L735(E-20)
- **类别**:规范 / 接口
- **严重程度**:必须改
- **依据**:
  - 设计:./assistants/V0.0.3/design/REQ-00027/RESULT.md §2.3 + §2.4
  - 详细设计:./assistants/V0.0.3/plan/REQ-00027/RESULT.md §2.2 + §3.2
  - 需求:./assistants/V0.0.3/require/REQ-00027/RESULT.md §7.2 + FR-2
- **现象**:
  - L73:"**4 种路径感知模式**(本需求 REQ-00024 改造,替代原"模式 A / 模式 B 关键字"):" — 应改为"5 种"
  - L75-80 表头缺第 5 行
  - L82-94 路径感知判定算法(伪代码)只列 4 种模式,缺第 5 种
  - L99 屏显契约:`[code-auto]   → 模式:<req-skip-require / req-run-require / fix-skip-require / req-content>` 缺 `bug-skip-require` 或 `req-content → bug-skip-require`
  - L273-323 步骤 1 子分支 1A/1B/1C/1D 缺 1E(BUG 路径)
  - L735 异常 E-20 已写"BUG 路径模式 C 错配" — 概念悬空
- **问题描述**:"模式 C" 在 E-20 中已被引用,但"5 种路径感知模式"未真正实现;步骤 1 子分支 1A-1D 仍按"需求路径"设计。必须把"模式 C" 在 §"路径感知模式" 表 / §"路径感知判定算法" / §"屏显契约" / §"步骤 1 子分支" 全部落地。
- **建议改修**:

1. **L73 段头改写**:
   ```
   **5 种路径感知模式**(本需求 REQ-00024 改造 + REQ-00027 新增模式 C):
   ```

2. **L75-80 表加第 5 行**:
   ```
   | **bug-skip-require** | 首段匹配 `^BUG-\d{5}$` + `fix/<BUG-NNN>/` 存在 | 缺陷已登记,走 BUG 路径(code-plan → code-it → code-unit(条件) → code-check) | 是(跳过 code-require + code-design,直接进 code-plan 走缺陷分支) |
   ```

3. **L82-94 路径感知判定算法加第 5 种**:
   ```
   1. 拼接所有参数 token 为单一字符串(空格分隔)
   2. 去除首尾空白
   3. 正则检测(优先于目录检测):
      - 首段匹配 `^BUG-\d{5}$` → 模式:bug-skip-require(模式 C,本轮 REQ-00027 新增)
   4. 检查 `require/<input>/` 目录(test -d):
      - 存在 → 继续检查 `require/<input>/RESULT.md` 文件(test -f):
        - 存在 → 模式:req-skip-require
        - 不存在 → 模式:req-run-require
   5. 检查 `fix/<input>/` 目录(test -d):
      - 存在 → 模式:fix-skip-require
   6. 既不是需求编号也不是缺陷编号 → 模式:req-content
   ```

4. **L99 屏显契约加 `bug-skip-require`**:
   ```
   [code-auto]   → 模式:<req-skip-require / req-run-require / fix-skip-require / bug-skip-require / req-content>
   ```

5. **L273-323 步骤 1 子分支新增 1E**:
   ```
   #### 1E. 模式 bug-skip-require(缺陷 BUG 路径,本轮 REQ-00027 新增) — 跳过 code-require + code-design,直接进 code-plan 走 BUG 路径

   1. 路径感知判定结果 = bug-skip-require(本步骤 0 之前已完成,正则匹配 `^BUG-\d{5}$`)
   2. 屏幕日志:
      [code-auto] 步骤 1/7:code-require(模式跳过,BUG 路径)
      [code-auto]   → 校验通过:fix/BUG-NNNNN/ 目录存在 ✓
      [code-auto] 步骤 2/7:code-design(模式跳过,BUG 路径不调概要设计)
   3. 进入步骤 3,步骤 3-7 走 BUG 路径子技能调用表(详 §"子技能调用表" 段 BUG 路径)
   ```
- **替代方案**:把"模式 C"作为"模式 fix-skip-require 的特例" — 部分缓解,但需求 §7.2 明确要求 5 种模式独立,**不推荐**

## 3. 应当改修的文件清单

### 文件 1:`plugins/code-skills/skills/code-auto/SKILL.md`
- **关联问题**:F-6
- **当前状态**:L73 / L75-80 / L82-94 / L99 / L273-323
- **应改为**:扩为 5 种模式 + 1A-1E 子分支
- **理由**:对齐需求 §7.2 + 设计 §2.3 + 详细设计 §2.2 + E-20 已存在引用
- **改动范围**:5 段(段头 + 表 + 算法 + 屏显契约 + 子分支)

## 4. 不需要做的(避免越界)

- **不**改 frontmatter
- **不**改步骤 2/3(由 T-010 适配)
- **不**改 BUG 路径子技能调用表(由 T-008 改触发模式措辞)
- **不**改 E-20 措辞(已正确)
- **不**改其他 `code-*` SKILL.md
- **不**改 README / CLAUDE.md

## 5. 验证手段

- **静态校验**:`git diff` 显示 5 段变更
- **字面校验**:`grep "4 种路径感知模式" code-auto/SKILL.md` 应为 0 处(原 1 处,改为"5 种"后 0 处)
- **字面校验**:`grep "bug-skip-require" code-auto/SKILL.md` 应有 ≥ 4 处(表 + 算法 + 屏显 + 子分支)
- **回退方式**:`git revert <commit>`

## 6. 关联依据汇总

| 类型 | 路径 | 章节 |
| --- | --- | --- |
| 设计 | ./assistants/V0.0.3/design/REQ-00027/RESULT.md | §2.3 + §2.4 决策 2 |
| 详细设计 | ./assistants/V0.0.3/plan/REQ-00027/RESULT.md | §2.2 + §3.2 |
| 需求 | ./assistants/V0.0.3/require/REQ-00027/RESULT.md | §7.2 + FR-2 |
| 评审报告 | ./assistants/V0.0.3/review/REQ-00027/REVIEW-REPORT.md | §3.2 / F-6 |

## 7. 完成定义(DoD)

- [ ] L73 改为"5 种路径感知模式"
- [ ] L75-80 表加第 5 行 `bug-skip-require`
- [ ] L82-94 算法加正则检测分支
- [ ] L99 屏显契约加 `bug-skip-require`
- [ ] L273-323 步骤 1 加 1E 子分支
- [ ] frontmatter 字节级一致
- [ ] E-20 措辞未改
- [ ] `git diff` 仅显示 code-auto/SKILL.md 5 段变更

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-08 17:30 | v1 | 初始创建 | 由 code-review 派生,基于 T-002 模式 C 概念悬空 | code-review(Claude Opus 4.8) |
