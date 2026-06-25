# 模块详细化 — REQ-00040

更新时间:2026-06-25
版本:V0.0.3

## 模块 1:`code-fix` 步骤 0 末尾追加"项目可启动性探测" 子节

### 路径

`plugins/code-skills/skills/code-fix/SKILL.md` §"## 步骤 0 — 版本上下文检测(强制前置)" 末尾(锚点:line 181 "4. 验证目录存在" 后,line 182 "### 步骤 1" 前)

### 关键伪代码

```
### 步骤 0.X — 项目可启动性探测(本需求新增子节,在步骤 0 第 4 项后)

伪代码:
function detectStartability(cwd):
  canStart = false
  startCommand = null

  // 优先级 1:Node.js / Frontend / Full-stack
  if exists(cwd + "/package.json"):
    pkg = readJson(cwd + "/package.json")
    if pkg.scripts and pkg.scripts.start:
      canStart = true
      if exists(cwd + "/pnpm-lock.yaml"): startCommand = "pnpm start"
      elif exists(cwd + "/yarn.lock"):    startCommand = "yarn start"
      else:                                startCommand = "npm start"

  // 优先级 2:Python
  elif exists(cwd + "/pyproject.toml") or exists(cwd + "/setup.py") or exists(cwd + "/requirements.txt"):
    canStart = true
    startCommand = "python -m <module>"  // 或 "python main.py"(用户后续可在 step 5 调整)

  // 优先级 3:Makefile
  elif exists(cwd + "/Makefile"):
    canStart = true
    startCommand = "make start"  // 或 "make run" / "make dev"(按 target 检测)

  // 优先级 4:Docker Compose
  elif exists(cwd + "/docker-compose.yml") or exists(cwd + "/docker-compose.yaml"):
    canStart = true
    startCommand = "docker compose up"

  // 优先级 5:Rust
  elif exists(cwd + "/Cargo.toml"):
    canStart = true
    startCommand = "cargo run"

  // 优先级 6:Go
  elif exists(cwd + "/go.mod"):
    canStart = true
    startCommand = "go run ."

  // 优先级 7:Java Maven
  elif exists(cwd + "/pom.xml"):
    canStart = true
    startCommand = "mvn spring-boot:run"

  // 优先级 8:Java Gradle
  elif exists(cwd + "/build.gradle") or exists(cwd + "/build.gradle.kts"):
    canStart = true
    startCommand = "gradle bootRun"

  // 写入内存上下文(不写文件,沿用 PD-1)
  context.canStart = canStart
  context.startCommand = startCommand
  return context
```

### 关键类 / 函数

- `detectStartability(cwd): Context` — 主探测函数;返回内存上下文对象 `{canStart: bool, startCommand: string | null}`

### 调用顺序

1. `code-fix` 步骤 0 第 4 项完成(验证目录存在)
2. **调用** `detectStartability(cwd)`
3. 内存上下文存 `context.canStart` / `context.startCommand`
4. 不输出屏显(NFR-3 不触发 `AskUserQuestion`)
5. 步骤 6 末尾子节读 `context.canStart` 判定是否触发复现动作

### 状态归属

- 内存上下文,生命周期 = 单次 `code-fix` 调用
- 不写 `fix/<BUG-NNN>/RESULT.md`
- 不写 `git` / 不修改项目配置

### 错误处理范式

- 配置文件不存在 / JSON 解析失败 → 跳过该优先级,继续下一优先级
- 所有优先级都未命中 → `canStart = false`,`startCommand = null`(沿用 E-1 降级)
- **不**抛异常;**不**中断 `code-fix` 主流程

### 日志埋点

- 探测命中 → 内存上下文,无屏显
- 探测全未命中 → 屏显 `⚠ 项目无可识别启动命令,跳过复现动作`

### 性能

- O(1) ~ O(8) 个 `Bash: test -f` 调用;总耗时 < 500ms(沿用 NFR-1)

### 与概要设计的对应

- `design/.../RESULT.md §3.1 D-1` + `§3.2 INV-1/2/3`
- 详设直接落地:不展开"接口细节"(无外部接口)

### 符合的规范

