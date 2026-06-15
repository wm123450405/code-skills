# 需求提示词文档 — 明文契约化 `code-require` 不涉及技术选型(只确定功能点)

- 需求编码:REQ-00033
- 所属版本:V0.0.3
- 文档创建时间:2026-06-15 11:10
- 最近更新:2026-06-15 11:10
- 文档状态:草稿(待 code-design 推进)
- 上游:无(用户口头/文本输入,2026-06-15 11:00,经 1 轮 AskUserQuestion 澄清)
- 遵循规范:`./assistants/rules/` 下 7 个文件(全沿用,无新增)
- 涉及技能:`code-require`(本需求唯一改造对象)

## 1. 需求概述

在 `code-require/SKILL.md` 中**显式**明文契约化"`code-require` 不涉及技术选型 / 技术栈 / 技术方案的确定,只确定功能点(FR / NFR / 页面 / 交互 / 数据 / 边界);技术选型归 `code-design`"。**没有**必要进行技术选型的需求,**无需**在 `code-require` 阶段分析技术选型选项。本需求属"**职责边界显式化**"型(把隐含契约落到文字),**不**新增模块 / 接口 / 数据结构 / 看板字段。

## 2. 背景与目标

### 2.1 背景

当前 `code-require` 全文(2026-06-15 经 Grep 校验)关于"技术选型"**0 命中**:
- 隐含契约:`code-require` 产出 = "详尽、可执行、可追溯的需求提示词文档"(§"目标"段),不涉及"用什么技术实现"
- 隐含风险:契约是**隐含**的,新读者 / AI agent 可能误读为"`code-require` 应回答技术选型"或"把技术选型写进 RESULT.md 模板"

同时,`code-design` 端**显式**承担技术选型:
- §"目标"段:基于需求 + 项目实际状况(语言/框架/既有模块/既有接口)给出架构方案
- 模板字段含"技术选型偏好 / 数据存储选型 / 接口风格"(SKILL.md L233 / L262 / L310 附近)
- §"目标"段第 13 行:跨模块的方案选型

结论:用户的话**与现状一致**,本需求是"**明文契约化**"——把隐含边界显式落到 `code-require/SKILL.md` 文字,避免后续误读 / 越界。

### 2.2 业务目标

- 显式化 `code-require` 端"不涉及技术选型"硬约束,降低跨技能误读风险
- 显式化 `code-design` 端"承担技术选型"职责(通过对偶引用,不修改 `code-design` SKILL.md)
- 屏幕日志 / RESULT.md 模板**不**追加"哪些需求需技术选型"判据表(由 `code-design` 自由裁量)

### 2.3 本次目标

- 范围:仅修改 `plugins/code-skills/skills/code-require/SKILL.md` 1 段(§"不要做的事"小节追加 1 条)
- 不涉及:`code-design` / `code-plan` / `code-it` / `code-unit` / `code-check` / `code-fix` / `code-auto` / `code-init` / `code-version` / `code-rule` / `code-dashboard` / `code-answer` 12 个 SKILL.md
- 不涉及:`plugins/code-skills/skills/code-require/templates/requirements.md`(NFR-2 零规范变更)
- 不涉及:`assistants/V0.0.3/require/REQ-00033/RESULT.md` 自身结构(本需求产出物即本文件)
- 触发 1 次看板同步:`assistants/V0.0.3/RESULT.md` §需求清单 追加 1 行 + §变更记录 追加 1 条

## 3. 用户角色与场景

### 3.1 角色

- **项目开发者**:使用 `code-require` 登记需求时,期望清晰知道"`code-require` 不会回答用什么技术"
- **AI 协作流程的用户**:跨 `code-require` → `code-design` → `code-plan` 时,期望边界清晰无歧义
- **新读者 / 维护者**:首次阅读 `code-require/SKILL.md` 时,期望在显著位置看到该技能的"不涉及"清单

### 3.2 场景

| 场景 | 现状体验 | 改造后体验 |
| --- | --- | --- |
| 用户在 `code-require` 阶段问"这个需求用什么技术栈实现?" | 无显式回答,AI 自由裁量,可能越界到 `code-design` 职责 | 完成后,`code-require` 阶段屏显 / RESULT.md 都不含技术选型;`code-design` 阶段统一承担 |
| 维护者读 `code-require/SKILL.md` 想确认"这技能到底做不做技术选型" | 需通读全文 + 推断"目标"段语义;Grep 0 命中"技术选型",但**无显式声明** | §"不要做的事"小节直接列出"不涉及技术选型 / 技术栈 / 技术方案"(FR-2 锁定) |

