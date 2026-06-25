# 接口详细规格 — REQ-00040

更新时间:2026-06-25
版本:V0.0.3

## 概述

本需求定义 5 个内部伪代码函数(`detectStartability` / `reproduceBug` / `terminate` / `mergeLogsWithTimestamp` / `executeStep`),**不**产出实际代码模块(沿用 D-9:不新建 `code-fix/lib/` 共享库);函数伪代码内联到 `code-fix/SKILL.md` 步骤 0 末尾 + 步骤 6 末尾子节。

**0 项外部接口变更**:本需求**不**修改 `code-plan` / `code-it` / `code-check` / 其他 9 个 `code-*` 技能的任何接口。

---

## 接口 1:`detectStartability(cwd)`

### 形式
函数(伪代码,内联到 SKILL.md)

### 路径
`plugins/code-skills/skills/code-fix/SKILL.md` §"## 步骤 0.X" 子节

### 签名
```
function detectStartability(cwd: string) -> {
  canStart: bool,
  startCommand: string | null
}
```

### 入参
| 参数 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `cwd` | string | 是 | 工作目录绝对路径(由 `code-fix` 主进程传入) |

### 出参
| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `canStart` | bool | true = 至少 1 个启动命令命中;false = 全未命中 |
| `startCommand` | string \| null | 启动命令字面;`canStart = false` 时为 null |

### 错误码
- **不**抛异常(沿用 NFR-4 失败降级)
- 配置文件不存在 / JSON 解析失败 → 跳过该优先级,继续下一优先级(不报错)

### 示例
```json
// 命中 package.json + yarn.lock
{
  "canStart": true,
  "startCommand": "yarn start"
}

// 全未命中(纯库项目)
{
  "canStart": false,
  "startCommand": null
}
```

### 性能
- 8 个 `Bash: test -f` 调用,每次 < 50ms
- 总耗时 < 500ms(沿用 NFR-1)

### 版本策略
- 无版本号(伪代码,**不**作为外部 API)

### 依据规范
- NFR-3(不触发 `AskUserQuestion`)
- NFR-9(不修改项目配置)

---

## 接口 2:`reproduceBug(bugNum, startCommand, reproSteps, timeout)`

### 形式
函数(伪代码,内联到 SKILL.md)

### 路径
`plugins/code-skills/skills/code-fix/SKILL.md` §"## 步骤 6.X" 子节

### 签名
```
function reproduceBug(
  bugNum: string,
  startCommand: string,
  reproSteps: Step[],
  timeout: number = 60  // 秒
) -> Meta
```

### 入参
| 参数 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `bugNum` | string | 是 | BUG-NNNNN 格式(沿用 `encoding-conventions §规则 1`) |
| `startCommand` | string | 是 | 启动命令字面(由 `detectStartability()` 产出) |
| `reproSteps` | Step[] | 是 | 复现步骤数组(由用户输入解析) |
| `timeout` | number | 否 | 总超时(秒),默认 60 |

### 出参
| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `bugNum` | string | BUG-NNNNN |
| `startCommand` | string | 启动命令 |
| `startedAt` | string | YYYY-MM-DD HH:mm:ss |
| `endedAt` | string | YYYY-MM-DD HH:mm:ss |
| `exitCode` | number | 子进程退出码(0 / 1 / 124) |
| `reproduceResult` | enum | `已复现` / `未复现` / `复现失败` |
| `artifacts` | Artifact[] | 产物清单 |
| `failureReason` | string \| null | 失败原因(成功时 null) |

### 错误码
- 启动失败(exit ≠ 0)→ `reproduceResult = 复现失败(启动失败)` + 屏显 `⚠`
- 超时(> timeout)→ `reproduceResult = 复现失败(超时)` + 屏显 `⚠ 启动超时`
- 异常(try 块)→ `reproduceResult = 复现失败(<message>)` + 屏显 `⚠ <message>`
- 任何错误**不**抛异常;**不**阻断 `code-fix` 主流程(NFR-4)

### 示例
```json
// 成功案例
{
  "bugNum": "BUG-00006",
  "startCommand": "yarn start",
  "startedAt": "2026-06-25 14:30:00",
  "endedAt": "2026-06-25 14:30:45",
  "exitCode": 0,
  "reproduceResult": "已复现",
  "artifacts": [
    { "type": "log", "path": "run.log", "size": 1234 },
    { "type": "interaction", "path": "interaction-1.json", "size": 567 }
  ],
  "failureReason": null
}

// 失败案例(超时)
{
  "bugNum": "BUG-00006",
  "startCommand": "yarn start",
  "startedAt": "2026-06-25 14:30:00",
  "endedAt": "2026-06-25 14:31:00",
  "exitCode": 124,
  "reproduceResult": "复现失败(超时)",
  "artifacts": [
    { "type": "log", "path": "run.log", "size": 0 }
  ],
  "failureReason": "Timeout after 60s"
}
```