- `skill-conventions §规则 1`:`code-fix/SKILL.md` frontmatter 字节级保留
- `skill-conventions §规则 2`:本子节**不**写"本需求 REQ-00040 新增" 等开发痕迹字面
- NFR-3:不触发 `AskUserQuestion`,不新增 CLI 参数
- NFR-9:不修改项目配置 / 不写入任何项目文件

## 模块 2:`code-fix` 步骤 6 末尾追加"复现产物登记" 子节

### 路径

`plugins/code-skills/skills/code-fix/SKILL.md` §"## 步骤 6 — 写缺陷详情 RESULT.md" 末尾(锚点:line 305 "**关键:不重写 RESULT.md 的稳定章节**" 注释前)

### 关键伪代码

```
### 步骤 6.X — 复现产物登记(本需求新增子节,在步骤 6 "**关键:不重写**" 注释前)

触发条件(全部满足时触发):
  1. context.canStart == true          (模块 1 探测结果)
  2. 当前是"新建分支"                   (更新分支不触发,沿用 NFR-6 幂等)
  3. 用户在步骤 1 / 5 提供了"复现步骤"  (可由 "### 复现步骤" 段内容长度 > 0 判定)

伪代码:
function reproduceBug(bugNum, startCommand, reproSteps, timeout = 60):
  reproduceDir = "./assistants/<version>/fix/" + bugNum + "/reproduce/"
  mkdir(reproduceDir)

  startedAt = now()
  // 启动子进程
  childProcess = Bash: <startCommand> > reproduceDir + "run.stdout.log" 2> reproduceDir + "run.stderr.log"
  sleep 5s  // 给程序启动时间

  // 执行复现步骤
  try:
    for each step in reproSteps:
      executeStep(step, reproduceDir)  // 详见模块 3
    exitCode = 0
    reproduceResult = "已复现"  // 默认;若步骤未触发 bug,改为 "未复现"
  except TimeoutError:
    terminate(childProcess, SIGTERM, 5s, SIGKILL)
    exitCode = 124  // timeout 退出码
    reproduceResult = "复现失败(超时)"
  except Exception as e:
    terminate(childProcess)
    exitCode = 1
    reproduceResult = "复现失败(" + e.message + ")"

  // 终止子进程(若仍在跑)
  if childProcess.isRunning():
    terminate(childProcess, SIGTERM, 5s, SIGKILL)

  endedAt = now()

  // 合并 stdout + stderr → run.log(加时间戳,沿用 PD-4)
  mergeLogsWithTimestamp(reproduceDir + "run.stdout.log", reproduceDir + "run.stderr.log", reproduceDir + "run.log")

  // 写元信息(沿用 PD-5 单行 JSON)
  meta = {
    bugNum: bugNum,
    startCommand: startCommand,
    startedAt: startedAt,
    endedAt: endedAt,
    exitCode: exitCode,
    reproduceResult: reproduceResult,
    artifacts: listArtifacts(reproduceDir),
    failureReason: e.message if exception else null
  }
  writeFile(reproduceDir + "RESULT-meta.json", jsonStringify(meta, no_indent))

  // 写"## 复现产物登记" 区段到 fix/<BUG-NNN>/RESULT.md
  writeReproSection(fixResultPath, meta, reproduceDir)

  return meta
```

### 关键类 / 函数

- `reproduceBug(bugNum, startCommand, reproSteps, timeout): Meta` — 主复现函数
- `terminate(childProcess, signal, waitTime, fallbackSignal)` — 终止子进程(沿用 PD-3)
- `mergeLogsWithTimestamp(stdout, stderr, outputPath)` — 合并日志(沿用 PD-4)
- `listArtifacts(reproduceDir): Artifact[]` — 列举产物(供 meta.artifacts)
- `writeReproSection(fixResultPath, meta, reproduceDir)` — 写"## 复现产物登记" 区段

### 调用顺序

1. `code-fix` 步骤 6 主体完成(写完 `fix/<BUG-NNN>/RESULT.md` 的"## 缺陷描述" 段等)
2. **检查触发条件 3 条**(canStart / 新建分支 / 有复现步骤)
3. **触发** → 调 `reproduceBug()`
4. **不触发** → 跳过(沿用 E-7 文本复现 / E-1 无启动命令)
5. 失败 → 屏显 `⚠` + 写元信息 + 写"## 复现产物登记" 区段(NFR-4 不阻断)

