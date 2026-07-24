# 任务排期 — BUG-00011 · 技能中残余无意义板块清理

> 所属版本:V0.0.6
> 创建时间:2026-07-24 10:15
> 任务总数:7

## 任务总览

| 任务编号 | 类型 | 标题 | 涉及文件 | 开发状态 | 测试状态 | 前置任务 |
| --- | --- | --- | --- | --- | --- | --- |
| TASK-BUG-00011-00001 | 删除 | 清理主 SKILL.md 末尾 `## 不要做的事` 空板块 | `plugins/code-skills/skills/code/SKILL.md` | 待开始 | 不适用 | — |
| TASK-BUG-00011-00002 | 删除 | 清理 rule SKILL.md 末尾 `## 不要做的事` 空板块 | `references/rule/SKILL.md` | 待开始 | 不适用 | — |
| TASK-BUG-00011-00003 | 删除 | 清理 faq SKILL.md 末尾 `## 不要做的事` 空板块 | `references/faq/SKILL.md` | 待开始 | 不适用 | — |
| TASK-BUG-00011-00004 | 删除 | 清理 ver SKILL.md `## 不要做的事` 空板块(附录 A 之前) | `references/ver/SKILL.md` | 待开始 | 不适用 | — |
| TASK-BUG-00011-00005 | 删除 | 清理 merge SKILL.md `## 不要做的事` 空板块(启动纪律自检表之前) | `references/merge/SKILL.md` | 待开始 | 不适用 | — |
| TASK-BUG-00011-00006 | 删除 | 清理 fix SKILL.md `## 不要做的事` 空板块(启动纪律自检表之前) | `references/fix/SKILL.md` | 待开始 | 不适用 | — |
| TASK-BUG-00011-00007 | 删除 | 清理 req SKILL.md `## 不要做的事` 空板块(启动纪律自检表之前) | `references/req/SKILL.md` | 待开始 | 不适用 | — |

## 任务依赖

```
无依赖 — 7 个任务独立,可并行执行
```

## 里程碑

| 里程碑 | 包含任务 | 完成定义 | 预计时间 |
| --- | --- | --- | --- |
| M1: 7 个 SKILL.md 空板块全部清理 | TASK-00001~00007 | 7 个文件均不再含 `## 不要做的事` 标题或 `本节保留位置` 占位 | 10 分钟 |

## 任务详情

### TASK-BUG-00011-00001: 清理主 SKILL.md 末尾空板块
- **类型**:删除
- **涉及文件**:`plugins/code-skills/skills/code/SKILL.md`
- **详细步骤**:
  1. `Read` 文件定位第 105-109 行(`---` + `## 不要做的事` + 空行 + 占位行 + EOF)
  2. `Edit` 删除第 105 行起的 `---` 之后所有内容(包括空行、板块标题、占位行),但保留第 105 行的 `---` 作为前一板块结束分隔
  3. 验证:文件结尾是 `---` + EOF,无残留
- **验证方式**:
  - `Read` 文件,grep `## 不要做的事` → 0 命中
  - `Read` 文件,grep `本节保留位置` → 0 命中

### TASK-BUG-00011-00002: 清理 rule SKILL.md 空板块
- **类型**:删除
- **涉及文件**:`plugins/code-skills/skills/code/references/rule/SKILL.md`
- **详细步骤**:
  1. `Read` 文件定位第 173-177 行
  2. `Edit` 删除 `## 不要做的事` 标题 + 空行 + 占位行 + 上一 `---` 后空行,保留第 173 行 `---` 与上一板块紧邻
  3. 验证:文件末尾 `## 启动纪律自检表...` 之前无空板块
- **验证方式**:grep 验证 `## 不要做的事` = 0

### TASK-BUG-00011-00003: 清理 faq SKILL.md 空板块
- **类型**:删除
- **涉及文件**:`plugins/code-skills/skills/code/references/faq/SKILL.md`
- **详细步骤**:同 TASK-00002
- **验证方式**:grep 验证

### TASK-BUG-00011-00004: 清理 ver SKILL.md 空板块
- **类型**:删除
- **涉及文件**:`plugins/code-skills/skills/code/references/ver/SKILL.md`
- **详细步骤**:
  1. `Read` 文件定位第 455-460 行(`---` + 板块 + 下一板块 `## 附录 A:`)
  2. `Edit` 删除第 456-458 行的板块全部内容,保留第 455 行 `---` 与 `## 附录 A:` 紧邻(中间仅 1 空行,标准段落分隔)
- **验证方式**:grep + Read 看 `## 附录 A:` 紧邻上一 `---`

### TASK-BUG-00011-00005: 清理 merge SKILL.md 空板块
- **类型**:删除
- **涉及文件**:`plugins/code-skills/skills/code/references/merge/SKILL.md`
- **详细步骤**:同 TASK-00002(下一板块为 `## 启动纪律自检表...`)
- **验证方式**:grep 验证

### TASK-BUG-00011-00006: 清理 fix SKILL.md 空板块
- **类型**:删除
- **涉及文件**:`plugins/code-skills/skills/code/references/fix/SKILL.md`
- **详细步骤**:同 TASK-00002
- **验证方式**:grep 验证

### TASK-BUG-00011-00007: 清理 req SKILL.md 空板块
- **类型**:删除
- **涉及文件**:`plugins/code-skills/skills/code/references/req/SKILL.md`
- **详细步骤**:同 TASK-00002
- **验证方式**:grep 验证

## 附录 A:测试状态流转规则(FR-7 来源)

> 本修复为纯文档型,所有任务测试状态 = `不适用`,无需流转校验。

### A.1 初值表(本修复适用)

| 任务类型 | 初始测试状态 |
| --- | --- |
| 文档型(仅 Markdown / 配置文件) | 不适用 |

## 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-24 10:15 | v1 | 初始创建 | 任务排期完成;7 任务 / 1 里程碑;并行执行 | wangmiao |