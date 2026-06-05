# 接口详细规格 — REQ-00013
更新时间:2026-06-05 21:30
版本:V0.0.2

## 接口:truncateTitle(共享工具函数)

- **形式**:函数(各 SKILL.md 内伪代码完整化,无独立文件)
- **签名**:`truncateTitle(title: string, maxLen: number = 30): string`
- **入参**:
  - `title`:原始标题(必填,字符串,无长度上限)
  - `maxLen`:最大字符数(选填,默认 30)
- **出参**:`string`(截断后的标题,超 maxLen 时末尾加 `...`)
- **字符数计算**:汉字/字母/数字/标点 = 1 字(用 JavaScript `[...title]` 数组 spread 按 Unicode code point 计数)
- **示例**:
  - 正常:`truncateTitle("Marketplace 改名落地", 30)` → `"Marketplace 改名落地"`(9 字,未截断)
  - 截断:`truncateTitle("优化 code-require / code-design / code-plan,增加'首步拉取最新代码'与'末步兜底提交'", 30)` → `"优化 code-require / code-design ..."`(30 字 + `...`)
- **错误码**:N/A(纯函数,无错误)
- **版本策略**:本轮 v1,后续 v2 可调整 `maxLen` 默认值
- **依据规范**:NFR-3

## 接口:formatReqTitle(需求标题格式化)

- **形式**:函数
- **签名**:`formatReqTitle(reqNum: string, title: string): string`
- **入参**:
  - `reqNum`:需求编码(必填,字符串,匹配 `^REQ-\d{5}$`)
  - `title`:需求标题(必填,字符串)
- **出参**:`string`(格式: `REQ-NNNNN · <截断后的标题>`)
- **示例**:
  - `formatReqTitle("REQ-00013", "优化 6 技能,启用'编号+标题'显示")` → `"REQ-00013 · 优化 6 技能,启用'编号+标题'显示"`
- **依据规范**:Q-2 锁定 A(中点 `·` + 半角空格)

## 接口:formatTaskTitle(任务标题格式化)