### 状态归属

- 子进程 = 临时,生命周期 ≤ 60s(timeout)
- `reproduce/` 子目录 = 持久(沿用 NFR-7)
- 内存状态(进程句柄) = 临时,函数返回后释放

### 错误处理范式

- 启动失败(子进程 exit ≠ 0 在 5s 内)→ 屏显 `⚠ 启动失败:<stderr 前 500 字符>` + meta.reproduceResult = "复现失败(启动失败)" + 继续
- 复现超时(> 60s)→ 终止进程 + 屏显 `⚠ 启动超时` + meta.reproduceResult = "复现失败(超时)" + 继续
- 步骤未触发 bug → meta.reproduceResult = "未复现" + 继续
- 日志过大(> 10MB)→ 截断到前 1MB + 屏显 `⚠ 日志过大,已截断` + 继续
- 截图工具不可用 → 跳过截图,屏显 `⚠ 截图工具不可用` + 继续
- 任何异常 → 屏显 `⚠ <错误信息>` + 继续(NFR-4)

### 日志埋点

- 启动成功 → 屏显 `=== code-fix 复现动作(步骤 6 末尾)===\n 启动命令:<command>\n 产物目录:<reproduceDir>`
- 启动失败 → 屏显 `⚠ 启动失败:<stderr 前 500 字符>`
- 复现完成 → 屏显 `=== code-fix 复现完成 ===\n 退出码:<N>\n 复现结论:<已复现 / 未复现 / 复现失败>\n 产物数:<N> 个`

### 性能

- 启动 5s + 步骤执行 < 55s = 总 < 60s(沿用 NFR-1)
- 屏显契约 O(1) 行

### 与概要设计的对应

- `design/.../RESULT.md §3.1 D-2/D-3/D-4` + `§3.2 INV-1/2/3`
- 详设直接落地:不展开"接口细节"(无外部接口)

### 符合的规范

- NFR-2:不触发状态推进(沿用 REQ-00037)
- NFR-3:不触发 `AskUserQuestion`,不新增 CLI 参数
- NFR-4:失败降级不阻断
- NFR-6:更新分支不触发(幂等)
- NFR-9:不修改项目配置

## 模块 3:`executeStep()` 3 类产物采集

### 路径

`code-fix/SKILL.md` 步骤 6 末尾子节内联(伪代码);不抽到 `lib/`

### 关键伪代码

```
function executeStep(step, reproduceDir):
  // 步骤 3 类:命令行 / HTTP / 浏览器操作
  switch step.type:
  case "cli":
    // 直接执行命令,stdout / stderr 已通过 > 重定向到子进程(本步骤无需额外操作)
    Bash: <step.command>
    break
  case "http":
    // 交互数据采集(沿用 PD-7)
    response = Bash: curl -X <step.method> -H "<step.headers>" -d '<step.body>' <step.url>
    interaction = {
      step: step.index,
      method: step.method,
      url: step.url,
      headers: step.headers,
      requestBody: step.body,
      responseStatus: response.status,
      responseBody: response.body,
      responseHeaders: response.headers
    }
    writeFile(reproduceDir + "interaction-" + step.index + ".json", jsonStringify(interaction, indent=2))
    break
  case "browser":
    // 截图采集(沿用 PD-6)
    // 链式降级:playwright → puppeteer → headless-chrome
    if Bash: command -v playwright:
      Bash: npx playwright screenshot <step.url> <reproduceDir + "screenshot-" + step.index + ".png">
    elif Bash: command -v puppeteer:
      Bash: npx puppeteer-cli screenshot <step.url> --output <reproduceDir + "screenshot-" + step.index + ".png">
    elif Bash: command -v chrome:
      Bash: chrome --headless --screenshot=<reproduceDir + "screenshot-" + step.index + ".png"> <step.url>
    else:
      // 截图工具不可用(E-6)
      log("⚠ 截图工具不可用,跳过截图产物")
    break
  default:
    log("⚠ 未知步骤类型:" + step.type)
```

### 关键类 / 函数

- `executeStep(step, reproduceDir)` — 步骤执行 + 产物采集
- 内部按 `step.type` 分发:`cli` / `http` / `browser`

