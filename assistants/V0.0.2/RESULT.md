# 版本开发进度看板 — V0.0.2

> 本文件是 `V0.0.2` 版本工作空间的**单一事实来源**。
> 所有 `code-*` 技能在推进工作时,都会同步更新对应的区段。
> 区段填写规则见 `skills/code-version/SKILL.md` 中的"看板字段约定"。

## 文档头
- 版本号:`V0.0.2`
- 创建时间:2026-06-04 12:48
- 最近更新:2026-06-04 18:13
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
| 最近更新 | 2026-06-04 18:13 |
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
| M1-REQ-00006-1:模板就绪 | T-002 ~ T-006(REQ-00006) | 5 份模板开发状态=已完成,测试状态全 `不适用` | 待开始 | 2026-06-05 | — |
| M1-REQ-00006-2:技能可触发 | M1-REQ-00006-1 + T-001(REQ-00006) | `code-publish` 技能可被 Claude Code 触发,工作流 7 步骤走通 | 待开始 | 2026-06-06 | — |
| M1:可发布 | 本版本所有任务(含 REQ-00006 全部 8 任务 + 其他 9 需求 ~> 未来任务) | **所有任务开发状态=已完成 且 测试状态∈{已运行-通过, 不适用}** | 待开始 | YYYY-MM-DD | — |

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
> - REQ-00005:6 FR / 8 NFR / ~32 AC / 4 项已锁定(Q-1/Q-2/Q-3/Q-4)+ 2 项采纳默认(Q-6/Q-8)+ 2 项未采用(Q-5/Q-7)+ 1 项建议派生(Q-9);用户原文 2 处笔误已纠正(`/code-desgin` → `/code-design`,`/code-require` → `/code-require`)
> - REQ-00006:9 FR / 9 NFR / ~33 AC / 4 项已锁定(Q-1/Q-2/Q-3/Q-4)+ 4 项采纳默认(Q-5/Q-6/Q-7/Q-8/Q-9)+ 1 项建议派生(Q-10);顺带创建项目级 `assistants/qanda/` 目录 + README.md
> - REQ-00007:10 FR / 10 NFR / ~40 AC / 5 项已锁定(Q-1~Q-5)+ 7 项采纳默认(Q-6/Q-7/Q-8/Q-9/Q-10/Q-11/Q-12)+ 1 项建议派生(Q-13);用户原文 1 处笔误已纠正(`/code-desgin` → `/code-design`);新增"第 10 个 `code-*` 技能"作为"编排者"驱动 9 个"被驱动"技能;FR-5 评审循环无轮数上限(Q-1 锁定 A);FR-6 用户确认全选推荐项(Q-4 锁定 A);NFR-4 不引入批量模式(Q-5 锁定 A);NFR-8 不实现增量恢复(Q-11 锁定 A);NFR-10 每步打印进度
> - REQ-00008:9 FR / 8 NFR / ~30 AC / 2 项已锁定(Q-1 仅已完成需求 + Q-2 聚合+单需求双写)+ 5 项采纳默认(Q-3/Q-4/Q-5/Q-6/Q-7)+ 1 项建议派生(Q-8);用户原文 1 处笔误已纠正(`/code-review` → `/code-review`);Q-1 锁定"仅评审'已完成'全周期需求"(未达全周期不评审);Q-2 锁定"双写":聚合 `REVIEW.md` + 单需求 `REVIEW-REPORT.md`,多次执行覆盖;NFR-4 `code-auto` 继续用模式 1;NFR-5 不参与 REQ-00005 改写;NFR-7 评审发现去重(跨需求按 `(需求编码, 描述)`);FR-7 不修改 `code-review` 现有模式 1 行为
> - REQ-00009:7 FR / 8 NFR / ~25 AC / 3 项已锁定(Q-1 只检查项目根构建/测试文件 + Q-2 复用"不适用" + Q-3 不写 test/&lt;任务编码&gt;/RESULT.md)+ 4 项采纳默认(Q-4/Q-5/Q-6/Q-7)+ 1 项建议派生(Q-8);用户原文**无笔误**;Q-1 锁定"守卫 7 项检查清单"(package.json + pyproject.toml + Cargo.toml + go.mod + pom.xml + build.gradle + test/ 目录);Q-2 锁定"复用 V0.0.1 既有'不适用'枚举"(`code-dashboard` 0 改动);Q-3 锁定"跳过时零新增产物"(仅看板写一行);NFR-4 与 `code-dashboard` 0 冲突;NFR-5 与 `code-publish` 0 冲突;NFR-6 与 `code-auto` 退出码兼容(守卫不通过 → 退出码 0)
> - REQ-00010:6 FR / 8 NFR / ~22 AC / 3 项已锁定(Q-1 不新增前置任务列完全按 PLAN.md 登记顺序 + Q-2 只看开发状态 + Q-3 中止+打印推荐执行命令+退出码≠0)+ 4 项采纳默认(Q-4/Q-5/Q-6/Q-7)+ 1 项建议派生(Q-8);用户原文 1 处笔误已纠正(`/code-it` → `/code-it`);Q-1 锁定"**不新增前置任务列,完全按 `PLAN.md` 文件登记顺序判定前置**"(零规范变更,`dashboard-conventions §规则 1` 不触发);Q-2 锁定"只看开发状态"(与 `code-publish` 前置检查同口径);Q-3 锁定"中止 + 打印推荐执行命令 + 退出码 ≠ 0"(`code-auto` 据此中断);NFR-3 零规范变更;NFR-4 与 `code-auto` 退出码兼容(守卫不通过 → 退出码 ≠ 0 → `code-auto` 中断);NFR-6 `PLAN.md` 缺失时守卫通过(退化,不阻止 `code-it`)
> - REQ-00011:9 FR / 8 NFR / ~30 AC / 3 项已锁定(Q-1 都走步骤 0b + Q-2 回写 RESULT.md 顶部"## 设计目标"小节 + Q-3 问多个问题分别细化)+ 5 项采纳默认(Q-4/Q-5/Q-6/Q-7/Q-8)+ 1 项建议派生(Q-9);用户原文 1 处笔误已纠正(`/code-desgin` → `/code-design`);Q-1 锁定"**都走步骤 0b**"(首步拉取之后、设计产出之前,与 REQ-00005 / REQ-00009 / REQ-00010 的"步骤 0a"模式同位叠加);Q-2 锁定"**回写** `RESULT.md` 顶部'## 设计目标' 小节"且**关键补充**"扩展性高的方法需要拆出'扩展架构设计' / '设计模式使用'等更细致任务步骤"(FR-4 据此设计);Q-3 锁定"**问多个问题**"(设计目标 + 4 维度,可分开提问,大需求场景);NFR-3 幂等;NFR-4 不触发 `dashboard-conventions §规则 1`;NFR-5 与 `code-auto` 协同 0 冲突(`code-auto` 仍按"总选推荐项")
> - REQ-00012:7 FR / 8 NFR / ~25 AC / 3 项已锁定(Q-1 只极简概览链到详情 + Q-2 移动 CLAUDE.md 到根 + Q-3 不保留原位置)+ 5 项采纳默认(Q-4/Q-5/Q-6/Q-7/Q-8)+ 1 项建议派生(Q-9);用户原文**无笔误**;Q-1 锁定"**只极简概览 + 链到详情**"(仓库根 README 是门面,`plugins/code-skills/README.md` 是详细);Q-2 锁定"**移动到根目录**"(`plugins/code-skills/CLAUDE.md` → `./CLAUDE.md`);Q-3 锁定"**不保留原位置**";FR-3 AC-3.1 显式 `git mv` 保留 git blame;FR-6 严格遵循 `doc-conventions §规则 1` (中英同次提交 + 章节对仗) / `§规则 2` (核心小节覆盖);NFR-2 < 50 行;NFR-3 git mv 保留历史;NFR-8 不提供重定向/软链
> - REQ-00013:11 FR / 10 NFR / ~30 AC / 3 项已锁定(Q-1 从已有内容派生零规范变更 + Q-2 REQ-00001 · 标题中点格式 + Q-3 字符数≤30 + Q-4 本轮升级 6 技能)+ 6 项采纳默认(Q-5/Q-6/Q-7/Q-8/Q-9/Q-10)+ 1 项建议派生(Q-11);用户原文 5 处笔误已纠正(3 个 `/code-X` → `/code-X` + "缺编" → "缺陷" + 2 处 "是" → "时");Q-1 锁定"**从已有内容派生,不新增字段**"(零规范变更 — `RESULT.md` 第 1 行 + `PLAN.md` 任务总览"标题"列已存在);Q-2 锁定"**`REQ-00001 · 标题`**"(中点 `·` 格式);Q-3 锁定"**字符数 ≤ 30**";Q-4 锁定"**本轮升级 6 技能**"(3 生成源 + 4 消费方,`code-dashboard` 不变因看板标题列已存在);`code-fix` 是 V0.0.0 起的真实存在技能(SKILL.md 17,878 bytes),本轮首次升级;NFR-4 历史自动生效(现有 12 需求 + 19 V0.0.1 任务的"标题"已存在,本轮仅启用"显示"环节)

