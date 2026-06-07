# 改修总结 — TASK-BUG-00001-00005

## 1. 任务信息
- 任务编码:TASK-BUG-00001-00005
- 标题:[修改] code-it 加"唯一可改"声明 + code-unit 加"可改测试代码"边界(2 段合并 1 任务)
- 类型:修改
- 触发/来源:缺陷修复
- 所属缺陷:BUG-00001
- 来源:`fix/BUG-00001/PLAN.md §3.5`
- 设计依据:`fix/BUG-00001/RESULT.md §7.4.5 + §7.4.6`

## 2. 改修内容总览

| 类别 | 文件 | 改动类型 |
| --- | --- | --- |
| 修改 | `plugins/code-skills/skills/code-it/SKILL.md` | 在 `## 目标` 段后新增 `## 唯一允许的生产代码改动场景` 小节 |
| 修改 | `plugins/code-skills/skills/code-unit/SKILL.md` | 在 `## 目标` 段后新增 `## 可改测试代码边界` 小节 |
| 0 新增 | — | — |
| 0 删除 | — | — |

**净变化**:+6 行(2 个文件 × 3 行 = 6 行;标题 + 空行 + 1 行内容)

## 3. 详细改动

### 3.1 `plugins/code-skills/skills/code-it/SKILL.md`

- **目标位置**:`## 目标` 段(line 11-12)与 `## 适用场景` 段(line 18)之间
- **新增内容**(原文):
  > ## 唯一允许的生产代码改动场景
  >
  > 本技能是 `code-skills` 体系中**唯一**被允许修改 `plugins/code-skills/skills/*/SKILL.md` 的技能。`code-require` / `code-design` / `code-plan` / `code-fix` 不得修改这些工程代码;`code-unit` 不得修改生产代码(只能写测试代码)。本技能读 `<版本号>/code/<TASK-...>/` 工作空间文档与 `plan/<REQ>/PLAN.md` 任务清单,逐任务产出 `code/<TASK-...>/RESULT.md` 实施记录。
- **影响范围**:
  - 既有 frontmatter(line 1-4)0 变化 — INV-16 通过
  - 既有 `## 目标` / `## 适用场景` / `## 不适用` / `## 工作目录约定` 等段全部保留
  - 与既有"## 工作目录约定"段中"这是唯一允许的生产代码改动场景"短语(line 58)语义一致,语义不冲突
- **语义影响**:`code-it` 技能"唯一可改 SKILL.md"职责**独立成段**显式声明

### 3.2 `plugins/code-skills/skills/code-unit/SKILL.md`

- **目标位置**:`## 目标` 段(line 8-9)与 `## 适用场景` 段(line 15)之间
- **新增内容**(原文):
  > ## 可改测试代码边界
  >
  > 本技能被允许**仅**修改 CWD 下的测试文件(如 `tests/` / `__tests__/` / `*.test.*` / `*.spec.*`)。**不得**修改 `plugins/code-skills/skills/*/SKILL.md` 或其他生产代码文件;生产代码改动由 `code-it` 唯一实施。本技能产出 `test/<TASK-...>/RESULT.md` 测试记录。
- **影响范围**:
  - 既有 frontmatter(line 1-4)0 变化 — INV-16 通过
  - 既有 `## 目标` / `## 适用场景` / `## 不适用` 等段全部保留
- **语义影响**:`code-unit` 技能"仅可改测试代码"职责**独立成段**显式声明

## 4. 关键决策与权衡

| 决策 | 选择 | 理由 |
| --- | --- | --- |
| 新增位置 | `## 目标` 段后 | 2 段声明本质是"职责边界的核心约束",与"## 目标"段紧邻,语义最连贯 |
| 2 段合并 1 任务 | code-it + code-unit 合并为 T-5 | 2 段存在反向引用(语义耦合),独立任务失去连贯性;沿用 PLAN.md §3.5 拆分 |
| 与既有 line 58 短语的关系 | 并存(独立小节 + 内嵌短语) | 不同粒度(独立声明 vs 工作目录约定),语义一致,可读性更好 |
| frontmatter 保留 | 0 变化 | INV-16 强约束;`skill-conventions §规则 1` 严守 |
| 既有条目保留 | 全部保留,仅追加 2 段 | 不重写稳定章节 |

## 5. 偏离设计 / 规范的地方

**0 偏离**(详 `deviations.md`)

## 6. 验证结果

| 校验 | 命令 | 结果 | 依据 |
| --- | --- | --- | --- |
| INV-14 静态校验 | `grep -n "唯一.*生产代码改动" code-it/SKILL.md` | ✅ 命中 2 行(line 14 + 58) | `fix/BUG-00001/RESULT.md §7.12` |
| INV-15 静态校验 | `grep -n "可改测试代码" code-unit/SKILL.md` | ✅ 命中 1 行(line 11) | `fix/BUG-00001/RESULT.md §7.12` |
| INV-16 frontmatter 字节级保留(2 个文件) | `git diff code-it/SKILL.md code-unit/SKILL.md` | ✅ diff 范围仅 `## 目标` 段后,2 个文件 frontmatter 0 变化 | `skill-conventions §规则 1` |

## 7. 已知问题 / 未完成项

**0 未完成项**。本任务为 BUG-00001 修复的最后一步(T-5)。T-1~T-5 全部实施完成。

## 8. 关联任务与提交

- 关联任务(自查):BUG-00001
- 关联计划:`fix/BUG-00001/PLAN.md`
- 完成时间:2026-06-07 17:54
- git 提交:**待末尾兜底 commit**

## 9. 同步文件清单

| 步骤 | 文件 | 改动 |
| --- | --- | --- |
| 步骤 22 | `plugins/code-skills/skills/code-it/SKILL.md` | 新增 `## 唯一允许的生产代码改动场景` 小节(+3 行) |
| 步骤 22 | `plugins/code-skills/skills/code-unit/SKILL.md` | 新增 `## 可改测试代码边界` 小节(+3 行) |
| 步骤 23 | (静态校验通过,无文件改动) | INV-14 / INV-15 / INV-16 全通过 |
| 步骤 25 | `code/TASK-BUG-00001-00005/{work-log, compile-and-run, test-results, deviations}.md` | 4 份过程文档新写 |
| 步骤 15 (待执行) | 看板任务清单 T-5 行 | 开发状态"待开始"→"已完成" |
| 步骤 15 (待执行) | 看板变更记录 | "任务完成"行追加 |

## 10. 下一步建议

1. **BUG-00001 5 任务全部完成** → 调 `code-fix BUG-00001` 推进状态"修复编码中"→"已修复-待验证"
2. 跑 7 项 INV 静态校验(INV-10~15)+ 1 项回归校验(4 commit 保留)→ 8 项验收清单(7 INV 已通过 T-1~T-5,仅剩回归校验)
3. 验收通过后,调 `code-fix BUG-00001` 推进"已修复-待验证"→"已修复-已验证"→"已关闭"
4. (可选)调 `code-check BUG-00001` 对本修复做正式评审
