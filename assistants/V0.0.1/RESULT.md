# 版本开发进度看板 — V0.0.1

> 本文件是 `V0.0.1` 版本工作空间的**单一事实来源**。
> 所有 `code-*` 技能在推进工作时,都会同步更新对应的区段。
> 区段填写规则见 `skills/code-version/SKILL.md` 中的"看板字段约定"。

## 文档头
- 版本号:`V0.0.1`
- 创建时间:2026-06-03 19:25
- 最近更新:2024-06-04 11:00
- 创建人:wangmiao
- 负责人:wangmiao
- 状态:活跃
- 描述:V0.0.0 基线之后的首个开发版本(基于 V0.0.0 创建,默认继承 V0.0.0 全部已完成功能)
- 当前里程碑:M3 — `code-rule` 技能扩展(已完成)

---

## 版本信息

| 字段 | 值 |
| --- | --- |
| 版本号 | `V0.0.1` |
| 创建时间 | 2026-06-03 19:25 |
| 最近更新 | 2024-06-04 11:00 |
| 创建人 | wangmiao |
| 负责人 | wangmiao |
| 状态 | 活跃 |
| 当前里程碑 | M3 — `code-rule` 技能扩展(已完成) |
| 预计交付 | — |
| 父版本 | `V0.0.0`(基线) |

---

## 里程碑

| 里程碑 | 包含任务范围 | 完成定义 | 状态 | 计划时间 | 实际完成 |
| --- | --- | --- | --- | --- | --- |
| M0:工作空间就绪 | — | 本看板创建 | 已完成 | 2026-06-03 | 2026-06-03 |
| M1:Marketplace 改名落地 | REQ-00001:T-001~T-004(`REQ-00001-001`~`004`) | 4 任务开发=已完成 ∧ 1 个 commit 已落地(单 commit,doc-conventions §规则 1) | 已完成 | 2026-06-03 | 2026-06-03 |
| M2:编码格式统一落地 | REQ-00002:T-001~T-008(`REQ-00002-001`~`008`) | 8 任务开发=已完成 ∧ 5 个 commit 已落地(多 commit,按文件类型拆分;2 个任务无 commit 符合预期) | 已完成 | 2026-06-03 | 2026-06-04 |
| M3:`code-rule` 技能扩展 | REQ-00003:T-001~T-006(`REQ-00003-001`~`006`)(T-007 审计为伴生) | 7 任务开发=已完成 ∧ 5 个 commit 已落地(类型识别+Type A/B/C 文档化 + 6 占位 + 1 弃用 + 模板扩展 + CLAUDE.md 新小节 + 全仓库审计 + 看板同步) | 已完成 | 2026-06-04 | 2024-06-04 |
| M4:可发布 | 本版本所有任务 | **所有任务开发状态=已完成 且 测试状态∈{已运行-通过, 不适用}** | 待开始 | YYYY-MM-DD | — |

> 完成定义显式列出两轴状态要求,避免把"开发完成"误当"可发布"。

---

## 需求清单

> 写入方:`code-require`(新建/变更/撤回时更新)
> 状态:`待开始` / `进行中` / `已完成` / `已取消` / `阻塞`

| 需求编码 | 标题 | 状态 | 创建时间 | 完成时间 | 需求文档 | 概要设计 | 详细设计 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-00001(原 REQ-2026-0001) | Marketplace 根名称添加 `-marketplace` 后缀 | 已完成 | 2026-06-03 20:10 | 2026-06-03 20:20 | [RESULT.md](require/REQ-00001/RESULT.md) | [RESULT.md](design/REQ-00001/RESULT.md) | [RESULT.md](plan/REQ-00001/RESULT.md) |
| REQ-00002 | 编码格式统一(REQ/TASK/BUG 均 5 位,采用新规则) | 已完成 | 2026-06-03 20:14 | 2026-06-03 20:18 | [RESULT.md](require/REQ-00002/RESULT.md) | [RESULT.md](design/REQ-00002/RESULT.md) | — |
| REQ-00003 | 优化 `code-rule` 技能,增加不同类型的核心编码规范的解析或引导 | 已完成 | 2026-06-03 20:35 | 2026-06-03 20:45 | [RESULT.md](require/REQ-00003/RESULT.md) | [RESULT.md](design/REQ-00003/RESULT.md) | [RESULT.md](plan/REQ-00003/RESULT.md) |

**统计**:
- 总数:3
- 已完成:3(需求分析阶段已完成,下游 design/plan/it/review 待开展)
- 进行中:0
- 待开始:0
- 已取消:0
- 阻塞:0

> 备注:本表"状态"反映**需求分析(code-require)**阶段是否完成;下游各阶段(概要设计/详细设计/编码/评审)状态在对应区段独立追踪。
> FR/NFR/AC 统计:
> - REQ-00001:7 FR / 7 NFR / 9 AC / 3 项待澄清(Q-3/Q-4/Q-5)
> - REQ-00002:10 FR / 7 NFR / 11 AC / 6 项待澄清(Q-6/Q-8/Q-9/Q-10/Q-11/Q-12)+ 1 项已锁定(Q-7);v2 已锁定 Q-7(TASK = `TASK-REQ-<REQ 数字段>-NNNNN` / `TASK-BUG-<BUG 数字段>-NNNNN`),并新增 Q-12("需求编码"在 TASK 编码中是否含 `REQ-` 前缀;默认 (a) 仅数字段);v3 反映 FR-6 部分提前落地
> - REQ-00003:10 FR / 6 NFR / 10 AC / 5 项待澄清(Q-4~Q-8)+ 3 项已锁定(Q-1/Q-2/Q-3);Q-1 锁定 6 类核心规范(部分条件性,部分默认,部分"未来占位"),Q-2 锁定类型识别"两者结合",Q-3 锁定 Type C 插入位置"两者都支持"
> 编码格式说明:REQ-00001 与 REQ-00002 均采用新格式(5 位纯数字);REQ-00001 原编码 REQ-2026-0001 已于 2026-06-03 20:20 提前重命名(部分落地 REQ-00002 FR-6,仅目录+本工作空间引用,SKILL.md/模板/README/CLAUDE.md 的旧编码引用由 REQ-00002 `code-it` 阶段统一清理)

