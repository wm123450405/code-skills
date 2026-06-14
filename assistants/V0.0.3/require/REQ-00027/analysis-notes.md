# 分析笔记 — REQ-00027
更新时间:2026-06-08 15:20

## 关键设计决策

### Q1:`code-fix` 状态机收敛范围
- 候选状态:报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞
- 移出"修复规划中 / 修复编码中 / 已修复-待验证 / 已修复-已验证 / 已关闭"——这些推进由 `code-plan` / `code-it` / `code-check` 负责

### Q2:`code-auto` BUG 路径的"任务循环"如何复用 REQ 路径
- 复用 `code-auto` 步骤 4 的"任务总览" + "执行档案"模式
- 关键差异:BUG 路径的"任务清单"是 `code-plan` 产出的 `fix-plan.md`(简化版,无 PLAN.md 任务列表)
- 路径:`fix/<BUG-NNN>/` 而非 `plan/<REQ-NNNNN>/` 与 `code/<TASK-...>/`

### Q3:`code-check` 与 `code-review` 内容一致性
- 本仓库 V0.0.3 现状:`plugins/code-skills/skills/code-check/SKILL.md` 存在(目录已建),但 `code-review/SKILL.md` 仍存在(SKILL.md 改名未完成)
- 沿用 `code-review` 能力,本需求不强制 SKILL.md 内容统一(由后续需求处理)

## 假设

- **假设 1**:`code-plan` / `code-it` / `code-unit` / `code-check` 的核心 SKILL.md 行为不变
- **假设 2**:BUUG 路径的"任务循环"通过 `code-plan` 产出的 `fix-plan.md` 步骤列表实现(沿用 `code-plan` 缺陷分支)
- **假设 3**:`code-check` 复用 `code-review` 能力(本仓库 V0.0.3 现状)

## 风险

- **风险 1**:`code-auto` 模式 C 与模式 A / B 的边界要清晰(正则互不冲突,已校验)
- **风险 2**:`code-check` 内容与 `code-review` 不一致时,BUG 路径评审可能输出与 REQ 路径不同——本需求不修复,留待后续

## 下一轮要深挖

- `code-check/SKILL.md` 内容与 `code-review/SKILL.md` 是否完全一致(本需求不修)
- BUG 路径的 `auto-report.md` 路径格式是否与 REQ 路径有差异(已在本需求中明确)
