# 现有功能需求 — EXISTING-001:工程初始化(code-init)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-init` 是项目的"一次性引导"技能:扫描现有源码,生成 `INIT-REPORT.md` 功能分析报告,把每个已有功能登记为 `require/EXISTING-NNN/`,创建基线版本工作空间。运行完成后,用户应调 `code-version` 开启新开发版本。**一个项目只应被 `code-init` 一次**。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-init/SKILL.md`(417 行) |
| 关键函数/类 | (N/A,技能为 Markdown 工作流,无可调用函数) |
| 涉及文件数 | 4(SKILL.md + 3 个模板 + assistants-layout.md) |
| 大致代码量 | 约 450 行(含 3 个模板) |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-init/SKILL.md:1-100` — 目标、适用场景、不适用场景、工作目录约定
- `plugins/code-skills/skills/code-init/SKILL.md:工作流程段` — 9 个步骤(0 收集版本号 → 1 探查 assistants/ → 1.5 决策分支 → 2 建骨架 → 3 写 current-version → 4 写 RESULT.md → 5 分析源码 → 6 写 INIT-REPORT → 7 写 EXISTING-NNN → 8/9 引导)
- `plugins/code-skills/skills/code-init/templates/INIT-REPORT.md` — 功能分析报告模板
- `plugins/code-skills/skills/code-init/templates/existing-requirement.md` — 现有功能需求模板
- `plugins/code-skills/skills/code-init/templates/assistants-layout.md` — assistants/ 目录布局约定

## 用户角色与场景

### 角色
- **项目负责人**(首次接入新/老项目,跑一次)

### 场景
- 全新空项目接入:扫描 CWD 无源码,直接建基线版本,跳过代码分析
- 老项目接入:扫描现有代码、登记 M 个现有功能为 `EXISTING-001~M`,基线版本看板显示 M 个"已完成"需求
- 项目重置(极少):用户明确确认后,`code-init` 增量补齐 `INIT-REPORT.md` 与 `EXISTING-NNN`

## 功能点(FR)

- **FR-1**:收集初始版本号(默认 `V0.0.0`,支持 semver/日期风格),校验不含路径分隔符与 Windows 保留字符
- **FR-2**:探查 `./assistants/` 现状,推断 `assistants_exists` / `previous_current_version` / `existing_versions` / `source_file_count`
- **FR-3**:四种决策分支处理(全新 / 部分初始化 / 版本号重名 / 完全已初始化)
- **FR-4**:创建 `./assistants/{rules, V0.0.0/{require, review, design, plan, code, test}}` 骨架目录
- **FR-5**:写入 `./assistants/.current-version` 为初始版本号
- **FR-6**:写入 `./assistants/<版本号>/RESULT.md` 版本看板(含 M0:工程初始化 里程碑,状态=已完成)
- **FR-7**:分析现有代码(项目类型识别/目录结构/入口/模块/数据模型/依赖/约定/可复用资产/技术债),生成 `INIT-REPORT.md`
- **FR-8**:把现有功能拆为 M 个用户可识别项,逐个写 `require/EXISTING-NNN/RESULT.md`
- **FR-9**:回填版本看板"需求清单" + 更新统计 + 追加变更记录
- **FR-10**:引导用户:汇报 `rules/` 状态、调 `code-rule` 补规范、调 `code-version` 开新版本

## 关键接口

### CLI(用户调用形式)
```
/code-skills:code-init
/code-skills:code-init V0.0.0
/code-skills:code-init 2026-06
```

### 模板输出(由 `code-init` 调用方/下游读取)
- `./assistants/.current-version` — 文件内容 = `<初始版本号>\n`
- `./assistants/<初始版本号>/RESULT.md` — 版本看板(基于 `version-RESULT.md` 模板)
- `./assistants/<初始版本号>/INIT-REPORT.md` — 功能分析报告
- `./assistants/<初始版本号>/require/EXISTING-NNN/RESULT.md` — 现有功能 ×N

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 版本工作空间 | `<版本号>/` 目录 | 含 RESULT.md / INIT-REPORT.md(仅基线)/ require/EXISTING-NNN/RESULT.md × M |
| 现有功能 | `EXISTING-NNN` 文件夹名 | 3 位数字,从 001 起递增,全局唯一 |
| 需求模板 | `templates/existing-requirement.md` | 字段:概述/实现位置/角色场景/FR/接口/数据模型/AC/关联/技术债/变更记录 |

## 验收标准(AC)

- **AC-1**:跑完 `code-init` 后,`./assistants/.current-version` 内容等于初始版本号
- **AC-2**:`./assistants/V0.0.0/RESULT.md` 存在,含 M0 里程碑(状态=已完成)与至少 1 条变更记录
- **AC-3**:有源码时,`./assistants/V0.0.0/INIT-REPORT.md` 存在,覆盖项目概述/技术栈/目录结构/核心模块/入口/外部接口/数据模型/构建/测试/可复用资产/技术债
- **AC-4**:有源码时,`./assistants/V0.0.0/require/EXISTING-NNN/RESULT.md` 数量等于分析得出的功能数 M
- **AC-5**:每份 `EXISTING-NNN/RESULT.md` 的"现有实现位置"引用了真实存在的文件路径
- **AC-6**:`code-init` **不**修改任何项目源代码(只读分析)
- **AC-7**:`code-init` **不**写入 `./assistants/rules/` 下任何文件(那是 `code-rule` 的职责)
- **AC-8**:情形 D(完全已初始化)下,未得到用户确认前不会创建新基线

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-002 | `code-version` 接续 `code-init` 创建的基线版本,开启新开发版本 | `code-init` 完成后必须调 `code-version` 才能进入主流程 |
| EXISTING-003 | `code-rule` 补齐 `./assistants/rules/` 后,所有下游技能都受影响 | `code-init` 后建议先调 `code-rule` 再 `code-version` |
| EXISTING-004 ~ 010 | `code-init` 生成的 `EXISTING-NNN` 格式与 `code-require` 的 `REQ-YYYY-NNNN` 格式对齐 | 未来对这些功能的修改可走 `code-require` 增量更新 |

## 已知限制/技术债

- 项目体量极大(> 10k 行)时,步骤 5 的"分析现有代码"可能需要分批;SKILL.md 未规定分批策略
- "功能边界拆分"在 M > 5 时会主动用 `AskUserQuestion` 让用户选择粒度,但小项目直接按"用户可见功能"拆分,粒度判断仍依赖 AI
- 情形 C(版本号重名)复用现有目录时,只补 `INIT-REPORT.md` 与 `EXISTING-NNN`,**不**重写 `RESULT.md` —— 已有的变更记录得以保留
- `EXISTING-NNN` 编号一旦分配**不会**回收(被取消的 EXISTING 编号仍占位)

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-001 | EXISTING-001 |