---

## 概要设计清单

> 写入方:`code-design`(新建/变更时更新)

| 需求编码 | 设计标题 | 状态 | 创建时间 | 完成时间 | 概要设计文档 |
| --- | --- | --- | --- | --- | --- |
| REQ-00001 | Marketplace 根名称添加 `-marketplace` 后缀 | 已完成 | 2026-06-03 20:25 | 2026-06-03 20:25 | [RESULT.md](design/REQ-00001/RESULT.md) |
| REQ-00002 | 编码格式统一(REQ/TASK/BUG 均 5 位,采用新规则) | 已完成 | 2026-06-03 20:25 | 2026-06-03 20:25 | [RESULT.md](design/REQ-00002/RESULT.md) |
| REQ-00003 | 优化 `code-rule` 技能,增加不同类型的核心编码规范的解析或引导 | 已完成 | 2026-06-03 21:00 | 2026-06-03 21:00 | [RESULT.md](design/REQ-00003/RESULT.md) |

**统计**:3 / 已完成 3 / 进行中 0

---

## 详细设计与任务计划汇总

> 写入方:`code-plan`(新建/变更/追加任务时更新)

| 需求编码 | 计划标题 | 状态 | 任务总数 | 开发完成 | 测试通过 | 创建时间 | 计划文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-00001 | Marketplace 根名称添加 `-marketplace` 后缀 | 已完成 | 4 | 4 | 0(全部不适用) | 2026-06-03 20:30 | [PLAN.md](plan/REQ-00001/PLAN.md) |
| REQ-00002 | 编码格式统一(REQ/TASK/BUG 均 5 位,采用新规则) | 已完成 | 8 | 0 | 0(全部不适用) | 2026-06-03 20:55 | [PLAN.md](plan/REQ-00002/PLAN.md) |
| REQ-00003 | 优化 `code-rule` 技能,增加不同类型的核心编码规范的解析或引导 | 已完成 | 7 | 0 | 0(全部不适用) | 2026-06-04 09:15 | [PLAN.md](plan/REQ-00003/PLAN.md) |

**统计**:3 个计划 / 共 19 个任务 / 开发完成 4 / 测试通过 0(全部不适用) / **真正可发布 4 / 19** |

---

## 任务清单

> 首次登记:`code-plan`(拆分任务时)
> 持续更新:
> - `code-it` 推进 `开发状态`(`待开始` → `进行中` → `已完成`)
> - `code-unit` 推进 `测试状态`(`未编写` → `已编写` → `已运行-通过` / `已运行-失败` / `不适用`)

| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 完成时间 | 提交哈希 | 关联任务 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REQ-00001-001` | REQ-00001 | 修改 | 需求新增 | 改 `.claude-plugin/marketplace.json` 根 name | 已完成 | 不适用 | `.claude-plugin/marketplace.json` | 2026-06-03 20:50 | f147ea7 | — |
| `REQ-00001-002` | REQ-00001 | 修改 | 需求新增 | 同步中英 README | 已完成 | 不适用 | `plugins/code-skills/README.md`, `README.en.md` | 2026-06-03 20:51 | f147ea7 | — |
| `REQ-00001-003` | REQ-00001 | 文档 | 需求新增 | 核查 `plugins/code-skills/CLAUDE.md` | 已完成 | 不适用 | `plugins/code-skills/CLAUDE.md`(0 变更) | 2026-06-03 20:52 | (不提交) | — |
| `REQ-00001-004` | REQ-00001 | 文档 | 需求新增 | 全仓库穷举式 Grep + 偏差日志 + 不变量自检 + commit | 已完成 | 不适用 | 无文件修改,产出 `code/REQ-00001-004/{RESULT,work-log,deviations}.md` | 2026-06-03 20:54 | f147ea7 | — |
| `REQ-00002-001` | REQ-00002 | 修改 | 需求新增 | 同步 10 个 SKILL.md(只改正文) | 已完成 | 不适用 | `plugins/code-skills/skills/{code-fix,code-it,code-plan,code-require,code-unit}/SKILL.md`(5 文件) | 2026-06-04 09:50 | 8ac1c9a | — |
| `REQ-00002-002` | REQ-00002 | 修改 | 需求新增 | 同步 27 模板(改正文占位符 + 示例值) | 已完成 | 不适用 | 11 templates(见 plan/REQ-00002/PLAN.md §2.2 + 偏离 1) | 2026-06-04 10:05 | 3df8ae7 | T-1 |
| `REQ-00002-003` | REQ-00002 | 修改 | 需求新增 | 同步中英 README(同次 commit) | 已完成 | 不适用 | `plugins/code-skills/README.md`, `README.en.md` | 2026-06-04 10:00 | 31d6221 | T-1, T-2 |
| `REQ-00002-004` | REQ-00002 | 文档 | 需求新增 | 核查 CLAUDE.md(预期 0 变更) | 已完成 | 不适用 | `plugins/code-skills/CLAUDE.md`(0 变更,无 commit) | 2026-06-04 10:00 | (无 commit) | — |
| `REQ-00002-005` | REQ-00002 | 新增 | 需求新增(FR-7) | 创建 encoding-conventions.md 规范文件 | 已完成 | 不适用 | `assistants/rules/encoding-conventions.md` | 2026-06-04 10:05 | b092dec | T-1, T-2 |
| `REQ-00002-006` | REQ-00002 | 新增 | 需求新增(FR-8) | 创建 migration-mapping.md 迁移映射 | 已完成 | 不适用 | `assistants/rules/migration-mapping.md` | 2026-06-04 10:08 | 5121e3f | T-5 |
| `REQ-00002-007` | REQ-00002 | 文档 | 需求新增 | 全仓库穷举式 Grep + 偏差日志 + 不变量自检 | 已完成 | 不适用 | 无文件修改,产出 `code/REQ-00002-007/{RESULT,work-log,deviations,compile-and-run}.md` | 2026-06-04 10:15 | (无 commit) | T-1 ~ T-6 |
| `REQ-00002-008` | REQ-00002 | 文档 | 需求新增 | 同步版本看板 | 已完成 | 不适用 | `assistants/V0.0.1/RESULT.md` + `plan/REQ-00002/PLAN.md` | 2026-06-04 10:20 | a24663d | T-1 ~ T-7 |
| `REQ-00003-001` | REQ-00003 | 修改 | 需求新增 | 扩展 `code-rule/SKILL.md` 正文(类型识别 + Type A/B/C 文档化 + 工作目录约定) | 已完成 | 不适用 | `plugins/code-skills/skills/code-rule/SKILL.md` | 2026-06-04 10:26 | 086890d | T-002, T-003, T-005 |
| `REQ-00003-002` | REQ-00003 | 新增 | 需求新增 | 创建 6 个新分类占位文件(C-1~C-6) | 已完成 | 不适用 | `assistants/rules/framework-conventions.md`, `dependency-conventions.md`, `naming-conventions.md`, `directory-conventions.md`, `coding-style.md`, `commit-conventions.md` | 2026-06-04 10:53 | bec5f13 | T-001 |
| `REQ-00003-003` | REQ-00003 | 修改 | 需求新增 | 追加 `module-conventions.md` DEPRECATED 标记 | 已完成 | 不适用 | `assistants/rules/module-conventions.md` | 2026-06-04 10:55 | 695c029 | T-002 |
| `REQ-00003-004` | REQ-00003 | 修改 | 需求新增 | 扩展 `templates/rule.md`(占位 + 引导模式) | 已完成 | 不适用 | `plugins/code-skills/skills/code-rule/templates/rule.md` | 2026-06-04 10:55 | 2f41bb0 | T-001 |
| `REQ-00003-005` | REQ-00003 | 修改 | 需求新增 | 追加 `CLAUDE.md` "## AI 工作约定"小节(首次) | 已完成 | 不适用 | `plugins/code-skills/CLAUDE.md` | 2026-06-04 10:55 | 35bc26b | T-001 |
| `REQ-00003-006` | REQ-00003 | 文档 | 需求新增 | 同步版本看板 + 更新 `plan/REQ-00003/PLAN.md` 状态 | 已完成 | 不适用 | `assistants/V0.0.1/RESULT.md`, `assistants/V0.0.1/plan/REQ-00003/PLAN.md` | 2024-06-04 11:00 | (无 commit) | T-001 ~ T-005 |
| `REQ-00003-007` | REQ-00003 | 文档 | 需求新增 | 全仓库 Grep + 不变量自检 + 6 commit 整理 | 已完成 | 不适用 | 无文件修改,产出 `code/REQ-00003-007/{RESULT,work-log,deviations,compile-and-run}.md` | 2024-06-04 10:55 | (无 commit) | T-001 ~ T-006 |
| `REQ-00002-009` | REQ-00002 | 文档 | 审查改修 | 同步 PLAN.md 任务总览 + M2 描述(审查派生) | 待开始 | 未编写 | `assistants/V0.0.1/plan/REQ-00002/PLAN.md`, `V0.0.1/RESULT.md` | — | — | REQ-00002-007, REQ-00002-008 |
| `REQ-00001-005` | REQ-00001 | 修改 | 审查改修 | 同步中英 README 中 GitHub URL 仓库名(审查派生) | 待开始 | 未编写 | `plugins/code-skills/README.md`, `README.en.md` | — | — | REQ-00001-002 |

**统计**:
- 总任务数:21(原 19 + REQ-00001-005 派生 + REQ-00002-009 派生)
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):19 / 21(M1 已达成, M2 已完成, **M3 已完成 7/7**)
- 开发已完成 / 未完成:19 / 2
- 测试已通过 / 已失败 / 不适用 / 未编写:0 / 0 / 21 / 0

---

## 缺陷清单

> 写入方:
> - `code-review` 评审时发现的严重缺陷(自动登记)
> - `code-it` 编码时发现的已记录缺陷
> - `code-unit` 测试时发现的代码 bug(转交 `code-it`)

| 缺陷编号 | 严重度 | 标题 | 状态 | 报告时间 | 修复时间 | 关联任务 | 修复提交 |
| --- | --- | --- | --- | --- | --- | --- | --- |

**统计**:0 / P0: 0 / P1: 0 / P2: 0 / 已修复 0 / 待修复 0

---

## 评审发现汇总

> 写入方:`code-review`

| 评审 ID | 需求 | 任务 | 维度 | 级别 | 描述 | 派生改修任务 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-1 | REQ-00001 | REQ-00001-002 | 一致性 / 规范 | 建议改 | GitHub 仓库 URL 未与 marketplace name 同步(`https://github.com/wm123450405/code-skills.git` 应询问用户后决定) | REQ-00001-005 | 待开始 |
| F-2 | REQ-00001 | REQ-00001-002 | 可维护性 | 可选 | CLAUDE.md 目录树图例与新 marketplace name 关联弱 | (无,记入 findings-no-task.md) | 留作 follow-up |
| F-3 | REQ-00002 | REQ-00002-005 | 可维护性 | 可选 | encoding-conventions.md 结构验证(212 行,4 规则,无偏离) | (无,记入 findings-no-task.md) | 留作 follow-up |
| F-4 | REQ-00002 | REQ-00002-007 | 一致性 | 建议改 | PLAN.md 任务总览行 27 T-007 状态字段"待开始",与看板(已完成) + 实际产出(4 文档)不一致 | REQ-00002-009 | 待开始 |
| F-5 | REQ-00002 | REQ-00002-008 | 一致性 | 建议改 | M2 里程碑描述"7 commit"与实际"5 commit + 2 无 commit task"不一致 | REQ-00002-009 | 待开始 |

