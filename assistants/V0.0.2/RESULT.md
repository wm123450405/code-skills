# 版本开发进度看板 — V0.0.2

> 本文件是 `V0.0.2` 版本工作空间的**单一事实来源**。
> 所有 `code-*` 技能在推进工作时,都会同步更新对应的区段。
> 区段填写规则见 `skills/code-version/SKILL.md` 中的"看板字段约定"。

## 文档头
- 版本号:`V0.0.2`
- 创建时间:2026-06-04 12:48
- 最近更新:2026-06-04 17:40
- 创建人:wangmiao
- 负责人:wangmiao
- 状态:活跃
- 描述:V0.0.1 之后的下一个开发版本(基于 V0.0.1 切换,默认继承 V0.0.1 全部已完成功能)
- 当前里程碑:M1:可发布(待开始)

---

## 版本信息

| 字段 | 值 |
| --- | --- |
| 版本号 | `V0.0.2` |
| 创建时间 | 2026-06-04 12:48 |
| 最近更新 | 2026-06-04 17:40 |
| 创建人 | wangmiao |
| 负责人 | wangmiao |
| 状态 | 活跃 |
| 当前里程碑 | M1:可发布(待开始) |
| 预计交付 | — |
| 父版本 | `V0.0.1` |

---

## 里程碑

| 里程碑 | 包含任务范围 | 完成定义 | 状态 | 计划时间 | 实际完成 |
| --- | --- | --- | --- | --- | --- |
| M0:工作空间就绪 | — | 本看板创建 | 已完成 | 2026-06-04 | 2026-06-04 |
| M1:可发布 | 本版本所有任务 | **所有任务开发状态=已完成 且 测试状态∈{已运行-通过, 不适用}** | 待开始 | YYYY-MM-DD | — |

> 完成定义显式列出两轴状态要求,避免把"开发完成"误当"可发布"。

---

## 需求清单

> 写入方:`code-require`(新建/变更/撤回时更新)
> 状态:`待开始` / `进行中` / `已完成` / `已取消` / `阻塞`

| 需求编码 | 标题 | 状态 | 创建时间 | 完成时间 | 需求文档 | 概要设计 | 详细设计 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-00004 | 添加 `/code-dashboard` 开发看板技能 | 已完成(需求分析) | 2026-06-04 12:50 | — | [RESULT.md](require/REQ-00004/RESULT.md) | — | — |
| REQ-00005 | 优化 `code-require` / `code-design` / `code-plan`,增加"首步拉取最新代码"与"末步兜底提交" | 已完成(需求分析) | 2026-06-04 13:33 | — | [RESULT.md](require/REQ-00005/RESULT.md) | — | — |
| REQ-00006 | 增加 `/code-publish` 发布部署技能,生成 DEPLOY.md / UPDATE.md / Q&A.md | 已完成(需求分析) | 2026-06-04 13:45 | — | [RESULT.md](require/REQ-00006/RESULT.md) | — | — |
| REQ-00007 | 增加 `/code-auto` 自动开发技能,驱动 6 子技能 + 评审循环 + 完全无人确认 | 已完成(需求分析) | 2026-06-04 13:59 | — | [RESULT.md](require/REQ-00007/RESULT.md) | — | — |
| REQ-00008 | 优化 `/code-review`,增加"不传入参数"的整版本模式 | 已完成(需求分析) | 2026-06-04 14:07 | — | [RESULT.md](require/REQ-00008/RESULT.md) | — | — |
| REQ-00009 | 优化 `/code-unit`,增加"项目可测性"守卫;不可测时跳过 + 看板标记"不适用" | 已完成(需求分析) | 2026-06-04 14:18 | — | [RESULT.md](require/REQ-00009/RESULT.md) | — | — |
| REQ-00010 | 优化 `/code-it`,增加"前置任务"守卫;按 PLAN.md 登记顺序判定,未完成则中止 + 引导 | 已完成(需求分析) | 2026-06-04 14:36 | — | [RESULT.md](require/REQ-00010/RESULT.md) | — | — |
| REQ-00011 | 优化 `/code-design` / `/code-plan`,增加"设计目标确认"环节;多问分别细化 + 回写 + 下游传导 | 已完成(需求分析) | 2026-06-04 14:57 | — | [RESULT.md](require/REQ-00011/RESULT.md) | — | — |
| REQ-00012 | 创建仓库根 README(中英)+ 移动 CLAUDE.md 到根(极简门面 + 详细子文档) | 已完成(需求分析) | 2026-06-04 15:11 | — | [RESULT.md](require/REQ-00012/RESULT.md) | — | — |
| REQ-00013 | 优化 6 技能(code-require/code-plan/code-fix/code-it/code-unit/code-review/code-auto),启用"编号+标题"显示(从已有内容派生,零规范变更) | 已完成(需求分析) | 2026-06-04 15:25 | — | [RESULT.md](require/REQ-00013/RESULT.md) | — | — |

**统计**:
- 总数:10
- 已完成:10(需求分析阶段已完成,下游 design/plan/it/review 待开展)
- 进行中:0
- 待开始:0
- 已取消:0
- 阻塞:0

