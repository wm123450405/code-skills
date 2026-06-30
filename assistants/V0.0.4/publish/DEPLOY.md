# 部署手册 — V0.0.4

> 版本:V0.0.4
> 基线:V0.0.0
> 生成时间:2026-06-30 19:00
> 前一版本:V0.0.3

## 版本概述

V0.0.4 是技能系统 v2 大改版,将 14 个技能缩减为 7 个,合并多项能力、重组输出目录结构、新增断点续跑机制、优化版本看板记录逻辑。

## 需求清单

| 需求编码 | 标题 | 状态 |
| --- | --- | --- |
| REQ-00041 | 技能多语言模块化重构 | 已完成 |
| REQ-00042 | 代码产出中禁止包含追踪编号 | 已完成 |
| REQ-00043 | 移除 fix-plan.md 废弃引用 | 已完成 |
| REQ-00044 | 技能系统 v2 大改版 | 已完成 |

## 任务统计

| 指标 | 数值 |
| --- | --- |
| 总任务数 | 18 |
| 开发完成 | 18 |
| 测试通过 | 0(不适用) |
| 缺陷 | 0 |

## 关键变更

### 技能合并 (14 → 7)

| 新技能 | 合并的旧技能 |
| --- | --- |
| code-ver | code-version + code-publish + code-init |
| code-req | code-require + code-design + code-plan + code-it + code-check |
| code-fix | code-fix + code-plan + code-it + code-check(缺陷路径) |
| code-faq | code-answer |
| code-rule | code-rule(保留,适配) |
| code-merge | code-merge(保留,适配) |
| code-dashboard | code-dashboard(保留,适配) |

### 废弃技能

`code-require`、`code-design`、`code-plan`、`code-it`、`code-check`、`code-auto`、`code-version`、`code-publish`、`code-init`、`code-answer` 共 10 个技能。

### 目录结构变更

- 旧: `require/` `design/` `plan/` `code/` `review/` `fix/`
- 新: `req/` + `fix/` 两大目录

### 新增能力

- `code-req --auto` / `code-fix --auto` 静默模式
- `PROCESS.md` 断点续跑
- `code-faq` 知识查询与文档导出
- 简化版版本看板

## 部署步骤

1. 确认 `plugins/code-skills/skills/` 下仅有 7 个技能目录
2. 确认 `.claude-plugin/plugin.json` 和 `marketplace.json` 已更新
3. 确认 `assistants/rules/` 下 4 个规范文件已更新
4. 旧版本数据(V0.0.0~V0.0.4)保持旧结构,不迁移
5. 新版本(V0.0.5+)将使用新目录结构

## 变更记录

| 时间 | 变更类型 | 变更摘要 |
| --- | --- | --- |
| 2026-06-30 19:00 | 发布 | V0.0.4 发布,部署手册生成 |