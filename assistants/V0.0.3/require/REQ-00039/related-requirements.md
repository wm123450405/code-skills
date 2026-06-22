# 关联需求 — REQ-00039

## REQ-00038(优化 /code-it 技能单测判定从工程粒度细化到模块粒度,所属版本 V0.0.3)

- **关联点**:
 - REQ-00038 在 `code-it` 步骤 8a / 8.5 落地了"模块级"判定(模块识别 + 守卫 + 单测输出)
 - 本需求 REQ-00039 在 `code-it` 步骤 8 末尾追加"逻辑行 metadata",**不**与 REQ-00038 冲突(不同位置)
 - 两者协同:`code-it` 步骤 8 = 实施开发 + 逻辑行 metadata → 步骤 8a = 模块级守卫 → 步骤 8.5 = 模块级单测
- **影响**:
 - REQ-00038 落地后:`code-it` 步骤 8a / 8.5 是模块级
 - 本需求落地后:`code-it` 步骤 8 末尾追加 `calcLogicLoc` 子步骤(模块级 / 整工程级 双模式)
 - 模块级 + 整工程级 = 完整逻辑行 metadata
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00038/RESULT.md` line 130-150(FR-3 字面)

## REQ-00037(优化 /code-fix 技能及整个缺陷修复流程的状态推进,所属版本 V0.0.3)

- **关联点**:
 - REQ-00037 在 `code-fix` / `code-plan` / `code-it` / `code-check` 落地了"5 处 *StateRollback"子步骤
 - 本需求**不**涉及缺陷路径(沿用既有 `code-it` §缺陷分支 17-25)
- **影响**:
 - 缺陷路径(任务编码 `TASK-BUG-...`)**不**走本需求的 `calcLogicLoc` 子步骤
 - 任务路径(任务编码 `TASK-REQ-...`)走本需求的 `calcLogicLoc` 子步骤
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00037/RESULT.md` §FR-3 关键变更

## 关联需求所在版本

- 全部位于 V0.0.3
- 不涉及跨版本关联(沿用既有 V0.0.3 内部版本空间)