> 备注:本表"状态"反映**需求分析(code-require)**阶段是否完成;下游各阶段(概要设计/详细设计/编码/评审)状态在对应区段独立追踪。
> FR/NFR/AC 统计:
> - REQ-00004:10 FR / 7 NFR / 30 AC / 3 项已锁定(Q-1/Q-2/Q-3)+ 2 项已采纳默认(Q-4/Q-5)+ 2 项未采用(Q-7/Q-8)
> - REQ-00005:6 FR / 8 NFR / ~32 AC / 4 项已锁定(Q-1/Q-2/Q-3/Q-4)+ 2 项采纳默认(Q-6/Q-8)+ 2 项未采用(Q-5/Q-7)+ 1 项建议派生(Q-9);用户原文 2 处笔误已纠正(`/code-desgin` → `/code-design`,`/core-require` → `/code-require`)
> - REQ-00006:9 FR / 9 NFR / ~33 AC / 4 项已锁定(Q-1/Q-2/Q-3/Q-4)+ 4 项采纳默认(Q-5/Q-6/Q-7/Q-8/Q-9)+ 1 项建议派生(Q-10);顺带创建项目级 `assistants/qanda/` 目录 + README.md
> - REQ-00007:10 FR / 10 NFR / ~40 AC / 5 项已锁定(Q-1~Q-5)+ 7 项采纳默认(Q-6/Q-7/Q-8/Q-9/Q-10/Q-11/Q-12)+ 1 项建议派生(Q-13);用户原文 1 处笔误已纠正(`/code-desgin` → `/code-design`);新增"第 10 个 `code-*` 技能"作为"编排者"驱动 9 个"被驱动"技能;FR-5 评审循环无轮数上限(Q-1 锁定 A);FR-6 用户确认全选推荐项(Q-4 锁定 A);NFR-4 不引入批量模式(Q-5 锁定 A);NFR-8 不实现增量恢复(Q-11 锁定 A);NFR-10 每步打印进度
> - REQ-00008:9 FR / 8 NFR / ~30 AC / 2 项已锁定(Q-1 仅已完成需求 + Q-2 聚合+单需求双写)+ 5 项采纳默认(Q-3/Q-4/Q-5/Q-6/Q-7)+ 1 项建议派生(Q-8);用户原文 1 处笔误已纠正(`/core-review` → `/code-review`);Q-1 锁定"仅评审'已完成'全周期需求"(未达全周期不评审);Q-2 锁定"双写":聚合 `REVIEW.md` + 单需求 `REVIEW-REPORT.md`,多次执行覆盖;NFR-4 `code-auto` 继续用模式 1;NFR-5 不参与 REQ-00005 改写;NFR-7 评审发现去重(跨需求按 `(需求编码, 描述)`);FR-7 不修改 `code-review` 现有模式 1 行为
> - REQ-00009:7 FR / 8 NFR / ~25 AC / 3 项已锁定(Q-1 只检查项目根构建/测试文件 + Q-2 复用"不适用" + Q-3 不写 test/&lt;任务编码&gt;/RESULT.md)+ 4 项采纳默认(Q-4/Q-5/Q-6/Q-7)+ 1 项建议派生(Q-8);用户原文**无笔误**;Q-1 锁定"守卫 7 项检查清单"(package.json + pyproject.toml + Cargo.toml + go.mod + pom.xml + build.gradle + test/ 目录);Q-2 锁定"复用 V0.0.1 既有'不适用'枚举"(`code-dashboard` 0 改动);Q-3 锁定"跳过时零新增产物"(仅看板写一行);NFR-4 与 `code-dashboard` 0 冲突;NFR-5 与 `code-publish` 0 冲突;NFR-6 与 `code-auto` 退出码兼容(守卫不通过 → 退出码 0)
> - REQ-00010:6 FR / 8 NFR / ~22 AC / 3 项已锁定(Q-1 不新增前置任务列完全按 PLAN.md 登记顺序 + Q-2 只看开发状态 + Q-3 中止+打印推荐执行命令+退出码≠0)+ 4 项采纳默认(Q-4/Q-5/Q-6/Q-7)+ 1 项建议派生(Q-8);用户原文 1 处笔误已纠正(`/core-it` → `/code-it`);Q-1 锁定"**不新增前置任务列,完全按 `PLAN.md` 文件登记顺序判定前置**"(零规范变更,`dashboard-conventions §规则 1` 不触发);Q-2 锁定"只看开发状态"(与 `code-publish` 前置检查同口径);Q-3 锁定"中止 + 打印推荐执行命令 + 退出码 ≠ 0"(`code-auto` 据此中断);NFR-3 零规范变更;NFR-4 与 `code-auto` 退出码兼容(守卫不通过 → 退出码 ≠ 0 → `code-auto` 中断);NFR-6 `PLAN.md` 缺失时守卫通过(退化,不阻止 `code-it`)
> - REQ-00011:9 FR / 8 NFR / ~30 AC / 3 项已锁定(Q-1 都走步骤 0b + Q-2 回写 RESULT.md 顶部"## 设计目标"小节 + Q-3 问多个问题分别细化)+ 5 项采纳默认(Q-4/Q-5/Q-6/Q-7/Q-8)+ 1 项建议派生(Q-9);用户原文 1 处笔误已纠正(`/core-desgin` → `/code-design`);Q-1 锁定"**都走步骤 0b**"(首步拉取之后、设计产出之前,与 REQ-00005 / REQ-00009 / REQ-00010 的"步骤 0a"模式同位叠加);Q-2 锁定"**回写** `RESULT.md` 顶部'## 设计目标' 小节"且**关键补充**"扩展性高的方法需要拆出'扩展架构设计' / '设计模式使用'等更细致任务步骤"(FR-4 据此设计);Q-3 锁定"**问多个问题**"(设计目标 + 4 维度,可分开提问,大需求场景);NFR-3 幂等;NFR-4 不触发 `dashboard-conventions §规则 1`;NFR-5 与 `code-auto` 协同 0 冲突(`code-auto` 仍按"总选推荐项")
> - REQ-00012:7 FR / 8 NFR / ~25 AC / 3 项已锁定(Q-1 只极简概览链到详情 + Q-2 移动 CLAUDE.md 到根 + Q-3 不保留原位置)+ 5 项采纳默认(Q-4/Q-5/Q-6/Q-7/Q-8)+ 1 项建议派生(Q-9);用户原文**无笔误**;Q-1 锁定"**只极简概览 + 链到详情**"(仓库根 README 是门面,`plugins/code-skills/README.md` 是详细);Q-2 锁定"**移动到根目录**"(`plugins/code-skills/CLAUDE.md` → `./CLAUDE.md`);Q-3 锁定"**不保留原位置**";FR-3 AC-3.1 显式 `git mv` 保留 git blame;FR-6 严格遵循 `doc-conventions §规则 1` (中英同次提交 + 章节对仗) / `§规则 2` (核心小节覆盖);NFR-2 < 50 行;NFR-3 git mv 保留历史;NFR-8 不提供重定向/软链
> - REQ-00013:11 FR / 10 NFR / ~30 AC / 3 项已锁定(Q-1 从已有内容派生零规范变更 + Q-2 REQ-00001 · 标题中点格式 + Q-3 字符数≤30 + Q-4 本轮升级 6 技能)+ 6 项采纳默认(Q-5/Q-6/Q-7/Q-8/Q-9/Q-10)+ 1 项建议派生(Q-11);用户原文 5 处笔误已纠正(3 个 `/core-X` → `/code-X` + "缺编" → "缺陷" + 2 处 "是" → "时");Q-1 锁定"**从已有内容派生,不新增字段**"(零规范变更 — `RESULT.md` 第 1 行 + `PLAN.md` 任务总览"标题"列已存在);Q-2 锁定"**`REQ-00001 · 标题`**"(中点 `·` 格式);Q-3 锁定"**字符数 ≤ 30**";Q-4 锁定"**本轮升级 6 技能**"(3 生成源 + 4 消费方,`code-dashboard` 不变因看板标题列已存在);`code-fix` 是 V0.0.0 起的真实存在技能(SKILL.md 17,878 bytes),本轮首次升级;NFR-4 历史自动生效(现有 12 需求 + 19 V0.0.1 任务的"标题"已存在,本轮仅启用"显示"环节)

