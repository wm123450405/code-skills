# 软件设计 — REQ-OPT-00001 · code-skills 技能能力优化建议报告 P0+P1 整改

> 所属版本:V0.0.6
> 创建时间:2026-07-22 10:50
> 上游输入:REQUIRE.md(14 FR / 7 NFR / 14 AC)
> 设计对象:code-skills 仓库自身的**技能文件**(Markdown 文档、模板、契约),非产品代码

## 1. 设计概述

本 REQ 的设计核心是**把"读写契约"从散落的多份文档提升为一份共享定义**,并在 14 个具体 FR 上执行"修复 → 落盘 → 自检"的循环。设计分三层:
1. **契约层**(新增 `skills/code/references/_shared/contracts.md`):统一字段名、状态枚举、章节锚点、schema 版本
2. **同步层**(覆盖 README、CLAUDE.md、各子命令 SKILL.md、模板):按契约层重写,行为只说一种话
3. **实现层**(各子命令的 common.md):按契约层重写解析算法,从同一数据源读取

设计原则:**不做架构级重构**(NFR-6);**所有修改都局限在已有文件**(不新增 SKILL.md、不重写主入口 description)。

## 2. 模块拆分

| 模块 | 职责 | 涉及文件 | 依赖 |
| --- | --- | --- | --- |
| **契约层** | 定义所有跨模块的字段名 / 状态枚举 / 章节锚点 / schema 版本 | 新增 `skills/code/references/_shared/contracts.md` | 无 |
| **RESULT.md schema** | 固定为 dashboard-v2 纯索引;定义区段、表头、统计行格式;merge 自检按此校验 | 新增 `templates/ver/RESULT.md`(已存在的话覆盖);修改 `references/ver/common.md` 的初始化与读取 | 契约层 |
| **看板派生层** | publish / 看板高优先级缺陷统计 / 建议生成全部从 PROCESS.md / PLAN.md / BUG.md / TASK-N.md 派生,提供 `deriveItemStatus()` 单一函数 | 修改 `references/ver/common.md`(publish + 看板算法);删除所有"从 RESULT 状态列读取"的伪代码 | 契约层、RESULT.md schema |
| **FAQ 导出层** | FAQ 需求导出以模板标题 / 稳定锚点为键,不再用章节号 | 修改 `references/faq/common.md`(章节映射表 + 占位符);为 templates/req/*.md、templates/fix/*.md、templates/ver/RESULT.md 加 `<!-- code-skills:field=* -->` 锚点 | 契约层 |
| **基线路径层** | 初始化基线版本时,基线需求写入 `req/EXISTING-NNN/`,旧 `require/` 走兼容读取 | 修改 `references/ver/common.md`(基线算法);新增 `require/` 兼容读取逻辑(限定 V0.0.7 之内有效) | 契约层 |
| **三态确认契约** | 默认/--confirm/--auto 三态在所有文档统一表述 | 修改:根 `CLAUDE.md`、`README.md`、`README.en.md`、`skills/code/SKILL.md`、`references/req/SKILL.md`、`references/fix/SKILL.md`、`references/req/common.md`、`references/help/SKILL.md` | 契约层 |
| **帮助选项计数** | 统一"7 个路由选项(6 业务命令 + help)" | 修改:`skills/code/SKILL.md`、`references/help/SKILL.md`、`README.md`、`README.en.md` | 契约层 |
| **PLAN 测试状态流转** | PLAN 模板测试状态列有初值规则;CODING 阶段状态转移有规则 | 修改:`templates/req/PLAN.md` + 新增"测试状态流转规则"附录;`references/req/plan.md`(初值表 + 转移图);`references/req/coding.md`(转移点) | 契约层(状态枚举) |
| **CHECK 模板维度** | 补齐 3 个缺失维度(需求一致性 / 测试覆盖 / 代码行数超标);每个维度有结果/证据/发现数 | 修改:`templates/req/CHECK.md` + `references/req/check.md`(共享维度表) | 契约层 |
| **`/code ver` 写权限** | 保留自动同步 CWD 描述文件的默认行为;增加差异预览 / 用户确认 / 失败回滚 / 提交记录四步 | 修改:`references/ver/SKILL.md`(声明从"只读"改为"默认同步 + 加四步");`references/ver/common.md`(为自动同步加四步前置) | 契约层 |
| **运行时状态枚举** | 模板与 reference 统一为 5 项机器值 | 修改:`templates/req/TASK.md` + `references/runtime-environment.md` | 契约层 |
| **需求分析技术选型词表** | 一份 `decisionKeywords` + 一份 `conflictKeywords` | 修改:`references/req/require.md`(移除第二份词表;移除"20 个"人工计数) | 契约层 |
| **`/code merge` worktree 操作** | 不在当前 worktree checkout 目标分支;在主工作区执行 merge;unresolved 返回非 0 | 修改:`references/merge/SKILL.md` + `references/merge/common.md`(如有) | 契约层 |
| **`/code merge` 看板自检** | merge 自检只校验 dashboard-v2 schema(不保留旧 schema 兼容模式) | 修改:`references/merge/SKILL.md`(自检逻辑);`templates/ver/RESULT.md`(头部加 schema 标记) | RESULT.md schema |
| **`/code rule` Type A/B/C** | 为 Type A/B/C 各定义目标文件 / 允许动作 / 完成条件 | 修改:`references/rule/SKILL.md`(新增 Type A/B/C 表格) | 契约层 |

## 3. 接口设计

### 3.1 `deriveItemStatus()`(看板派生)

- **路径/签名**:`references/ver/common.md` → `function deriveItemStatus(reqOrBugId: string): ItemStatus`
- **入参**:需求编号 `REQ-NNNNN` 或缺陷编号 `BUG-NNNNN`
- **出参**:`{ stage: string; devStatus: string; testStatus: string; completed: boolean }`
- **异常**:编号不存在 → 返回 `{ stage: 'UNKNOWN', completed: false }`(保守行为,不抛错)
- **数据源**:
  - 阶段 ← `PROCESS.md` 最后一行
  - 开发状态 / 测试状态 ← `PLAN.md` 任务表的对应列(`TASK-N.md` 在 CODING 中由 coding agent 写入)
  - 缺陷状态 ← `BUG.md`
- **使用方**:`/code ver --publish`、`/code ver`(看板)、`/code faq` 的 `--summary` 导出

### 3.2 `RESULT.md schema` 契约

- **路径**:`templates/ver/RESULT.md`(头部 frontmatter)+ `references/_shared/contracts.md`(规范定义)
- **schema 标记**:`schema: dashboard-v2`(位于文档头注释块)
- **强制结构**:
  ```markdown
  # 版本开发进度看板 — <版本号>
  <!-- schema: dashboard-v2 -->
  ## 需求清单
  | 需求编码 | 标题 | 进度文档 |
  ## 缺陷清单
  | 缺陷编号 | 标题 | 进度文档 |
  ## 变更记录
  | 时间 | 变更类型 | 变更摘要 | 关联项 |
  ```
- **禁止列**(回归保护):"状态 / 优先级 / 测试状态 / 开发状态"等动态字段不允许出现在 schema-v2 中
- **【用户确认 2026-07-22 10:55】不保留旧 schema 兼容模式**:现存 `RESULT.md` 不符合 dashboard-v2 的,迁移代码就地升级(把"统计"行按新格式重写;动态状态列直接删除,状态来源已切到 PROCESS 派生)

### 3.3 FAQ 章节映射契约

- **路径**:`references/faq/common.md` + 各模板的稳定锚点
- **映射规则**(以标题为键,章节号为 fallback):
  | 字段 | 模板标题 | 可选锚点 |
  | --- | --- | --- |
  | FR_LIST | `## 3. 功能需求(FR)` | `<!-- code-skills:field=FR_LIST -->` |
  | NFR_LIST | `## 4. 非功能需求(NFR)` | `<!-- code-skills:field=NFR_LIST -->` |
  | AC_LIST | `## 5. 验收标准(AC)` | `<!-- code-skills:field=AC_LIST -->` |
  | 关联需求 | `## 6. 关联需求` | `<!-- code-skills:field=RELATED -->` |
  | 待澄清 | (来自 `clarifications.md`) | (无,直接读文件) |
- **解析顺序**:先匹配锚点,锚点不存在再匹配标题;都不命中 → 标记"未识别字段",不抛错

### 3.4 三态确认契约

- **路径**:所有引用三态的文档(README、CLAUDE.md、req/SKILL.md、fix/SKILL.md、req/common.md、help/SKILL.md)
- **契约内容**(统一表格,所有文档原文复用):
  | 模式 | 阶段边界 | 阶段内补充内容确认 |
  | --- | --- | --- |
  | 默认 | 自动继续,无需中断 | 需要用户确认补充的内容(需求澄清、方案选型、任务拆分等)等待用户确认,不自动跳过 |
  | --confirm | 每阶段完成后强制确认(产出物路径 + 重读 + 继续/中止) | 正常询问 |
  | --auto | 自动继续 | 所有需要用户确认补充的内容使用推荐选项自动继续,无需中断等待 |
- **关键边界**:默认模式 ≠ 全部跳过询问;--auto 才是两个都跳过(用户 2026-07-22 10:42 确认)

### 3.5 运行时状态枚举契约

- **路径**:`references/_shared/contracts.md`(机器值)+ 各引用方(展示值)
- **机器值**(5 项):
  ```text
  runtimeStatus:
    configured       — 运行时已就绪
    user-provided    — 用户提供运行时路径
    auto-installed   — 自动安装
    skipped          — 用户跳过(明示同意)
    unavailable      — 运行时不可用
  ```
- **展示映射**(中文):
  | 机器值 | 中文 |
  | --- | --- |
  | configured | 已配置 |
  | user-provided | 由用户提供路径 |
  | auto-installed | 由用户授权自动安装 |
  | skipped | 由用户跳过 |
  | unavailable | 未配置 |

### 3.6 `/code ver` 版本同步四步流程

- **触发**:`/code ver <version>` 默认走版本同步四步流程(用户 2026-07-22 10:58 拍板方案 B)
- **行为**:四步流程
  1. **差异预览**:扫描 CWD 描述文件(`package.json` / `pom.xml` / `Cargo.toml` / `pyproject.toml` / `manifest.json` 等),`git diff --stat` + 每个文件的 diff 摘要
  2. **用户确认**:屏显差异 + AskUserQuestion(继续 / 中止 / 仅修改特定文件)
  3. **失败回滚**:写失败 → `git checkout -- <files>` 回退 + 返回非 0
  4. **提交记录**:成功后写入版本切换 commit
- **声明同步**:`references/ver/SKILL.md:48-53` 的"只读"声明需同步改为"默认同步 CWD 描述文件,加差异预览 / 用户确认 / 失败回滚 / 提交记录"

### 3.7 `/code merge` worktree 操作契约

- **签名**:`/code merge [target]`
- **前置检查**:
  1. 当前 worktree 是否 dirty(若是 → 拒绝)
  2. feature worktree 是否 dirty(若是 → 拒绝)
  3. target worktree 是否 dirty(若是 → 拒绝)
  4. `git worktree list --porcelain` 找到 target 主工作区
- **merge 命令**:`git -C <main-worktree> merge <feature-branch> --no-ff`
- **失败语义**:有 unresolved 冲突 → 返回非 0 退出码 + 屏显列出冲突文件,不报告成功

### 3.8 `/code rule` Type A/B/C 契约

- **路径**:`references/rule/SKILL.md`
- **契约表格**:
  | 类型 | 目标文件 | 允许动作 | 完成条件 |
  | --- | --- | --- | --- |
  | A | `assistants/rules/<category>.md` | 新建或末尾追加 | 分类、级别、范围、例外已记录 |
  | B | 明确指定的 `CLAUDE.md` | 仅追加 AI 工作约定区段 | 指引编号唯一,未改仓库说明区 |
  | C | 明确指定的 template | 末尾/字段内二选一并记录 | 提示位置和触发字段可定位 |

## 4. 数据设计

### 4.1 `ItemStatus` 结构(看板派生层)

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| stage | string | 当前阶段(INIT/REQUIRE/DESIGN/PLAN/CODING/CHECK/DONE/UNKNOWN) |
| devStatus | string | 任务开发状态(待开始/进行中/已完成/已取消/阻塞/待重新评估) |
| testStatus | string | 任务测试状态(未编写/已编写/已运行-通过/已运行-失败/不适用/阻塞) |
| completed | boolean | 是否可发布(stage=DONE && devStatus=已完成 && testStatus ∈ {已运行-通过, 不适用}) |

### 4.2 `dashboard-v2` RESULT.md 结构

| 区段 | 必需 | 表头 |
| --- | --- | --- |
| 文档头 | 是 | 版本号 / 创建时间 / 最近更新 / 创建人 / 负责人 / 状态 / 描述 |
| 需求清单 | 是 | 需求编码 / 标题 / 进度文档 |
| 缺陷清单 | 是 | 缺陷编号 / 标题 / 进度文档 |
| 变更记录 | 是 | 时间 / 变更类型 / 变更摘要 / 关联项 |

(无动态状态 / 优先级 / 测试状态列)

### 4.3 章节锚点 schema

```markdown
<!-- code-skills:field=<FIELD_NAME> -->
```

- 字段名:大写 + 下划线(FR_LIST、NFR_LIST、AC_LIST、RELATED)
- 位置:对应章节标题**之前**(同段)或**之后**(单独段落)

### 4.4 状态字面表(各文档统一)

| 字段 | 字面值集合 |
| --- | --- |
| 阶段 | INIT / REQUIRE / DESIGN / PLAN / CODING / CHECK / DONE |
| 开发状态 | 待开始 / 进行中 / 已完成 / 已取消 / 阻塞 / 待重新评估 |
| 测试状态 | 未编写 / 已编写 / 已运行-通过 / 已运行-失败 / 不适用 / 阻塞 |
| 运行时状态 | configured / user-provided / auto-installed / skipped / unavailable |

## 5. 关键流程

### 5.1 publish 检查流程(FR-1)

```
触发: /code ver --publish
步骤:
  1. 读取 assistants/.current-version,记为 <V>
  2. 扫描 <V>/req/REQ-*/ 和 <V>/fix/BUG-*/
  3. 对每个需求/缺陷调用 deriveItemStatus(id)
  4. 收集所有 completed=false 的条目
  5. 若集合为空 → 通过,生成发布手册
  6. 若非空 → 列出未完成条目,AskUserQuestion 询问(继续 / 中止)
