# 任务排期 — REQ-OPT-00003 · 移除板块标题序号,引用处同步改为板块标题

> 所属版本:V0.0.6
> 创建时间:2026-07-24 11:30
> 任务总数:5

## 任务总览

| 任务编号 | 类型 | 标题 | 涉及文件 | 开发状态 | 测试状态 | 前置任务 |
| --- | --- | --- | --- | --- | --- | --- |
| TASK-REQ-OPT-00003-00001 | 修改 | 契约层 + 6 个 references 详细流程去序号标题 | `_shared/contracts.md` + `references/req/coding.md` + `references/req/design.md` + `references/req/require.md` + `references/req/plan.md` + `references/merge/SKILL.md` + `references/ver/common.md` + `references/faq/common.md` + `references/runtime-environment.md` + `references/req/common.md` | 待开始 | 不适用 | — |
| TASK-REQ-OPT-00003-00002 | 修改 | 6 个 language 适配文件去序号标题 | `references/req/languages/{go,java-maven,java-gradle,nodejs,python,rust}.md` | 待开始 | 不适用 | — |
| TASK-REQ-OPT-00003-00003 | 修改 | 9 个 templates 文件去序号标题 | `templates/{req/REQUIRE,req/DESIGN,req/TASK,req/CHECK,req/PLAN,fix/BUG,faq/REQUIRE-EXPORT,faq/DESIGN-EXPORT,faq/SUMMARY-EXPORT}.md` | 待开始 | 不适用 | — |
| TASK-REQ-OPT-00003-00004 | 修改 | 7 个 SKILL.md 中正文 § 引用改为板块标题 | `SKILL.md` + `references/{ver,faq,rule,fix,merge,help}/SKILL.md` + `references/fix/fix-register.md` + `references/ver/SKILL.md` | 待开始 | 不适用 | TASK-00001~00003(标题清理完后引用目标才确定) |
| TASK-REQ-OPT-00003-00005 | 修改 | templates/ver/RESULT.md § 引用改为板块标题 | `templates/ver/RESULT.md` | 待开始 | 不适用 | TASK-00001 |

## 任务依赖

```
TASK-00001 ─┐
TASK-00002 ─┼─→ TASK-00004 (引用目标必须先清理完才能映射)
TASK-00003 ─┘
TASK-00001 ─→ TASK-00005
```

## 里程碑

| 里程碑 | 包含任务 | 完成定义 | 预计时间 |
| --- | --- | --- | --- |
| M1: 板块标题清理 | TASK-00001~00003 | 16 个文件的 `^#+\s+(\d\|§)` 命中数 = 0 | 30 分钟 |
| M2: 正文引用清理 | TASK-00004~00005 | 跨文件 § 引用全部改为板块标题 | 20 分钟 |

## 任务详情

### TASK-REQ-OPT-00003-00001: 契约层 + references 详细流程去序号标题

- **类型**:修改
- **涉及文件**:见任务总览
- **详细步骤**:
  1. 对每个文件,先 Grep 所有匹配行 → 输出"原标题 → 新标题"对照表
  2. 等用户(或一次性)确认后,逐文件 Edit 替换
  3. Read 验证 grep `^#+\s+(\d|§)` = 0
- **验证方式**:文件级 grep + Read

### TASK-REQ-OPT-00003-00002: 6 个 language 适配文件去序号标题

- **类型**:修改
- **涉及文件**:6 个 languages/*.md
- **详细步骤**:同 TASK-00001
- **验证方式**:文件级 grep

### TASK-REQ-OPT-00003-00003: 9 个 templates 文件去序号标题

- **类型**:修改
- **涉及文件**:9 个 templates/*.md
- **详细步骤**:同 TASK-00001;注意 templates 中的 `<占位符>` 视作模板内容,保留(不动)
- **验证方式**:文件级 grep

### TASK-REQ-OPT-00003-00004: SKILL.md 正文 § 引用改为板块标题

- **类型**:修改
- **涉及文件**:所有 SKILL.md + fix-register.md
- **详细步骤**:
  1. 对每个文件 Grep 所有 `§\d+(\.\d+)*` 引用 → 输出"原引用 → 新引用(板块标题文字)"对照表
  2. 等用户(或一次性)确认后,逐文件 Edit 替换
  3. Read 验证 grep `§\d+(\.\d+)*` (非标题行) = 0
- **验证方式**:文件级 grep + Read

### TASK-REQ-OPT-00003-00005: templates/ver/RESULT.md § 引用清理

- **类型**:修改
- **涉及文件**:1 个 templates/ver/RESULT.md
- **详细步骤**:同 TASK-00004
- **验证方式**:grep

## 附录 A:测试状态流转规则(FR-7 来源)

> 本修复为纯文档型,所有任务测试状态 = `不适用`,无需流转校验。

## 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-24 11:30 | v1 | 初始创建 | 任务排期完成;5 任务 / 2 里程碑 | wangmiao |