---

## 概要设计清单

> 写入方:`code-design`(新建/变更时更新)

| 需求编码 | 设计标题 | 状态 | 创建时间 | 完成时间 | 概要设计文档 |
| --- | --- | --- | --- | --- | --- |
| REQ-00004 | 添加 `/code-dashboard` 开发看板技能 | 已完成 | 2026-06-04 15:50 | 2026-06-04 15:50 | [RESULT.md](design/REQ-00004/RESULT.md) |

**统计**:1 / 已完成 1 / 进行中 0

---

## 详细设计与任务计划汇总

> 写入方:`code-plan`(新建/变更/追加任务时更新)

| 需求编码 | 计划标题 | 状态 | 任务总数 | 开发完成 | 测试通过 | 创建时间 | 计划文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-00004 | `/code-dashboard` 只读型开发看板技能 | 草稿 | 3 | 0 | 0 | 2026-06-04 16:10 | [PLAN.md](plan/REQ-00004/PLAN.md) / [RESULT.md](plan/REQ-00004/RESULT.md) |

**统计**:1 个计划 / 共 3 个任务 / 开发完成 3 / 测试通过 0

---

## 任务清单

> 首次登记:`code-plan`(拆分任务时)
> 持续更新:
> - `code-it` 推进 `开发状态`(`待开始` → `进行中` → `已完成`)
> - `code-unit` 推进 `测试状态`(`未编写` → `已编写` → `已运行-通过` / `已运行-失败` / `不适用`)

| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 完成时间 | 提交哈希 | 关联任务 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-REQ-00004-00001 | REQ-00004 | 新增 | 需求新增 | 写 `plugins/code-skills/skills/code-dashboard/SKILL.md` | 已完成 | 不适用 | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 2026-06-04 16:40 | — | — |
| TASK-REQ-00004-00002 | REQ-00004 | 新增 | 需求新增 | (可选)改 `plugins/code-skills/CLAUDE.md` 追加"指引 N: code-dashboard 行为约定" | 已完成 | 不适用 | `plugins/code-skills/CLAUDE.md` | 2026-06-04 16:55 | — | — |
| TASK-REQ-00004-00003 | REQ-00004 | 新增 | 需求新增 | (可选)改 `plugins/code-skills/README.md` + `README.en.md` 技能清单各 +1 行 | 已完成 | 不适用 | `plugins/code-skills/README.md` + `plugins/code-skills/README.en.md` | 2026-06-04 17:12 | — | — |

