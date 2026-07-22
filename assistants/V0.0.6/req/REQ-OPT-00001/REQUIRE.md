# 需求分析 — REQ-OPT-00001 · code-skills 技能能力优化建议报告 P0+P1 整改

> 所属版本:V0.0.6
> 创建时间:2026-07-22 10:39
> 模式:--confirm
> 范围:P0(4 项)+ P1(10 项) = 14 项问题,BUG 类问题本 REQ 内一起处理

## 0. 用户原始输入

> 用户在终端输入的命令:
> `/code:code req REQ-OPT-00001`
> 对应参数:`req REQ-OPT-00001`

> 用户准备的补充材料:
> `assistants/V0.0.6/req/REQ-OPT-00001/opt.md`(56KB)
> 标题:`code-skills 技能能力全景与优化建议报告`
> 审计日期:2026-07-22
> 该报告 §3 列出了 16 个已确认问题(4 个 P0、10 个 P1、3 个 P2),§6 给出 5 个 Phase 实施路线,§8.1 给出最小可行改修集 8 项。

> 用户在 REQUIRE 阶段开始前的三项决策(已在 AskUserQuestion 中确认,详见 clarifications.md):
> 1. 范围:P0+P1 全部 14 项整改
> 2. BUG 类问题处理:本 REQ 内一起处理
> 3. 模式:--confirm

## 1. 需求概述

`code-skills` 仓库自身的 Claude Code 技能集合存在**契约不一致**(字段、路径、状态、阶段数在 README/主入口/子技能/模板/解析算法之间相互矛盾),已确认 14 项 P0/P1 问题影响功能正确性(FAQ 导出、模板读取、基线初始化、看板/发布检查、merge 操作、确认模式、状态枚举)。本需求把 14 项问题转化为可独立验证的 FR,要求每项都有清晰的"修复前 → 修复后"判定,以及为后续 P2/P3 改造留下不冲突的数据契约基础。

## 2. 背景与目标

### 背景

- opt.md §3 列出 16 个 P0/P1/P2 静态可确认的问题,根因集中在三类:
  1. **数据契约不一致**:消费者按一种 schema 读取,生产者按另一种 schema 写入(如看板/发布/FAQ/模板/基线)
  2. **文档同步漂移**:README、CLAUDE.md、子命令 SKILL.md、common.md、模板对同一行为给出不同描述
  3. **权限/范围不清晰**:`/code ver` 声明只读却写 CWD 描述文件;`/code rule` Type B/C 隐式写权限;`/code merge` 直接 checkout 已被主工作区占用的目标分支
- 当前版本 V0.0.6 已有 2 个 BUG(00009/00010)和一个进行中的 REQ(REQ-00051 主 SKILL.md 拆分),本 REQ 是后续契约整改入口

### 目标

1. 修复全部 4 项 P0 问题,使 `/code ver --publish`、看板、FAQ 导出、模板读取、基线初始化按同一份数据契约工作
2. 修复全部 10 项 P1 问题,统一确认模式、状态枚举、字段定义、merge 流程、规则子流程
3. 为 P2/P3 改造(P2=架构级重构,P3=一致性验证和文档同步)留下不冲突的基础,不在本 REQ 内推进 P2/P3

## 3. 功能需求(FR)

### FR-1:统一看板数据契约(P0-3.1)
- **描述**:`/code ver --publish`、看板高优先级缺陷统计、建议生成全部从 `PROCESS.md` / `PLAN.md` / `BUG.md` 派生,不再从 `RESULT.md` 的"状态"字段派生
- **输入**:`PROCESS.md` 最后一条记录、各任务 TASK-N.md 的开发/测试状态、`BUG.md` 的状态字段
- **输出**:发布检查的"全部完成"判定 = 所有需求都到达 `DONE` 阶段且所有任务的开发状态为 `已完成`、测试状态 ∈ {`已运行-通过`, `不适用`}
- **来源**:opt.md §3.1