### 调用顺序

由 `reproduceBug()` 在循环中调 `executeStep(step, reproduceDir)`

### 错误处理范式

- HTTP 调用失败 → 仍写 `interaction-N.json`,`responseStatus = null` + `error = "<失败信息>"`
- 截图工具不可用 → 跳过,屏显 `⚠`
- 步骤类型未知 → 屏显 `⚠`,跳过该步骤

### 与概要设计的对应

- `design/.../RESULT.md §3.1 D-5` + `§5 FR-3.1/3.2/3.3`

## 模块 4:`bug.md` 模板扩展

### 路径

`plugins/code-skills/skills/code-fix/templates/bug.md`(模板)

### 变更

1. **文档头"## 文档头" 表新增 2 行**(锚点:line 22 后,line 24 `### 状态枚举` 前):
 - 复现方式:`程序复现` / `文本复现` / `未复现`
 - 产物路径:`reproduce/`(子目录相对路径;空表示无产物)
2. **"## 缺陷描述" 段后(在 `---` 分隔符 + "## 根因分析" 段前)插入"## 复现产物登记" 区段**(锚点:line 60 前)
3. **既有 9 区段字节级保留**(INV-4)

### 关键区段结构

```markdown
## 复现产物登记(由 code-fix 步骤 6 末尾)

> 复现方式:程序复现 / 文本复现 / 未复现
> 启动命令:<command>(若启动成功)
> 运行时间:YYYY-MM-DD HH:mm ~ HH:mm

### 产物清单

| 产物类型 | 文件路径(相对 RESULT.md) | 大小 | 用途 |
| --- | --- | --- | --- |
| 日志 | reproduce/run.log | <N> KB | 进程 stdout/stderr 合并记录 |
| 截图 | reproduce/screenshot-1.png | <N> KB | 步骤 1 后 UI 状态 |
| 交互数据 | reproduce/interaction-1.json | <N> KB | 步骤 1 后 API 响应 |

### 实际行为

<复现过程中观察到的现象,含错误信息/堆栈/UI 异常>

### 复现结论

已复现 / 未复现 / 复现失败(<原因>)
```

### 与概要设计的对应

- `design/.../RESULT.md §3.1 D-6/D-7` + `§3.2 INV-4`

### 符合的规范

- NFR-3:不触发 `AskUserQuestion`,不新增字段(除文档头 2 行)
- NFR-8:**不**含"本需求 REQ-00040 新增" 等开发痕迹字面
- `skill-conventions §规则 2`:模板内容纯净度

## 模块 5:`assistants-layout.md` 同步更新

### 路径

`plugins/code-skills/skills/code-fix/templates/assistants-layout.md`

### 变更

在 `fix/<BUG-NNN>/` 子目录列表(line 16-19)中追加 `reproduce/` 行:

```diff
├── BUG-00001/ # 第一个缺陷
│ ├── RESULT.md # ★ 缺陷详情(本技能首次/更新)
│ ├── investigation.md # 调查笔记(可选)
│ ├── fix-plan.md # 修复方案(由 code-plan 写入)
│ ├── fix-work-log.md # 实施日志(由 code-it 写入)
│ ├── fix-compile-and-run.md # 编译/运行(由 code-it 写入)
│ ├── fix-test-results.md # 测试结果(由 code-it 写入)
│ ├── deviations.md # 偏离记录(由 code-it 写入)
+│ └── reproduce/ # 复现产物(由 code-fix 步骤 6 末尾生成,可选)
```

### 与概要设计的对应

- `design/.../RESULT.md §3.1 D-8`

## 模块 6:版本看板同步

### 路径

`./assistants/V0.0.3/RESULT.md`(由 `code-plan` 步骤 16A 同步)

### 变更

- 文档头"最近更新"时间刷新
- "详细设计与任务计划汇总" 区段追加 1 行(本计划)
- "任务清单" 区段追加 6 行(6 个任务)
- "里程碑" 区段追加 1 行(M1-REQ-00040)
- "变更记录" 区段追加 1 条

### 与概要设计的对应

- `code-plan/SKILL.md §步骤 16A` 强约束
- 0 触发 `dashboard-conventions §规则 1`(任务清单 12 列字节级保留)