**统计**:
- 总任务数:3
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):3 / 3
- 开发已完成 / 未完成:3 / 0
- 测试已通过 / 已失败 / 不适用 / 未编写:0 / 0 / 3 / 0

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
| F-001 | REQ-00004 | TASK-REQ-00004-00001 | 正确性 / 可维护性 | 建议改 | SKILL.md 步骤 5"全版本已完成"触发条件不完整(未提及无 P0/P1 缺陷) | —(留作 follow-up) | 待处理 |
| F-002 | REQ-00004 | TASK-REQ-00004-00001 / TASK-REQ-00004-00002 | 一致性 / 规范 | 建议改 | SKILL.md 与 CLAUDE.md 解析锚点正则字面略不一致(`(.+)` vs `.*`) | —(留作 follow-up) | 待处理 |
| F-003 | REQ-00004 | TASK-REQ-00004-00002 | 一致性 / 可维护性 | 建议改 | CLAUDE.md 指引 N 编号占位说明不显式 | —(留作 follow-up) | 待处理 |
| F-004 | REQ-00004 | TASK-REQ-00004-00003 | 详细设计符合度 / 一致性 | 建议改 | README 技能清单"下游"列语义与既有 10 行略不同(引导 vs 被调用) | —(留作 follow-up) | 待处理 |

**统计**:4 / 必须改: 0 / 建议改: 4 / 可选: 0 / 已处理: 0

---

## 派生任务记录

> 写入方:`code-review`(派生"审查改修"任务时)
> 用途:追踪"由 review 派生、关联到原任务"的特殊任务链路

| 派生任务 | 关联原任务 | 派生时间 | review 来源 | 状态 |
| --- | --- | --- | --- | --- |
| (无) | — | — | — | — |

> 本评审 0 条"必须改" → 未派生"审查改修"任务(用户授权"全部留作 follow-up")
> 4 条"建议改"全部记录到 `./assistants/V0.0.2/review/REQ-00004/findings-no-task.md`

---

## 执行的开发命令记录

> 写入方:各 `code-*` 技能在执行编译/启动/测试等命令后追加
> 用途:审计"本版本中跑过哪些命令、结果如何"

| 时间 | 命令 | 工具 | 退出码 | 结果 | 关联任务/阶段 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-04 16:35 | 静态自检 9 项(frontmatter / 节标题 / 步骤齐全 / 边界 E-1~E-10 / NFR-7 禁用词语境 / NFR-6 边界 / 任务编号双格式 / ASCII 字符 / git status) | code-it 步骤 9~10 替代 | 0 | 9/9 通过 | TASK-REQ-00004-00001 |
| 2026-06-04 16:55 | 静态自检 7 项(行数 +8 / 节标题顺序 / Grep 指引 N / 6 子项完整 / git diff 净度 / 未触碰其他段 / NFR-6 严守) | code-it 步骤 9~10 替代 | 0 | 7/7 通过 | TASK-REQ-00004-00002 |
| 2026-06-04 17:12 | 静态自检 7 项(行数各 +1 / 表格末行 / 表格总行数 13:13 / Grep code-dashboard / git diff 净度 / 未触碰其他段 / NFR-6 严守) | code-it 步骤 9~10 替代 | 0 | 7/7 通过 | TASK-REQ-00004-00003 |

---

## 变更记录