---

## 概要设计清单

> 写入方:`code-design`(新建/变更时更新)

| 需求编码 | 设计标题 | 状态 | 创建时间 | 完成时间 | 概要设计文档 |
| --- | --- | --- | --- | --- | --- |
| REQ-00004 | 添加 `/code-dashboard` 开发看板技能 | 已完成 | 2026-06-04 15:50 | 2026-06-04 15:50 | [RESULT.md](design/REQ-00004/RESULT.md) |
| REQ-00006 | `/code-publish` 发布部署技能(7 模块 + 5 模板 + 0 修改 + 0 依赖) | 已完成(首次) | 2026-06-04 16:48 | 2026-06-04 16:48 | [RESULT.md](design/REQ-00006/RESULT.md) |

**统计**:2 / 已完成 2 / 进行中 0

---

## 详细设计与任务计划汇总

> 写入方:`code-plan`(新建/变更/追加任务时更新)

| 需求编码 | 计划标题 | 状态 | 任务总数 | 开发完成 | 测试通过 | 创建时间 | 计划文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-00004 | `/code-dashboard` 只读型开发看板技能 | 已完成(详细设计) | 2026-06-04 12:50 | 3 | 3 | 0 | [PLAN.md](plan/REQ-00004/PLAN.md) / [RESULT.md](plan/REQ-00004/RESULT.md) |
| REQ-00005 | 优化 `code-require` / `code-design` / `code-plan`,增加"首步拉取最新代码"与"末步兜底提交" | 已完成(详细设计) | 2026-06-04 16:00 | 5 | 5 | 0 | [PLAN.md](plan/REQ-00005/PLAN.md) |
| REQ-00006 | `/code-publish` 发布部署技能(7 模块 + 5 模板 + 双 README 同步 + 自检) | **已完成** | 8 | 8 | 0 | 2026-06-04 17:01 | [RESULT.md](plan/REQ-00006/RESULT.md) / [PLAN.md](plan/REQ-00006/PLAN.md) |