### FR-2:修正 FAQ 章节映射(P0-3.2)
- **描述**:`references/faq/common.md` 的需求导出映射以模板真实标题为键,而不是手工章节号
- **输入**:REQUIRE.md / DESIGN.md / PLAN.md / CHECK.md / TASK.md 的实际章节标题
- **输出**:FR_LIST → `## 3. 功能需求(FR)`,NFR_LIST → `## 4. 非功能需求(NFR)`,AC_LIST → `## 5. 验收标准(AC)`,关联需求 → `## 6. 关联需求`,待澄清 → `clarifications.md` 或 REQUIRE.md 中显式定义的章节
- **可选增强**:为每个可导出字段定义稳定锚点(如 `<!-- code-skills:field=FR_LIST -->`),避免章节编号变化再次破坏导出
- **来源**:opt.md §3.2

### FR-3:修正所有模板引用路径(P0-3.3)
- **描述**:所有 reference 内的模板链接统一从技能根目录写成相对路径,确保链接存在且唯一
- **输入**:6 处已知坏链接(`references/req/require.md:166`、`design.md:266`、`plan.md:193`、`coding.md:336`、`check.md:180`、`references/fix/fix-register.md:110`)
- **输出**:6 处链接全部指向实际存在的模板文件(`templates/req/*.md`、`templates/fix/*.md`),且为可解析的 Markdown 相对链接
- **来源**:opt.md §3.3

### FR-4:统一基线路径(P0-3.4)
- **描述**:`/code ver` 初始化基线版本时,基线需求写入 `req/EXISTING-NNN/`,而不是 `require/EXISTING-NNN/`
- **输入**:基线版本扫描结果(`existing require/...` 命名约定)
- **输出**:基线需求全部落在 `req/EXISTING-NNN/` 下,与主流程 `/code req` / `/code faq` / 看板扫描路径一致
- **迁移策略**:在迁移期间提供旧 `require/` 兼容读取,但不重命名已有用户工作空间
- **来源**:opt.md §3.4

### FR-5:统一默认确认行为(P1-3.5)
- **描述**:根 `CLAUDE.md`、`README.md`、`references/req/SKILL.md`、`references/fix/SKILL.md`、`common.md`、`help/SKILL.md` 对默认/--confirm/--auto 三态给出同一份行为契约
- **输入**:三态模型描述(默认 / --confirm / --auto)
- **输出**:所有文档统一表述为:
  | 模式 | 阶段边界 | 阶段内补充内容确认 |
  | --- | --- | --- |
  | 默认 | 自动继续,无需中断 | 需要用户确认补充的内容(需求澄清、方案选型、任务拆分等)等待用户确认,不自动跳过 |
  | --confirm | 每阶段完成后强制确认(产出物路径 + 重读 + 继续/中止) | 正常询问 |
  | --auto | 自动继续 | 所有需要用户确认补充的内容使用推荐选项自动继续,无需中断等待 |
- **关键边界**:默认模式 ≠ 全部跳过询问;它跳过的是**阶段边界**,不跳过**阶段内补充内容确认**;--auto 才是两个都跳过
- **来源**:opt.md §3.5;用户 2026-07-22 10:42 在 clarifications.md 明确细化

### FR-6:统一帮助选项数量(P1-3.6)
- **描述**:`SKILL.md`、`help/SKILL.md`、`README.md` 对"路由选项数量"给出同一表述
- **输入**:实际路由分支数(`ver`、`req`、`fix`、`faq`、`rule`、`merge`、`help` = 7)
- **输出**:统一为"7 个路由选项(6 个业务命令 + help)",同一命令矩阵作为 README、help 和主入口的唯一来源
- **来源**:opt.md §3.6

### FR-7:补齐 PLAN 测试状态流转规则(P1-3.7)
- **描述**:`templates/req/PLAN.md` 的"测试状态"列在 PLAN 阶段有明确的初值规则,CODING 阶段的状态转移有明确规则
- **输入**:任务类型清单
- **输出**:
  - 每种任务类型的初始测试状态(默认 `未编写`;文档型任务 = `不适用`)
  - "不适用"的判定条件
  - CODING 编译/运行/测试后的状态转移图
  - 运行环境缺失时 = `阻塞`
  - CHECK 与 publish 如何消费测试状态字段
- **来源**:opt.md §3.7

### FR-8:补齐 CHECK 模板审查维度(P1-3.8)
- **描述**:`templates/req/CHECK.md` 与 `references/req/check.md` 的审查维度定义一致,模板承载全部 9 个维度的产出位置
- **输入**:`check.md` 定义的 9 个维度(正确性 / 需求一致性 / 设计一致性 / 规范性 / 安全性 / 性能 / 可维护性 / 测试覆盖 / 代码行数超标)
- **输出**:模板补齐 3 个缺失维度(需求一致性、测试覆盖、代码行数超标)的产出位;每个维度有"结果 / 证据 / 发现数"列;结论由可检查条件生成(`必须改` 数量 = 0)
- **来源**:opt.md §3.8