> 写入方:所有 `code-*` 技能,在自己的关键节点追加
> 格式:`YYYY-MM-DD HH:mm  <变更类型>  <摘要>  <关联任务/需求>(可选)`

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-04 12:48 | 初始化 | 创建版本 V0.0.2 工作空间(从 V0.0.1 切换) | — |
| 2026-06-04 12:50 | 需求新增 | REQ-00004 需求分析完成(共 10 条 FR / 7 条 NFR / 30 条 AC / 3 项已锁定 Q-1~Q-3 + 2 项采纳默认 Q-4~Q-5 + 2 项未采用 Q-7~Q-8)。范围:新增 `code-dashboard` 只读型技能(无 `Write`/`Edit`/写命令),支持无参数(版本总览:ASCII 进度表 + 文本柱状图)与指定 `REQ-NNNNN`(需求粒度)双粒度;自动生成最多 5 条下一步建议(可执行命令 + 依据 + 优先级);严守 NFR-6 边界(不修改 marketplace.json / plugin.json / 其他 7 SKILL.md / 模板);Q-1 锁定 ASCII 形态,Q-2 锁定可执行命令推荐,Q-3 锁定只突出 P0/P1 | REQ-00004 |
| 2026-06-04 13:33 | 需求新增 | REQ-00005 需求分析完成(共 6 条 FR / 8 条 NFR / ~32 条 AC / 13 个边界场景 / 4 项已锁定 Q-1~Q-4 + 2 项采纳默认 Q-6/Q-8 + 2 项未采用 Q-5/Q-7 + 1 项建议派生 Q-9)。范围:增量修改 `code-require/SKILL.md` + `code-design/SKILL.md` + `code-plan/SKILL.md` 三个技能的"步骤 0 之前"与"末尾"(不改 frontmatter,不改 `code-it` / `code-version` / `code-unit` / `code-review` / `marketplace.json` / `plugin.json` / CLAUDE.md);Q-1 锁定版本不一致时"询问用户二选一"(默认推荐远端),Q-2 锁定 `git pull` 失败时"中断 + 报错退出",Q-3 锁定末尾 commit message "技能自动生成 + 预览确认",Q-4 锁定"保留 `code-it` 内部 commit,本需求末尾兜底提交与之并存,聚焦'过程文件 + 结果文件'";用户原文 2 处笔误已纠正(`/code-desgin` → `/code-design`,`/core-require` → `/code-require`) | REQ-00005 |
| 2026-06-04 13:45 | 需求新增 | REQ-00006 需求分析完成(共 9 条 FR / 9 条 NFR / ~33 条 AC / 10 个边界场景 / 4 项已锁定 Q-1~Q-4 + 4 项采纳默认 Q-5/Q-6/Q-7/Q-8/Q-9 + 1 项建议派生 Q-10)。范围:新增 `code-publish` 技能,前置检查(全检查最严:需求=已完成 ∧ 任务 开发=已完成 ∧ 测试∈{已运行-通过, 不适用} ∧ 缺陷=已修复)通过后,在 `assistants/<版本号>/publish/` 下生成 `DEPLOY.md` + `UPDATE.md`(基线版本跳过) + `Q&A.md`(从 `assistants/qanda/` 聚合);3 份手册均为"通用发布部署骨架 + 最常见部署方式默认内容 + placeholder"(用户必须手动补全);**顺带**在项目级创建 `assistants/qanda/` 目录 + README.md;严守 NFR-4(不参与 REQ-00005 的"首步拉取+末步提交") + NFR-5(通用性优先) + NFR-8(与 `code-dashboard` 数据源一致);`code-publish` 自身**不**自动 commit(留 dirty tree 给用户审阅);Q-1 锁定全检查,Q-2 锁定创建 qanda 骨架,Q-3 锁定基线不生成 UPDATE,Q-4 锁定通用骨架 | REQ-00006 |
| 2026-06-04 13:59 | 需求新增 | REQ-00007 需求分析完成(共 10 条 FR / 10 条 NFR / ~40 条 AC / 10 个边界场景 / 5 项已锁定 Q-1~Q-5 + 7 项采纳默认 Q-6/Q-7/Q-8/Q-9/Q-10/Q-11/Q-12 + 1 项建议派生 Q-13)。范围:**新增第 10 个 `code-*` 技能 `code-auto`,作为"编排者"驱动 9 个"被驱动"技能**;调用序列:`code-require` → `code-design` → `code-plan` → (任务循环:`code-it` + `code-unit`) → `code-review` → (派生任务循环,直到"必须改"列表为空);所有 `AskUserQuestion` 场景**总选推荐项**(完全无人确认,Q-4 锁定 A);异常立即中断 + 报告(Q-2 锁定 A);用户可随时 `Ctrl+C` 中止(中止时输出报告,NFR-7 约定中止时不写 `auto-report.md`);FR-9 完整报告写入 `require/REQ-NNNNN/auto-report.md` 留痕;Q-1 锁定"仅按状态终止"无轮数上限(接受"修改引入新问题"风险),Q-2 锁定"立即中断 + 报告",Q-3 锁定"Ctrl+C 中止 + 报告",Q-4 锁定"总选推荐项",Q-5 锁定"不引入批量模式";严守 NFR-3(`code-auto` 自身不 commit) + NFR-4(不引入批量模式) + NFR-8(不实现增量恢复) + NFR-9(与 REQ-00004/00005/00006 协同) | REQ-00007 |
| 2026-06-04 14:07 | 需求新增 | REQ-00008 需求分析完成(共 9 条 FR / 8 条 NFR / ~30 条 AC / 9 个边界场景 / 2 项已锁定 Q-1/Q-2 + 5 项采纳默认 Q-3/Q-4/Q-5/Q-6/Q-7 + 1 项建议派生 Q-8)。范围:**优化 `/code-review` 技能**(不改 frontmatter,不改模式 1 行为),**增加"无参入口" = 整版本模式**;整版本模式只评审 `状态=已完成` 的需求(Q-1 锁定 B);输出**双写**:聚合 `./assistants/<版本号>/REVIEW.md`(顶层,与 `RESULT.md` 同级)+ 单需求 `./assistants/<版本号>/review/REQ-NNNNN/REVIEW-REPORT.md`(与模式 1 同路径);多次执行 → 全部覆盖(NFR-3 幂等);派生任务**支持**(Q-4 采纳默认),按"必须改"发现追加到对应 `PLAN.md` 任务总览;NFR-4 `code-auto` 继续用模式 1(不触发 `code-auto` 升级);NFR-5 不参与 REQ-00005 改写;NFR-7 评审发现按 `(需求编码, 描述)` 去重;FR-7 不修改模式 1 行为;用户原文 1 处笔误已纠正(`/core-review` → `/code-review`) | REQ-00008 |
| 2026-06-04 14:18 | 需求新增 | REQ-00009 需求分析完成(共 7 条 FR / 8 条 NFR / ~25 条 AC / 8 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3 + 4 项采纳默认 Q-4/Q-5/Q-6/Q-7 + 1 项建议派生 Q-8)。范围:**优化 `/code-unit` 技能**(不改 frontmatter,不改"可测"流程),**新增"步骤 0a 项目可测性检查"守卫**;守卫检查项目根 7 项文件/目录(任一存在 → 可测):`package.json` 含 `scripts.test` / `pyproject.toml` 含测试配置 / `Cargo.toml` / `go.mod` / `pom.xml` / `build.gradle`(.kts) / `test/` 目录(Q-1 锁定 A,只检查项目根);**不可测 → 跳过单测过程** + 看板"任务清单"区段测试状态 = `不适用`(Q-2 锁定 A,**复用 V0.0.1 既有枚举,不新增枚举值**,`code-dashboard` 0 改动)+ **不**写 `test/<任务编码>/RESULT.md`(Q-3 锁定 A,零新增产物);退出码 = 0 让 `code-auto` 继续(NFR-6);用户原文**无笔误**;NFR-4 与 `code-dashboard` 0 冲突;NFR-5 与 `code-publish` 0 冲突(`code-publish` 前置检查"测试∈{已运行-通过, 不适用}"已兼容) | REQ-00009 |
| 2026-06-04 14:36 | 需求新增 | REQ-00010 需求分析完成(共 6 条 FR / 8 条 NFR / ~22 条 AC / 8 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3 + 4 项采纳默认 Q-4/Q-5/Q-6/Q-7 + 1 项建议派生 Q-8)。范围:**优化 `/code-it` 技能**(不改 frontmatter,不改"无前置"流程),**新增"步骤 0a 前置任务检查"守卫**;Q-1 锁定"**不新增前置任务列,完全按 `PLAN.md` 文件登记顺序判定前置**"(零规范变更 — `PLAN.md` 模板/看板均不变,`dashboard-conventions §规则 1` 不触发);Q-2 锁定"只看开发状态"(与 `code-publish` 前置检查同口径);Q-3 锁定"中止 + 打印推荐执行命令 + 退出码 ≠ 0"(`code-auto` 据此中断;中止报告含"⛔ code-it 中止(存在未完成的前置任务)"+ 所有前置状态+ "推荐执行 /code-it <第一个未完成> 完成后,再执行 /code-it <当前任务>");用户原文 1 处笔误已纠正(`/core-it` → `/code-it`);NFR-3 零规范变更;NFR-4 与 `code-auto` 退出码兼容(守卫不通过 → 退出码 ≠ 0 → `code-auto` 中断);NFR-6 `PLAN.md` 缺失时守卫通过(退化,不阻止 `code-it`);FR-4 不修改 `code-auto`(本需求守卫作为"双保险"与 `code-auto` 现有"按序"逻辑协同) | REQ-00010 |
| 2026-06-04 14:57 | 需求新增 | REQ-00011 需求分析完成(共 9 条 FR / 8 条 NFR / ~30 条 AC / 10 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3 + 5 项采纳默认 Q-4/Q-5/Q-6/Q-7/Q-8 + 1 项建议派生 Q-9)。范围:**优化 `/code-design` + `/code-plan` 2 个技能**(不改 frontmatter,不改"无设计目标"流程),**新增"步骤 0b 设计目标确认"环节**;Q-1 锁定"**都走步骤 0b**"(首步拉取之后、设计产出之前,与 REQ-00005 / REQ-00009 / REQ-00010 的"步骤 0a"模式同位叠加);Q-2 锁定"**回写** `RESULT.md` 顶部'## 设计目标' 小节"且**关键补充**"扩展性高的方法需要拆出'扩展架构设计' / '设计模式使用'等更细致任务步骤"(FR-4 据此设计);Q-3 锁定"**问多个问题**"(设计目标 + 4 维度,可分开提问,大需求场景);用户原文 1 处笔误已纠正(`/core-desgin` → `/code-design`);FR-2 `code-plan` 读 `design/.../RESULT.md` 的"## 设计目标"小节并沿用(不重新问);FR-3 `code-plan` 读不到时退化(回退到用户手动确认 + 仅写 `plan/.../RESULT.md`);FR-4 `code-plan` 据"设计目标"调整任务拆分粒度(扩展性高 → 加"扩展架构设计"等任务);FR-5 回写"## 设计目标"小节结构(整体 3 选项 + 4 维度优先级 + 回写时间 + 回写触发);NFR-3 幂等;NFR-4 不触发 `dashboard-conventions §规则 1`;NFR-5 与 `code-auto` 协同 0 冲突(`code-auto` 仍按"总选推荐项") | REQ-00011 |
| 2026-06-04 15:11 | 需求新增 | REQ-00012 需求分析完成(共 7 条 FR / 8 条 NFR / ~25 条 AC / 9 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3 + 5 项采纳默认 Q-4/Q-5/Q-6/Q-7/Q-8 + 1 项建议派生 Q-9)。范围:**新建仓库根 `./README.md` + `./README.en.md`**(极简 < 50 行,中英同次提交,`doc-conventions §规则 1` 严格遵循),**移动 `plugins/code-skills/CLAUDE.md` → `./CLAUDE.md`**(git mv 保留历史,原位置**不保留**);仓库根 README 是"门面",`plugins/code-skills/README.md` 保留作为"详细技能文档";NFR-2 < 50 行;NFR-3 git mv 保留 blame;NFR-8 不提供重定向/软链;用户原文**无笔误** | REQ-00012 |
| 2026-06-04 15:25 | 需求新增 | REQ-00013 需求分析完成(共 11 条 FR / 10 条 NFR / ~30 条 AC / 9 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3/Q-4 + 6 项采纳默认 Q-5/Q-6/Q-7/Q-8/Q-9/Q-10 + 1 项建议派生 Q-11)。范围:**优化 6 技能** `code-require`/`code-plan`/`code-fix`/`code-it`/`code-unit`/`code-review`/`code-auto`(其中 `code-fix` 是 V0.0.0 起的真实存在技能,SKILL.md 17,878 bytes,本轮**首次**升级),**统一启用"编号+标题"显示**(格式 `REQ-00001 · 标题` / `TASK-... · 标题` / `BUG-NNNNN · 标题`);Q-1 锁定"从已有内容派生,不新增字段"(零规范变更 — `RESULT.md` 第 1 行 + `PLAN.md` 任务总览"标题"列已存在);Q-2 锁定"`REQ-00001 · 标题`"(中点 `·` 格式);Q-3 锁定"字符数 ≤ 30";Q-4 锁定"本轮升级 6 技能"(`code-dashboard` 不变因看板标题列已存在);用户原文 5 处笔误已纠正;NFR-4 历史自动生效;NFR-5 `code-publish` 报告升级;NFR-6 不改 4 技能 | REQ-00013 |
| 2026-06-04 15:50 | 设计新增 | REQ-00004 概要设计完成(共 8 个关键设计问题 Q-1~Q-8 + 4 段总览 + 5 段需求粒度 + 10 项边界 + 0 新增依赖 + 30 AC 全继承)。范围:新增 `code-dashboard` 单文件技能(`plugins/code-skills/skills/code-dashboard/SKILL.md`);SKILL.md 章节结构完全复用既有 10 个 `code-*` 骨架(目标 / 适用 / 不适用 / 目录 / 输入 / 输出 / 工具 / 步骤 / 边界 / 衔接 / 不要做);**不**修改 marketplace.json / plugin.json / 其他 10 SKILL.md frontmatter(NFR-6 严守);**不**新增 `templates/` / `checklists/` / `guidelines/` 子目录(无独立资源);**不**引入运行时依赖(NFR-1 锁零依赖);解析器单遍扫描 + 行号锚点;任务编号解析双格式兼容(新格式优先 + 旧格式透传,NFR-3);建议生成器 5 类优先级 + 最多 5 条;ASCII 比例条固定 12 字符 + `█` / `░` / `▓`;性能估算 < 1 秒(NFR-4 远低于 5 秒);Q-D1/2/3/4 本轮新增默认(显示策略 / 不读评审发现段 / 12 字符宽度 / 需求模式不折叠);遵循 9 个规范文件(详见 `design/REQ-00004/rule-compliance.md`),3 项用户授权偏离(A-1 单文件 / A-2 不改 marketplace / A-3 无历史版本切换) | REQ-00004 |
| 2026-06-04 16:10 | 设计新增 | REQ-00004 详细设计与编码计划完成(共 6 个可直接编码算法 算法 0~5 + 8 个内存数据结构 + 3 条任务 T-001 必 + T-002/T-003 可 + 1 个里程碑 M3 可发布)。范围:详细设计 14 节(概述 / 上游引用 / 规范遵循 / 模块详细化 / 算法与逻辑 / 数据结构 / 接口细节 / 异常处理 / 安全 / 状态机 / 性能 / 测试要点 / 关联 / 待澄清 / 变更记录);PLAN.md 8 节(计划概述 / 任务总览 / 任务详情 / 任务依赖图 / 里程碑 / 状态管理规则 / 关联计划 / 变更记录);3 项本阶段新增偏离(P-A1 状态字面不归一化 / P-A2 测试状态=不适用 / P-A3 需求模式不显示里程碑);测试状态全部 `不适用`(P-A2 锁定,纯 Markdown 指令无单元测试载体);M3 完成定义=所有任务开发状态=已完成 | REQ-00004 |
| 2026-06-04 16:40 | 开发状态更新 | T-001 状态"待开始"→"已完成"(新增 `plugins/code-skills/skills/code-dashboard/SKILL.md`,367 行,单文件);YAML frontmatter 完整(`name: code-dashboard` + 完整 `description`)+ 12 节正文严格对齐既有 10 个 `code-*` 骨架 + 步骤 0~6 齐全 + 边界 E-1~E-10 完整覆盖 + NFR-7 禁用词 4 处均在"不调用"上下文 + NFR-6 边界 2 处均在"不动"上下文 + 任务编号双格式正则严格按 `encoding-conventions §规则 1/3` + 6 项 design/plan 偏离全部落地;静态自检 9/9 通过;`git status` 净度:NFR-6 严守(`marketplace.json` / `plugin.json` / 其他 10 SKILL.md frontmatter 全部未改);提交哈希待用户后续 `git commit` 生成 | TASK-REQ-00004-00001 |
| 2026-06-04 16:55 | 开发状态更新 | T-002 状态"待开始"→"已完成"(修改 `plugins/code-skills/CLAUDE.md` 追加 8 行:`### 指引 N: code-dashboard 行为约定` + 6 个子项;134 → 142 行,纯追加无任何已有行修改);用户授权依据:PLAN.md 行 194 "用户在 `code-it` 阶段明确授权" + 用户主动调用 `code-it REQ-00004-002` 即为信号;接受 `code-rule` 后续覆盖本段的风险(由 CLAUDE.md 显式声明);静态自检 7/7 通过;git diff 净度:`marketplace.json` / `plugin.json` / 其他 10 SKILL.md 全部未触碰;6 个子项内容与 T-001 落地的 SKILL.md 行为**完全一致** | TASK-REQ-00004-00002 |
| 2026-06-04 17:12 | 开发状态更新 | T-003 状态"待开始"→"已完成"(修改 `plugins/code-skills/README.md` + `README.en.md` 各追加 1 行:`code-dashboard` 在 `code-review` 之后;883 → 884 行,纯追加无任何已有行修改);保留 5 列结构(与既有 10 行严格对仗;与 PLAN.md 4 列字面偏离,理由:`doc-conventions §规则 1` 严守);中英同次提交(同一消息块 Edit);用户授权依据:PLAN.md 行 231 + 用户主动调用 `code-it TASK-REQ-00004-00003`;静态自检 7/7 通过;git diff 净度:`marketplace.json` / `plugin.json` / 其他 10 SKILL.md 全部未触碰;**本需求 3 任务全部完成,M3 里程碑达成**(开发完成度 3/3,真正可发布 3/3) | TASK-REQ-00004-00003 |
| 2026-06-04 17:40 | 评审发现 | REQ-00004 评审完成(共 3 任务 / 4 维度检查 / 0 必须改 / 4 建议改全部留作 follow-up / 0 派生任务);整体结论 ✅ 通过(无阻塞,REVIEW 完整);评审产物 4 件:REVIEW-REPORT.md(整体) + work-log.md(过程) + review-checklist-applied.md(清单应用) + findings-no-task.md(4 条建议改详情);F-001 SKILL.md 步骤 5 触发条件不完整 / F-002 SKILL.md 与 CLAUDE.md 解析锚点正则字面不一致 / F-003 CLAUDE.md 指引 N 编号占位说明不显 / F-004 README 下游列语义与既有 10 行不同 | REQ-00004 |

