# 缺陷分析 — BUG-00008 · REQ-00049 阶段 references 未适配三态确认模式

> 所属版本:V0.0.5
> 创建时间:2026-06-30

## 1. 缺陷描述

### 用户原始报告

> REQ-00049 需求开发时对于各阶段的阶段文档中的 阶段完成确认 部分内容没有对 `--confirm` 和 非`--confirm` 模式进行适配。

### 期望行为 vs 实际行为

- **期望**:各阶段 reference 文档(require.md/design.md/plan.md/coding.md/check.md/fix-register.md)的"阶段完成确认"章节应反映 REQ-00049 实现的三态确认模型
- **实际**:这些章节仍使用旧的"非 --auto 模式确认"描述，选项为 A(继续)/B(暂停)/C(取消)，未适配 --confirm 模式

## 2. 触发条件

- **必要条件**:REQ-00049 已完成，但未同步更新各阶段 reference 的确认章节
- **发生频率**:必现(6 个 reference 文件全部未更新)

## 3. 可能成因

- REQ-00049 只更新了 SKILL.md 和 common.md，遗漏了各阶段 reference 文档中的"阶段完成确认"章节
- 涉及文件:require.md / design.md / plan.md / coding.md / check.md / fix-register.md

## 4. 影响范围

- **影响模块**:6 个 reference 文件
- **严重程度**:P2(文档不一致，不影响功能执行)
- **后果**:AI 协作者阅读这些 reference 时看到的是旧确认模式，可能与 SKILL.md 中的三态描述不一致

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 | v1 | 初始创建 | 缺陷登记完成 | wangmiao |