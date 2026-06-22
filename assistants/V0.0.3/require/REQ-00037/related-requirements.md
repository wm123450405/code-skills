# 关联需求 — REQ-00037

## REQ-00027 (优化 code-fix 流程 + code-auto BUG 路径,V0.0.3)
- **关联点**:本轮需求是对 REQ-00027 落地的"用户体验改进"。REQ-00027 已把 `code-fix` 改为纯登记型、把 BUG 状态推进的责任交给 `code-plan`/`code-it`/`code-check`,但落地时仍要求用户多次复跑 `code-fix <BUG-NNN>` 来"校验/刷新"状态。本轮需求把"`code-fix` 复跑推进状态"也去掉,改成"由下游技能自动推进"。
- **影响**:本轮**不**修改 `code-fix` 的"前 3 段状态"(`报告 / 调查中`)+ 终态判定(`已关闭-非缺陷 / 已取消`),仅去掉"修复规划中 → 修复编码中 → 已修复-待验证 → 已修复-已验证"的复跑校验/提示步骤;**下游技能(`code-plan` / `code-it` / `code-check`)在状态变更时主动回写 `fix/<BUG-NNN>/RESULT.md` + `fix/RESULT.md` + 看板**。
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00027/RESULT.md` §7.1 / §8.2 状态推进权限表

## BUG-00001 / BUG-00002 / BUG-00003 (V0.0.3 已有 3 个登记缺陷)
- **关联点**:这 3 个缺陷当前是历史登记的样本;**不**直接被本需求修改。
- **影响**:本需求若落地(改完 SKILL.md),这些历史 BUG 的 `fix/<BUG-NNN>/RESULT.md` **不**受影响(本需求只改"未来新流程"中的状态推进归属);但**已存在**的、由 `code-fix` 复跑写入的"修复规划中"等条目**保留**(NFR-3 字节级沿用)。
- **来源**:`./assistants/V0.0.3/fix/` 目录 Glob

## REQ-00022 (code-review → code-check 重命名,V0.0.3)
- **关联点**:本需求改动涉及 `code-check`(缺陷评审/收尾),依赖 REQ-00022 已完成的重命名。
- **影响**:`code-check` 的"缺陷收尾"职责(原 `code-review` 缺陷路径)在 REQ-00022 已落地;本轮仅需修改其"评审完成后 BUG 状态推进"的具体动作。
- **来源**:`./assistants/V0.0.3/require/REQ-00022/RESULT.md`

## REQ-00034 (移除 /code-unit,整合进 /code-it,V0.0.3)
- **关联点**:`code-it` 自含按需写单测(沿用 REQ-00034),意味着 BUG 修复后的单测**不**再由独立 `code-unit` 推动,而是 `code-it` 完成时的副产品。
- **影响**:本轮需求中 "`code-it` 完成后直接标记缺陷为待审查/开发中" 的判定,与 REQ-00034 的"单测整合进 code-it"协同一致 —— 单测在 `code-it` 内部完成,**不**影响"开发完成 → 待审查"的推进逻辑。
- **来源**:`./assistants/V0.0.3/require/REQ-00034/RESULT.md`