### FR-9:明确 `/code ver` 写权限边界(P1-3.9)
- **描述**:`/code ver` 在版本切换时保留自动同步 CWD 描述文件的行为,但为同步过程增加"差异预览 / 用户确认 / 失败回滚 / 提交记录"四步;同时把 SKILL.md 的"只读"声明改为与之匹配的"默认同步 + 加四步"
- **输入**:版本切换命令(默认)、CWD 描述文件清单(`package.json` / `pom.xml` / `Cargo.toml` / `pyproject.toml` / `manifest.json` 等)
- **输出**:
  - 切换时,默认走"扫描 → 差异预览 → AskUserQuestion 确认 → 写入 → 失败回滚 → 提交"流程
  - 用户可选择"中止"(只更新 `.current-version`,不写 CWD)或"仅修改特定文件"
  - 写失败必须回退到原状,返回非 0
  - 成功时把同步结果写入 commit
  - `references/ver/SKILL.md:48-53` 的"只读"声明改为"默认同步 + 加四步"
- **关键**:声明与行为必须一致,不再保留两套语义
- **来源**:opt.md §3.9;用户 2026-07-22 10:58 拍板方案 B

### FR-10:统一运行时状态枚举(P1-3.10)
- **描述**:`templates/req/TASK.md` 与 `references/runtime-environment.md` 使用同一份运行时状态枚举
- **输入**:当前两套枚举(`TASK.md` = 已配置/用户提供路径/自动安装/用户跳过/未配置;runtime-environment.md = 已配置/由用户跳过/由用户授权自动安装/由用户提供路径)
- **输出**:
  ```text
  runtimeStatus:
    configured
    user-provided
    auto-installed
    skipped
    unavailable
  ```
  文档展示再映射为中文,模板直接使用机器值
- **来源**:opt.md §3.10

### FR-11:统一需求分析技术选型词表(P1-3.11)
- **描述**:`references/req/require.md` 内部对"技术选型过滤关键词"只维护一份词表
- **输入**:当前两份不一致的关键词集(20 个关键词 + 一份较短的 `decisionKeywords`)
- **输出**:
  - `decisionKeywords`:只用于延迟到 DESIGN
  - `conflictKeywords`:即使属于技术词也必须在 REQUIRE 确认
  - 每条命中记录:命中的词 / 原问题 / 延迟原因
  - 删除"20 个"这类人工计数,改为由校验工具生成或不再强调数字
- **来源**:opt.md §3.11

### FR-12:修复 `/code merge` 目标分支操作(P1-3.12)
- **描述**:`/code merge` 不在当前 worktree 内直接 checkout 目标分支;通过 `git worktree list --porcelain` 找到主工作区,使用 `git -C <main-worktree> merge <feature-branch> --no-ff` 完成合回
- **输入**:feature worktree 路径、目标分支名
- **输出**:
  - 在开始前分别检查 feature worktree 和 target worktree 是否 dirty
  - 在主工作区执行 merge,不切换当前 worktree
  - unresolved 冲突时返回非 0,不报告成功
  - `CODE_MERGE_TARGET` 的分支名、远端 ref、本地 checkout 目标分开建模
- **需验证**:这是一项高概率运行时问题,需在实际 git worktree 场景冒烟验证后才定案
- **来源**:opt.md §3.12

### FR-13:统一 `/code merge` 看板自检契约(P1-3.13)
- **描述**:`RESULT.md` 有明确的 schema 版本,`/code merge` 自检只验证该 schema,旧 schema 走兼容模式
- **输入**:`RESULT.md` 当前内容
- **输出**:
  - `RESULT.md` schema 标记为 `dashboard-v2`
  - **schema-v2 固定为"纯索引"**(无动态状态/优先级/测试状态列);动态信息全部从 PROCESS.md / PLAN.md / BUG.md / TASK-N.md 派生(与 FR-1 一致)
  - 固定区段名称、表头、统计行格式
  - merge 自检只验证该 schema;旧 schema 走兼容解析并明确标记"兼容模式"
  - 若采用"状态从 PROCESS 派生",则 merge 只检查索引链接和条目唯一性,不检查不存在的状态列
