# REQ-00027 概要设计 — 优化 code-fix 流程(纯登记型)+ code-auto BUG 路径

- **上游**:`./assistants/V0.0.3/require/REQ-00027/RESULT.md`
- **遵循规范**:`./assistants/rules/` 下 13 个文件
- **版本**:V0.0.3
- **最后更新**:2026-06-08 15:30

## 1. 设计目标

回答"`code-fix` 纯登记型 + `code-auto` BUG 路径编排"在系统层面的形态:
- **目标 A**:`code-fix` 仅产出 `fix/<BUG-NNN>/RESULT.md`,不实施代码改动、不产出 `fix-plan.md`、不推进"修复规划中"及之后状态
- **目标 B**:`code-auto` 在检测到 BUG-NNN 任务时,自动编排 `code-plan` → `code-it` → `code-unit`(条件) → `code-check` 流水线
- **目标 C**:`code-check` 复用 `code-review` 能力(本仓库 V0.0.3 现状,REQ-00022 已重命名)

(源自:FR-1 / FR-2 / FR-3 / FR-4)

## 2. 架构方案

### 2.1 整体架构(本仓库 + BUG 路径)

```
Claude Code
   │
   ├── /code-fix <BUG-NNN>        →  纯登记(本轮优化)
   │      ↓ 产出 fix/<BUG-NNN>/RESULT.md
   │      ↓ 不产出 fix-plan.md
   │
   ├── /code-plan <BUG-NNN>        →  沿用既有缺陷分支
   │      ↓ 产出 fix-plan.md
   │      ↓ 推进状态 调查中→修复规划中
   │
   ├── /code-it <BUG-NNN>          →  沿用既有缺陷分支
   │      ↓ 产出 fix-work-log.md 等
   │      ↓ 推进状态 修复规划中→修复编码中→已修复-待验证
   │
   ├── /code-unit <BUG-NNN>        →  沿用既有(条件触发)
   │      ↓ 若 fix-plan.md 标记"项目可测性=Y"
   │      ↓ 产出 fix-test-results.md
   │
   ├── /code-check <BUG-NNN>       →  沿用 code-review 能力
   │      ↓ 产出 fix/<BUG-NNN>/REVIEW-REPORT.md
   │      ↓ 推进状态 已修复-待验证→已修复-已验证→已关闭
   │
   └── /code-auto <BUG-NNN>        →  本轮新增模式 C
          ↓ 一次性串行:code-plan → code-it → code-unit → code-check
          ↓ 写 fix/<BUG-NNN>/auto-report.md
```

### 2.2 `code-fix` 状态机收敛(本轮优化)

```
报告 ←──┐
  │     │  (用户调 code-fix)
调查 中  │
  │     │
  ↓     │
修复规划中  ←──── code-plan 推进
  │
  ↓  (本轮 code-fix 不再推进此状态之后)
  ✗

修复编码中  ←──── code-it 推进
  │
已修复-待验证  ←──── code-it 推进
  │
已修复-已验证  ←──── code-check 推进
  │
已关闭  ←──── code-check 推进(终态)
```

`code-fix` 仅推进 报告 / 调查中 / 修复规划中(前 3 段);后续由 `code-plan` / `code-it` / `code-check` 推进

### 2.3 `code-auto` 模式 C(BUG 路径)状态机

```
模式识别:首段匹配 ^BUG-\d{5}$ → 模式 C
   ↓
code-plan <BUG-NNN>
   ↓ 产出 fix-plan.md
code-it <BUG-NNN>
   ↓ 产出 fix-work-log.md 等
code-unit <BUG-NNN>  (条件:fix-plan.md 标记 项目可测性=Y)
   ↓ 产出 fix-test-results.md
code-check <BUG-NNN>
   ↓ 产出 fix/<BUG-NNN>/REVIEW-REPORT.md
   ↓
解析"必须改"列表(若空 → 步骤 7 完成)
   ↓
派生任务循环(若有"必须改"→ code-it → code-check)
   ↓
写 fix/<BUG-NNN>/auto-report.md
```

### 2.4 关键架构决策