**统计**:5 / 必须改: 0 / 建议改: 3 / 可选: 2 / 已处理: 0
**统计**:0 / 必须改: 0 / 建议改: 0 / 可选: 0 / 已处理: 0

---

## 派生任务记录

> 写入方:`code-review`(派生"审查改修"任务时)
> 用途:追踪"由 review 派生、关联到原任务"的特殊任务链路

| 派生任务 | 关联原任务 | 派生时间 | review 来源 | 状态 |
| --- | --- | --- | --- | --- |
| REQ-00001-005 | REQ-00001-002 | 2026-06-04 10:35 | [REVIEW-REPORT.md](review/REQ-00001/REVIEW-REPORT.md) | 待开始 |
| REQ-00002-009 | REQ-00002-007, REQ-00002-008 | 2026-06-04 10:40 | [REVIEW-REPORT.md](review/REQ-00002/REVIEW-REPORT.md) | 待开始 |

| 派生任务 | 关联原任务 | 派生时间 | review 来源 | 状态 |
| --- | --- | --- | --- | --- |

---

## 执行的开发命令记录

> 写入方:各 `code-*` 技能在执行编译/启动/测试等命令后追加
> 用途:审计"本版本中跑过哪些命令、结果如何"

| 时间 | 命令 | 工具 | 退出码 | 结果 | 关联任务/阶段 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-03 20:50 | `git diff .claude-plugin/marketplace.json` | Bash | 0 | 1 行变更(L3 根 name) | REQ-00001-001 |
| 2026-06-03 20:51 | `git diff --stat plugins/code-skills/README.md plugins/code-skills/README.en.md` | Bash | 0 | 2 files, 4 insertions, 4 deletions | REQ-00001-002 |
| 2026-06-03 20:53 | `Grep "code-skills@code-skills" --glob="**/*.{md,json}" .` | Grep | 0 | 见 RESULT.md §6.1 分类报告 | REQ-00001-004 |
| 2026-06-03 20:54 | `git add .claude-plugin/marketplace.json plugins/code-skills/README.md plugins/code-skills/README.en.md` | Bash | 0 | staged 3 files | REQ-00001-004 |
| 2026-06-03 20:54 | `git commit -m "chore(marketplace): rename ..."` | Bash | 0 | commit `f147ea7` 创建成功 | REQ-00001-004 |
| 2026-06-04 09:50 | `git diff --stat plugins/code-skills/skills/` | Bash | 0 | 5 files changed, 31 insertions(+), 31 deletions(-) | REQ-00002-001 |
| 2026-06-04 09:50 | `git add plugins/code-skills/skills/{code-fix,code-it,code-plan,code-require,code-unit}/SKILL.md` | Bash | 0 | staged 5 files | REQ-00002-001 |
| 2026-06-04 09:50 | `git commit -m "chore(encoding): sync 5 SKILL.md ..."` | Bash | 0 | commit `8ac1c9a` 创建成功 | REQ-00002-001 |
| 2026-06-04 10:05 | `git diff --stat plugins/code-skills/skills/*/templates/` | Bash | 0 | 11 files changed, 40 insertions(+), 40 deletions(-) | REQ-00002-002 |
| 2026-06-04 10:05 | `git add plugins/code-skills/skills/*/templates/` | Bash | 0 | staged 11 files | REQ-00002-002 |
| 2026-06-04 10:05 | `git commit -m "chore(encoding): sync 11 templates ..."` | Bash | 0 | commit `3df8ae7` 创建成功 | REQ-00002-002 |
| 2026-06-04 10:00 | `git diff --stat plugins/code-skills/README.md plugins/code-skills/README.en.md` | Bash | 0 | 2 files, 72 insertions(+), 72 deletions(-) | REQ-00002-003 |
| 2026-06-04 10:00 | `git add plugins/code-skills/README.md plugins/code-skills/README.en.md` | Bash | 0 | staged 2 files | REQ-00002-003 |
| 2026-06-04 10:00 | `git commit -m "chore(encoding): sync README ..."` | Bash | 0 | commit `31d6221` 创建成功 | REQ-00002-003 |
| 2026-06-04 10:05 | `git add assistants/rules/encoding-conventions.md` | Bash | 0 | staged 1 file (212 insertions) | REQ-00002-005 |
| 2026-06-04 10:05 | `git commit -m "chore(rules): add encoding-conventions.md ..."` | Bash | 0 | commit `b092dec` 创建成功 | REQ-00002-005 |
| 2026-06-04 10:08 | `git add assistants/rules/migration-mapping.md` | Bash | 0 | staged 1 file (230 insertions) | REQ-00002-006 |
| 2026-06-04 10:08 | `git commit -m "chore(rules): add migration-mapping.md ..."` | Bash | 0 | commit `5121e3f` 创建成功 | REQ-00002-006 |
| 2026-06-04 10:26 | `git diff --stat plugins/code-skills/skills/code-rule/SKILL.md` | Bash | 0 | 1 file, 197 insertions(+), 25 deletions(-) | REQ-00003-001 |
| 2026-06-04 10:26 | `git add plugins/code-skills/skills/code-rule/SKILL.md` | Bash | 0 | staged 1 file | REQ-00003-001 |
| 2026-06-04 10:26 | `git commit -m "feat(code-rule): add 3 target types ..."` | Bash | 0 | commit `086890d` 创建成功 | REQ-00003-001 |
| 2026-06-04 10:53 | `git add assistants/rules/{framework,dependency,naming,directory,coding-style,commit}-conventions.md` | Bash | 0 | staged 6 files | REQ-00003-002 |
| 2026-06-04 10:53 | `git commit -m "feat(rules): add 6 placeholder classification files ..."` | Bash | 0 | commit `bec5f13` 创建成功 | REQ-00003-002 |
| 2026-06-04 10:55 | `git add assistants/rules/module-conventions.md` | Bash | 0 | staged 1 file (+2 insertions) | REQ-00003-003 |
| 2026-06-04 10:55 | `git commit -m "chore(rules): deprecate module-conventions.md ..."` | Bash | 0 | commit `695c029` 创建成功 | REQ-00003-003 |
| 2026-06-04 10:55 | `git add plugins/code-skills/skills/code-rule/templates/rule.md` | Bash | 0 | staged 1 file (+23 insertions) | REQ-00003-004 |
| 2026-06-04 10:55 | `git commit -m "feat(code-rule): extend templates/rule.md ..."` | Bash | 0 | commit `2f41bb0` 创建成功 | REQ-00003-004 |
| 2026-06-04 10:55 | `git add plugins/code-skills/CLAUDE.md` | Bash | 0 | staged 1 file (+7 insertions) | REQ-00003-005 |
| 2026-06-04 10:55 | `git commit -m "feat(CLAUDE.md): add AI 工作约定 section ..."` | Bash | 0 | commit `35bc26b` 创建成功 | REQ-00003-005 |

