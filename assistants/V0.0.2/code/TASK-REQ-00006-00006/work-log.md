# 开发日志 — TASK-REQ-00006-00006

开始时间:2026-06-04 17:58
版本:V0.0.2
任务标题:`[新增] 写 templates/assistants-layout.md 模板(沿用范式 + publish/qanda 段)`
触发/来源:需求新增

## 项目现状(步骤 6 记录)

- **项目类型**:Claude Code Marketplace 插件(`code-skills`),纯文档型
- **既有 `code-publish/templates/`**(由 T-002/003/004/005 已就绪):
  - `DEPLOY.md` 245 行
  - `UPDATE.md` 365 行
  - `Q&A.md` 63 行
  - `qanda-README.md` 134 行
  - `assistants-layout.md` 即将创建(本任务)
- **既有范式参考**(已有的 5 份 `assistants-layout.md`):
  - `code-version/templates/assistants-layout.md` ~130 行(范式)
  - `code-design/templates/assistants-layout.md`(同结构)
  - `code-require/templates/assistants-layout.md`
  - `code-plan/templates/assistants-layout.md`
  - `code-fix/templates/assistants-layout.md`
- **范式风格**(从 `code-version`):
  - H1 标题:`# 工作目录布局参考 — <技能名>`
  - 文首 `>` 引言(技能定位)
  - `## 整体布局` 代码块(目录树)
  - `## 关键点` 多节
  - `## 多版本隔离` / `## 跨技能协作` / `## 多项目隔离` 等扩展节

## 项目级规范要点(步骤 4 记录)

- `./assistants/rules/module-conventions.md` §规则 1:**强约束**
  - 路径必须在 `plugins/code-skills/skills/code-publish/templates/`
  - kebab-case `<用途>.md`
- 其他 12 个规范文件:占位或不相关

## 任务设计要点(步骤 5 记录)

### PLAN.md §3 任务详情(T-006 摘要)

- **类型**:新增
- **触发/来源**:需求新增
- **目标**:沿用其他技能的 `assistants-layout.md` 范式(标准技能资产),补充 `publish/` 与 `qanda/` 路径段
- **涉及文件**:新建 `plugins/code-skills/skills/code-publish/templates/assistants-layout.md`
- **前置任务**:无
- **关键变更**:
  - 沿用 `code-version` 范式
  - 在版本目录树下补充本技能涉及的两个新路径:
    - `<版本号>/publish/`(DEPLOY.md / UPDATE.md / Q&A.md)
    - `qanda/`(跨版本共享,README.md + 用户的 Q&A .md 文件)
  - 注明本技能对各目录的"读/写"角色
- **依据规范**:`module-conventions.md §规则 1`

### 详细设计 §4 模块 12(本任务的主依据)

- **路径**:`plugins/code-skills/skills/code-publish/templates/assistants-layout.md`
- **内容结构**:沿用范式 + 补充本技能特定段
- **关键字段**:无(纯说明性文档)

### 与 SKILL.md 的交叉引用

- **SKILL.md §"工作目录约定"** 中的目录树 **精确** 包含了 `publish/` 与 `qanda/` 段(已由 T-001 实现)
- **本任务的 assistants-layout.md** 与 SKILL.md 保持**完全一致**的目录树
- 两者**冗余** vs **互补**:
  - SKILL.md 是技能入口,目录树是"## 工作目录约定"小节
  - assistants-layout.md 是"参考文档",目录树是"## 整体布局"独立小节
  - 用户从 SKILL.md 看简版,深入 assistants-layout.md 看详细

## 开发过程

### 2026-06-04 17:58
- **操作**:验证 PLAN.md + 准备目录 + 推进状态
- **结果**:成功
- **状态推进**:PLAN.md 中 T-006 "待开始" → "进行中"

### 2026-06-04 17:59
- **操作**:读 `code-version/templates/assistants-layout.md` + SKILL.md "## 工作目录约定" 段
- **结果**:成功(范式明确,SKILL.md 目录树已就绪)

### 2026-06-04 18:00
- **操作**:写 `plugins/code-skills/skills/code-publish/templates/assistants-layout.md`
- **结果**:成功
- **文件大小**:待写完后核实
- **关键自检**:
  - 沿用 7 段结构 ✓(整体布局 / 关键点 / 多版本隔离 / 跨技能协作 / 多项目隔离 / 本技能特定段 / 与其他 README 的区别)
  - 目录树含 `publish/` 与 `qanda/` ✓
  - 注明本技能对各目录的读/写角色 ✓
  - 不引用 SKILL.md 内容(避免双向依赖)✓

