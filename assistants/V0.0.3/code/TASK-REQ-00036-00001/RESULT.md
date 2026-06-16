# 任务结果 — TASK-REQ-00036-00001

## 任务信息
- **任务编码**:TASK-REQ-00036-00001
- **任务标题**:扫描并产出 14 技能 SKILL.md + templates/ 待清理文件表与命中计数基线
- **类型**:文档
- **触发/来源**:需求新增
- **需求**:REQ-00036
- **版本**:V0.0.3
- **开始时间**:2026-06-16 17:33
- **完成时间**:2026-06-16 17:33
- **完成人**:用户

## 改修内容总览

本任务**纯只读扫描**,无任何源文件改动。产出:
1. 待清理文件表(47 文件)
2. 6 条清理规则的命中计数基线(总 286 行命中)
3. 范围过滤特例 5 条(已收敛)

## 详细产出

### A. 待清理文件表(47 文件 = 14 SKILL.md + 33 templates)

| 技能 | SKILL.md | templates 数 | templates 文件清单 |
| --- | --- | --- | --- |
| code-answer | ✓ | 0 | — |
| code-auto | ✓ | 0 | — |
| code-check | ✓ | 4 | REVIEW-FIX.md / REVIEW-REPORT.md / assistants-layout.md / process-doc-decisions.md |
| code-dashboard | ✓ | 0 | — |
| code-design | ✓ | 3 | assistants-layout.md / design.md / process-doc-decisions.md |
| code-fix | ✓(R-5 豁免) | 3(R-5 豁免) | assistants-layout.md / bug.md / fix-registry.md |
| code-init | ✓ | 3 | INIT-REPORT.md / assistants-layout.md / existing-requirement.md |
| code-it | ✓ | 3 | RESULT.md / assistants-layout.md / process-doc-dec-decisions.md |
| code-merge | ✓ | 0 | — |
| code-plan | ✓ | 5 | assistants-layout.md / fix-plan.md / plan.md / process-doc-decisions.md / task-plan.md |
| code-publish | ✓ | 5 | DEPLOY.md / Q&A.md / UPDATE.md / assistants-layout.md / qanda-README.md |
| code-require | ✓ | 3 | assistants-layout.md / process-doc-decisions.md / requirements.md |
| code-rule | ✓ | 2 | assistants-layout.md / rule.md |
| code-version | ✓ | 2 | assistants-layout.md / version-RESULT.md |

### B. 6 条规则命中计数基线(全 47 文件)

| 规则 | 描述 | 命中行数 | 命中文件数 | 备注 |
| --- | --- | --- | --- | --- |
| R-1 | 段尾「本需求 REQ/BUG-NNNNN」 | **132** | 11 | 最高频;主要在 6 个 SKILL.md(code-check 13 / code-dashboard 17 / code-auto 14 / code-design 17 / code-require 6 / code-plan 40 / code-it 18)+ 5 个 templates |
| R-2 | 「原 code-unit/fix-plan」回溯 | **4** | 3 | 极少;code-auto 1 / code-check 1 / code-it 2 |
| R-3 | 「Q-N 锁定 / Q-PN 锁定」决策记录 | **29** | 12 | 散布;code-auto 8 / code-require 3 / code-plan 3 / code-it 2 / 等 |
| R-4 | 「YYYY-MM-DD 起生效」标记 | **37** | 9 | 主要在 code-check 5 / code-it 8 / code-plan 13 / code-require 5 |
| R-5 | 退场文件名 `fix-*.md` 引用 | **84** | 6 | 集中(code-fix SKILL.md 20 + code-fix/templates/assistants-layout.md 5 + code-fix/templates/bug.md 6 + code-plan SKILL.md 22 + code-it SKILL.md 28 + code-auto 3);`code-fix` 技能整体豁免 R-5 |
| R-6 | 杂项(自然人名 + 旧版「原 X 位数字」) | **0** | 0 | 设计上为 0;T-2 该规则实际无操作 |
| **合计** | | **286** | | |

### C. 占位符(不应被误清,NFR-6)

`REQ-00001` 字面在 templates/ 中出现 **32 次**,分布在 11 文件。T-2 应用规则时**必须保留**这些字面(它们是模板占位符)。

### D. 范围过滤特例(算法 0)