---

## 变更记录

> 写入方:所有 `code-*` 技能,在自己的关键节点追加
> 格式:`YYYY-MM-DD HH:mm  <变更类型>  <摘要>  <关联任务/需求>(可选)`

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 19:25 | 初始化 | 创建版本 V0.0.1 工作空间(从 V0.0.0 切换) | — |
| 2026-06-03 20:10 | 需求新增 | REQ-00001 需求分析完成(原 REQ-2026-0001,共 7 条 FR / 7 条 NFR / 9 条 AC / 3 项待澄清)。范围:仅 `.claude-plugin/marketplace.json` 根 `name` 字段 `code-skills` → `code-skills-marketplace`;同步 README.md / README.en.md / CLAUDE.md 中引用,严禁修改 plugin.json / 目录结构 / SKILL.md / 规范文件 | REQ-00001(原 REQ-2026-0001) |
| 2026-06-03 20:14 | 需求新增 | REQ-00002 需求分析完成(10 FR / 7 NFR / 11 AC / 6 项待澄清 Q-6~Q-11)。范围:三类编码格式统一(REQ-NNNNN / TASK-? / BUG-NNNNN,5 位);追溯重命名 REQ-2026-0001 → REQ-00001;横切 10 个 SKILL.md / 20+ 模板 / README / CLAUDE.md;严禁修改 marketplace 协议清单与目录结构 | REQ-00002 |
| 2026-06-03 20:18 | 需求变更 | REQ-00002 增量更新 v2:用户回答 Q-7,TASK 编码改为嵌套式 `TASK-REQ-<REQ 编码>-NNNNN`(需求任务) / `TASK-BUG-<BUG 编码>-NNNNN`(修复任务);FR-1 / FR-2 / FR-3 正则与示例同步;新增 Q-12 澄清"需求编码"在 TASK 编码中是否含 `REQ-` 前缀 | REQ-00002 |
| 2026-06-03 20:20 | 需求重命名 | 按用户指令提前落地 REQ-00002 FR-6 部分工作:目录 `assistants/V0.0.1/require/REQ-2026-0001/` → `REQ-00001/`,本工作空间及 V0.0.1 看板中的"当前"引用同步;v1 历史变更记录保留原字面值。**未触及**:SKILL.md / 模板 / README / CLAUDE.md / V0.0.0 EXISTING-* — 仍由 REQ-00002 `code-it` 阶段统一清理 | REQ-00001(原 REQ-2026-0001) |
| 2026-06-03 20:20 | 需求变更 | REQ-00002 增量更新 v3:同步反映 FR-6 部分提前落地的状态(FR-6 描述、AC-6 步骤、§场景 1、§1 概述、§11 关联需求、related-requirements.md §实施顺序建议均标注"已发生 / ✅");Q-11 措辞调整为"原先后顾虑部分消解" | REQ-00002 |
| 2026-06-03 20:25 | 设计新增 | REQ-00001 概要设计完成(v1,7 项设计决策,4 文件变更集,关键不变量 7 条,规范 100% 合规;Q-3/Q-4/Q-5 采用 REQU 文档默认值,详见 design/REQ-00001/clarifications.md)。范围:仅 .claude-plugin/marketplace.json 根 name + 2 README + 1 CLAUDE?(Grep 后决定);严守 marketplace-protocol §规则 1.3(plugin 标识保持)、doc-conventions §规则 1(中英同次提交) | REQ-00001 |
| 2026-06-03 20:25 | 设计新增 | REQ-00002 概要设计完成(v1,8 项设计决策,5 个修改文件类型 + 2 条件新文件,11 个子任务预想,11 条不变量;Q-7 已锁定 v2 G4 新嵌套式;Q-6/Q-8/Q-9/Q-10/Q-12 采用 REQU 文档默认值,详见 design/REQ-00002/clarifications.md)。范围:10 SKILL.md(只改正文)+ 20+ 模板(占位符+示例值)+ 3 文档 + 1 看板模板(只改示例值,不触发 dashboard-conventions §规则 1)+ (条件)encoding-conventions.md + (条件)migration-mapping.md;严守 doc-conventions §规则 1/2、skill-conventions §规则 1(frontmatter 保持) | REQ-00002 |
| 2026-06-03 20:30 | 计划新增 | REQ-00001 详细设计与编码计划完成(共 4 个任务,`REQ-00001-001` ~ `REQ-00001-004`)。范围:`.claude-plugin/marketplace.json` 根 name + 中英 README 同步 + CLAUDE.md 核查 + 全仓库 Grep + 单 commit 提交;继承概要设计 7 决策 + 11 不变量;Q-3/Q-4/Q-5 采用 REQU 文档默认;无新增依赖,无偏离规范 | REQ-00001 |
| 2026-06-03 20:45 | 需求新增 | REQ-00003 需求分析完成(共 10 FR / 6 NFR / 10 AC / 5 项待澄清 Q-4~Q-8 + 3 项已锁定 Q-1/Q-2/Q-3)。范围:扩展 `code-rule` 技能支持 3 种目标类型(Type A 规则 / Type B CLAUDE.md / Type C 模板),Type A 覆盖 6 类核心规范(部分条件性,部分支持"未来占位");类型识别为"自动+显式"两者结合;Type C 支持末尾追加与内联两种插入位置;保持现有 Type A 流程向后兼容(NFR-1);严守 FR-9 边界(不修改 marketplace.json / plugin.json / 其他 9 SKILL.md frontmatter / V0.0.0~V0.0.1 工作文件);Q-1 锁定 6 类规范(C-1 框架 / C-2 三方依赖 / C-3 语言与命名 / C-4 目录与模块 / C-5 代码书写 / C-6 提交与合并),Q-2 锁定"自动+显式",Q-3 锁定"两者都支持"。**未阻塞** `code-design` 阶段(Q-4~Q-8 采用合理默认并显式记录回退路径) | REQ-00003 |
| 2026-06-03 20:50 | 开发状态更新 | `REQ-00001-001` 开发状态"待开始"→"已完成",commit `f147ea7`,T-001 改 marketplace.json 根 name | `REQ-00001-001` |
| 2026-06-03 20:51 | 开发状态更新 | `REQ-00001-002` 开发状态"待开始"→"已完成",commit `f147ea7`,T-002 同步中英 README(2 文件 × 2 处字面量) | `REQ-00001-002` |
| 2026-06-03 20:52 | 开发状态更新 | `REQ-00001-003` 开发状态"待开始"→"已完成",T-003 核查 CLAUDE.md(0 命中 3 关键词,0 变更,无 commit) | `REQ-00001-003` |
| 2026-06-03 20:54 | 开发状态更新 | `REQ-00001-004` 开发状态"待开始"→"已完成",T-004 全仓库 Grep + 11 不变量自检 + 单 commit `f147ea7`(3 files, 5+/5-);3 处偏离记入 `code/REQ-00001-004/deviations.md`;**M1 达成** | `REQ-00001-004` |
| 2026-06-03 20:55 | 计划新增 | REQ-00002 详细设计与编码计划完成(共 8 个任务,`REQ-00002-001` ~ `REQ-00002-008`)。范围:10 SKILL.md(只改正文)+ 27 模板(占位符+示例值)+ 中英 README + CLAUDE.md 核查 + (条件)encoding-conventions.md + (条件)migration-mapping.md + 全仓库 Grep + 看板同步;多 commit 粒度按文件类型(7 个 commit);继承概要设计 8 决策 + 11 不变量 + 本设计新增 2 不变量(INV-12/13);Q-1 ~ Q-12 全部采纳 REQU 文档默认;plan 阶段 D-PLAN-1(`code-it` 创建新规范文件,授权);无新增依赖,无偏离规范;**M2 待开始** | REQ-00002 |
| 2026-06-03 21:00 | 设计新增 | REQ-00003 概要设计完成(v1,核心架构=单技能 + 3 子流程;9 个模块 M-1~M-9;Type A 6 分类 + 4 保留 + 1 弃用[H2 决策];Type B/C 数据结构 5/4 字段;9 条不变量;5 commit 实施计划)。范围:扩展 `code-rule/SKILL.md` 正文(不改 frontmatter)+ 扩展 `templates/rule.md`(占位/引导模式)+ 6 个新分类文件(全空占位 H1 决策)+ `module-conventions.md` 追加 DEPRECATED 标记 + `plugins/code-skills/CLAUDE.md` 末尾追加"AI 工作约定"小节。严守 FR-9 边界(不修改 marketplace.json / plugin.json / 9 个其他 SKILL.md / 4 保留规范文件 / V0.0.0~V0.0.1 工作文件);Q-4(C-4=`directory-conventions`)/Q-5(全空占位)/Q-8(H2 module→directory 迁移)用户确认,Q-6(Type B 无示例字段)/Q-7(Type C `## 提示:` + `### 提示:` 并存)采纳默认;design 阶段新增 D-DESIGN-1(保留旧关键词向后兼容)/D-DESIGN-2(`code-rule` description 不变)/D-DESIGN-3(5 commit 按模块拆分);无新增依赖,无偏离规范;**M3 待开始,REQ-00003 阻塞 `code-plan` REQ-00003 等待用户触发** | REQ-00003 |
| 2026-06-04 09:15 | 计划新增 | REQ-00003 详细设计与编码计划完成(共 7 个任务,`REQ-00003-001` ~ `REQ-00003-007`)。范围:扩展 `code-rule/SKILL.md` 正文(类型识别 + Type A/B/C 文档化 + 工作目录约定) + 6 个新分类占位文件 + `module-conventions.md` 弃用标记 + 扩展 `templates/rule.md`(占位/引导模式) + 追加 `CLAUDE.md` "AI 工作约定"小节 + 看板同步 + 全仓库审计;6 commit 粒度按模块(commit 1 含 T-001 + T-006 看板同步);继承 design 8 决策 + 9 不变量 + 本 plan 新增 2 不变量(INV-10/11);**plan 阶段对 design 的微调**:**Q-PLAN-2 类型识别合并到步骤 4 子段 4.2**(design M-1 原为"独立子流程",变更为"步骤 4 子模块",模块命名保留便于追踪);**Q-PLAN-1 任务粒度按 5 commit 拆 7-9 任务**;无新增依赖,无偏离规范;**M3 待开始,REQ-00003 阻塞 `code-it` 等待用户触发** | REQ-00003 |
| 2026-06-04 09:50 | 开发状态更新 | `REQ-00002-001` 开发状态"待开始"→"已完成",提交 `8ac1c9a`(5 SKILL.md 改正文,31+/31-;frontmatter 完整保留) | `REQ-00002-001` |
| 2026-06-04 10:05 | 开发状态更新 | `REQ-00002-002` 开发状态"待开始"→"已完成",提交 `3df8ae7`(11 templates 改正文占位符/示例值,40+/40-;实际改 11/27,16 个 0 命中无需改) | `REQ-00002-002` |
| 2026-06-04 10:00 | 开发状态更新 | `REQ-00002-003` 开发状态"待开始"→"已完成",提交 `31d6221`(2 README 改正文示例,72+/72-;中英严格对仗,`doc-conventions §规则 1` 严格遵循) | `REQ-00002-003` |
| 2026-06-04 10:00 | 开发状态更新 | `REQ-00002-004` 开发状态"待开始"→"已完成"(核查 0 命中,无 commit;符合 PLAN §2.4 预期) | `REQ-00002-004` |
| 2026-06-04 10:05 | 开发状态更新 | `REQ-00002-005` 开发状态"待开始"→"已完成",提交 `b092dec`(新建 `encoding-conventions.md` 212 行;4 规则权威源;`code-it` 创建新文件由 D-PLAN-1 授权) | `REQ-00002-005` |
| 2026-06-04 10:08 | 开发状态更新 | `REQ-00002-006` 开发状态"待开始"→"已完成",提交 `5121e3f`(新建 `migration-mapping.md` 230 行;5 规则;22 条映射数据;`code-it` 创建新文件由 D-PLAN-1 授权) | `REQ-00002-006` |
| 2026-06-04 10:15 | 开发状态更新 | `REQ-00002-007` 开发状态"待开始"→"已完成"(13/13 不变量自检通过;全仓库 0 命中;2 项 PLAN 推断与实际不符已记录;无 commit) | `REQ-00002-007` |
| 2026-06-04 10:20 | 开发状态更新 | `REQ-00002-008` 开发状态"待开始"→"已完成"(M2 全部 8 任务已完成;看板 6 区段同步完成;M2 状态推进"待开始"→"已完成") | `REQ-00002-008` |
| 2026-06-04 10:26 | 开发状态更新 | `REQ-00003-001` 开发状态"待开始"→"已完成",提交 `086890d`(SKILL.md 272 → 449 行,+177;6 个变更;frontmatter 完整保留;关键词表 11 → 13 项) | `REQ-00003-001` |
| 2026-06-04 10:53 | 开发状态更新 | `REQ-00003-002` 开发状态"待开始"→"已完成",提交 `bec5f13`(新建 6 个新分类占位文件,896-1088 bytes/各;INV-2 最小骨架;INV-5 既有未改;`directory-conventions.md` 含迁移说明) | `REQ-00003-002` |
| 2026-06-04 10:55 | 开发状态更新 | `REQ-00003-003` 开发状态"待开始"→"已完成",提交 `695c029`(`module-conventions.md` 头部 +2 行 DEPRECATED 引用块;INV-7 仅追加不删;不修改其他 12 规范文件) | `REQ-00003-003` |
| 2026-06-04 10:55 | 开发状态更新 | `REQ-00003-004` 开发状态"待开始"→"已完成",提交 `2f41bb0`(`templates/rule.md` 头部 +23 行 2 个 H2 小节;INV-1 8 字段结构保持) | `REQ-00003-004` |
| 2026-06-04 10:55 | 开发状态更新 | `REQ-00003-005` 开发状态"待开始"→"已完成",提交 `35bc26b`(`CLAUDE.md` 末尾 +7 行 1 个 H2 小节"## AI 工作约定(由 code-rule 维护)";INV-3 纯追加不删;原 7 个小节保留) | `REQ-00003-005` |
| 2024-06-04 10:55 | 开发状态更新 | `REQ-00003-007` 开发状态"待开始"→"已完成"(11/11 不变量自检通过;全仓库 0 命中;5 commit 顺序正确;无 commit) | `REQ-00003-007` |
| 2024-06-04 11:00 | 开发状态更新 | `REQ-00003-006` 开发状态"待开始"→"已完成"(M3 全部 7 任务完成;看板 6 区段同步;M3 状态"待开始"→"已完成";累积未提交看板同步一次性 commit) | `REQ-00003-006` |
| 2026-06-04 10:35 | 评审发现 | REQ-00001 评审完成(2 条发现:F-1 建议改派生 T-005 + F-2 可选记入 findings-no-task.md;无 P0/P1 阻塞;M1 派生 1 任务) | REQ-00001 |
| 2026-06-04 10:40 | 评审发现 | REQ-00002 评审完成(3 条发现:F-4 + F-5 建议改合并派生 T-009 + F-3 可选;8 任务全部通过 8/8;无 P0/P1 阻塞) | REQ-00002 |

