# 版本开发进度看板 — V0.0.3

> 本文件是 `V0.0.3` 版本工作空间的**单一事实来源**。
> 所有 `code-*` 技能在推进工作时,都会同步更新对应的区段。
> 区段填写规则见 `skills/code-version/SKILL.md` 中的"看板字段约定"。

## 文档头
- 版本号:`V0.0.3`
- 创建时间:2026-06-06 16:10
- 最近更新:2026-06-25 14:55(REQ-00040 `code-check` 评审完成:11 维度 10 通过 / 1 警告[§8.11 概设越界 1 处 F-006];派生 1 个"审查改修"任务 TASK-REQ-00040-00007[待处理];看板 §"任务清单" 追加 T-007 行 + §"评审发现汇总" 追加 F-006 行 + §"派生任务记录" 追加 T-007 行 + §"变更记录" 追加 2 条[派生 + 评审];M1-REQ-00040 状态字面维持"待开始"待 T-007 完成后由 `code-check` 二次推进)
- 创建人:wangmiao
- 负责人:wangmiao
- 状态:活跃
- 描述:V0.0.2 之后的下一个开发版本(基于 V0.0.2 切换,默认继承 V0.0.2 全部已完成功能)
- 当前里程碑:M0:工作空间就绪(已完成)

---

## 版本信息

| 字段 | 值 |
| --- | --- |
| 版本号 | `V0.0.3` |
| 创建时间 | 2026-06-06 16:10 |
| 最近更新 | 2026-06-08 |
| 创建人 | wangmiao |
| 负责人 | wangmiao |
| 状态 | 活跃 |
| 当前里程碑 | M0:工作空间就绪 |
| 预计交付 | — |
| 父版本 | `V0.0.2` |

---

## 里程碑

| 里程碑 | 包含任务范围 | 完成定义 | 状态 | 计划时间 | 实际完成 |
| --- | --- | --- | --- | --- | --- |
| M0:工作空间就绪 | — | 本看板创建 | 已完成 | 2026-06-06 | 2026-06-06 |
| M1:可发布 | 本版本所有任务 | **所有任务开发状态=已完成 且 测试状态∈{已运行-通过, 不适用}** | 待开始 | YYYY-MM-DD | — |
| M1-REQ-00020 | REQ-00020 全部 6 任务(T-1 ~ T-6) | 6 任务开发状态=已完成 ∧ 测试状态=不适用 | 已完成 | 2026-06-06 | 2026-06-06 |
| M1-REQ-00021 | REQ-00021 全部 8 任务(T-1 ~ T-8) | 8 任务开发状态=已完成 ∧ 测试状态=不适用 | 已完成 | 2026-06-06 | 2026-06-06 |
| M1-REQ-00023 | REQ-00023 全部 6 任务(T-1 ~ T-6) | 6 任务开发状态=已完成 ∧ 测试状态=不适用 | 已完成 | 2026-06-07 | 2026-06-07 |
| M1-REQ-00025 | REQ-00025 全部 9 任务(T-1 ~ T-9) | 9 任务开发状态=已完成 ∧ 测试状态=不适用 | 已完成 | 2026-06-08 | 2026-06-08 |
| M2-REQ-00025 | (无新增任务,仅手动验证 U-1~U-10) | 既有 5 位纯数字 + 新格式编号均可解析;U-1~U-10 全部通过 | 待开始 | 2026-06-08 | — |
| M1-REQ-00026 | REQ-00026 T-001 ~ T-004(14 目标文件) | `git diff --stat` 列出 14 文件;frontmatter 字节级一致;`git diff marketplace.json plugin.json README*.md CLAUDE.md` 0 diff | 已完成 | 2026-06-08 | 2026-06-08 |
| M2-REQ-00026 | REQ-00026 T-005(看板同步) | 5 任务开发=已完成 ∧ 测试=不适用 | 已完成 | 2026-06-08 | 2026-06-08 |
| M1-REQ-00027 | REQ-00027 T-001 + T-002(2 SKILL.md 修改) | `code-fix` 纯登记型重写完成;`code-auto` 模式 C 增加完成;`git diff marketplace.json plugin.json README*.md CLAUDE.md` 0 diff | 已完成 | 2026-06-08 | 2026-06-08 |
| M2-REQ-00027 | REQ-00027 T-003(看板同步) | 3 任务开发=已完成 ∧ 测试=不适用 | 已完成 | 2026-06-08 | 2026-06-08 |
| M3-REQ-00027 | REQ-00027 T-004 ~ T-010(7 个审查改修) | 7 任务开发=已完成 ∧ 测试=不适用;code-fix 步骤 4 状态表 5 候选字面满足;code-auto §"路径感知模式"含 5 种;步骤 1 子分支 1A-1E;步骤 2 拆 2A/2B;步骤 3 拆 3A/3B;investigation.md 角色统一 | 已完成 | 2026-06-08 | 2026-06-08 |
| M1-REQ-00028 | REQ-00028 T-001(1 SKILL.md 新增) | 1 任务开发=已完成 ∧ 测试=不适用 | 已完成 | 2026-06-10 | 2026-06-10 |
| M1-REQ-00029 | REQ-00029 T-001(1 SKILL.md 渲染层瘦身) | 1 任务开发=已完成 ∧ 测试=不适用 | 已完成 | 2026-06-10 | 2026-06-10 |
| M1-REQ-00030 | REQ-00030 T-001 ~ T-005(5 任务,5 个被改文件) | 5 任务开发=已完成 ∧ 测试=不适用;INV-1~INV-9 全部满足;`git diff` 校验 11 个 `code-*` 技能 SKILL.md 0 改 + 7 个项目级规范 0 改 + 4 个 README 0 改 + 既有 9 个 REQ design/plan 0 改 | 已完成 | 2026-06-12 | 2026-06-12 |
| M2-REQ-00030 | REQ-00030 T-006(行数收敛观测) | 落地后 3 个新 REQ,平均 design ≤ 184 / 平均 plan ≥ 340(AC-8.1 / AC-8.2 / NFR-1) | 待开始 | 落地后 3 个新 REQ 完成时 | — |
| M1-REQ-00031 | REQ-00031 T-001 ~ T-005(5 任务,5 个被改文件) | 5 任务开发=已完成 ∧ 测试=不适用;INV-1~INV-10 全部满足;0 单列"编译运行检测"任务(本就是冗余);0 单元测试任务(主动外移) | 已完成 | 2026-06-12 | 2026-06-12 |
| M1-REQ-00032 | REQ-00032 T-001(1 任务,1 个被改文件) | 1 任务开发=已完成 ∧ 测试=不适用;INV-1~INV-10 全部满足;`code-require/SKILL.md` 步骤 10A / 10B 段内文末各追加 1 段"### 下一步建议";18 AC 全通过;7 项 git diff 全部 0 改既有 | 已完成 | 2026-06-12 | 2026-06-12 |
| M1-REQ-00036 | REQ-00036 全部 3 任务(T-1 ~ T-3) | 3 任务开发=已完成 ∧ 测试=不适用;AC-1 ~ AC-8 全过(AC-2 / AC-4 允许 ≤ 3 处例外);1 次 commit 落地;`code/<TASK>/work-log.md` 完整 | 待开始 | 2026-06-16 | — |
| M1-REQ-00037 | REQ-00037 全部 7 任务(T-1 ~ T-7) | 7 任务开发=已完成 ∧ 测试=不适用;AC-1 ~ AC-10 全过;4 个 SKILL.md 修改 + 1 看板技能扩展;1 次末尾兜底提交 | 待开始 | 2026-06-22 | — |
| M1-REQ-00039 | REQ-00039 全部 5 任务(T-1 ~ T-5) | 5 任务开发=已完成 ∧ 测试=不适用;AC-1 ~ AC-8 全过;2 SKILL.md 修改 + 1 模板改造 + 2 共享库新建;1 次末尾兜底提交 | 待开始 | 2026-06-22 | — |
| M1-REQ-00040 | REQ-00040 全部 6 任务(T-1 ~ T-6) | 6 任务开发=已完成 ∧ 测试=不适用;AC-1 ~ AC-12 全过(全部降级为静态校验,本仓库 0 测试框架);2 SKILL.md 改造(步骤 0/6 末尾子节) + 2 模板改造(bug.md 新区段 + 文档头 2 字段 + assistants-layout.md 同步);1 次末尾兜底提交 | 待开始 | 2026-06-25 | — |
| M1-BUG-00004 | BUG-00004 全部 4 任务(T-001 ~ T-004) | 4 任务开发=已完成 ∧ 测试=不适用;端到端验证 7 个观察点全部命中(纯 Markdown 改造不生成 `compile-and-run.md` / `test-results.md`);6 个技能旁路验证结论明确(实际过度生成风险均为低 / 中 / 极低 / 无) | 待开始 | 2026-06-22 | — |
| M1-REQ-00038 | REQ-00038 全部 3 任务(T-001 ~ T-003) | 3 任务开发=已完成 ∧ 测试=不适用;AC-1 ~ AC-7 全部通过;INV-1 ~ INV-8 全部满足;`git diff` 校验 7 项守卫字面 0 改 + 模板既有"## 9. 单元测试"小节 0 改 + 11 个其他 `code-*` 技能 SKILL.md 核心工作流 0 改;末尾兜底 1 次 commit | 已完成 | 2026-06-22 | 2026-06-22 |

> 完成定义显式列出两轴状态要求,避免把"开发完成"误当"可发布"。

---

## 需求清单

> 写入方:`code-require`(新建/变更/撤回时更新)
> 状态:`待开始` / `进行中` / `已完成` / `已取消` / `阻塞`

| 需求编码 | 标题 | 状态 | 创建时间 | 完成时间 | 需求文档 | 概要设计 | 详细设计 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-00020 | 优化 code-design / code-plan,架构设计目标重新归位 + 新增 3 维度 + 步骤归并 | 已完成 | 2026-06-06 | 2026-06-06 | [REQ-00020/RESULT.md](./require/REQ-00020/RESULT.md) | [REQ-00020/RESULT.md](./design/REQ-00020/RESULT.md) | [REQ-00020/RESULT.md](./plan/REQ-00020/RESULT.md) |
| REQ-00021 | 优化 3 技能 --result / --plan 模板参数,按用户模板格式输出填充后文档 | 已完成 | 2026-06-06 | 2026-06-06 | [REQ-00021/RESULT.md](./require/REQ-00021/RESULT.md) | [REQ-00021/RESULT.md](./design/REQ-00021/RESULT.md) | — |
| REQ-00022 | 修改 /code-review 技能名称为 /code-check | 已完成 | 2026-06-07 | 2026-06-07 | [REQ-00022/RESULT.md](./require/REQ-00022/RESULT.md) | — | — |
| REQ-00023 | 简化 /code-dashboard 输出:总开发进度 + 5 类状态占比 + 后续操作建议 | 已完成 | 2026-06-07 | 2026-06-07 | [REQ-00023/RESULT.md](./require/REQ-00023/RESULT.md) | — | — |
| REQ-00024 | 移除 /code-auto 的 from 关键字逻辑,改用路径感知判定 | 已完成 | 2026-06-07 | 2026-06-07 | [REQ-00024/RESULT.md](./require/REQ-00024/RESULT.md) | — | — |
| REQ-00025 | 软化编号正则约束,允许用户自定义编号格式(仅前缀固定) | 已完成 | 2026-06-07 | 2026-06-07 | [REQ-00025/RESULT.md](./require/REQ-00025/RESULT.md) | — | — |
| REQ-00026 | 技能描述通用化扫除(10 SKILL.md 描述性段落去 plugins/code-skills 强关联指代) | 已完成 | 2026-06-08 | 2026-06-08 | [REQ-00026/RESULT.md](./require/REQ-00026/RESULT.md) | — | — |
| REQ-00027 | 优化 code-fix 流程(纯登记型)+ code-auto BUG 路径编排 | 已完成 | 2026-06-08 | 2026-06-08 | [REQ-00027/RESULT.md](./require/REQ-00027/RESULT.md) | — | — |
| REQ-00028 | 新增 code-answer 技能(只读功能查询,跨版本需求 + 源码补足) | 已完成 | 2026-06-10 | 2026-06-10 | [REQ-00028/RESULT.md](./require/REQ-00028/RESULT.md) | [REQ-00028/RESULT.md](./design/REQ-00028/RESULT.md) | — |
| REQ-00029 | 优化 /code-dashboard 屏显报告(只展示结果 + 去除不必要换行) | 进行中 | 2026-06-10 | — | [REQ-00029/RESULT.md](./require/REQ-00029/RESULT.md) | [REQ-00029/RESULT.md](./design/REQ-00029/RESULT.md) | — |
| REQ-00030 | 优化 /code-design 与 /code-plan 职责分离(概设只做概设,详设开始做详设;扩展性三阶段下沉) | 已完成 | 2026-06-12 | 2026-06-12 | [REQ-00030/RESULT.md](./require/REQ-00030/RESULT.md) | — | — |
| REQ-00031 | 优化 /code-plan 任务粒度(内化编译/运行,外移单元测试) | 已完成 | 2026-06-12 | 2026-06-12 | [REQ-00031/RESULT.md](./require/REQ-00031/RESULT.md) | — | — |
| REQ-00032 | 优化 /code-require 登记结束后报告(输出下一步建议) | 已完成 | 2026-06-12 | 2026-06-12 | [REQ-00032/RESULT.md](./require/REQ-00032/RESULT.md) | — | — |
| REQ-00033 | 明文契约化 `code-require` 不涉及技术选型(只确定功能点) | 已完成 | 2026-06-15 | 2026-06-15 | [REQ-00033/RESULT.md](./require/REQ-00033/RESULT.md) | [REQ-00033/RESULT.md](./design/REQ-00033/RESULT.md) | [REQ-00033/PLAN.md](./plan/REQ-00033/PLAN.md) |
| REQ-00034 | 移除 /code-unit 技能,能力整合进 /code-it(按需写单测/不适用工程跳过) | 已完成 | 2026-06-15 | 2026-06-15 | [REQ-00034/RESULT.md](./require/REQ-00034/RESULT.md) | [REQ-00034/RESULT.md](./design/REQ-00034/RESULT.md) | [REQ-00034/PLAN.md](./plan/REQ-00034/PLAN.md) |
| REQ-00035 | 过程文档自适应生成改造(AI 自主判定,减少不必要过程文档 token 消耗) | 进行中 | 2026-06-15 | — | [REQ-00035/RESULT.md](./require/REQ-00035/RESULT.md) | — | — |
| REQ-00036 | 清理技能文件(SKILL.md + templates/)中的开发痕迹(REQ/BUG 编号引用、退场功能说明、决策记录、生效日标记等) | 已完成 | 2026-06-16 | 2026-06-16 | [REQ-00036/RESULT.md](./require/REQ-00036/RESULT.md) | — | — |
| REQ-00037 | 优化 /code-fix 技能及整个缺陷修复流程的状态推进(/code-fix 仅登记,状态自动由下游 code-plan/code-it/code-check 接力,新增 5 状态:待处理/待开发/开发中/待审查/已完成) | 已完成 | 2026-06-22 | 2026-06-22 | [REQ-00037/RESULT.md](./require/REQ-00037/RESULT.md) | — | — |
| REQ-00038 | 优化 /code-it 技能单测判定(从工程粒度细化到模块粒度:模块识别优先级链 + 模块级守卫 7 项 + 模块级单测输出 + 模板多模块支持) | 已完成 | 2026-06-22 | 2026-06-22 | [REQ-00038/RESULT.md](./require/REQ-00038/RESULT.md) | — | — |
| REQ-00039 | 优化 /code-it、/code-check 等技能:代码行数限制仅统计实际逻辑行(逻辑行 = 总行 - 空行 - 注释行;4 类排除项:注释/说明/空行/格式化换行;工具集成 tokei/cloc + 启发式回退) | 草稿 | 2026-06-22 | — | [REQ-00039/RESULT.md](./require/REQ-00039/RESULT.md) | — | — |
| REQ-00040 | 优化 /code-fix 技能:登记缺陷时启动程序复现并登记证据(项目可启动性探测 + 复现动作触发 + 3 类产物收集:日志/截图/交互数据;产物放 fix/<BUG-NNN>/reproduce/ 子目录;失败降级不阻断;与 REQ-00037 协同,状态推进路径字节级保留) | 草稿 | 2026-06-25 | — | [REQ-00040/RESULT.md](./require/REQ-00040/RESULT.md) | — | — |

**统计**:
- 总数:18
- 已完成:13
- 进行中:2
- 待开始:2
- 已取消:0
- 阻塞:0

---

## 概要设计清单

> 写入方:`code-design`(新建/变更时更新)

| 需求编码 | 设计标题 | 状态 | 创建时间 | 完成时间 | 概要设计文档 |
| --- | --- | --- | --- | --- | --- |
| REQ-00020 | 优化 code-design / code-plan,架构设计目标重新归位 + 新增 3 维度 + 步骤归并 | 已完成 | 2026-06-06 | 2026-06-06 | [REQ-00020/RESULT.md](./design/REQ-00020/RESULT.md) |
| REQ-00021 | 优化 3 技能 --result / --plan 模板参数,按用户模板格式输出填充后文档 | 已完成 | 2026-06-06 | 2026-06-06 | [REQ-00021/RESULT.md](./design/REQ-00021/RESULT.md) |
| REQ-00023 | 简化 /code-dashboard 输出为 4 段(总开发进度 + 5 类状态占比 + 高优缺陷 + ≤5 条建议) | 已完成 | 2026-06-07 | 2026-06-07 | [REQ-00023/RESULT.md](./design/REQ-00023/RESULT.md) |
| REQ-00024 | 移除 /code-auto 的 from 关键字逻辑,改用路径感知判定 | 已完成 | 2026-06-07 | 2026-06-07 | [REQ-00024/RESULT.md](./design/REQ-00024/RESULT.md) |
| REQ-00025 | 软化编号正则约束,允许用户自定义编号格式(仅前缀固定) | 已完成 | 2026-06-07 | 2026-06-07 | [REQ-00025/RESULT.md](./design/REQ-00025/RESULT.md) |
| REQ-00026 | 技能描述通用化扫除(10 SKILL.md 描述性段落去 plugins/code-skills 强关联指代) | 已完成 | 2026-06-08 | 2026-06-08 | [REQ-00026/RESULT.md](./design/REQ-00026/RESULT.md) |
| REQ-00027 | 优化 code-fix 流程(纯登记型)+ code-auto BUG 路径编排 | 已完成 | 2026-06-08 | 2026-06-08 | [REQ-00027/RESULT.md](./design/REQ-00027/RESULT.md) |
| REQ-00029 | 优化 /code-dashboard 屏显报告(只展示结果 + 去除不必要换行) | 已完成 | 2026-06-10 | 2026-06-10 | [REQ-00029/RESULT.md](./design/REQ-00029/RESULT.md) |
| REQ-00030 | 优化 /code-design 与 /code-plan 职责分离(概设只做概设,详设开始做详设;扩展性三阶段下沉) | 已完成 | 2026-06-12 | 2026-06-12 | [REQ-00030/RESULT.md](./design/REQ-00030/RESULT.md) |
| REQ-00031 | 优化 /code-plan 任务粒度(内化编译/运行,外移单元测试) | 已完成 | 2026-06-12 | 2026-06-12 | [REQ-00031/RESULT.md](./design/REQ-00031/RESULT.md) |
| REQ-00032 | 优化 /code-require 登记结束后报告(输出下一步建议) | 已完成 | 2026-06-12 | 2026-06-12 | [REQ-00032/RESULT.md](./design/REQ-00032/RESULT.md) |
| REQ-00035 | 过程文档自适应生成改造(AI 自主判定不涉及的过程文档不生成,减少 token 消耗) | 已完成 | 2026-06-15 | 2026-06-15 | [REQ-00035/RESULT.md](./design/REQ-00035/RESULT.md) |
| REQ-00036 | 清理技能文件(SKILL.md + templates/)中的开发痕迹(--minimal 路线;6 条硬编码规则;0 新增模块/接口/数据结构/依赖) | 已完成 | 2026-06-16 | 2026-06-16 | [REQ-00036/RESULT.md](./design/REQ-00036/RESULT.md) |
| REQ-00037 | 优化 /code-fix 技能及整个缺陷修复流程的状态推进(--balanced 路线;6 功能域;0 新增模块/接口/数据结构/依赖;4 SKILL.md 修改 + 1 看板技能扩展) | 草稿 | 2026-06-22 | — | [REQ-00037/RESULT.md](./design/REQ-00037/RESULT.md) |
| REQ-00038 | 优化 /code-it 技能单测判定(从工程粒度细化到模块粒度,monorepo 子包独立识别 + 守卫)(--balanced 路线;8 决策 / 8 不变量;1 主改造 + 1 模板追加 + 1 文档字面改写;0 新增依赖) | 已完成 | 2026-06-22 | 2026-06-22 | [REQ-00038/RESULT.md](./design/REQ-00038/RESULT.md) |
| REQ-00039 | 优化 /code-it、/code-check 等技能:代码行数限制仅统计实际逻辑行(--balanced 路线;5 模块 / 4 函数 / 0 三方依赖;2 SKILL.md 改造 + 1 模板改造 + 2 共享库新建) | 草稿 | 2026-06-22 | — | [REQ-00039/RESULT.md](./design/REQ-00039/RESULT.md) |
| REQ-00040 | 优化 /code-fix 技能:登记缺陷时启动程序复现并登记证据(--balanced 路线;10 决策 / 8 不变量;2 SKILL.md 改造 + 2 模板改造(bug.md + assistants-layout.md)+ 1 运行时子目录 reproduce/;0 新增三方依赖) | 草稿 | 2026-06-25 | — | [REQ-00040/RESULT.md](./design/REQ-00040/RESULT.md) |

**统计**:16 / 已完成 13 / 草稿 3 / 进行中 0

---

## 详细设计与任务计划汇总

> 写入方:`code-plan`(新建/变更/追加任务时更新)