---

## 索引:本版本所有文件

- 需求:`./assistants/V0.0.2/require/<需求编号>/RESULT.md` × N
  - REQ-00004 → [require/REQ-00004/RESULT.md](require/REQ-00004/RESULT.md)
  - REQ-00005 → [require/REQ-00005/RESULT.md](require/REQ-00005/RESULT.md)
  - REQ-00006 → [require/REQ-00006/RESULT.md](require/REQ-00006/RESULT.md)
  - REQ-00007 → [require/REQ-00007/RESULT.md](require/REQ-00007/RESULT.md)
  - REQ-00008 → [require/REQ-00008/RESULT.md](require/REQ-00008/RESULT.md)
  - REQ-00009 → [require/REQ-00009/RESULT.md](require/REQ-00009/RESULT.md)
  - REQ-00010 → [require/REQ-00010/RESULT.md](require/REQ-00010/RESULT.md)
  - REQ-00011 → [require/REQ-00011/RESULT.md](require/REQ-00011/RESULT.md)
  - REQ-00012 → [require/REQ-00012/RESULT.md](require/REQ-00012/RESULT.md)
  - REQ-00013 → [require/REQ-00013/RESULT.md](require/REQ-00013/RESULT.md)
- 概要设计:`./assistants/V0.0.2/design/<需求编号>/RESULT.md` × N
- 详细设计:`./assistants/V0.0.2/plan/<需求编号>/RESULT.md` × N
- 任务计划:`./assistants/V0.0.2/plan/<需求编号>/PLAN.md` × N
- 过程文档:`./assistants/V0.0.2/plan/<需求编号>/*.md` × N
- 代码改修正文:`./assistants/V0.0.2/code/<任务编码>/RESULT.md` × N
- 测试改修正文:`./assistants/V0.0.2/test/<任务编码>/RESULT.md` × N
- 评审报告:`./assistants/V0.0.2/review/<需求编号>/REVIEW-REPORT.md` × N
- 审查改修任务:`./assistants/V0.0.2/review/<任务编码>/RESULT.md` × N