---

## 索引:本版本所有文件

- 需求:`./assistants/V0.0.1/require/<需求编号>/RESULT.md` × N
  - REQ-00001 → [require/REQ-00001/RESULT.md](require/REQ-00001/RESULT.md)
  - REQ-00002 → [require/REQ-00002/RESULT.md](require/REQ-00002/RESULT.md)
  - REQ-00003 → [require/REQ-00003/RESULT.md](require/REQ-00003/RESULT.md)
- 概要设计:`./assistants/V0.0.1/design/<需求编号>/RESULT.md` × N
  - REQ-00001 → [design/REQ-00001/RESULT.md](design/REQ-00001/RESULT.md)
  - REQ-00002 → [design/REQ-00002/RESULT.md](design/REQ-00002/RESULT.md)
  - REQ-00003 → [design/REQ-00003/RESULT.md](design/REQ-00003/RESULT.md)
- 详细设计:`./assistants/V0.0.1/plan/<需求编号>/RESULT.md` × N
  - REQ-00001 → [plan/REQ-00001/RESULT.md](plan/REQ-00001/RESULT.md)
  - REQ-00002 → [plan/REQ-00002/RESULT.md](plan/REQ-00002/RESULT.md)
  - REQ-00003 → [plan/REQ-00003/RESULT.md](plan/REQ-00003/RESULT.md)