异常路径:
  - 编号不存在 → 标记为 UNKNOWN,记入未完成集合(保守行为)
  - PROCESS.md 不存在 → 同上,标记 UNKNOWN
```

### 5.2 FAQ 导出流程(FR-2)

```
触发: /code faq --require <REQ>
步骤:
  1. 读 req/<REQ>/REQUIRE.md
  2. 对每个目标字段(FR_LIST/NFR_LIST/AC_LIST/RELATED):
     a. 优先匹配 <!-- code-skills:field=<F> --> 锚点
     b. 锚点不存在则匹配章节标题 "## <N>. <标题>"
     c. 都不存在 → 标记"未识别字段",不抛错
  3. 读 req/<REQ>/clarifications.md(若存在)
  4. 按模板组装输出
异常路径:
  - REQUIRE.md 不存在 → 返回错误信息,不输出半成品
  - 输出路径越界 → 返回错误信息
```

### 5.3 `/code merge` 流程(FR-12)

```
触发: /code merge [target]
步骤:
  1. 解析参数(默认 target=origin/main)
  2. 当前 worktree dirty? 是 → 拒绝,提示用户先 commit/stash
  3. feature worktree dirty? 是 → 拒绝
  4. target worktree dirty? 是 → 拒绝
  5. git worktree list --porcelain → 找到 target 主工作区路径
  6. git -C <main-worktree> fetch origin
  7. git -C <main-worktree> merge <feature-branch> --no-ff
  8. 完成后做看板自检(走 FR-13 契约)
  9. 自检通过 → 提示用户推送
