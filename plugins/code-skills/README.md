# code-skills

**中文** | [English](./README.en.md)

一套用于引导 AI 走完完整软件开发生命周期的 Claude Code 技能集合,内置**版本感知工作空间管理**。

## 安装

```bash
# 1. 注册 marketplace
claude plugin marketplace add https://github.com/wm123450405/code-skills.git

# 2. 安装插件
claude plugin install code-skills@code-skills-marketplace

# 3. 激活技能
/reload-plugins
```

安装完成后,主技能为 `/code-skills:code`,通过首参数区分子命令,例如 `/code-skills:code ver`、`/code-skills:code req`。

> ⚠️ `claude plugin install code-skills@https://github.com/...` 这种直接把 GitHub URL 拼到 `@` 后面的形式在当前 Claude Code 版本下**不会工作** —— 必须先 `marketplace add` 注册,再用 `@marketplace-name` 安装。

## 技能概览

本插件提供 **1 个入口技能 `/code`**,含 6 个子命令:

**主流程**:

| 子命令 | 用途 | 一句话说明 |
| --- | --- | --- |
| `/code ver` | 版本管理与开发看板 | 新项目初始化 / 切换开发版本 / 发布检查 / 开发进度看板,所有子命令的前置门 |
| `/code req` | 需求开发 | 从需求分析到代码审查的全流程:需求分析→软件设计→任务排期→编码→审查 |
| `/code fix` | 缺陷修复 | 缺陷登记→修复设计→任务排期→编码→审查,全流程闭环 |

**辅助工具**:

| 子命令 | 用途 | 一句话说明 |
| --- | --- | --- |
| `/code faq` | 知识查询 | 跨版本查询需求/缺陷,支持导出文档 |
| `/code rule` | 编码规范 | 用自然语言描述规范,自动整理为结构化条款 |
| `/code merge` | 分支合并 | Worktree 模式下自动合并回主干,智能解决冲突 |

## 快速上手

### 第一次使用(新项目)

```
第 1 步: /code ver            ← 初始化项目,扫描代码,创建基线版本
第 2 步: /code rule           ← (可选但推荐)建立编码规范
第 3 步: /code ver V0.0.5     ← 切换到新开发版本
第 4 步: /code req "你的需求"  ← 开始需求开发
```

### 日常开发

```
/code ver          ← 确保在正确的版本上(或查看进度)
/code req "xxx"    ← 一句话描述需求,AI 会引导你走完全流程
/code fix "xxx"    ← 报告缺陷,AI 会引导你修复
```

### 静默模式

```
/code req "xxx" --auto   ← 全自动执行,无需人工确认
/code fix "xxx" --auto   ← 同上
```

## 工作流全景

```mermaid
flowchart LR
    CV[/code ver<br/>版本管理+看板] --> CR[/code req<br/>需求开发]
    CV --> CF[/code fix<br/>缺陷修复]

    CR -->|需求完成| CV
    CF -->|缺陷完成| CV

    subgraph 辅助
        CQ[/code faq<br/>知识查询]
        CRL[/code rule<br/>编码规范]
        CM[/code merge<br/>分支合并]
    end
```

### 核心流程: `/code req` 需求开发

当你调用 `/code req "添加用户登录功能"` 时,AI 会按以下阶段自动推进:

```
需求分析 → 软件设计 → 任务排期 → 编码执行 → 代码审查
(REQUIRE)   (DESIGN)   (PLAN)    (CODING)    (CHECK)
```

- **默认模式**:每阶段完成后询问你"是否继续",你随时可以暂停或取消
- **`--auto` 模式**:无人值守,全自动跑通
- **断点续跑**:中断后重跑,从上次停下的阶段继续(通过 `PROCESS.md` 追踪)

### 支线流程: `/code fix` 缺陷修复

```
缺陷登记 → 修复设计 → 任务排期 → 编码执行 → 代码审查
(INIT)     (DESIGN)    (PLAN)    (CODING)    (CHECK)
```

与 `/code req` 共享 DESIGN/PLAN/CODING/CHECK 阶段的流程逻辑。

## 版本工作空间

所有技能在 `./assistants/<版本号>/` 下工作:

```
assistants/
├── rules/                  ← 项目级编码规范(跨版本共享)
├── .current-version        ← 当前激活版本标记
└── V0.0.5/                 ← 版本工作空间
    ├── RESULT.md           ← 版本看板(需求清单 + 缺陷清单)
    ├── req/<REQ-00045>/    ← 需求产出(REQUIRE/DESIGN/PLAN/TASK/CHECK/PROCESS)
    └── fix/<BUG-00001>/    ← 缺陷产出(BUG/DESIGN/PLAN/TASK/CHECK/PROCESS)
```

## 速查

| 我想... | 调哪个命令 |
| --- | --- |
| 初始化项目 | `/code ver` |
| 切换版本 | `/code ver V0.0.5` |
| 查看进度 | `/code ver` |
| 开发新功能 | `/code req "功能描述"` |
| 静默开发 | `/code req "功能描述" --auto` |
| 修复缺陷 | `/code fix "缺陷描述"` |
| 查询需求 | `/code faq "关键词"` |
| 加编码规范 | `/code rule "规范描述"` |
| 合并分支 | `/code merge` |
| 发布版本 | `/code ver --publish` |

## 详细文档

主技能入口:[`code/SKILL.md`](skills/code/SKILL.md),含 6 个子命令完整工作流说明。