# 设计笔记 — REQ-00013(plan 阶段)
更新时间:2026-06-05 21:30
版本:V0.0.2

## 本计划阶段 0 新增设计问题(8 项设计问题已在 design 阶段全部锁定)

本计划阶段沿用 `design/REQ-00013/design-notes.md` 的 8 项设计决策(D-1~D-8),0 新增。

## 与上游概要设计的一致性

| 上游设计章节 | 本计划如何落地 |
| --- | --- |
| §1.4 8 项设计决策 D-1~D-8 | 100% 沿用,无修订 |
| §3 模块拆分 M-1~M-8 | 100% 沿用,转为 8 个任务 + 1 收尾任务 |
| §4 接口与数据结构(`truncateTitle` / `formatReqTitle` / `formatTaskTitle` / `formatBugTitle`)| 各任务的"关键变更"段落显式给出伪代码 |
| §9 边界与异常 E-1~E-12 | 各任务的"边界与异常"段落覆盖 E-1~E-12 |
| §8 关键不变量 INV-1~8 | 收尾任务执行 8 项 INV 自检 |

## 任务拆分(REQ-00014 + REQ-00017 强约束)

### 拆分原则(REQ-00014)
- 1 个任务 = 1 个完整的功能点 = 1 个用户完整可用的能力
- 本设计的 8 个模块 M-1~M-8 各对应 1 个**用户可见能力**:
  - M-1:在 `code-require` 屏幕输出中看到"编号+标题"
  - M-2:在 `code-plan` 屏幕输出中看到"编号+标题"
  - M-3:在 `code-fix` 屏幕输出中看到"编号+标题" + `fix/.../RESULT.md` 含"## 缺陷标题"
  - M-4:在 `code-it` 屏幕输出中看到"编号+标题"
  - M-5:在 `code-unit` 屏幕输出中看到"编号+标题"
  - M-6:在 `code-review` 屏幕输出中看到"编号+标题"
  - M-7:在 `code-auto` 进度日志中看到"编号+标题"
  - M-8:在 `code-publish` 前置检查报告中看到"编号+标题"

### 拆任务约束(REQ-00017)
- 0 拆"更新看板"派生任务
- 0.5-2 天内可完成(本设计 8 任务 × 文档型 + 1 收尾 = 1-2 天)

### 任务编号
- T-001~T-008:8 个 SKILL.md 增量追加任务(M-1~M-8 一一对应)
- T-009:1 个收尾任务(8 项 INV 自检 + 看板同步 + 收尾报告)
- 0 任务编号 T-002~T-008 间隔预留未来追加

### 任务类型
- T-001~T-008:`修改`(对既有 SKILL.md 增量追加)
- T-009:`文档`(纯收尾自检 + 看板同步)

## 算法与逻辑

### 算法 1:`truncateTitle`(共享工具函数)

```ts
function truncateTitle(title: string, maxLen: number = 30): string {
  if ([...title].length <= maxLen) return title
  return [...title].slice(0, maxLen).join('') + '...'
}
```

### 算法 2:`formatReqTitle`(需求标题格式化)

```ts
function formatReqTitle(reqNum: string, title: string): string {
  return `${reqNum} · ${truncateTitle(title)}`
}
```

### 算法 3:`formatTaskTitle`(任务标题格式化)

```ts
function formatTaskTitle(taskNum: string, title: string): string {
  return `${taskNum} · ${truncateTitle(title)}`
}
```

### 算法 4:`formatBugTitle`(缺陷标题格式化)

```ts
function formatBugTitle(bugNum: string, title: string): string {
  return `${bugNum} · ${truncateTitle(title)}`
}
```

### 算法 5:6 技能标题解析入口(各技能独立实现)

| 技能 | 解析源 | 提取方法 |
| --- | --- | --- |
| `code-require` | `require/.../RESULT.md` 第 1 行 | `require('fs').readFileSync` + 正则 `^# 需求提示词文档 — (.+)$` |
| `code-plan` | `require/.../RESULT.md` 第 1 行 + `plan/.../PLAN.md` 任务总览"标题"列 | 同上 + 正则 `^\| TASK-... \| .* \| .* \| (.+) \| .* \|$` |
| `code-fix` | `fix/.../RESULT.md` "## 缺陷标题"小节 | `require('fs').readFileSync` + 正则 `^## 缺陷标题\n+(.+)$` |
| `code-it` / `code-unit` | `plan/.../PLAN.md` 任务总览"标题"列 | 正则 `^\| TASK-... \| .* \| .* \| (.+) \| .* \|$` |
| `code-review` | `require/.../RESULT.md` 第 1 行 + `plan/.../PLAN.md` 任务总览 | 同 `code-require` + `code-plan` |
| `code-auto` | 子技能输入 + 子技能预期产物 | 自读 `require/.../RESULT.md` / `PLAN.md` / `fix/.../RESULT.md` |
| `code-publish` | 同 6 技能源 | 复用同 3 个解析源 |

### 算法 6:`code-fix` "## 缺陷标题"小节生成

```
[/code-fix 步骤 1 末尾追加]
  读取用户原始缺陷描述(从 stdin 或 args)
  → truncateTitle(描述, 30)
  → 写入 fix/<BUG-NNN>/RESULT.md 顶部"## 缺陷标题"小节:
      ## 缺陷标题
      <截断后的标题>
```

### 算法 7:`code-auto` 屏幕日志格式升级

```
[/code-auto 步骤 1 / 步骤 2 / 步骤 3 / 步骤 4 / 步骤 5 / 步骤 6]
  调子技能前,自读"标题"源:
    步骤 1 / 2 / 3 / 5:read require/<REQ-NNNNN>/RESULT.md 第 1 行
    步骤 4 / 6:read plan/<REQ-NNNNN>/PLAN.md 任务总览"标题"列
    步骤 6 派生:read fix/<BUG-NNNNN>/RESULT.md "## 缺陷标题"
  → 拼接"编号+标题"到屏幕日志:
    [code-auto] 步骤 1/6:code-require REQ-00013 · 优化 6 技能,启用"编号+标题"显示
    [code-auto]   → 1/8:code-it TASK-REQ-00013-001 · code-require/SKILL.md 增量追加 ✓
    [code-auto]   → 1/8:code-unit TASK-REQ-00013-001 · code-require/SKILL.md 增量追加 ✓ (跳过,无需测试)
```

### 算法 8:`code-publish` PreflightChecker 拼接升级

```
[/code-publish PreflightChecker 步骤 2.6]
  对每条"未完成项"行:
    原格式: REQ-NNNNN 状态=...
    新格式: REQ-NNNNN · <需求标题> 状态=...
  解析源:read require/<REQ-NNNNN>/RESULT.md 第 1 行
  退化:解析失败 → 沿用原格式(无标题)
```

## 与上游概要设计的不一致

**0 项**:本计划 100% 沿用概要设计 8 项决策 + 8 项不变量 + 8 个模块拆分。
