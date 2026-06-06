# 关联概要设计 — REQ-00019
更新时间:2026-06-06 15:00
版本:V0.0.2

## 同版本关联

### REQ-00005 概要设计(优化 code-require / code-design / code-plan,首步拉取+末步提交)
- **关联点**:`code-plan` 步骤 0a(首步拉取)+ 步骤 N(末步兜底提交)对 BUG 路径同样适用
- **影响**:本需求在 `code-plan` 缺陷分支(步骤 19-28A)之外,步骤 0a + 步骤 N 沿用既有;**不**重复实现
- **链接**:`./assistants/V0.0.2/design/REQ-00005/RESULT.md`

### REQ-00007 概要设计(/code-auto 自动开发技能)
- **关联点**:`code-auto` 子技能调用 `code-plan` 时,BUG 路径(若有)同样接受"自动选推荐项"约束
- **影响**:本需求在 BUG 路径实施后,`code-auto` 调 `code-plan BUG-NNN` 不触发步骤 0b 设计目标确认(沿用 BUG-00001 修复方案 A3 脏标记文件)
- **链接**:`./assistants/V0.0.2/design/REQ-00007/RESULT.md`

### REQ-00009 概要设计(/code-unit 项目可测性守卫)
- **关联点**:BUG 任务的测试状态初始化:本仓库无测试框架,守卫判定"不可测" → 测试状态 = `不适用`
- **影响**:FR-3 字段填法:BUG 任务的"测试状态"初值 = `不适用`(纯文档型)或 `未编写`(代码类任务)
- **链接**:`./assistants/V0.0.2/design/REQ-00009/RESULT.md`

### REQ-00010 概要设计(/code-it 步骤 0a 前置任务守卫)
- **关联点**:BUG 任务执行时也走前置守卫(按 `PLAN.md` 文件登记顺序判定)
- **影响**:本需求 BUG 任务登记到 `PLAN.md` 任务总览后,守卫判定覆盖到 `TASK-BUG-...` 任务
- **链接**:`./assistants/V0.0.2/design/REQ-00010/RESULT.md`

### REQ-00011 概要设计(/code-design / /code-plan 步骤 0b 设计目标确认)
- **关联点**:BUG 路径**不**触发步骤 0b(修复是已发生的设计偏差,无需再确认)
- **影响**:NFR-3.4 锁定;`code-plan` 步骤 0b 章节对 BUG 路径**不**适用
- **链接**:`./assistants/V0.0.2/design/REQ-00011/RESULT.md`

### REQ-00013 概要设计(6 技能启用"编号+标题" 显示)
- **关联点**:BUG 任务沿用 `formatTaskTitle` + `truncateTitle`;`code-plan` / `code-it` 屏幕输出统一格式
- **影响**:FR-3 / NFR-4 字段填法;`code-plan/SKILL.md` 标题解析 L107-109 `formatTaskTitle` 工具函数已支持 `TASK-...` 任意前缀
- **链接**:`./assistants/V0.0.2/design/REQ-00013/RESULT.md`

### REQ-00014 概要设计(/code-plan 任务拆分维度)
- **关联点**:BUG 路径**不**触发"架构任务作为首个"(修复不引入新架构)
- **影响**:0 派生架构任务;BUG 任务拆分仅按"修复步骤"维度
- **链接**:`./assistants/V0.0.2/design/REQ-00014/RESULT.md`

### REQ-00015 概要设计(/code-merge worktree 自动合并)
- **关联点**:本需求在 BUG 路径实施后,`code-merge` 仍按 V0.0.1 既有合并(本需求不修改 `code-merge`)
- **影响**:0 影响(沿用)
- **链接**:`./assistants/V0.0.2/design/REQ-00015/RESULT.md`

### REQ-00016 概要设计(/code-design / /code-plan 快模式)
- **关联点**:BUG 路径同样支持快模式(沿用 `code-plan` 步骤 0.5 模式选择)
- **影响**:本需求在 BUG 路径实施后,`code-plan BUG-NNN --fast` 仍可触发快模式(跳非必要步骤 + 减少过程文档)
- **链接**:`./assistants/V0.0.2/design/REQ-00016/RESULT.md`

### REQ-00017 概要设计(/code-plan 不再为"更新看板"拆派生任务)
- **关联点**:BUG 任务沿用 FR-3 强约束;看板推进由 `code-it` P-1 自行承担
- **影响**:INV-7 0 派生"更新看板"任务
- **链接**:`./assistants/V0.0.2/design/REQ-00017/RESULT.md`

### REQ-00018 概要设计(/code-version 优化)
- **关联点**:BUG 路径产出物写入版本工作空间时,沿用 CWD 同步(若 V0.0.2 是新版本首次切)
- **影响**:无直接依赖;间接:本需求在 V0.0.2 实施
- **链接**:`./assistants/V0.0.2/design/REQ-00018/RESULT.md`

## 跨版本关联(可选)

无。

## 缺陷路径关联

### BUG-00001 修复方案
- **关联点**:BUG-00001 已有 `fix-plan.md`(624 行)+ 5 份 `fix-` 前缀过程文档;本需求**不**迁移
- **影响**:NFR-3.2 锁定;`code-plan` 步骤 23 + `code-it` 步骤 17 步骤 22 步骤 24 全部增加 E-1 / E-7 / E-9 / E-11 历史兼容检测
- **链接**:`./assistants/V0.0.2/fix/BUG-00001/fix-plan.md`
