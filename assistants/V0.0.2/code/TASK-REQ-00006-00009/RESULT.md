# 改修总结 — TASK-REQ-00006-00009(审查改修 — F-002)

## 1. 任务信息

- **任务编码**:`TASK-REQ-00006-00009`
- **任务标题**:`[修改] 修订双 README <code-publish> 行措辞(明确"首次调用"语义)`
- **类型**:修改
- **触发/来源**:**审查改修**(由 `code-review` REQ-00006 派生,REVIEW-REPORT.md §F-002)
- **关联任务**:T-008(双 README 同步)— T-009 对其引入的"code-publish"行做措辞修订
- **前置任务**:T-008(已完成 ✓)
- **来源 PLAN.md**:`./assistants/V0.0.2/plan/REQ-00006/PLAN.md` v1.9
- **完成时间**:2026-06-04 18:13
- **完成人**:wangmiao
- **提交哈希**:`<不提交 — 留 dirty tree 由用户整体 commit>`

## 2. 改修内容总览

| 类别 | 路径 | 操作 | 大小 |
| --- | --- | --- | --- |
| 修改 | `plugins/code-skills/README.md` | Edit 1 行(L38 "用途"列) | +1 行替换 |
| 修改 | `plugins/code-skills/README.en.md` | Edit 1 行(L38 "Purpose"列) | +1 行替换 |

**总计**:0 个新文件,2 个文件修改(各 +1 行)。**git diff --stat**:
```
plugins/code-skills/README.en.md | 1 +
plugins/code-skills/README.md    | 1 +
2 files changed, 2 insertions(+)
```

## 3. 详细改动

### 3.1 `plugins/code-skills/README.md`(中文版)

**位置**:L38(技能表第 12 行,`code-publish` 行的"用途"列)

**当前**(改前):
> ...用户手动补全;顺带在项目级创建 `assistants/qanda/` 目录

**应改为**(改后):
> ...用户手动补全;**(首次调用时)在项目级创建 `assistants/qanda/` 目录(若已存在则跳过)**

**理由**:与 SKILL.md §2.5 QandaScaffolder 行为一致(FR-6.AC-6.1 + FR-7.AC-7.4)— 仅在 qanda/ 不存在时创建。

**与 SKILL.md 的对仗**:SKILL.md §2.5 "**目的**"段写"本需求顺带在项目级创建 ..."(表述"本需求一次性副作用");本任务修订 README "**用途**"列(表述"运行时行为")。两者**互补**而非冲突:
- SKILL.md 解释"为什么这个需求会有 qanda/ 目录"
- README 解释"用户使用本技能时,会发生什么"

### 3.2 `plugins/code-skills/README.en.md`(英文版)

**位置**:L38(技能表第 12 行,`code-publish` 行的"Purpose"列)

**当前**(改前):
> ...all 3 manuals are generic skeletons with placeholders and default examples that users must complete; also creates the project-level `assistants/qanda/` directory

**应改为**(改后):
> ...all 3 manuals are generic skeletons with placeholders and default examples that users must complete; **(on first call) creates the project-level `assistants/qanda/` directory if it does not yet exist**

**理由**:与 zh 同(中英对仗 + 同次提交就绪)。

## 4. 关键决策与权衡(4 项)

| # | 决策 | 选定 | 理由 |
| --- | --- | --- | --- |
| IT-1 | 严格按 review/T-009/RESULT.md §6 "不需要做的"约束 | 不越界 | 防止任务扩大化 |
| IT-2 | **不**修改 SKILL.md §2.5 "本需求顺带"措辞 | SKILL.md §2.5 语义正确(本需求一次性副作用);与 README 修订后两者**互补** | 最小变更原则 |
| IT-3 | 中英同次 commit(用户后续操作) | 2 文件在 1 次 code-it 调用中同时 Edit | `doc-conventions §规则 1` |
| IT-4 | 不实际跑 `git commit`(NFR-3) | 仅 Edit 2 文件;`git commit` 留待用户整体 commit | NFR-3 |

## 5. 偏离设计/规范的地方

详 `deviations.md`。**0 项与设计冲突**;4 项"关键选择"显式说明,均与 review/T-009/RESULT.md + NFR-3 + `doc-conventions §规则 1` 合规。

## 6. 验证结果(详 `compile-and-run.md` + `test-results.md`)

| 验证项 | 结论 |
| --- | --- |
| 9 项静态验证(关键词 + 行/列数 + git diff) | ✓ 全过 |
| 9 项不变量自检(FR-8 + NFR + 强约束) | ✓ 全过 |
| `git diff --stat`:2 files, 2 insertions | ✓ |
| 中英 H2 数量对仗(11 / 11) | ✓ |
| 表格列数对仗(5 / 5) | ✓ |
| 表格行数对仗(11 / 11) | ✓ |

## 7. 已知问题/未完成项

### 已知问题
- **无**