**统计**:3 个计划 / 共 16 个任务 / **开发完成 16 ✅** / 测试通过 0 / **真正可发布 16 / 16 ✅**(任务全部测试状态预设 `不适用` — 纯文档型)

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
| TASK-REQ-00005-00001 | REQ-00005 | 修改 | 需求新增 | `code-require/SKILL.md` 增量追加 步骤 0a + 0b + N | 已完成 | 不适用 | `plugins/code-skills/skills/code-require/SKILL.md` | 2026-06-04 16:50 | a157d7b | — |
| TASK-REQ-00005-00002 | REQ-00005 | 修改 | 需求新增 | `code-design/SKILL.md` 增量追加 步骤 0a + N | 已完成 | 不适用 | `plugins/code-skills/skills/code-design/SKILL.md` | 2026-06-04 17:00 | 3e1573e | — |
| TASK-REQ-00005-00003 | REQ-00005 | 修改 | 需求新增 | `code-plan/SKILL.md` 增量追加 步骤 0a + N | 已完成 | 不适用 | `plugins/code-skills/skills/code-plan/SKILL.md` | 2026-06-04 17:10 | e568328 | — |
| TASK-REQ-00005-00004 | REQ-00005 | 文档 | 需求新增 | 同步 V0.0.2/RESULT.md 看板 | 已完成 | 不适用 | assistants/V0.0.2/RESULT.md | 2026-06-04 17:20 | 1171d98 | — |
| TASK-REQ-00005-00005 | REQ-00005 | 修改 | 审查改修 | 回填 T-004 RESULT.md 的提交哈希 | 已完成 | 不适用 | code/TASK-REQ-00005-00004/RESULT.md | 2026-06-04 17:54 | e5c4dcd | T-004 |
| `TASK-REQ-00006-00001` | REQ-00006 | 新增 | 需求新增 | [新增] 写 `code-publish/SKILL.md`(7 模块工作流 + frontmatter) | 已完成 | 不适用 | `plugins/code-skills/skills/code-publish/SKILL.md` | 2026-06-04 17:30 | (不提交) | — |
| `TASK-REQ-00006-00002` | REQ-00006 | 新增 | 需求新增 | [新增] 写 `templates/DEPLOY.md` 模板(8 章节 + placeholder + 默认示例) | 已完成 | 不适用 | `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` | 2026-06-04 17:34 | (不提交) | — |
| `TASK-REQ-00006-00003` | REQ-00006 | 新增 | 需求新增 | [新增] 写 `templates/UPDATE.md` 模板(8 章节 + §8 回滚) | 已完成 | 不适用 | `plugins/code-skills/skills/code-publish/templates/UPDATE.md` | 2026-06-04 17:45 | (不提交) | — |
| `TASK-REQ-00006-00004` | REQ-00006 | 新增 | 需求新增 | [新增] 写 `templates/Q&A.md` 模板(占位章节 + 提示) | 已完成 | 不适用 | `plugins/code-skills/skills/code-publish/templates/Q&A.md` | 2026-06-04 17:52 | (不提交) | — |
| `TASK-REQ-00006-00005` | REQ-00006 | 新增 | 需求新增 | [新增] 写 `templates/qanda-README.md` 模板(用途/命名/引用/维护) | 已完成 | 不适用 | `plugins/code-skills/skills/code-publish/templates/qanda-README.md` | 2026-06-04 17:56 | (不提交) | — |
| `TASK-REQ-00006-00006` | REQ-00006 | 新增 | 需求新增 | [新增] 写 `templates/assistants-layout.md` 模板(沿用范式 + publish/qanda 段) | 已完成 | 不适用 | `plugins/code-skills/skills/code-publish/templates/assistants-layout.md` | 2026-06-04 18:00 | (不提交) | — |
| `TASK-REQ-00006-00007` | REQ-00006 | 文档 | 需求新增 | [文档] 不变量自检 + 同步 V0.0.2 看板 + 偏差日志 | 已完成 | 不适用 | `assistants/V0.0.2/RESULT.md` + `code/TASK-REQ-00006-00007/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | 2026-06-04 18:03 | (不提交) | — |
| `TASK-REQ-00006-00008` | REQ-00006 | 修改 | 需求新增 | [修改] 同步双 README "主要能力" 段(中英同次提交) | 已完成 | 不适用 | `plugins/code-skills/README.md`, `plugins/code-skills/README.en.md` | 2026-06-04 18:08 | (不提交) | — |
| `TASK-REQ-00006-00009` | REQ-00006 | 修改 | 审查改修 | [修改] 修订双 README `<code-publish>` 行措辞(明确"首次调用"语义) | 已完成 | 不适用 | `plugins/code-skills/README.md`, `plugins/code-skills/README.en.md` | 2026-06-04 18:13 | (不提交) | `TASK-REQ-00006-00008` |

**统计**:
- 总任务数:17
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):17 / 17 ✅
- 开发已完成 / 未完成:17 / 0
- 测试已通过 / 已失败 / 不适用 / 未编写:0 / 0 / 16 / 1

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
| F-005 (I-001) | REQ-00005 | T-001 | 可维护性 | 可选 | 3 个 SKILL.md 步骤 0a 章节内容几乎完全相同;DRY 违反,但接受(3 独立技能) | — | 已接受 |
| F-006 (I-002) | REQ-00005 | T-001 | 可维护性 | 可选 | 步骤 0a 列举大量 stderr 关键词字符串;NFR-5 透传 stderr 兜底 | — | 已接受 |
| F-007 (I-003) | REQ-00005 | T-002 | 一致性 | 可选 | 章节注释"`code-design` **不**含步骤 0b"是有意防御性提示 | — | 已接受 |
| F-008 (I-004) | REQ-00005 | T-003 | 文档同步 | 可选 | T-003 步骤 N commit 模板"结果文件 2"与 T-001 "结果文件 1"差异;有意(`code-plan` 唯一 2 结果文件) | — | 已接受 |
| F-009 (W-002) | REQ-00005 | T-004 | 文档与代码同步 | 建议改 | T-004 RESULT.md 文档头 + §3.1 表格"提交哈希"字段显示 `<TBD>`,实际 hash `1171d98ef51e5910f4b8567794bada77397042d4` 未回填 | TASK-REQ-00005-00005 | 已处理(2026-06-04 17:54) |
| F-010 | REQ-00006 | T-001 | 一致性 / 可维护性 | 建议改 | SKILL.md "## 报告模板" 中 S-6 强制发布场景与"## 不要做的事" 第 8 条(v1 不实现 --force)口径不一致 | (留 findings-no-task.md) | v2 follow-up |
| F-011 | REQ-00006 | T-008 | 规范遵循 / 一致性 | **必须改** | `README.md` L38 + `README.en.md` L38 `<code-publish>` 行 "用途"列"顺带在项目级创建 `assistants/qanda/` 目录" 措辞误导(实际仅首次调用时创建) | **T-009** | **已完成** |
| F-012 | REQ-00006 | T-002 | 设计符合度(规范内偏离) | 建议改 | DEPLOY.md §7 placeholder 拆分偏离已记录,但 `data-changes.md §4.1` 章节 7 需同步标注 | (留 findings-no-task.md) | v2 follow-up |
| F-013 | REQ-00006 | T-006 | 一致性 | 可选 | assistants-layout.md 范式与 code-version 略有不同(简化了"目录粒度对比"表) | (留 findings-no-task.md) | v2 整体范式更新时处理 |
| F-014 | REQ-00006 | T-001 | 安全 | 建议改 | SKILL.md 步骤 2.6 QandaAggregator 应显式提示 qanda/ 内容的 XSS 风险 + 解释为什么不防 | (留 findings-no-task.md) | v2 整体安全审视时处理 |
| F-015 | REQ-00006 | T-006 / T-001 | 一致性 / 可维护性 | 建议改 | SKILL.md §工作目录约定 应补充"5 模板在项目级(不进入版本工作空间)"说明 | (留 findings-no-task.md) | v2 整体审视时处理 |
| F-016 | REQ-00006 | T-005 | 可维护性 | 建议改 | qanda-README.md 应加"以模板为准"维护说明(避免循环引用导致的不同步) | (留 findings-no-task.md) | v2 整体审视时处理 |
| F-017 | REQ-00006 | T-007 / T-008 | 可维护性 | 可选 | T-007 与 T-008 自检流程部分重叠;v2 应设计统一自检脚本 | (留 findings-no-task.md) | v2 整体流程优化时处理 |

**统计**:17 / **必须改: 1 / 建议改: 9 / 可选: 6** / 已处理: 2(派生 T-005 已完成;派生 T-009 已完成)

---

## 派生任务记录

> 写入方:`code-review`(派生"审查改修"任务时)
> 用途:追踪"由 review 派生、关联到原任务"的特殊任务链路

| 派生任务 | 关联原任务 | 派生时间 | review 来源 | 状态 |
| --- | --- | --- | --- | --- |
| TASK-REQ-00005-00005 | TASK-REQ-00005-00004 | 2026-06-04 17:45 | review/REQ-00005/REVIEW-REPORT.md §5(派生任务表) + §6(findings-no-task.md) | 已完成(2026-06-04 17:54,e5c4dcd) |
| `TASK-REQ-00006-00009` | `TASK-REQ-00006-00008` | 2026-06-04 18:09 | [REVIEW-REPORT.md §F-002](review/REQ-00006/REVIEW-REPORT.md) | 已完成 |

> REQ-00004 评审 0 条"必须改" → 未派生"审查改修"任务(用户授权"全部留作 follow-up")
> REQ-00004 4 条"建议改"全部记录到 `./assistants/V0.0.2/review/REQ-00004/findings-no-task.md`

> REQ-00005 评审派生 1 个"审查改修"任务(T-005),已完成 2026-06-04 17:54

> REQ-00006 评审派生 1 个"审查改修"任务(T-009),已完成 2026-06-04 18:13

---

## 执行的开发命令记录

> 写入方:各 `code-*` 技能在执行编译/启动/测试等命令后追加
> 用途:审计"本版本中跑过哪些命令、结果如何"

| 时间 | 命令 | 工具 | 退出码 | 结果 | 关联任务/阶段 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-04 16:35 | 静态自检 9 项(frontmatter / 节标题 / 步骤齐全 / 边界 E-1~E-10 / NFR-7 禁用词语境 / NFR-6 边界 / 任务编号双格式 / ASCII 字符 / git status) | code-it 步骤 9~10 替代 | 0 | 9/9 通过 | TASK-REQ-00004-00001 |
| 2026-06-04 16:55 | 静态自检 7 项(行数 +8 / 节标题顺序 / Grep 指引 N / 6 子项完整 / git diff 净度 / 未触碰其他段 / NFR-6 严守) | code-it 步骤 9~10 替代 | 0 | 7/7 通过 | TASK-REQ-00004-00002 |
| 2026-06-04 17:12 | 静态自检 7 项(行数各 +1 / 表格末行 / 表格总行数 13:13 / Grep code-dashboard / git diff 净度 / 未触碰其他段 / NFR-6 严守) | code-it 步骤 9~10 替代 | 0 | 7/7 通过 | TASK-REQ-00004-00003 |
| 2026-06-04 16:45 | `git status --porcelain` | Bash | 0 | 成功(列出 5 个 dirty:RESULT.md / SKILL.md / code/ / design/ / plan/) | TASK-REQ-00005-00001 步骤 8 探索 |
| 2026-06-04 16:46 | `git rev-parse HEAD` | Bash | 0 | 成功(`a78d40440ec22015a0a562c9bcd32935aca85e08`) | TASK-REQ-00005-00001 步骤 8 探索 |
| 2026-06-04 16:48 | `grep -c "^### 步骤 0a\|^### 步骤 0b\|^### 步骤 N" SKILL.md` | Bash | 0 | 成功(各 1 命中) | TASK-REQ-00005-00001 步骤 9 验证 |
| 2026-06-04 16:48 | `head -4 SKILL.md` | Bash | 0 | 成功(frontmatter 字节级保留) | TASK-REQ-00005-00001 步骤 9 验证 |
| 2026-06-04 16:48 | `git diff --stat SKILL.md` | Bash | 0 | 成功(74 行新增,0 删除) | TASK-REQ-00005-00001 步骤 9 验证 |
| 2026-06-04 16:49 | `git status --porcelain`(步骤 N 收集) | Bash | 0 | 成功 | TASK-REQ-00005-00001 步骤 N 第 1 步 |
| 2026-06-04 16:50 | `git add plugins/code-skills/skills/code-require/SKILL.md` | Bash | 0 | 成功 | TASK-REQ-00005-00001 步骤 N 第 2 步 |
| 2026-06-04 16:50 | `git commit -m "chore(code-require): REQ-00005 优化 3 个技能,首步拉取+末步兜底提交..."` | Bash | 0 | 成功(`a157d7b`,1 file changed, 74 insertions) | TASK-REQ-00005-00001 步骤 N 第 5 步 |
| 2026-06-04 16:55 | `grep -n "^### 步骤 0 — 版本上下文检测\|^### 步骤 15A\|^## 过程文档格式" SKILL.md` | Bash | 0 | 成功(锚点定位:84/271/324) | TASK-REQ-00005-00002 步骤 8 探索 |
| 2026-06-04 16:56 | `Edit SKILL.md` 步骤 0a | Edit | 0 | 成功(+30 行) | TASK-REQ-00005-00002 步骤 8 实施 |
| 2026-06-04 16:57 | `Edit SKILL.md` 步骤 N | Edit | 0 | 成功(+17 行步骤 N 内容,总 +47) | TASK-REQ-00005-00002 步骤 8 实施 |
| 2026-06-04 16:58 | `grep -c "^### 步骤 0a\|^### 步骤 N\|^### 步骤 0b" SKILL.md` | Bash | 0 | 成功(0a=1, N=1, 0b=0 严禁) | TASK-REQ-00005-00002 步骤 9 验证 |
| 2026-06-04 16:58 | `git diff --stat SKILL.md` | Bash | 0 | 成功(47 行新增,0 删除) | TASK-REQ-00005-00002 步骤 9 验证 |
| 2026-06-04 16:59 | `git status --porcelain`(步骤 N 收集) | Bash | 0 | 成功 | TASK-REQ-00005-00002 步骤 N 第 1 步 |
| 2026-06-04 17:00 | `git add plugins/code-skills/skills/code-design/SKILL.md` | Bash | 0 | 成功 | TASK-REQ-00005-00002 步骤 N 第 2 步 |
| 2026-06-04 17:00 | `git commit -m "chore(code-design): REQ-00005 优化 3 个技能,首步拉取+末步兜底提交..."` | Bash | 0 | 成功(`3e1573e`,1 file changed, 47 insertions) | TASK-REQ-00005-00002 步骤 N 第 5 步 |
| 2026-06-04 17:05 | `grep -n "^### 步骤 0 — 版本上下文检测\|^## 工作流程\|^## 过程文档格式" SKILL.md` | Bash | 0 | 成功(锚点定位:90/92/543) | TASK-REQ-00005-00003 步骤 8 探索 |
| 2026-06-04 17:06 | `Edit SKILL.md` 步骤 0a | Edit | 0 | 成功(+30 行) | TASK-REQ-00005-00003 步骤 8 实施 |
| 2026-06-04 17:07 | `Edit SKILL.md` 步骤 N | Edit | 0 | 成功(+17 行步骤 N 内容,总 +47) | TASK-REQ-00005-00003 步骤 8 实施 |
| 2026-06-04 17:08 | `grep -c "^### 步骤 0a\|^### 步骤 N\|^### 步骤 0b" SKILL.md` | Bash | 0 | 成功(0a=1, N=1, 0b=0 严禁) | TASK-REQ-00005-00003 步骤 9 验证 |
| 2026-06-04 17:08 | `git diff --stat SKILL.md` | Bash | 0 | 成功(47 行新增,0 删除) | TASK-REQ-00005-00003 步骤 9 验证 |
| 2026-06-04 17:09 | `git status --porcelain`(步骤 N 收集) | Bash | 0 | 成功 | TASK-REQ-00005-00003 步骤 N 第 1 步 |
| 2026-06-04 17:10 | `git add plugins/code-skills/skills/code-plan/SKILL.md` | Bash | 0 | 成功 | TASK-REQ-00005-00003 步骤 N 第 2 步 |
| 2026-06-04 17:10 | `git commit -m "chore(code-plan): REQ-00005 优化 3 个技能,首步拉取+末步兜底提交..."` | Bash | 0 | 成功(`e568328`,1 file changed, 47 insertions) | TASK-REQ-00005-00003 步骤 N 第 5 步 |
| 2026-06-04 17:15 | `grep -n "^## 任务清单\|## 里程碑\|## 变更记录" RESULT.md` | Bash | 0 | 成功(锚点定位:111/35/202) | TASK-REQ-00005-00004 步骤 8 探索 |
| 2026-06-04 17:17 | `Edit RESULT.md` 5 处(任务清单 T-004 行 + 统计 + 里程碑 M1.REQ-00005 + 变更记录 + 文档头) | Edit | 0 | 成功(67 insertions / 8 deletions) | TASK-REQ-00005-00004 步骤 8 实施 |
| 2026-06-04 17:18 | `git diff --stat RESULT.md` | Bash | 0 | 成功(67 insertions / 8 deletions) | TASK-REQ-00005-00004 步骤 9 验证 |
| 2026-06-04 17:19 | `git status --porcelain`(本任务收集) | Bash | 0 | 成功(1 文件 dirty) | TASK-REQ-00005-00004 手工 commit 第 1 步 |
| 2026-06-04 17:20 | `git add assistants/V0.0.2/RESULT.md` | Bash | 0 | 成功 | TASK-REQ-00005-00004 手工 commit 第 2 步 |
| 2026-06-04 17:20 | `git commit -m "chore(dashboard): REQ-00005 看板同步(任务清单/统计/里程碑/变更记录)..."` | Bash | 0 | 成功(`1171d98`,1 file changed, 67 insertions / 8 deletions) | TASK-REQ-00005-00004 手工 commit 第 3 步 |

---

## 变更记录

> 写入方:所有 `code-*` 技能,在自己的关键节点追加
> 格式:`YYYY-MM-DD HH:mm  <变更类型>  <摘要>  <关联任务/需求>(可选)`

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-04 12:48 | 初始化 | 创建版本 V0.0.2 工作空间(从 V0.0.1 切换) | — |
| 2026-06-04 12:50 | 需求新增 | REQ-00004 需求分析完成(共 10 条 FR / 7 条 NFR / 30 条 AC / 3 项已锁定 Q-1~Q-3 + 2 项采纳默认 Q-4~Q-5 + 2 项未采用 Q-7~Q-8)。范围:新增 `code-dashboard` 只读型技能(无 `Write`/`Edit`/写命令),支持无参数(版本总览:ASCII 进度表 + 文本柱状图)与指定 `REQ-NNNNN`(需求粒度)双粒度;自动生成最多 5 条下一步建议(可执行命令 + 依据 + 优先级);严守 NFR-6 边界(不修改 marketplace.json / plugin.json / 其他 7 SKILL.md / 模板);Q-1 锁定 ASCII 形态,Q-2 锁定可执行命令推荐,Q-3 锁定只突出 P0/P1 | REQ-00004 |
| 2026-06-04 13:33 | 需求新增 | REQ-00005 需求分析完成(共 6 条 FR / 8 条 NFR / ~32 条 AC / 13 个边界场景 / 4 项已锁定 Q-1~Q-4 + 2 项采纳默认 Q-6/Q-8 + 2 项未采用 Q-5/Q-7 + 1 项建议派生 Q-9)。范围:增量修改 `code-require/SKILL.md` + `code-design/SKILL.md` + `code-plan/SKILL.md` 三个技能的"步骤 0 之前"与"末尾"(不改 frontmatter,不改 `code-it` / `code-version` / `code-unit` / `code-review` / `marketplace.json` / `plugin.json` / CLAUDE.md);Q-1 锁定版本不一致时"询问用户二选一"(默认推荐远端),Q-2 锁定 `git pull` 失败时"中断 + 报错退出",Q-3 锁定末尾 commit message "技能自动生成 + 预览确认",Q-4 锁定"保留 `code-it` 内部 commit,本需求末尾兜底提交与之并存,聚焦'过程文件 + 结果文件'";用户原文 2 处笔误已纠正(`/code-desgin` → `/code-design`,`/code-require` → `/code-require`) | REQ-00005 |
| 2026-06-04 13:45 | 需求新增 | REQ-00006 需求分析完成(共 9 条 FR / 9 条 NFR / ~33 条 AC / 10 个边界场景 / 4 项已锁定 Q-1~Q-4 + 4 项采纳默认 Q-5/Q-6/Q-7/Q-8/Q-9 + 1 项建议派生 Q-10)。范围:新增 `code-publish` 技能,前置检查(全检查最严:需求=已完成 ∧ 任务 开发=已完成 ∧ 测试∈{已运行-通过, 不适用} ∧ 缺陷=已修复)通过后,在 `assistants/<版本号>/publish/` 下生成 `DEPLOY.md` + `UPDATE.md`(基线版本跳过) + `Q&A.md`(从 `assistants/qanda/` 聚合);3 份手册均为"通用发布部署骨架 + 最常见部署方式默认内容 + placeholder"(用户必须手动补全);**顺带**在项目级创建 `assistants/qanda/` 目录 + README.md;严守 NFR-4(不参与 REQ-00005 的"首步拉取+末步提交") + NFR-5(通用性优先) + NFR-8(与 `code-dashboard` 数据源一致);`code-publish` 自身**不**自动 commit(留 dirty tree 给用户审阅);Q-1 锁定全检查,Q-2 锁定创建 qanda 骨架,Q-3 锁定基线不生成 UPDATE,Q-4 锁定通用骨架 | REQ-00006 |
| 2026-06-04 13:59 | 需求新增 | REQ-00007 需求分析完成(共 10 条 FR / 10 条 NFR / ~40 条 AC / 10 个边界场景 / 5 项已锁定 Q-1~Q-5 + 7 项采纳默认 Q-6/Q-7/Q-8/Q-9/Q-10/Q-11/Q-12 + 1 项建议派生 Q-13)。范围:**新增第 10 个 `code-*` 技能 `code-auto`,作为"编排者"驱动 9 个"被驱动"技能**;调用序列:`code-require` → `code-design` → `code-plan` → (任务循环:`code-it` + `code-unit`) → `code-review` → (派生任务循环,直到"必须改"列表为空);所有 `AskUserQuestion` 场景**总选推荐项**(完全无人确认,Q-4 锁定 A);异常立即中断 + 报告(Q-2 锁定 A);用户可随时 `Ctrl+C` 中止(中止时输出报告,NFR-7 约定中止时不写 `auto-report.md`);FR-9 完整报告写入 `require/REQ-NNNNN/auto-report.md` 留痕;Q-1 锁定"仅按状态终止"无轮数上限(接受"修改引入新问题"风险),Q-2 锁定"立即中断 + 报告",Q-3 锁定"Ctrl+C 中止 + 报告",Q-4 锁定"总选推荐项",Q-5 锁定"不引入批量模式";严守 NFR-3(`code-auto` 自身不 commit) + NFR-4(不引入批量模式) + NFR-8(不实现增量恢复) + NFR-9(与 REQ-00004/00005/00006 协同) | REQ-00007 |
| 2026-06-04 14:07 | 需求新增 | REQ-00008 需求分析完成(共 9 条 FR / 8 条 NFR / ~30 条 AC / 9 个边界场景 / 2 项已锁定 Q-1/Q-2 + 5 项采纳默认 Q-3/Q-4/Q-5/Q-6/Q-7 + 1 项建议派生 Q-8)。范围:**优化 `/code-review` 技能**(不改 frontmatter,不改模式 1 行为),**增加"无参入口" = 整版本模式**;整版本模式只评审 `状态=已完成` 的需求(Q-1 锁定 B);输出**双写**:聚合 `./assistants/<版本号>/REVIEW.md`(顶层,与 `RESULT.md` 同级)+ 单需求 `./assistants/<版本号>/review/REQ-NNNNN/REVIEW-REPORT.md`(与模式 1 同路径);多次执行 → 全部覆盖(NFR-3 幂等);派生任务**支持**(Q-4 采纳默认),按"必须改"发现追加到对应 `PLAN.md` 任务总览;NFR-4 `code-auto` 继续用模式 1(不触发 `code-auto` 升级);NFR-5 不参与 REQ-00005 改写;NFR-7 评审发现按 `(需求编码, 描述)` 去重;FR-7 不修改模式 1 行为;用户原文 1 处笔误已纠正(`/code-review` → `/code-review`) | REQ-00008 |
| 2026-06-04 14:18 | 需求新增 | REQ-00009 需求分析完成(共 7 条 FR / 8 条 NFR / ~25 条 AC / 8 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3 + 4 项采纳默认 Q-4/Q-5/Q-6/Q-7 + 1 项建议派生 Q-8)。范围:**优化 `/code-unit` 技能**(不改 frontmatter,不改"可测"流程),**新增"步骤 0a 项目可测性检查"守卫**;守卫检查项目根 7 项文件/目录(任一存在 → 可测):`package.json` 含 `scripts.test` / `pyproject.toml` 含测试配置 / `Cargo.toml` / `go.mod` / `pom.xml` / `build.gradle`(.kts) / `test/` 目录(Q-1 锁定 A,只检查项目根);**不可测 → 跳过单测过程** + 看板"任务清单"区段测试状态 = `不适用`(Q-2 锁定 A,**复用 V0.0.1 既有枚举,不新增枚举值**,`code-dashboard` 0 改动)+ **不**写 `test/<任务编码>/RESULT.md`(Q-3 锁定 A,零新增产物);退出码 = 0 让 `code-auto` 继续(NFR-6);用户原文**无笔误**;NFR-4 与 `code-dashboard` 0 冲突;NFR-5 与 `code-publish` 0 冲突(`code-publish` 前置检查"测试∈{已运行-通过, 不适用}"已兼容) | REQ-00009 |
| 2026-06-04 14:36 | 需求新增 | REQ-00010 需求分析完成(共 6 条 FR / 8 条 NFR / ~22 条 AC / 8 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3 + 4 项采纳默认 Q-4/Q-5/Q-6/Q-7 + 1 项建议派生 Q-8)。范围:**优化 `/code-it` 技能**(不改 frontmatter,不改"无前置"流程),**新增"步骤 0a 前置任务检查"守卫**;Q-1 锁定"**不新增前置任务列,完全按 `PLAN.md` 文件登记顺序判定前置**"(零规范变更 — `PLAN.md` 模板/看板均不变,`dashboard-conventions §规则 1` 不触发);Q-2 锁定"只看开发状态"(与 `code-publish` 前置检查同口径);Q-3 锁定"中止 + 打印推荐执行命令 + 退出码 ≠ 0"(`code-auto` 据此中断;中止报告含"⛔ code-it 中止(存在未完成的前置任务)"+ 所有前置状态+ "推荐执行 /code-it <第一个未完成> 完成后,再执行 /code-it <当前任务>");用户原文 1 处笔误已纠正(`/code-it` → `/code-it`);NFR-3 零规范变更;NFR-4 与 `code-auto` 退出码兼容(守卫不通过 → 退出码 ≠ 0 → `code-auto` 中断);NFR-6 `PLAN.md` 缺失时守卫通过(退化,不阻止 `code-it`);FR-4 不修改 `code-auto`(本需求守卫作为"双保险"与 `code-auto` 现有"按序"逻辑协同) | REQ-00010 |
| 2026-06-04 14:57 | 需求新增 | REQ-00011 需求分析完成(共 9 条 FR / 8 条 NFR / ~30 条 AC / 10 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3 + 5 项采纳默认 Q-4/Q-5/Q-6/Q-7/Q-8 + 1 项建议派生 Q-9)。范围:**优化 `/code-design` + `/code-plan` 2 个技能**(不改 frontmatter,不改"无设计目标"流程),**新增"步骤 0b 设计目标确认"环节**;Q-1 锁定"**都走步骤 0b**"(首步拉取之后、设计产出之前,与 REQ-00005 / REQ-00009 / REQ-00010 的"步骤 0a"模式同位叠加);Q-2 锁定"**回写** `RESULT.md` 顶部'## 设计目标' 小节"且**关键补充**"扩展性高的方法需要拆出'扩展架构设计' / '设计模式使用'等更细致任务步骤"(FR-4 据此设计);Q-3 锁定"**问多个问题**"(设计目标 + 4 维度,可分开提问,大需求场景);用户原文 1 处笔误已纠正(`/code-desgin` → `/code-design`);FR-2 `code-plan` 读 `design/.../RESULT.md` 的"## 设计目标"小节并沿用(不重新问);FR-3 `code-plan` 读不到时退化(回退到用户手动确认 + 仅写 `plan/.../RESULT.md`);FR-4 `code-plan` 据"设计目标"调整任务拆分粒度(扩展性高 → 加"扩展架构设计"等任务);FR-5 回写"## 设计目标"小节结构(整体 3 选项 + 4 维度优先级 + 回写时间 + 回写触发);NFR-3 幂等;NFR-4 不触发 `dashboard-conventions §规则 1`;NFR-5 与 `code-auto` 协同 0 冲突(`code-auto` 仍按"总选推荐项") | REQ-00011 |
| 2026-06-04 15:11 | 需求新增 | REQ-00012 需求分析完成(共 7 条 FR / 8 条 NFR / ~25 条 AC / 9 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3 + 5 项采纳默认 Q-4/Q-5/Q-6/Q-7/Q-8 + 1 项建议派生 Q-9)。范围:**新建仓库根 `./README.md` + `./README.en.md`**(极简 < 50 行,中英同次提交,`doc-conventions §规则 1` 严格遵循),**移动 `plugins/code-skills/CLAUDE.md` → `./CLAUDE.md`**(git mv 保留历史,原位置**不保留**);仓库根 README 是"门面",`plugins/code-skills/README.md` 保留作为"详细技能文档";NFR-2 < 50 行;NFR-3 git mv 保留 blame;NFR-8 不提供重定向/软链;用户原文**无笔误** | REQ-00012 |
| 2026-06-04 15:25 | 需求新增 | REQ-00013 需求分析完成(共 11 条 FR / 10 条 NFR / ~30 条 AC / 9 个边界场景 / 3 项已锁定 Q-1/Q-2/Q-3/Q-4 + 6 项采纳默认 Q-5/Q-6/Q-7/Q-8/Q-9/Q-10 + 1 项建议派生 Q-11)。范围:**优化 6 技能** `code-require`/`code-plan`/`code-fix`/`code-it`/`code-unit`/`code-review`/`code-auto`(其中 `code-fix` 是 V0.0.0 起的真实存在技能,SKILL.md 17,878 bytes,本轮**首次**升级),**统一启用"编号+标题"显示**(格式 `REQ-00001 · 标题` / `TASK-... · 标题` / `BUG-NNNNN · 标题`);Q-1 锁定"从已有内容派生,不新增字段"(零规范变更 — `RESULT.md` 第 1 行 + `PLAN.md` 任务总览"标题"列已存在);Q-2 锁定"`REQ-00001 · 标题`"(中点 `·` 格式);Q-3 锁定"字符数 ≤ 30";Q-4 锁定"本轮升级 6 技能"(`code-dashboard` 不变因看板标题列已存在);用户原文 5 处笔误已纠正;NFR-4 历史自动生效;NFR-5 `code-publish` 报告升级;NFR-6 不改 4 技能 | REQ-00013 |
| 2026-06-04 15:50 | 设计新增 | REQ-00004 概要设计完成(共 8 个关键设计问题 Q-1~Q-8 + 4 段总览 + 5 段需求粒度 + 10 项边界 + 0 新增依赖 + 30 AC 全继承)。范围:新增 `code-dashboard` 单文件技能(`plugins/code-skills/skills/code-dashboard/SKILL.md`);SKILL.md 章节结构完全复用既有 10 个 `code-*` 骨架(目标 / 适用 / 不适用 / 目录 / 输入 / 输出 / 工具 / 步骤 / 边界 / 衔接 / 不要做);**不**修改 marketplace.json / plugin.json / 其他 10 SKILL.md frontmatter(NFR-6 严守);**不**新增 `templates/` / `checklists/` / `guidelines/` 子目录(无独立资源);**不**引入运行时依赖(NFR-1 锁零依赖);解析器单遍扫描 + 行号锚点;任务编号解析双格式兼容(新格式优先 + 旧格式透传,NFR-3);建议生成器 5 类优先级 + 最多 5 条;ASCII 比例条固定 12 字符 + `█` / `░` / `▓`;性能估算 < 1 秒(NFR-4 远低于 5 秒);Q-D1/2/3/4 本轮新增默认(显示策略 / 不读评审发现段 / 12 字符宽度 / 需求模式不折叠);遵循 9 个规范文件(详见 `design/REQ-00004/rule-compliance.md`),3 项用户授权偏离(A-1 单文件 / A-2 不改 marketplace / A-3 无历史版本切换) | REQ-00004 |
| 2026-06-04 16:00 | 设计新增 | REQ-00005 概要设计完成(共 3 个 SKILL.md 增量追加 7 步骤:`code-require` × 3 步 + `code-design` × 2 步 + `code-plan` × 2 步;4 项关键设计决策 D-1/D-2/D-3/D-5 全部选定;10 个候选方案与选定理由;13 条关键不变量全部保留 frontmatter / marketplace.json / plugin.json / CLAUDE.md / README / 4 个未触达技能;13 个规范文件 0 冲突 0 偏离 0 授权;3 项 follow-up Q-9/Q-10/Q-11 留 `code-review` 派生)。本设计为首个概要设计(同版本下 9 个其他需求 design 阶段未开展),严格遵循 `skill-conventions.md §规则 1`(frontmatter 字节级保留)+ `marketplace-protocol.md §规则 1`(协议清单不动)+ `dashboard-conventions.md §规则 1`(字段约定不扩展);`code-require` 步骤 0b 仅专属;末尾兜底与 `code-it` 内部 commit 并存(Q-4 锁定 B,D-5 选定 B);commit 沿用 V0.0.1 实践 `chore(<scope>): <subject>`(NFR-6) | REQ-00005 |
| 2026-06-04 16:10 | 设计新增 | REQ-00004 详细设计与编码计划完成(共 6 个可直接编码算法 算法 0~5 + 8 个内存数据结构 + 3 条任务 T-001 必 + T-002/T-003 可 + 1 个里程碑 M3 可发布)。范围:详细设计 14 节(概述 / 上游引用 / 规范遵循 / 模块详细化 / 算法与逻辑 / 数据结构 / 接口细节 / 异常处理 / 安全 / 状态机 / 性能 / 测试要点 / 关联 / 待澄清 / 变更记录);PLAN.md 8 节(计划概述 / 任务总览 / 任务详情 / 任务依赖图 / 里程碑 / 状态管理规则 / 关联计划 / 变更记录);3 项本阶段新增偏离(P-A1 状态字面不归一化 / P-A2 测试状态=不适用 / P-A3 需求模式不显示里程碑);测试状态全部 `不适用`(P-A2 锁定,纯 Markdown 指令无单元测试载体);M3 完成定义=所有任务开发状态=已完成 | REQ-00004 |
| 2026-06-04 16:30 | 设计新增 | REQ-00005 详细设计与编码计划完成(共 4 个任务 TASK-REQ-00005-00001~00004,严格遵循 `encoding-conventions.md §规则 1+3` 5+5 位嵌套式;1 个里程碑 M1:本需求可发布;T-001~T-003 可并行 + T-004 依赖前三;测试状态全部 = `不适用` 因本仓库无构建/测试文件 — REQ-00009 守卫判定"不可测";3 个 SKILL.md 增量插入点(步骤 0a + N;`code-require` 额外 + 0b)用 `module-details.md` 显式给出精确行号 + 锚点字符串 + 完整 Markdown;伪代码 + 弹窗文本 + 错误码在 `interface-specs.md` 完整化;100% 规范合规 — 0 冲突 0 偏离 0 授权) | REQ-00005 |
| 2026-06-04 16:40 | 开发状态更新 | T-001 状态"待开始"→"已完成"(新增 `plugins/code-skills/skills/code-dashboard/SKILL.md`,367 行,单文件);YAML frontmatter 完整(`name: code-dashboard` + 完整 `description`)+ 12 节正文严格对齐既有 10 个 `code-*` 骨架 + 步骤 0~6 齐全 + 边界 E-1~E-10 完整覆盖 + NFR-7 禁用词 4 处均在"不调用"上下文 + NFR-6 边界 2 处均在"不动"上下文 + 任务编号双格式正则严格按 `encoding-conventions §规则 1/3` + 6 项 design/plan 偏离全部落地;静态自检 9/9 通过;`git status` 净度:NFR-6 严守(`marketplace.json` / `plugin.json` / 其他 10 SKILL.md frontmatter 全部未改);提交哈希待用户后续 `git commit` 生成 | TASK-REQ-00004-00001 |
| 2026-06-04 16:48 | 设计新增 | REQ-00006 概要设计完成(首次):7 个新增模块(`code-publish` SKILL + PreflightChecker / BaselineDetector / ManualBuilder / QandaScaffolder / QandaAggregator / ReportFormatter)+ 5 份模板(DEPLOY/UPDATE/Q&A/qanda-README/assistants-layout)+ 0 修改既有(严格遵循 FR-8.AC-8.1~4)+ 0 新增依赖(NFR-1)+ 1 顺带产物(`assistants/qanda/` 项目级目录骨架);决策 D-1~D-8 全部从需求 v1 + 规范 + 项目现状演绎(0 阻塞);D-1 独立第 11 个 code-* 技能(用户口语化"第 9 个")、D-2 按行硬解析、D-3 字典序基线、D-4 可选参数缺省 `.current-version`、D-5 v1 不实现 `--force`、D-6 全部聚合 qanda、D-7 始终覆盖 + 报告"将覆盖 N"、D-8 纯文本 + 图标;规范自检 `dashboard-conventions §规则 1` 0 触发(不扩展看板字段) + `skill-conventions §规则 1` ✓ + `module-conventions §规则 1` ✓(templates/ 5 份);7 项 Q-D 留作 follow-up(Q-D-1 注册到 marketplace、Q-D-2 同步 README "主要能力"、Q-D-3 沉淀 publish-conventions、Q-D-4 dashboard 升级、Q-D-5 加入 REQ-00005、Q-D-6 v2 `--force` 实现方式、Q-D-7 报告升级 REQ-NNNNN·标题格式) | REQ-00006 |
| 2026-06-04 16:50 | 开发状态更新 | TASK-REQ-00005-00001 开发状态"进行中"→"已完成",提交 a157d7b(`code-require/SKILL.md` 增量追加 3 章节 — 步骤 0a 拉取 / 步骤 0b 版本对齐(仅 `code-require` 专属)/ 步骤 N 末尾兜底提交,74 行新增 0 删除,frontmatter 字节级保留,既有步骤 0-10A/5B-10B 全文不动,3 验证全部通过,0 偏离) | TASK-REQ-00005-00001 |
| 2026-06-04 16:55 | 开发状态更新 | T-002 状态"待开始"→"已完成"(修改 `plugins/code-skills/CLAUDE.md` 追加 8 行:`### 指引 N: code-dashboard 行为约定` + 6 个子项;134 → 142 行,纯追加无任何已有行修改);用户授权依据:PLAN.md 行 194 "用户在 `code-it` 阶段明确授权" + 用户主动调用 `code-it REQ-00004-002` 即为信号;接受 `code-rule` 后续覆盖本段的风险(由 CLAUDE.md 显式声明);静态自检 7/7 通过;git diff 净度:`marketplace.json` / `plugin.json` / 其他 10 SKILL.md 全部未触碰;6 个子项内容与 T-001 落地的 SKILL.md 行为**完全一致** | TASK-REQ-00004-00002 |
| 2026-06-04 17:00 | 开发状态更新 | TASK-REQ-00005-00002 开发状态"进行中"→"已完成",提交 3e1573e(`code-design/SKILL.md` 增量追加 2 章节 — 步骤 0a 拉取 / 步骤 N 末尾兜底提交,**不含步骤 0b**(FR-2 显式仅 `code-require` 专属),47 行新增 0 删除,frontmatter 字节级保留,既有步骤 0-15A 全文不动,0b 验证 0 命中,4 验证全部通过,0 偏离) | TASK-REQ-00005-00002 |
| 2026-06-04 17:01 | 设计新增 | REQ-00006 详细设计 + 编码计划完成(首次):RESULT.md 14 章节(覆盖详细化模块/算法/数据/接口/异常/安全/性能/测试/规范) + PLAN.md 8 条任务;实现层 8 项决策 DD-1~DD-8 全部演绎(0 阻塞);任务编号 TASK-REQ-00006-00001 ~ 00008(5 位嵌套式 `encoding-conventions §规则 3`);任务拆分:T-001 SKILL.md + T-002~T-006 5 份模板 + T-007 不变量自检与看板同步 + T-008 双 README 同步(纳入 Q-D-2 决策);全部测试状态预设"不适用"(纯文档型);依赖图:T-002~T-006 + T-008 并行 → T-001 → T-007;新里程碑:M1-REQ-00006-1 模板就绪 / M1-REQ-00006-2 技能可触发(嵌入版本 M1 之前);估算合计 ~2.9 天 | REQ-00006 |
| 2026-06-04 17:10 | 开发状态更新 | TASK-REQ-00005-00003 开发状态"进行中"→"已完成",提交 e568328(`code-plan/SKILL.md` 增量追加 2 章节 — 步骤 0a 拉取 / 步骤 N 末尾兜底提交,**不含步骤 0b**(FR-2 显式仅 `code-require` 专属),步骤 N 对 REQ 路径 / BUG 路径都适用(7A/7B/19-28 都执行),47 行新增 0 删除,frontmatter 字节级保留,既有步骤 0-18A/13B/19-28 全文不动,0b 验证 0 命中,4 验证全部通过,0 偏离) | TASK-REQ-00005-00003 |
| 2026-06-04 17:12 | 开发状态更新 | T-003 状态"待开始"→"已完成"(修改 `plugins/code-skills/README.md` + `README.en.md` 各追加 1 行:`code-dashboard` 在 `code-review` 之后;883 → 884 行,纯追加无任何已有行修改);保留 5 列结构(与既有 10 行严格对仗;与 PLAN.md 4 列字面偏离,理由:`doc-conventions §规则 1` 严守);中英同次提交(同一消息块 Edit);用户授权依据:PLAN.md 行 231 + 用户主动调用 `code-it TASK-REQ-00004-00003`;静态自检 7/7 通过;git diff 净度:`marketplace.json` / `plugin.json` / 其他 10 SKILL.md 全部未触碰;**本需求 3 任务全部完成,M3 里程碑达成**(开发完成度 3/3,真正可发布 3/3) | TASK-REQ-00004-00003 |
| 2026-06-04 17:20 | 开发状态更新 | TASK-REQ-00005-00004 开发状态"进行中"→"已完成"(本任务不含末尾兜底 commit — 详见 `code/TASK-REQ-00005-00004/RESULT.md §4.5`;本任务的 dirty 文件由本任务手动 `git commit` 收尾;看板 5 处同步:任务清单 T-004 行 + 统计行 + 里程碑 M1.REQ-00005 达成 + 变更记录 + 文档头) | TASK-REQ-00005-00004 |
| 2026-06-04 17:30 | 开发状态更新 | T-001 `[新增] 写 code-publish/SKILL.md` 开发状态"进行中"→"已完成";完成时间 2026-06-04 17:30;完成人 wangmiao;不提交(留 dirty tree 由 T-007 后统一 commit);SKILL.md 475 行,严格遵循 `skill-conventions §规则 1`(name=code-publish,description ~800 字符) + `module-conventions §规则 1`(SKILL.md 在技能根目录);前置任务顺序偏离:用户已确认 T-001 按"当前应该第一个"执行(SKILL.md 中仅字符串引用模板路径,不依赖文件存在);详 `code/TASK-REQ-00006-00001/RESULT.md` | T-001 |
| 2026-06-04 17:34 | 开发状态更新 | T-002 `[新增] 写 templates/DEPLOY.md 模板` 开发状态"进行中"→"已完成";完成时间 2026-06-04 17:34;完成人 wangmiao;不提交;DEPLOY.md 245 行,8 大章节 + 7 子节 + 1 附录(可选);14 种 placeholder;15 项验证 checkbox;3 项实现细节细化/增量(URL 拆为 server:port / 附录"发布后通知" / 启动方式 3 种补充),**0 与设计冲突的偏离**;详 `code/TASK-REQ-00006-00002/RESULT.md` | T-002 |
| 2026-06-04 17:40 | 评审发现 | REQ-00004 评审完成(共 3 任务 / 4 维度检查 / 0 必须改 / 4 建议改全部留作 follow-up / 0 派生任务);整体结论 ✅ 通过(无阻塞,REVIEW 完整);评审产物 4 件:REVIEW-REPORT.md(整体) + work-log.md(过程) + review-checklist-applied.md(清单应用) + findings-no-task.md(4 条建议改详情);F-001 SKILL.md 步骤 5 触发条件不完整 / F-002 SKILL.md 与 CLAUDE.md 解析锚点正则字面不一致 / F-003 CLAUDE.md 指引 N 编号占位说明不显 / F-004 README 下游列语义与既有 10 行不同 | REQ-00004 |
| 2026-06-04 17:45 | 评审发现 | REQ-00005 评审完成(共 5 条发现 — 0 必须改 + 1 建议改 F-005 派生为 TASK-REQ-00005-00005 + 4 可选 I-001~I-004 全部接受;0 冲突 / 0 错误修复循环 / 0 偏离;评审时间 17:30 ~ 17:45) | REQ-00005 |
| 2026-06-04 17:45 | 开发状态更新 | T-003 `[新增] 写 templates/UPDATE.md 模板` 开发状态"进行中"→"已完成";完成时间 2026-06-04 17:45;完成人 wangmiao;不提交;UPDATE.md 365 行,8 大章节 + 11 子节(§5 4 子节 / §8 4 子节),§8 回滚方案为新增(本模板专属),26 项 checkbox;2 自动 placeholder(`<本版本号>` + `<源版本>`);7 项实现细节细化/增量/收敛(均 0 与设计冲突),详 `code/TASK-REQ-00006-00003/RESULT.md` | T-003 |
| 2026-06-04 17:52 | 开发状态更新 | T-004 `[新增] 写 templates/Q&A.md 模板` 开发状态"进行中"→"已完成";完成时间 2026-06-04 17:52;完成人 wangmiao;不提交;Q&A.md 63 行(对比 DEPLOY/UPDATE 是"小模板",符合设计预期);H1 + 引言 + 占位章节(含 4 步添加 Q&A 指南 + 完整生成结果示例 + 排除/排序规则);1 自动 placeholder;5 项实现细节增量/收敛(均 0 与设计冲突);模块边界清晰:Q&A.md 模板只占位,具体问答由 QandaAggregator 动态聚合 qanda/*.md;详 `code/TASK-REQ-00006-00004/RESULT.md` | T-004 |
| 2026-06-04 17:54 | 开发状态更新 | TASK-REQ-00005-00005 开发状态"待开始"→"已完成",提交 e5c4dcd(`code/T-004/RESULT.md` F-1 文档头 + F-2 §3.1 表格 2 处 `<TBD>` → `1171d98ef51e5910f4b8567794bada77397042d4` 回填;0 偏离;严格遵守 review §4 不重写其他字段;看板 + PLAN.md + 任务自身 RESULT.md 三处完全一致;W-002 已处理) | TASK-REQ-00005-00005 |
| 2026-06-04 17:56 | 开发状态更新 | T-005 `[新增] 写 templates/qanda-README.md 模板` 开发状态"进行中"→"已完成";完成时间 2026-06-04 17:56;完成人 wangmiao;不提交;qanda-README.md 134 行,4 大章节(用途/命名/引用/维护);与 T-004 Q&A.md 模板形成完整闭环(T-004 说什么做,T-005 说怎么做);7 项实现细节增量/收敛(均 0 与设计冲突);命名建议含 7 个具体示例(deploy-faq / db-init-faq / 等);引用规范显式说明 README.md 不被聚合 + 字典序排序;维护方式含 4 步流程 + 当前 v1 / 未来 v2 / "不做的事"3 条;详 `code/TASK-REQ-00006-00005/RESULT.md` | T-005 |
| 2026-06-04 18:00 | 开发状态更新 | T-006 `[新增] 写 templates/assistants-layout.md 模板` 开发状态"进行中"→"已完成";完成时间 2026-06-04 18:00;完成人 wangmiao;不提交;assistants-layout.md 172 行,沿用 code-version 范式 6 段 + 1 段"code-publish 的特定扩展";目录树与 SKILL.md §工作目录约定 一致(含 publish/ + qanda/ + 完整结构);7 项实现细节增量/收敛(均 0 与设计冲突);5 类资源 + 4 类读/写角色表标注本技能访问模式;可写目录边界 4 行表;不反向引用 SKILL.md(模块边界);详 `code/TASK-REQ-00006-00006/RESULT.md` | T-006 |
| 2026-06-04 18:03 | 开发状态更新 | T-007 `[文档] 不变量自检 + 同步 V0.0.2 看板 + 偏差日志` 开发状态"进行中"→"已完成";完成时间 2026-06-04 18:03;完成人 wangmiao;不提交;**收尾任务完成**;8 项不变量(FR-8.AC-8.1~8.4 + 看板责任划分 + 模板位置)全部通过;9 项 NFR 全部通过;0 项与设计冲突(36 项实现细节汇总,详 T-001~T-006 各 deviations.md);端到端 3 场景本任务未实际执行(等用户实际调用 code-publish 时验证);**T-008(双 README 同步)仍待开始,需用户后续手动处理**;详 `code/TASK-REQ-00006-00007/RESULT.md` | T-007 |
| 2026-06-04 18:08 | 开发状态更新 | T-008 `[修改] 同步双 README "主要能力" 段(中英同次提交)` 开发状态"进行中"→"已完成";完成时间 2026-06-04 18:08;完成人 wangmiao;不提交;**REQ-00006 全部 8 任务完成**;`README.md` + `README.en.md` 各 +1 行(git diff --stat: 2 files, 2 insertions);中英 H2 数量对仗(11/11) + 表格列数对仗(5/5) + 表格行数对仗(12/12) + 同次提交就绪(2 文件 M);0 项与设计冲突;严格遵循 `doc-conventions §规则 1`;详 `code/TASK-REQ-00006-00008/RESULT.md` | T-008 |
| 2026-06-04 18:09 | 评审发现 | REQ-00006 评审完成:8 任务 / 8 维度 / 8 条发现(1 必须改 F-002 + 5 建议改 F-001/F-003/F-005/F-006/F-007 + 2 可选 F-004/F-008);派生新"审查改修"任务 T-009(F-002 修订双 README `<code-publish>` 行措辞,明确"首次调用"语义);7 项建议改/可选留 `findings-no-task.md` 作为 v2 follow-up;本需求**条件性可合并**(T-009 完成后);详 `review/REQ-00006/REVIEW-REPORT.md` | REQ-00006 |
| 2026-06-04 18:13 | 开发状态更新 | T-009 `[修改] 修订双 README <code-publish> 行措辞(明确"首次调用"语义)` 开发状态"进行中"→"已完成";完成时间 2026-06-04 18:13;完成人 wangmiao;不提交;**REQ-00006 全部 9 任务完成**;`README.md` + `README.en.md` 各修订 L38(git diff --stat: 2 files, 2 insertions);9 项静态验证 + 9 项不变量自检全部通过;0 项与设计冲突;严格遵循 `doc-conventions §规则 1` 与 `review/T-009/RESULT.md` §6 "不需要做的"约束;详 `code/TASK-REQ-00006-00009/RESULT.md` | T-009 |

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
- [design/REQ-00006/materials-index.md](design/REQ-00006/materials-index.md)
- [design/REQ-00006/design-notes.md](design/REQ-00006/design-notes.md)
- [design/REQ-00006/module-breakdown.md](design/REQ-00006/module-breakdown.md)
- [design/REQ-00006/dependencies.md](design/REQ-00006/dependencies.md)
- [design/REQ-00006/related-designs.md](design/REQ-00006/related-designs.md)
- [design/REQ-00006/rule-compliance.md](design/REQ-00006/rule-compliance.md)
- [design/REQ-00006/clarifications.md](design/REQ-00006/clarifications.md)
- [plan/REQ-00006/RESULT.md](plan/REQ-00006/RESULT.md)
- [plan/REQ-00006/PLAN.md](plan/REQ-00006/PLAN.md)
- [plan/REQ-00006/materials-index.md](plan/REQ-00006/materials-index.md)
- [plan/REQ-00006/design-notes.md](plan/REQ-00006/design-notes.md)
- [plan/REQ-00006/module-details.md](plan/REQ-00006/module-details.md)
- [plan/REQ-00006/interface-specs.md](plan/REQ-00006/interface-specs.md)
- [plan/REQ-00006/data-changes.md](plan/REQ-00006/data-changes.md)
- [plan/REQ-00006/risk-analysis.md](plan/REQ-00006/risk-analysis.md)
- [plan/REQ-00006/rule-compliance.md](plan/REQ-00006/rule-compliance.md)
- [plan/REQ-00006/clarifications.md](plan/REQ-00006/clarifications.md)
- [code/TASK-REQ-00006-00009/RESULT.md](code/TASK-REQ-00006-00009/RESULT.md)
- [code/TASK-REQ-00006-00009/work-log.md](code/TASK-REQ-00006-00009/work-log.md)
- [code/TASK-REQ-00006-00009/compile-and-run.md](code/TASK-REQ-00006-00009/compile-and-run.md)
- [code/TASK-REQ-00006-00009/deviations.md](code/TASK-REQ-00006-00009/deviations.md)
- [code/TASK-REQ-00006-00009/test-results.md](code/TASK-REQ-00006-00009/test-results.md)

过程文档(本需求):
- [review/REQ-00006/REVIEW-REPORT.md](review/REQ-00006/REVIEW-REPORT.md)
- [review/REQ-00006/work-log.md](review/REQ-00006/work-log.md)
- [review/REQ-00006/review-checklist-applied.md](review/REQ-00006/review-checklist-applied.md)
- [review/REQ-00006/findings-no-task.md](review/REQ-00006/findings-no-task.md)
- [review/TASK-REQ-00006-00009/RESULT.md](review/TASK-REQ-00006-00009/RESULT.md)
- [review/TASK-REQ-00006-00009/work-log.md](review/TASK-REQ-00006-00009/work-log.md)

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