## 4. 功能需求(FR)

### FR-1:`code-require` 端 0 产出技术选型内容

- **触发位置**:`code-require` 步骤 5A(首次分析) / 步骤 5B(增量更新) / 步骤 7A 澄清 / 步骤 8A 撰写 RESULT.md
- **不产出范围**(在 RESULT.md / 屏幕日志 / 任何过程文档中**均不**出现):
  - **技术选型**:语言 / 框架 / 库 / 存储 / 中间件(FR-1.1)
  - **架构风格**:分层 / 微服务 / 事件驱动 / 六边形(FR-1.2)
  - **接口风格**:REST / GraphQL / gRPC / 消息队列(FR-1.3)
  - **数据模型**:库表 / 字段类型 / 索引(FR-1.4)
  - **部署形态**:单机 / 集群 / 容器 / K8s(FR-1.5)
- **可保留范围**(本技能**仍**产出,因属"功能点"):
  - 功能点(FR)
  - 非功能需求(NFR:性能 / 安全 / 可用性 / 合规 / 可观测性 / 兼容性)
  - 页面与界面(布局 / 组件 / 样式)
  - 交互逻辑(状态机 / 流程)
  - 数据与状态(**业务实体**层,不涉及**库表层**)
  - 边界与异常
- **失败降级**:`code-require` 误产出技术选型 → 在 `code-check` 评审时由"§不要做的事"小节兜底校验(本需求**不**实现 `code-check` 改造,留作 follow-up)

### FR-2:在 `code-require/SKILL.md` §"不要做的事"小节追加 1 条硬约束

- **精确位置**:`plugins/code-skills/skills/code-require/SKILL.md` 中"## 不要做的事"小节末尾(沿用 BUG-00001 范式)
- **新增条目措辞**(锁定):
  ```
  - 不涉及技术选型 / 技术栈 / 技术方案的确定:本技能只确定功能点(FR / NFR / 页面 / 交互 / 数据 / 边界);技术选型 / 架构风格 / 接口风格 / 数据模型(库表层) / 部署形态归 `code-design`(由其结合项目实际状况给出方案);没有**必要**进行技术选型的需求,**无需**在 `code-require` 阶段分析技术选型选项。
  ```
- **位置理由**(Q-3 隐含确认,见 `clarifications.md`):
  - 候选 §"目标"段:偏泛,放"边界"语义略偏(拒)
  - 候选 §"工作流程"步 5A/8A 段内:位置过深,首屏不可见(拒)
  - **候选 §"不要做的事"小节**:沿用 BUG-00001 同类范式,语义最清晰(选)
  - 候选新增 §"范围外"小节:净增行数最多,违反 NFR-2 最小化变更(拒)
- **NFR-1 字节级保留**:`code-require/SKILL.md` frontmatter L1-3 字节级保留(沿用 INV-1);§"工作流程"既有段 0 改(本需求**只**追加,不改既有)
- **NFR-2 模板零规范变更**:`plugins/code-skills/skills/code-require/templates/requirements.md` 0 改

### FR-3:对偶引用 `code-design` 承担技术选型

- **引用方式**:在 FR-2 新增条目中**显式**对偶引用"`code-design`(由其结合项目实际状况给出方案)"
- **不修改 `code-design/SKILL.md`**:本需求**不**在 `code-design` 端加"## 必做"段(避免越界)
- **不引入看板字段**:本需求**不**在 `V0.0.3/RESULT.md` §"需求清单" 加"涉及技术选型" 列(沿用既有 7 列结构)
- **不引入 RESULT.md 模板字段**:`templates/requirements.md` 0 改(FR-1 限定本技能 0 产出技术选型,**不**约束模板)

### FR-4:不修改其他 11 个 `code-*` 技能 SKILL.md