| 特例 | 处理 |
| --- | --- |
| `checklists/` 子目录 | 排除(FR-7) |
| `guidelines/` 子目录 | 排除(FR-7) |
| `code-unit/` 目录(已退场) | 排除(自然不命中) |
| `code-fix` 技能 SKILL.md + templates/ 中的 R-1 ~ R-4 + R-6 | **应用**(它们也是痕迹) |
| `code-fix` 技能 SKILL.md + templates/ 中的 R-5 | **豁免**(本技能职责范围是 fix/ 目录) |

### E. 文件级命中明细(R-1 ~ R-5 总命中数 ≥ 1 的文件)

```
code-check/SKILL.md                       : R-1=13, R-2=1, R-3=2, R-4=5, R-5=0   (合计 21)
code-dashboard/SKILL.md                   : R-1=17, R-3=0, R-4=1                  (合计 18)
code-auto/SKILL.md                        : R-1=14, R-2=1, R-3=8, R-4=1, R-5=3   (合计 27)
code-check/templates/process-doc-decisions.md: R-1=1                              (合计 1)
code-design/SKILL.md                      : R-1=17, R-3=3, R-4=2                  (合计 22)
code-design/templates/design.md           : R-1=3                               (合计 3)
code-plan/templates/plan.md               : R-1=2, R-3=0, R-4=1                  (合计 3)
code-require/SKILL.md                     : R-1=6, R-3=3, R-4=5                  (合计 14)
code-plan/SKILL.md                        : R-1=40, R-3=3, R-4=13, R-5=22         (合计 78)
code-it/SKILL.md                          : R-1=18, R-2=2, R-3=2, R-4=8, R-5=28  (合计 58)
code-it/templates/RESULT.md               : R-1=1, R-4=1                          (合计 2)
code-fix/SKILL.md                         : R-3=1, R-5=20(R-5 豁免 → 仅记)         (合计 1 after exempt)
code-fix/templates/assistants-layout.md   : R-5=5(R-5 豁免)                      (合计 0)
code-fix/templates/bug.md                 : R-5=6(R-5 豁免)                      (合计 0)
code-version/SKILL.md                     : R-3=2                               (合计 2)
code-publish/SKILL.md                     : R-3=2                               (合计 2)
code-publish/templates/assistants-layout.md: R-3=1                              (合计 1)
code-publish/templates/qanda-README.md    : R-3=1                               (合计 1)
code-merge/SKILL.md                       : R-3=1                               (合计 1)
```

> 说明:code-fix 技能 R-5 命中 31 行(20 + 5 + 6),但按豁免规则 T-2 不应用 R-5。其他 5 条规则在 code-fix 上的命中仍要清理。

## 关键决策与权衡

1. **文件计数修正**:PLAN.md 估算 37(14 SKILL.md + 23 templates),实盘 47(14 SKILL.md + 33 templates)。修正已同步到 PLAN.md + 看板。
2. **R-6 实际为 0 命中**:设计上 R-6 是个兜底规则(自然人名 + 旧版「原 X 位数字」),实盘无任何命中。T-2 该规则无操作,但仍按规则顺序跑一遍(以防被新文件引入)。
3. **code-fix 技能 R-5 豁免**:R-5 命中集中在 code-fix 自身(31 行 = 20 SKILL.md + 5 + 6 templates),但因本技能职责范围是 fix/ 目录,豁免 R-5;R-1 ~ R-4 + R-6 仍正常清理。
4. **占位符 32 命中**:仅 `REQ-00001`,分布在 11 文件的 templates/ 中。T-2 应用规则时需保证这些占位符不被任何规则误伤。

## 偏离设计/规范的地方

无(本任务纯扫描,0 文件改动)。

## 验证结果

- 扫描:完成
- 命中计数:完成(286 总命中)
- 文件表:完成(47 文件)
- 范围过滤:验证(无 checklists/guidelines/code-unit 命中)

## 已知问题/未完成项

- 偏差已修正到 PLAN.md + 看板(文件数 37 → 47)
- 无未完成项

## 关联任务与提交

- 提交哈希:无(本任务无代码改动,暂不 commit)
- 关联任务:—
- 下游:TASK-REQ-00036-00002(应用规则,直接消费本任务的命中基线)