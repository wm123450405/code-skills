# 缺陷分析 — BUG-00001 · code-req 未按阶段顺序执行,跳过需求/设计/排期直接修改代码

> 所属版本:V0.0.5
> 创建时间:2026-06-30 20:20

## 1. 缺陷描述

当用户执行 `/code-req` 技能(未添加 `--auto` 参数)时,AI 有时会跳过 REQUIRE→DESIGN→PLAN→CODING→CHECK 的强制阶段顺序,直接进入代码修改,且未生成 REQUIRE.md/DESIGN.md/PLAN.md/PROCESS.md 等需求文档和进度管理文件。

**严重程度**:高(影响核心工作流完整性)

## 2. 触发条件

1. 用户调用 `/code-req <需求描述>`(无 `--auto`)
2. AI 模型在读取 SKILL.md 后,未严格遵循阶段顺序
3. 直接跳转到 CODING 阶段修改代码
4. 未创建 `req/<REQ-NNNNN>/` 目录及任何产出文档

## 3. 可能成因

### 根因 1: SKILL.md 阶段强制约束不够强

SKILL.md 中描述了阶段顺序,但缺少"门控"机制:
- 没有明确声明"在 REQUIRE/DESIGN/PLAN 阶段完成前,严禁修改 CWD 源码"
- 没有强制要求每个阶段启动前检查上一阶段的产出物
- 阶段执行器描述为"详见 references/xxx.md",但 references 文档本身可能被模型跳过

### 根因 2: 缺少"阶段门控"守卫

当前 SKILL.md 的工作流程步骤 0 仅做版本检测和 PROCESS.md 恢复,但没有做"代码修改权限"的守卫:
- 没有在 CODING 阶段之外设置"只读"约束
- 没有在阶段切换时做产出物存在性校验

### 根因 3: PROCESS.md 的断点续跑机制可能被绕过

当 PROCESS.md 不存在时,SKILL.md 指示从 INIT 开始,但模型可能:
- 跳过 INIT 阶段,直接开始修改代码
- 不创建 PROCESS.md,导致后续无法追踪

## 4. 影响范围

- **code-req/SKILL.md**:需要增强阶段门控约束
- **code-req/references/common.md**:需要增加阶段前置校验
- **code-req/references/coding.md**:需要增加"仅当 CODING 阶段激活时才可修改代码"的守卫

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 20:20 | v1 | 初始创建 | 缺陷登记完成 | wangmiao |