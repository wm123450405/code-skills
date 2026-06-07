# 改修总结 — TASK-BUG-00001-00003

## 1. 任务信息
- 任务编码:TASK-BUG-00001-00003
- 标题:[修改] code-plan 加"不修改 SKILL.md"硬约束
- 类型:修改
- 触发/来源:缺陷修复
- 所属缺陷:BUG-00001
- 来源:`fix/BUG-00001/PLAN.md §3.3`
- 设计依据:`fix/BUG-00001/RESULT.md §7.4.3`(模块详细化 — 6.4.3 code-plan 段)

## 2. 改修内容总览

| 类别 | 文件 | 改动类型 |
| --- | --- | --- |
| 修改 | `plugins/code-skills/skills/code-plan/SKILL.md` | 在 `## 不要做的事` 段首插入 1 条新条目 |
| 0 新增 | — | — |
| 0 删除 | — | — |

**净变化**:`+1 行`(1 条新条目,约 95 字符;原条目全部保留)

## 3. 详细改动

### 3.1 `plugins/code-skills/skills/code-plan/SKILL.md`

- **目标位置**:`## 不要做的事` 段(line 1086)段首插入
- **新增内容**(原文):
  > - 不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件(工程代码改动由 `code-it` 实施,本技能只写 `plan/<REQ>/RESULT.md` / `PLAN.md` 等工作空间文档)
- **影响范围**:
  - 既有 frontmatter(line 1-4)0 变化 — INV-16 通过
  - 既有"不要做的事"条目 + "缺陷分支额外禁止"子段全部保留
  - 既有其他章节(`## 工作流程` / `## 工具使用约定` / `## 衔接` 等)0 变化
- **语义影响**:`code-plan` 技能边界明确化 — 不再修改工程代码(本仓库 SKILL.md),只能写 `plan/<REQ>/` 工作空间文档;与 BUG-00001 §1.2 期望行为一致

## 4. 关键决策与权衡

| 决策 | 选择 | 理由 |
| --- | --- | --- |
| 段首插入位置 | 在 line 1086 标题与 line 1087 原第一个条目之间 | PLAN.md §3.3 明确"段首";新条目享有最高阅读优先级 |
| 文案措辞 | "不修改 X"陈述句(沿用 T-1/T-2 风格) | 4 个技能(T-1~T-4)统一硬约束风格;陈述句约束力更强 |
| 文案具体性 | 列出 2 个工作空间文档(`RESULT.md` + `PLAN.md`) | `code-plan` 实际产 2 文件,文案需诚实反映 |
| frontmatter 保留 | 0 变化 | INV-16 强约束;`skill-conventions §规则 1` 严守 |
| 既有条目保留 | 全部保留,仅追加 1 条 | 不重写稳定章节 |

## 5. 偏离设计 / 规范的地方

**0 偏离**(详 `deviations.md`)

## 6. 验证结果

| 校验 | 命令 | 结果 | 依据 |
| --- | --- | --- | --- |
| INV-12 静态校验 | `grep -n "不修改.*SKILL.md" plugins/code-skills/skills/code-plan/SKILL.md` | ✅ 命中 1 行(line 1087) | `fix/BUG-00001/RESULT.md §7.12` |
| INV-16 frontmatter 字节级保留 | `git diff plugins/code-skills/skills/code-plan/SKILL.md` | ✅ diff 范围仅 `## 不要做的事` 段,frontmatter 0 变化 | `skill-conventions §规则 1` |

## 7. 已知问题 / 未完成项

**0 未完成项**。本任务为 BUG-00001 修复的第 3 步,后续 T-4~T-5 由独立任务实施。

## 8. 关联任务与提交

- 关联任务(自查):BUG-00001
- 关联计划:`fix/BUG-00001/PLAN.md`
- 完成时间:2026-06-07 17:41
- git 提交:**待末尾兜底 commit**

## 9. 同步文件清单

| 步骤 | 文件 | 改动 |
| --- | --- | --- |
| 步骤 22 | `plugins/code-skills/skills/code-plan/SKILL.md` | 段首插入 1 条新条目(+1 行) |
| 步骤 23 | (静态校验通过,无文件改动) | INV-12 / INV-16 全通过 |
| 步骤 25 | `code/TASK-BUG-00001-00003/{work-log, compile-and-run, test-results, deviations}.md` | 4 份过程文档新写 |
| 步骤 15 (待执行) | 看板任务清单 T-3 行 | 开发状态"待开始"→"已完成" |
| 步骤 15 (待执行) | 看板变更记录 | "任务完成"行追加 |

## 10. 下一步建议

1. 继续实施 TASK-BUG-00001-00004(`code-fix` 加硬约束)— 用户手动调 `code-it TASK-BUG-00001-00004`
2. 实施 TASK-BUG-00001-00005(`code-it` + `code-unit` 声明,合并 1 任务)
3. T-1~T-5 全部完成 → 调 `code-fix BUG-00001` 推进状态
4. 跑 7 项 INV 静态校验(INV-10~15) + 1 项回归校验(4 commit 保留)→ 8 项验收清单
5. 验收通过后,调 `code-fix BUG-00001` 推进至"已关闭"