- **不修改**:
  - `code-design` / `code-plan` / `code-it` / `code-unit` / `code-check` / `code-fix` / `code-auto` / `code-init` / `code-version` / `code-rule` / `code-dashboard` / `code-answer` 12 个 SKILL.md(INV-4 字节级保留;实际 11 个非本技能 + 1 个本技能,共 12 个含 `code-require` 自身)
  - 既有 12 个 REQ 的 RESULT.md(INV-7 字节级保留;既有 REQ-00020 ~ REQ-00032)
  - 7 个项目级规范(INV-5)
  - 4 个 README / marketplace / plugin / CLAUDE.md(INV-6)
  - `plugins/code-skills/skills/code-require/templates/requirements.md`(NFR-2 零规范变更)
- **范围限定**:本需求**只**修改 `code-require/SKILL.md` 1 段(§"不要做的事"小节追加 1 条)

## 5. 非功能需求 / 约束(NFR)

- **NFR-1 字节级保留**:`code-require/SKILL.md` frontmatter L1-3 字节级保留;§"工作流程"既有段 0 改(沿用 INV-1 / INV-2)
- **NFR-2 模板零规范变更**:`plugins/code-skills/skills/code-require/templates/requirements.md` **不**修改(沿用 REQ-00032 NFR-2)
- **NFR-3 净增行数**:本需求在 `code-require/SKILL.md` 净增 **+2 ~ +4 行**(1 条 markdown 列表项;沿用 REQ-00026 NFR-6 最小化变更原则)
- **NFR-4 幂等性**:多次执行 `code-require` 涉及本硬约束时,屏显 / 行为**不**累积(本硬约束是"不产出",无副作用累积风险)
- **NFR-5 不引入新依赖**:0 新增三方依赖
- **NFR-6 与 REQ-00032 协同**:REQ-00032 锚点 = §"工作流程 步骤 10A/10B 段内文末";本需求锚点 = §"不要做的事" 段;无交叉
- **NFR-7 不引入"哪些需求需技术选型"判据表**:沿用用户原始输入"**没有**必要进行技术选型的需求**无需**分析技术选型选项";`code-require` 端**只**做"不提技术选型"的硬约束,**不**给出反向判据
- **NFR-8 不引入"是否需要技术选型"用户偏好**:本需求**不**在 `code-require` 步骤 7A 澄清中新增"本需求是否需要技术选型"问路(用户已显式回答"无需分析",无需再问)
- **NFR-9 看板三同步**:`V0.0.3/RESULT.md` §"需求清单" 追加 1 行(REQ-00033) + §"变更记录" 追加 1 条;统计数字刷新;不触发 dashboard-conventions 字段扩展
- **NFR-10 不引入新任务类型 / 新测试类型**:沿用 REQ-00031 元技能改规则;本需求无 `code-plan` / `code-it` / `code-unit` 任务
- **NFR-11 不变更状态机**:`code-fix` 状态机 5 候选状态 0 改(沿用 REQ-00027)

## 6. 页面与界面

不适用(本需求无 UI 变更)。

## 7. 交互逻辑(状态机、关键流程)

### 7.1 边界判定流程

```
材料进入 code-require
  ↓
提取候选需求(FR / NFR / 页面 / 交互 / 数据 / 边界)
  ↓
本技能**不**判定"是否需要技术选型"(由 code-design 自由裁量)
  ↓
输出 RESULT.md(0 包含技术选型)
  ↓
(code-design 阶段)若需技术选型,code-design 给出方案
```

### 7.2 code-require 与 code-design 边界状态机

```
+-------------------------+        +-------------------------+
|     code-require         |        |     code-design          |
|  - 提取功能点             | -----> |  - 技术选型               |
|  - 写 NFR                |  交接  |  - 架构风格               |
|  - 0 产出技术选型         |        |  - 接口风格               |
|  (本硬约束,FR-1 锁定)    |        |  - 数据模型(库表层)       |
+-------------------------+        +-------------------------+
```

## 8. 数据与状态

### 8.1 内部变量(非文档字段)

无新增内部变量(本需求是"不产出"型约束,无状态机变更)。

### 8.2 文档结构变更(本需求产出)

