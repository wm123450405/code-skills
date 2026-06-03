# 现有功能需求 — EXISTING-002:版本管理(code-version)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-version` 是所有其他 `code-*` 技能(主流程)的**前置门**:负责切换/创建版本工作空间。用户输入一个版本号,若工作空间已存在则切换;若不存在则在 `./assistants/<版本号>/` 下创建 `RESULT.md` 看板,最后写入 `./assistants/.current-version` 作为激活标记。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-version/SKILL.md`(204 行) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 3(SKILL.md + 2 个模板) |
| 大致代码量 | 约 250 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-version/SKILL.md` — 工作流(校验版本号 → 探查 assistants/ → 创建或切换 → 写 RESULT.md → 写 .current-version → 引导)
- `plugins/code-skills/skills/code-version/templates/version-RESULT.md` — 版本看板模板(本项目已采用)
- `plugins/code-skills/skills/code-version/templates/assistants-layout.md` — assistants/ 目录布局

## 用户角色与场景

### 角色
- **项目开发者**:启动新版本、切换版本、归档/回看历史

### 场景
- 首次使用或开新开发版本:输入 `V0.1.0`,创建对应工作空间
- 跨版本回看:输入旧版本号,只读浏览该版本的 `RESULT.md` 与所有子目录
- 切换当前激活:在多个版本工作空间间来回切换

## 功能点(FR)

- **FR-1**:接收版本号(交互式或参数),校验非空且不含路径分隔符与 Windows 保留字符
- **FR-2**:探查 `./assistants/<版本号>/` 是否存在,决定"创建"还是"切换"
- **FR-3**:**创建**时,在 `./assistants/<版本号>/` 下写入 `RESULT.md`(基于 `version-RESULT.md` 模板)
- **FR-4**:**切换**时,不修改任何版本工作空间内容
- **FR-5**:写入 `./assistants/.current-version` 为当前版本号(创建与切换都会做)
- **FR-6**:汇报"当前激活版本"与下一步建议(新版本无需求 → 调 `code-require`;已有需求 → 调 `code-design` / `code-plan`)

## 关键接口

### CLI
```
/code-skills:code-version
/code-skills:code-version V0.1.0
/code-skills:code-version 2026-Q2
```

### 写入
- `./assistants/.current-version` — 文件内容 = `<版本号>\n`(创建与切换都会覆写)
- `./assistants/<版本号>/RESULT.md` — 创建新版本时才生成

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 激活版本标记 | `.current-version` 文件内容 | 字符串,等于已存在的 `<版本号>/` 目录名之一 |
| 版本工作空间 | `<版本号>/` 目录 | 必含 `RESULT.md`;其余子目录(需/设/计/码/测/评)由后续技能按需创建 |
| 版本看板 | `RESULT.md` | 10 段固定结构:文档头 / 版本信息 / 里程碑 / 需求清单 / 概要设计清单 / 详细设计与任务计划汇总 / 任务清单 / 缺陷清单 / 评审发现汇总 / 派生任务记录 / 执行的开发命令记录 / 变更记录 / 索引 |

## 验收标准(AC)

- **AC-1**:首次跑 `code-version V0.1.0`,`./assistants/V0.1.0/RESULT.md` 被创建,内容符合 `version-RESULT.md` 模板结构
- **AC-2**:跑完任何一次 `code-version`,`./assistants/.current-version` 内容 = 所输入的版本号
- **AC-3**:切换到已存在版本(如 `code-version V0.0.0`),不修改该版本工作空间任何内容
- **AC-4**:版本号校验拒绝含 `/` `\` `:` `*` `?` `"` `<` `>` `|` 的输入
- **AC-5**:版本号与已存在版本重名时,走"切换"分支,不创建重复目录

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-001 | `code-init` 创建基线版本 = `code-version V0.0.0` 的特化 | `code-init` 完成后 `.current-version` 已指向基线 |
| EXISTING-003 | `code-rule` 不做版本感知,可在任何 `code-version` 之前/之后调用 | 无顺序约束 |
| EXISTING-004 ~ 010 | 全部主流程技能的第一步都是读 `.current-version` | `code-version` 是它们的强制前置 |

## 已知限制/技术债

- **不**支持版本号重命名(若想改,只能新建版本 + 手动迁移文件)
- **不**内置"列出所有版本"命令(用户需自己 `ls ./assistants/`)
- **不**处理 `.current-version` 文件丢失的恢复(若文件被删,所有主流程技能会中止)
- 创建新版本时,`./assistants/<版本号>/` 下除 `RESULT.md` 外**不**预创建 `require/` / `design/` / `plan/` / `code/` / `test/` / `review/` 子目录(由后续技能按需创建) —— 这与 `code-init` 创建基线时"全量预创建"的行为不一致,可能在主流程中产生首次写文件失败

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-002 | EXISTING-002 |
