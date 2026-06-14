# 设计笔记 — REQ-00027
更新时间:2026-06-08 15:30

## 关键设计问题

### Q1:`code-fix` 状态机收敛范围
- 候选状态:报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞
- 移出"修复规划中 / 修复编码中 / 已修复-待验证 / 已修复-已验证 / 已关闭"——这些推进由 `code-plan` / `code-it` / `code-check` 负责
- 仍保留"修复规划中"在候选中:用户调 `code-fix` 复跑时,如果 BUG 状态是"修复规划中"且需校验,`code-fix` 可**校验但不主动推进**——这是 NFR-2 状态推进路径一致性的细节

### Q2:`code-auto` BUG 路径的"任务循环"如何复用 REQ 路径
- 复用 `code-auto` 步骤 4 的"任务总览" + "执行档案"模式
- 关键差异:BUG 路径的"任务清单"是 `code-plan` 产出的 `fix-plan.md`(简化版,无 PLAN.md 任务列表)
- 路径:`fix/<BUG-NNN>/` 而非 `plan/<REQ-NNNNN>/` 与 `code/<TASK-...>/`

### Q3:`code-check` 与 `code-review` 内容一致性
- 本仓库 V0.0.3 现状:`plugins/code-skills/skills/code-check/SKILL.md` 存在(目录已建),但 `code-review/SKILL.md` 仍存在(SKILL.md 改名未完成)
- 沿用 `code-review` 能力,本需求不强制 SKILL.md 内容统一(由后续需求处理)

### Q4:`code-auto` 模式 C 的"附加约束"如何复用
- 沿用 REQ 路径的"`AskUserQuestion` 自动选推荐项"约束(本仓库已具备)
- BUG 路径的"必须改"列表解析与 REQ 路径一致

## 候选方案权衡

### 方案 A(选定):纯登记型 code-fix + code-auto 增加模式 C
- 优点:职责清晰;code-fix 与 `code-require` 模式对称;code-auto 一次串行 4 个子技能
- 缺点:本轮工作量较大(2 个 SKILL.md 重写)

### 方案 B(否决):code-fix 仍负责部分状态推进
- 优点:改动面小
- 缺点:违反"纯登记型"诉求

### 方案 C(否决):code-auto 用新增独立 BUG 路径子技能表
- 优点:不与 REQ 路径混用
- 缺点:增加技能数量,违反"零修改 9 个子技能 SKILL.md"原则

## 选定方案

**方案 A**:纯登记型 code-fix + code-auto 增加模式 C。

理由:
- 直接对应用户原话"code-fix 只登记并分析缺陷(类似 code-require)"
- code-auto 模式识别表扩展与 REQ 路径正则互不冲突
- 与本仓库"零修改 9 个子技能 SKILL.md"原则相符(本轮只改 code-fix + code-auto)

## 假设

- **假设 1**:`code-plan` / `code-it` / `code-unit` / `code-check` 的核心 SKILL.md 行为不变
- **假设 2**:BUG 路径的"任务循环"通过 `code-plan` 产出的 `fix-plan.md` 步骤列表实现(沿用 `code-plan` 缺陷分支)
- **假设 3**:`code-check` 复用 `code-review` 能力(本仓库 V0.0.3 现状)
- **假设 4**:用户对 `code-fix` 的"修复规划中"状态可由 `code-fix` 自身推进(用户调 `code-fix` 复跑时显式确认)

## 风险

- **风险 1**:`code-fix` 状态机收敛后,某些遗留的"已修复-待验证"等状态无法被 `code-fix` 推进——**缓解**:由 `code-it` / `code-check` 推进
- **风险 2**:`code-auto` 模式 C 与模式 A / B 边界要清晰(正则互不冲突,已校验)
- **风险 3**:`code-check` SKILL.md 与 `code-review` 不一致时,BUG 路径评审可能输出与 REQ 路径不同——**不修复**,留待后续

## 下一轮要深挖

- `code-check/SKILL.md` 内容与 `code-review/SKILL.md` 是否完全一致(本需求不修)
- BUG 路径的 `auto-report.md` 路径格式是否与 REQ 路径有差异(已在本需求中明确)
