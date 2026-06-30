# 审查改修要求 — TASK-REQ-00044-00011 · 更新 CLAUDE.md 为 v2 结构

> 来源:评审 REQ-00044,发现 F-1(必须改)
> 关联:REVIEW-REPORT.md

## 1. 问题描述

`CLAUDE.md` 是项目根的核心入口文档,AI 协作者在仓库中工作时会以此为指引。当前 CLAUDE.md 仍引用 v1 的旧技能名和旧目录结构,与已完成的 v2 大改版不一致:

### 1.1 过时的技能名引用

| 位置 | 当前(v1) | 应为(v2) |
| --- | --- | --- |
| §仓库用途 流程图 | `code-version → code-require → code-design → code-plan → code-it → code-check` | `code-ver → code-req(含 REQUIRE/DESIGN/PLAN/CODING/CHECK 阶段)` |
| §仓库用途 说明 | `code-version` 是必备前置门 | `code-ver` 是必备前置门 |
| §仓库用途 说明 | `code-init` 新项目一次性引导 | 已合并到 `code-ver`(自动检测新项目) |
| §仓库用途 说明 | `code-fix` 支线流程入口,与 code-plan/code-it 协作 | `code-fix` 独立全流程(含 DESIGN/PLAN/CODING/CHECK) |
| §仓库结构 目录树 | `code-init/`, `code-version/`, `code-require/`, `code-design/`, `code-plan/`, `code-it/`, `code-fix/`, `code-check/` | `code-ver/`, `code-req/`, `code-fix/`, `code-faq/`, `code-rule/`, `code-merge/`, `code-dashboard/` |
| §版本感知工作空间约定 目录树 | `require/`, `design/`, `plan/`, `code/`, `review/`, `fix/` | `req/`, `fix/`(两大目录) |
| §版本感知工作空间约定 说明 | `code-init` 创建基线版本 | `code-ver` 初始化时自动检测 |
| §版本感知工作空间约定 说明 | `code-fix` 与 code-plan/code-it 协作 | `code-fix` 独立全流程 |
| §版本感知工作空间约定 说明 | `code-plan` 与 `code-it` 双路径 | 已内化到 `code-req`/`code-fix` |
| §看板写入责任划分 | 7 个技能的写入责任 | 应更新为 `code-req`(需求清单)/`code-fix`(缺陷清单) |
| §指引 N | "10 个 code-* SKILL.md" | "7 个 code-* SKILL.md" |
| §指引 N | "看板 3 区段" | "看板 2 区段(需求清单+缺陷清单)" |

### 1.2 过时的目录结构

CLAUDE.md §版本感知工作空间约定 中的目录树仍使用旧格式,应更新为:

```
assistants/
├── rules/                  # 项目级规范,跨版本共享,由 code-rule 维护
├── .current-version        # 当前激活版本标记
└── <版本号>/               # 版本工作空间
    ├── RESULT.md           # 版本开发进度看板(简化版)
    ├── req/<REQ-NNNNN>/    # 需求路径(code-req 产出)
    │   ├── REQUIRE.md / DESIGN.md / PLAN.md
    │   ├── TASK-N.md / CHECK.md / PROCESS.md
    └── fix/<BUG-NNNNN>/    # 缺陷路径(code-fix 产出)
        ├── BUG.md / DESIGN.md / PLAN.md
        ├── TASK-N.md / CHECK.md / PROCESS.md
```

## 2. 改修方案

### 2.1 更新 §仓库用途

- 流程图:`code-ver → code-req → code-fix → code-faq → code-dashboard`
- 技能说明:更新为 7 个 v2 技能,移除 `code-init`/`code-version` 等旧引用
- 新增 `code-faq` 和 `code-dashboard` 说明

### 2.2 更新 §仓库结构

- 目录树:替换为 7 个 v2 技能目录
- 技能说明:code-ver(版本管理), code-req(需求开发), code-fix(缺陷修复), code-faq(知识查询), code-rule(规范管理), code-merge(分支合并), code-dashboard(开发看板)

### 2.3 更新 §版本感知工作空间约定

- 目录树:替换为 `req/`+`fix/` 两大目录结构
- 说明文字:更新技能引用,移除 `code-init`/`code-plan`/`code-it` 独立说明
- 看板写入责任:简化为 `code-req`(需求清单) + `code-fix`(缺陷清单)

### 2.4 更新 §指引 N

- "10 个 code-*" → "7 个 code-*"
- "看板 3 区段" → "看板 2 区段(需求清单+缺陷清单)"
- 状态分类:从"5 类状态"更新为 PROCESS.md 阶段追踪

## 3. 影响范围

- 仅修改 `CLAUDE.md`(仓库根目录)
- 不涉及其他文件

## 4. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 19:00 | v1 | 初始创建 | 审查改修要求,由 code-check REQ-00044 派生 | wangmiao |