异常路径:
  - 有 unresolved 冲突 → 返回非 0,屏显列出冲突文件,不做后续步骤
  - 步骤 8 自检失败 → 不报告成功,返回非 0
```

### 5.4 `/code ver` 版本同步流程(FR-9)

```
触发: /code ver <version>
步骤:
  1. 解析 <version>
  2. 扫描 CWD 描述文件(package.json / pom.xml / Cargo.toml / pyproject.toml / manifest.json 等)
  3. 计算差异(列出每个文件 + diff 摘要)
  4. 屏显差异 + AskUserQuestion(继续 / 中止 / 仅修改特定文件)
  5. 用户选择"继续" → 写文件
  6. 写失败 → git checkout -- <files> 回退 + 返回非 0
  7. 写成功 → git add + git commit(走 BUG-00009 的修复路径)
异常路径:
  - 未检测到任何 CWD 描述文件 → 提示"无需同步",按默认流程走
  - 用户选择"中止" → 不写任何文件,只更新 .current-version
声明同步:
  - references/ver/SKILL.md:48-53 的"只读"声明改为"默认同步 + 加四步"
```

## 6. 方案选型

### 决策 D-1:契约层的承载形式
- **选择**:`references/_shared/contracts.md`(新增文件)
- **备选**:
  - A. 不新增文件,把契约直接写入各 common.md —— 优点:无新文件;缺点:无法单一定义,违反 NFR-1 契约一致性
  - B. 写入各子命令 SKILL.md —— 优点:就近;缺点:契约分散,难保单一来源
- **理由**:契约层是"被所有子命令只读引用"的共享定义,独立文件最符合"单一来源"原则;NFR-1 硬约束
- **权衡**:增加一个新文件;换取契约可维护性

### 决策 D-2:`deriveItemStatus()` 的异常行为
- **选择**:编号 / PROCESS.md / PLAN.md 不存在 → 返回 `UNKNOWN` 状态,不抛错
- **备选**:抛错退出
- **理由**:publish 检查是"查全部条目",中途抛错会让用户无法得到完整失败清单;保守返回 UNKNOWN 让 publish 仍可继续判定
- **权衡**:可能掩盖真问题(若某 REQ 整个目录被误删,会被当作"未完成");由 CHECK 阶段的人类审查兜底

### 决策 D-3:FAQ 章节映射的 fallback 策略
- **选择**:锚点优先 → 标题 fallback → 标记未识别
- **备选**:只匹配标题
- **理由**:opt.md §3.2 建议方案 = 锚点优先,可同时支持模板编号变化;不引入额外风险
- **权衡**:锚点需要修改所有模板头部(但模板本身要规范化,可接受)

### 决策 D-4:`/code ver` 写权限边界的最终方案
- **选择**(用户 2026-07-22 10:58 拍板):**opt.md §3.9 推荐方案 2** —— 保留自动同步,加差异预览 / 用户确认 / 失败回滚 / 提交记录
- **备选**:
  - A. opt.md §3.9 推荐方案 1 —— 默认只读 + 显式 `--sync-project-version`
  - B. opt.md §3.9 推荐方案 2 —— 保留自动同步 + 加确认/回滚(**已选**)
  - C. 完全只读 + 不提供同步能力
- **理由**:用户选择保留现有用户习惯(切换版本 = 自动同步项目文件),通过"加确认 + 加回滚"补强安全网
- **权衡**:方案 B 需要同步修改 SKILL.md 的"只读"声明(把声明改为"默认同步 + 加确认 + 加回滚"),改动面比方案 A 大;换取"用户习惯不被打断"
- **与 SKILL.md 声明的关系**:本决策要求同步修改 `references/ver/SKILL.md:48-53` 的"只读"声明,改为"默认同步 CWD 描述文件,加差异预览 / 用户确认 / 失败回滚 / 提交记录"

### 决策 D-5:`/code merge` target 默认值
- **选择**:默认 `origin/main`(与现有 FR-7 一致)
- **备选**:默认 `main`(本地分支)
- **理由**:与现有 FR-7 行为兼容,不动用户心智
- **权衡**:无

### 决策 D-6:`/code rule` Type B/C 的命运
- **选择**(用户 2026-07-22 10:42 在 clarifications 隐含确认):**保留**,但通过表格明确写权限
- **备选**:从公开命令中移除
- **理由**:opt.md §3.15 同时给出两种建议;当前仓库已有 Type B/C 使用记录(根 CLAUDE.md 的"AI 工作约定"区段就是 Type B 产物),直接移除会破坏现有数据
- **权衡**:接受 Type B/C 的存在,但要求"权限明文化"作为前置条件

## 7. 规范合规

| 规范文件 | 检查项 | 结果 |
| --- | --- | --- |
| 根 `CLAUDE.md` | "/code req 阶段纪律" — 严禁 EnterPlanMode / 严禁非 CODING 阶段改 CWD 源码 / 必须先建工作产物 | ✅ 本 DESIGN 仅写工作产物(DESIGN.md),不动 CWD 源码 |
| 根 `CLAUDE.md` | "AI 工作约定" — 看板展示策略 / 解析锚点 / 状态字面 / 工具集限制(Read/Glob/Grep,禁用 Write/Edit/Bash) | ✅ 本 DESIGN 解析锚点沿用 `^## .*$` + `^| .* |$`;工具集不引入 Write/Edit/Bash |
| `references/runtime-environment.md` | 运行时状态枚举只有 5 项;不记录路径到文档 | ✅ FR-10 输出对齐 |

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-22 10:50 | v1 | 初始创建 | DESIGN 阶段完成;15 模块 / 8 接口 / 6 决策;契约层独立文件 + 三层拆分(契约/同步/实现);NFR-6 约束下不预留新扩展点 | wangmiao |
| 2026-07-22 10:55 | v1.1 | 用户确认调整 | FR-13 移除旧 schema 兼容模式,直接就地升级到 dashboard-v2;FR-9 /code ver 默认行为变更待用户再次确认 | wangmiao |
| 2026-07-22 10:58 | v1.2 | D-4 拍板 | FR-9 改为方案 B(保留自动同步 + 加四步),SKILL.md "只读"声明需同步修改为"默认同步 + 加四步" | wangmiao |