过程文档(本需求):
- [require/REQ-00004/materials-index.md](require/REQ-00004/materials-index.md)
- [require/REQ-00004/clarifications.md](require/REQ-00004/clarifications.md)
- [require/REQ-00004/related-requirements.md](require/REQ-00004/related-requirements.md)

过程文档(本需求):
- [require/REQ-00005/materials-index.md](require/REQ-00005/materials-index.md)
- [require/REQ-00005/clarifications.md](require/REQ-00005/clarifications.md)
- [require/REQ-00005/related-requirements.md](require/REQ-00005/related-requirements.md)

过程文档(本需求):
- [require/REQ-00006/materials-index.md](require/REQ-00006/materials-index.md)
- [require/REQ-00006/clarifications.md](require/REQ-00006/clarifications.md)
- [require/REQ-00006/related-requirements.md](require/REQ-00006/related-requirements.md)

过程文档(本需求):
- [require/REQ-00007/materials-index.md](require/REQ-00007/materials-index.md)
- [require/REQ-00007/clarifications.md](require/REQ-00007/clarifications.md)
- [require/REQ-00007/related-requirements.md](require/REQ-00007/related-requirements.md)

过程文档(本需求):
- [require/REQ-00008/materials-index.md](require/REQ-00008/materials-index.md)
- [require/REQ-00008/clarifications.md](require/REQ-00008/clarifications.md)
- [require/REQ-00008/related-requirements.md](require/REQ-00008/related-requirements.md)