### 未完成项(由后续任务承接)
- **整体 commit**:本任务**不**自动 commit;由用户审阅 `git status` + `git diff` 后整体 commit
- **端到端 3 场景**(详 test-results.md §端到端验证场景):由用户实际调用 code-publish 时验证
- **7 项 findings-no-task.md**(F-001 / F-003~F-008):作为 v2 follow-up,本需求不阻塞

## 8. 关联任务与提交

- **关联原任务**:T-008(双 README 同步)
- **关联后续任务**:**无**(本任务是审查收尾的最后 1 任务,执行后 REQ-00006 全部完成)
- **Git 提交**:**未提交**;由用户整体 commit
- **建议 commit message**(若用户单独 commit T-009):
  ```
  docs(code-publish): refine README "code-publish" row wording (F-002)
  
  Clarify that qanda/ is created on first call only, not on
  every code-publish invocation. Aligns with SKILL.md step
  2.5 (QandaScaffolder) behavior.
  
  Co-synced zh + en (doc-conventions §规则 1).
  ```

## 9. REQ-00006 全部 9 任务完成总览

| # | 任务 | 类型 | 状态 | 完成时间 | 涉及文件 |
| --- | --- | --- | --- | --- | --- |
| T-001 | SKILL.md | 新增 | ✅ | 17:30 | `plugins/code-skills/skills/code-publish/SKILL.md`(475 行) |
| T-002 | DEPLOY.md | 新增 | ✅ | 17:34 | `templates/DEPLOY.md`(245 行) |
| T-003 | UPDATE.md | 新增 | ✅ | 17:45 | `templates/UPDATE.md`(365 行) |
| T-004 | Q&A.md | 新增 | ✅ | 17:52 | `templates/Q&A.md`(63 行) |
| T-005 | qanda-README.md | 新增 | ✅ | 17:56 | `templates/qanda-README.md`(134 行) |
| T-006 | assistants-layout.md | 新增 | ✅ | 18:00 | `templates/assistants-layout.md`(172 行) |
| T-007 | 不变量自检 | 文档 | ✅ | 18:03 | `code/T-007/*`(5 文档) |
| T-008 | 双 README 同步 | 修改 | ✅ | 18:08 | `README.md` + `README.en.md` 各 +1 行 |
| **T-009** | **双 README 措辞修订** | **修改** | ✅ | **18:13** | **`README.md` + `README.en.md` 各修订 L38** |

### 看板指标(收尾状态)
- **任务清单 9/9 已完成** ✓
- **真正可发布数 9/9** ✓
- **0 与设计冲突的偏离**(8 项审查发现仅 F-002 派生 T-009,其余 7 项留 v2 follow-up)
- **0 修改 marketplace / plugin / 10 既有 SKILL.md / rules / CLAUDE.md**
- **总耗时**:~50 分钟(17:30 → 18:13 + 18:09~18:13 评审 → 审查改修)

## 10. 步骤 14 状态更新(PLAN.md)

| 字段 | 旧值 | 新值 |
| --- | --- | --- |
| 开发状态 | 进行中 | **已完成** |
| 完成时间 | — | 2026-06-04 18:13 |
| 完成人 | — | wangmiao |
| 涉及文件 | `README.md`, `README.en.md` | 同(2 文件,各 L38 修订) |
| 提交哈希 | (空) | (不提交 — 留 dirty tree 由用户整体 commit) |

## 11. 下一步建议(用户)

### 立即可执行

1. **整体 commit**:审阅 `git status` + `git diff` 后整体 commit
   - 涉及:1 SKILL.md + 5 模板 + 40 过程文档 + 2 README 改动(各 +1 行)+ 2 README 修订(各修订 L38)+ V0.0.2 看板 60+ 行增加
   - 建议 commit message:
     ```
     feat(code-publish): add release & deployment skill (REQ-00006)
     
     - New code-publish skill: preflight check on 3 board sections,
       generate DEPLOY.md / UPDATE.md (baseline skipped) / Q&A.md
     - 5 templates under plugins/code-skills/skills/code-publish/templates/
     - Project-level qanda/ directory for long-term Q&A aggregation
     - Synced double-README "Skills Overview" tables (zh + en, same commit)
     - Code review pass: refined README "code-publish" row wording
       to clarify "first call" semantics (F-002)
     
     NFR: zero deps / pure read-only / no auto-commit / not in REQ-00005
     FR-8: 0 changes to marketplace.json / plugin.json / 10 existing SKILL.md
     ```

2. **实际调 code-publish**(端到端 3 场景):
   - `/code-publish`(V0.0.2 应不通过 — 看板有未完成项,验证 E-1)
   - `/code-publish V0.0.0`(基线 + 仅 2 份手册,验证 S-3 / E-3)
   - 删除 `qanda/` 后调(自动重建,验证 S-4 / E-4)

### 后续版本(留待 v2)

- **7 项 findings-no-task.md**(F-001 / F-003~F-008):作为 v2 follow-up
- **Q-D-1**:注册 `code-publish` 到 `marketplace.json` / `plugin.json`
- **Q-D-3**:`publish-conventions.md` 沉淀