- **形式**:函数
- **签名**:`formatTaskTitle(taskNum: string, title: string): string`
- **入参**:
  - `taskNum`:任务编码(必填,字符串,匹配 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` 或旧格式 `^(REQ|BUG)-\d{5}-\d{5}$`)
  - `title`:任务标题(必填,字符串)
- **出参**:`string`(格式: `TASK-... · <截断后的标题>`)
- **示例**:
  - `formatTaskTitle("TASK-REQ-00013-001", "code-require/SKILL.md 增量追加")` → `"TASK-REQ-00013-001 · code-require/SKILL.md 增量追加"`
- **依据规范**:Q-2 锁定 A + `encoding-conventions §规则 1+3`

## 接口:formatBugTitle(缺陷标题格式化)

- **形式**:函数
- **签名**:`formatBugTitle(bugNum: string, title: string): string`
- **入参**:
  - `bugNum`:缺陷编码(必填,字符串,匹配 `^BUG-\d{5}$`)
  - `title`:缺陷标题(必填,字符串)
- **出参**:`string`(格式: `BUG-NNNNN · <截断后的标题>`)
- **示例**:
  - `formatBugTitle("BUG-00001", "某 X 函数崩溃")` → `"BUG-00001 · 某 X 函数崩溃"`
- **依据规范**:Q-2 锁定 A

## 接口:parseResultTitle(需求标题解析)

- **形式**:函数
- **签名**:`parseResultTitle(filePath: string): string`
- **入参**:`filePath`:`./assistants/<版本号>/require/<需求编号>/RESULT.md` 路径
- **出参**:`string`(需求标题,失败时返回空字符串 `""`,退化场景 E-3)
- **实现**:
  ```ts
  const content = readFileSync(filePath, 'utf-8')
  const match = content.match(/^# 需求提示词文档 — (.+)$/m)
  return match ? match[1] : ''
  ```
- **失败处理**:E-3 退化 — 返回空字符串,屏幕输出"编号+(无标题)"

## 接口:parsePlanTaskTitle(任务标题解析)

- **形式**:函数
- **签名**:`parsePlanTaskTitle(planPath: string, taskNum: string): string`
- **入参**:
  - `planPath`:`./assistants/<版本号>/plan/<需求编号>/PLAN.md` 路径
  - `taskNum`:任务编码
- **出参**:`string`(任务标题,失败时返回空字符串)
- **实现**:
  ```ts
  const content = readFileSync(planPath, 'utf-8')
  // 任务总览表格行: | 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | ... |
  const lines = content.split('\n').filter(l => l.startsWith('|') && l.includes(taskNum))
  for (const line of lines) {
    const cols = line.split('|').map(c => c.trim())
    if (cols[1] === taskNum && cols[5]) return cols[5] // 第 5 列为"标题"
  }
  return ''
  ```
- **失败处理**:E-3 退化

## 接口:parseFixTitle(缺陷标题解析)

- **形式**:函数
- **签名**:`parseFixTitle(fixPath: string): string`
- **入参**:`fixPath`:`./assistants/<版本号>/fix/<缺陷编号>/RESULT.md` 路径
- **出参**:`string`(缺陷标题,失败时返回空字符串)
- **实现**:
  ```ts
  const content = readFileSync(fixPath, 'utf-8')
  // 匹配 "## 缺陷标题" 后第 1 行非空内容
  const match = content.match(/^## 缺陷标题\s*\n+(.+?)$/m)
  return match ? match[1] : ''
  ```
- **失败处理**:E-3 / E-5 退化

## 接口:屏幕输出格式契约(13 类)

| 输出场景 | 格式 | 触发技能 |
| --- | --- | --- |
| 启动 | `正在处理: REQ-NNNNN · <需求标题>` | `code-require` / `code-plan` / `code-review` |
| 启动 | `正在处理: TASK-... · <任务标题>` | `code-it` / `code-unit` |
| 启动 | `正在处理: BUG-NNNNN · <缺陷标题>` | `code-fix` |
| 完成 | `完成: REQ-NNNNN · <需求标题>` | `code-require` |
| 完成 | `完成: REQ-NNNNN · <需求标题>(拆 N 个任务)` | `code-plan` |
| 完成 | `已修复: BUG-NNNNN · <缺陷标题>` | `code-fix` |
| 完成 | `已完成: TASK-... · <任务标题>` | `code-it` |
| 完成 | `已运行-通过/失败: TASK-... · <任务标题>` | `code-unit` |
| 完成 | `已评审: REQ-NNNNN · <需求标题>(N 条发现)` | `code-review` |
| 拆分 | `拆分: TASK-... · <任务标题>` | `code-plan` |
| 派生任务 | `派生任务: TASK-... · <任务标题>(审查派生)` | `code-review` |
| 中止 | `⛔ code-it 中止(存在未完成的前置任务)\n正在处理: REQ-NNNNN · <需求标题>(任务 TASK-... · <任务标题>)` | `code-it` |
| 守卫跳过 | `⏭ code-unit 跳过: TASK-... · <任务标题>(项目不可测)` | `code-unit` |
| 进度日志 | `[code-auto] 步骤 N/M:code-require REQ-NNNNN · <需求标题>` | `code-auto` |
| 进度日志 | `[code-auto]   → 1/N:code-it TASK-... · <任务标题> ✓` | `code-auto` |
| 报告 | `✓ code-auto 完成: REQ-NNNNN · <需求标题>` | `code-auto` |
| 报告"未完成项" | `[需求] REQ-NNNNN · <需求标题> 状态=...(应该=...)` | `code-publish` |
| 报告"未完成项" | `[任务] TASK-... · <任务标题> 开发状态=...(应该=...)` | `code-publish` |
| 报告"未完成项" | `[缺陷] BUG-NNNNN · <缺陷标题> 状态=...(应该=...)` | `code-publish` |
