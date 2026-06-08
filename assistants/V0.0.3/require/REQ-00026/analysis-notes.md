# 分析笔记 — REQ-00026

## 当前理解的疑点
1. "描述性段落" vs "硬约束段落"的边界,需要 grep 后逐句判断。
   - 已通过 `Grep "plugins/code-skills" -l` 找到 10 个 SKILL.md + 3 个模板的命中点。
   - 需在 `code-plan` / `code-it` 阶段逐条扫除。

## 候选方案权衡
- **方案 A:全部替换为 `<本仓库>`**(用户已选,推荐):彻底去专属,但可能在硬约束段落(如"`code-it` 不修改 `plugins/code-skills/skills/*/SKILL.md`")引入模糊
- **方案 B:仅改描述性段落,硬约束保留字面**(已锁定):保留字面以保可追溯,代价是"半改半留"
- 决策:**B** + "如某硬约束明显是描述性而非约束性,可一并改"(`code-rule` L336 就是这种)

## 临时假设
- 假设 1:`./assistants/` 路径在所有 10 个 SKILL.md 中保持原样(用户 Q4 已确认)
- 假设 2:`marketplace.json` / `plugin.json` / 旧需求档案 0 改动
- 假设 3:本需求不重写 SKILL.md,只做"局部 Edit"扫除

## 下一轮要深挖的方向
- `code-plan` 阶段:列出每条 Edit 的 file:line 范围,逐条确认"是否在描述性段落"
- `code-it` 阶段:逐条 Edit,每条 Edit 后跑 `git diff --stat` 校验 AC-1 / AC-2
- `code-check` 阶段:重点查"半改半留"是否一致