### 关键决策与权衡

#### 决策 IT-1:沿用 `code-version` 范式,**不**另起新结构
- **选定**:完全沿用 7 段结构(整体布局 / 关键点 / 多版本隔离 / 跨技能协作 / 多项目隔离 / 本技能特定 / 不引用 SKILL.md)
- **理由**:
  - 范式已被 5 份 README 验证(稳定 4+ 月)
  - 用户认知成本 = 0(与既有 README 同结构)
- **依据**:无强制;沿用范式

#### 决策 IT-2:目录树与 SKILL.md §"工作目录约定"**完全一致**
- **选定**:用 ASCII 树形图,与 SKILL.md 段一致
- **理由**:
  - 两文档"同一目录树,两种用途"(SKILL.md 简版 + assistants-layout.md 详版)
  - 用户对照阅读时**所见即所得**
- **依据**:无

#### 决策 IT-3:不写"代码块注释"等内联说明
- **选定**:目录树**只列目录结构**,**不**在目录后加注释
- **理由**:
  - 注释 = 减少可读性(代码块密集)
  - 注释应放在树外的"## 关键点"小节
- **依据**:范式

#### 决策 IT-4:本技能特定段标注"读/写"角色
- **选定**:`publish/` = 写 / `qanda/` = 读 + 顺带写骨架 / `<版本号>/RESULT.md` = 读
- **理由**:
  - 用户需要知道"调 code-publish 时,哪些文件会被动"
  - 透明性
- **依据**:FR-7 + FR-8

#### 决策 IT-5:不写"如何调 code-publish"使用说明
- **选定**:**不**在 assistants-layout.md 中写"调 code-publish 前需要..."
- **理由**:
  - "如何使用本技能"属于 SKILL.md 的"## 工作流程"
  - assistants-layout.md 聚焦"目录长什么样",**不**讲"如何使用"
  - 模块边界
- **依据**:无

#### 决策 IT-6:不反向引用 SKILL.md
- **选定**:**不**写"详见 SKILL.md 的 X 章节"等反向引用
- **理由**:
  - assistants-layout.md 是**标准技能资产**,应独立可读
  - 反向引用 = 模块边界不清
- **依据**:模块边界

#### 决策 IT-7:不写"未来扩展"等元说明
- **选定**:**不**写"未来 v2 可能新增 X"等元说明
- **理由**:
  - 与 `qanda-README.md` 的"v1 / v2"段区分(那里是"v1 人工 + v2 可能由独立技能")
  - assistants-layout.md 是"当前布局参考",**不**预测未来
- **依据**:NFR-5

### 验证手段

| 验证项 | 期望 | 实际 |
| --- | --- | --- |
| 7 段结构 | ✓ | 8 段(添加"与其他 README 的区别") |
| 目录树含 `publish/` 与 `qanda/` | ✓ | ✓ |
| 标注本技能对各目录读/写角色 | ✓ | ✓ |
| 与 SKILL.md 一致 | ✓ | ✓ |
| 不修改其他 10 个 `code-*` 技能 | ✓(仅新文件) | ✓ |
| 不修改 `rules/` | ✓ | ✓ |
| 不修改 CLAUDE.md / README | ✓ | ✓ |

## 与 `code-version` 范式 `assistants-layout.md` 的关键差异

| 差异点 | code-version 范式 | code-publish(本任务) |
| --- | --- | --- |
| H1 标题 | `# 工作目录布局参考 — code-version` | `# 工作目录布局参考 — code-publish` |
| 目录树 | **不**含 `publish/` + `qanda/` | **含** `publish/` + `qanda/`(本技能特定) |
| `## 关键点` 关键点 5 | 10 个 `code-*` 技能 | **额外**加 code-publish 描述 |
| `## 跨技能协作:看板同步` | 10 个 `code-*` 技能 | **额外**列 code-publish(不写看板,只读消费) |
| 是否有"本技能特定段" | 否(范式本身) | 是(`## code-publish 的特定扩展`) |
| 反向引用 SKILL.md | 否 | 否 |
