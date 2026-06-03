# 现有功能需求 — EXISTING-009:缺陷登记与跟踪(code-fix)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-fix` 是**支线流程入口**(版本感知):负责缺陷的**登记与状态跟踪**,**不**直接改代码。典型流程:用户报告 bug → `code-fix`(登记,自动生成 `BUG-NNN`)→ `code-plan BUG-NNN`(规划)→ `code-it BUG-NNN`(实施)→ `code-fix BUG-NNN`(推进到"已修复-已验证")→ `code-fix BUG-NNN`(关闭)。同时支持查看当前所有 bug 的清单与状态。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-fix/SKILL.md`(345 行) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 4(SKILL.md + 3 个模板) |
| 大致代码量 | 约 400 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-fix/SKILL.md` — 工作流(判定 BUG-NNN vs 描述 → 登记或推进状态 → 写 fix/RESULT.md + fix/<BUG-NNN>/RESULT.md → 更新看板)
- `plugins/code-skills/skills/code-fix/templates/bug.md` — 单个 bug 详情模板
- `plugins/code-skills/skills/code-fix/templates/fix-registry.md` — 缺陷总览(索引)模板
- `plugins/code-skills/skills/code-fix/templates/assistants-layout.md`

## 用户角色与场景

### 角色
- **测试 / 用户 / 开发者**:报告 bug;**项目负责人**:查看清单、推进状态

### 场景
- 用户报告了一个 bug,需要登记跟踪
- bug 修复过程中,需要刷新状态(报告 → 修复中 → 已修复)
- bug 已修复,需要确认验证或关闭
- 查看当前所有 bug 的清单与状态

## 功能点(FR)

- **FR-1**:读 `.current-version` 确认激活版本
- **FR-2**:接收"缺陷编号 `BUG-NNN`"或"缺陷描述"(二选一)
- **FR-3 (新建)**:自动生成 `BUG-NNN` 编号,创建 `fix/<BUG-NNN>/RESULT.md` + 更新 `fix/RESULT.md`
- **FR-4 (新建)**:用 `AskUserQuestion` 收集严重度(`P0/P1/P2/P3`,默认 `P2`)、报告人/模块/路径/复现步骤
- **FR-5 (推进)**:用 `Edit` 增量刷新状态、修复日志、变更记录
- **FR-6 (双路径共)**:同步更新看板"缺陷清单" / "变更记录"
- **FR-7 (双路径共)**:**不**直接改代码(那是 `code-plan BUG-NNN` + `code-it BUG-NNN` 的事)
- **FR-8 (双路径共)**:支持 10 个状态的状态机(报告 → 调查中 → 修复规划中 → 修复编码中 → 已修复-待验证 → 已修复-已验证 → 已关闭 / 已关闭-非缺陷 / 已关闭-不修复;任何状态 → 阻塞 / 已取消)

## 关键接口

### CLI
```
/code-skills:code-fix "用户报告:登录页密码框不显示"   # 新建,自动生成 BUG-001
/code-skills:code-fix BUG-001                          # 查看/推进已有 bug
/code-skills:code-fix                                  # 交互式
```

### 输出
- 新建:`./assistants/<版本号>/fix/<BUG-NNN>/RESULT.md` + `fix/RESULT.md`
- 更新:`Edit` 增量刷新状态、修复日志、变更记录
- 同步更新 `<版本号>/RESULT.md` 看板"缺陷清单" / "变更记录"

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 缺陷编号 | `BUG-NNN` | 3 位数序号,版本内唯一 |
| 缺陷状态 | 10 个枚举(报告/调查中/修复规划中/修复编码中/已修复-待验证/已修复-已验证/已关闭/已关闭-非缺陷/已关闭-不修复/阻塞/已取消) | 看板字段 |
| 严重度 | `P0/P1/P2/P3` | 默认 `P2` |
| 缺陷模板 | `bug.md` | 字段:标题/严重度/报告人/模块/路径/复现步骤/预期/实际/根因/修复方案/验证 |
| 缺陷总览 | `fix/RESULT.md` | 索引所有 `BUG-NNN` 的状态 |

## 验收标准(AC)

- **AC-1**:无 `.current-version` 时立即中止
- **AC-2**:新建时自动生成 `BUG-NNN`,写 `fix/<BUG-NNN>/RESULT.md` + `fix/RESULT.md`
- **AC-3**:新建时用 `AskUserQuestion` 收集严重度等补充信息(可跳过)
- **AC-4**:推进时用 `Edit` 增量刷新,**不**覆盖已有内容
- **AC-5**:同步更新看板"缺陷清单" / "变更记录"
- **AC-6**:`code-fix` 只跟踪,**不**改代码
- **AC-7**:10 个状态的状态机严格按 SKILL.md 规定推进

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-006 (BUG) | 下游:`code-plan BUG-NNN` 读 `fix/<BUG>/RESULT.md` | 必走"修复规划中" |
| EXISTING-007 (BUG) | 下游:`code-it BUG-NNN` 实施修复 | 必走"修复编码中" |
| EXISTING-002 | `code-version` 是前置门 | 必须先有激活版本 |
| EXISTING-001 (回看) | `code-init` 生成的 `EXISTING-NNN` 不是 `BUG-NNN` —— 两者不互通 | 现有功能修改走 `code-require`;新发现的 bug 走 `code-fix` |

## 已知限制/技术债

- `code-fix` 只跟踪,**不**实施 —— 用户需自己串联 `code-fix → code-plan → code-it → code-fix → code-fix` 流程
- 缺陷状态机的"任何状态 → 阻塞 / 已取消"是模糊的,没有规定"被谁/为什么阻塞"
- 10 个状态机不强制某些步骤必须留痕(如"已修复-待验证"必须有"验证方法"字段)—— 完全靠 AI 自觉
- `fix/RESULT.md` 的索引格式与"缺陷清单"看板字段的对应关系靠 AI 维护,容易漂移

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-009 | EXISTING-009 |
