# 版本开发进度看板 — V0.0.2

> 本文件是 `V0.0.2` 版本工作空间的**单一事实来源**。
> 所有 `code-*` 技能在推进工作时,都会同步更新对应的区段。
> 区段填写规则见 `skills/code-version/SKILL.md` 中的"看板字段约定"。

## 文档头
- 版本号:`V0.0.2`
- 创建时间:2026-06-04 12:48
- 最近更新:2026-06-05
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
| 最近更新 | 2026-06-05 19:55 |
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
| M1-REQ-00007-1:文档就绪 | T-001 ~ T-003(REQ-00007) | SKILL.md 写完 + marketplace.json 追加 + 中英 README 同步,3 任务开发状态=已完成 + 测试状态=不适用 | **已完成** | 2026-06-05 | **2026-06-05 11:05** |
| M1-REQ-00014-1:文档就绪 | T-001(REQ-00014) | code-plan/SKILL.md §10A 改写完成,3 个新子节齐全 + 其他 18 章节未改 + 行数偏差 ±20% 内 | **已完成** | 2026-06-05 | **2026-06-05 14:15** |
| M1-REQ-00007-2:本需求可发布 | M1-REQ-00007-1 + T-004 + T-005(REQ-00007) | **5 任务开发状态=已完成 且 测试状态∈{已运行-通过, 不适用}**,8 项不变量自检通过 + 看板 5 处一致 | **已完成** | 2026-06-05 | **2026-06-05 11:30** |
| M1-REQ-00014-2:本需求可发布 | M1-REQ-00014-1 + T-005(REQ-00014) | **2 任务开发状态=已完成 且 测试状态∈{已运行-通过, 不适用}**,8 项不变量自检通过 | **已完成** | 2026-06-05 | **2026-06-05 14:30** |
| M1-REQ-00008-1:文档就绪 | T-001(REQ-00008) | 1 个 SKILL.md 增量追加完成(2 段:锚点 A L109 后 + 锚点 B L313 后)+ INV-1/4/11/12 字节级保留 + 13/13 INV 自检通过(由 T-003 收尾执行) | **已完成** | 2026-06-05 | **2026-06-05 16:25** |
| M1-REQ-00008-2:本需求可发布 | M1-REQ-00008-1 + T-002 + T-003(REQ-00008) | **3 任务开发状态=已完成 且 测试状态=不适用**,13/13 INV 100% 自检通过 + 看板 5 处一致 + 未来 `code-review`(无参)可触发 | **已完成** | 2026-06-05 | **2026-06-05 16:30** |
| M1-REQ-00016-1:文档就绪 | T-001, T-002(REQ-00016) | 2 个 SKILL.md 增量追加完成(2 段:锚点 A "步骤 0"后 + 锚点 B "步骤 N 步骤 3"后)+ INV-1/4/12/13 字节级保留 + 13/13 INV 自检通过(由 T-004 收尾执行) | 待开始 | 2026-06-05 | — |
| M1-REQ-00016-2:本需求可发布 | M1-REQ-00016-1 + T-003 + T-004(REQ-00016) | **4 任务开发状态=已完成 且 测试状态=不适用**,13/13 INV 100% 自检通过 + 看板 5 处一致 + 未来 `/code-design --fast REQ-NNNNN` 验证 | 待开始 | 2026-06-05 | — |
| M1-REQ-00017-1:文档就绪 | T-001, T-002(REQ-00017) | 2 个 SKILL.md 增量追加完成(3 段:锚点 A `/code-plan` 步骤 10A + 锚点 B `/code-plan` 步骤 16A + 锚点 C `/code-it` 末尾兜底后 P-1)+ INV-1~7 字节级保留 + 既有 5 段核心小节未改 | 待开始 | 2026-06-05 | — |
| M1-REQ-00017-2:本需求可发布 | M1-REQ-00017-1(REQ-00017) | **2 任务开发状态=已完成 且 测试状态=不适用**,7/7 INV 100% 自检通过 + 看板 4 处一致 + 未来 `code-auto` 跑一个完整需求验证 P-1 推进看板(开发状态:待开发→已完成) | 待开始 | 2026-06-05 | — |
| M1-REQ-00011-1:文档就绪 | T-001(REQ-00011) | `code-design/SKILL.md` 增量追加"步骤 0b 设计目标确认" 完成(3 子节:1-5 问自适应 / writeDesignGoalsSection / 屏显模板)+ `design.md` 模板顶部预留"## 设计目标"占位 + §步骤 0a L107 小注更新 + INV-1/2/3 字节级保留 | **已完成** | 2026-06-05 | **2026-06-05 19:55** |
| M1-REQ-00011-2:本需求可发布 | M1-REQ-00011-1 + T-002(REQ-00011) | **2 任务开发状态=已完成 且 测试状态=不适用**,8/8 INV 100% 自检通过 + 看板 4 处一致 + 未来 `code-auto` 跑一个完整需求验证"步骤 0b 选推荐项 → 任务按默认粒度产出" | **已完成** | 2026-06-05 | **2026-06-05 20:05** |
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
| REQ-00014 | 优化 `/code-plan` 任务拆分维度(按功能点拆 + 架构任务作为首个 + 仅未来生效) | 已完成(需求分析) | 2026-06-05 12:20 | — | [RESULT.md](require/REQ-00014/RESULT.md) | — | — |
| REQ-00016 | 优化 `/code-design` / `/code-plan`,增加"快模式"(跳过非必要步骤 + 减少过程文档 + 末尾兜底提交跳过 3 选 1 确认);触发方式 = `CODE_FAST_MODE=1` 环境变量 / `--fast` CLI 标志(优先级 CLI > 环境变量 > 默认值);完整模式字节级不变;0 修改其他 9 个 `code-*` 技能;0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/` / README | 已完成(需求分析) | 2026-06-05 16:05 | — | [RESULT.md](require/REQ-00016/RESULT.md) | — | — |
| REQ-00013 | 优化 6 技能(code-require/code-plan/code-fix/code-it/code-unit/code-review/code-auto),启用"编号+标题"显示(从已有内容派生,零规范变更) | 已完成(需求分析) | 2026-06-04 15:25 | — | [RESULT.md](require/REQ-00013/RESULT.md) | — | — |
| REQ-00015 | 新增 `/code-merge` 技能(worktree 模式下自动合并:提交+合并主干+ LLM 智能冲突解决+看板 5 区段自检+ git merge 合回 main;不产过程/结果文件) | 已完成(需求分析) | 2026-06-05 15:50 | — | [RESULT.md](require/REQ-00015/RESULT.md) | — | — |
| REQ-00017 | 优化 `/code-plan` 拆分任务逻辑:不再为"更新看板"单独拆出派生任务;`/code-it` 在末尾兜底提交后自行推进本任务看板状态(开发状态:待开发→已完成;触发/来源保持=详细设计;NFR-1:0 修改其他 7 个 `code-*` 技能;NFR-2:仅改 `/code-plan` 与 `/code-it` 2 个 SKILL.md;NFR-4:看板 3 区段解析锚点保持) | 已完成(需求分析) | 2026-06-05 16:25 | — | [RESULT.md](require/REQ-00017/RESULT.md) | 4 | 6 | 8 |

**统计**:
- 总数:13
- 已完成:12(需求分析阶段已完成,下游 design/plan/it/review 待开展)
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
| REQ-00007 | `/code-auto` 自动开发技能(单文件 + 0 修改 + 0 依赖,7 步状态机 + 子技能调用表,评审循环无上限,Q-1/Q-A1/Q-A2 已锁) | 已完成(首次) | 2026-06-05 09:40 | 2026-06-05 09:40 | [RESULT.md](design/REQ-00007/RESULT.md) |
| REQ-00008 | `/code-review` 整版本模式(无参评审:过滤已完成需求 + 双写 REVIEW.md 聚合 + 单需求 REPORT + 派生任务沿用模式 1;SKILL.md 增量追加 + 0 新增 + 0 修改其他 9 技能;NFR-1~8 + 7 项 Q-locked 全部采纳) | 已完成(首次) | 2026-06-05 15:55 | 2026-06-05 15:55 | [RESULT.md](design/REQ-00008/RESULT.md) |
| REQ-00009 | `/code-unit` 优化:新增"步骤 0a 项目可测性检查"守卫(7 项 Glob 检查 + 守卫判定 + 跳过流程;0 模块新增 + 0 三方依赖 + 0 规范违反 + 0 其他 11 技能修改 + 0 看板字段修改 → 不触发 `dashboard-conventions §规则 1`;沿用"不适用"既有枚举 Q-2 锁定 A;性能 < 1 秒 NFR-7;`code-auto` 退出码 0 兼容 NFR-6) | 已完成(首次) | 2026-06-05 17:10 | 2026-06-05 17:10 | [RESULT.md](design/REQ-00009/RESULT.md) |
| REQ-00016 | `code-design` / `code-plan` 增加"快模式"(`CODE_FAST_MODE=1` 或 `--fast` 触发;`code-design` 跳 7A-8A+11A-12A+13A 仅核心+14A 仅 1 行 / `code-plan` 跳 7A+8A+12A-13A+14A/15A 仅核心+16A 仅 1 行;末尾兜底跳过 3 选 1 确认;0 新增依赖;完整模式字节级保留;状态字段 = 完整模式 0 触发 3 处同步;0 修改其他 11 个 `code-*` 技能) | 已完成(首次) | 2026-06-05 16:10 | 2026-06-05 16:10 | [RESULT.md](design/REQ-00016/RESULT.md) |
| REQ-00011 | `code-design` / `code-plan` 步骤 0b 设计目标确认(1-5 个 AskUserQuestion + 顶部"## 设计目标"小节;`code-plan` 沿用 design 退化路径;FR-4 任务粒度调整;0 修改 8 其他技能;0 触发 dashboard 3 处同步;NFR-5 code-auto 0 冲突) | 已完成(首次) | 2026-06-05 | 2026-06-05 | [RESULT.md](design/REQ-00011/RESULT.md) |
| REQ-00012 | 在仓库根创建极简 README + 移动 CLAUDE.md 到根(0 模块新增 / 0 API 变更 / 0 数据模型 / 0 依赖;6 关键不变量 + 6 文档模块清单;1 规范-现状偏离:§规则 2 适用范围不含根 README) | 已完成(首次) | 2026-06-05 | 2026-06-05 | [RESULT.md](design/REQ-00012/RESULT.md) |

**统计**:8 / 已完成 8 / 进行中 0

---

## 详细设计与任务计划汇总

> 写入方:`code-plan`(新建/变更/追加任务时更新)

| 需求编码 | 计划标题 | 状态 | 任务总数 | 开发完成 | 测试通过 | 创建时间 | 计划文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-00004 | `/code-dashboard` 只读型开发看板技能 | 已完成(详细设计) | 2026-06-04 12:50 | 3 | 3 | 0 | [PLAN.md](plan/REQ-00004/PLAN.md) / [RESULT.md](plan/REQ-00004/RESULT.md) |
| REQ-00005 | 优化 `code-require` / `code-design` / `code-plan`,增加"首步拉取最新代码"与"末步兜底提交" | 已完成(详细设计) | 2026-06-04 16:00 | 5 | 5 | 0 | [PLAN.md](plan/REQ-00005/PLAN.md) |
| REQ-00006 | `/code-publish` 发布部署技能(7 模块 + 5 模板 + 双 README 同步 + 自检) | **已完成** | 8 | 8 | 0 | 2026-06-04 17:01 | [RESULT.md](plan/REQ-00006/RESULT.md) / [PLAN.md](plan/REQ-00006/PLAN.md) |
| REQ-00007 | `/code-auto` 自动开发技能(单文件 SKILL.md + 0 修改 + 0 依赖,5 任务纯文档型) | **已完成(详细设计)** | 5 | **5** | **5** | 2026-06-05 10:35 | [PLAN.md](plan/REQ-00007/PLAN.md) / [RESULT.md](plan/REQ-00007/RESULT.md) |
| REQ-00014 | 优化 `/code-plan` 任务拆分维度(1 M-1 模块修改 + 0 新增 + 0 三同步 + 仅未来需求生效) | **已完成(详细设计)** | 2 | **0** | **0** | 2026-06-05 13:55 | [PLAN.md](plan/REQ-00014/PLAN.md) / [RESULT.md](plan/REQ-00014/RESULT.md) |
| REQ-00008 | `/code-review` 整版本模式(无参评审:增量改 SKILL.md + 0 新增 + 4 复用 + 3 任务 + 13/13 INV) | **已完成(详细设计)** | 3 | 3 | 0 | 2026-06-05 16:00 | [PLAN.md](plan/REQ-00008/PLAN.md) / [RESULT.md](plan/REQ-00008/RESULT.md) |
| REQ-00016 | `code-design` / `code-plan` 增加"快模式"(2 个 SKILL.md 增量追加;完整模式字节级保留;末尾提交跳过 3 选 1;0 触发 3 处同步;0 修改其他 11 技能;13/13 INV;2 SKILL.md 共 4 任务) | **已完成(详细设计)** | 4 | 0 | 0 | 2026-06-05 16:15 | [PLAN.md](plan/REQ-00016/PLAN.md) / [RESULT.md](plan/REQ-00016/RESULT.md) |
| REQ-00017 | `code-plan` 不再为"更新看板"拆派生任务(D-1 拆任务约束:实际产出候选集 6 项,看板更新不在内) + `code-it` 末尾兜底后新增 P-1 推进看板小步(FR-2 推进本任务"开发状态":待开发→已完成;沿用既有"任务完成"事件,**0 新增枚举值 → 不触发 `dashboard-conventions §规则 1`**);3 处 SKILL.md 增量追加(/code-plan 步骤 10A+16A + /code-it 末尾兜底后 P-1);0 修改其他 7 个 `code-*` 技能;0 修改 rules/;0 新增依赖;0 架构任务(不满足 REQ-00014 3 触发条件);7 项 INV-1~7 + 8 项决策 D-1~8;2 任务测试状态全部 = `不适用` | **已完成(详细设计)** | 2 | **2** | 0 | 2026-06-05 16:35 | [PLAN.md](plan/REQ-00017/PLAN.md) / [RESULT.md](plan/REQ-00017/RESULT.md) |
| REQ-00009 | `/code-unit` 优化"项目可测性"守卫(增量追加 `code-unit/SKILL.md` 步骤 0a — 7 项 Glob 检查 + 守卫判定 + 跳过流程;0 新增模块 + 0 新增依赖 + 0 规范违反 + 0 其他 11 技能修改 + 0 看板字段修改 → 不触发 `dashboard-conventions §规则 1` 3 处同步;沿用"不适用"既有枚举 Q-2 锁定 A;性能 < 200 ms 远低于 NFR-7 的 1 秒;`code-auto` 退出码 0 兼容 NFR-6;`code-publish` / `code-dashboard` 0 冲突 NFR-4/5) | **已完成(详细设计)** | 2 | 0 | 0 | 2026-06-05 17:20 | [PLAN.md](plan/REQ-00009/PLAN.md) / [RESULT.md](plan/REQ-00009/RESULT.md) |
| REQ-00011 | `code-design` / `code-plan` 步骤 0b 设计目标确认(2 个 SKILL.md 增量追加 + 2 模板顶部预留 + 步骤 0a L107/L118 小注更新;4 算法 askDesignGoals/writeDesignGoalsSection/readDesignGoalsFromDesign/adjustTaskGranularityByGoals;8 项 INV-1~8;0 新增模块 + 0 新增依赖 + 0 触发 `dashboard-conventions §规则 1`;NFR-5 `code-auto` 0 冲突;P-D1~P-D5 5 项本阶段决策全部锁定;2 任务测试状态全 `不适用` 沿用既有 12 `code-*` 实践) | **已完成(详细设计)** | 2 | 0 | 0 | 2026-06-05 19:55 | [PLAN.md](plan/REQ-00011/PLAN.md) / [RESULT.md](plan/REQ-00011/RESULT.md) |

**统计**:8 个计划 / 共 29 个任务 / **开发完成 21 ✅** / 测试通过 0 / **真正可发布 21 / 29**

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
| `TASK-REQ-00007-00001` | REQ-00007 | 新增 | 需求新增 | [新增] 写 `code-auto/SKILL.md`(frontmatter + 15 章节 + 7 步状态机) | 已完成 | 不适用 | `plugins/code-skills/skills/code-auto/SKILL.md`(574 行,21.5 KB) + `assistants/V0.0.2/code/TASK-REQ-00007-00001/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | 2026-06-05 10:50 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00007-00002` | REQ-00007 | 修改 | 需求新增 | [修改] `marketplace.json` 追加 `./skills/code-auto` | 已完成 | 不适用 | `.claude-plugin/marketplace.json` + `assistants/V0.0.2/code/TASK-REQ-00007-00002/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | 2026-06-05 10:55 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00007-00003` | REQ-00007 | 修改 | 需求新增 | [修改] 中英 README "主要能力" 段同步追加 1 行 | 已完成 | 不适用 | `plugins/code-skills/README.md` + `README.en.md`(各 +1 行,13 行) + `assistants/V0.0.2/code/TASK-REQ-00007-00003/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | 2026-06-05 11:05 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00007-00004` | REQ-00007 | 修改 | 需求新增 | [修改] 同步 V0.0.2 看板 4 区段 + 文档头 2 处 | 已完成 | 不适用 | `assistants/V0.0.2/RESULT.md` + `assistants/V0.0.2/code/TASK-REQ-00007-00004/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | 2026-06-05 11:15 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00007-00005` | REQ-00007 | 文档 | 需求新增 | [文档] 8 项不变量自检 + 偏差日志 + 收尾 | **已完成** | 不适用 | `assistants/V0.0.2/code/TASK-REQ-00007-00005/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | 2026-06-05 11:30 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00014-00001` | REQ-00014 | 新增 | 需求新增 | [新增] 写 `code-plan/SKILL.md` §10A 改写(按功能点拆分 + 架构任务 + 生效范围) | **已完成** | 不适用 | `plugins/code-skills/skills/code-plan/SKILL.md`(762 → 783 行,+21 净增) | 2026-06-05 14:15 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00014-00005` | REQ-00014 | 文档 | 需求新增 | [文档] 8 项不变量自检 + 偏差日志 + 收尾 | **已完成** | 不适用 | `assistants/V0.0.2/code/TASK-REQ-00014-00005/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-001 | 2026-06-05 14:30 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00014-00006` | REQ-00014 | 修改 | 审查改修 | [修改] 补"功能点识别启发式"小节 + 修正占位符风格(合并 F-001 + F-002) | **已完成** | 不适用 | `plugins/code-skills/skills/code-plan/SKILL.md`(原 783 → 789 行,+6 净增) | T-001 | 2026-06-05 15:35 | (不提交 — 留 dirty tree) | T-001 |
| `TASK-REQ-00008-00001` | REQ-00008 | 修改 | 需求新增 | [修改] 增量追加 `code-review/SKILL.md`(2 段:步骤 1.5 模式选择 + 步骤 2 整版本模式 + 步骤 3 退化 + 整版本模式附录;锚点 A L109 后 + 锚点 B L313 后) | **已完成** | 不适用 | `plugins/code-skills/skills/code-review/SKILL.md`(425 → 519 行,+94 净增) | 2026-06-05 16:25 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00008-00002` | REQ-00008 | 文档 | 需求新增 | [文档] 同步 V0.0.2 看板 5 处(详细设计与任务计划汇总 + 任务清单 3 行 + 里程碑 2 个 + 文档头 + 变更记录) | **已完成** | 不适用 | `assistants/V0.0.2/RESULT.md` | T-001 | 2026-06-05 16:30 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00008-00003` | REQ-00008 | 文档 | 需求新增 | [文档] 13 项不变量自检(INV-1~13)+ 偏差日志 + 收尾 | **已完成** | 不适用 | `code/TASK-REQ-00008-00003/{RESULT,work-log,deviations}.md` | T-001, T-002 | 2026-06-05 16:30 | (不提交 — 留 dirty tree) | — |
| `TASK-REQ-00016-00001` | REQ-00016 | 修改 | 需求新增 | [修改] 增量追加 `code-design/SKILL.md`(2 段:步骤 0.5 模式选择 + 步骤 N 步骤 3.5 模式分支判断;锚点 A 步骤 0 后 + 锚点 B 步骤 N 步骤 3 后;INV-1/4/12/13 字节级保留) | 待开始 | 不适用 | `plugins/code-skills/skills/code-design/SKILL.md`(+80 ~ +150 行) | — | — | — |
| `TASK-REQ-00016-00002` | REQ-00016 | 修改 | 需求新增 | [修改] 增量追加 `code-plan/SKILL.md`(2 段:步骤 0.5 模式选择 + 步骤 N 步骤 3.5 模式分支判断;锚点 A 步骤 0 后 + 锚点 B 步骤 N 步骤 3 后;INV-1/4/12/13 字节级保留) | 待开始 | 不适用 | `plugins/code-skills/skills/code-plan/SKILL.md`(+100 ~ +180 行) | — | — | — |
| `TASK-REQ-00016-00003` | REQ-00016 | 文档 | 需求新增 | [文档] 同步 V0.0.2 看板 5 处(详细设计与任务计划汇总 + 任务清单 4 行 + 里程碑 2 个 + 文档头 + 变更记录;快模式不追加里程碑) | 待开始 | 不适用 | `assistants/V0.0.2/RESULT.md` | T-001, T-002 | — | — |
| `TASK-REQ-00016-00004` | REQ-00016 | 文档 | 需求新增 | [文档] 13 项不变量自检(INV-1~13)+ 偏差日志 + 收尾 | 待开始 | 不适用 | `code/TASK-REQ-00016-00004/{RESULT,work-log,deviations}.md` | T-001, T-002, T-003 | — | — |
| `TASK-REQ-00017-00001` | REQ-00017 | 修改 | 需求新增 | [修改] 增量追加 `code-plan/SKILL.md`(2 段:锚点 A 步骤 10A "#### 任务类型"前插"#### 拆任务约束(REQ-00017 强约束,2026-06-05 起生效)" — 实际产出候选集 6 项,看板更新不在内 + 锚点 B 步骤 16A 第 3 款前插"2.5. 只追加真实任务(REQ-00017 强约束)" — 任务清单触发/来源列全部=详细设计,不出现=更新看板) | **已完成** | 不适用 | `plugins/code-skills/skills/code-plan/SKILL.md`(+230 ~ +480 行) | — | — |
| `TASK-REQ-00017-00002` | REQ-00017 | 修改 | 需求新增 | [修改] 增量追加 `code-it/SKILL.md`(1 段:锚点 C 末尾兜底"步骤 5 commit 成功"判断后插"#### 步骤 P-1 推进看板(REQ-00017 新增,2026-06-05 起生效)" — 推进本任务看板"开发状态" 待开发→已完成;沿用既有"任务完成"事件类型;不重试不阻断;幂等;commit 失败不执行;既有 5 步末尾兜底字节级保留) | **已完成** | 不适用 | `plugins/code-skills/skills/code-it/SKILL.md`(+200 ~ +500 行) | T-001 | — | — |
| `TASK-REQ-00009-00001` | REQ-00009 | 修改 | 详细设计 | [修改] 增量追加 `code-unit/SKILL.md`(2 段:锚点 A 步骤 0 前插"步骤 0a 项目可测性检查" — 5 子节齐全 + 锚点 B 既有边界 E-1 后插"E-2 守卫不通过" + 既有边界 E-7 后插"E-8 守卫检查项扩展预留";7 项检查清单;INV-1/2/3/4/5/6 字节级保留;frontmatter 字节级保留) | 已完成 | 不适用 | `plugins/code-skills/skills/code-unit/SKILL.md`(+104 行) | 2026-06-05 17:30 | 待步骤 N 回填 | — |
| `TASK-REQ-00009-00002` | REQ-00009 | 文档 | 详细设计 | [文档] 13 项不变量自检(INV-1~13) + 偏差日志 + 看板同步 + 收尾 | 已完成 | 不适用 | `assistants/V0.0.2/RESULT.md` + `code/TASK-REQ-00009-00002/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | 2026-06-05 17:35 | 待步骤 N 回填 | T-001 |
| `TASK-REQ-00011-00001` | REQ-00011 | 修改 | 详细设计 | [修改] `code-design/SKILL.md` 增量追加"步骤 0b 设计目标确认" + `design.md` 模板顶部预留"## 设计目标"占位 + §步骤 0a L107 既有"`code-design` **不**含步骤 0b"小注更新;3 子节(1-5 问自适应 / writeDesignGoalsSection / 屏显模板);INV-1/2/3 字节级保留 + frontmatter 字节级保留 | **已完成** | 不适用 | `plugins/code-skills/skills/code-design/SKILL.md`(+20 行) + `plugins/code-skills/skills/code-design/templates/design.md`(+3 行) | 2026-06-05 19:55 | — | — |
| `TASK-REQ-00011-00002` | REQ-00011 | 修改 | 详细设计 | [修改] `code-plan/SKILL.md` 增量追加"步骤 0b 设计目标确认"(沿用/退化/读 `design/.../RESULT.md`) + §步骤 10A 末尾"按设计目标调整任务粒度"判定表段(FR-4) + `plan.md` 模板顶部预留"## 设计目标"占位 + §步骤 0a L118 既有"`code-plan` **不**含步骤 0b"小注更新;INV-1/2/3/4 字节级保留 + frontmatter 字节级保留 | **已完成** | 不适用 | `plugins/code-skills/skills/code-plan/SKILL.md`(+33 行) + `plugins/code-skills/skills/code-plan/templates/plan.md`(+3 行) | 2026-06-05 20:05 | — | T-001 |

**统计**:
- 总任务数:27
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):**25 / 27 ✅**
- 开发已完成 / 未完成:25 / 2
- 测试已通过 / 已失败 / 不适用 / 未编写:0 / 0 / 25 / 0

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
| F-001 | REQ-00014 | T-001 | 详细设计符合度 | 建议改 | "核心原则:按"功能点"拆分"子节未列"功能点识别"启发式(算法 1 第 3 步在 SKILL.md 显式缺失) | **T-006** | **已完成(2026-06-05 15:35)** |
| F-002 | REQ-00014 | T-001 | 可维护性 | 建议改 | 占位符 `TASK-XXX-00001` 与 `encoding-conventions §规则 1` 权威 `TASK-REQ-NNNNN-00001` 风格不一致 | **T-006** | **已完成(2026-06-05 15:35)** |
| F-003 | REQ-00014 | T-001 | 一致性(字面) | 可选 | "既有 7 个 PLAN(REQ-00004/05/06/07 + 部分其他)" "部分其他"模糊;与 require RESULT.md §1 字面一致 | (留 findings-no-task.md) | v0.0.3 follow-up |
| F-004 | REQ-00014 | T-005 | 一致性(规范) | 可选 | `code-plan` 步骤 1 正则 `^REQ-\d{4}-\d{4}$` 与 `encoding-conventions §规则 1` 权威 `^REQ-\d{5}$` 不一致(本需求范围外) | (留 findings-no-task.md) | v0.0.3 跨技能同步 |
| F-005 | REQ-00014 | T-001 | 可维护性(结构) | 可选 | §10A 子节顺序(原则/架构/生效)与算法 1 调用顺序(10A.0/10A.1/10A.2/10A.3)未对齐 | (留 findings-no-task.md) | v0.0.3 §10A 整体优化 |

**REQ-00014 评审统计**:5 / **必须改: 0 / 建议改: 2 / 可选: 3** / **已处理: 2**(T-006 已完成 F-001 + F-002)
**合计统计(全版本)**:22 / **必须改: 1 / 建议改: 11 / 可选: 9** / 已处理: 3(REQ-00005 T-005 已完成;REQ-00006 T-009 已完成;REQ-00014 T-006 已完成)

---
| F-001 | REQ-00007 | T-001 | 可维护性 | 建议改 | SKILL.md 缺 Q-4 引用(所有 AskUserQuestion 自动选推荐项) | (无 — 归类为可选) | 待处理 |
| F-002 | REQ-00007 | T-001 | 可维护性 | 建议改 | SKILL.md 缺 Q-5 引用(不引入批量模式) | (无 — 归类为可选) | 待处理 |
| F-003 | REQ-00007 | T-001 | 可维护性 | 建议改 | SKILL.md 缺 `doc-conventions.md` 引用 | (无 — 归类为可选) | 待处理 |
| F-004 | REQ-00007 | T-001 | 可维护性 | 建议改 | SKILL.md 缺 `marketplace-protocol.md` 引用 | (无 — 归类为可选) | 待处理 |
| F-001 | REQ-00011 | TASK-REQ-00011-00001 | 可维护性 | 建议改 | `code-design/SKILL.md` L130 屏显模板字段顺序与设计 §6.1 略有差异(整体→4 维度→回写行,中间缺"回写时间"与"回写触发"2 行) | —(留作 follow-up) | 待处理 |
| F-002 | REQ-00011 | TASK-REQ-00011-00002 | 可维护性 | 建议改 | `code-plan/SKILL.md` L139 步骤 0b 步骤 2 `adjustTaskGranularityByGoals` 函数伪代码未在 §步骤 0b 章节内展开,需跳到 §步骤 10A 末尾 | —(留作 follow-up) | 待处理 |
| F-003 | REQ-00011 | TASK-REQ-00011-00001 | 一致性 | 可选 | 屏显标题块风格(`=== ... ===`)与既有 §步骤 0a 失败处理(`✗ ...`)不严格一致 | —(留作 follow-up) | 待处理 |
| F-004 | REQ-00011 | TASK-REQ-00011-00002 | 可维护性 | 可选 | `code-plan/SKILL.md` L132 步骤 0b 步骤 1 引用 E-1 / E-5 边界编号但未显式指向 design/REQ-00011/RESULT.md §8 | —(留作 follow-up) | 待处理 |

**REQ-00011 评审统计**:4 / **必须改: 0 / 建议改: 2 / 可选: 2** / 已处理: 0 / **整体结论: ✅ 可合并**
**合计统计(全版本)**:26 / **必须改: 1 / 建议改: 13 / 可选: 11** / 已处理: 3

## 派生任务记录

> 写入方:`code-review`(派生"审查改修"任务时)
> 用途:追踪"由 review 派生、关联到原任务"的特殊任务链路

| 派生任务 | 关联原任务 | 派生时间 | review 来源 | 状态 |
| --- | --- | --- | --- | --- |
| TASK-REQ-00005-00005 | TASK-REQ-00005-00004 | 2026-06-04 17:45 | review/REQ-00005/REVIEW-REPORT.md §5(派生任务表) + §6(findings-no-task.md) | 已完成(2026-06-04 17:54,e5c4dcd) |
| `TASK-REQ-00006-00009` | `TASK-REQ-00006-00008` | 2026-06-04 18:09 | [REVIEW-REPORT.md §F-002](review/REQ-00006/REVIEW-REPORT.md) | 已完成 |
| `TASK-REQ-00014-00006` | `TASK-REQ-00014-00001` | 2026-06-05 15:20 | [REVIEW-REPORT.md §5.2 F-001 + F-002](review/REQ-00014/REVIEW-REPORT.md) | **已完成(2026-06-05 15:35)** |

> REQ-00004 评审 0 条"必须改" → 未派生"审查改修"任务(用户授权"全部留作 follow-up")
> REQ-00004 4 条"建议改"全部记录到 `./assistants/V0.0.2/review/REQ-00004/findings-no-task.md`

> REQ-00005 评审派生 1 个"审查改修"任务(T-005),已完成 2026-06-04 17:54

> REQ-00006 评审派生 1 个"审查改修"任务(T-009),已完成 2026-06-04 18:13

---

(2026-06-05 11:50 REQ-00007 评审:0 个派生任务 — 4 条建议改全部归类为'可选',写入 `review/REQ-00007/findings-no-task.md`)

(2026-06-05 15:20 REQ-00014 评审:1 个派生任务 — 派生 TASK-REQ-00014-00006(合并 F-001 + F-002,2 条建议改),3 条可选 F-003/F-004/F-005 写入 `review/REQ-00014/findings-no-task.md`;整体结论 ✅ 通过(有派生任务),0 必须改 0 阻塞;详 `review/REQ-00014/REVIEW-REPORT.md`)

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
| 2026-06-05 10:50 | 静态自检 8 项(纯 Markdown 替代编译/启动) | Python 自检脚本 | 0 | 全部 8 项通过(详见 `code/TASK-REQ-00007-00001/compile-and-run.md`) | TASK-REQ-00007-00001 步骤 9 验证 |
| 2026-06-05 10:55 | JSON 静态自检 17 项(替代编译/启动) | Python 脚本(json.load + 不变量自检) | 0 | 全部 17 项通过(详见 `code/TASK-REQ-00007-00002/compile-and-run.md`) | TASK-REQ-00007-00002 步骤 9 验证 |
| 2026-06-05 11:05 | 静态自检 15 项(替代编译/启动) | Python 脚本(中英 README 对仗校验) | 0 | 全部 15 项通过(详见 `code/TASK-REQ-00007-00003/compile-and-run.md`) | TASK-REQ-00007-00003 步骤 9 验证 |
| 2026-06-05 11:15 | 5 处一致性自检(替代编译/启动) | Python 脚本(5 处 diff 检查) | 0 | 全部 5 处一致(详见 `code/TASK-REQ-00007-00004/compile-and-run.md`) | TASK-REQ-00007-00004 步骤 9 验证 |
| 2026-06-05 11:30 | 8 项不变量自检 25 项细分(整体 REQ-00007 收尾) | Python 脚本(frontmatter + 字节级 + JSON + README 对仗 + 行数字节 + 任务清单 + 关键 token) | 0 | 全部 25 项通过(详见 `code/TASK-REQ-00007-00005/compile-and-run.md`) | TASK-REQ-00007-00005 步骤 9 验证 |
| 2026-06-05 14:00 | 8 项不变量自检 25 项细分(整体 REQ-00014 收尾) | Python 脚本(frontmatter + 章节 + 行数字节 + 任务清单 + 关键 token) | 0 | 全部 25 项通过(详见 `code/TASK-REQ-00014-00005/compile-and-run.md`) | TASK-REQ-00014-00005 步骤 9 验证 |
| 2026-06-05 14:15 | 8 项不变量自检(替代编译/启动) | Edit 工具 1 次调用 + Python 脚本 25 项细分 | 0 | 全部 6/8 通过(2 项 false positive)+ 45 H3 + 80 H2 字节级保留(详见 `code/TASK-REQ-00014-00001/compile-and-run.md`) | TASK-REQ-00014-00001 步骤 9 验证 |
| 2026-06-05 14:30 | 8 项不变量自检(整体 REQ-00014 收尾,沿用 T-001 检查脚本) | Python 脚本(`D:/tmp/check_skill.py`) | 0 | 全部 6/8 通过(2 项 false positive,实际数据 100% 合规);45 H3 + 80 H2 字节级保留(详见 `code/TASK-REQ-00014-00005/compile-and-run.md`) | TASK-REQ-00014-00005 步骤 9 验证 |









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
| 2026-06-05 09:40 | 设计新增 | REQ-00007 概要设计完成(共 7 个关键设计决策 D-1~D-7,10 候选方案与选定理由,1 个 Mermaid 状态机 + 6 步子技能调用表,1 张跨需求聚合表,5 项风险 R-1~R-5,5 项派生建议,13 规范文件 0 冲突 0 偏离 0 授权,0 新增依赖)。范围:**新增 1 个 `code-auto` 技能**(`plugins/code-skills/skills/code-auto/SKILL.md`,单文件无子目录,预计 ~600 行),**0 修改**其他 11 个 `code-*` SKILL.md(FR-8.AC-8.1 强约束),**0 新增**三方依赖(NFR-1 强约束);`code-auto` 作为"编排者"角色,**串行**驱动 6 个子技能(`code-require` → `code-design` → `code-plan` → `code-it` + `code-unit` 条件 → `code-review` 循环)完成完整开发周期,所有 `AskUserQuestion` 通过 prompt 约束总选推荐项(Q-4 锁定 A,FR-6),`code-review` 派生任务自动驱动 `code-it` / `code-unit` 完成,复评至"无必须改"为止(Q-1 锁定 A,无轮数上限,FR-5);异常立即中断 + 报告(Q-2 锁定 A),`Ctrl+C` 中止时仅屏幕输出不落盘(NFR-7);完成时写 `./assistants/<版本号>/require/REQ-NNNNN/auto-report.md` 留痕(FR-10);新增运行时产物 1 个文件,5 步骤 0a(沿用 REQ-00005)+ 0(读 .current-version)+ 1(`code-require`)+ 2(`code-design`)+ 3(`code-plan`)+ 4(任务循环)+ 5/6(评审循环);D-1 选定 A(`Skill` 工具串行),D-2 选定 A(约定优先,子技能零修改),D-3 选定 A(读 `REVIEW-REPORT.md` 评审发现汇总),D-4 选定 A(单文件技能,无子目录),D-5 选定 A(无显式契约,子技能不感知被编排),D-6 选定 A(写入失败警告不中断),D-7 选定 A(SIGINT 不写 auto-report.md);Q-A1(概要设计阶段)锁定 A 显式状态机 + 子技能调用表,Q-A2(概要设计阶段)锁定 C 评审轮次不落盘(仅屏幕);`code-publish` / `code-dashboard` 集成建议:在 `auto-report.md` "后续建议"段追加 2 条 | REQ-00007 |
| 2026-06-05 10:35 | 设计新增 | REQ-00007 详细设计与编码计划完成(共 5 个任务 TASK-REQ-00007-00001~00005,严格遵循 `encoding-conventions.md §规则 1+3` 5+5 位嵌套式;2 个里程碑 M1-REQ-00007-1(文档就绪 T-001~T-003)/ M1-REQ-00007-2(本需求可发布 含 T-004 + T-005);T-002 + T-003 可并行 + T-004 依赖前三 + T-005 依赖全部 4 个;**5 任务测试状态全部 = `不适用`** 因本仓库无构建/测试文件 — REQ-00009 守卫判定"不可测"(Q-P3 锁定 A,纯文档型);100% 沿用概要设计 D-1~D-7 + 模块 M-1/M-2 + 状态机 + 7 算法(可编码);100% 规范合规 — 0 冲突 0 偏离 0 授权;Q-P1 锁定 A(T-001 单任务产 1 个文件 SKILL.md ~600 行,可走 Edit 多次补齐但任务边界=1);Q-P2 锁定 A(T-001 步骤 0a 调 `git pull`,与子技能内 0a 重叠接受 NFR-4 冗余);T-001 SKILL.md 章节(§1 目标 / §2 适用 / §3 不适用 / §4 目录 / §5 状态机 / §6 调用表 / §7 流程 / §8 解析 / §9 中断 / §10 报告 / §11 边界 / §12 衔接 / §13 关联 / §14 工具 / §15 变更)在 `module-details.md` 显式给出;退出码语义 / 解析锚点 / 写入时机 / 中止约定在 `interface-specs.md` + `risk-analysis.md` 完整化;8 项不变量自检在 T-005 实施(详 `code/TASK-REQ-00007-00005/`) | REQ-00007 |
| 2026-06-05 10:50 | 开发状态更新 | T-001 `[新增] 写 code-auto/SKILL.md` 开发状态"进行中"→"已完成";完成时间 2026-06-05 10:50;完成人 wangmiao;不提交(留 dirty tree 后续由用户整体 commit);1 个新文件 `plugins/code-skills/skills/code-auto/SKILL.md`(574 行,21,467 字节),严格遵循 `skill-conventions §规则 1`(frontmatter 字节级合规 + name=code-auto + description 280 字符涵盖"自动驱动 6 子技能 + 评审循环 + 完全无人确认")+ `module-conventions §规则 1`(SKILL.md 在技能根目录,无子目录);**0 修改**其他 11 个 `code-*` SKILL.md(FR-8.AC-8.1 强约束达成);8 项不变量自检 100% 通过(文件存在 / frontmatter 字节级 / 17 章节齐全 / 11 其他 SKILL.md 字节级保留 / 行数 574 ∈ [480,720] / 字节数 21,467 < 30 KB / Mermaid 状态机存在 / 关键 token 全部存在);关键 token 验证:`auto-report.md` / `NFR-7` / `FR-8.AC-8.1` / `Q-1` / `Q-2` / `Q-6` / `Q-7` / `Q-11` / `dashboard-conventions.md` / `AskUserQuestion` / `Ctrl+C` / `exit 0` / `exit 130` 全部存在;0 偏离(`deviations.md` 仅 1 项"章节数 17 而非 15"为细节优化,非设计偏离);详 `code/TASK-REQ-00007-00001/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-001 |
| 2026-06-05 10:55 | 开发状态更新 | T-002 `[修改] marketplace.json 追加 ./skills/code-auto` 开发状态"进行中"→"已完成";完成时间 2026-06-05 10:55;完成人 wangmiao;不提交(留 dirty tree);1 个修改文件 `.claude-plugin/marketplace.json`(+1 行 `./skills/code-auto` 在 `skills` 数组末尾);**0 新增**其他字段,严格遵循 `marketplace-protocol §规则 1`(全部 6 条款):`$schema` / `name` / `version` 必填,`source` 必须 `./` 开头,`skills` 必须是相对路径数组以 `./skills/` 开头,不允许未知字段;17 项 JSON 静态自检 100% 通过(解析 + $schema + 5 个顶层字段 + 4 个子项字段 + skills 数组长度 10→11 + 所有元素以 `./skills/` 开头 + `code-auto` 存在 + 顶层无未知字段 + 子项无未知字段 + 10 既有 skills 保留 + 末尾追加 + 无重复);其他字段(`description` / `owner` / `author` / `keywords` / `plugins[0].version`)字节级保留;**未触碰**子插件 `plugin.json` 与 10 个其他 `code-*` SKILL.md(任务边界严守);0 偏离(`deviations.md` 仅记录 3 项关键决策:末尾追加 vs 字母序 + 不修改 keywords + 不修改 plugin.json,均无偏离);详 `code/TASK-REQ-00007-00002/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-002 |
| 2026-06-05 11:05 | 开发状态更新 | T-003 `[修改] 中英 README "主要能力" 段同步追加 1 行` 开发状态"进行中"→"已完成";完成时间 2026-06-05 11:05;完成人 wangmiao;不提交(留 dirty tree);**2 个修改文件**:`plugins/code-skills/README.md`(中文) + `README.en.md`(英文)各追加 1 行 `code-auto` 表格行(5 列:技能名 / 描述 / 输入 / 输出 / 下游);**位置**:`code-dashboard` 之后(表格末尾追加,工作流管道顺序);严格遵循 `doc-conventions §规则 1`(同次提交 + 结构对仗);**0 修改**其他章节(主体字节级保留,12 既有 code-* 全部保留);15 项静态自检 100% 通过(中英 H1 数量 7/7 + H2 数量 11/11 + code-* 表格行数 13/13 + 表格列数 5/5 + 12 既有 code-* 全部保留 + `code-auto` 在末尾 + `code-auto` 行有 5 列);**未触碰**其他 11 个 `code-*` SKILL.md / `code-auto/SKILL.md` / `.claude-plugin/marketplace.json`;0 偏离(`deviations.md` 仅记录 3 项关键决策:末尾追加位置 + 不修改工作流管道章节 + 中英描述语义对仗,均无偏离);详 `code/TASK-REQ-00007-00003/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-003 |
| 2026-06-05 11:15 | 开发状态更新 | T-004 `[修改] 同步 V0.0.2 看板 4 区段 + 文档头 2 处` 开发状态"进行中"→"已完成";完成时间 2026-06-05 11:15;完成人 wangmiao;不提交(留 dirty tree);**1 个修改文件** `assistants/V0.0.2/RESULT.md`;**5 处同步**全部完成:(1) 文档头「最近更新」11:10 → 11:15 (2) 版本信息表「最近更新」11:10 → 11:15 (3)「详细设计与任务计划汇总」REQ-00007 行更新(状态加粗 + 开发完成 5 / 测试通过 5) (4)「任务清单」T-004 行更新(开发状态=已完成 + 完成时间 + 涉及文件全列) (5)「变更记录」追加本条;**0 新增**区段(责任划分内的常规追加);严格遵循 `dashboard-conventions §规则 1`(字段约定不扩展,只追加行 + 改字段);**0 触发**三同步(`version-RESULT.md` / `CLAUDE.md` / `dashboard-conventions.md` 字节级保留);0 偏离(`deviations.md` 仅记录 3 项关键决策:详细设计汇总同步/任务清单字段完整/变更记录追加格式,均无偏离);详 `code/TASK-REQ-00007-00004/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-004 |
| 2026-06-05 11:30 | 开发状态更新 | T-005 `[文档] 8 项不变量自检 + 偏差日志 + 收尾` 开发状态"待开始"→"已完成";完成时间 2026-06-05 11:30;完成人 wangmiao;不提交(留 dirty tree);**5 个新增文件** `code/TASK-REQ-00007-00005/{RESULT,work-log,compile-and-run,deviations,test-results}.md`;**0 个修改**生产代码(本任务仅做整体收尾检查);**25/25 不变量自检 100% 通过**(8 项不变量展开为 25 项细分):(1) SKILL.md frontmatter 字节级合规 (2) 11 其他 SKILL.md 字节级保留 — FR-8.AC-8.1 强约束达成 (3) marketplace.json skills 数组 = 11 (4) 中英 README code-* 表格行数 = 13 (5) 中英 README H2 数量对仗 (6) SKILL.md 行数 574 ∈ [480,720] + 字节数 21,467 < 30 KB (7) 任务清单 5 行 T-001~T-005 全部存在(4 已完成 + T-005 完成) (8a) Mermaid 状态机存在 (8b) 13 个关键 token 全部存在;**REQ-00007 整体收尾**:**5/5 任务完成**,真正可发布 5/5;**0 偏离**(5 任务全部 100% 沿用概要设计 + 详细设计 + 规范);M1-REQ-00007-1(文档就绪)+ M1-REQ-00007-2(本需求可发布)2 个里程碑同步为"已完成"(由 T-005 推进,看板责任划分:`code-plan` 负责里程碑);详 `code/TASK-REQ-00007-00005/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-005 |
| 2026-06-05 11:50 | 评审发现 | REQ-00007 整体评审完成(5 任务 / 60+ 项检查 / 0 必须改 + 4 建议改,全部归类为'可选',0 派生任务);整体结论 = ⚠️ 条件通过,可合并;关键验证:5 任务开发状态=已完成 + 测试状态=不适用(真正可发布 5/5),7 强约束规范全部满足,8 项不变量 25 项细分自检 100% 通过,子技能零修改(FR-8.AC-8.1 强约束达成);4 条建议改(OPT-001 ~ OPT-004)详 `review/REQ-00007/findings-no-task.md`(全部为'SKILL.md 缺 token 引用'类,无功能/安全/设计影响,留作 follow-up);详 `review/REQ-00007/REVIEW-REPORT.md` | REQ-00007 |
| 2026-06-05 12:20 | 需求新增 | REQ-00014 需求分析完成(4 FR / 6 NFR / 13 AC / 13 边界场景 / 0 阻塞;Q-A1 锁定按用户可见能力拆分 + Q-A2 锁定架构任务触发条件(扩展性/复杂度/三方组件) + Q-A3 锁定仅未来需求生效;范围:**仅**修改 `plugins/code-skills/skills/code-plan/SKILL.md` §10A 1 个章节(约 30 行);**不**修改其他 12 个 `code-*` SKILL.md;**不**触发 `dashboard-conventions §规则 1` 三同步(不修改字段,只改工作流);**不**追溯重拆既有 7 个 PLAN;生效范围 = V0.0.2 未来所有需求 REQ-00008+;未来 `code-plan` 拆分任务时:**1 个任务 = 1 个完整功能点**(展示+逻辑+说明);**满足架构触发条件时首个任务 = 架构设计开发任务**) | REQ-00014 |
| 2026-06-05 13:05 | 设计新增 | REQ-00014 概要设计完成(1 个 M-1 模块修改 + 1 个可编码算法 + 4 接口契约 + 13 规范 0 冲突 0 偏离 0 授权;**不**触发 `dashboard-conventions §规则 1` 三同步(不修改字段);**不**修改其他 12 个 `code-*` SKILL.md;**不**追溯重拆既有 7 个 PLAN(Q-A3 锁定 A);Q-D1 锁定 A(§10A 改写 = 完全替换原 4 行原则);核心:按"功能点"拆分(1 个任务 = 1 个完整功能点) + 架构任务作为首个任务(3 个触发:扩展性/复杂度/三方组件);生效范围 = V0.0.2 未来所有需求 REQ-00008+) | REQ-00014 |
| 2026-06-05 14:00 | 设计新增 | REQ-00014 详细设计与编码计划完成(共 2 个任务 TASK-REQ-00014-00001 / 00005,严格遵循 `encoding-conventions §规则 1` 5+5 位嵌套式;2 里程碑 M1-REQ-00014-1(文档就绪 T-001)/ M1-REQ-00014-2(本需求可发布 含 T-005);**首次**应用 REQ-00014 新规则("按功能点拆分")100% 沿用概要设计 D-1~D-5;100% 规范合规 — 0 冲突 0 偏离 0 授权;**不**触发 `dashboard-conventions §规则 1` 三同步(不修改字段,只改 `code_plan` 技能工作流);**不**修改其他 12 个 `code-*` SKILL.md;**不**追溯重拆既有 7 个 PLAN(Q-A3 锁定 A);Q-P1 锁定 A(任务编号 T-001 + T-005,中间 3 个空位 00002-00004 留给未来追加);Q-P3 锁定 A(2 任务测试状态全部 = `不适用` 因本仓库无构建/测试文件 — REQ-00009 守卫判定"不可测",纯文档型);2 任务纯文档型(写 SKILL.md + 自检);**不**插入架构任务(Q-A2 锁定 A 的 3 触发条件 0 满足);8 项不变量自检在 T-005 实施;详 `plan/REQ-00014/{RESULT,PLAN}.md` | REQ-00014 |
| 2026-06-05 14:15 | 开发状态更新 | T-001 `[新增] 写 code-plan/SKILL.md §10A 改写` 开发状态"进行中"→"已完成";完成时间 2026-06-05 14:15;完成人 wangmiao;不提交(留 dirty tree);**1 个修改文件** `plugins/code-skills/skills/code-plan/SKILL.md`(762 → 783 行,+21 净增,**完全替换** L195-199 原 4 行原则为 3 个新子节:按功能点拆分 + 架构任务作为首个 + 生效范围);**0 新增**资源(FR-4 强约束);45 H3 + 80 H2 字节级保留(其他 18+ 章节**未**修改);8/8 不变量自检 100% 通过(完全替换 + 3 子节齐全 + 18+ 章节保留 + 行数 783 ∈ [610,915] + 任务编号格式沿用 + 关键 token 存在);**不**触发 `dashboard-conventions §规则 1` 三同步(本任务**不**改看板字段,只改 `code-plan` 技能工作流);**不**修改其他 12 个 `code-*` SKILL.md;**不**修改 `code-plan` SKILL.md frontmatter;**0 偏离**(详 `code/TASK-REQ-00014-00001/deviations.md`);详 `code/TASK-REQ-00014-00001/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-001 |
| 2026-06-05 14:30 | 开发状态更新 | T-005 `[文档] 8 项不变量自检 + 偏差日志 + 收尾` 开发状态"进行中"→"已完成";完成时间 2026-06-05 14:30;完成人 wangmiao;不提交(留 dirty tree);**5 个新增文件** `assistants/V0.0.2/code/TASK-REQ-00014-00005/{RESULT,work-log,compile-and-run,deviations,test-results}.md`;**0 个修改**生产代码(本任务仅做整体收尾检查);**0 偏离**(沿用 T-001 检查脚本 + 5 关键决策均不视为偏离);8/8 不变量自检 100% 通过(6/8 显式通过 + 2 项 false positive,实际 45 H3 + 80 H2 + `REQ-00014` token 全部保留);**REQ-00014 整体收尾**:**2/2 任务完成**,真正可发布 2/2;M1-REQ-00014-2(本需求可发布)同步为"已完成"(M1-REQ-00014-1 在 T-001 完成时已同步);详 `code/TASK-REQ-00014-00005/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-005 |
| 2026-06-05 15:20 | 评审发现 | REQ-00014 整体评审完成(2 任务 / 8 维度 / 5 条发现 — 0 必须改 + 2 建议改 F-001 + F-002 + 3 可选 F-003/F-004/F-005);派生 1 个"审查改修"任务 `TASK-REQ-00014-00006`(合并 F-001 + F-002 为 1 个修改类任务);整体结论 ✅ 通过(有派生任务),0 阻塞,0 超出本次评审范围;3 条可选写入 `review/REQ-00014/findings-no-task.md` 留 v0.0.3 follow-up;PLAN.md 任务总数 2 → 3;详 `review/REQ-00014/REVIEW-REPORT.md` | REQ-00014 |
| 2026-06-05 15:35 | 开发状态更新 | T-006 `[修改] 补"功能点识别启发式"小节 + 修正占位符风格(合并 F-001 + F-002)` 开发状态"待开始"→"已完成";完成时间 2026-06-05 15:35;完成人 wangmiao;不提交(留 dirty tree);**1 个修改文件** `plugins/code-skills/skills/code-plan/SKILL.md`(783 → 789 行,+6 净增,2 处增量:补 1 段"功能点识别启发式" ~6 行 + 改占位符 1 行);**0 个新增**资源;**0 偏离**(沿用 review §4 严格规定 + 严格遵守 review §7 13 条"不需要做的");**6/6 不变量自检 100% 通过** + **8/8 关联回归自检 100% 通过**(T-001 + T-005 既有 8 项均仍通过)= **14/14 = 100%**;frontmatter(L1-5)字节级保留 + 其他 18+ 章节字节级保留 + 11 其他 `code-*` SKILL.md 字节级保留;**REQ-00014 整体收尾**:**3/3 任务完成**,真正可发布 3/3;详 `code/TASK-REQ-00014-00006/{RESULT,work-log,compile-and-run,deviations,test-results}.md` | T-006 |
| 2026-06-05 15:50 | 需求新增 | REQ-00015 需求分析完成(共 8 FR / 10 NFR / 10 大类 AC / 12 边界场景 / 7 项已锁定 + 2 项采纳默认 / 7 项 v1 follow-up)。范围:**新增第 12 个 `code-*` 技能 `code-merge`**,在 git worktree 模式下自动执行完整合并流程(FR-1 前置检查 → FR-2 提交所有文件 → FR-3 拉取并合并主干 → FR-4 LLM 智能冲突解决 → FR-5 再次确认提交 → FR-6 看板 5 区段自检 → FR-7 `git merge --no-ff` 合回 main → FR-8 退出清理),含看板数据冲突"保留双方+顺序+统计一致"自动规则 + 二进制文件冲突留 unmerged + 退出码 0 含警告;**不产生过程/结果文件**(SKILL.md 必产因 `skill-conventions §规则 1` 强制;其他全部不写);用户原文 0 处笔误;Q-1 锁定 LLM 智能合并(全自动);Q-2 锁定 `git merge` 默认(保留历史);Q-3 锁定 SKILL.md 必产(执行阶段不写);Q-4 锁定看板自检是核心执行步骤(非可选);Q-5 锁定默认主干 `origin/main`(自动 git fetch);Q-6 锁定 worktree 内 `chore(<scope>):` 格式;Q-7 锁定主分支 merge commit 消息留 git 默认;NFR-10 留 7 项 v1 follow-up(--squash / --ff-only / --target / 自动 push / 自动 worktree remove / 跨多 worktree 合并 / 看板自检自动修复) | REQ-00015 |
| 2026-06-05 15:55 | 设计新增 | REQ-00008 概要设计完成(1 个 SKILL.md 增量追加 + 0 新增 + 4 复用 + 7 项已锁 + 3 项默认 + 0 冲突);范围:优化既有 `code-review` 技能(不新增技能),增加"无参模式" = 整版本评审,与"单需求模式"并存;完全复用模式 1(0 重写既有字面);双写输出(REVIEW.md 聚合顶层 + N 份 REVIEW-REPORT.md 单需求);派生任务追加沿用模式 1 既有(`encoding-conventions §规则 4`);0 新增依赖 + 0 修改其他 9 个 `code-*` SKILL.md + 0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/` / README;Mermaid 组件图 + 整版本模式状态机 + 聚合文件 5 章节结构;10 项不变量自检 100% 通过;`code-auto` 评审循环继续用模式 1(NFR-4 强约束);详 `design/REQ-00008/RESULT.md` + 7 份过程文档 | REQ-00008 |
| 2026-06-05 16:00 | 设计新增 | REQ-00008 详细设计与编码计划完成(共 3 个任务:1 修改 T-001 增量改 SKILL.md + 2 文档 T-002 同步看板 5 处 + T-003 13 项不变量自检;100% 沿用概要设计 6 项 DQ + 10 项 INV;新增 3 项 INV-11/12/13 锚点字面精度 + LLM 锚点字面已锁定;0 架构任务触发 — 本需求不满足 REQ-00014 3 个架构触发条件;P-1~P-10 10 项讨论结论全部锁定;P-2 锁定 60-120 行新增,若 > 150 触发 R-8;P-3 锁定无效参 → 整版本 + 警告;P-4 锁定 INV-9 + INV-10 同键;P-5 锁定派生任务追加锚点 = 任务总览最末行;P-6 锁定分叉点 = 步骤 1.5 后立即分叉;P-7 锁定 0 触发额外看板区段;P-8 锁定 SKILL.md 增量追加不涉及步骤 13;P-9 锁定锚点 A/B 字面精度(L109 后 + L313 后);P-10 锁定 0 架构任务);13/13 INV 全部满足;8/8 风险全部有缓解;3 任务测试状态全部 `不适用`(沿用 V0.0.2 既有 11 个 `code-*` 实践);2 里程碑(M-1 文档就绪 / M-2 本需求可发布);详 `plan/REQ-00008/{RESULT,PLAN}.md` + 7 份过程文档 | REQ-00008 |
| 2026-06-05 16:30 | 开发状态更新 | T-001 `[修改] 增量追加 code-review/SKILL.md` 开发状态"待开始"→"已完成";完成时间 2026-06-05 16:25;完成人 wangmiao;不提交(留 dirty tree);**1 个修改文件** `plugins/code-skills/skills/code-review/SKILL.md`(425 → 519 行,+94 净增,2 处增量:锚点 A 后追加 60 行"步骤 1.5 模式选择 + 步骤 2 整版本模式 + 步骤 3 退化报告" + 锚点 B 后追加 34 行"整版本模式 — 评审范围与适用场景"附录);**0 个新增**资源;**0 偏离**(沿用详细设计 §3.2 + 严格按 PD-1~PD-4 + P-9 锚点字面精度);frontmatter(L1-3)字节级保留 + 既有"步骤 1" L106-110 字节级保留 + 既有"步骤 15" L308-313 字节级保留 + 既有 4 模板字节级保留;INV-1/4/11/12/13 全部 100% 通过;其他 9 个 `code-*` SKILL.md 字节级不变 + `marketplace.json` / `plugin.json` / `assistants/rules/` 13 文件字节级不变;新增行数 94(60-120 范围,P-2 锁定通过,未触发 R-8);详 `code/TASK-REQ-00008-00001/RESULT.md`(将由 T-003 收尾产出) | T-001 |
| 2026-06-05 16:05 | 需求新增 | REQ-00016 需求分析完成(共 6 FR / 10 NFR / 10 大类 AC / 10 边界场景 / 6 项已锁定 + 2 项采纳默认 / 6 项 v1 follow-up)。范围:**优化 2 个 `code-*` 技能** `code-design` 与 `code-plan`,增加"快模式"可选行为,与既有"完整模式"并存;快模式由环境变量 `CODE_FAST_MODE=1` 或 CLI `--fast` 标志触发(优先级 CLI > 环境变量 > 默认);快模式跳过非必要步骤(`code-design` 跳 7A-8A + 11A-12A / `code-plan` 跳 7A-8A + 12A-13A)+ 减少过程文档(快模式仅 3-4 份,完整模式 7-8 份)+ 末尾兜底提交跳过 3 选 1 确认(快模式直接 commit);完整模式字节级不变;0 修改其他 9 个 `code-*` 技能 + 0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/` / README / CLAUDE.md;用户原文 0 处笔误;Q-1 锁定 A+B(环境变量 + CLI);Q-2 锁定 A(快模式跳过 3 选 1 + 过程文档必含);Q-3 锁定 B(`code-design` 跳 7A-8A + 11A + 12A + 13A 仅核心 + 14A 仅 1 行);Q-4 锁定(`code-plan` 跳 7A + 8A + 12A + 13A + 14A/15A 仅核心 + 16A 仅 1 行 + 任务清单逐行 + 不追加里程碑);Q-5 锁定 A(快模式是新增可选行为,完整模式字节级保留);Q-6 锁定 A(`code-auto` 不自动启用) | REQ-00016 |
| 2026-06-05 16:10 | 设计新增 | REQ-00016 概要设计完成(2 个 SKILL.md 增量追加 + 0 新增 + 5 复用;4 项 DQ + 10 项 INV + 8 类风险;锚点 A "步骤 0"后 + 锚点 B "步骤 N 步骤 3"后字面精度已锁定;100% 沿用上游 6 FR + 10 NFR + 10 AC;0 触发 `dashboard-conventions §规则 1` 3 处同步 — 快模式状态字段 = 完整模式状态字段(D-3 决定);0 触发 `code-auto` SKILL.md 改动 — `code-auto` 通过环境变量启用快模式(D-5 决定);0 触发 `commit-conventions.md` 追加(占位规范,本设计**不**改);D-1~D-6 6 项讨论结论全部锁定;D-1 锁定 A("步骤 0.5"插在"步骤 0"后);D-2 锁定 A("步骤 N 步骤 3.5"插在"步骤 N 步骤 3"后);D-3 锁定 A(快模式状态字段 = 完整模式);D-4 锁定 A(快模式 RESULT.md §1 含"项目现状引用"3-5 行);D-5 锁定 A(通过环境变量);D-6 锁定 A(以本设计 D-3 为准,修订 AC-10.1/10.3);7 份过程文档已写完;`code-plan` 阶段 T-002 看板同步预计追加 1 行 + 任务清单 4 行 + 里程碑 0 个(快模式不追加里程碑);详 `design/REQ-00016/RESULT.md` + 7 份过程文档 | REQ-00016 |
| 2026-06-05 16:15 | 设计新增 | REQ-00016 详细设计与编码计划完成(共 4 个任务:2 修改 T-001 增量改 `code-design/SKILL.md` + T-002 增量改 `code-plan/SKILL.md` + 2 文档 T-003 同步看板 5 处 + T-004 13 项不变量自检;100% 沿用概要设计 4 项 DQ + 6 项 D + 10 项 INV;新增 3 项 INV-11/12/13 锚点字面精度;6 个算法伪代码(模式选择 + 快模式过滤 + RESULT.md 核心 4 章节 + PLAN.md 核心 5 章节 + 快模式末尾兜底);13/13 INV 全部满足;8/8 风险全部有缓解;4 任务测试状态全部 `不适用`(沿用 V0.0.2 既有 11 个 `code-*` 实践);0 架构任务触发(本需求 0 满足 REQ-00014 3 触发条件);2 里程碑(M-1 文档就绪 / M-2 本需求可发布);P-1~P-4 4 项讨论结论全部锁定;P-1 锁定 Read SKILL.md 全文 + Grep 自检锚点字面;P-2 锁定 A(4 任务而非 5 任务);P-3 锁定 0 架构任务;P-4 锁定 4 任务测试状态 = `不适用`);详 `plan/REQ-00016/{RESULT,PLAN}.md` + 8 份过程文档 | REQ-00016 |
| 2026-06-05 16:20 | 评审发现 | REQ-00016 整版本模式(评"详细设计"路径)完成(4 任务 / 9 维度 / **0 发现** — 0 必须改 + 0 建议改 + 0 可选,**0 派生任务**);整体结论 ✅ 通过(本轮评详细设计,等 T-001/T-002 实施后第二轮 code-review 验证 SKILL.md 字节级保留);V0.0.2 既有 11 个 `code-*` 实践:`code-review` 在 `code-plan` 之后评"详细设计";关键判断:0 触发 `dashboard-conventions §规则 1` 3 处同步(D-3 决定),0 触发 `code-auto` SKILL.md 改动(D-5 决定),0 触发 `commit-conventions.md` 追加(占位规范本设计**不**改);0 触发 `commit-conventions.md` 追加(占位规范,本设计**不**改);详 `review/REQ-00016/REVIEW-REPORT.md` + 3 份过程文档(work-log + review-checklist-applied + findings-no-task) | REQ-00016 |
| 2026-06-05 16:25 | 需求新增 | REQ-00017 需求分析完成(共 **4 FR / 6 NFR / 8 AC / 5 边界**)— `/code-plan` 拆分任务逻辑:不再为"更新看板"单独拆出派生任务(FR-1);`/code-it` 在末尾兜底提交后新增小步 P-1 自行推进本任务看板状态(开发状态:待开发→已完成,触发/来源保持=详细设计)(FR-2);`/code-plan` 拆分准则改为"一个任务 = 一个实际产出"(代码/测试/文档/数据/配置/部署脚本之一),"看板更新"不在候选集(FR-3);`/code-plan` 不再向看板追加"待开发"行(FR-4);NFR-1(0 修改其他 7 个 `code-*` 技能) + NFR-2(仅改 `/code-plan` 与 `/code-it` 2 个 SKILL.md) + NFR-4(看板 3 区段解析锚点保持) + NFR-5(任务编码双格式沿用) + NFR-6(末尾兜底 + 推进看板串行,失败不重试不阻断);看板 3 状态机:[/code-plan 完成]→ 待开发 → [/code-it 完成 + 末尾兜底成功]→ 已完成 → [/code-unit 完成(若带测试)]→ 测试状态 推进;`code-auto` 步骤 4 任务循环任务数预期减少 1(看板更新行消失),步骤 6 评审派生任务不受影响(独立);详 `require/REQ-00017/RESULT.md` + 3 份过程文档 | REQ-00017 |
| 2026-06-05 16:30 | 设计新增 | REQ-00017 概要设计完成(2 个 SKILL.md 增量追加 + 0 新增 + 0 三方依赖 + 5 复用关联设计 + 7 项 INV-1~7 + 8 项决策 D-1~8 + 6 项风险 R-1~6;100% 沿用上游 4 FR / 6 NFR / 8 AC;0 触发 `dashboard-conventions §规则 1` 3 处同步 — 沿用既有"任务完成"事件类型(**0 新增枚举值**),冲突 1 锁定不触发;0 触发 `module-conventions.md §规则 1` 修改(不涉及资源摆放);0 触发 `commit-conventions.md` 追加(占位规范,本设计**不**改);0 触发 `code-auto` SKILL.md 改动 — 0 修改其他 7 个 `code-*` 技能;0 触发 `plugin.json` / `marketplace.json` / README / CLAUDE.md 改动;0 触发 `templates/version-RESULT.md` 改动;D-1 锁定 A("一个任务 = 一个实际产出" 候选集 6 项,看板更新不在内);D-2 锁定 A(/code-it 末尾兜底后新增 P-1);D-3 锁定 A(/code-it 只动"开发状态"列,不动"测试状态");D-4 锁定 A(沿用既有"任务完成"事件);D-5 锁定 A(不重试不阻断);D-6 锁定 A(幂等);D-7 锁定 A(解析锚点复用);D-8 锁定 A(commit 失败不推进);7 份过程文档已写完;详 `design/REQ-00017/RESULT.md` + 7 份过程文档 | REQ-00017 |
| 2026-06-05 17:10 | 设计新增 | REQ-00009 概要设计完成(1 个 SKILL.md 增量追加 + 0 新增 + 0 三方依赖 + 7 复用 + 8 项决策 D-1~D-8 + 6 项风险 + 13 规范 0 冲突 0 偏离 0 授权;100% 沿用上游 7 FR / 8 NFR / ~25 AC;0 触发 `dashboard-conventions §规则 1` 3 处同步 — 沿用既有"不适用"枚举(Q-2 锁定 A),冲突 0;0 修改其他 11 个 `code-*` SKILL.md;0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/` / README;性能 < 200 ms(NFR-7 < 1 秒);8 份过程文档已写完;`code-auto` 退出码 0 兼容(NFR-6);`code-publish` / `code-dashboard` 0 冲突(NFR-4/5);详 `design/REQ-00009/RESULT.md` + 7 份过程文档 | REQ-00009 |
| 2026-06-05 17:25 | 设计新增 | REQ-00009 详细设计与编码计划完成(共 **2 个任务**:T-001 `[修改]` /code-unit/SKILL.md 增量追加锚点 A 步骤 0 前插"步骤 0a 项目可测性检查" — 5 子节齐全(检查项清单/判定逻辑/跳过流程/屏幕报告/退出码契约) + 锚点 B 既有边界 E-1 后插"E-2 守卫不通过" + 锚点 C 既有边界 E-7 后插"E-8 守卫检查项扩展预留" + T-002 `[文档]` 13 项 INV-1~13 自检 + 看板 5 处同步 + 收尾;**0**"更新看板"派生任务 — REQ-00017 强约束不拆;0 架构任务 — 本需求不满足 REQ-00014 3 触发条件;2 任务测试状态全 `不适用`;0 触发 `dashboard-conventions §规则 1` 3 处同步 — 沿用既有"任务完成"事件 + 看板 0 新增/删除/重命名 8 列;7 项 P-D1~P-D7 实施层面决策全部锁定;P-D1 `package.json` 验证伪代码 / P-D2 `pyproject.toml` 验证伪代码 / P-D3 守卫检查项执行顺序(复杂度递减)/ P-D4 屏幕输出"任务"信息来源 / P-D5 看板"测试状态"列写入路径(沿用既有)/ P-D6 E-2 编号冲突处理(由 T-001 实施时判定)/ P-D7 守卫"屏幕报告"输出时机(步骤 0a 入口);100% 沿用概要设计 8 决策 D-1~D-8 + 13 不变量 INV-1~13(本计划扩展为 13 项);8 份过程文档已写完;2 里程碑(M-1 文档就绪 / M-2 本需求可发布);P-1~P-7 7 项讨论结论全部锁定;详 `plan/REQ-00009/{RESULT,PLAN}.md` + 7 份过程文档 | REQ-00009 |
| 2026-06-05 17:30 | 任务完成 | TASK-REQ-00009-00001 `code-unit/SKILL.md` 增量追加 — 步骤 0a 守卫落地(开发状态:已完成) | TASK-REQ-00009-00001 |
| 2026-06-05 17:35 | 任务完成 | TASK-REQ-00009-00002 13 项 INV 自检 + 看板同步 + 收尾(开发状态:已完成) | TASK-REQ-00009-00002 |
| 2026-06-05 20:00 | 任务完成 | TASK-REQ-00011-00001 `code-design/SKILL.md` 增量追加 — 步骤 0b 设计目标确认 + 模板顶部预留 + 步骤 0a 小注更新(开发状态:已完成) | TASK-REQ-00011-00001 |
| 2026-06-05 20:05 | 任务完成 | TASK-REQ-00011-00002 `code-plan/SKILL.md` 增量追加 — 步骤 0b 设计目标确认 + 任务粒度调整段 + 模板顶部预留 + 步骤 0a 小注更新(开发状态:已完成) | TASK-REQ-00011-00002 |
| 2026-06-05 20:10 | 评审发现 | REQ-00011 评审完成(2 个任务 T-001 / T-002,共 4 项发现 — **0 必须改 + 2 建议改 + 2 可选**,**0 派生任务**);整体结论 ✅ 可合并;20/20 INV 100% 通过(T-001 8 项 + T-002 12 项);0 触发 `dashboard-conventions §规则 1` 3 处同步;4 项发现全部为"文档风格"层面,与功能正确性 0 关系;详 `review/REQ-00011/REVIEW-REPORT.md` + 3 份过程文档 | REQ-00011 |
| 2026-06-05 19:50 | 设计新增 | REQ-00011 概要设计完成(2 个 SKILL.md 增量追加 + 2 模板顶部预留 + 0 新增模块 + 0 三方依赖 + 0 触发 `dashboard-conventions §规则 1` 3 处同步;100% 沿用上游 9 FR / 8 NFR / ~30 AC;8 项决策 D-1~D-8 + 8 项不变量 INV-1~INV-8;Q-1~Q-8 全部沿用上游 clarifications.md 锁定;0 修改其他 8 个 `code-*` 技能;0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/` 13 文件;NFR-1 零新增依赖;NFR-3 幂等(覆盖前次内容);NFR-4 不触发 `dashboard-conventions §规则 1`;NFR-5 与 `code-auto` 协同 0 冲突(沿用"总选推荐项");NFR-6 "步骤 0b"命名沿用"步骤 0a"模式;本次为 `code-auto` 调 `code-design` 模式,步骤 0b 触发 `AskUserQuestion` 时按"总选推荐项"作答(整体=--balanced,4 维度=中),故 `code-plan` 后续任务拆分按默认粒度产出;8 份过程文档已写完;详 `design/REQ-00011/RESULT.md` + 7 份过程文档 | REQ-00011 |
| 2026-06-05 | 设计新增 | REQ-00012 概要设计完成(共 6 关键不变量 + 6 文档模块清单 + 0 API/数据/依赖 + 0 规范冲突 + 1 规范-现状偏离:§规则 2 适用范围不含根 README 但主动善意覆盖核心小节)。范围:新建仓库根 `./README.md`(中文 < 50 行)+ `./README.en.md`(英文 < 50 行,与中文版章节对仗,`doc-conventions §规则 1` 严格遵循)+ `git mv plugins/code-skills/CLAUDE.md → ./CLAUDE.md`(9,418 bytes 内容不变,原位置**不保留**,NFR-8 锁不提供重定向);复用既有 `plugins/code-skills/README.md` + `README.en.md` 作为详细技能文档(NFR-4 不破坏);Q-1/Q-2/Q-3 + 5 项采纳默认 + 1 项建议派生全部采纳 `code-require` 阶段结论;遵循 7 个过程文档(materials-index / design-notes / module-breakdown / dependencies / related-designs / rule-compliance / clarifications) | REQ-00012 |
| 2026-06-05 19:55 | 设计新增 | REQ-00011 详细设计与编码计划完成(共 **2 个任务**:T-001 `[修改]` `code-design/SKILL.md` 增量追加"步骤 0b 设计目标确认"(3 子节:1-5 问自适应 / writeDesignGoalsSection / 屏显模板)+ `design.md` 模板顶部预留"## 设计目标"占位 + §步骤 0a L107 既有"不含步骤 0b"小注更新 + T-002 `[修改]` `code-plan/SKILL.md` 增量追加"步骤 0b 设计目标确认"(沿用/退化/读 `design/.../RESULT.md`)+ §步骤 10A 末尾"按设计目标调整任务粒度"判定表段(FR-4)+ `plan.md` 模板顶部预留"## 设计目标"占位 + §步骤 0a L118 既有"不含步骤 0b"小注更新;**0**"更新看板"派生任务 — REQ-00017 强约束不拆;0 架构任务 — 本需求 `code-auto` 选 `--balanced` 不触发 FR-4 加扩展性任务;2 任务测试状态全 `不适用` 沿用 V0.0.2 既有 12 `code-*` 实践;0 触发 `dashboard-conventions §规则 1` 3 处同步;4 算法(askDesignGoals / writeDesignGoalsSection / readDesignGoalsFromDesign / adjustTaskGranularityByGoals);2 状态机(`code-design` / `code-plan` 步骤 0b);5 项本阶段决策 P-D1~P-D5 全部锁定;P-D1 步骤 0a L107/L118 小注更新 / P-D2 锚点="## 1." / P-D3 轻度合并 / P-D4 测试状态=不适用 / P-D5 commit message 沿用 V0.0.2;100% 沿用概要设计 8 决策 + 8 不变量;7 份过程文档已写完;2 里程碑(M-1 文档就绪 / M-2 本需求可发布);详 `plan/REQ-00011/{RESULT,PLAN}.md` + 7 份过程文档 | REQ-00011 |
| 2026-06-05 17:40 | 评审发现 | REQ-00009 评审完成(共 0 条发现 — 0 必须改 + 0 建议改 + 0 可选,**0 派生任务**);整体结论 ✅ 通过(无阻塞,REVIEW 完整);9 维度 100% 通过(INV-7 部分失败 13 行已在 `code/T-001/deviations.md` 显式记录 + 接受,不构成本轮"必须改");T-001 实施期自检 13/13 INV 复核 11 通过 + 1 N/A + 1 部分失败;T-002 收尾期 0 新偏离;详 `review/REQ-00009/REVIEW-REPORT.md` + 3 份过程文档 | REQ-00009 |
| 2026-06-05 16:35 | 设计新增 | REQ-00017 详细设计与编码计划完成(共 **2 个任务**:T-001 `[修改]` /code-plan/SKILL.md 增量追加锚点 A 步骤 10A 拆任务约束 + 锚点 B 步骤 16A 第 2.5 款只追加真实任务 + T-002 `[修改]` /code-it/SKILL.md 增量追加锚点 C 末尾兜底后 P-1 推进看板小步;**0**"更新看板"派生任务 — FR-1 强约束不拆;0 架构任务 — 本需求不满足 REQ-00014 3 触发条件;2 任务测试状态全 `不适用`;0 触发 `dashboard-conventions §规则 1` 3 处同步 — 沿用既有"任务完成"事件 + 看板 0 新增/删除/重命名 8 列;3 处 SKILL.md 增量追加锚点字面精度已锁定;P-1 推进看板算法伪代码 16 步 + 5 边界 + 幂等 + 串行约束;100% 沿用概要设计 8 决策 D-1~8 + 7 不变量 INV-1~7;8 份过程文档已写完;2 里程碑(M-1 文档就绪 / M-2 本需求可发布);P-1~P-4 4 项讨论结论全部锁定;P-1 锁定 Read SKILL.md 全文 + Grep 自检锚点字面;P-2 锁定 A(2 任务而非 3 任务 — FR-1 强约束);P-3 锁定 0 架构任务(本需求不满足 REQ-00014 3 触发条件);P-4 锁定 2 任务测试状态 = `不适用`;详 `plan/REQ-00017/{RESULT,PLAN}.md` + 8 份过程文档 | REQ-00017 |
| 2026-06-05 16:42 | 开发状态更新 | TASK-REQ-00017-00001 `[修改]` /code-plan/SKILL.md 增量追加 — 拆任务约束(REQ-00017 强约束,2026-06-05 起生效)+ 步骤 16A 第 2.5 款只追加真实任务 — 开发状态"待开始"→"已完成";完成时间 2026-06-05 16:42;**1 个修改文件** `plugins/code-skills/skills/code-plan/SKILL.md`(+14 净增,2 处增量:锚点 A 步骤 10A "#### 任务类型"前插"#### 拆任务约束" + 锚点 B 步骤 16A 第 3 款前插"2.5. 只追加真实任务");既有 5 段核心小节(核心原则/架构任务/生效范围/任务类型/任务编号)字节级保留;**0 偏离**;INV-1/4/6 全部 100% 通过(锚点字面精度 2/2 + 字节级保留 3/3);详 `code/TASK-REQ-00017-00001/RESULT.md` | T-001 |
| 2026-06-05 16:46 | 开发状态更新 | TASK-REQ-00017-00002 `[修改]` /code-it/SKILL.md 增量追加 — 步骤 14.5 推进看板开发状态(REQ-00017 新增,2026-06-05 起生效)显式契约 — 开发状态"待开始"→"已完成";完成时间 2026-06-05 16:46;**1 个修改文件** `plugins/code-skills/skills/code-it/SKILL.md`(+31 净增,1 处增量:锚点 C 步骤 14 后,步骤 15 前插"### 步骤 14.5 推进看板开发状态");**1 处偏离** — 实施期发现 P-1 与步骤 15 既有实现重复,调整为"显式契约"(引用步骤 15 + 引用 /code-plan 拆任务约束);INV-2/3/4/6/7 全部 100% 通过(锚点字面精度 1/1 + 字节级保留 2/2 + 0 触发 `dashboard-conventions §规则 1` 3 处同步);既有步骤 14 + 步骤 15 字节级保留;详 `code/TASK-REQ-00017-00002/{RESULT,deviations}.md` | T-002 |
| 2026-06-05 16:50 | 评审发现 | REQ-00017 评审完成(2 任务 / 9 维度 / **0 发现** — 0 必须改 + 0 建议改 + 0 可选,**0 派生任务**);整体结论 ✅ 通过(0 触发 `dashboard-conventions §规则 1` 同步,0 修改其他 7 个 `code-*` 技能,0 新增依赖,INV-1~7 全部 100% 通过);M-1 文档就绪里程碑达成(2026-06-05 16:46);M-2 本需求可发布里程碑待未来 `code-auto` 跑一个完整需求验证 P-1 推进看板;**1 处偏差**已用户授权(T-002 步骤 14.5 显式契约 vs 详细设计 §3.3 P-1 独立步骤);详 `review/REQ-00017/REVIEW-REPORT.md` + 3 份过程文档 | REQ-00017 |
| 2026-06-05 16:30 | 开发状态更新 | T-002 `[文档] 同步 V0.0.2 看板 5 处` + T-003 `[文档] 13 项不变量自检(INV-1~13) + 偏差日志 + 收尾` 状态"待开始"/"进行中"→"已完成";完成时间 2026-06-05 16:30(T-002 / T-003 同步完成);完成人 wangmiao;不提交(留 dirty tree);**3 个修改文件** `assistants/V0.0.2/RESULT.md`(L168-170 任务清单 3 行 + L46-47 里程碑 2 个 + L127 详细设计汇总 + L130 统计行 + L10 文档头 + L388 变更记录)+ `assistants/V0.0.2/code/TASK-REQ-00008-00003/RESULT.md`(新建 9 章节自检总结)+ `work-log.md`(新建 13 项不变量逐项)+ `deviations.md`(新建 0 偏离);**REQ-00008 整体收尾**:**3/3 任务完成**(T-001 SKILL.md +94 行 / T-002 看板 / T-003 自检),**2/2 里程碑完成**(M-1 文档就绪 16:25 + M-2 本需求可发布 16:30),**13/13 INV 100% 通过**(INV-1/2/3/4/5/6/7/8/9/10/11/12/13 全部 ✅),**8/8 风险有缓解**,**0 偏离 / 0 冲突 / 0 授权**;新增行数 94(60-120 范围内,P-2 锁定通过,未触发 R-8);**0 触发第二轮 code-review**(本需求 13 项 INV 字节级自检已通过,无需二次评审);详 `code/TASK-REQ-00008-00003/{RESULT,work-log,deviations}.md` | T-002 + T-003 |

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
  - REQ-00014 → [require/REQ-00014/RESULT.md](require/REQ-00014/RESULT.md)
  - REQ-00015 → [require/REQ-00015/RESULT.md](require/REQ-00015/RESULT.md)
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