过程文档(本需求):
- [require/REQ-00009/materials-index.md](require/REQ-00009/materials-index.md)
- [require/REQ-00009/clarifications.md](require/REQ-00009/clarifications.md)
- [require/REQ-00009/related-requirements.md](require/REQ-00009/related-requirements.md)

过程文档(本需求):
- [require/REQ-00010/materials-index.md](require/REQ-00010/materials-index.md)
- [require/REQ-00010/clarifications.md](require/REQ-00010/clarifications.md)
- [require/REQ-00010/related-requirements.md](require/REQ-00010/related-requirements.md)


过程文档(本需求):
- [require/REQ-00012/materials-index.md](require/REQ-00012/materials-index.md)
- [require/REQ-00012/clarifications.md](require/REQ-00012/clarifications.md)
- [require/REQ-00012/related-requirements.md](require/REQ-00012/related-requirements.md)

过程文档(本需求):
- [require/REQ-00013/materials-index.md](require/REQ-00013/materials-index.md)
- [require/REQ-00013/clarifications.md](require/REQ-00013/clarifications.md)
- [require/REQ-00013/related-requirements.md](require/REQ-00013/related-requirements.md)
过程文档(本需求):
- [require/REQ-00011/materials-index.md](require/REQ-00011/materials-index.md)
- [require/REQ-00011/clarifications.md](require/REQ-00011/clarifications.md)
- [require/REQ-00011/related-requirements.md](require/REQ-00011/related-requirements.md)
