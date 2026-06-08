# 风险分析 — REQ-00027
更新时间:2026-06-08 15:35
版本:V0.0.3

## 异常处理
- 异常路径 1:`code-fix` 复跑时,BUG 状态是"修复规划中"或之后,`code-fix` 仍可读取但不主动推进
  - 处理:`code-fix` 步骤 9 引导建议明确提示用户调 `code-plan` / `code-it` / `code-check`
- 异常路径 2:`code-auto` 模式 C 错配(例如 args 含 `BUG-00001-00001` 而非 `BUG-00001`)
  - 处理:模式识别正则 `^BUG-\\d{5}$` 拒绝,提示格式错误
- 异常路径 3:`code-check` 缺失(本仓库 V0.0.3 现状 SKILL.md 改名未完成)
  - 处理:沿用既有"`fix/<BUG-NNN>/RESULT.md` 缺失 → 提示先调 `code-fix`" 模式

## 安全边界
- 鉴权要求:N/A(本仓库 0 鉴权)
- 输入校验:模式识别正则严格匹配
- 敏感数据处理:N/A
- 审计日志:commit message 含任务编号

## 性能与资源
- 关键路径预估:0 改代码,仅改 SKILL.md 文字
- 资源限制:本仓库 0 性能要求
- 缓存策略:N/A

## 回退策略
- 触发条件:`code-check` 校验发现本轮改动破坏既有功能
- 步骤:`git revert` 本轮 commit → 重跑 `code-plan REQ-00027` 重新规划
- 验证:重跑 `code-fix BUG-00001` 端到端校验(沿用既有流程)

## 测试要点
- 单元:N/A(本轮 0 改代码,无单测)
- 集成:N/A
- 端到端:`code-fix` 人工调 → 校验只产出 `fix/BUG-NNN/RESULT.md` 不产出 `fix-plan.md`;`code-auto BUG-NNN` 人工调 → 校验自动编排 7 步子技能
- 性能/安全:N/A
