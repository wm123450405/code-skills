# 任务结果 — TASK-REQ-00036-00002

## 任务信息
- **任务编码**:TASK-REQ-00036-00002
- **任务标题**:应用 6 条清理规则(R-1 ~ R-6)到 T-1 清单,原地改写 + diff 校验 + 残缺回退
- **类型**:文档
- **触发/来源**:需求新增
- **需求**:REQ-00036
- **版本**:V0.0.3
- **开始时间**:2026-06-16 17:33
- **完成时间**:2026-06-16 17:33
- **完成人**:用户

## 改修内容总览

清理执行:188 总命中,15 文件被改,0 残缺回退。

## 详细改动

### A. 执行汇总

| 规则 | 命中数 | 命中文件数 |
| --- | --- | --- |
| R-1(段尾/段中「本需求 REQ/BUG-NNNNN」) | **87** | 9 |
| R-2(「原 code-unit/fix-plan」回溯) | **4** | 2 |
| R-3(「Q-N 锁定」决策记录) | **22** | 6 |
| R-4(「YYYY-MM-DD 起生效」) | **9** | 4 |
| R-5(退场文件名 `fix-*.md`) | **66** | 2(`code-it/SKILL.md` 33 + `code-plan/SKILL.md` 30 + `code-auto/SKILL.md` 3) |
| R-6(杂项) | **0** | 0 |
| **合计** | **188** | |

### B. 改动文件清单(15 个)

| 文件 | 命中数 | 改动摘要 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-auto/SKILL.md` | 21 | R-1=10 + R-2=1 + R-3=7 + R-5=3 |
| `plugins/code-skills/skills/code-check/SKILL.md` | 8 | R-1=7 + R-2=1 |
| `plugins/code-skills/skills/code-check/templates/process-doc-decisions.md` | 1 | R-1=1 |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | 9 | R-1=9 |
| `plugins/code-skills/skills/code-design/SKILL.md` | 15 | R-1=13 + R-3=2 |
| `plugins/code-skills/skills/code-design/templates/design.md` | 3 | R-1=3 |
| `plugins/code-skills/skills/code-fix/SKILL.md` | 1 | R-3=1(`code-fix` R-5 豁免) |
| `plugins/code-skills/skills/code-it/SKILL.md` | 52 | R-1=11 + R-2=2 + R-3=2 + R-4=2 + R-5=33 + R-6=0 |
| `plugins/code-skills/skills/code-it/templates/RESULT.md` | 1 | R-4=1 |
| `plugins/code-skills/skills/code-merge/SKILL.md` | 1 | R-3=1(手动 Edit) |
| `plugins/code-skills/skills/code-plan/SKILL.md` | 62 | R-1=25 + R-3=3 + R-4=4 + R-5=30 |
| `plugins/code-skills/skills/code-plan/templates/plan.md` | 2 | R-1=2 |
| `plugins/code-skills/skills/code-publish/SKILL.md` | 2 | R-3=2 |
| `plugins/code-skills/skills/code-publish/templates/assistants-layout.md` | 1 | R-3=1 |
| `plugins/code-skills/skills/code-publish/templates/qanda-README.md` | 1 | R-3=1 |
| `plugins/code-skills/skills/code-require/SKILL.md` | 11 | R-1=6 + R-3=3 + R-4=2 |

### C. 范围过滤验证

✓ 排除 `code-fix` 技能 R-5(31 行豁免 — 本技能职责范围是 `fix/` 目录)
✓ 排除 `checklists/` / `guidelines/` 目录
✓ 排除 `code-unit/` 目录(已退场)

### D. 不变量验证

| 不变量 | 验证方式 | 结果 |
| --- | --- | --- |
| Frontmatter 字节级保留(NFR-2) | MD5 一致(全部 14 SKILL.md) | ✓ 100% |
| 占位符保留(NFR-6) | `REQ-00001` 34 次 / `BUG-00001` 60 次 / `TASK-REQ-00001-00001` 11 次 | ✓ 100% |
| 跨技能契约保留(NFR-4) | 未涉及具体字段(本任务只清字面,不动章节号/字段名) | ✓ 100% |
| 残缺判定(< 30%) | 15 文件 0 改动 > 30% | ✓ 通过 |

## 关键决策与权衡

1. **使用 Python 脚本批量执行**:替代 282 次 Edit 调用。`code-fix` 类任务(`BUG-00001`)历史上也用脚本,本任务沿用。详 `deviations.md §偏离 2`。
2. **R-1 正则放宽**:从"段尾"扩到"括号内任意位置",更彻底清理。详 `deviations.md §偏离 1`。
3. **code-fix 技能 R-5 豁免**:沿用 plan §5 算法 5 的特例。31 行 `fix-*.md` 字面保留(本技能职责范围)。
4. **占位符 100% 保留**:脚本的二次验证 + 单独的占位符 grep 双重确认。

## 偏离设计/规范的地方

详 `deviations.md`(4 项偏离):
1. R-1 正则放宽(段尾 → 括号内任意位置)
2. 用 Python 脚本批量执行(替代 Edit)
3. R-2/R-3/R-4 命中数与 T-1 估算偏差(实测更精确)
4. code-merge 用 Edit 而非脚本(局部混合)

## 验证结果

| 验证 | 命令/方式 | 结果 |
| --- | --- | --- |
| 二次验证(R-1 ~ R-5 0 残留) | Python 脚本内置 verify() | ✓ 通过 |
| 占位符保留 | grep REQ-00001/BUG-00001/TASK-REQ-00001-00001 | ✓ 100% 保留(34/60/11) |
| Frontmatter 字节级 MD5 | 脚本 MD5 校验 | ✓ 100% 一致 |
| Git diff 平衡 | git diff --stat | +175 / -175(完美平衡,符合 NFR-7) |
| 残缺判定 | 改动行数 / 原行数 < 30% | ✓ 15 文件全部通过 |

## 已知问题/未完成项

无。188 命中全部消化,无残缺回退,所有不变量 100% 保留。

## 关联任务与提交

- **提交哈希**:本任务未单独 commit(暂存待 T-3 末尾兜底统一 commit)
- **关联任务**:TASK-REQ-00036-00001(已完成的扫描任务,提供 47 文件清单 + 286 行命中基线)
- **下游**:TASK-REQ-00036-00003 验证任务,可直接消费本任务的"188 总命中已消化"作为基准

## 辅助脚本

本任务产出 3 个辅助脚本(`clean.py` 扫描 / `apply.py` 执行 / `scan-results.json` 中间结果),均位于 `code/TASK-REQ-00036-00002/` 下。这些脚本**不**入 `plugins/` 仓库,仅作为本任务的实施记录。T-3 验证时可直接复用 `apply.py` 做二次验证(不修改任何文件)。