- **与 FR-1 的关系**:FR-1 禁止从 RESULT 状态列派生,FR-13 把 RESULT 固定为"纯索引 schema-v2";两 FR 协同,不冲突
- **来源**:opt.md §3.13

### FR-14:明确 `/code rule` Type A/B/C 子流程的写权限与完成条件(P1-3.15,BUG 类问题本 REQ 内处理)
- **描述**:`references/rule/SKILL.md` 为 Type A/B/C 各定义独立的目标文件、schema、写入权限、完成条件
- **输入**:Type A(新建/追加规则)、Type B(写入 CLAUDE.md AI 工作约定区段)、Type C(写入模板)
- **输出**:
  | 类型 | 目标文件 | 允许动作 | 完成条件 |
  | --- | --- | --- | --- |
  | A | `assistants/rules/<category>.md` | 新建或末尾追加 | 分类、级别、范围、例外已记录 |
  | B | 明确指定的 `CLAUDE.md` | 仅追加 AI 工作约定区段 | 指引编号唯一,未改仓库说明区 |
  | C | 明确指定的 template | 末尾/字段内二选一并记录 | 提示位置和触发字段可定位 |
- **关联 BUG**:本 FR 替代 opt.md §3.15 描述的问题,BUG-OPT-00001/00002/00003 不另开编号,本 REQ 内闭环
- **来源**:opt.md §3.15

## 4. 非功能需求(NFR)

| 编号 | 类型 | 描述 | 约束 |
| --- | --- | --- | --- |
| NFR-1 | 契约一致性 | FR-1 ~ FR-13 涉及的所有数据契约(schema 字段、状态枚举、章节锚点)在生产者侧和消费者侧**同源** | 任一消费者读取的字段必须在生产者侧有明确定义;不允许"消费者按 A 读、生产者按 B 写" |
| NFR-2 | 文档同步 | FR-5 / FR-6 / FR-10 / FR-11 涉及的文档(README、CLAUDE.md、子命令 SKILL.md、common.md、help、模板)对同一行为只说一种话 | 同一行为描述出现 ≥2 处时,以本 REQ 产出的 DESIGN.md 为唯一基准,其他位置同步修改 |
| NFR-3 | 可恢复性 | 所有写入操作都有"用户中止 / 失败回滚 / 不留下半成品"语义 | FR-9 的 `--sync-project-version` 必须支持回滚;FR-12 的 merge 操作 unresolved 必须返回非 0 |
| NFR-4 | 权限边界 | `/code ver` / `/code rule` / `/code merge` 的写权限范围有明文声明 | FR-9 / FR-14 / FR-12 的权限边界必须写入各自的 SKILL.md 和 README |
| NFR-5 | 可追溯 | 每个 FR 的修复前/修复后都有可静态验证的差异点 | 修复前 → 修复后的差异在 PLAN.md 任务描述中明确写出"如何验证" |
| NFR-6 | 不影响 P2/P3 | 本 REQ 的所有修复都不应阻塞 P2(架构重构)/ P3(一致性验证)的推进 | 不增加新的硬门 / 不重写主入口描述 / 不引入新的 SKILL.md(若必须新增,在 DESIGN 阶段标记为 Phase 2 改造前置) |
| NFR-7 | 维护期兼容 | FR-4 的 `require/` 兼容读取与 FR-13 的旧 schema 兼容模式在迁移期内可用 | 兼容期不超过 1 个版本号(V0.0.6 → V0.0.7 之内),V0.0.8 起移除兼容代码 |

## 5. 验收标准(AC)

