# 规范遵循记录 — REQ-00010

更新时间:2026-06-06 12:10
版本:V0.0.2
需求编码:REQ-00010

## 1. 本次参考的规范文件

(同 `design/.../rule-compliance.md §1`,本计划延用)

## 2. 规范 vs 现状偏离
**无**(沿用概要设计结论)

## 3. 规范 vs 需求冲突
**无**

## 4. 用户授权的偏离
**无**

## 5. 关键约束条款遵循清单(13 项 INV)

| INV# | 条款 | 来源 | 验证方式 | T-001 实施 | T-002 自检 |
| --- | --- | --- | --- | --- | --- |
| **INV-1** | `code-it/SKILL.md` frontmatter L1-3 字节级保留 | `skill-conventions §规则 1` + NFR-7 | `head -3 SKILL.md` 输出原 frontmatter 完整 | 锚点 A 在 frontmatter 之后插入(沿用 REQ-00013 模式) | `git diff SKILL.md` 验证 frontmatter 无 - 行 |
| **INV-2** | `code-it/SKILL.md` §"工作流程"步骤 0~16 内容不变 | FR-3.AC-3.1 + NFR-3 | 既有步骤 0~16 字符串精确匹配 | 不重写既有章节,仅在步骤 0 前插入步骤 0a | `git diff SKILL.md` 既有步骤 0~16 0 改动 |
| **INV-3** | `code-it/SKILL.md` §"缺陷分支"步骤 17~25 内容不变 | FR-4.AC-4.1 | 既有步骤 17~25 字符串精确匹配 | 不修改缺陷分支 | `git diff SKILL.md` 步骤 17~25 0 改动 |
| **INV-4** | `code-it/SKILL.md` §"标题解析(REQ-00013 新增)" 小节不变 | 锚点参照 | 既有"标题解析"小节字符串精确匹配 | 锚点 A 在"标题解析"段**后**插入(不重写) | `git diff SKILL.md` 标题解析小节 0 改动 |
| **INV-5** | `PLAN.md` 模板 / 看板"任务清单"区段 / `dashboard-conventions.md` 0 改动 | FR-5.AC-5.3/5.4 + NFR-3 | `git diff` 三个文件为空 | 不动 | T-002 收尾时验证 |
| **INV-6** | `marketplace.json` / `plugin.json` 0 改动 | FR-5.AC-5.1 | `git diff` 两文件为空 | 不动 | T-002 收尾时验证 |
| **INV-7** | 9 个其他 `code-*` 技能 SKILL.md 0 改动 | FR-4.AC-4.1 | `git diff --stat skills/<其他 9 个>/SKILL.md` 为空 | 不动 | T-002 收尾时验证 |
| **INV-8** | `code-auto` FR-4.AC-4.3 "按任务总览行序"逻辑 0 改动 | FR-4.AC-4.2 | `git diff code-auto/SKILL.md` 为空 | 不动 | T-002 收尾时验证 |
| **INV-9** | `code-unit` / `code-publish` / `code-dashboard` / `code-review` 现有逻辑 0 改动 | FR-4.AC-4.3 | `git diff` 四个 SKILL.md 为空 | 不动 | T-002 收尾时验证 |
| **INV-10**(本计划新增) | SKILL.md 锚点 A 后的"步骤 0a"小节含完整 5 子节 | 概要设计 §1 + 沿用 REQ-00009 | `grep -c "^#### 步骤 0a\."` ≥ 5 | 实施时按 §"设计笔记"§"模块详细化"产出 5 子节 | T-002 验证 |
| **INV-11**(本计划新增) | 9 个其他 `code-*` 技能 SKILL.md 行数**不**变化 | INV-7 精确验证 | `wc -l <其他 9 SKILL.md>` 与 baseline 比对 0 差异 | 不动 | T-002 收尾时逐文件验证 |
| **INV-12**(本计划新增) | `/code-plan` / `/code-unit` 既有"## 工作流程"步骤 0a 守卫与本需求守卫**并存**,职责正交 | NFR-3 零规范变更 | 既有 REQ-00005 / REQ-00009 守卫**不**修改 | T-001 锚点 A 仅追加"## 步骤 0a"小节,**不**改既有 | T-002 收尾时验证 |
| **INV-13**(本计划新增) | 整体收尾:2 任务开发状态 = `已完成` + 测试状态 = `不适用` | 双状态语义 | 看板"任务清单"2 行开发状态 = `已完成`,测试状态 = `不适用` | T-001 完成后 | T-002 收尾时验证 |

**13/13 INV 自检清单 → T-002 实施期执行**。

## 6. 规范变更响应(本计划为首次拆分,无历史规范变更需响应)
**无**

## 7. 派生建议(留作 follow-up,本计划不阻塞)

- 沿用需求 §12 Q-8 派生预警
- 沿用概要设计 `rule-compliance.md §8` 派生预警