| 文档 | 变更类型 | 位置 | 行数变化 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-require/SKILL.md` | 追加 1 条列表项 | §"不要做的事" 小节末尾 | +2 ~ +4 行 |
| `assistants/V0.0.3/RESULT.md` | 追加 1 行 | §"需求清单" 表格 | +1 行 |
| `assistants/V0.0.3/RESULT.md` | 追加 1 条 | §"变更记录" 表格 | +1 行 |

## 9. 边界与异常

- **E-1**(材料含技术选型字面):`code-require` **不**主动提取;若用户**强提示**"本需求就是需要技术选型",`code-require` 沿用既有"用户口头补充"语义,放进"## 12 待澄清"或"## 13 变更记录",**不**进 FR-1 ~ FR-5
- **E-2**(材料 0 含技术选型字面):`code-require` **不**主动加技术选型条目(沿用 FR-1)
- **E-3**(`code-require` 重入):本硬约束**不**累积(沿用 NFR-4)
- **E-4**(增量更新 / 步骤 5B):同样触发 FR-1 硬约束,本硬约束**不**因增量更新而失效
- **E-5**(用户在建议前中断):`code-require` 既有"中止"逻辑(本需求不介入)
- **E-6**(本仓库无项目级规范):沿用 `code-require` 既有 `AskUserQuestion`(本需求不介入)
- **E-7**(`code-require` 误产出技术选型 → `code-check` 评审):本需求**不**实现 `code-check` 改造,留作 follow-up(本硬约束的"事后校验"是流程约定,非代码)

## 10. 验收标准(AC)

### AC-1:`code-require` 0 产出技术选型

- **AC-1.1** `code-require` 步骤 5A 提取的候选需求中**不**含"技术选型 / 技术栈 / 技术方案 / 选型" 字面关键词(FR-1 锁定;经 Grep `RESULT.md` 校验)
- **AC-1.2** `code-require` 步骤 8A 输出的 RESULT.md "## 4 功能需求" / "## 5 NFR" / "## 6 页面" / "## 8 数据" 章节**不**含库表层数据模型 / 语言 / 框架 / 库 / 中间件字面
- **AC-1.3** `code-require` 屏幕日志**不**出现"建议用 X 语言 / Y 框架"等输出
- **AC-1.4** 业务实体层字段(FR / NFR / 页面 / 交互)保留(FR-1 "可保留范围")

### AC-2:`code-require/SKILL.md` 硬约束落地

- **AC-2.1** `plugins/code-skills/skills/code-require/SKILL.md` §"不要做的事"小节**新增** 1 条,内容**完全包含**以下 3 个语义子句(FR-2 锁定):
  - 子句 1:"不涉及技术选型 / 技术栈 / 技术方案的确定"
  - 子句 2:"技术选型归 `code-design`"
  - 子句 3:"没有**必要**进行技术选型的需求,**无需**在 `code-require` 阶段分析技术选型选项"
- **AC-2.2** `code-require/SKILL.md` frontmatter L1-3 字节级保留(NFR-1 / INV-1)
- **AC-2.3** `code-require/SKILL.md` §"工作流程" 既有段 0 改(NFR-1 / INV-2);本需求**只**在 §"不要做的事"小节末尾**纯追加** 1 条
- **AC-2.4** `code-require/SKILL.md` 净增行数 **+2 ~ +4 行**(NFR-3 锁定)
- **AC-2.5** 硬约束措辞与 FR-2 锁定措辞**完全一致**(经 git diff 校验,无 typo 漂移)

### AC-3:零变更校验

- **AC-3.1** 其他 11 个 `code-*` 技能 SKILL.md 0 改(`code-design` / `code-plan` / `code-it` / `code-unit` / `code-check` / `code-fix` / `code-auto` / `code-init` / `code-version` / `code-rule` / `code-dashboard` / `code-answer`;INV-4)
- **AC-3.2** 既有 12 个 REQ 的 RESULT.md 0 改(REQ-00020 ~ REQ-00032;INV-7)
- **AC-3.3** 7 个项目级规范 0 改(INV-5)
- **AC-3.4** 4 个 README / marketplace / plugin / CLAUDE.md 0 改(INV-6)
- **AC-3.5** `plugins/code-skills/skills/code-require/templates/requirements.md` 0 改(NFR-2 零规范变更)
- **AC-3.6** `code-fix` 5 候选状态机 0 改(NFR-11)
- **AC-3.7** `code-dashboard` 算法 0 改(AC-3.1 已覆盖)
- **AC-3.8** `code-auto` 5 种路径感知模式 0 改(AC-3.1 已覆盖)

### AC-4:看板同步

- **AC-4.1** `assistants/V0.0.3/RESULT.md` §"需求清单" 追加 1 行:需求编码 = REQ-00033,标题 = "明文契约化 `code-require` 不涉及技术选型(只确定功能点)",状态 = "草稿"
- **AC-4.2** `assistants/V0.0.3/RESULT.md` §"变更记录" 追加 1 条:`2026-06-15 11:10  需求新增  REQ-00033 需求分析完成(...)  REQ-00033`
- **AC-4.3** `assistants/V0.0.3/RESULT.md` 统计区段"总数 + 1"(NFR-9;由 code-require 步骤 9A 自动刷新)
- **AC-4.4** 看板其他区段(概要设计清单 / 详细设计 / 任务清单 / 缺陷清单 / 评审发现 / 派生任务)0 改(本需求尚未推进到 design / plan / it / check)

### AC-5:与既有规则协同

- **AC-5.1** 沿用 REQ-00030 元技能改规则(本需求只改 1 个 SKILL.md,1 段)
- **AC-5.2** 沿用 REQ-00031 元技能改规则(本需求不涉及 /code-unit,不涉及任务类型变更)
- **AC-5.3** 沿用 REQ-00032 屏显契约(本需求**不**涉及屏显建议,只改 SKILL.md 文字)
- **AC-5.4** 沿用 BUG-00001 §"不要做的事" 范式(本需求 FR-2 锚点 = §"不要做的事" 小节)
- **AC-5.5** 沿用 REQ-00026 最小化变更原则(NFR-3 净增 +2 ~ +4 行)

## 11. 关联需求

| 需求 | 版本 | 关联点 | 影响 |
| --- | --- | --- | --- |
| BUG-00001 | V0.0.3 | 5 技能加"不修改 SKILL.md"硬约束(范式 = §"不要做的事" 小节) | 沿用同套范式;本需求锚点 = §"不要做的事" 小节 |
| REQ-00026 | V0.0.3 | SKILL.md 描述通用化扫除 | 沿用最小化变更原则;本需求净增 +2 ~ +4 行 |
| REQ-00030 | V0.0.3 | 元技能改 + 12 维度评审 + INV 字节级保留 | 沿用 INV 校验;本需求只改 1 段 |
| REQ-00031 | V0.0.3 | 元技能改 /code-plan /code-it /code-unit /code-auto | 沿用元技能改路径;本需求**不**涉及 /code-unit |
| REQ-00032 | V0.0.3 | code-require 步骤 10A/10B 末尾追加"下一步建议"段 | 同属 code-require 增量改造;锚点不交叉(REQ-00032 = §"工作流程 步骤 10A/10B 段内文末";本需求 = §"不要做的事" 小节) |
| REQ-00007 | V0.0.3 | `code-auto` 整版本自动流水线 | 不涉及(本需求不触发 /code-auto 路径) |
| REQ-00025 | V0.0.3 | 编码 / 字符数 / 屏显格式 | 沿用 |

## 12. 待澄清 / 未决项

- **Q-1**(`code-check` 是否需要加"`code-require` 0 产出技术选型"校验点):本需求**不**实现(避免越过本需求边界到 `code-check` 改造);留作 follow-up REQ
- **Q-2**(本需求是否需要 `code-require` 步骤 7A 澄清中新增"本需求是否需要技术选型"问路):**不**新增(用户已显式回答"无需分析";NFR-8 锁定)
- **Q-3**(`code-design` 端是否需要加"## 必做"段对偶声明):本需求**不**实现(避免越界 `code-design` 改造);留作 follow-up
- **Q-4**(`templates/requirements.md` 是否需要在 §4 / §5 章节追加"不含技术选型"提示):本需求**不**实现(NFR-2 零规范变更);留作 follow-up
- **Q-5**(本需求对偶引用 `code-design` 时,是否在 `code-design/SKILL.md` 加反向引用):**不**修改 `code-design` SKILL.md(FR-3 锁定);由 `code-design` 端在后续 REQ 自由裁量

## 13. 变更记录

```
2026-06-15 11:10  需求新增  REQ-00033 需求分析完成(共 4 FR / 11 NFR / 23 AC),本需求唯一改造对象 = code-require/SKILL.md §"不要做的事" 小节追加 1 条硬约束(不涉及技术选型);0 改 frontmatter / templates / 其他 11 个 SKILL.md / 既有 12 个 REQ / 7 项目级规范 / 4 README 等  REQ-00033
```
