# 现有功能需求 — EXISTING-007:开发编码(code-it)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-it` 是主流程的**第五步** + 缺陷修复流程的**实施步骤**(**双路径**,版本感知):按"输入 ID 格式"自动判定走任务路径(`REQ-YYYY-NNNN-NNN`)还是缺陷路径(`BUG-NNN`)。任务路径按 `PLAN.md` 单任务执行编码;缺陷路径按 `fix-plan.md` 实施修复;同时支持"审查改修"任务(由 `code-review` 派生)。强制要求"可编译可启动",有 5 次连续失败硬上限。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-it/SKILL.md`(611 行) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 4(SKILL.md + guidelines/ + 2 个模板) |
| 大致代码量 | 约 700 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-it/SKILL.md` — 双路径 + 触发/来源(13 个枚举)工作流
- `plugins/code-skills/skills/code-it/guidelines/coding-style.md` — 强制执行的编码风格
- `plugins/code-skills/skills/code-it/templates/RESULT.md` — 任务级 RESULT.md 模板
- `plugins/code-skills/skills/code-it/templates/assistants-layout.md`

## 用户角色与场景

### 角色
- **开发者**:按 PLAN.md 逐任务实施编码,或实施 bug 修复,或执行审查派生的改修任务

### 场景
- 任何按 `PLAN.md` 单条任务执行的编码工作
- 重构或特性开发的具体落地
- Bug 修复的具体落地
- `code-review` 派生的"审查改修"任务的执行
- `code-fix` 支线下,实施缺陷修复

## 功能点(FR)

- **FR-1**:读 `.current-version` 确认激活版本
- **FR-2**:按输入 ID 格式自动判定路径(任务 vs 缺陷)
- **FR-3 (任务路径)**:按任务的"触发/来源"读上游(大多数 → `plan/<需求>/RESULT.md`;`审查改修` → `review/<任务编码>/RESULT.md`)
- **FR-4 (任务路径)**:实施 CWD 下实际代码改动(diff/提交)
- **FR-5 (任务路径)**:写 `code/<任务编码>/RESULT.md` + 推进 PLAN.md 中本任务开发状态
- **FR-6 (缺陷路径)**:读 `fix/<BUG-NNN>/RESULT.md` + `fix-plan.md` 实施修复
- **FR-7 (缺陷路径)**:写 `fix/<BUG-NNN>/fix-*.md`,推进 `fix/<BUG-NNN>/RESULT.md` 状态
- **FR-8 (双路径共)**:**必须**确保软件可正常编译、可启动运行,出现错误时迭代修复直到消除
- **FR-9 (双路径共)**:**5 次连续失败硬上限**,每次失败记录到 `work-log.md` / `fix-work-log.md`,超限必须停下询问用户
- **FR-10 (双路径共)**:**禁止**用 `--no-verify` / `--force` / 注释失败代码等方式绕过错误
- **FR-11 (双路径共)**:同步更新看板(任务路径 → "任务清单/缺陷清单/执行的开发命令记录/变更记录";缺陷路径 → "缺陷清单/执行的开发命令记录/变更记录")

## 关键接口

### CLI
```
/code-skills:code-it REQ-2026-0001-001   # 主流程:第 1 个任务
/code-skills:code-it BUG-001              # 缺陷修复
/code-skills:code-it REQ-2026-0001-005   # 派生"审查改修"任务
```

### 输出
- 任务路径:`./assistants/<版本号>/code/<任务编码>/{RESULT.md, work-log.md, ...}` + 实际代码改动
- 缺陷路径:`./assistants/<版本号>/fix/<BUG-NNN>/{fix-work-log.md, fix-compile-and-run.md, fix-test-results.md, deviations.md, ...}`

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 任务编码 | `REQ-YYYY-NNNN-NNN` | 3 位数任务序号 |
| 触发/来源 | 13 个枚举 | 决定读 `plan/` 还是 `review/` 上游 |
| 开发状态 | 待开始/进行中/已完成/已取消/阻塞/待重新评估 | 看板"任务清单"字段 |
| work-log 模板 | `code/<任务>/work-log.md` | 字段:尝试次数/失败原因/修复动作/重试结果 |
| 失败硬上限 | 5 次 | 连续失败 5 次必须停下询问用户 |

## 验收标准(AC)

- **AC-1**:无 `.current-version` 时立即中止
- **AC-2**:任务路径校验 `plan/<需求>/RESULT.md` 存在;`审查改修` 任务校验 `review/<任务>/RESULT.md` 存在
- **AC-3**:缺陷路径校验 `fix/<BUG>/RESULT.md` + `fix-plan.md` 都存在
- **AC-4**:**5 次连续失败硬上限**:超限必须停下询问用户,不能自行继续
- **AC-5**:**禁止**用 `--no-verify` / `--force` / 注释失败代码等方式绕过错误
- **AC-6**:写 `code/<任务>/RESULT.md` 含本任务开发状态推进结果
- **AC-7**:推进 PLAN.md 中本任务开发状态(`待开始` → `进行中` → `已完成`)
- **AC-8**:同步更新看板"任务清单" / "缺陷清单" / "执行的开发命令记录" / "变更记录"

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-006 | 任务路径读 `plan/<需求>/RESULT.md` + `PLAN.md` | 主流程上游 |
| EXISTING-006 (BUG) | 缺陷路径读 `fix-plan.md` | 缺陷分支上游 |
| EXISTING-010 | 读 `review/<任务>/RESULT.md` 作为`审查改修`任务上游 | `code-review` 派生 |
| EXISTING-003 | 读 `rules/` + `guidelines/coding-style.md` 作为约束 | 强约束 |
| EXISTING-008 | 下游:本任务开发完成后调 `code-unit` 补单测 | 强制后续 |
| EXISTING-002 | `code-version` 是前置门 | 必须先有激活版本 |

## 已知限制/技术债

- **5 次失败硬上限**只看"连续失败",不区分"编译失败" vs "测试失败" vs "lint 失败" —— 任何错误都计入同一计数
- 不自动提交(只写 diff);实际 git commit 由用户或 harness 决定
- "审查改修"任务的 `RESULT.md` 模板可能与"需求新增"任务的 `RESULT.md` 模板不完全一致,需在技能 SKILL.md 中显式说明
- 不支持"批量跨任务"的批量改动(应拆分为多次本技能调用)

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-007 | EXISTING-007 |