- 任务计划:`./assistants/V0.0.1/plan/<需求编号>/PLAN.md` × N
  - REQ-00001 → [plan/REQ-00001/PLAN.md](plan/REQ-00001/PLAN.md)(4 个任务:`REQ-00001-001`~`004`)
  - REQ-00002 → [plan/REQ-00002/PLAN.md](plan/REQ-00002/PLAN.md)(8 个任务:`REQ-00002-001`~`008`)
  - REQ-00003 → [plan/REQ-00003/PLAN.md](plan/REQ-00003/PLAN.md)(7 个任务:`REQ-00003-001`~`007`)
- 过程文档:`./assistants/V0.0.1/plan/REQ-00002/*.md`
  - [materials-index.md](plan/REQ-00002/materials-index.md) / [design-notes.md](plan/REQ-00002/design-notes.md) / [module-details.md](plan/REQ-00002/module-details.md) / [interface-specs.md](plan/REQ-00002/interface-specs.md) / [data-changes.md](plan/REQ-00002/data-changes.md) / [risk-analysis.md](plan/REQ-00002/risk-analysis.md) / [rule-compliance.md](plan/REQ-00002/rule-compliance.md) / [clarifications.md](plan/REQ-00002/clarifications.md)
- 过程文档:`./assistants/V0.0.1/plan/REQ-00003/*.md`
  - [materials-index.md](plan/REQ-00003/materials-index.md) / [design-notes.md](plan/REQ-00003/design-notes.md) / [module-details.md](plan/REQ-00003/module-details.md) / [interface-specs.md](plan/REQ-00003/interface-specs.md) / [data-changes.md](plan/REQ-00003/data-changes.md) / [risk-analysis.md](plan/REQ-00003/risk-analysis.md) / [rule-compliance.md](plan/REQ-00003/rule-compliance.md) / [clarifications.md](plan/REQ-00003/clarifications.md)
- 代码改修正文:`./assistants/V0.0.1/code/<任务编码>/RESULT.md` × N
  - REQ-00001-001 → [code/REQ-00001-001/RESULT.md](code/REQ-00001-001/RESULT.md) + [work-log.md](code/REQ-00001-001/work-log.md)
  - REQ-00001-002 → [code/REQ-00001-002/RESULT.md](code/REQ-00001-002/RESULT.md) + [work-log.md](code/REQ-00001-002/work-log.md)
  - REQ-00001-003 → [code/REQ-00001-003/RESULT.md](code/REQ-00001-003/RESULT.md) + [work-log.md](code/REQ-00001-003/work-log.md)
  - REQ-00001-004 → [code/REQ-00001-004/RESULT.md](code/REQ-00001-004/RESULT.md) + [work-log.md](code/REQ-00001-004/work-log.md) + [deviations.md](code/REQ-00001-004/deviations.md)
- 测试改修正文:`./assistants/V0.0.1/test/<任务编码>/RESULT.md` × N(待添加)
- 评审报告:`./assistants/V0.0.1/review/<需求编号>/REVIEW-REPORT.md` × N(待添加)
- 审查改修任务:`./assistants/V0.0.1/review/<任务编码>/RESULT.md` × N(待添加)