| 决策 | 选定 | 理由 | 规范依据 |
| --- | --- | --- | --- |
| `code-fix` 状态机 | 前 3 段(报告/调查中/修复规划中)+ 不再推进后续 | "纯登记型"语义,后续推进由 `code-plan` / `code-it` / `code-check` 负责 | `module-conventions.md`(沿用既有缺陷路径分工) |
| `code-auto` 模式 C | 首段匹配 `^BUG-\d{5}$` 进入 BUG 路径 | 与模式 A / B 正则互不冲突;`code-auto` 步骤 1 模式识别表扩展 | `code-auto/SKILL.md` 既有"模式识别"约定 |
| BUG 路径子技能调用 | `code-plan` → `code-it` → `code-unit`(条件) → `code-check` | 复用 REQ 路径的"任务总览 + 执行档案"模式;`code-unit` 沿用 `code-plan` §"项目可测性" | `module-conventions.md` §模块边界 |
| BUG 路径完成报告路径 | `fix/<BUG-NNN>/auto-report.md` | 与 REQ 路径的 `require/<REQ-NNNNN>/auto-report.md` 对称 | `code-auto/SKILL.md` 既有"auto-report.md"约定 |
| `code-check` 身份 | 复用 `code-review` 能力(本仓库 V0.0.3 现状) | REQ-00022 已完成重命名,直接用 `code-check` | (无新增规范) |

## 3. 组件 / 模块拆分

详见 `module-breakdown.md`:
- **修改 1**:`plugins/code-skills/skills/code-fix/SKILL.md`(纯登记型重写)
- **修改 2**:`plugins/code-skills/skills/code-auto/SKILL.md`(模式 C 增加 + BUG 路径子技能调用表)
- **复用**:`code-plan` / `code-it` / `code-unit` / `code-check`(本轮不修改)
- **0 新增**

## 4. 接口与数据结构

本需求**不新增**接口 / 数据结构(纯 SKILL.md 文字重写)。

`fix/<BUG-NNN>/RESULT.md` 模板结构沿用既有,**不**改。

`fix/<BUG-NNN>/auto-report.md` 是**新增**的文件输出路径,但**不**对应任何 SKILL.md 内部数据结构——它是 `code-auto` 步骤 7 的输出。

## 5. 三方依赖

本需求**0 新增**三方依赖。详见 `dependencies.md`。

## 6. 关联概要设计

- **无强关联设计**(本轮聚焦自身 SKILL.md 重写)
- 弱关联:REQ-00022 `code-review` → `code-check` 重命名(本需求依赖此重命名)
- 弱关联:BUG-00001 / BUG-00002 / BUG-00003 现有 BUG 修复全流程(本需求为该全流程的自动化编排)

## 7. 规范遵循

### 7.1 本次参考的规范
- `skill-conventions.md`(SKILL.md frontmatter 必含 name+description)
- `module-conventions.md`(模块边界 / 目录结构)
- `commit-conventions.md`(commit 沿用 `chore(code-fix):` / `chore(code-auto):` 前缀)
- `doc-conventions.md`(README 多语言对仗,本轮不触发)

### 7.2 规范 vs 现状偏离
- 偏离 1:`code-check/SKILL.md` 与 `code-review/SKILL.md` 内容是否完全一致(本需求不修)
- 偏离 2:`code-auto` 模式 C 的子技能调用表与 REQ 路径的相似度(本需求沿用既有模式)

### 7.3 用户授权的偏离
- 无

## 8. 设计不变量 (INV)

- **INV-1**:`code-fix` 仍维护"报告 → 调查中 → 修复规划中"前 3 段状态推进
- **INV-2**:"修复规划中 → 修复编码中 → 已修复-待验证 → 已修复-已验证 → 已关闭"由 `code-plan` / `code-it` / `code-check` 推进
- **INV-3**:`code-fix` 不产出 `fix-plan.md`(沿用 `code-require` 模式)
- **INV-4**:`code-auto` 模式 C 的"任务循环"复用 REQ 路径的"任务总览 + 执行档案"模式
- **INV-5**:`code-auto` 模式 C 的"附加约束"(自动选推荐项)与模式 A / B 一致
- **INV-6**:`code-check` 复用 `code-review` 能力(不新增 marketplace 词条)
- **INV-7**:`code-fix` 不实施代码改动(沿用 `code-require` 模式)
- **INV-8**:`code-fix` 不直接关闭缺陷("已关闭"由 `code-check` 推进后,`code-fix` 复跑时直接确认)

## 9. 待澄清 / 未决项

| 编号 | 项 | 状态 |
| --- | --- | --- |
| Q1 | `code-fix` 步骤 6 "修复方案小节"是否仍保留(指向未来 `code-plan` 产出) | 已决策:保留(链接到 `fix-plan.md`) |
| Q2 | `code-check` SKILL.md 与 `code-review` 内容是否完全等价,还是需要补充 BUG 路径的专项内容 | 已决策:沿用 `code-review` 内容(本需求不修改) |

## 10. 变更记录

- `2026-06-08 15:30` 概要设计完成(4 项决策,8 条不变量)
