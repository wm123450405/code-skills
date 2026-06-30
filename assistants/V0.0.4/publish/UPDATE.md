# 升级说明 — V0.0.3 → V0.0.4

> 升级时间:2026-06-30 19:00
> 从版本:V0.0.3
> 到版本:V0.0.4

## 破坏性变更

### 技能目录重组

V0.0.4 删除了 10 个旧技能目录,新增 4 个新技能目录。旧技能名不再可用:

| 旧技能名 | 替代方案 |
| --- | --- |
| `code-require` | `code-req`(需求开发全流程) |
| `code-design` | `code-req`(内化到 DESIGN 阶段) |
| `code-plan` | `code-req`(内化到 PLAN 阶段) |
| `code-it` | `code-req`(内化到 CODING 阶段) |
| `code-check` | `code-req`(内化到 CHECK 阶段) |
| `code-auto` | `code-req --auto` / `code-fix --auto` |
| `code-version` | `code-ver`(版本管理) |
| `code-publish` | `code-ver --publish`(发布检查) |
| `code-init` | `code-ver`(自动检测新项目) |
| `code-answer` | `code-faq`(知识查询与导出) |

### 目录结构变更

| 旧路径 | 新路径 |
| --- | --- |
| `require/<REQ>/RESULT.md` | `req/<REQ>/REQUIRE.md` |
| `design/<REQ>/RESULT.md` | `req/<REQ>/DESIGN.md` |
| `plan/<REQ>/RESULT.md` + `PLAN.md` | `req/<REQ>/DESIGN.md` + `PLAN.md` |
| `code/<TASK>/RESULT.md` | `req/<REQ>/TASK-N.md` |
| `review/<REQ>/REVIEW-REPORT.md` | `req/<REQ>/CHECK.md` |
| `fix/<BUG>/RESULT.md` | `fix/<BUG>/BUG.md` |

### 看板简化

版本看板从多区段(需求清单/设计清单/任务清单/缺陷清单/评审汇总/派生任务/命令记录)简化为仅需求清单+缺陷清单 2 区段。进度通过 `PROCESS.md` 追踪。

## 兼容性

- V0.0.0~V0.0.4 的历史数据保持旧格式,不迁移
- V0.0.5+ 的新版本使用新目录结构
- 旧版本看板仍可被 `code-dashboard` 降级解析

## 新增功能

- `--auto` 静默模式:所有 `AskUserQuestion` 自动选推荐项
- `PROCESS.md` 断点续跑:中断后从上次阶段继续
- `code-faq` 文档导出:`--require`/`--design`/`--summary`/`--template`

## 变更记录

| 时间 | 变更类型 | 变更摘要 |
| --- | --- | --- |
| 2026-06-30 19:00 | 升级说明 | V0.0.3 → V0.0.4 升级说明生成 |