| 编号 | 描述 | 验证方式 |
| --- | --- | --- |
| AC-1 | 看板 / publish / FAQ 导出全部从同一份数据源读取,不再从 `RESULT.md` 状态列派生 | `grep -rE "状态列\|状态字段" references/ver/ references/faq/` 应无业务读取代码;`references/ver/common.md` 的发布检查算法改为 `deriveItemStatus()` |
| AC-2 | FAQ 章节映射以模板标题为键,且支持稳定锚点 | 在 `references/faq/common.md` 中查找 FR/NFR/AC/关联需求的读取路径,均为 `## 3. 功能需求(FR)` 等标题或 `<!-- code-skills:field=* -->` 锚点 |
| AC-3 | 6 处模板链接全部指向实际文件 | 人工/脚本验证:`refs/req/require.md:166`、`design.md:266`、`plan.md:193`、`coding.md:336`、`check.md:180`、`refs/fix/fix-register.md:110` 全部命中 `templates/req/*.md` 或 `templates/fix/*.md` |
| AC-4 | 基线初始化只写 `req/EXISTING-NNN/`,不再写 `require/` | 在新项目上跑 `/code ver` 初始化,验证 `assistants/<version>/req/` 下有 EXISTING-NNN 目录,`require/` 下为空 |
| AC-5 | 三态确认行为在所有文档中表述一致;默认模式阶段自动继续、阶段内补充内容仍等待确认 | 在 README、CLAUDE.md、req/SKILL.md、fix/SKILL.md、common.md、help/SKILL.md 中 grep "默认\|--confirm\|--auto" 表格,内容与 FR-5 输出列一致 |
| AC-6 | 帮助选项数量统一为"7 个路由选项(6 个业务命令 + help)" | 在 SKILL.md、help/SKILL.md、README.md 中 grep "路由选项\|业务命令",数字与名称一致 |
| AC-7 | PLAN 模板的测试状态列有完整流转规则 | `templates/req/PLAN.md` 有"测试状态初值表";"不适用"判定条件"在 references/req/plan.md 中明文存在;CODING 阶段状态转移图存在 |
| AC-8 | CHECK 模板承载全部 9 个维度 | `templates/req/CHECK.md` 包含:正确性 / 需求一致性 / 设计一致性 / 规范性 / 安全性 / 性能 / 可维护性 / 测试覆盖 / 代码行数超标;每个维度有"结果 / 证据 / 发现数" |
| AC-9 | `/code ver` 默认同步 CWD 描述文件,加差异预览 / 用户确认 / 失败回滚 / 提交记录四步;SKILL.md 声明同步修改 | 默认场景下 `git status --porcelain` 在版本切换后能列出同步变更;带 `--sync-project-version` 时同样走四步;`references/ver/SKILL.md` 不再保留"只读"声明 |
| AC-10 | 运行时状态枚举在模板与 reference 中一致 | `templates/req/TASK.md` 与 `references/runtime-environment.md` 中的枚举值集合相等(5 项机器值) |
| AC-11 | 需求分析技术选型词表只有一份 | `references/req/require.md` 内 `decisionKeywords` / `conflictKeywords` 各一组,无重复词表 |
| AC-12 | `/code merge` 不在当前 worktree 内 checkout 目标分支 | 流程代码包含 `git worktree list --porcelain` 调用,merge 命令前缀为 `git -C <main-worktree> merge` |
| AC-13 | `RESULT.md` schema 标记为 dashboard-v2,merge 自检只验证该 schema | `templates/ver/RESULT.md` 头部含 `schema: dashboard-v2`;`references/merge/SKILL.md` 自检逻辑按该 schema 校验 |
| AC-14 | `/code rule` Type A/B/C 有明确的目标、权限、完成条件 | `references/rule/SKILL.md` 含 Type A/B/C 表格(目标文件 / 允许动作 / 完成条件) |

## 6. 关联需求

| 需求编码 | 版本 | 关联点 | 影响 |
| --- | --- | --- | --- |
| REQ-00051 | V0.0.6 | 主 SKILL.md 拆分 + help 子命令化 | FR-6 / FR-5 的部分改动可能与 REQ-00051 重叠;PLAN 阶段需确认边界,避免重复修复 |
| BUG-00009 | V0.0.6 | /code ver 切换版本后未在最后阶段提交代码 | FR-9 涉及 `/code ver` 写权限,可能引入新的 commit 时机;需在 CHECK 阶段验证 BUG-00009 的修复不退化 |
| BUG-00010 | V0.0.6 | req/fix CHECK 阶段建议改/可选改自动应用规则不明确 | FR-8 涉及 CHECK 模板维度,与 BUG-00010 的"建议改/可选改"应用规则相邻;需在 PLAN 阶段决定是否合并处理 |

## 7. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-22 10:39 | v1 | 初始创建 | REQUIRE 阶段完成;14 项 P0+P1 问题全部转化为 FR;范围/模式决策已记录到 clarifications.md | wangmiao |
