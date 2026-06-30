# 概要设计 — REQ-00043 · 移除 fix-plan.md 废弃引用

> 上游:./assistants/V0.0.4/require/REQ-00043/RESULT.md

## 文档头
- 需求编码:REQ-00043
- 所属版本:V0.0.4
- 状态:已完成
- 创建:2026-06-29 00:00

## 1. 设计概述
纯文本替换:将 `plugins/code-skills/` 下所有 `fix-plan.md` 引用替换为 `PLAN.md`(修复方案)或 `RESULT.md`(缺陷详情)。不涉及模块拆分、接口变更、数据结构变更。

## 2. 替换规则

| 上下文 | 原文本 | 替换为 |
| --- | --- | --- |
| code-plan BUG 路径产出 | `fix-plan.md` | `PLAN.md` |
| code-it BUG 路径输入 | `fix-plan.md` | `PLAN.md` |
| 缺陷详情文件引用 | `fix/<BUG>/fix-plan.md` | `fix/<BUG>/PLAN.md` |
| 目录结构中的文件 | `fix-plan.md` | `PLAN.md` |
| 状态描述中的引用 | `产出 fix-plan.md` | `产出 PLAN.md` |

## 3. 方案选型
- **选择**:直接替换 `fix-plan.md` → `PLAN.md`
- **理由**:`code-plan` BUG 路径已与 REQ 路径同构,产出 `RESULT.md` + `PLAN.md`

## 4. 变更记录
| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-29 00:00 | v1 | 初始创建 | 概要设计完成 | wangmiao |