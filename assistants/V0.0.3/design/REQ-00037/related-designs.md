# 关联设计 — REQ-00037

更新时间:2026-06-22 09:18
版本:V0.0.3

## REQ-00027 (优化 code-fix 流程 + code-auto BUG 路径,V0.0.3)

- **关联点**:本轮需求是对 REQ-00027 落地的"用户体验改进"。
- **影响**:
  - REQ-00027 把 `code-fix` 改为纯登记型 + 下游接力(`code-plan` → `code-it` → `code-check`);本轮把"状态推进"职责从 `code-fix` 复跑转为下游技能自动推进
  - 本轮**不**修改 `code-fix` 的"前 5 段状态"职责(报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞),仅收敛其"修复规划中及之后"的状态推进边界
- **来源**:扫描 `./assistants/V0.0.3/design/REQ-00027/RESULT.md`

## REQ-00022 (code-review → code-check 重命名,V0.0.3)

- **关联点**:本轮 FR-5 扩展 `code-check` 接受 BUG-NNN 入参,依赖此重命名。
- **影响**:
  - `code-check` 已是统一技能名(原 `code-review`)
  - 本轮在 `code-check` 步骤 1 增加"BUG-NNN 识别"分支
- **来源**:扫描 `./assistants/V0.0.3/design/REQ-00022/RESULT.md`

## REQ-00034 (移除 code-unit,整合进 code-it,V0.0.3)

- **关联点**:`code-it` 自含按需写单测(沿用 REQ-00034)。
- **影响**:
  - 本轮 FR-3 / FR-4 在 `code-it` 步骤 21 / 24 末尾追加"状态回写"动作,与 REQ-00034 的"单测整合进 code-it"协同一致
  - 单测在 `code-it` 步骤 8.5 内部完成,**不**影响"开发完成 → 待审查"的推进逻辑
- **来源**:扫描 `./assistants/V0.0.3/design/REQ-00034/RESULT.md`

## REQ-00036 (清理 SKILL.md + templates/ 中的开发痕迹,V0.0.3)

- **关联点**:本轮落地后的 SKILL.md 仍按 REQ-00036 的清理标准。
- **影响**:
  - 本轮**新写**的 SKILL.md 段落(FR-8 典型完整流程举例 / FR-6 状态推进表新增行)**不**引入开发痕迹
  - 与 REQ-00036 保持兼容:本轮的"状态推进规则"用"当前事实"陈述,不写"本需求 REQ-00037 新增"类尾注
- **来源**:扫描 `./assistants/V0.0.3/design/REQ-00036/RESULT.md`

## BUG-00001 / 02 / 03 (V0.0.3 已有 3 个登记缺陷)

- **关联点**:这 3 个历史 BUG 维持原状态字面(沿用 NFR-3)。
- **影响**:
  - 本轮**不**修改 `fix/<BUG-NNN>/RESULT.md` 中"状态"字段
  - 本轮**不**写迁移工具
- **来源**:`./assistants/V0.0.3/fix/` 目录 Glob
