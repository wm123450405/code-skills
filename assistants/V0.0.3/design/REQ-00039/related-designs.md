# 关联概要设计 — REQ-00039

更新时间:2026-06-22 14:30
版本:V0.0.3

## REQ-00038(优化 /code-it 技能单测判定从工程粒度细化到模块粒度,V0.0.3,已落地初步)

- **关联点**:
 - REQ-00038 改造 `code-it` 步骤 8a / 8.5(模块级单测判定)
 - 本需求改造 `code-it` 步骤 8 末尾(`calcLogicLoc`)
 - 两者协同:`code-it` 步骤 8 = 实施开发 + `calcLogicLoc` → 步骤 8a = 模块级守卫 → 步骤 8.5 = 模块级单测
- **影响**:
 - `code-it/SKILL.md` 在 REQ-00038 落地后,既有"## 步骤 8"末尾追加本需求的 `calcLogicLoc` 子步骤
 - 字面顺序:`## 步骤 8 实施开发` → `calcLogicLoc`(本需求新增,line 1170+ 末尾) → `## 步骤 8a 项目可测性守卫`(REQ-00038 改造)
- **版本协调**:本需求与 REQ-00038 均为 V0.0.3 需求,同版本内并行
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00038/RESULT.md` line 130-150(FR-3)

## REQ-00037(优化 /code-fix 技能及整个缺陷修复流程的状态推进,V0.0.3,已落地完成)

- **关联点**:
 - REQ-00037 在 `code-fix` / `code-plan` / `code-it` / `code-check` 落地 5 处 `*StateRollback` 子步骤
 - 本需求**不**涉及缺陷路径(沿用既有 `code-it` §缺陷分支 17-25)
- **影响**:
 - 缺陷路径(任务编码 `TASK-BUG-...`)**不**走本需求的 `calcLogicLoc` 子步骤(NFR-8)
 - 任务路径(任务编码 `TASK-REQ-...`)走本需求的 `calcLogicLoc` 子步骤
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00037/RESULT.md` §FR-3

## REQ-00034(移除 /code-unit 技能,能力整合进 /code-it,V0.0.3,已落地完成)

- **关联点**:
 - REQ-00034 在 `code-it` 步骤 8a / 8.5 落地"项目可测性守卫 7 项" + "按需写单测"
 - 本需求**不**涉及单测逻辑(沿用 REQ-00034 既有 7 项检查 + 3 类任务判定)
- **影响**:
 - `code-it/SKILL.md` 步骤 8a / 8.5 字面字节级保留
 - 本需求仅在步骤 8 末尾新增 `calcLogicLoc` 子步骤,**不**与 REQ-00034 冲突
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00034/RESULT.md` line 92-130(FR-2 / FR-3)

## REQ-00022(`code-review` → `code-check` 重命名,V0.0.3,已落地完成)

- **关联点**:
 - 本需求改造 `code-check/SKILL.md`(原 `code-review`)
 - 评审维度速查表新增第 13 维度"代码行数超标",与既有 12 维度协同
- **影响**:
 - `code-check/SKILL.md` 步骤 8.13 派生发现 → 走既有 8.1 ~ 8.12 子步骤同构的派生发现清单格式
 - 评审维度速查表(line 574-589)既有 12 维度字节级保留,仅追加第 13 维度
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00022/RESULT.md`(仅关联,未读全文)

## 关联需求所在版本

- 全部位于 V0.0.3
- 不涉及跨版本关联(沿用既有 V0.0.3 内部版本空间)