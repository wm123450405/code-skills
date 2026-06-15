# 关联需求 — REQ-00033

版本:V0.0.3
需求编码:REQ-00033
更新时间:2026-06-15 11:10

## REQ-00032 (code-require 步骤 10A/10B 末尾追加下一步建议段,V0.0.3)

- **关联点**:同属 `code-require/SKILL.md` 增量改造;两需求都只在末尾追加段,不动既有结构
- **影响**:本需求追加位置应**避开** REQ-00032 已占用的"步骤 10A / 10B 末尾"锚点,改在 §"目标" 段或 §"工作流程 → 步骤 5A / 步骤 8A" 段内
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00032/RESULT.md` §4 FR-3 / §11 关联需求 / §13 变更记录
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00032/materials-index.md` §3.5

## BUG-00001 (code-require / code-design / code-plan / code-fix 加"不修改 SKILL.md"硬约束,V0.0.3)

- **关联点**:同属"技能职责边界显式化"型需求,范式 = 在 SKILL.md §"不要做的事" 小节加硬约束
- **影响**:本需求追加的硬约束**优先**沿用 BUG-00001 范式(在 §"不要做的事"小节追加 1 条),**不**复制粘贴措辞(避免与"不修改 SKILL.md"语义混淆)
- **来源**:扫描 `./assistants/V0.0.3/fix/BUG-00001/RESULT.md`

## REQ-00026 (SKILL.md 描述通用化扫除,V0.0.3)

- **关联点**:同属"SKILL.md 描述性段落调整"型需求;最小化变更原则 + 字节级保留既有段落
- **影响**:本需求追加"## 不涉及技术选型"段,净增行数估算 +5 ~ +10 行(沿用 REQ-00026 NFR-6 风格)
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00026/RESULT.md` §5 NFR

## REQ-00030 (code-design 与 code-plan 职责分离,V0.0.3)

- **关联点**:上游把"概设只做概设,详设开始做详设"职责分离落到 SKILL.md;本需求在 `code-require` 端做"对偶"的边界显式化
- **影响**:沿用 INV 字节级保留约束(INV-1 ~ INV-10)
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00030/RESULT.md` §5 NFR-1

## REQ-00031 (优化 /code-plan 任务粒度,V0.0.3)

- **关联点**:元技能改规则;本需求不涉及任务粒度,但 INV 字节级保留约束沿用
- **影响**:不涉及 /code-unit(Q-4 沿用 REQ-00031 元技能改规则)
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00031/RESULT.md` §4 FR-1 ~ FR-7

## (本需求不跨版本扫描)

按 code-require 步骤 6A 约定,跨版本扫描**可选**。本需求范围窄(只在 V0.0.3 当前激活版本内显式化 `code-require` 边界),不跨版本扫描以避免噪音。

## 关联点汇总

| 维度 | 关联点 |
| --- | --- |
| 范式(职责边界显式化) | BUG-00001, REQ-00026, REQ-00030, REQ-00032 |
| 元技能改规则 | REQ-00031 |
| 字节级保留约束 | REQ-00030, REQ-00032 |
| 技能分工 | `code-require`(不涉及) ↔ `code-design`(涉及) |