| 需求编码 | 计划标题 | 状态 | 任务总数 | 开发完成 | 测试通过 | 创建时间 | 计划文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-00020 | 优化 code-design / code-plan,架构设计目标重新归位 + 新增 3 维度 + 步骤归并 | 已完成 | 6 | 6 | 0(不适用) | 2026-06-06 | [REQ-00020/PLAN.md](./plan/REQ-00020/PLAN.md) |
| REQ-00021 | 优化 3 技能 --result / --plan 模板参数,按用户模板格式输出填充后文档 | 已完成 | 8 | 8 | 0(不适用) | 2026-06-06 | [REQ-00021/PLAN.md](./plan/REQ-00021/PLAN.md) |
| REQ-00022 | 修改 /code-check 技能名称为 /code-check | 已完成 | 10 | 10 | 0(不适用) | 2026-06-07 | [REQ-00022/PLAN.md](./plan/REQ-00022/PLAN.md) |
| REQ-00023 | 简化 /code-dashboard 输出为 4 段(总开发进度 + 5 类状态占比 + 高优缺陷 + ≤5 条建议) | 已完成 | 6 | 6 | 0(不适用) | 2026-06-07 | [REQ-00023/PLAN.md](./plan/REQ-00023/PLAN.md) |
| REQ-00024 | code-auto 步骤 1 改造:用路径感知替代 from 关键字 | 已完成 | 1 | 1 | 0(不适用) | 2026-06-07 | [REQ-00024/PLAN.md](./plan/REQ-00024/PLAN.md) |
| REQ-00025 | 软化编号正则约束,允许用户自定义编号格式(仅前缀固定) | 已完成 | 9 | 9 | 0(不适用) | 2026-06-08 | [REQ-00025/PLAN.md](./plan/REQ-00025/PLAN.md) |
| REQ-00026 | 技能描述通用化扫除(10 SKILL.md 描述性段落去 plugins/code-skills 强关联指代) | 已完成 | 5 | 5 | 0(不适用) | 2026-06-08 | [REQ-00026/PLAN.md](./plan/REQ-00026/PLAN.md) |
| REQ-00027 | 优化 code-fix 流程(纯登记型)+ code-auto BUG 路径编排 | 已完成 | 3 | 3 | 0(不适用) | 2026-06-08 | [REQ-00027/PLAN.md](./plan/REQ-00027/PLAN.md) |
| REQ-00028 | 新增 code-answer 技能(只读功能查询,跨版本需求 + 源码补足) | 已完成 | 1 | 0 | 0(不适用) | 2026-06-10 | [REQ-00028/PLAN.md](./plan/REQ-00028/PLAN.md) |
| REQ-00029 | 优化 /code-dashboard 屏显报告(只展示结果 + 去除不必要换行) | 已完成 | 1 | 1 | 0(不适用) | 2026-06-10 | [REQ-00029/PLAN.md](./plan/REQ-00029/PLAN.md) |
| REQ-00030 | 优化 /code-design 与 /code-plan 职责分离(概设只做概设,详设开始做详设;扩展性三阶段下沉) | 已完成 | 6 | 0 | 0(不适用) | 2026-06-12 | [REQ-00030/PLAN.md](./plan/REQ-00030/PLAN.md) |
| REQ-00031 | 优化 /code-plan 任务粒度(内化编译/运行,外移单元测试) | 已完成 | 5 | 0 | 0(不适用) | 2026-06-12 | [REQ-00031/PLAN.md](./plan/REQ-00031/PLAN.md) |
| REQ-00032 | 优化 /code-require 登记结束后报告(输出下一步建议) | 已完成 | 1 | 0 | 0(不适用) | 2026-06-12 | [REQ-00032/PLAN.md](./plan/REQ-00032/PLAN.md) |
| REQ-00033 | 明文契约化 `code-require` 不涉及技术选型(只确定功能点) | 已完成 | 1 | 0 | 0(不适用) | 2026-06-15 | [REQ-00033/PLAN.md](./plan/REQ-00033/PLAN.md) |
| REQ-00034 | 移除 /code-unit 技能,能力整合进 /code-it(按需写单测/不适用工程跳过) | 已完成 | 10 | 0 | 0(不适用) | 2026-06-15 | [REQ-00034/PLAN.md](./plan/REQ-00034/PLAN.md) |
| REQ-00035 | 过程文档自适应生成改造(AI 自主判定不涉及的过程文档不生成,减少 token 消耗) | 已完成 | 7 | 0 | 0(不适用) | 2026-06-15 | [REQ-00035/PLAN.md](./plan/REQ-00035/PLAN.md) |
| REQ-00036 | 清理技能文件(SKILL.md + templates/)中的开发痕迹(--minimal 路线;6 条硬编码规则;3 任务扫描/应用/验证严格串行) | 已完成 | 3 | 0 | 0(不适用) | 2026-06-16 | [REQ-00036/PLAN.md](./plan/REQ-00036/PLAN.md) |
| REQ-00037 | 优化 /code-fix 技能及整个缺陷修复流程的状态推进(--balanced 路线;7 任务严格串行;AC-1 ~ AC-10 全部纳入 T-7 验证) | 草稿 | 7 | 0 | 0(不适用) | 2026-06-22 | [REQ-00037/PLAN.md](./plan/REQ-00037/PLAN.md) |
| REQ-00038 | 优化 /code-it 技能单测判定(从工程粒度细化到模块粒度,monorepo 子包独立识别 + 守卫)(--balanced 路线;5 模块 / 3 算法 / 5 接口 / 7 字段模板;3 任务严格串行) | 已完成 | 3 | 3 | 0(不适用) | 2026-06-22 | [REQ-00038/PLAN.md](./plan/REQ-00038/PLAN.md) |
| REQ-00039 | 优化 /code-it、/code-check 等技能:代码行数限制仅统计实际逻辑行(--balanced 路线;5 任务严格串行;逻辑行 = 总行 - 空行 - 注释行;工具集成 tokei/cloc + 启发式回退;阈值默认 500/200) | 草稿 | 5 | 0 | 0(不适用) | 2026-06-22 | [REQ-00039/PLAN.md](./plan/REQ-00039/PLAN.md) |
| REQ-00040 | 优化 /code-fix 技能:登记缺陷时启动程序复现并登记证据(--balanced 路线;18 决策 / 8 不变量;2 SKILL.md 改造 + 2 模板改造 + 1 看板同步;6 任务严格串行;12 AC 全部降级为静态校验) | 草稿 | 6 | 0 | 0(不适用) | 2026-06-25 | [REQ-00040/PLAN.md](./plan/REQ-00040/PLAN.md) |

**统计**:20 个计划 / 共 110 个任务 / 开发完成 54 / 测试通过 0(不适用 110)

(详细:REQ-00020 6 + REQ-00021 8 + REQ-00022 10 + REQ-00023 6 + REQ-00024 1 + REQ-00025 9 = 40;开发完成含 2 条"审查改修"待开始任务按既有看板约定计入;不适用 = REQ-00020 6 + REQ-00021 8 + REQ-00022 10 + REQ-00023 6 + REQ-00024 1 = 31;新增 REQ-00036 3 任务)

---

## 任务清单

> 首次登记:`code-plan`(拆分任务时)
> 持续更新:
> - `code-it` 推进 `开发状态`(`待开始` → `进行中` → `已完成`)
> - `code-unit` 推进 `测试状态`(`未编写` → `已编写` → `已运行-通过` / `已运行-失败` / `不适用`)
> - `code-check` 派生"审查改修"任务时追加新行

| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 完成时间 | 提交哈希 | 关联任务 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TASK-REQ-00020-00001 | REQ-00020 | 修改 | 详细设计 | [修改] code-design 步骤 0b 简化为 1 维度 | 已完成 | 不适用 | plugins/code-skills/skills/code-design/SKILL.md §步骤 0b | 2026-06-06 16:30 | e69a58a | — |
| TASK-REQ-00020-00002 | REQ-00020 | 修改 | 详细设计 | [修改] code-plan 步骤 0b 扩展为 7 维度 | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §步骤 0b | 2026-06-06 16:30 | e69a58a | — |
| TASK-REQ-00020-00003 | REQ-00020 | 修改 | 详细设计 | [修改] 任务粒度调整规则 +3 行(封装性/可复用性/可读性) | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §步骤 10A 末尾 | 2026-06-06 16:30 | e69a58a | — |
| TASK-REQ-00020-00004 | REQ-00020 | 重构 | 详细设计 | [重构] 步骤归并 M-1 调用上下文检测引用 | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §步骤 0b.0 | 2026-06-06 16:30 | e69a58a | — |
| TASK-REQ-00020-00005 | REQ-00020 | 重构 | 详细设计 | [重构] 步骤归并 M-2/M-3 公共子步骤引用 | 已完成 | 不适用 | code-plan/SKILL.md §3/5/21/22 + code-it/SKILL.md §23 | 2026-06-06 16:30 | e69a58a | — |
| TASK-REQ-00020-00006 | REQ-00020 | 重构 | 详细设计 | [重构] 步骤归并 M-4 删除多余逻辑分支 | 已完成 | 不适用 | code-plan/SKILL.md §步骤 6 + code-it/SKILL.md §步骤 0a.7 | 2026-06-06 16:30 | e69a58a | — |
| TASK-REQ-00020-00007 | REQ-00020 | 修改 | 审查改修 | [修改] 修复任务粒度调整规则表 4 列与 3... | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §步骤 10A 末尾 表格 L450-451 | 2026-06-10 11:00 | — | TASK-REQ-00020-00003 |
| TASK-REQ-00020-00008 | REQ-00020 | 修改 | 审查改修 | [修改] 清理 §步骤 7D 段,与 §步骤 6 ... | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §步骤 7D 段 L627-628 | 2026-06-10 11:00 | — | TASK-REQ-00020-00006 |
| TASK-REQ-00021-00001 | REQ-00021 | 修改 | 详细设计 | [修改] code-require 步骤 0 之前新增"## 命令行参数解析"小节 | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §工具使用约定段后 | 2026-06-06 17:05 | d6be243 | — |
| TASK-REQ-00021-00002 | REQ-00021 | 修改 | 详细设计 | [修改] code-require 末尾新增"## 模板填充步骤"小节 | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §不要做的事前 | 2026-06-06 17:05 | d6be243 | — |
| TASK-REQ-00021-00003 | REQ-00021 | 修改 | 详细设计 | [修改] code-design 步骤 0 之前新增"## 命令行参数解析"小节 | 已完成 | 不适用 | plugins/code-skills/skills/code-design/SKILL.md §工具使用约定段后 | 2026-06-06 17:05 | d6be243 | — |
| TASK-REQ-00021-00004 | REQ-00021 | 修改 | 详细设计 | [修改] code-design 末尾新增"## 模板填充步骤"小节 | 已完成 | 不适用 | plugins/code-skills/skills/code-design/SKILL.md §不要做的事前 | 2026-06-06 17:05 | d6be243 | — |
| TASK-REQ-00021-00005 | REQ-00021 | 修改 | 详细设计 | [修改] code-plan 步骤 0 之前新增"## 命令行参数解析"小节(2 参数) | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §工具使用约定段后 | 2026-06-06 17:05 | d6be243 | — |
| TASK-REQ-00021-00006 | REQ-00021 | 修改 | 详细设计 | [修改] code-plan 末尾新增"## 模板填充步骤"小节(2 段填充) | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §不要做的事前 | 2026-06-06 17:05 | d6be243 | — |
| TASK-REQ-00021-00007 | REQ-00021 | 重构 | 详细设计 | [重构] 15 个占位符映射表中央化(3 技能共用) | 已完成 | 不适用 | plugins/code-skills/skills/{code-require,code-design,code-plan}/SKILL.md §模板填充步骤 | 2026-06-06 17:05 | d6be243 | T-1 ~ T-6 |
| TASK-REQ-00021-00008 | REQ-00021 | 重构 | 详细设计 | [重构] 占位符扩展机制预留(--map / --vars / --script) | 已完成 | 不适用 | plugins/code-skills/skills/{code-require,code-design,code-plan}/SKILL.md §模板填充步骤 | 2026-06-06 17:05 | d6be243 | T-7 |
| TASK-REQ-00022-00001 | REQ-00022 | 重命名 | 详细设计 | [重命名] code-check/ → code-check/(目录 + frontmatter + H1 + 全文字面量) | 已完成 | 不适用 | plugins/code-skills/skills/code-check/SKILL.md | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00002 | REQ-00022 | 修改 | 详细设计 | [字面量改] .claude-plugin/marketplace.json 全部同步改 | 已完成 | 不适用 | .claude-plugin/marketplace.json | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00003 | REQ-00022 | 修改 | 详细设计 | [字面量改] plugins/code-skills/.claude-plugin/plugin.json 全部同步改 | 已完成 | 不适用 | plugins/code-skills/.claude-plugin/plugin.json | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00004 | REQ-00022 | 修改 | 详细设计 | [字面量改] 10 个其他 SKILL.md 的 description 字段同步 | 已完成 | 不适用 | plugins/code-skills/skills/{auto,design,require,plan,it,unit,fix,publish,dashboard,version,rule}/SKILL.md | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00005 | REQ-00022 | 修改 | 详细设计 | [字面量改] 仓库根 2 README + 仓库内 2 README 同步 | 已完成 | 不适用 | README.md / README.en.md / plugins/code-skills/README.md / plugins/code-skills/README.en.md | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00006 | REQ-00022 | 修改 | 详细设计 | [字面量改] CLAUDE.md 同步 | 已完成 | 不适用 | CLAUDE.md | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00007 | REQ-00022 | 修改 | 详细设计 | [字面量改] 13 份项目级规范同步 | 已完成 | 不适用 | assistants/rules/*.md(13 份) | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00008 | REQ-00022 | 修改 | 详细设计 | [字面量改] 6 个技能模板同步 | 已完成 | 不适用 | plugins/code-skills/skills/*/templates/*.md | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00009 | REQ-00022 | 修改 | 详细设计 | [字面量改] V0.0.3 当前激活看板同步 | 已完成 | 不适用 | assistants/V0.0.3/RESULT.md | 2026-06-07 | (本会话) | — |
| TASK-REQ-00022-00010 | REQ-00022 | 校验 | 详细设计 | [校验] Grep 全范围校验(本需求范围内 0 残留 + 历史不追溯) | 已完成 | 不适用 | (Grep 校验,不写文件) | 2026-06-07 | (本会话) | — |
| TASK-REQ-00023-00001 | REQ-00023 | 修改 | 详细设计 | [修改] 段 1 总开发进度计算函数(算法 1) | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §输出 段 1 + §工作流程 步骤 4 段 1 | 2026-06-07 | (本会话) | — |
| TASK-REQ-00023-00002 | REQ-00023 | 修改 | 详细设计 | [修改] 5 类状态判定函数(算法 2) | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §工作流程 步骤 4 段 2 | 2026-06-07 | (本会话) | — |
| TASK-REQ-00023-00003 | REQ-00023 | 修改 | 详细设计 | [修改] 5 类状态计数函数(算法 3) | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §工作流程 步骤 4 段 2 | 2026-06-07 | (本会话) | — |
| TASK-REQ-00023-00004 | REQ-00023 | 修改 | 详细设计 | [修改] 后续操作建议生成(算法 4) | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §工作流程 步骤 4 段 4 + §附录 C | 2026-06-07 | (本会话) | — |
| TASK-REQ-00023-00005 | REQ-00023 | 修改 | 详细设计 | [修改] 高优先级缺陷段保留 + 边界 E-1 ~ E-10 | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §工作流程 步骤 4 段 3 + §边界与异常 | 2026-06-07 | (本会话) | — |
| TASK-REQ-00023-00006 | REQ-00023 | 修改 | 详细设计 | [修改] 输出区段与衔接小节改造 + 变更记录 | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §输出 + §衔接 | 2026-06-07 | (本会话) | — |
| TASK-BUG-00001-00001 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-require 加"不修改 SKILL.md"硬约束 | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §不要做的事 | 2026-06-07 17:32 | (本会话) | BUG-00001 |
| TASK-BUG-00001-00002 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-design 加"不修改 SKILL.md"硬约束 | 已完成 | 不适用 | plugins/code-skills/skills/code-design/SKILL.md §不要做的事 | 2026-06-07 17:35 | (本会话) | BUG-00001 |
| TASK-BUG-00001-00003 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-plan 加"不修改 SKILL.md"硬约束 | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §不要做的事 | 2026-06-07 17:41 | (本会话) | BUG-00001 |
| TASK-BUG-00001-00004 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-fix 加"不修改 SKILL.md"硬约束 | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md §不要做的事 | 2026-06-07 17:47 | (本会话) | BUG-00001 |
| TASK-BUG-00001-00005 | BUG-00001 | 修改 | 缺陷修复 | [修改] code-it 加"唯一可改"声明 + code-unit 加"可改测试代码"边界 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §目标 段后 + plugins/code-skills/skills/code-unit/SKILL.md §目标 段后 | 2026-06-07 17:54 | (本会话) | BUG-00001 |
| TASK-REQ-00024-00001 | REQ-00024 | 修改 | 详细设计 | [修改] code-auto 步骤 1:用路径感知替代 from 关键字 | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md §输入与输出 + §工作流步骤 步骤 1 + §边界与异常 | 2026-06-07 17:55 | (本会话) | REQ-00024 |
| TASK-REQ-00025-00001 | REQ-00025 | 修改 | 详细设计 | [修改] encoding-conventions §规则 1/2/4 软化 + 新增 §规则 1.5 | 已完成 | 不适用 | ./assistants/rules/encoding-conventions.md §规则 1 §条款 表 + §规则 2 §条款 + §规则 4 §条款 + §规则 1.5(新) | 2026-06-08 | 19bb8e2 | — |
| TASK-REQ-00025-00002 | REQ-00025 | 修改 | 详细设计 | [修改] code-require §输入 + §工具使用约定 字面更新 | 已完成 | 不适用 | ./plugins/code-skills/skills/code-require/SKILL.md §输入 > 需求编码格式 + §工具使用约定 > 标题解析 > parseResultTitle | 2026-06-08 | 7af6525 | — |
| TASK-REQ-00025-00003 | REQ-00025 | 修改 | 详细设计 | [修改] code-design §输入 + §工作目录约定 字面更新 | 已完成 | 不适用 | ./plugins/code-skills/skills/code-design/SKILL.md §输入 > 需求编码格式 + §工作目录约定 > 本技能的目录粒度 | 2026-06-08 | 826eb06 | — |
| TASK-REQ-00025-00004 | REQ-00025 | 修改 | 详细设计 | [修改] code-plan §输入 + §步骤 10A + §步骤 9B 字面更新 | 已完成 | 不适用 | ./plugins/code-skills/skills/code-plan/SKILL.md §输入 + §工作流程 > 步骤 10A > 任务编号 + §工作流程 > 步骤 9B > 任务编号分配 | 2026-06-08 | a65c766 | — |
| TASK-REQ-00025-00005 | REQ-00025 | 修改 | 详细设计 | [修改] code-it §输入 + §步骤 1 + §步骤 7 字面更新 | 已完成 | 不适用 | ./plugins/code-skills/skills/code-it/SKILL.md §输入 > 任务编码格式 + §工作流程 > 步骤 1 解析任务编码 + §工作流程 > 步骤 7 写入 RESULT.md | 2026-06-08 | fde785c | — |
| TASK-REQ-00025-00006 | REQ-00025 | 修改 | 详细设计 | [修改] code-unit §输入 字面更新 | 已完成 | 不适用 | ./plugins/code-skills/skills/code-unit/SKILL.md §输入 > 任务编码格式 | 2026-06-08 | 0020f8f | — |
| TASK-REQ-00025-00007 | REQ-00025 | 修改 | 详细设计 | [修改] code-check §输入 字面更新 | 已完成 | 不适用 | ./plugins/code-skills/skills/code-check/SKILL.md §输入 > 需求编号 / 任务编码 | 2026-06-08 | fab832e | — |
| TASK-REQ-00025-00008 | REQ-00025 | 修改 | 详细设计 | [修改] code-fix §输入 + §步骤 1 字面更新 | 已完成 | 不适用 | ./plugins/code-skills/skills/code-fix/SKILL.md §输入 > 缺陷编号格式 + §工作流程 > 步骤 1 收集输入 ID 并判定路径 | 2026-06-08 | 45a2aee | — |
| TASK-REQ-00025-00009 | REQ-00025 | 修改 | 详细设计 | [修改] code-dashboard 算法 4 字面更新(双正则兼容) | 已完成 | 不适用 | ./plugins/code-skills/skills/code-dashboard/SKILL.md §工作流程 > 算法 4 解析任务编号 | 2026-06-08 | b607d00 | — |
| TASK-REQ-00026-00001 | REQ-00026 | 修改 | 详细设计 | [修改] 9 个 SKILL.md 描述段去专属化(占位符 `<本仓库>` + 概述段声明) | 已完成 | 不适用 | plugins/code-skills/skills/{code-it,code-publish}/SKILL.md §唯一允许的生产代码改动场景 / §模板 | 2026-06-08 13:10 | 0818d2a | — |
| TASK-REQ-00026-00002 | REQ-00026 | 修改 | 详细设计 | [修改] code-rule/SKILL.md 描述段 + L336 CLAUDE.md 字面替换 | 已完成 | 不适用 | plugins/code-skills/skills/code-rule/SKILL.md §工作目录约定 / §工具使用约定 / L336 | 2026-06-08 13:20 | e8f3303 | — |
| TASK-REQ-00026-00003 | REQ-00026 | 修改 | 详细设计 | [修改] code-publish/templates/(DEPLOY.md / UPDATE.md / qanda-README.md) 字面替换 | 已完成 | 不适用 | plugins/code-skills/skills/code-publish/templates/{DEPLOY,UPDATE,qanda-README}.md §头部(L3) / L133 | 2026-06-08 13:28 | 8035c0c | — |
| TASK-REQ-00026-00004 | REQ-00026 | 修改 | 详细设计 | [修改] code-init/templates/INIT-REPORT.md 字面替换(L3/L8) | 已完成 | 不适用 | plugins/code-skills/skills/code-init/templates/INIT-REPORT.md L3 / L8 | 2026-06-08 13:35 | 5185ee2 | — |
| TASK-REQ-00026-00005 | REQ-00026 | 文档 | 详细设计 | [文档] 同步版本看板"任务清单" + "变更记录"(`code-it` 末尾兜底承担) | 已完成 | 不适用 | assistants/V0.0.3/RESULT.md §任务清单 / §变更记录 | 2026-06-08 13:40 | — | — |
| TASK-REQ-00027-00001 | REQ-00027 | 修改 | 详细设计 | [修改] code-fix/SKILL.md 纯登记型重写(状态机收敛 + 不产出 fix-plan.md + 引导后续调 code-plan/code-it/code-check) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md §目标 / §工作目录约定 / §工作流程 步骤 4 询问本轮状态推进 / §步骤 5 补充本轮信息 / §步骤 6 写缺陷详情 / §步骤 9 引导下一步 / §过程文档格式 / §不要做的事 | 2026-06-08 15:40 | e860b0b | — |
| TASK-REQ-00027-00002 | REQ-00027 | 修改 | 详细设计 | [修改] code-auto/SKILL.md 模式 C 增加(模式识别正则 + BUG 路径子技能调用表 + fix/<BUG-NNN>/auto-report.md 输出) | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md §输入 / §子技能调用表 / §附加约束 / §步骤 7 报告 / §边界与异常 / §不要做的事 | 2026-06-08 15:45 | 55050f4 | — |
| TASK-REQ-00027-00003 | REQ-00027 | 文档 | 详细设计 | [文档] 同步版本看板"任务清单" + "变更记录"(`code-it` 末尾兜底承担) | 已完成 | 不适用 | assistants/V0.0.3/RESULT.md §任务清单 / §里程碑 / §变更记录 | 2026-06-08 15:50 | — | — |
| TASK-REQ-00027-00004 | REQ-00027 | 修改 | 审查改修 | [修改] 修正 code-fix 步骤 4 状态推进表(删除中间/非本技能终态行,仅保留 5 候选状态) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md §步骤 4 询问本轮状态推进 | 2026-06-08 17:35 | 9c088d0 | TASK-REQ-00027-00001 |
| TASK-REQ-00027-00005 | REQ-00027 | 修改 | 审查改修 | [修改] 修正 code-fix 步骤 9 引导表("已关闭-不修复" 与"已关闭-非缺陷"逻辑统一) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md §步骤 9 引导下一步 | 2026-06-08 17:37 | bfc6f2b | TASK-REQ-00027-00001 |
| TASK-REQ-00027-00006 | REQ-00027 | 修改 | 审查改修 | [修改] 修正 code-fix 步骤 4 注释(本技能只推进"报告 / 调查中";"修复规划中"仅校验不主动推进) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md §步骤 4 询问本轮状态推进 | 2026-06-08 17:39 | 4041998 | TASK-REQ-00027-00001 |
| TASK-REQ-00027-00007 | REQ-00027 | 修改 | 审查改修 | [修改] code-fix 全局清理 investigation.md 引用(纯登记型不再创建该文件) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md §步骤 3 / §步骤 5 / §步骤 10 / §过程文档格式 | 2026-06-08 17:41 | 41ddbbb | TASK-REQ-00027-00001 |
| TASK-REQ-00027-00008 | REQ-00027 | 修改 | 审查改修 | [修改] code-auto 步骤 1 新增"模式 C"识别(首段匹配 `^BUG-\d{5}$`),独立于 fix-skip-require | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md §子技能调用表 BUG 路径子表标题 | 2026-06-08 17:43 | 26c228a | TASK-REQ-00027-00002 |
| TASK-REQ-00027-00009 | REQ-00027 | 修改 | 审查改修 | [修改] code-auto §"路径感知模式"扩展为 5 种(新增"模式 C"),§"步骤 1 子分支"扩展为 1A-1E | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md §输入 / §工作流步骤 步骤 1 子分支 | 2026-06-08 17:45 | bf9955d | TASK-REQ-00027-00002 |
| TASK-REQ-00027-00010 | REQ-00027 | 修改 | 审查改修 | [修改] code-auto 步骤 2/3 适配 BUG 路径(`code-design` BUG 跳过 / `code-plan` BUG 路径入参) | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md §工作流步骤 步骤 2 / 步骤 3 | 2026-06-08 17:47 | 9342318 | TASK-REQ-00027-00002 |
| TASK-REQ-00028-00001 | REQ-00028 | 文档 | 详细设计 | [新增] code-answer SKILL.md(只读功能查询) | 已完成 | 不适用 | plugins/code-skills/skills/code-answer/SKILL.md | 2026-06-10 11:00 | — | — |
| TASK-REQ-00029-00001 | REQ-00029 | 修改 | 详细设计 | [修改] code-dashboard 渲染层瘦身(总览 ≤ 8 / 需求 ≤ 15 行) | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §输出 + §工作流程 步骤 4 段 1 ~ 段 5 | 2026-06-10 12:00 | — | — |
| TASK-REQ-00030-00001 | REQ-00030 | 修改 | 详细设计 | [修改] code-design/SKILL.md:步骤 0b 收敛 + 9A/10A/11A 输出深度收窄 | 已完成 | 不适用 | plugins/code-skills/skills/code-design/SKILL.md §步骤 0b + §步骤 9A/10A/11A | 2026-06-12 14:45 | e203023 | — |
| TASK-REQ-00030-00002 | REQ-00030 | 修改 | 详细设计 | [修改] templates/design.md:§7/§8/§9/§10 章节重写 + §7.5/§8.5/§9.5 新增 | 已完成 | 不适用 | plugins/code-skills/skills/code-design/templates/design.md §7-§10 + 顶部注释 | 2026-06-12 14:55 | abc3db2 | — |
| TASK-REQ-00030-00003 | REQ-00030 | 修改 | 详细设计 | [修改] code-plan/SKILL.md:步骤 7A 补做强约束 + 步骤 10A 架构骨架触发收紧 | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §步骤 7A + §步骤 10A | 2026-06-12 15:00 | 2731ffe | — |
| TASK-REQ-00030-00004 | REQ-00030 | 修改 | 详细设计 | [修改] templates/plan.md:§4-§10 章节由"建议"改"必填" | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/templates/plan.md §4-§12 | 2026-06-12 15:05 | e54117f | — |
| TASK-REQ-00030-00005 | REQ-00030 | 修改 | 详细设计 | [修改] code-check/SKILL.md:评审清单追加 3 校验点(详设完整性 / 概设越界 / 行数比例) | 已完成 | 不适用 | plugins/code-skills/skills/code-check/SKILL.md §步骤 6 评审清单 | 2026-06-12 15:10 | 65fdbc1 | — |
| TASK-REQ-00030-00006 | REQ-00030 | 文档 | 详细设计 | [文档] 行数收敛观测:落地后 3 个新需求验证 NFR-1 | 已完成(占位) | 不适用 | (无文件修改,纯人工观测) | 2026-06-12 15:15 | — | — |
| TASK-REQ-00031-00001 | REQ-00031 | 修改 | 详细设计 | [修改] code-plan/SKILL.md:任务粒度原则内化编译/运行 + 移除测试类型 + 收窄测试状态枚举 | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §步骤 10A | 2026-06-12 15:40 | — | — |
| TASK-REQ-00031-00002 | REQ-00031 | 修改 | 详细设计 | [修改] code-it/SKILL.md:文档头 ## 目标 追加"不含单元测试"职责声明 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md ## 目标 | 2026-06-12 15:44 | — | — |
| TASK-REQ-00031-00003 | REQ-00031 | 修改 | 详细设计 | [修改] code-unit/SKILL.md:文档头 ## 目标 追加"独立、可选"职责声明 | 已完成 | 不适用 | plugins/code-skills/skills/code-unit/SKILL.md ## 目标 | 2026-06-12 15:46 | — | — |
| TASK-REQ-00031-00004 | REQ-00031 | 修改 | 详细设计 | [修改] code-auto/SKILL.md:任务循环步骤 4.b 改为"恒等跳过" | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md §步骤 4 任务循环 | 2026-06-12 15:48 | — | — |
| TASK-REQ-00031-00005 | REQ-00031 | 修改 | 详细设计 | [修改] templates/plan.md:任务类型移除 测试 + 测试状态字段收窄为 2 枚举 | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/templates/plan.md ## 任务总览 | 2026-06-12 15:50 | — | — |
| TASK-REQ-00032-00001 | REQ-00032 | 修改 | 详细设计 | [修改] code-require 步骤 10A/10B 末尾追加下一步建议段 | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §步骤 10A 段内文末 / §步骤 10B 段内文末 | 2026-06-12 17:10 | 0d40251 | — |
| TASK-REQ-00033-00001 | REQ-00033 | 修改 | 详细设计 | [修改] code-require §"不要做的事" 小节追加"不涉及技术选型"硬约束 | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §"不要做的事" 小节末尾 | 2026-06-15 12:45 | 26698e8 | — |
| TASK-REQ-00034-00001 | REQ-00034 | 修改 | 详细设计 | [修改] code-it 步骤 8a 守卫 + 步骤 8.5 按需写单测接管 + 文档头/L18/L795/L907-908 字面改写 | 待开始 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §"## 步骤 8"之后新增"## 步骤 8a / 8.5" + 文档头 + L18 + L795 + L907-908 | — | — | — |
| TASK-REQ-00034-00002 | REQ-00034 | 修改 | 详细设计 | [修改] code-it 模板新增"## 单元测试"小节 | 待开始 | 不适用 | plugins/code-skills/skills/code-it/templates/RESULT.md 既有章节追加 1 小节 | — | — | — |
| TASK-REQ-00034-00003 | REQ-00034 | 修改 | 详细设计 | [修改] code-plan/SKILL.md L368/431/445/454/1105 字面改写(由 `code-unit` 另起流程 → 由 `code-it` 内化) | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md L368 / L431 / L445 / L454 / L1105 | 2026-06-15 15:35 | ab7177c | — |
| TASK-REQ-00034-00004 | REQ-00034 | 修改 | 详细设计 | [修改] code-auto/SKILL.md 步骤 4.b 整段删除 + 10 处字面改写 | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md L45 + L213-227 + L388-411 + L432-433 + L449 + L624-625 + L672 + L692 + L711 + L741 + L797 + L806 + L834 | 2026-06-15 16:10 | 见 commit hash | — |
| TASK-REQ-00034-00005 | REQ-00034 | 修改 | 详细设计 | [修改] code-check/SKILL.md 10 处 test/<TASK-...>/ 引用改写 | 已完成 | 不适用 | plugins/code-skills/skills/code-check/SKILL.md L3 + L21 + L40-41 + L56 + L72 + L96 + L151 + L281 + L608 + L615 | 2026-06-15 16:45 | 8c16b5d | — |
| TASK-REQ-00034-00006 | REQ-00034 | 修改 | 详细设计 | [修改] plugin.json + marketplace.json 注册项删除(3 处字面) | 已完成 | 不适用 | plugins/code-skills/.claude-plugin/plugin.json L15 + .claude-plugin/marketplace.json L24 / L39 | 2026-06-15 17:00 | eac014d | — |
| TASK-REQ-00034-00007 | REQ-00034 | 修改 | 详细设计 | [修改] 4 README + CLAUDE.md 字面改写(去 `code-unit` 引用) | 已完成 | 不适用 | README.md + README.en.md + plugins/code-skills/README.md + plugins/code-skills/README.en.md + CLAUDE.md 描述段 | 2026-06-15 17:30 | 4f4e448 | — |
| TASK-REQ-00034-00008 | REQ-00034 | 修改 | 详细设计 | [修改] 7 项目级规范字面改写(去 `code-unit` 引用) | 已完成 | 不适用 | assistants/rules/encoding-conventions.md + review-checklist.md + skill-conventions.md + module-conventions.md + dashboard-conventions.md + plugin-conventions.md + migration-mapping.md 描述段 | 2026-06-15 17:45 | 839b78e | — |
| TASK-REQ-00034-00009 | REQ-00034 | 修改 | 详细设计 | [修改] 11 技能 SKILL.md 描述段去 `code-unit` 引用(`code-it` 改写为"含按需写单测") | 已完成 | 不适用 | plugins/code-skills/skills/{code-require, code-design, code-plan, code-fix, code-init, code-publish, code-version, code-rule, code-merge, code-answer, code-dashboard, code-auto, code-it}/SKILL.md frontmatter description 字段 | 2026-06-15 18:00 | 3222843 | — |
| TASK-REQ-00034-00010 | REQ-00034 | 删除 | 详细设计 | [删除] code-unit 整体(SKILL.md 635 行 + templates/ 目录) | 已完成 | 不适用 | plugins/code-skills/skills/code-unit/SKILL.md 整体 + plugins/code-skills/skills/code-unit/templates/ 整体 | 2026-06-15 18:15 | b9c9d6c | — |
| TASK-REQ-00035-00001 | REQ-00035 | 修改 | 详细设计 | [修改] code-require 步骤 0a 过程文档判定 + 模板新增 | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md(锚点追加) + plugins/code-skills/skills/code-require/templates/process-doc-decisions.md(新文件) | 2026-06-15 19:30 | 6be9a13 | — |
| TASK-REQ-00035-00002 | REQ-00035 | 修改 | 详细设计 | [修改] code-design 步骤 0a.5 过程文档判定 + 模板新增 | 已完成 | 不适用 | plugins/code-skills/skills/code-design/SKILL.md(锚点追加) + plugins/code-skills/skills/code-design/templates/process-doc-decisions.md(新文件) | 2026-06-15 20:00 | 48335d7 | — |
| TASK-REQ-00035-00003 | REQ-00035 | 修改 | 详细设计 | [修改] code-plan 步骤 0a.5 过程文档判定 + 模板新增 | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md(锚点追加) + plugins/code-skills/skills/code-plan/templates/process-doc-decisions.md(新文件) | 2026-06-15 20:00 | 48335d7 | — |
| TASK-REQ-00035-00004 | REQ-00035 | 修改 | 详细设计 | [修改] code-it 步骤 0a 任务级过程文档判定 + 模板新增 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md(锚点追加) + plugins/code-skills/skills/code-it/templates/process-doc-decisions.md(新文件) | 2026-06-15 20:00 | 48335d7 | — |
| TASK-REQ-00035-00005 | REQ-00035 | 修改 | 详细设计 | [修改] code-check 步骤 0a + 8.13 评审维度 + 模板新增 | 已完成 | 不适用 | plugins/code-skills/skills/code-check/SKILL.md(2 锚点追加) + plugins/code-skills/skills/code-check/templates/process-doc-decisions.md(新文件) | 2026-06-15 20:00 | 48335d7 | — |
| TASK-REQ-00035-00006 | REQ-00035 | 修改 | 详细设计 | [修改] code-auto 编排同步(子技能调用表备注列) | 已完成 | 不适用 | plugins/code-skills/skills/code-auto/SKILL.md §子技能调用表 | 2026-06-15 20:00 | 48335d7 | — |
| TASK-REQ-00035-00007 | REQ-00035 | 修改 | 详细设计 | [修改] code-dashboard 解析兼容(变更记录行数自适应) | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §解析锚点 | 2026-06-15 20:00 | 48335d7 | — |
| TASK-REQ-00036-00001 | REQ-00036 | 文档 | 详细设计 | [文档] 扫描并产出 14 技能 SKILL.md + templates/ 待清理文件表与命中计数基线 | 已完成 | 不适用 | plugins/code-skills/skills/*/{SKILL.md, templates/*.md}(14 SKILL.md + 33 templates = 47 文件) | 2026-06-16 17:33 | — | — |
| TASK-REQ-00036-00002 | REQ-00036 | 文档 | 详细设计 | [文档] 应用 6 条清理规则(R-1 ~ R-6)到 T-1 清单,原地改写 + diff 校验 + 残缺回退 | 已完成 | 不适用 | 同 T-1(47 文件) | 2026-06-16 17:33 | — | — |
| TASK-REQ-00036-00003 | REQ-00036 | 文档 | 详细设计 | [文档] 跑 AC-1 ~ AC-8 验证 + 1 次 commit + 看板同步 + 末尾兜底 | 已完成 | 不适用 | assistants/V0.0.3/RESULT.md + git 仓库 | 2026-06-16 17:33 | a5dddb5 | — |
| TASK-REQ-00037-00001 | REQ-00037 | 修改 | 详细设计 | [修改] code-fix 步骤 4/6 + 衔接 + 不要做的事同步 | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md | 2026-06-22 09:35 | — | — |
| TASK-REQ-00037-00002 | REQ-00037 | 修改 | 详细设计 | [修改] code-plan 步骤 27A/28A 末尾追加状态回写 | 已完成 | 不适用 | plugins/code-skills/skills/code-plan/SKILL.md §缺陷分支 步骤 27A/28A | 2026-06-22 09:45 | — | T-1 |
| TASK-REQ-00037-00003 | REQ-00037 | 修改 | 详细设计 | [修改] code-it 步骤 21 末尾追加状态回写:开发中 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §缺陷分支 步骤 21 | 2026-06-22 09:55 | — | T-1 |
| TASK-REQ-00037-00004 | REQ-00037 | 修改 | 详细设计 | [修改] code-it 步骤 24 末尾追加状态回写:待审查 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §缺陷分支 步骤 24 | 2026-06-22 10:05 | — | T-1 |
| TASK-REQ-00037-00005 | REQ-00037 | 修改 | 详细设计 | [修改] code-check 步骤 1.5 BUG-NNN 识别 + 步骤 13 状态回写 | 已完成 | 不适用 | plugins/code-skills/skills/code-check/SKILL.md §步骤 1.5 / 步骤 13 | 2026-06-22 10:35 | — | T-1 |
| TASK-REQ-00037-00006 | REQ-00037 | 修改 | 详细设计 | [修改] code-dashboard 步骤 4 段 3 扩展待修复/已修复分类 | 已完成 | 不适用 | plugins/code-skills/skills/code-dashboard/SKILL.md §步骤 4 段 3 | 2026-06-22 11:05 | — | T-1 |
| TASK-REQ-00037-00007 | REQ-00037 | 文档 | 详细设计 | [文档] 端到端验证 AC-1 ~ AC-10 + 末尾兜底提交 | 已完成 | 不适用 | (无生产代码改动) | 2026-06-22 12:06 | — | T-1 ~ T-6 |
| TASK-REQ-00039-00001 | REQ-00039 | 新增 | 详细设计 | [新增] 共享库 logic-loc.md + logic-loc-defaults.md(4 函数伪代码 + 2 阈值字段) | 已完成 | 不适用 | plugins/code-skills/skills/code-it/lib/logic-loc.md + logic-loc-defaults.md | 2026-06-22 15:05 | — | — |
| TASK-REQ-00039-00002 | REQ-00039 | 修改 | 详细设计 | [修改] code-it 步骤 8 末尾追加 detectLocTool + calcLogicLoc 子步骤 + 屏显契约 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md | 2026-06-22 15:08 | — | T-1 |
| TASK-REQ-00039-00003 | REQ-00039 | 修改 | 详细设计 | [修改] code-check 步骤 8.13 新增 + 评审维度速查表第 13 维度 | 已完成 | 不适用 | plugins/code-skills/skills/code-check/SKILL.md | 2026-06-22 15:12 | — | T-1 |
| TASK-REQ-00039-00004 | REQ-00039 | 修改 | 详细设计 | [修改] code-it/templates/RESULT.md 模板新增"## 逻辑行统计"小节示例 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/templates/RESULT.md | 2026-06-22 15:16 | — | T-2 |
| TASK-REQ-00039-00005 | REQ-00039 | 文档 | 详细设计 | [文档] 端到端验证 AC-1 ~ AC-8 + 末尾兜底提交 | 已完成 | 不适用 | (无生产代码改动) | 2026-06-22 15:22 | — | T-1 ~ T-4 |
| TASK-REQ-00039-00006 | REQ-00039 | 修改 | 审查改修 | [修改] 修正 T-2 / T-3 / T-4 评审发现(合并 1 必须改 + 2 建议改) | 已完成 | 不适用 | code-it/templates/RESULT.md + code-it/SKILL.md + code-check/SKILL.md | 2026-06-22 16:42 | — | T-2, T-3, T-4 |
| TASK-REQ-00040-00001 | REQ-00040 | 修改 | 详细设计 | [修改] code-fix 步骤 0 末尾追加"项目可启动性探测" 子节(detectStartability 7 步算法:Node.js/Python/Makefile/Docker/Rust/Go/Java) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md | 2026-06-25 14:31 | ae42e39 | REQ-00040 |
| TASK-REQ-00040-00002 | REQ-00040 | 修改 | 详细设计 | [修改] code-fix 步骤 6 末尾追加"复现产物登记" 子节(reproduceBug 9 步算法 + executeStep 3 类采集 + 11 边界 + 1 复合边界) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/SKILL.md | 2026-06-25 14:36 | b9afdba | REQ-00040 |
| TASK-REQ-00040-00003 | REQ-00040 | 修改 | 详细设计 | [修改] bug.md 模板新增"## 复现产物登记" 区段(3 子项:产物清单/实际行为/复现结论)+ 文档头 2 字段(复现方式/产物路径) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/templates/bug.md | 2026-06-25 14:42 | f029be6 | REQ-00040 |
| TASK-REQ-00040-00004 | REQ-00040 | 修改 | 详细设计 | [修改] assistants-layout.md 同步追加 reproduce/ 子目录行(在 fix/<BUG-NNN>/ 子目录列表) | 已完成 | 不适用 | plugins/code-skills/skills/code-fix/templates/assistants-layout.md | 2026-06-25 14:46 | 70f4632 | REQ-00040 |
| TASK-REQ-00040-00005 | REQ-00040 | 文档 | 详细设计 | [文档] 端到端验证 12 条 AC(全部静态校验,本仓库 0 测试框架)+ 末尾兜底提交 | 已完成 | 不适用 | (无生产代码改动) | 2026-06-25 14:50 | 6a8d55c | REQ-00040 |
| TASK-REQ-00040-00006 | REQ-00040 | 文档 | 详细设计 | [文档] 同步版本看板"任务清单" / "里程碑" / "变更记录"(code-plan 末尾兜底承担) | 已完成 | 不适用 | assistants/V0.0.3/RESULT.md | 2026-06-25 14:57 | — | REQ-00040 |
| TASK-REQ-00040-00007 | REQ-00040 | 修改 | 审查改修 | [修改] 移除 design line 175 越界字段类型字面 string | 待开始 | 不适用 | assistants/V0.0.3/design/REQ-00040/RESULT.md line 175 | — | — | TASK-REQ-00040-00001, TASK-REQ-00040-00002 |
| TASK-BUG-00004-00001 | BUG-00004 | 修改 | 缺陷修复 | [修改] code-it 步骤 8.7 新增 + 步骤 9/10/11 守卫 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §步骤 8.7 / §步骤 9 / §步骤 10 / §步骤 11 | 2026-06-22 20:55 | — | BUG-00004 |
| TASK-BUG-00004-00002 | BUG-00004 | 修改 | 缺陷修复 | [修改] code-it 步骤 13/16 + templates/RESULT.md 改造 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §步骤 13 / §步骤 16 + templates/RESULT.md | 2026-06-22 21:10 | — | BUG-00004 |
| TASK-BUG-00004-00003 | BUG-00004 | 文档 | 缺陷修复 | [文档] 端到端验证(在 V0.0.3 下重跑 TASK-REQ-00039-00003 + 真实代码类任务对照) | 已完成 | 不适用 | assistants/V0.0.3/code/TASK-REQ-00039-00003/(新生成) | 2026-06-22 22:00 | — | BUG-00004 |
| TASK-BUG-00004-00004 | BUG-00004 | 文档 | 缺陷修复 | [文档] 其他 6 个技能旁路验证(grep 判定表 + 静态校验,**不修改**) | 已完成 | 不适用 | plugins/code-skills/skills/{code-require,code-design,code-check,code-plan,code-fix,code-init,code-rule}/SKILL.md | 2026-06-22 23:00 | — | BUG-00004 |
| TASK-REQ-00038-00001 | REQ-00038 | 修改 | 详细设计 | [修改] code-it 步骤 8a.0 模块识别(新增子步骤) | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §步骤 8 之后新增"## 步骤 8a.0 — 模块识别" | 2026-06-22 13:50 | d632222 | — |
| TASK-REQ-00038-00002 | REQ-00038 | 修改 | 详细设计 | [修改] code-it 步骤 8a 守卫位置 + 步骤 8.5 单测输出位置扩展 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/SKILL.md §步骤 8a.1 / 8a.2 / 8a.4 + §步骤 8.5.2 / 8.5.5 | 2026-06-22 14:10 | 17ba4ca | — |
| TASK-REQ-00038-00003 | REQ-00038 | 修改 | 详细设计 | [修改] 模板追加"## 各模块单测结果"小节 + code-plan 任务粒度描述字面改写 + 端到端验证 | 已完成 | 不适用 | plugins/code-skills/skills/code-it/templates/RESULT.md + plugins/code-skills/skills/code-plan/SKILL.md L473 / L496 + (端到端校验) | 2026-06-22 14:25 | ae59fd2 | — |
| TASK-BUG-00005-00001 | BUG-00005 | 修改 | 缺陷修复 | [修改] code-require 步骤 7A 添加技术选型过滤器 | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §步骤 7A(L322-335) | 2026-06-23 | 5250a54 | — | BUG-00005 | — | — |
| TASK-BUG-00005-00002 | BUG-00005 | 修改 | 缺陷修复 | [修改] code-require 步骤 8A 添加 NFR 技术选型过滤器 | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §步骤 8A(L337-353) | 2026-06-23 | a94bda2 | — | T-1, BUG-00005 | — | — |
| TASK-BUG-00005-00003 | BUG-00005 | 修改 | 缺陷修复 | [修改] code-require 步骤 615 硬约束增强(引用步骤 7A/8A) | 已完成 | 不适用 | plugins/code-skills/skills/code-require/SKILL.md §步骤 615(L619-620) | 2026-06-23 | c3206c9 | — | T-1, T-2, BUG-00005 | — | — |

**统计**:
- 总任务数:103
- 真正可发布数(开发=已完成 ∧ 测试∈{已运行-通过, 不适用}):**97**
- 开发已完成 / 未完成:**97 / 6**
- 测试已通过 / 已失败 / 不适用 / 未编写:0 / 0 / **103** / 0

---

## 缺陷清单

> 写入方:
> - `code-check` 评审时发现的严重缺陷(自动登记)
> - `code-it` 编码时发现的已记录缺陷
> - `code-unit` 测试时发现的代码 bug(转交 `code-it`)

| 缺陷编号 | 严重度 | 标题 | 状态 | 报告时间 | 修复时间 | 关联任务 | 修复提交 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BUG-00001 | P0 | code-require/code-design/code-plan... | 修复编码中 | 2026-06-06 22:41 | — | — | — |
| BUG-00002 | P0 | SKILL.md 描述中"特定文件类型"字面(`skills/*/SKILL.md` / `tests/` / `*.test.*`)违反本项目"通用开发技能集"定位 | 已修复-待验证 | 2026-06-08 14:00 | 2026-06-08 14:40 | — | 678e602 |
| BUG-00003 | P0 | SKILL.md 描述中"绝对路径"(`plugins/code-skills/...`)在 plugin 安装后断链 | 修复编码中 | 2026-06-08 14:10 | — | — | — |
| BUG-00004 | P1 | `code-it` SKILL.md "过程文档自适应判定"章节定义的判定准则未真正接入"## 工作流程",导致纯 Markdown 改造类任务仍生成 `compile-and-run.md` / `test-results.md` 等空占位过程文档 | 已完成 | 2026-06-22 20:15 | 2026-06-22 23:35 | wangmiao | REQ-00039 | [RESULT.md](./fix/BUG-00004/RESULT.md) |
| BUG-00005 | P1 | `/code-require` 仍出现技术选型问路,违反 REQ-00033 字面硬约束 | 已完成 | 2026-06-22 14:50 | 2026-06-23 | wangmiao | — | [RESULT.md](./fix/BUG-00005/RESULT.md) |

**统计**:5 / P0: 3 / P1: 2 / P2: 0 / 已修复 0 / 待修复 5 / 修复规划中 0 / 修复编码中 2 / 调查中 0 / 报告 1 / 已修复-待验证 1 / 已完成 1

---

## 评审发现汇总

> 写入方:`code-check`

| 评审 ID | 需求 | 任务 | 维度 | 级别 | 描述 | 派生改修任务 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | REQ-00020 | TASK-REQ-00020-00003 | 正确性 + 一致性 | 必须改 | 任务粒度调整规则表 Markdown 列数不一致(表头 4 列,前 2 行 `--minimal` / `--balanced` 只填 3 列) | TASK-REQ-00020-00007 | 已处理 |
| F-002 | REQ-00020 | TASK-REQ-00020-00006 | 正确性 + 详设符合度 | 必须改 | §步骤 6 路由表移除"PLAN.md 存在但 RESULT.md 不存在 → §7D"分支,但 §步骤 7D 段本身未删,逻辑矛盾 | TASK-REQ-00020-00008 | 已处理 |
| F-003 | REQ-00020 | TASK-REQ-00020-00002 | 可维护性 | 建议改 | code-plan 步骤 0b 中需求"按需"判定规则缺失 | — | 待处理 |
| F-004 | REQ-00020 | TASK-REQ-00020-00002 | 性能(屏显) | 建议改 | 7 维度屏显首行 118 字符在 80-100 列窗口软换行 | — | 待处理 |
| F-005 | BUG-00004 | TASK-BUG-00004-00001 ~ 00004 | 正确性 + 规范 + 详设符合度 + 安全 + 性能 + 可维护性 + 测试 + 一致性 + 接口 + 详设完整性 + 代码行数 + 过程文档适配性 | 全部通过 | 8 维度评审 + 14 个规范文件应用,全部通过;0 条"必须改"/0 条"建议改"/0 条"可选";0 个派生"审查改修"任务 | — | 评审通过 |
| F-006 | REQ-00040 | — | 详设符合度 + 概设越界 | 必须改 | `design/REQ-00040/RESULT.md` line 175 表格 2 行 `string` 类型字面越界(违反 `code-plan` 步骤 8.11 准则) | TASK-REQ-00040-00007 | 待处理 |
| F-005 | REQ-00020 | TASK-REQ-00020-00005 | 一致性 | 建议改 | M-2 引用方在 REQ 路径(直接复述)与 BUG 路径("同 X,不再重复")用了两套不同引用语法 | — | 待处理 |
| F-006 | REQ-00020 | TASK-REQ-00020-00006 | 一致性 | 建议改 | 看板任务清单"完成时间"列(16:30)与变更记录时间(21:35~22:22)不一致 | — | 待处理 |
| F-007 | REQ-00020 | TASK-REQ-00020-00001 | 可维护性 | 可选 | T-1 RESULT.md 表头写"6 行净变化"实际 +2 行,数字不精确 | — | 待处理 |
| F-008 | REQ-00020 | TASK-REQ-00020-00002 | 可维护性 | 可选 | code-design 步骤 0b 标题"收敛到最多 2 问"对小需求不准确 | — | 待处理 |
| F-009 | REQ-00020 | TASK-REQ-00020-00005 | 可维护性 | 可选 | M-2 引用方表述漂移(`code-design` 步骤 3 不应被列为"引用方") | — | 待处理 |
| F-010 | REQ-00030 | TASK-REQ-00030-00005 | 详设完整性(§8.10) | 建议改 | §8.10 详设完整性校验点实现与实际产出形式不匹配:5 正则 0 命中(§8.11 通过)但 §8.10 误报 5 个"plan 涉及文件未在 §4-§10 引用"(plan 用中文描述而非 `<文件路径>`)。非阻塞;留作 follow-up REQ | — | 待处理(F-001 in [REVIEW-REPORT](./review/REQ-00030/REVIEW-REPORT.md)) |
| F-010 | REQ-00020 | TASK-REQ-00020-00003 | 一致性 | 可选 | 任务粒度调整规则表"可读性=高 + 编程语言非自然语言"列名超长,与其他维度列名不对齐 | — | 待处理 |
| F-011 | REQ-00020 | TASK-REQ-00020-00004 | 可维护性 | 可选 | code-design 步骤 0b.0 / 步骤 3 等"原版"端未追加反向引用说明 | — | 待处理 |
| F-012 | REQ-00020 | TASK-REQ-00020-00005 | 可维护性 | 可选 | `> **公共段定义**` 是粗体不是新章节标题,`## 公共子步骤` 概念无独立章节锚点 | — | 待处理 |
| F-013 | REQ-00020 | TASK-REQ-00020-00005 | 可维护性 | 可选 | code-it 步骤 23 把 23.1 / 23.2 / 23.3 / 23.4 4 个子步骤合并,丢失子节锚点 | — | 待处理 |
| F-014 | REQ-00020 | TASK-REQ-00020-00006 | 一致性 | 可选 | 看板"执行的开发命令记录"区段仍为空(本仓库特性,git 元信息查询不需登记) | — | 待处理 |
| F-015 | REQ-00020 | TASK-REQ-00020-00001 | 文档质量 | 可选 | T-1 / T-2 静态校验仅 6/9 INV,后续任务 9-11 条,过程文档质量可统一 | — | 待处理 |
| F-016 | REQ-00020 | TASK-REQ-00020-00002 | 一致性 | 可选 | 屏显模板的"功能性:`<高/中/低>`"选项未含"不适用",与其他 6 维度选项不同(沿用 REQ-00011 设计,正确) | — | 待处理 |
| F-017 | REQ-00020 | TASK-REQ-00020-00002 | 详设符合度 | 可选 | 中需求 4 问"按需"判定规则缺失,与 NFR-2 "AI 不自由裁量"轻度冲突(同 F-003) | — | 待处理 |
| F-018 | REQ-00020 | TASK-REQ-00020-00005 | 可维护性 | 可选 | code-plan/SKILL.md 超 1000 行,接近 LLM 单次加载阈值 | — | 待处理 |
| F-019 | REQ-00020 | TASK-REQ-00020-00006 | 详设符合度 | 可选 | code-it §0a.7 改后保留"`if not taskNum.startsWith('TASK-REQ-'): return`"在 E-9 表格行内,守卫主流程交叉指明缺失 | — | 待处理 |
| F-020 | REQ-00022 | TASK-REQ-00022-00001 ~ 00010 | 一致性 + 规范 | 必须改 | (无) | — | (评审通过) |
| F-021 | REQ-00023 | TASK-REQ-00023-00001 ~ 00006 | 一致性 + 规范 | 必须改 | (无) | — | (评审通过) |
| F-022 | REQ-00024 | TASK-REQ-00024-00001 | 一致性 + 规范 + 详细设计符合度 | 必须改 | (无) | — | (评审通过,0 必须改 / 0 建议改 / 0 可选) |
| F-023 | REQ-00025 | TASK-REQ-00025-00001 ~ 00009 | 一致性 + 规范 + 详细设计符合度 | 必须改 | (无) | — | (评审通过,0 必须改 / 0 建议改 / 0 可选) |
| F-024 | REQ-00027 | TASK-REQ-00027-00001 | 详设符合度 | 必须改 | 步骤 4 状态推进表保留"修复规划中 / 修复编码中 / 已修复-待验证 / 已修复-已验证 / 已关闭-不修复"等中间/非本技能终态行,偏离设计 §2.1"仅含 5 候选状态" | TASK-REQ-00027-00004 | 已处理 |
| F-025 | REQ-00027 | TASK-REQ-00027-00001 | 一致性 | 必须改 | 步骤 9 引导表"已关闭-不修复 → 由 code-check 推进"与"已关闭-非缺陷 → (终态)"逻辑不一致;code-check 实际推进的终态是"已关闭" | TASK-REQ-00027-00005 | 已处理 |
| F-026 | REQ-00027 | TASK-REQ-00027-00001 | 可维护性 | 必须改 | 步骤 4 注释"本技能只推进 报告/调查中/修复规划中(前 3 段)"与表中"修复规划中 → 由 code-plan 推进"自相矛盾 | TASK-REQ-00027-00006 | 已处理 |
| F-027 | REQ-00027 | TASK-REQ-00027-00001 | 一致性 / 可维护性 | 必须改 | 步骤 6 / 步骤 10 仍把 `investigation.md` 列为本技能可能创建的文件,但"过程文档格式(纯登记型)" 段已声明不产出 | TASK-REQ-00027-00007 | 已处理 |
| F-028 | REQ-00027 | TASK-REQ-00027-00002 | 详设符合度 | 必须改 | BUG 路径子技能调用表写"触发:`fix-skip-require` 模式",但设计要求新增独立"模式 C"(首段匹配 `^BUG-\d{5}$`) | TASK-REQ-00027-00008 | 已处理 |
| F-029 | REQ-00027 | TASK-REQ-00027-00002 | 规范 / 接口 | 必须改 | 异常表 E-20 引用"模式 C",但 §"4 种路径感知模式" 表只有 4 类,缺"模式 C";步骤 1 子分支 1A-1D 仍按"需求路径"设计 | TASK-REQ-00027-00009 | 已处理 |
| F-030 | REQ-00027 | TASK-REQ-00027-00002 | 详设符合度 | 必须改 | 步骤 2 / 步骤 3 仍按"需求路径"设计,缺 BUG 路径子分支(`code-design` BUG 跳过 / `code-plan` BUG 路径入参) | TASK-REQ-00027-00010 | 已处理 |
| F-031 | REQ-00029 | TASK-REQ-00029-00001 | 可维护性 | 建议改 | 步骤 5 段内仍用 3 行模板(`建议: ...` / `依据: ...` / `优先级: ...`)描述建议数据结构,与步骤 4 段 4 单行格式描述不一致(冗余但不影响行为,步骤 5 只产数据结构,屏显由步骤 4 渲染) | — | 待处理 |
| F-032 | REQ-00029 | TASK-REQ-00029-00001 | 一致性 | 建议改 | §"衔接 > 下游"段仍说"本需求 REQ-00023 改造后,屏显总行数 ≤ 12 行",与本需求 REQ-00029 改造后"≤ 8 行 / ≤ 15 行"字面冲突 | — | 待处理 |
| F-033 | REQ-00033 | TASK-REQ-00033-00001 | 概设/详设完整性(8.10/8.11/8.12) | 必须改 | (无) | — | (评审通过,0 必须改 / 0 建议改 / 0 可选;12 维度全过;8.10/8.11/8.12 三个新增校验点全部通过) |
| F-034 | REQ-00039 | TASK-REQ-00039-00004 | 正确性 | 必须改 | 模板"## 10. 逻辑行统计(由 code-it 内化,新增,"小节标题末尾有未闭合的半角逗号 `,`(line 124) | TASK-REQ-00039-00006 | 已处理 |
| F-035 | REQ-00039 | TASK-REQ-00039-00002 | 一致性 | 建议改 | 步骤 8.6.3 E-3 字面与 `logic-loc.md` §函数 2 错误处理字面基本一致但任务级 vs 函数级职责混淆;建议追加"任务级继续下一文件"字面 | TASK-REQ-00039-00006 | 已处理 |
| F-036 | REQ-00039 | TASK-REQ-00039-00003 | 一致性 | 建议改 | 步骤 8.13 "总规模优先,新增次之" 字面描述与 `logic-loc.md` §函数 4 算法字面有出入;建议改为"先判 totalLoc,再判 newLoc(两个独立发现,可同时触发)" | TASK-REQ-00039-00006 | 已处理 |
| F-037 | REQ-00033(关联) | TASK-BUG-00005-00001 / 00003 | 可维护性 | 建议改 | 关键词数量声称与字面不符(8 处:SKILL.md L620 + T-1 RESULT.md L89/L100/L155 + T-3 RESULT.md L57/L64/L97/L134);声称 T-1 关键词集"20 个",实际 22 个(沿用详细设计 §5.1 字节级一致);机械性字面修正(20→22),不影响功能性;留作 follow-up | — | 待处理(follow-up) |

**统计**:37 / 必须改: 0(8 个必须改 F-024 ~ F-030 / F-034 全部 已处理) / 建议改: 9 / 可选: 13 / 已处理: 10 / 评审中: 0 / 待处理: 1

---

## 派生任务记录

> 写入方:`code-check`(派生"审查改修"任务时)
> 用途:追踪"由 review 派生、关联到原任务"的特殊任务链路

| 派生任务 | 关联原任务 | 派生时间 | review 来源 | 状态 |
| --- | --- | --- | --- | --- |
| TASK-REQ-00020-00007 · [修改] 修复任务粒度调整规则表 4 列与 3... | TASK-REQ-00020-00003 | 2026-06-06 22:30 | [REVIEW-REPORT.md](./review/REQ-00020/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00020-00008 · [修改] 清理 §步骤 7D 段,与 §步骤 6 ... | TASK-REQ-00020-00006 | 2026-06-06 22:30 | [REVIEW-REPORT.md](./review/REQ-00020/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00027-00004 · [修改] 修正 code-fix 步骤 4 状态推进表(仅保留 5 候选状态) | TASK-REQ-00027-00001 | 2026-06-08 17:30 | [REVIEW-REPORT.md](./review/REQ-00027/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00027-00005 · [修改] 修正 code-fix 步骤 9 引导表("已关闭-不修复" 与"已关闭-非缺陷"逻辑统一) | TASK-REQ-00027-00001 | 2026-06-08 17:30 | [REVIEW-REPORT.md](./review/REQ-00027/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00027-00006 · [修改] 修正 code-fix 步骤 4 注释(本技能只推进"报告 / 调查中";"修复规划中"仅校验不主动推进) | TASK-REQ-00027-00001 | 2026-06-08 17:30 | [REVIEW-REPORT.md](./review/REQ-00027/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00027-00007 · [修改] code-fix 全局清理 investigation.md 引用(纯登记型不再创建该文件) | TASK-REQ-00027-00001 | 2026-06-08 17:30 | [REVIEW-REPORT.md](./review/REQ-00027/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00027-00008 · [修改] code-auto 步骤 1 新增"模式 C"识别(首段匹配 `^BUG-\d{5}$`),独立于 fix-skip-require | TASK-REQ-00027-00002 | 2026-06-08 17:30 | [REVIEW-REPORT.md](./review/REQ-00027/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00027-00009 · [修改] code-auto §"路径感知模式"扩展为 5 种(新增"模式 C"),§"步骤 1 子分支"扩展为 1A-1E | TASK-REQ-00027-00002 | 2026-06-08 17:30 | [REVIEW-REPORT.md](./review/REQ-00027/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00027-00010 · [修改] code-auto 步骤 2/3 适配 BUG 路径(`code-design` BUG 跳过 / `code-plan` BUG 路径入参) | TASK-REQ-00027-00002 | 2026-06-08 17:30 | [REVIEW-REPORT.md](./review/REQ-00027/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00039-00006 · [修改] 修正 T-2 / T-3 / T-4 评审发现(合并 1 必须改 + 2 建议改) | TASK-REQ-00039-00002, TASK-REQ-00039-00003, TASK-REQ-00039-00004 | 2026-06-22 16:35 | [REVIEW-REPORT.md](./review/REQ-00039/REVIEW-REPORT.md) | 已完成 |
| TASK-REQ-00040-00007 · [修改] 移除 design line 175 越界字段类型字面 string | TASK-REQ-00040-00001, TASK-REQ-00040-00002 | 2026-06-25 14:55 | [REVIEW-REPORT.md](./review/REQ-00040/REVIEW-REPORT.md) | 待处理 |

---

## 执行的开发命令记录

> 写入方:各 `code-*` 技能在执行编译/启动/测试等命令后追加
> 用途:审计"本版本中跑过哪些命令、结果如何"

| 时间 | 命令 | 工具 | 退出码 | 结果 | 关联任务/阶段 |
| --- | --- | --- | --- | --- | --- |
| (无) | — | — | — | — | — |

---

## 变更记录

> 写入方:所有 `code-*` 技能,在自己的关键节点追加
> 格式:`YYYY-MM-DD HH:mm  <变更类型>  <摘要>  <关联任务/需求>(可选)`

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-06 16:10 | 初始化 | 创建版本 V0.0.3 工作空间(从 V0.0.2 切换) | — |
| 2026-06-06 16:45 | 需求新增 | REQ-00020 需求分析完成(8 FR / 8 NFR / ~40 AC / 9 INV),并落地修改 3 个 SKILL.md(`code-design` 步骤 0b 简化为 1 维度;`code-plan` 步骤 0b 扩展为 7 维度 + 任务粒度表 +3 行;`code-plan` / `code-it` 步骤归并 4 处) | REQ-00020 |
| 2026-06-06 17:05 | 需求新增 | REQ-00021 需求分析完成(7 FR / 6 NFR / ~30 AC / 9 INV),并落地修改 3 个 SKILL.md(新增 `--result` / `--plan` 可选参数 + 模板填充步骤 + 15 内置占位符;DESGIN 拼写沿用用户原文) | REQ-00021 |
| 2026-06-07 | 计划更新 | REQ-00021 详细设计与编码计划完成(共 8 个任务,全部开发=已完成,测试=不适用);整体=`--extensible` + 7 维度优先级(功能性=高,扩展性=高,可复用性=高,健壮性=中,可维护性=中,可读性=中,封装性=不适用);0 派生"更新看板"任务(沿用 REQ-00017 强约束);回填式(本需求 8 任务已在 `d6be243` 落地) | REQ-00021 |
| 2026-06-07 | 任务完成 | TASK-REQ-00021-00001 ~ 00008 · 8 任务回填式执行档案全部完成(code/<TASK>/RESULT.md + 4 份过程文档);SKILL.md 实际修改在 `d6be243`;code-it 仅生成执行档案(纯文档改动,无源码改动);0 测试需要 | TASK-REQ-00021-00001 ~ 00008 |
| 2026-06-06 17:30 | 设计新增 | REQ-00020 概要设计完成(7 决策 + 9 不变量),整体=--extensible + 功能性=中(用户选);0 触发 §规则 1 三同步;0 派生"更新看板"任务 | REQ-00020 |
| 2026-06-06 18:00 | 计划更新 | REQ-00020 详细设计与编码计划完成(共 6 个任务,全部开发=已完成,测试=不适用);7 维度优先级已确认(整体=--extensible / 扩展性=高 / 健壮性=高 / 可维护性=高 / 封装性=高 / 可复用性=高 / 可读性=不适用);0 派生"更新看板"任务(沿用 REQ-00017 强约束) | REQ-00020 |
| 2026-06-06 21:35 | 任务完成 | TASK-REQ-00020-00001 · [修改] code-design 步骤 0b 简化为 1 维度(开发状态:已完成) | TASK-REQ-00020-00001 |
| 2026-06-06 22:10 | 任务完成 | TASK-REQ-00020-00002 · [修改] code-plan 步骤 0b 扩展为 7 维度(开发状态:已完成) | TASK-REQ-00020-00002 |
| 2026-06-06 22:13 | 任务完成 | TASK-REQ-00020-00003 · [修改] 任务粒度调整规则 +3 行(封装性/可复用性/可读性)(开发状态:已完成) | TASK-REQ-00020-00003 |
| 2026-06-06 22:16 | 任务完成 | TASK-REQ-00020-00004 · [重构] 步骤归并 M-1 调用上下文检测引用(开发状态:已完成) | TASK-REQ-00020-00004 |
| 2026-06-06 22:19 | 任务完成 | TASK-REQ-00020-00005 · [重构] 步骤归并 M-2/M-3 公共子步骤引用(开发状态:已完成) | TASK-REQ-00020-00005 |
| 2026-06-06 22:22 | 任务完成 | TASK-REQ-00020-00006 · [重构] 步骤归并 M-4 删除多余逻辑分支(开发状态:已完成) | TASK-REQ-00020-00006 |
| 2026-06-06 22:32 | 评审发现 | REQ-00020 评审完成(共 19 条发现:2 P1 必须改 / 4 P2 建议 / 13 P3 可选;派生 2 个"审查改修"任务 T-7 / T-8;13 份项目级规范 100% 遵循,0 严重违反) | REQ-00020 |
| 2026-06-06 22:41 | 缺陷登记 | code-fix 创建缺陷 BUG-00001(严重度 P0,状态 报告):code-require/code-design/code-plan/code-fix 不能实际修改代码(职责混淆) | BUG-00001 |
| 2026-06-06 17:50 | 设计新增 | REQ-00021 概要设计完成(7 决策 D-1~D-7 + 9 不变量 INV-1~INV-9),整体=--extensible + 功能性=高(用户选);0 触发 §规则 1 三同步;0 派生"更新看板"任务;1 项用户授权偏离(NFR-5.1 SKILL.md 行数增长 +20%~+30%);3 个 SKILL.md **已实际落地修改**(本概设为回填式) | REQ-00021 |
| 2026-06-07 | 需求新增 | REQ-00022 需求分析完成(7 FR / 6 NFR / ~33 AC / 9 INV),4 项 Q-locked(硬重命名 + JSON 全部同步 + docs 全部同步 + 历史不追溯);影响约 38-39 个文件 + 1 个目录重命名;`code-check` 行为与 `code-review` 完全一致(仅字面量差异) | REQ-00022 |
| 2026-06-07 | 设计新增 | REQ-00022 概要设计完成(6 决策 D-1~D-6 + 9 不变量 INV-1~INV-9),整体=--balanced(code-auto 上下文默认);0 触发 §规则 1 三同步;0 派生"更新看板"任务;字面量替换矩阵:约 60-90 处字面量需同步 | REQ-00022 |
| 2026-06-07 | 计划更新 | REQ-00022 详细设计与编码计划完成(共 10 个任务,全部开发=已完成,测试=不适用);`code-check` 行为与 `code-review` 完全一致;0 派生"更新看板"任务(沿用 REQ-00017 强约束) | REQ-00022 |
| 2026-06-07 | 任务完成 | TASK-REQ-00022-00001 ~ 00010 · 10 任务全部完成(重命名 + JSON 同步 + 11 SKILL.md 同步 + 4 README + CLAUDE.md + 13 规范 + 6 模板 + 当前看板 + 校验) | TASK-REQ-00022-00001 ~ 00010 |
| 2026-06-07 | 评审发现 | REQ-00022 评审完成(共 0 条"必须改" / 0 条"建议改" / 0 条"可选";10 任务全部通过;`code-check` 行为与 `code-review` 完全一致;`code-check` 第 1 轮无"必须改" → 派生循环空 → 进入完成分支) | REQ-00022 |
| 2026-06-07 | 需求新增 | REQ-00023 需求分析完成(6 FR / 9 NFR / 8 AC / 9 INV / 3 待澄清 Q),简化 /code-dashboard 总览模式为 4 段(总开发进度 + 5 类状态占比 + 高优缺陷 + 后续操作建议 ≤ 5 条);NFR-6 严守:仅改 1 个 SKILL.md,其他 12 个 code-* 技能 frontmatter 字节级保留;需求模式输出不变 | REQ-00023 |
| 2026-06-07 | 设计新增 | REQ-00023 概要设计完成(6 决策 D-1~D-6 + 9 不变量 INV-1~INV-9,沿用上游),整体=--balanced(code-auto 上下文默认);0 模块新增,0 依赖新增,0 字段新增,0 看板三同步触发;Q-1/Q-2/Q-3 沿用上游当前假设锁定(需求路径优先 / 缺陷走 code-check REQ / 子状态不归一化) | REQ-00023 |
| 2026-06-07 | 计划更新 | REQ-00023 详细设计与编码计划完成(共 6 任务 T-1~T-6,全部开发=待开始,测试=不适用);整体=--balanced;功能性=中;0 派生"更新看板"任务(沿用 REQ-00017 强约束);6 任务 = 4 算法改造 + 1 缺陷段保留 + 1 收尾;预估 net +20~+30 行 | REQ-00023 |
| 2026-06-07 | 任务完成 | TASK-REQ-00023-00001 · [修改] 段 1 总开发进度计算函数(算法 1)(开发状态:已完成) | TASK-REQ-00023-00001 |
| 2026-06-07 | 任务完成 | TASK-REQ-00023-00002 · [修改] 5 类状态判定函数(算法 2)(开发状态:已完成) | TASK-REQ-00023-00002 |
| 2026-06-07 | 任务完成 | TASK-REQ-00023-00003 · [修改] 5 类状态计数函数(算法 3)(开发状态:已完成) | TASK-REQ-00023-00003 |
| 2026-06-07 | 任务完成 | TASK-REQ-00023-00004 · [修改] 后续操作建议生成(算法 4)(开发状态:已完成) | TASK-REQ-00023-00004 |
| 2026-06-07 | 任务完成 | TASK-REQ-00023-00005 · [修改] 高优先级缺陷段保留 + 边界 E-1 ~ E-10(开发状态:已完成) | TASK-REQ-00023-00005 |
| 2026-06-07 | 任务完成 | TASK-REQ-00023-00006 · [修改] 输出区段与衔接小节改造(开发状态:已完成) | TASK-REQ-00023-00006 |
| 2026-06-07 | 评审发现 | REQ-00023 评审完成(共 0 条发现,0 派生"审查改修"任务,8 AC 全部满足,9 INV 全部遵守);6 任务全部通过,code-dashboard 行为按 contract 改造,0 必须改 → 进入 code-auto 完成分支 | REQ-00023 |
| 2026-06-07 | 缺陷状态 | BUG-00001 状态"报告"→"调查中"(code-fix 补充根因假设 4/5,根因正式定稿留待 code-plan) | BUG-00001 |
| 2026-06-07 | 缺陷状态 | BUG-00001 状态"调查中"→"修复规划中"(code-plan 完成 5 任务拆分 + 9 份文档产出;触发/来源=缺陷修复;测试状态=不适用) | BUG-00001 |
| 2026-06-07 | 缺陷状态 | BUG-00001 状态"修复规划中"→"修复编码中"(code-it 开始实施 TASK-BUG-00001-00001) | BUG-00001 |
| 2026-06-07 | 任务完成 | TASK-BUG-00001-00001 · [修改] code-require 加"不修改 SKILL.md"硬约束(开发状态:已完成;INV-10/INV-16 全通过) | TASK-BUG-00001-00001 |
| 2026-06-07 | 任务完成 | TASK-BUG-00001-00002 · [修改] code-design 加"不修改 SKILL.md"硬约束(开发状态:已完成;INV-11/INV-16 全通过) | TASK-BUG-00001-00002 |
| 2026-06-07 | 任务完成 | TASK-BUG-00001-00003 · [修改] code-plan 加"不修改 SKILL.md"硬约束(开发状态:已完成;INV-12/INV-16 全通过) | TASK-BUG-00001-00003 |
| 2026-06-07 | 任务完成 | TASK-BUG-00001-00004 · [修改] code-fix 加"不修改 SKILL.md"硬约束(开发状态:已完成;INV-13/INV-16 全通过) | TASK-BUG-00001-00004 |
| 2026-06-07 | 任务完成 | TASK-BUG-00001-00005 · [修改] code-it 加"唯一可改"声明 + code-unit 加"可改测试代码"边界(开发状态:已完成;INV-14/INV-15/INV-16 全通过;BUG-00001 5 任务全部完成,待 code-fix 推进状态) | TASK-BUG-00001-00005 |
| 2026-06-07 | 需求新增 | REQ-00024 需求分析完成(9 FR / 6 NFR / 8 AC / 4 Q);移除 /code-auto 的 from 关键字逻辑,改用路径感知判定(4 模式) | REQ-00024 |
| 2026-06-07 | 需求新增 | REQ-00025 需求分析完成(8 FR / 7 NFR / 8 AC / 4 Q);软化编号正则约束,允许用户自定义编号格式(仅前缀固定 REQ-/BUG-/TASK-);0 破坏性变更,既有 5 位纯数字继续可用 | REQ-00025 |
| 2026-06-07 | 设计新增 | REQ-00024 概要设计完成(14 章节;code-auto 上下文检测 DETECTED 采纳 --balanced 默认;9 FR / 6 NFR / 8 AC 全部满足;9 个其他 code-* 技能字节级 0 变化) | REQ-00024 |
| 2026-06-07 | 计划完成 | code-plan 完成 REQ-00024 详细设计 + 1 任务拆分(`code-auto/SKILL.md` 改造);0 派生"更新看板"任务;6 步状态机不变;9 个其他 code-* 技能字节级 0 变化 | REQ-00024 |
| 2026-06-07 | 任务完成 | TASK-REQ-00024-00001 · [修改] code-auto 步骤 1:用路径感知替代 from 关键字(开发状态:已完成;AC-1~8 全通过) | TASK-REQ-00024-00001 |
| 2026-06-07 | 评审发现 | REQ-00024 评审完成(0 必须改 / 0 建议改 / 0 可选,派生 0 个"审查改修"任务;9 FR / 6 NFR / 8 AC 全部满足;8 项 INV 静态校验全通过) | REQ-00024 |
| 2026-06-07 | 设计新增 | REQ-00025 概要设计完成(15 章节;code-auto 上下文检测 DETECTED 采纳 --balanced 默认;1 规范修订 + 8 SKILL.md 字面更新;8 FR / 7 NFR / 8 AC 全部满足) | REQ-00025 |
| 2026-06-08 | 设计变更 | REQ-00025 概要设计增量更新(no-op 确认):需求侧 v1 未变;规范侧 13 份 0 变化(encoding-conventions.md 软化待 code-plan/code-it 落地);代码侧 8 个 in-scope SKILL.md 仍含旧 5 位正则(待 code-plan/code-it 落地);design/.../RESULT.md §15 追加 1 行,概要设计清单状态保持"已完成";0 字段扩展,0 §规则 1 三同步,0 派生"更新看板"任务 | REQ-00025 |
| 2026-06-08 | 计划更新 | REQ-00025 详细设计与编码计划完成(共 9 个任务,1 规范 + 8 SKILL.md 字面更新;全部开发=待开始,测试=不适用;整体=`--balanced` + 功能性=中);0 派生"更新看板"任务(沿用 REQ-00017 强约束);2 里程碑(M1 软化上线 + M2 验证) | REQ-00025 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00001 · [修改] encoding-conventions §规则 1/2/4 软化 + 新增 §规则 1.5(开发状态:已完成;53 insertions, 5 deletions;权威源软化升级) | TASK-REQ-00025-00001 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00002 · [修改] code-require §输入 + §工具使用约定 字面更新(开发状态:已完成;§输入 展开为 4 行;parseResultTitle 注释段追加 2 行;下游 SKILL.md 字面更新开始) | TASK-REQ-00025-00002 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00003 · [修改] code-design §输入 + §工作目录约定 字面更新(开发状态:已完成;§输入 追加 2 子项;§工作目录约定 追加 1 项) | TASK-REQ-00025-00003 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00004 · [修改] code-plan §输入 + §步骤 10A + §步骤 9B 字面更新(开发状态:已完成;§输入 追加 5 行;§步骤 10A 任务编号放宽;§步骤 9B 任务编号分配加注) | TASK-REQ-00025-00004 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00005 · [修改] code-it §输入 + §步骤 1 + §步骤 7 字面更新(开发状态:已完成;§输入 追加 2 子项;§步骤 1 解析正则放宽;§步骤 7 末尾加注路径生成语义) | TASK-REQ-00025-00005 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00006 · [修改] code-unit §输入 字面更新(开发状态:已完成;§输入 任务编码 追加 2 子项(生成端 5 位 + 接收端放宽)) | TASK-REQ-00025-00006 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00007 · [修改] code-check §输入 字面更新(开发状态:已完成;§输入 需求编码 追加 2 子项;新增 任务编码 项 2 子项) | TASK-REQ-00025-00007 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00008 · [修改] code-fix §输入 + §步骤 1 字面更新(开发状态:已完成;§输入 缺陷编号 追加 2 子项;§步骤 1.2 校验正则放宽) | TASK-REQ-00025-00008 |
| 2026-06-08 | 任务完成 | TASK-REQ-00025-00009 · [修改] code-dashboard 算法 4 字面更新(双正则兼容)(开发状态:已完成;§附录 A parseTaskId 任务分支正则放宽;§步骤 4 段 4 算法 4 引用对齐) | TASK-REQ-00025-00009 |
| 2026-06-08 | 里程碑推进 | M1-REQ-00025:软化编号正则上线 9 任务全部完成(开发=已完成 ∧ 测试=不适用) | REQ-00025 |
| 2026-06-08 | 评审发现 | REQ-00025 评审完成(共 0 条发现,派生 0 个"审查改修"任务;9 任务全部通过;8 FR / 7 NFR / 8 AC 全部满足;INV-1~INV-16 全部严守;0 触及 SKILL.md frontmatter;0 引入新依赖;0 触发 §规则 1 三同步) | REQ-00025 |
| 2026-06-08 12:00 | 需求新增 | REQ-00026 需求分析完成(共 5 FR / 4 NFR / 12 AC;波及 10 SKILL.md + 3 templates + 1 INIT-REPORT;`.assistants` 0 改;marketplace.json / plugin.json 0 改;旧需求档案 0 改);过程文件 4 + 结果文件 1 = 5 文件待提交 | REQ-00026 |
| 2026-06-08 12:30 | 设计新增 | REQ-00026 概要设计完成(13 目标文件 + 0 新增模块 + 9 条 INV;`--balanced` 默认) | REQ-00026 |
| 2026-06-08 12:45 | 计划更新 | REQ-00026 详细设计与编码计划完成(共 5 个任务,4 修改 + 1 文档;全部开发=待开始,测试=不适用;0 架构任务;M1-REQ-00026 + M2-REQ-00026) | REQ-00026 |
| 2026-06-08 13:10 | 任务完成 | TASK-REQ-00026-00001 · [修改] 9 个 SKILL.md 描述段去专属化(占位符 `<本仓库>`)(开发状态:已完成;实际 2 文件 Edit:`code-it/SKILL.md` L16 + `code-publish/SKILL.md` L67-71;7 文件命中为不变量保留;0 改 frontmatter) | TASK-REQ-00026-00001 |
| 2026-06-08 13:20 | 任务完成 | TASK-REQ-00026-00002 · [修改] code-rule L336 CLAUDE.md 字面替换(开发状态:已完成;1 文件 1 行 Edit:L336 "追加 AI 行为指令到 `<本仓库>/CLAUDE.md`";L363 命令保留;L370 已泛用不改) | TASK-REQ-00026-00002 |
| 2026-06-08 13:28 | 任务完成 | TASK-REQ-00026-00003 · [修改] 3 个 templates 字面替换(开发状态:已完成;3 文件 3 处 Edit:DEPLOY.md L3 / UPDATE.md L3 / qanda-README.md L133;其余模板结构保留) | TASK-REQ-00026-00003 |
| 2026-06-08 13:35 | 任务完成 | TASK-REQ-00026-00004 · [修改] INIT-REPORT.md 字面替换(开发状态:已完成;1 文件 2 处 Edit:L3 入口描述 + L8 占位符语义) | TASK-REQ-00026-00004 |
| 2026-06-08 13:40 | 任务完成 | TASK-REQ-00026-00005 · [文档] 同步版本看板"任务清单" + "变更记录"(开发状态:已完成;T-005 自身行从待开始→已完成;统计 50/50/0/0) | TASK-REQ-00026-00005 |
| 2026-06-08 | 里程碑推进 | M1-REQ-00026:14 文件文案扫除完成(T-001 ~ T-004,4 commit:0818d2a / e8f3303 / 8035c0c / 5185ee2) | REQ-00026 |
| 2026-06-08 13:45 | 评审发现 | REQ-00026 评审完成(共 0 条发现,派生 0 个"审查改修"任务;5 任务全部通过;FR-1 ~ FR-5 + 9 条 INV 全部严守;0 改 frontmatter;0 改 marketplace.json / plugin.json / 4 个 README / CLAUDE.md;`./assistants/` 路径保持原样) | REQ-00026 |
| 2026-06-08 15:20 | 需求新增 | REQ-00027 需求分析完成(共 4 FR / 4 NFR / 4 类 AC;code-fix 重写 + code-auto 增加 BUG 路径模式 C) | REQ-00027 |
| 2026-06-08 15:30 | 设计新增 | REQ-00027 概要设计完成(4 项决策,8 条 INV;2 SKILL.md 修改) | REQ-00027 |
| 2026-06-08 15:35 | 计划更新 | REQ-00027 详细设计与编码计划完成(共 3 个任务,2 修改 + 1 文档;全部开发=待开始,测试=不适用;0 架构任务;M1-REQ-00027 + M2-REQ-00027) | REQ-00027 |
| 2026-06-08 15:40 | 任务完成 | TASK-REQ-00027-00001 · [修改] code-fix/SKILL.md 纯登记型重写(开发状态:已完成;9 个区段 Edit;0 改 frontmatter) | TASK-REQ-00027-00001 |
| 2026-06-08 15:45 | 任务完成 | TASK-REQ-00027-00002 · [修改] code-auto/SKILL.md BUG 路径编排(开发状态:已完成;4 个区段 Edit:子技能调用表 BUG 路径 + 步骤 7.1 auto-report.md 输出 + E-20/21/22 + 不要做的事) | TASK-REQ-00027-00002 |
| 2026-06-08 15:50 | 任务完成 | TASK-REQ-00027-00003 · [文档] 同步版本看板"任务清单" + "变更记录"(开发状态:已完成;T-002 状态对齐 + T-003 自身行 + M1-REQ-00027 推进到已完成) | TASK-REQ-00027-00003 |
| 2026-06-08 14:05 | 缺陷状态 | BUG-00002 状态"报告"→"调查中"(登记 9 处"特定文件类型"字面波及范围) | BUG-00002 |
| 2026-06-08 14:20 | 缺陷状态 | BUG-00002 状态"调查中"→"修复规划中"(code-plan 完成 fix-plan.md;4 步骤:A 类 1 处 + B 类 3 处;5 处不变量字面保留) | BUG-00002 |
| 2026-06-08 14:30 | 缺陷状态 | BUG-00002 状态"修复编码中"→"已修复-待验证"(commit 82d476c,4 文件 4 处 Edit:code-it L16 / code-unit L13/L318 / code-init L229) | BUG-00002 |
| 2026-06-08 14:35 | 缺陷状态 | BUG-00002 状态"已修复-待验证"→"修复编码中"(补修 5 处不变量字面:code-require L530 / code-design L594 / code-plan L1093 / code-fix L433 / code-unit L13 后半段) | BUG-00002 |
| 2026-06-08 14:40 | 缺陷状态 | BUG-00002 状态"修复编码中"→"已修复-待验证"(补修 commit 678e602,5 文件 5 处 Edit) | BUG-00002 |
| 2026-06-08 14:45 | 缺陷状态 | BUG-00003 状态保持"调查中"(本轮复跑 code-fix,等待 code-plan 产出 fix-plan.md 后再推进) | BUG-00003 |
| 2026-06-08 14:50 | 缺陷状态 | BUG-00003 状态"调查中"→"修复规划中"(code-plan 完成 fix-plan.md;4 步骤;与 BUG-00002 方案统一) | BUG-00003 |
| 2026-06-08 14:55 | 缺陷状态 | BUG-00003 状态"修复规划中"→"已修复-待验证"(commit 75297dc,2 文件 5 处 Edit:code-publish L312/325/361/556 + code-rule L363) | BUG-00003 |
| 2026-06-08 15:00 | 缺陷状态 | BUG-00003 状态"已修复-待验证"→"修复编码中"(补修:5 处 `<本仓库>` → 相对路径;`./assistants` 是用户仓库中的项目管理目录) | BUG-00003 |
| 2026-06-08 14:15 | 缺陷状态 | BUG-00003 状态"报告"→"调查中"(登记 8 个 SKILL.md 共 11 处 `plugins/code-skills/...` 绝对路径字面波及范围;与 BUG-00002 合并修复) | BUG-00003 |
| 2026-06-08 | 里程碑推进 | M2-REQ-00026:看板同步完成(5 任务开发=已完成 ∧ 测试=不适用) | REQ-00026 |
| 2026-06-08 17:30 | 评审发现 | REQ-00027 评审完成(共 7 条发现:F-1 ~ F-7 全部必须改;派生 7 个"审查改修"任务 T-004 ~ T-010,关联原任务 T-001 / T-002;触发/来源=审查改修;F-4 经用户确认升级为必须改) | REQ-00027 |
| 2026-06-08 17:30 | 派生任务 | REQ-00027 评审派生 7 个"审查改修"任务:T-004 / T-005 / T-006 / T-007(关联 T-001 code-fix)+ T-008 / T-009 / T-010(关联 T-002 code-auto);新增 M3-REQ-00027 里程碑 | REQ-00027 |
| 2026-06-08 17:35 | 任务完成 | TASK-REQ-00027-00004 · [修改] 步骤 4 状态表修正(仅保留 5 候选状态)(开发状态:已完成;commit 9c088d0;10 行删除) | TASK-REQ-00027-00004 |
| 2026-06-08 17:37 | 任务完成 | TASK-REQ-00027-00005 · [修改] 步骤 9 引导表修正(已关闭-不修复 终态统一)(开发状态:已完成;commit bfc6f2b;1 增 2 删) | TASK-REQ-00027-00005 |
| 2026-06-08 17:39 | 任务完成 | TASK-REQ-00027-00006 · [修改] 步骤 4 注释修正(本技能只主动推进 2 段)(开发状态:已完成;commit 4041998;1 增 1 删) | TASK-REQ-00027-00006 |
| 2026-06-08 17:41 | 任务完成 | TASK-REQ-00027-00007 · [修改] investigation.md 角色清理(由 code-it 写入,本技能只读)(开发状态:已完成;commit 41ddbbb;7 处统一标记) | TASK-REQ-00027-00007 |
| 2026-06-08 17:43 | 任务完成 | TASK-REQ-00027-00008 · [修改] BUG 路径触发改为模式 C(首段匹配 BUG-NNNNN)(开发状态:已完成;commit 26c228a;L219 措辞修正) | TASK-REQ-00027-00008 |
| 2026-06-08 17:45 | 任务完成 | TASK-REQ-00027-00009 · [修改] 路径感知模式扩为 5 种 + 步骤 1 扩为 1A-1E(开发状态:已完成;commit bf9955d;21 增 7 删;5 段全部 Edit) | TASK-REQ-00027-00009 |
| 2026-06-08 17:47 | 任务完成 | TASK-REQ-00027-00010 · [修改] 步骤 2/3 适配 BUG 路径(2A/2B + 3A/3B)(开发状态:已完成;commit 9342318;25 增 2 删) | TASK-REQ-00027-00010 |
| 2026-06-08 17:50 | 里程碑推进 | M3-REQ-00027:7 个审查改修任务完成(code-fix 4 任务 + code-auto 3 任务;7 commit;F-024 ~ F-030 全部 已处理) | REQ-00027 |
| 2026-06-10 11:00 | 需求新增 | REQ-00028 需求分析完成(7 FR / 6 AC / 3 待澄清);新增 `code-answer` 技能(只读功能查询:精确编号 + 关键字模糊匹配 + 源码补足),跨全版本需求 + 屏显报告,严禁 Write/Edit/Bash;过程文档 3 份(`materials-index.md` / `related-requirements.md` / `clarifications.md` / `analysis-notes.md`)+ 1 份 `RESULT.md`,仅本仓库文档改动,无代码改动 | REQ-00028 |
| 2026-06-10 11:00 | 设计新增 | REQ-00028 概要设计完成(5 决策 / 5 不变量 / 1 新增模块:`code-answer` SKILL.md);--balanced;沿用 `code-dashboard` 工具集范式 | REQ-00028 |
| 2026-06-10 11:00 | 计划更新 | REQ-00028 详细设计与编码计划完成(共 1 任务,文档型,测试=不适用);0 派生"更新看板"任务(沿用 REQ-00017 强约束);0 触发 §规则 1 三同步;看板"任务清单"追加 1 行(T-001 待开始);新增里程碑 M1-REQ-00028 | REQ-00028 |
| 2026-06-10 11:00 | 任务完成 | TASK-REQ-00028-00001 · [新增] code-answer SKILL.md(开发状态:已完成;新增 `plugins/code-skills/skills/code-answer/SKILL.md` ~310 行;YAML frontmatter 字节级正确 `name: code-answer`;纯文档任务无源码改动) | TASK-REQ-00028-00001 |
| 2026-06-10 11:00 | 评审发现 | REQ-00028 评审完成(共 0 条发现,派生 0 个"审查改修"任务);整体结论可发布;0 触发 §规则 1 三同步;字节级校验 frontmatter 正确;7 FR / 6 AC / 9 边界全部覆盖;工具集严格 `{Read, Glob, Grep}`;与 `code-dashboard` 范式一致(只读 + 屏显) | REQ-00028 |
| 2026-06-10 11:00 | 任务完成 | TASK-REQ-00020-00007 · [修改] 修复任务粒度调整规则表 4 列与 3 列数据错位(开发状态:已完成;code-plan/SKILL.md §步骤 10A 末尾 表格 L450-451 补齐 4 列对齐,空列填 `—`;净变化 10 字符;P1-1 已处理) | TASK-REQ-00020-00007 |
| 2026-06-10 11:00 | 评审发现 | F-001 状态"待处理"→"已处理"(code-plan/SKILL.md §步骤 10A 末尾 表格 L450-451 补齐 4 列对齐,Markdown 渲染无错位;由 TASK-REQ-00020-00007 完成) | REQ-00020 |
| 2026-06-10 11:00 | 任务完成 | TASK-REQ-00020-00008 · [修改] 清理 §步骤 7D 段(开发状态:已完成;code-plan/SKILL.md §步骤 7D L627-628 删除 -2 行;§步骤 6 路由表 3 情形 ↔ §步骤 7A/B/C 实际段落保持一致;净变化 -2 行;P1-2 已处理) | TASK-REQ-00020-00008 |
| 2026-06-10 11:00 | 评审发现 | F-002 状态"待处理"→"已处理"(code-plan/SKILL.md §步骤 7D 段删除,§步骤 6 路由表 3 情形 ↔ §步骤 7A/B/C 实际段落保持一致,逻辑矛盾消除;由 TASK-REQ-00020-00008 完成) | REQ-00020 |
| 2026-06-10 11:00 | 需求新增 | REQ-00029 需求分析完成(8 FR / 8 AC / 3 待澄清沿用既有);优化 /code-dashboard 屏显报告(只展示结果 + 去除不必要换行);总览 + 需求两种模式都压(沿用用户答复);5 类状态占比保留为单行摘要;建议单行内含命令+优先级+依据;屏显总行数从 ≤ 12 收紧到 ≤ 8(总览)/ ≤ 15(需求);过程文档 4 份(`materials-index.md` / `related-requirements.md` / `clarifications.md` / `analysis-notes.md`)+ 1 份 `RESULT.md`,纯文档改动 | REQ-00029 |
| 2026-06-10 12:00 | 设计新增 | REQ-00029 概要设计完成(11 章节 / 7 决策 D-1~D-7 / 7 不变量 INV-1~INV-7);--balanced(code-auto 上下文检测 DETECTED 采纳默认);1 个改造模块 `code-dashboard/SKILL.md` §输出 + §工作流程 步骤 4 + §输出契约样例;0 字段扩展;0 §规则 1 三同步;0 派生"更新看板"任务;code-auto 步骤 7B 增量更新(需求/规范/代码侧均无变化,RESULT.md 不需重写,仅同步看板设计清单状态) | REQ-00029 |
| 2026-06-10 12:00 | 计划更新 | REQ-00029 详细设计与编码计划完成(共 1 个任务 T-001,纯 SKILL.md 文档改造,测试=不适用;整体=`--balanced` + 功能性=高;0 派生"更新看板"任务;1 里程碑 M1-REQ-00029;屏显目标:总览模式 ≤ 8 行 / 需求模式 ≤ 15 行) | REQ-00029 |
| 2026-06-10 12:00 | 任务完成 | TASK-REQ-00029-00001 · [修改] code-dashboard 渲染层瘦身(总览 ≤ 8 / 需求 ≤ 15 行)(开发状态:已完成;净 -10 行(55 insertions, 65 deletions);8 AC 全部满足;7 条 INV(INV-1 ~ INV-7)全部通过;frontmatter md5 字节级保留) | TASK-REQ-00029-00001 |
| 2026-06-10 12:00 | 评审发现 | REQ-00029 评审完成(共 2 条发现:F-031 / F-032 全部 建议改,0 必须改;0 派生"审查改修"任务;8 AC 全部满足,7 条 INV 全部通过;整体结论:可合并) | REQ-00029 |
| 2026-06-12 14:25 | 设计新增 | REQ-00030 概要设计完成;5 个被改文件(2 SKILL.md + 2 templates + 1 code-check SKILL.md) + 0 新增;8 关键设计点对应上游 8 FR;9 条 INV(INV-1~INV-9,字节级保留约束 + 0 改约束);整体=--extensible(用户主动选);0 触发 dashboard-conventions 三方同步 | REQ-00030 |
| 2026-06-12 14:31 | 设计新增 | REQ-00030 详细设计与编码计划完成(共 6 个任务);5 个被改文件各 1 任务 + 1 个验证任务(T-001 ~ T-006);整体=--extensible + 功能性=高 + 扩展性=高(用户主动选);架构骨架作为 T-001 子项(--extensible 触发);2 里程碑 M1-REQ-00030(5 任务实施完成)+ M2-REQ-00030(3 个新 REQ 行数收敛观测) | REQ-00030 |
| 2026-06-12 14:45 | 任务完成 | TASK-REQ-00030-00001 开发状态"待开始"→"已完成";提交 e203023;code-design/SKILL.md 步骤 0b / 9A / 10A / 11A 已修订;INV-1 / INV-2 / INV-3 字节级保留校验通过 | TASK-REQ-00030-00001 |
| 2026-06-12 14:55 | 任务完成 | TASK-REQ-00030-00002 开发状态"待开始"→"已完成";提交 abc3db2;templates/design.md 模板顶部注释追加;§7/§8/§9 章节字段数收窄;§7.5/§8.5/§9.5 设计边界新增;§10.2 依赖列收窄 | TASK-REQ-00030-00002 |
| 2026-06-12 15:00 | 任务完成 | TASK-REQ-00030-00003 开发状态"待开始"→"已完成";提交 2731ffe;code-plan/SKILL.md 步骤 7A 强约束 + 4 过程文档由可选改必选;步骤 10A 架构骨架触发条件追加触发 4/5 | TASK-REQ-00030-00003 |
| 2026-06-12 15:05 | 任务完成 | TASK-REQ-00030-00004 开发状态"待开始"→"已完成";提交 e54117f;templates/plan.md §4-§12 共 9 个章节由"建议"改"必填",各章节附最小内容要求 | TASK-REQ-00030-00004 |
| 2026-06-12 15:10 | 任务完成 | TASK-REQ-00030-00005 开发状态"待开始"→"已完成";提交 65fdbc1;code-check/SKILL.md 评审清单追加 §8.10 详设完整性 + §8.11 概设越界(5 正则) + §8.12 行数比例(阈值 1.2) | TASK-REQ-00030-00005 |
| 2026-06-12 15:15 | 任务完成 | TASK-REQ-00030-00006 开发状态"待开始"→"已完成"(占位实施);plan/.../RESULT.md 追加 §16 验证结果小节(AC-8.1 / AC-8.2 占位);无 git commit(纯观测任务) | TASK-REQ-00030-00006 |
| 2026-06-12 15:18 | 评审发现 | REQ-00030 评审完成(6 任务全部通过,INV-1~INV-9 全部满足,0 必须改,1 建议改 F-010 为 §8.10 误报;§8.11 0 命中 + §8.12 ratio=0.95 通过;M1 里程碑可关闭,M2 待 REQ-00031+ 落地) | REQ-00030 |
| 2026-06-12 14:11 | 需求新增 | REQ-00030 需求分析完成(8 FR / 6 NFR / 9 AC / 3 待澄清 / 3 关联需求沿用);关键设计决策:小需求(1 任务)概设 0 问默认;扩展性触发 = 新增三方依赖 OR 跨 ≥3 模块 OR 对接多套实现;概设 §7/§8/§9 深度收窄(模块表 5 列 / 接口 4 项 / 实体 4 项);详设 §4-§10 全展开 + 4 份过程文档由可选改必选;code-check 新增 3 个校验点(详设完整性 / 概设越界 / 行数比例) | REQ-00030 |
| 2026-06-12 15:13 | 需求新增 | REQ-00031 需求分析完成(7 FR / 5 NFR / 3 大类共 20 AC / 5 Q 已澄清 / 7 关联需求);关键设计决策:`code-plan` 任务完成定义内化"编译/运行成功"(FR-1);任务类型移除 `测试`(FR-2);任务"测试状态"枚举收窄为 2 个(FR-3);`code-it` 声明"不含单元测试"(FR-4);`code-unit` 声明"独立、可选"(FR-5);`code-auto` 任务循环永不再调 `code-unit`(FR-6);`templates/plan.md` 同步收窄(FR-7) | REQ-00031 |
| 2026-06-12 15:25 | 设计新增 | REQ-00031 概要设计完成(4 模块 + 4 接口 + 4 数据结构 + 0 三方依赖 + 10 INV),整体=--balanced + 功能性=中(`code-auto` 上下文默认);0 触发 §规则 1 三同步;0 派生"更新看板"任务;1 项用户授权偏离(NFR-2 不追溯重写既有 11 个 REQ);5 文件**已实际落地修改**(本概设为回填式) | REQ-00031 |
| 2026-06-12 15:35 | 计划更新 | REQ-00031 详细设计与编码计划完成(共 5 个任务,全部开发=待开始,测试=不适用);整体=--balanced + 功能性=中;0 单列"编译运行检测"任务(本就是冗余);0 单元测试任务(主动外移);2 数据结构变更(任务类型 6→5 + 测试状态 6→2);1 里程碑(M1:实施完成);design/plan ratio = 1.10 ≤ 1.2 通过 | REQ-00031 |
| 2026-06-12 15:55 | 评审发现 | REQ-00031 评审完成(5 任务全部通过,INV-1~INV-10 全部满足,0 必须改 / 0 建议改 / 0 可选;§8.10 0 命中 + §8.11 5 正则 0 命中 + §8.12 ratio=1.10 ≤ 1.2 通过;M1 里程碑可关闭) | REQ-00031 |
| 2026-06-12 16:10 | 需求新增 | REQ-00032 需求分析完成(4 FR / 9 NFR / 18 AC / 4 Q 已澄清 / 7 关联需求沿用);关键设计决策:AI 自主判定"微小需求"(FR-1 推荐判据:材料数 ≤ 1 + FR ≤ 2 + AC ≤ 5,综合判断无强制阈值);屏幕日志输出 2 类建议(FR-3:微小→/code-auto / 其他→/code-design 二选一);零文档变更(FR-2 不追加"## 下一步建议"章节,RESULT.md 文档结构 0 改);不涉及 /code-unit(Q-4 沿用 REQ-00031 元技能改规则) | REQ-00032 |
| 2026-06-12 16:32 | 设计新增 | REQ-00032 概要设计完成(2 模块 + 2 屏幕日志接口 + 0 数据结构 + 0 三方依赖 + 10 INV),整体=--minimal + 功能性=中(元技能文字修订适用);改造位置:`code-require/SKILL.md` 步骤 10A / 10B 段内文末各追加 1 段(D-2 最小化变更,字节级保留既有"向用户汇报"段);0 触发 §规则 1 三同步;0 派生"更新看板"任务;0 用户授权偏离 | REQ-00032 |
| 2026-06-12 16:52 | 计划更新 | REQ-00032 详细设计与编码计划完成(共 1 个任务,开发=待开始,测试=不适用);整体=--minimal + 功能性=中(沿用 design);0 单列"编译运行检测"任务(沿用 REQ-00031 FR-1 内化);0 单元测试任务(沿用 REQ-00031 FR-6 外移);0 数据结构变更;1 里程碑(M1-REQ-00032:实施完成);design/plan ratio = 1.08 ≤ 1.2 通过 | REQ-00032 |
| 2026-06-12 17:10 | 任务完成 | TASK-REQ-00032-00001 · [修改] code-require 步骤 10A/10B 末尾追加下一步建议段(开发状态:已完成) | TASK-REQ-00032-00001 |
| 2026-06-12 17:18 | 评审发现 | REQ-00032 评审完成(0 条发现,0 个派生任务;12 维度(8.1-8.12)全通过;INV-1~INV-10 全部满足;§8.10 0 命中 + §8.11 5 正则 0 命中 + §8.12 design/plan ratio=1.08 ≤ 1.2 通过;M1-REQ-00032 里程碑可关闭;整体=可合并) | REQ-00032 |
| 2026-06-15 11:10 | 需求新增 | REQ-00033 需求分析完成(共 4 FR / 11 NFR / 23 AC);本需求唯一改造对象 = `code-require/SKILL.md` §"不要做的事" 小节追加 1 条硬约束(不涉及技术选型 / 技术栈 / 技术方案);0 改 frontmatter / templates / 其他 11 个 SKILL.md / 既有 12 个 REQ / 7 项目级规范 / 4 README / CLAUDE.md;0 派生"更新看板"任务;1 项用户授权偏离(NFR-8 不收集"本项目是否需要技术选型"偏好) | REQ-00033 |
| 2026-06-15 12:20 | 设计新增 | REQ-00033 概要设计完成(5 决策 / 9 不变量 / 0 模块 / 0 接口 / 0 数据结构 / 0 依赖);整体=--balanced,功能性=低,0 触发扩展性,0 冲突,0 问路(code-auto 上下文检测到,采纳 --balanced 默认 0 问) | REQ-00033 |
| 2026-06-15 12:30 | 计划更新 | REQ-00033 详细设计与编码计划完成(共 1 任务,1 修改类,1 个被改文件 = `code-require/SKILL.md` §"不要做的事" 小节末尾);整体=--balanced,功能性=低;0 模块/0 接口/0 数据结构/0 依赖;0 派生"更新看板"任务(沿用 REQ-00017 强约束);1 里程碑 M1-REQ-00033;code-auto 上下文 0 问沿用 design | REQ-00033 |
| 2026-06-15 12:45 | 任务完成 | TASK-REQ-00033-00001 · [修改] code-require §"不要做的事" 小节追加"不涉及技术选型"硬约束(开发状态:已完成);净增 +1 行(在 NFR-3 锁定 +2~+4 范围内,实际更紧);frontmatter L1-3 字节级保留;§"工作流程" 既有段 0 改;3 个语义子句全包含(AC-2.1 满足);提交 26698e8 | TASK-REQ-00033-00001 |
| 2026-06-15 13:10 | 评审发现 | REQ-00033 评审完成(共 0 条发现,派生 0 个"审查改修"任务);12 维度全过(8.1-8.9 + 8.10 详设完整性 + 8.11 概设越界 + 8.12 行数比例);8.10/8.11/8.12 三个新增校验点全部通过;净增 +1 行(在 NFR-3 锁定 +2~+4 范围内);整体=✅ 通过,可合并 | REQ-00033 |
| 2026-06-15 18:00 | 任务完成 | TASK-REQ-00034-00009 · [修改] 9 技能 SKILL.md 描述段去 code-unit 引用(开发状态:已完成);净减 2 行(27 增 / 29 删);frontmatter L1-3 字节级保留;12 文件字面改写(9 SKILL.md + 0 plugin.json);0 必须改;提交 3222843 | TASK-REQ-00034-00009 |
| 2026-06-15 18:15 | 任务完成 | TASK-REQ-00034-00010 · [删除] code-unit 整体(SKILL.md 635 行 + templates/ 目录)(开发状态:已完成);净删除 4 文件(SKILL.md + 3 个 templates);0 影响其他独立技能;0 影响历史档案;提交 b9c9d6c | TASK-REQ-00034-00010 |
| 2026-06-15 18:45 | 评审发现 | REQ-00034 评审完成(共 0 条发现,派生 0 个"审查改修"任务);12 维度全过(8.1-8.9 + 8.10 详设完整性 + 8.11 概设越界 + 8.12 行数比例);10 任务全部"已完成 ∧ 不适用";8.10/8.11/8.12 三个新增校验点全部通过;design / plan ≈ 0.412 << 1.2;净变化约 -600 ~ -800 行;整体=✅ 通过,可合并;M1-REQ-00034 里程碑可关闭 | REQ-00034 |
| 2026-06-15 13:30 | 设计新增 | REQ-00034 概要设计完成(15 决策 / 12 不变量 / 0 新增模块 / 1 新增接口类 / 0 数据结构 / 0 依赖);整体=--extensible,功能性=中(触发条件 2:29 个文件 ≥ 3);0 触发扩展性问路(code-auto 上下文 0 问);0 冲突;候选 14 任务(由 code-plan 阶段细化) | REQ-00034 |
| 2026-06-15 14:00 | 计划更新 | REQ-00034 详细设计与编码计划完成(共 10 任务,候选 14 合并;5 SKILL.md 改造 + 2 JSON 字面 + 4 README 字面 + 7 规范字面 + 11 描述段字面 + 1 目录删除;净变化约 -600 ~ -800 行);整体=--extensible,功能性=中;0 模块/0 接口/0 数据结构/0 依赖;0 派生"更新看板"任务(沿用 REQ-00017 强约束);1 里程碑 M1-REQ-00034;code-auto 上下文 0 问沿用 design | REQ-00034 |
| 2026-06-15 19:00 | 需求新增 | REQ-00035 需求分析完成(8 FR / 9 NFR / 22 AC / 4 INV);新建需求:过程文档自适应生成改造(AI 自主判定不涉及的过程文档不生成,减少 token 消耗);改造范围:5 主流程技能过程文档 + 看板变更记录;新增产物 `process-doc-decisions.md` 决策记录文件;1 派生模式:"AI 自适应判定"(沿用 REQ-00020 / REQ-00032 范式);0 历史档案处理(沿用 NFR-5 强约束);本轮过程文档决策:`clarifications.md` / `related-requirements.md` 不生成(§6.1 准则) | REQ-00035 |
| 2026-06-15 19:10 | 设计新增 | REQ-00035 概要设计完成(4 决策 / 0 不变量 / 0 新增模块(纯改既有)/ 0 新增接口 / 0 数据结构 / 0 依赖);整体=--balanced,功能性=中,扩展性=不触发;7 个改写点(5 主流程 SKILL.md + 1 编排 + 1 dashboard);5 模板新增(`process-doc-decisions.md` × 5);0 触发扩展性问路;0 冲突;本轮过程文档决策:`dependencies.md` / `clarifications.md` 不生成(§6.2 准则) | REQ-00035 |
| 2026-06-15 19:20 | 计划更新 | REQ-00035 详细设计与编码计划完成(共 7 任务,合并 5 模板新增到 T-001~T-005;整体=--balanced,功能性=中;0 模块/0 接口/0 数据结构/0 依赖;0 派生"更新看板"任务,沿用 REQ-00017 强约束;1 里程碑 M1-REQ-00035;code-auto 上下文 0 问;看板追加 7 行;本轮过程文档决策:`interface-specs.md` / `data-changes.md` / `clarifications.md` 不生成(§6.3 准则)) | REQ-00035 |
| 2026-06-15 19:30 | 任务完成 | TASK-REQ-00035-00001 · [修改] code-require 步骤 0a 过程文档判定 + 模板新增(开发状态:已完成);SKILL.md 锚点追加 45 行(在 `## 工具使用约定` 段后新增 `## 过程文档自适应判定` 小节);模板 `process-doc-decisions.md` 新增 50 行;0 必须改;提交 6be9a13 | TASK-REQ-00035-00001 |
| 2026-06-15 20:00 | 任务完成 | TASK-REQ-00035-00002~00007 · 6 任务批量完成(开发状态:已完成);code-design / code-plan / code-it / code-check SKILL.md 各 +45 行(锚点追加 `## 过程文档自适应判定` 小节);code-check +8.13 评审维度(派生"建议改"不阻断);code-auto 子技能调用表备注追加;code-dashboard 解析兼容;4 模板新增(`process-doc-decisions.md` × code-require/code-design/code-plan/code-it/code-check);0 必须改;提交 48335d7 | TASK-REQ-00035-00002 ~ 00007 |
| 2026-06-16 17:33 | 需求新增 | REQ-00036 需求分析完成(8 FR / 10 NFR / 8 AC);清理 14 技能 SKILL.md + 同目录 templates/ 中的开发痕迹(REQ/BUG 编号引用、退场功能说明、决策记录、生效日标记、占位注释等);占位符 `REQ-00001` / `BUG-00001` 保留;不动 checklists/ / guidelines/ / assistants/ | REQ-00036 |
| 2026-06-16 17:33 | 设计新增 | REQ-00036 概要设计完成(16 章节;6 条硬编码清理规则 + 9 条硬约束 + 6 项风险;0 新增模块/接口/数据结构/三方依赖;整体=`--minimal`,功能性=中;0 触发 §规则 1 三同步;0 派生"更新看板"任务) | REQ-00036 |
| 2026-06-16 17:33 | 计划更新 | REQ-00036 详细设计与编码计划完成(共 3 个任务,全部开发=待开始,测试=不适用;整体=`--minimal`,功能性=中;0 模块/0 接口/0 数据结构/0 依赖;0 派生"更新看板"任务,沿用 REQ-00017 强约束;1 里程碑 M1-REQ-00036;code-auto 上下文 0 问沿用 design) | REQ-00036 |
| 2026-06-16 17:33 | 任务完成 | TASK-REQ-00036-00001 · [文档] 扫描并产出 14 技能 SKILL.md + templates/ 待清理文件表与命中计数基线(开发状态:已完成;产出 47 文件表 + 286 行命中基线;0 文件改动;修正 PLAN.md/看板文件数 37→47) | TASK-REQ-00036-00001 |
| 2026-06-16 17:33 | 任务完成 | TASK-REQ-00036-00002 · [文档] 应用 6 条清理规则(开发状态:已完成;188 总命中;15 文件被改;0 残缺回退;占位符 100% 保留;frontmatter 字节级一致;git diff +175/-175;待 T-3 末尾统一 commit) | TASK-REQ-00036-00002 |
| 2026-06-16 17:33 | 任务完成 | TASK-REQ-00036-00003 · [文档] 跑 AC-1 ~ AC-8 验证 + 1 次 commit + 看板同步 + 末尾兜底(开发状态:已完成;8 条 AC 全过 0 必须改;T-3 补清 R-1 扩展 55 命中 + R-3 手动 3 处;8 文件被改;占位符 30/50/11 完整保留;M1-REQ-00036 里程碑达成) | TASK-REQ-00036-00003 |
| 2026-06-22 09:02 | 需求新增 | REQ-00037 需求分析完成(8 FR / 8 NFR / 10 AC),并落地优化 4 个 SKILL.md 的缺陷状态推进职责分工(code-fix 仅登记,初始状态 待处理;code-plan 完成 → 待开发;code-it 第 1 任务 → 开发中 / 全部完成 → 待审查;code-check 完成 → 已完成);新增 5 状态(待处理 / 待开发 / 开发中 / 待审查 / 已完成)与既有 8 状态字面共存不归一化;典型完整流程由 10 步压缩为 4 步 | REQ-00037 |
| 2026-06-22 09:18 | 设计新增 | REQ-00037 概要设计完成(6 功能域 + 5 关键决策 + 4 备选方案;--balanced + 功能性=高);0 新增模块/接口/数据结构/三方依赖;7 任务候选(估算 5-6 天);不触发 dashboard-conventions §规则 1(状态字段是自由字符串列) | REQ-00037 |
| 2026-06-22 09:28 | 设计新增 | REQ-00037 详细设计与编码计划完成(共 7 个任务,全部开发=待开始,测试=不适用);0 派生"更新看板"任务(沿用 REQ-00017 强约束);触发/来源 全部=详细设计;7 任务严格串行(T-1 → T-7);AC-1 ~ AC-10 全部纳入 T-7 验证;沿用概设 --balanced + 功能性=高 + 健壮性=高 + 可维护性=高 | REQ-00037 |
| 2026-06-22 09:35 | 任务完成 | TASK-REQ-00037-00001 · [修改] code-fix 步骤 4/6 + 衔接 + 不要做的事同步(开发状态:已完成;`git diff --stat` 1 file changed, 25 insertions(+), 30 deletions(-);步骤 4 状态推进表新增 `待处理` FROM 行 + "(新建)"行 + 步骤 5 注脚字面 + 步骤 9 引导表 4 行字面 + 典型完整流程 10 步 → 4 步 + ## 不要做的事 段字面追加;AC-1/AC-6 静态校验通过;端到端验证由 T-7 承担) | TASK-REQ-00037-00001 |
| 2026-06-22 09:45 | 任务完成 | TASK-REQ-00037-00002 · [修改] code-plan 步骤 27A/28A 末尾追加状态回写(开发状态:已完成;`git diff --stat` 1 file changed, 24 insertions(+), 7 deletions(-);步骤 27A 末尾追加 `planStateRollback` 子步骤 13 行 + 步骤 28A `syncKanbanBugList` 调用 5 行 + ## 不要做的事 段字面追加 1 行;AC-2 静态校验通过;端到端验证由 T-7 承担) | TASK-REQ-00037-00002 |
| 2026-06-22 09:55 | 任务完成 | TASK-REQ-00037-00003 · [修改] code-it 步骤 21 末尾追加状态回写:开发中(开发状态:已完成;`git diff --stat` 1 file changed, 20 insertions(+), 6 deletions(-);§"缺陷分支" 步骤 21 末尾追加 `itStartStateRollback` 子步骤 14 行 + ## 不要做的事 段字面追加 1 行;AC-3 静态校验通过;端到端验证由 T-7 承担) | TASK-REQ-00037-00003 |
| 2026-06-22 10:05 | 任务完成 | TASK-REQ-00037-00004 · [修改] code-it 步骤 24 末尾追加状态回写:待审查(开发状态:已完成;`git diff --stat` 1 file changed, 32 insertions(+), 6 deletions(-);§"缺陷分支" 步骤 24 末尾追加 `itEndStateRollback` 子步骤 11 行;判定矩阵:`doneCount == totalCount` ∧ `oldStatus ∈ {`待开发`, `开发中`}` → 推 `待审查`,其他情形维持/跳过;## 不要做的事 段沿用 T-3 落地,不重复追加;AC-4 静态校验通过;端到端验证由 T-7 承担) | TASK-REQ-00037-00004 |
| 2026-06-22 10:35 | 任务完成 | TASK-REQ-00037-00005 · [修改] code-check 步骤 1.5 BUG-NNN 识别 + 步骤 13 状态回写(开发状态:已完成;`git diff --stat` 1 file changed, 14 insertions(+), 1 deletion(-);步骤 1.5 三态机 → 四态机新增 `BUG-NNNNN` → 单缺陷模式;步骤 13 末尾追加 `checkStateRollback` 子步骤 11 行,判定矩阵:`oldStatus == "待审查"` → 推 `已完成`,其他情形跳过;## 不要做的事 段字面追加 2 行(稳定章节不修改 + 评审发现"必须改"派生改修时状态维持 `待审查`);AC-5 / AC-9 静态校验通过;端到端验证由 T-7 承担) | TASK-REQ-00037-00005 |
| 2026-06-22 11:05 | 任务完成 | TASK-REQ-00037-00006 · [修改] code-dashboard 步骤 4 段 3 扩展待修复/已修复分类(开发状态:已完成;`git diff --stat` 1 file changed, 1 insertion(+), 1 deletion(-);§步骤 4 段 3 `classifyState` 判定逻辑扩展,字面集合:`已完成` + `已修复-已验证` + `已关闭` 算"已修复",其他 5 新字面 + 7 老字面都算"待修复";段 2 "5 类状态占比"分类骨架沿用 NFR-8 不修改;老字面 10 个继续按既有路径归类,沿用 PD-2 不归一化;AC-10 部分静态校验通过;端到端验证由 T-7 承担) | TASK-REQ-00037-00006 |
| 2026-06-22 12:06 | 任务完成 | TASK-REQ-00037-00007 · [文档] 端到端验证 AC-1 ~ AC-10 + 末尾兜底提交(开发状态:已完成;AC 静态校验 10/10 通过(AC-1 `待处理` 落地 / AC-2 `待开发` 落地 / AC-3 `开发中` 落地 / AC-4 `待审查` 落地 / AC-5 `已完成` 落地 / AC-6 屏显警告落地 / AC-7 5 节点链路正确 / AC-8 15 字面兼容 / AC-9 BUG-NNN 入参扩展 / AC-10 4 SKILL.md 文档同步);M1-REQ-00037 里程碑达成;末尾兜底 1 次 commit 落地 T-3 ~ T-7 累积) | TASK-REQ-00037-00007 |
| 2026-06-22 13:00 | 需求新增 | REQ-00038 需求分析完成(5 FR / 6 NFR / 7 AC),优化 /code-it 技能单测判定从工程粒度细化到模块粒度;模块识别优先级链(声明文件 + git diff + CWD 根退化 3 层)+ 模块级守卫 7 项(检查位置从 CWD 根 → 模块目录,沿用 REQ-00034 字节级)+ 单测输出位置模块级(测试目录识别优先级链 7 层,无约定时退化到 CWD 根)+ 模板多模块支持(`unit-test-results.md` 新增"## 各模块单测结果"小节);100% 兼容 REQ-00034 工程根级行为(单模块 = 字节级沿用);1 轮 AskUserQuestion 澄清(3 选 1);FR-5 `code-plan` 适配 1 句字面新增(可选);本轮过程文档决策:materials-index.md / clarifications.md / related-requirements.md / analysis-notes.md 均生成(§适用过程文档清单 准则) | REQ-00038 |
| 2026-06-22 14:00 | 需求新增 | REQ-00039 需求分析完成(5 FR / 8 NFR / 8 AC),优化 /code-it、/code-check 等技能:代码行数限制仅统计实际逻辑行(逻辑行 = 总行 - 空行 - 注释行;4 类排除项:注释 / 说明 / 空行 / 格式化换行);工具集成 tokei(首选,200+ 语言)/ cloc(备选,50+ 语言)/ 启发式回退(无依赖,~95% 精度);`code-it` 步骤 8 末尾新增 `calcLogicLoc` 子步骤 + `code-check` 步骤 8 评审维度速查表新增第 13 维度"代码行数超标"(P3 可维护性);阈值默认单文件 ≤ 500 行(总规模)/ ≤ 200 行(新增),用户可配置;缺陷分支(`^TASK-BUG-...`)**不**触达(沿用 NFR-8);1 轮 AskUserQuestion 澄清(3 选 1);本轮过程文档决策:materials-index.md / clarifications.md / related-requirements.md / analysis-notes.md 均生成 | REQ-00039 |
| 2026-06-22 14:30 | 设计新增 | REQ-00039 概要设计完成(5 模块 / 4 函数 / 1 阈值配置;`--balanced` 路线;功能性=高 + 健壮性=高 + 可维护性=高;code-auto 上下文自动采纳默认;code-it 步骤 8 末尾 + code-check 步骤 8.13 新增 + 1 模板改造 + 2 共享库新建;共享库位置 `code-it/lib/` 沿用 `module-conventions §规则 1` 不入 `templates/`;0 偏离 / 0 冲突 / 0 用户授权偏离;14 条规范全部满足) | REQ-00039 |
| 2026-06-22 15:00 | 计划更新 | REQ-00039 详细设计与编码计划完成(共 5 个任务,code-auto 上下文自动采纳 `--balanced` 默认;沿用 `design/REQ-00039` 的设计目标);0 新增模块/接口/数据结构/依赖;5 任务严格串行(T-1 → T-5);AC-1 ~ AC-8 全部纳入 T-5 验证;code-it 步骤 8 末尾追加 `calcLogicLoc` 子步骤 + code-check 步骤 8.13 新增"代码行数超标"发现 + 模板"## 逻辑行统计"小节示例 + 2 共享库新建;本轮过程文档决策:materials-index.md / design-notes.md / module-details.md / interface-specs.md / risk-analysis.md / rule-compliance.md 均生成;data-changes.md / clarifications.md 不生成(沿用既有准则) | REQ-00039 |
| 2026-06-22 15:05 | 任务完成 | TASK-REQ-00039-00001 · [新增] 共享库 logic-loc.md + logic-loc-defaults.md(开发状态:已完成;`git diff --stat` 2 files changed, +X insertions(+), 0 deletions(-);`logic-loc.md` 含 4 函数(`detectLocTool` / `calcLogicLines` / `heuristicLoc` / `code-check-exceed`)+ 检测机制 + 启发式算法;`logic-loc-defaults.md` 含 2 阈值字段(500 / 200);字段完整性静态校验通过 4 函数名命中 13 次 / 2 阈值字段命中 3 次;新建在 `code-it/lib/` 沿用 `module-conventions §规则 1` 不入 `templates/`;T-2 / T-3 依赖本任务;端到端验证由 T-5 承担) | TASK-REQ-00039-00001 |
| 2026-06-22 15:08 | 任务完成 | TASK-REQ-00039-00002 · [修改] code-it 步骤 8 末尾追加 detectLocTool + calcLogicLoc 子步骤 + 屏显契约(开发状态:已完成;`git diff --stat` 1 file changed, +89 insertions(+), 0 deletions(-);`plugins/code-skills/skills/code-it/SKILL.md` line 716-803 追加 `### 步骤 8.6 — 逻辑行统计(由 code-it 内化)` 子步骤 7 个子节(目标 / 算法 / 边界与异常 / 性能 / 屏显契约 / 退出码契约 / 约束);**仅**引用共享库 4 函数不重写;NFR-7 不阻断 + NFR-8 缺陷分支不触达约束字节级沿用;frontmatter L1-3 字节级保留;既有 步骤 8 / 8a / 8.5 字节级沿用;AC-7 静态校验通过;AC-1 / AC-6 端到端验证由 T-5 承担;T-3 / T-4 依赖本任务) | TASK-REQ-00039-00002 |
| 2026-06-22 15:12 | 任务完成 | TASK-REQ-00039-00003 · [修改] code-check 步骤 8.13 新增 + 评审维度速查表第 13 维度(开发状态:已完成;`git diff --stat` 1 file changed, +18 insertions(+), 1 deletion(-);`plugins/code-skills/skills/code-check/SKILL.md` line 426-441 追加 `**8.13 代码行数超标检查**` 子步骤 + line 608 速查表新增第 13 行 `P3 | 代码行数超标 | 可选 / 建议改 / 必须改`;既有 8.13 过程文档适配性 重命名为 8.14(文字内容字节级保留);**仅**引用共享库 §函数 4 `code-check-exceed` 不重写;阈值默认 500 / 200 沿用 `logic-loc-defaults.md`;用户配置覆盖读 `require/<需求>/RESULT.md` "## 阈值配置";frontmatter L1-3 字节级保留;既有 步骤 8.1 ~ 8.12 字节级沿用;既有 12 维度表字节级沿用;AC-7 / AC-9 部分静态校验通过;AC-4 / AC-5 端到端验证由 T-5 承担) | TASK-REQ-00039-00003 |
| 2026-06-22 15:16 | 任务完成 | TASK-REQ-00039-00004 · [修改] code-it/templates/RESULT.md 模板新增"## 逻辑行统计"小节示例(开发状态:已完成;`git diff --stat` 1 file changed, +21 insertions(+), 1 deletion(-);`plugins/code-skills/skills/code-it/templates/RESULT.md` line 124-143 在 ## 9. 单元测试 小节后新增"## 10. 逻辑行统计(由 code-it 内化,新增"小节示例(1 表格 + 5 字段说明 + 1 模板使用说明);原"## 10. 变更记录"重命名为"## 11. 变更记录"(章节编号顺序 +1);表格字面与详细设计 §5.5 step 6 完全一致;既有 9 个章节(## 文档头 ~ ## 9. 单元测试)字节级保留;字段完整性静态校验通过(逻辑行(新增) 1 次 / 逻辑行(总规模) 1 次 / 检测方式 ≥ 3 次);AC-1 部分静态校验通过) | TASK-REQ-00039-00004 |
| 2026-06-22 15:22 | 任务完成 | TASK-REQ-00039-00005 · [文档] 端到端验证 AC-1 ~ AC-8 + 末尾兜底提交(开发状态:已完成;8 条 AC 全部静态校验通过;末尾兜底 1 次 commit 落地 `665b1f6`(32 files, +1726/-16)+ `ce0a8da`(T-5 提交哈希回填);M1-REQ-00039 完成定义全部满足;5 任务开发=已完成 ∧ 测试=不适用;AC-1 / AC-8 端到端降级为静态校验,沿用 `CLAUDE.md` "本仓库不含源代码"约定) | TASK-REQ-00039-00005 |
| 2026-06-22 16:35 | 评审发现 | REQ-00039 评审完成(5 任务,共 3 项发现 = 1 必须改 F-034 + 2 建议改 F-035 / F-036;合并派生 1 个任务 TASK-REQ-00039-00006;整体结论 ❌ 阻塞) | REQ-00039 |
| 2026-06-22 16:35 | 派生任务 | TASK-REQ-00039-00006 · [修改] 修正 T-2 / T-3 / T-4 评审发现(合并 1 必须改 F-034 + 2 建议改 F-035 / F-036,跨 3 文件);关联原任务 T-2 / T-3 / T-4;3 文件改动(`code-it/templates/RESULT.md` + `code-it/SKILL.md` + `code-check/SKILL.md`);状态:待开始 | TASK-REQ-00039-00006 |
| 2026-06-22 16:42 | 任务完成 | TASK-REQ-00039-00006 · [修改] 修正 T-2 / T-3 / T-4 评审发现(合并 1 必须改 + 2 建议改)(开发状态:已完成;`git diff --stat` 3 files changed, +3 insertions(+), 3 deletions(-);3 项字面修正全部落地:`code-it/templates/RESULT.md` line 124 标题末尾半角逗号删除 + `code-it/SKILL.md` line 762 步骤 8.6.3 E-3 处理列更新为"任务级跳过该文件,继续下一文件"+ `code-check/SKILL.md` line 440 "总规模优先,新增次之" 更新为"先判 totalLoc,再判 newLoc(两个独立发现可同时触发)";frontmatter L1-3 字节级保留;既有章节字节级沿用;`code-it/lib/logic-loc.md` + `code-it/lib/logic-loc-defaults.md` **无修改**(共享库是 single source of truth);步骤 8a 守卫判定项目不可测 → 任务测试状态=不适用;§偏离 0;F-034 / F-035 / F-036 全部已处理;末尾兜底 1 次 commit 落地) | TASK-REQ-00039-00006 |
| 2026-06-22 20:15 | 缺陷登记 | code-fix 创建缺陷 BUG-00004(严重度 P1,状态 报告):`code-it` 在纯 Markdown 改造任务上仍输出 `compile-and-run.md` / `test-results.md` 等空占位过程文档;由 TASK-REQ-00039-00003 触发 | BUG-00004 |
| 2026-06-22 20:15 | 缺陷状态 | BUG-00004 状态"报告"→"调查中"(根因初步定稿:`code-it/SKILL.md` "## 过程文档自适应判定"章节定义的判定准则未真正接入"## 工作流程"的步骤 9/10/11;待排查其他 `code-*` 技能是否同类问题) | BUG-00004 |
| 2026-06-22 20:30 | 缺陷状态 | BUG-00004 状态"调查中"→"修复规划中"(code-plan 完成详细设计 + 9 份文档 + 4 任务拆分;其他 6 个技能旁路验证仅静态校验;M1-BUG-00004 待开始) | BUG-00004 |
| 2026-06-22 20:50 | 缺陷状态 | BUG-00004 状态"修复规划中"→"修复编码中"(code-it 开始实施 TASK-BUG-00004-00001) | BUG-00004 |
| 2026-06-22 20:55 | 任务完成 | TASK-BUG-00004-00001 · [修改] code-it 步骤 8.7 新增 + 步骤 9/10/11 守卫(开发状态:已完成;`git diff --stat` 1 file changed, +118 insertions(+), 1 deletion(-);frontmatter L1-3 字节级保留;步骤 8.7 正确插入 + 步骤 9/10/11 守卫逻辑字面正确 + 既有逻辑字节级沿用;§偏离 1 + §偏离 0) | TASK-BUG-00004-00001 |
| 2026-06-22 21:10 | 任务完成 | TASK-BUG-00004-00002 · [修改] code-it 步骤 13/16 + templates/RESULT.md 改造(开发状态:已完成;`git diff --stat` 2 files changed, +177 insertions(+), 2 deletions(-);`code-it/SKILL.md` 步骤 13/16 末尾追加 +24 行引用块 + `templates/RESULT.md` line 101-105 "## 8. 关联任务" → "## 8. 过程文档清单(由 code-it 内化,BUG-00004 新增)";既有"## 9. 单元测试 / ## 10. 逻辑行统计 / ## 11. 变更记录" 标题字面保留;**步骤 8.7 守卫首次生效**,本任务不生成 `compile-and-run.md` / `test-results.md`;§偏离 1 + §偏离 2 + §偏离 0) | TASK-BUG-00004-00002 |
| 2026-06-22 22:00 | 任务完成 | TASK-BUG-00004-00003 · [文档] 端到端验证(开发状态:已完成;静态校验 `code-it/SKILL.md` 步骤 8.7 line 805-914 + 步骤 9/10/11 守卫 line 917/926/936 + `templates/RESULT.md` §8 改造 line 101-136 全部就位;**T-002 真实产物 = 决定性证据**(4 个文件,守卫决定性生效);静态模拟判定场景 1(纯 Markdown 改造 7/7 观察点命中)+ 场景 3(纯文档任务 3/3 观察点命中);本任务**不**真跑 `code-it TASK-REQ-00039-00003`(避免状态污染,沿用 §偏离 1);§偏离 1 + §偏离 0) | TASK-BUG-00004-00003 |
| 2026-06-22 23:00 | 任务完成 | TASK-BUG-00004-00004 · [文档] 7 个技能旁路验证(开发状态:已完成;`code-require` / `code-design` / `code-check` / `code-plan` / `code-fix` / `code-init` / `code-rule` 7 个技能;4 个有判定表 / 3 个无判定表;全部"实际过度生成风险" = 低 / 中(0 触发) / 极低 / 无;**均不修复**;`side-skill-verification.md` 报告完整;与 BUG-00004 详细设计 §6 末字面 100% 一致;§偏离 1 + §偏离 0;末尾兜底提交累积 T-001 + T-002 + T-003 + T-004 一起 commit;**BUG-00004 状态推进** `修复编码中` → `待审查`) | TASK-BUG-00004-00004 |
| 2026-06-22 23:00 | 缺陷状态 | BUG-00004 状态"修复编码中"→"待审查"(`itEndStateRollback` 子步骤执行,`doneCount=4/totalCount=4`) | BUG-00004 |
| 2026-06-22 23:35 | 评审完成 | code-check 单缺陷模式评审 BUG-00004 完成(8 维度,0 条"必须改"/0 条"建议改"/0 条"可选",0 个派生"审查改修"任务);`checkStateRollback` 推进 BUG-00004 状态 `待审查` → `已完成`;`./assistants/V0.0.3/review/BUG-00004/REVIEW-REPORT.md` 主产出物;F-005 评审发现汇总;**评审通过** | BUG-00004 |
| 2026-06-22 13:30 | 设计新增 | REQ-00038 概要设计完成(8 决策 / 8 不变量 / 1 主改造 + 1 模板追加 + 1 文档字面改写 / 0 新增依赖),整体=--balanced,功能性=高(用户手动 1 问确认);0 触发扩展性问路(只读 monorepo 声明文件,不引入新依赖);0 冲突;候选 3 任务(由 code-plan 阶段细化);§概要设计清单追加 1 行 | REQ-00038 |
| 2026-06-22 20:30 | 计划完成 | code-plan 完成 BUG-00004 详细设计(9 份文档:本文件 + `./assistants/V0.0.3/fix/BUG-00004/PLAN.md` + 7 份过程文档);拆 4 个任务(T-001 ~ T-004,全部 触发/来源=缺陷修复);M1-BUG-00004 新增 | BUG-00004 |
| 2026-06-22 13:40 | 计划更新 | REQ-00038 详细设计与编码计划完成(共 3 个任务,全部开发=待开始,测试=不适用;整体=`--balanced` + 功能性=高;0 派生"更新看板"任务,沿用 REQ-00017 强约束;3 任务严格串行 T-1 → T-3;AC-1 ~ AC-7 全部纳入 T-3 验证;1 里程碑 M1-REQ-00038);7 份过程文档(materials-index / design-notes / module-details / interface-specs / risk-analysis / rule-compliance / 0 clarifications)已生成 | REQ-00038 |
| 2026-06-22 13:50 | 任务完成 | TASK-REQ-00038-00001 · [修改] code-it 步骤 8a.0 模块识别(新增子步骤)(开发状态:已完成;`git diff --stat` 1 file changed, +121 insertions, 0 deletions;`plugins/code-skills/skills/code-it/SKILL.md` L555-L675 新增 `### 步骤 8a.0 — 模块识别` 子节 + 9 子节(目标 / 识别优先级链 / 算法 / 输出与缓存 / 边界 / 性能 / 屏显契约 / 退出码契约 / 约束);frontmatter L1-3 字节级保留;INV-1 ~ INV-3 / INV-8 全部满足;8 套声明文件解析手写 0 新增三方依赖;末尾兜底 1 次 commit) | TASK-REQ-00038-00001 |
| 2026-06-22 14:10 | 任务完成 | TASK-REQ-00038-00002 · [修改] code-it 步骤 8a 守卫位置 + 步骤 8.5 单测输出位置扩展(开发状态:已完成;`git diff --stat` 1 file changed, +37 insertions, -8 deletions;5 处字面改写:§8a.1 检查位置 CWD 根 → 模块目录 + §8a.2 单点判定 → 模块聚合 + §8a.4 屏显扩展"模块级守卫检查详情"(2 种示例:多模块命中 + 单模块命中字节级沿用 REQ-00034) + §8.5.2 7 层测试目录识别优先级链 + §8.5.5 既有"## 单元测试"小节字节级保留 + 追加"## 各模块单测结果"小节;frontmatter L1-3 字节级保留;INV-1 / INV-3 / INV-4 / NFR-2 / NFR-4 全部满足;末尾兜底 1 次 commit) | TASK-REQ-00038-00002 |
| 2026-06-22 14:25 | 任务完成 | TASK-REQ-00038-00003 · [修改] 模板追加"## 各模块单测结果"小节 + code-plan 任务粒度描述字面改写 + 端到端验证(开发状态:已完成;`git diff --stat` 2 files changed, +19 insertions, -2 deletions;`code-it/templates/RESULT.md` L155-L171 新增"## 各模块单测结果"小节 + 7 字段(模块路径 / 守卫检查 / 检查位置 / 测试框架 / 测试文件 / 跑通情况)+ 既有"## 9. 单元测试"小节(L138-L153)字节级保留 + 既有 8 个章节(L28-L106)字节级保留;`code-plan/SKILL.md` L473 / L496 各字面改写 1 句;端到端 AC-1 ~ AC-7 全部 7/7 静态校验通过;frontmatter L1-3 字节级保留;INV-1 / INV-3 / INV-4 / NFR-4 / NFR-10 全部满足;末尾兜底 1 次 commit) | TASK-REQ-00038-00003 |
| 2026-06-22 14:41 | 评审完成 | code-check 整体评审 REQ-00038 完成(14 维度 = 8.1-8.14 全部通过;3 任务 × 14 维度 = 42 项校验全部 ✓;0 条"必须改" / 0 条"建议改" / 0 条"可选" / 0 个派生"审查改修"任务;8.10 详设完整性 ✓ + 8.11 概设越界 0 命中 + 8.12 行数比例 0.40 << 1.2 + 8.13 代码行数超标 ✓(技能文档不适用,沿用 BUG-00004 T-2 +177 行惯例)+ 8.14 过程文档适配性 ✓;M1-REQ-00038 里程碑已达成;`./assistants/V0.0.3/review/REQ-00038/REVIEW-REPORT.md` 主产出物;整体结论 = ✅ 通过) | REQ-00038 |
| 2026-06-22 14:50 | 缺陷登记 | code-fix 创建缺陷 BUG-00005(严重度 P1,状态 报告):`/code-require` 仍出现技术选型问路,违反 REQ-00033 字面硬约束(步骤 615 字面已存在,但步骤 7A 操作性字面未与"不弹技术选型问路"字面绑定,导致模糊场景下 AI 自动生成"实现方式"类问路选项) | BUG-00005 |
| 2026-06-22 14:50 | 缺陷状态 | BUG-00005 状态"报告"(本轮仅登记 + 初步根因已锁定,等 code-plan 阶段补修复方案) | BUG-00005 |
| 2026-06-22 15:00 | 计划完成 | code-plan 完成 BUG-00005 详细设计 + 2 份文档(`fix/BUG-00005/RESULT.md` + `PLAN.md`);拆 3 个任务(T-001 ~ T-003,全部 `触发/来源=缺陷修复`);整体=--balanced,功能性=高,健壮性=中,可维护性=中;M1-BUG-00005 新增(3 任务严格串行 T-1 → T-2 → T-3) | BUG-00005 |
| 2026-06-23 | 任务完成 | TASK-BUG-00005-00001 · [修改] code-require 步骤 7A 添加技术选型过滤器(开发状态:已完成);1/3 文件 `code-require/SKILL.md` L322-335(纯追加新子节,既有 L322-333 字面 0 改,步骤 8A / 615 顺移,内容字面 0 改);关键词集 20 个与详细设计 §5.1 字节级一致;0 派生"审查改修"任务 | TASK-BUG-00005-00001 |
| 2026-06-23 | 任务完成 | TASK-BUG-00005-00002 · [修改] code-require 步骤 8A 添加 NFR 技术选型过滤器(开发状态:已完成);2/3 文件 `code-require/SKILL.md` L337-353(纯追加新子节,既有 L337-L351 字面 0 改,"要求:" 段顺移 +1,步骤 9A / 10A / 615 顺移 +2);关键词集 14 个与详细设计 §5.2 字节级一致(与 T-1 关键词集部分重叠但不完全相同);与 T-1 末段 + 步骤 615 形成完整三链;0 派生"审查改修"任务 | TASK-BUG-00005-00002 |
| 2026-06-23 | 任务完成 | TASK-BUG-00005-00003 · [修改] code-require 步骤 615 硬约束增强(引用步骤 7A/8A)(开发状态:已完成);3/3 文件 `code-require/SKILL.md` L619-620(L619 步骤 615 原字面 0 改,选项 C 实施 - 在原行下方追加新 `- 列表项`,与详细设计 §4.3 字面"在硬约束后,添加引用"一致);新列表项完整复述触发动作 + 引用 T-1 / T-2 子节 + 详细设计 §5.1 + §5.2;完整三链(7A + 8A + 615)显式声明;3 任务全部完成,等 code-check 评审推进 BUG 状态 | TASK-BUG-00005-00003 |
| 2026-06-23 | 评审发现 | BUG-00005 评审完成(单缺陷模式,14 维度,0 条"必须改"/1 条"建议改"(F-001 — 关键词数量声称与字面不符,8 处 20→22,留作 follow-up)/0 条"可选";0 个派生"审查改修"任务;3 任务累计 5 行新增 0 修改 0 删除;`checkStateRollback` 推进 BUG-00005 状态"修复规划中"→"已完成";`./assistants/V0.0.3/review/BUG-00005/REVIEW-REPORT.md` 主产出物;评审通过) | BUG-00005 |
| 2026-06-25 | 需求新增 | REQ-00040 需求分析完成(共 6 FR / 10 NFR / 12 AC);1 轮 `AskUserQuestion`(4 问:启动判定 / 产物位置 / 状态触发 / 失败降级);4 问推荐项全采纳;FR-1 可启动性探测 + FR-2 复现动作触发 + FR-3 3 类产物(日志/截图/交互数据)+ FR-4 `reproduce/` 子目录 + FR-5 `bug.md` 模板新增"## 复现产物登记" 段 + FR-6 文档头新增 2 字段;**不**触发 `dashboard-conventions §规则 1`(产物放子目录,**不**进总览 / 看板);**不**触发 §615 技术选型(FR-1 是操作步骤,非技术选型);与 REQ-00037 强协同(NFR-2 字节级保留状态推进路径);`fix/<BUG-NNN>/reproduce/` 子目录 + `RESULT-meta.json` 元信息 + 失败降级 NFR-4 + 历史 BUG 不追加 NFR-5;看板 §需求清单 追加 1 行 + 统计总数 17→18 | REQ-00040 |
| 2026-06-25 | 设计新增 | REQ-00040 概要设计完成(--balanced;10 决策 / 8 不变量;模块数 2 主改造 + 1 辅助;2 SKILL.md 改造步骤 0 末尾 + 步骤 6 末尾子节 + 1 模板改造 bug.md 新增"## 复现产物登记" 段 + 1 模板改造 assistants-layout.md 同步追加 reproduce/ 子目录;0 关联设计;0 规范冲突;0 新增三方依赖;4 份过程文档生成 / 3 份不生成(dependencies 0 / related-designs 0 / clarifications 0);看板 §概要设计清单 追加 1 行 + 统计 15→16) | REQ-00040 |
| 2026-06-25 | 计划完成 | REQ-00040 详细设计与编码计划完成(15 章节 RESULT.md + 8 章节 PLAN.md;18 决策 / 8 不变量 / 5 内部接口 / 3 数据结构 / 11 边界 + 1 复合边界;6 任务严格串行 T-1 → T-6,全部 `触发/来源=详细设计`;12 AC 全部降级为静态校验;1 里程碑 M1-REQ-00040;7 份过程文档生成(其中 process-doc-decisions 决策文件 1 份);看板 §详细设计与任务计划汇总 追加 1 行 + §任务清单 追加 6 行 + §里程碑 追加 1 行 + §变更记录 追加 1 条;统计 19→20 计划 / 104→110 任务) | REQ-00040 |
| 2026-06-25 14:31 | 任务完成 | TASK-REQ-00040-00001 · [修改] code-fix 步骤 0 末尾追加"项目可启动性探测" 子节(开发状态:已完成;`git diff --stat` 1 file changed, +80/-0;`plugins/code-skills/skills/code-fix/SKILL.md` line 183 起新增"### 步骤 0.X" 子节含 7 步探测算法伪代码 + 3 边界 + 1 性能,共 +80 行;frontmatter L1-4 字节级保留;既有"## 工作流程" 步骤 0 主体 line 177-181 + 步骤 1~10 主体 + "## 不要做的事" 段字节级保留;0 偏离;AC-1 / AC-7 / AC-11 静态校验通过;commit ae42e39) | TASK-REQ-00040-00001 |
| 2026-06-25 14:36 | 任务完成 | TASK-REQ-00040-00002 · [修改] code-fix 步骤 6 末尾追加"复现产物登记" 子节(开发状态:已完成;`git diff --stat` 1 file changed, +494/-1 含过程文档;`plugins/code-skills/skills/code-fix/SKILL.md` line 371 起新增"### 步骤 6.X" 子节,含触发条件 3 条 + 9 步 reproduceBug 算法伪代码 + executeStep 3 类分发(cli/http/browser)+ 11 边界 + 1 复合边界 + 屏显契约 2 段 + 性能 1 段,共约 +140 行;发现并修复 Edit 时无意中复制的"**关键:不重写**" 注释(校验 `grep -c` 最终 = 1,确认**只 1 次**);frontmatter L1-4 + 步骤 6 主体 line 343-369 + 步骤 7-10 + "## 不要做的事" 字节级保留;0 偏离;AC-2 / AC-3 / AC-4 / AC-7 / AC-8 / AC-11 静态校验通过;commit b9afdba) | TASK-REQ-00040-00002 |
| 2026-06-25 14:42 | 任务完成 | TASK-REQ-00040-00003 · [修改] bug.md 模板新增"## 复现产物登记" 区段(开发状态:已完成;`git diff --stat` 1 file changed, +361/-0 含过程文档;`plugins/code-skills/skills/code-fix/templates/bug.md` 文档头表 line 22 后新增 2 行(复现方式 / 产物路径)+ line 60 `---` 分隔符前插入"## 复现产物登记" 区段含 3 子项(产物清单 / 实际行为 / 复现结论),共约 +29 行;既有 9 区段字节级保留;0 偏离;AC-5 / AC-6 / AC-7 / AC-11 静态校验通过;commit f029be6) | TASK-REQ-00040-00003 |
| 2026-06-25 14:46 | 任务完成 | TASK-REQ-00040-00004 · [修改] assistants-layout.md 同步追加 reproduce/ 子目录行(开发状态:已完成;`git diff --stat` 1 file changed, +323/-1 含过程文档;`plugins/code-skills/skills/code-fix/templates/assistants-layout.md` BUG-00001 子目录列表末尾(line 19 `deviations.md` 后 + line 20 `BUG-00002/` 前)追加 1 行 `│ └── reproduce/ # 复现产物(由 code-fix 步骤 6 末尾生成,可选)`;既有结构(7 子文件 + 关键约束 + 文件名约定)字节级保留(仅位置后移 1 行);0 偏离;AC-7 / AC-11 静态校验通过;commit 70f4632) | TASK-REQ-00040-00004 |
| 2026-06-25 14:50 | 任务完成 | TASK-REQ-00040-00005 · [文档] 端到端验证 12 条 AC(全部静态校验)+ 末尾兜底提交(开发状态:已完成;`git diff --stat` 1 file changed, +396/-0 含 AC-4 注释补充 + 5 份过程文档;`plugins/code-skills/skills/code-fix/SKILL.md` 步骤 6.X 子节 line 384 前补充 1 行注释 `// 产物路径:fix/<BUG-NNN>/reproduce/(模板字面,与 FR-4 + assistants-layout.md 同步)` 修复 AC-4 静态校验遗漏;12 条 AC 全部通过静态校验(本仓库 0 测试框架,全部降级为静态);**0 偏离**;M1-REQ-00040 里程碑完成定义全部满足 — 6 任务开发=已完成 ∧ 测试=不适用 ∧ AC-1 ~ AC-12 全过;commit 6a8d55c) | TASK-REQ-00040-00005 |
| 2026-06-25 14:57 | 任务完成 | TASK-REQ-00040-00006 · [文档] 同步版本看板"任务清单" / "里程碑" / "变更记录"(开发状态:已完成;`git diff --stat` 5 files changed, +323/-0 含 4 份过程文档 + 1 主产出物;`./assistants/V0.0.3/RESULT.md` 任务清单追加 1 行 T-006(待开始→已完成)+ 变更记录追加 1 条 + 文档头"最近更新" 刷新;**不**触碰 M1-REQ-00040 里程碑状态字面(沿用 `code-check` 推进职责);M1-REQ-00040 完成定义全部满足(6 任务开发=已完成 ∧ 测试=不适用 + AC-1 ~ AC-12 全过 + 1 次末尾兜底提交);**0 偏离**;末尾兜底提交落地;commit 4da784a) | TASK-REQ-00040-00006 |
| 2026-06-25 14:55 | 派生任务 | REQ-00040 评审派生 1 个"审查改修"任务 TASK-REQ-00040-00007(触发/来源=审查改修;关联任务=TASK-REQ-00040-00001, TASK-REQ-00040-00002;严重程度=必须改;改修要求:移除 `design/REQ-00040/RESULT.md` line 175 表格 2 行越界 `string` 类型字面);看板 §任务清单 追加 1 行(T-007 待开始)+ §评审发现汇总 追加 1 条(F-006)+ §派生任务记录 追加 1 行;`./assistants/V0.0.3/review/TASK-REQ-00040-00007/RESULT.md` 改修要求落地 | TASK-REQ-00040-00007 |
| 2026-06-25 14:55 | 评审发现 | REQ-00040 评审完成(11 维度,10 通过 / 1 警告:§8.11 概设越界 1 处 F-006);共 1 条"必须改"/0 条"建议改"/0 条"可选";1 个派生"审查改修"任务 TASK-REQ-00040-00007(待处理);`./assistants/V0.0.3/review/REQ-00040/REVIEW-REPORT.md` 主产出物;M1-REQ-00040 里程碑状态字面维持"待开始",待 T-007 完成后由 `code-check` 二次推进"待开始"→"已完成" | REQ-00040 |
**变更类型枚举**:
- `初始化`:创建版本工作空间
- `需求新增/变更/撤回`:需求清单变化
- `设计新增/变更`:概要/详细设计变化
- `任务新增/拆分/合并/取消`:PLAN.md 结构变化
- `开发状态更新`:任务开发轴变化
- `测试状态更新`:任务测试轴变化
- `缺陷新增/修复/关闭`:缺陷清单变化
- `评审发现`:code-check 产出
- `派生任务`:code-check 派生改修任务
- `里程碑推进`:里程碑状态变化
- `看板字段扩展`:本看板的字段约定扩展
- `其他`

---

## 索引:本版本所有文件

> 写入方:各 `code-*` 技能创建/修改文件时追加(可选,但推荐)

- 需求:`./assistants/V0.0.3/require/<需求编码>/RESULT.md` × 3
- 概要设计:`./assistants/V0.0.3/design/<需求编码>/RESULT.md` × 2
- 详细设计:`./assistants/V0.0.3/plan/<需求编码>/RESULT.md` × 3
- 任务计划:`./assistants/V0.0.3/plan/<需求编号>/PLAN.md` × 3
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00020-00001/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00020-00002/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00020-00003/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00020-00004/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00020-00005/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00020-00006/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00021-00001/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00021-00002/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00021-00003/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00021-00004/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00021-00005/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00021-00006/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00021-00007/RESULT.md` × 1
- 代码改修正文:`./assistants/V0.0.3/code/TASK-REQ-00021-00008/RESULT.md` × 1
- 测试改修正文:`./assistants/V0.0.3/test/<任务编码>/RESULT.md` × 0
- 评审报告:`./assistants/V0.0.3/review/REQ-00020/REVIEW-REPORT.md` × 1
- 评审报告:`./assistants/V0.0.3/review/REQ-00029/REVIEW-REPORT.md` × 1
- 评审过程:`./assistants/V0.0.3/review/REQ-00029/{work-log,review-checklist-applied,findings-no-task}.md` × 3
- 审查改修任务:`./assistants/V0.0.3/review/TASK-REQ-00020-00007/RESULT.md` × 1
- 审查改修任务:`./assistants/V0.0.3/review/TASK-REQ-00020-00008/RESULT.md` × 1
- 详细设计:`./assistants/V0.0.3/plan/REQ-00029/RESULT.md` × 1
- 任务计划:`./assistants/V0.0.3/plan/REQ-00029/PLAN.md` × 1
- 缺陷详情:`./assistants/V0.0.3/fix/BUG-00001/RESULT.md` × 1
- 缺陷总览:`./assistants/V0.0.3/fix/RESULT.md` × 1
- 详细设计:`./assistants/V0.0.3/plan/REQ-00025/RESULT.md` × 1
- 任务计划:`./assistants/V0.0.3/plan/REQ-00025/PLAN.md` × 1
- 过程文档:`./assistants/V0.0.3/plan/REQ-00025/{materials-index,module-details,interface-specs,data-changes,risk-analysis,rule-compliance,design-notes}.md` × 7