### 性能
- 启动 5s + 步骤执行 < 55s = 总 < 60s
- 屏显契约 O(1) 行

### 版本策略
- 无版本号(伪代码)

### 兼容策略
- 沿用既有 `code-fix` 主流程;**不**修改 5 步既有步骤 0~10 的任何字面

### 依据规范
- NFR-2(不触发状态推进)
- NFR-3(不触发 `AskUserQuestion`)
- NFR-4(失败降级不阻断)
- NFR-6(更新分支不触发,幂等)

---

## 接口 3:`executeStep(step, reproduceDir)`

### 形式
函数(伪代码,内联到 SKILL.md 步骤 6.X 子节)

### 路径
`plugins/code-skills/skills/code-fix/SKILL.md` §"## 步骤 6.X" 子节(由 `reproduceBug()` 在循环中调)

### 签名
```
function executeStep(step: Step, reproduceDir: string) -> void
```

### 入参
| 参数 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `step` | Step | 是 | 复现步骤对象(由用户输入解析) |
| `reproduceDir` | string | 是 | 产物目录绝对路径 |

### Step 对象结构
```typescript
interface Step {
  index: number;          // 步骤序号(从 1 起)
  type: "cli" | "http" | "browser";  // 步骤类型
  command?: string;       // type=cli 时,命令行
  method?: "GET" | "POST" | "PUT" | "DELETE";  // type=http 时,HTTP 方法
  url?: string;           // type=http/browser 时,URL
  headers?: object;       // type=http 时,HTTP headers
  body?: any;             // type=http 时,请求体
}
```

### 出参
- void(产物写到 `reproduceDir` 子进程 stdout / stderr + 独立文件)

### 错误码
- HTTP 调用失败 → 仍写 `interaction-N.json`,`responseStatus = null` + `error = "<失败信息>"`
- 截图工具不可用 → 跳过,屏显 `⚠ 截图工具不可用,跳过截图产物`(E-6)
- 步骤类型未知 → 屏显 `⚠ 未知步骤类型:<type>`,跳过该步骤

### 示例
```typescript
// HTTP 步骤
{
  "index": 1,
  "type": "http",
  "method": "POST",
  "url": "http://localhost:3000/api/login",
  "headers": { "Content-Type": "application/json" },
  "body": { "username": "test", "password": "wrong" }
}

// CLI 步骤
{
  "index": 2,
  "type": "cli",
  "command": "curl -X POST http://localhost:3000/api/logout"
}

// 浏览器步骤
{
  "index": 3,
  "type": "browser",
  "url": "http://localhost:3000/login"
}
```

### 性能
- 单步骤 < 30s(在 60s 总超时内)
- 3 类产物各 O(1) 次 Bash 调用

### 依据规范
- NFR-1(性能 < 60s)
- NFR-3(不触发 `AskUserQuestion`)

---

## 接口 4:`mergeLogsWithTimestamp(stdout, stderr, outputPath)`

### 形式
函数(伪代码)

### 签名
```
function mergeLogsWithTimestamp(
  stdoutPath: string,
  stderrPath: string,
  outputPath: string
) -> void
```

### 入参
| 参数 | 类型 | 必填 | 约束 |
| --- | --- | --- | --- |
| `stdoutPath` | string | 是 | `run.stdout.log` 绝对路径 |
| `stderrPath` | string | 是 | `run.stderr.log` 绝对路径 |
| `outputPath` | string | 是 | `run.log` 绝对路径(输出) |

### 出参
- void(写到 `outputPath`)

### 行为
- 读 `stdoutPath` + `stderrPath` 行
- 每行加 `YYYY-MM-DD HH:mm:ss` 时间戳前缀(沿用 PD-4)
- 合并 → `outputPath`(stdout 在前,stderr 在后)
- 日志过大(> 10MB)→ 截断到前 1MB + 屏显 `⚠ 日志过大,已截断`(E-5)

### 依据规范
- NFR-4(失败降级)

---

## 接口 5:`terminate(childProcess, signal, waitTime, fallbackSignal)`

### 形式
函数(伪代码)

### 签名
```
function terminate(
  childProcess: Process,
  signal: "SIGTERM" | "SIGKILL" = "SIGTERM",
  waitTime: number = 5,  // 秒
  fallbackSignal: "SIGKILL" = "SIGKILL"
) -> void
```

### 行为
- 沿用 PD-3:先 `kill -SIGTERM` → 等 `waitTime` 秒 → 进程仍在跑 → `kill -SIGKILL`

### 出参
- void

### 依据规范
- NFR-4(失败降级)
- NFR-9(不修改项目配置)

---

## 总体约束(本节)

- **0 项外部 API 变更**(本需求**不**修改任何 `code-*` 技能的对外接口)
- **5 项内部伪代码函数**(全部内联到 `code-fix/SKILL.md`,不抽出 `lib/` 目录)
- **不**产出实际代码(本仓库是 Markdown 技能库,无 TS/JS 编译)
- **不**触发现有任何接口的版本号变更
