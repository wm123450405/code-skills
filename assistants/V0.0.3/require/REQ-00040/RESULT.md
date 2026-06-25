# 需求提示词文档 — 优化 /code-fix 技能:登记缺陷时启动程序复现并登记证据

- 需求编码:REQ-00040
- 所属版本:V0.0.3
- 文档创建时间:2026-06-25
- 最近更新:2026-06-25
- 文档状态:草稿(待 code-design 推进)
- 上游:用户口头/文本输入(2026-06-25)
- 遵循规范:`./assistants/rules/` 下 13 个文件(全沿用,无新增)
- 涉及技能:`code-fix`(主改造)+ `code-fix/templates/bug.md`(模板改造)

## 1. 需求概述

**优化** `/code-fix` 技能在登记缺陷时的能力:分析项目是否允许启动程序,若允许则启动并按缺陷描述复现,获取 3 类证据(日志 / 截图 / 交互数据)作为缺陷附件。

**核心机制**:
- **可启动性探测**(FR-1):在 `code-fix` 步骤 0 末尾追加"项目可启动性探测" 子节,自动判定 `canStart: bool` + 推导 `startCommand: string | null`
- **复现动作触发**(FR-2):在 `code-fix` 步骤 6 末尾追加"复现产物登记" 动作,`canStart = true` 且用户提供复现步骤时执行
- **3 类产物收集**(FR-3):日志(进程 stdout/stderr)/ 截图(UI 缺陷)/ 交互数据(API 缺陷)
- **产物子目录**(FR-4):`fix/<BUG-NNN>/reproduce/`,产物以相对路径登记到 RESULT.md
- **模板扩展**(FR-5):`bug.md` 新增"## 复现产物登记" 区段,与既有"## 缺陷描述" 段协同
- **失败降级**(NFR-4):启动失败 / 复现未触发 / 超时 → 屏显 `⚠` + 记录原因 + 继续以 `待处理` 状态登记

涉及 1 SKILL.md(`code-fix`)+ 1 模板(`bug.md`),共 2 个文件,净变化约 +60 ~ +100 行(扩展,不删除)。

## 2. 背景与目标

### 2.1 背景

V0.0.3 期间 `code-fix` 是**纯登记型**技能:用户报告缺陷 → 写入 `fix/<BUG-NNN>/RESULT.md` → 状态推进 → 引导用户调 `code-plan` / `code-it` / `code-check`(沿用 REQ-00027 / REQ-00037)。当前模板(`bug.md`)虽含"复现步骤 / 期望行为 / 实际行为" 三段,但**没有"复现证据"概念** —— 证据全靠用户在"实际行为"段文字描述,无法承载:

- 进程的 stdout / stderr 原始日志
- UI 缺陷的截图
- API 缺陷的请求/响应报文

`code-fix` 复跑既有 BUG(BUG-00001~05)时,这 5 个 BUG 的"实际行为" 段均为纯文字(无产物),后续 `code-plan` 写修复方案时**只能靠文字推断**根因,无法引用"用户跑出来的真实堆栈"。

**用户原始输入(verbatim)**:
> 优化 `/code-fix` 技能,在登记缺陷时,分析是否需要启动程序复现缺陷过程。若当前项目允许启动程序时应当启动程序并按照缺陷描述复现缺陷发生过程,以此可获得更多的日志、截图或交互数据来作证缺陷,方便后续分析并解决缺陷。复现过程中的日志、截图、交互数据都要被登记到缺陷信息中。

### 2.2 业务目标

- 在 `code-fix` 登记阶段增加"复现证据" 能力:启动程序 + 收集 3 类产物
- 产物放 `fix/<BUG-NNN>/reproduce/` 子目录,**不**进 `fix/RESULT.md` 总览 / 看板(沿用 NFR-7)
- 失败降级:启动失败不阻断 `code-fix` 主流程(沿用 REQ-00037 的"code-fix 不阻断" 精神)
- 模板扩展:在 `bug.md` 新增"## 复现产物登记" 区段,与既有"## 缺陷描述" 段协同
- 现有屏显契约 / frontmatter / 既有"## 工作流程" / "## 不要做的事" 全部字节级保留
- 与 REQ-00037 完全协同:本需求**不**改 REQ-00037 确定的初始态(`待处理`)与状态推进路径

### 2.3 本次目标

- **范围**:**改造** `code-fix/SKILL.md` 步骤 0 末尾 + 步骤 6 末尾 + **改造** `code-fix/templates/bug.md` 新增"## 复现产物登记" 区段
- **不涉及**:`code-fix` frontmatter / 既有"## 工作流程" 小节 / "## 不要做的事" 小节
- **不涉及**:其他 9 个 `code-*` 技能 SKILL.md / rules/ 目录
- **不涉及**:`fix/RESULT.md` 总览模板(`fix-registry.md`)**不**新增列(产物放 `fix/<BUG-NNN>/reproduce/` 子目录,**不**进总览)
- **不涉及**:版本看板"缺陷清单" 区段新增列(`dashboard-conventions §规则 1` 0 触发)
- **不涉及**:`code-fix` 既定状态推进路径(沿用 REQ-00037)
- **不涉及**:历史 5 个 BUG 的 `fix/<BUG-NNN>/RESULT.md`(字节级保留)
- 触发 1 次看板同步:`assistants/V0.0.3/RESULT.md` §需求清单 追加 1 行 + §变更记录 追加 1 条

## 3. 用户角色与场景

### 3.1 角色

- **缺陷报告人**:在 `code-fix` 登记时,期望"我描述了缺陷,工具自动帮我跑一遍并把证据贴进来",**不**需手动收集日志/截图
- **修复实施人(AI 协作者)**:在 `code-plan BUG-NNN` 时,期望直接读"## 复现产物登记" 段的真实堆栈/截图/响应,**不**靠文字推断根因
- **评审者**:在 `code-check BUG-NNN` 时,可交叉对照"## 缺陷描述" 的"### 期望行为" 与"## 复现产物登记" 段的"### 实际行为"是否一致
- **`code-auto` 编排者**:在自动流水线中,可读取"## 复现产物登记" 段判断"缺陷是否已复现"(`复现结论 = 已复现`)

### 3.2 场景

| 场景 | 现状体验(本需求前) | 改造后体验(本需求) |
| --- | --- | --- |
| 报告 web 缺陷,UI 错位 | 文字描述"按钮错位 2 像素" | `code-fix` 启动 web 服务,触发 UI 步骤,自动截图 → `reproduce/screenshot-1.png` |
| 报告 API 缺陷,500 错误 | 文字描述"返回 500" | `code-fix` 启动 api 服务,触发 API 请求,自动保存请求/响应 → `reproduce/interaction-1.json` |
| 报告命令行缺陷,segfault | 文字描述"程序崩溃" | `code-fix` 启动程序,触发步骤,自动保存 stdout/stderr → `reproduce/run.log` |
| 用户未给复现步骤 | `code-fix` 文字描述登记 | `code-fix` 跳过复现动作,`复现方式 = 文本复现`(沿用) |
| 项目无启动命令(纯库项目) | 文字描述 | `code-fix` 探测 → `canStart = false` → 跳过复现动作,继续登记 |
| 启动失败 / 进程崩溃 | 不存在此场景(纯文字) | `code-fix` 屏显 `⚠` + 把失败原因写入"## 复现产物登记" 段,继续以 `待处理` 状态登记 |
| 复现超时(> 60s) | 不存在此场景 | `code-fix` 屏显 `⚠ 启动超时` + 终止进程 + 降级为文本复现 |
| 日志过大(> 10MB) | 不存在此场景 | `code-fix` 截断到前 1MB + 屏显 `⚠ 日志过大,已截断` |

## 4. 功能需求(FR)

### FR-1:项目可启动性探测(步骤 0 末尾子节)

- **位置**:`plugins/code-skills/skills/code-fix/SKILL.md` §"## 步骤 0 — 版本上下文检测" 末尾追加子节(在"4. 验证目录存在" 后)
- **作用**:探测 build/start/test 等命令是否可用,自动判定 `canStart: bool` + 推导 `startCommand: string | null`
- **算法**:
 ```
 function detectStartability(cwd):
 1. 检查 package.json:
 - 若 scripts.start 存在 → startCommand = "npm start" / "yarn start" / "pnpm start"(按 lockfile)
 2. 检查 Python:
 - 若 pyproject.toml / setup.py / requirements.txt 存在 → startCommand = "python -m <module>" 或 "python <entrypoint>"
 3. 检查 Makefile:
 - 若 target "start" / "run" / "dev" 存在 → startCommand = "make <target>"
 4. 检查 docker-compose.yml:
 - 若存在 → startCommand = "docker compose up"
 5. 检查 Cargo.toml / go.mod / pom.xml / build.gradle → 推导对应命令
 6. 若 ≥ 1 个命中 → canStart = true;否则 canStart = false
 7. 写入上下文(供步骤 6 末尾使用)
 ```
- **不**触发 `AskUserQuestion`(NFR-3 强约束;自动判定)
- **不**尝试启动:本子节只探测配置,**不**实际运行命令
- **超时预算**:探测总耗时 < 500ms(只读 `package.json` / `pyproject.toml` 等文件,无需 IO 密集操作)
- **不**写文件:探测结果只存内存上下文,**不**写 `fix/<BUG-NNN>/RESULT.md`(避免"空跑时也写产物")

### FR-2:复现动作触发(步骤 6 末尾子节)

- **位置**:`plugins/code-skills/skills/code-fix/SKILL.md` §"## 步骤 6 — 写缺陷详情 RESULT.md" 末尾追加子节(在"**关键:不重写 RESULT.md 的稳定章节**" 注释前)
- **触发条件**(全部满足时触发):
 1. `canStart = true`(FR-1 探测结果)
 2. 当前是"新建分支"(更新分支**不**触发,避免反复启动)
 3. 用户在步骤 1 / 5 提供了"复现步骤"(可由 `### 复现步骤` 段内容长度 > 0 判定)
- **算法**:
 ```
 function reproduceBug(bugNum, startCommand, reproSteps, timeout = 60s):
 1. mkdir -p fix/<bugNum>/reproduce/
 2. 启动子进程:<startCommand> > reproduce/run.stdout.log 2> reproduce/run.stderr.log
 3. 等 5s(给程序启动时间)
 4. 按 reproSteps 顺序执行(用 Bash 调 HTTP / CLI / 浏览器自动化工具,见 FR-3)
 5. 收集产物(见 FR-3)
 6. 进程仍在跑 → 终止(graceful shutdown,kill -SIGTERM 5s 后 kill -SIGKILL)
 7. 合并 stdout + stderr → reproduce/run.log(加时间戳前缀)
 8. 写 reproduce/RESULT-meta.json(含运行时间、退出码、产物清单)
 9. 失败降级(见 NFR-4)
 ```
- **执行环境**:子进程在 `cwd` 下运行(与 `code-fix` 主进程同 cwd);**不**改 cwd
- **超时**:默认 60s(可用 `code-fix` 内部计时器);超时 → 终止 + 降级
- **不**触发 `AskUserQuestion`(NFR-3)
- **不**修改项目源码(只读运行)

### FR-3:3 类产物收集

#### FR-3.1 日志产物
- **类型**:`run.log`(合并 stdout + stderr)
- **路径**:`fix/<BUG-NNN>/reproduce/run.log`
- **格式**:每行加 `YYYY-MM-DD HH:mm:ss` 时间戳前缀
- **截断**:**> 10MB → 截断到前 1MB**,屏显 `⚠ 日志过大,已截断到前 1MB`

#### FR-3.2 截图产物
- **类型**:`screenshot-{N}.png`
- **路径**:`fix/<BUG-NNN>/reproduce/screenshot-{N}.png`(N 从 1 起)
- **触发条件**:`startCommand` 启动的是 web 服务(端口 3000/5000/8000/8080 监听)或 desktop 应用(可执行文件以 `.app` / `.exe` 结尾)
- **采集时机**:每个复现步骤后
- **工具**:**首选** `playwright` (CLI:`npx playwright codegen` 已被嵌入,本需求用 `npx playwright screenshot URL output.png`);**备选** `puppeteer`(`npx puppeteer-cli`);**回退** `headless-chrome` (`chrome --headless --screenshot=output.png URL`)
- **N = 0 时**:**不**创建空 `reproduce/` 子目录(避免空目录)
- **失败降级**:截图工具不可用 → 跳过截图,屏显 `⚠ 截图工具不可用,跳过截图产物`

#### FR-3.3 交互数据产物
- **类型**:`interaction-{N}.json` 或 `interaction-{N}.txt`
- **路径**:`fix/<BUG-NNN>/reproduce/interaction-{N}.{json|txt}`
- **触发条件**:`startCommand` 启动的是 web/api 服务
- **采集时机**:每个 HTTP / API 请求
- **内容**:
 ```json
 {
  "step": 1,
  "method": "POST",
  "url": "http://localhost:3000/api/login",
  "headers": { "Content-Type": "application/json" },
  "request_body": { "username": "test", "password": "wrong" },
  "response_status": 500,
  "response_body": { "error": "Internal Server Error" },
  "response_headers": { "Content-Type": "application/json" }
 }
 ```
- **N = 0 时**:跳过
- **失败降级**:HTTP 调用失败 → 仍写入 `interaction-N.json`,`response_status = null` + `error = "<失败信息>"`

### FR-4:产物子目录设计

- **位置**:`fix/<BUG-NNN>/reproduce/`
- **结构**:
 ```
 fix/<BUG-NNN>/
 ├── RESULT.md
 └── reproduce/         ← 本需求新增子目录
 ├── run.log            ← 进程日志(必)
 ├── screenshot-1.png   ← 截图(可选)
 ├── interaction-1.json ← 交互数据(可选)
 └── RESULT-meta.json   ← 元信息(必):运行时间 / 退出码 / 产物清单
 ```
- **`RESULT-meta.json` 结构**:
 ```json
 {
  "bugNum": "BUG-00001",
  "startCommand": "npm start",
  "startedAt": "2026-06-25 14:30:00",
  "endedAt": "2026-06-25 14:30:45",
  "exitCode": 0,
  "reproduceResult": "已复现" | "未复现" | "复现失败",
  "artifacts": [
  { "type": "log", "path": "run.log", "size": 1234 },
  { "type": "screenshot", "path": "screenshot-1.png", "size": 5678 }
  ],
  "failureReason": null | "<失败原因>"
 }
 ```
- **不**进 `fix/RESULT.md` 总览(NFR-7 严守);**不**进看板(NFR-7)
- **清理**:`code-fix` **不**清理产物;若 `fix/<BUG-NNN>/` 被人工删除,子目录同步删除

### FR-5:`bug.md` 模板新增"## 复现产物登记" 区段

- **位置**:`plugins/code-skills/skills/code-fix/templates/bug.md` 在"## 缺陷描述" 段后(在"---" 分隔符 + "## 根因分析" 段前)插入新区段
- **结构**:
 ```markdown
 ## 复现产物登记(由 code-fix 步骤 6 末尾)

 > 复现方式:程序复现 / 文本复现 / 未复现
 > 启动命令:<command>(若启动成功)
 > 运行时间:YYYY-MM-DD HH:mm ~ HH:mm

 ### 产物清单

 | 产物类型 | 文件路径(相对 RESULT.md) | 大小 | 用途 |
 | --- | --- | --- | --- |
 | 日志 | reproduce/run.log | <N> KB | 进程 stdout/stderr 合并记录 |
 | 截图 | reproduce/screenshot-1.png | <N> KB | 步骤 N 后 UI 状态 |
 | 交互数据 | reproduce/interaction-1.json | <N> KB | 步骤 N 后 API 响应 |

 ### 实际行为

 <复现过程中观察到的现象,含错误信息/堆栈/UI 异常>

 ### 复现结论

 已复现 / 未复现 / 复现失败(<原因>)
 ```
- **既有"## 缺陷描述" 段协同**:
 - `### 复现步骤(若有)` 段:沿用,**不**重写
 - `### 期望行为` 段:沿用
 - `### 实际行为` 段(在"## 缺陷描述" 内):**保留**,作为用户文字描述;"## 复现产物登记" 段下的"### 实际行为" 是程序跑出来的证据
- **触发条件**:仅在"新建分支" 触发复现动作时填写;更新分支 / 文本复现 / 复现失败时,新区段仍生成但产物清单为空 / 复现结论写明
- **模板占位符**:`<bugNum>` / `<command>` / `<时间>` 沿用 `bug.md` 既有占位符风格

### FR-6:`fix/<BUG-NNN>/RESULT.md` 文档头新增字段

- **位置**:`bug.md` 文档头"## 文档头" 表新增 1 行
- **新增字段**:
 | 字段 | 值 |
 | --- | --- |
 | 复现方式 | `程序复现` / `文本复现` / `未复现` |
 | 产物路径 | `reproduce/`(子目录相对路径;空表示无产物) |
- **不触发** `dashboard-conventions §规则 1`(字段在 `fix/<BUG-NNN>/RESULT.md` 内部,**不**进 `fix/RESULT.md` 总览 / 看板)

## 5. 非功能需求 / 约束(NFR)

- **NFR-1(性能)**:探测耗时 < 500ms(FR-1);启动到 5s 等待 + 单步骤执行 < 60s 总超时(FR-2)
- **NFR-2(与 REQ-00037 协同)**:**不**改 REQ-00037 已确定的初始态(`待处理`)与状态推进路径;**不**改 5 新状态字面
- **NFR-3(零规范变更)**:
 - **不**修改 `code-fix` frontmatter(L1-3 字节级保留)
 - **不**修改既有"## 工作流程" 小节结构(只在步骤 0 / 6 末尾追加子节,既有步骤 1~5 字节级保留)
 - **不**修改"## 不要做的事" 小节
 - **不**触发 `AskUserQuestion`(自动探测 + 自动执行,无需用户介入)
 - **不**新增 CLI 参数(无 `--reproduce` / `--no-reproduce` 等)
- **NFR-4(失败降级)**:
 - 启动失败 / 进程崩溃 / 超时(> 60s)→ 屏显 `⚠` + 把失败原因写入"## 复现产物登记" 段的"### 复现结论" 子项 + 继续以 `待处理` 状态登记,**不**阻断 `code-fix` 主流程
 - 复现未触发 bug → 把"未触发"写入区段 + 继续登记
 - 日志过大(> 10MB)→ 截断到前 1MB + 屏显 `⚠ 日志过大,已截断`
- **NFR-5(历史 BUG 不追加)**:**不**改历史 5 个 BUG(BUG-00001~05)的 `fix/<BUG-NNN>/RESULT.md`(字节级保留);新区段仅对未来新登记的 BUG 生成
- **NFR-6(幂等)**:`code-fix` 复跑同一 BUG 多次 → 复现动作**不**重复执行(本需求只在"新建分支" 触发)
- **NFR-7(不污染总览 / 看板)**:产物放 `fix/<BUG-NNN>/reproduce/` 子目录;`fix/RESULT.md` 总览**不**新增列;版本看板"缺陷清单" 区段**不**新增列(`dashboard-conventions §规则 1` 0 触发)
- **NFR-8(不引入开发痕迹)**:**不**在 `code-fix/SKILL.md` / `bug.md` 模板中写"本需求 REQ-00040 新增" / "沿用原 code-fix" 等开发痕迹字面(沿用 `skill-conventions §规则 2`)
- **NFR-9(不修改项目源码)**:复现动作只读运行,触发命令均不修改任何项目文件;`code-fix` 复跑本身**不**写入 `package.json` / `pyproject.toml` 等配置文件
- **NFR-10(可追溯)**:每个有产物的 BUG 在 `fix/<BUG-NNN>/RESULT.md` 文档头有"复现方式" + "产物路径" 字段;在"## 复现产物登记" 段有完整产物清单

## 6. 页面与界面

不适用(本需求是 Markdown 技能行为变更 + 模板区段扩展,无 UI 改动)

## 7. 交互逻辑

不适用(无状态机变更;沿用既有 `code-fix` 主流程 + REQ-00037 已收敛的状态推进路径)

## 8. 数据与状态

- **输入数据**:
 - `cwd` 下的 `package.json` / `pyproject.toml` / `Makefile` / `docker-compose.yml` 等配置文件
 - 用户提供的"复现步骤"(`### 复现步骤` 段内容)
 - 上下文:`canStart` / `startCommand` / `timeout` / `projectType`
- **输出数据**(`fix/<BUG-NNN>/reproduce/`):
 - `run.log`(合并 stdout + stderr)
 - `screenshot-{N}.png`(UI 缺陷)
 - `interaction-{N}.{json|txt}`(API 缺陷)
 - `RESULT-meta.json`(元信息)
- **数据生命周期**:
 - `code-fix` 步骤 0 末尾:探测 1 次,写入内存上下文
 - `code-fix` 步骤 6 末尾:触发复现动作,写入 `fix/<BUG-NNN>/reproduce/` + `fix/<BUG-NNN>/RESULT.md` 的"## 复现产物登记" 段
 - 后续 `code-plan` / `code-it` / `code-check` 可**读**产物子目录(沿用既有"## 关联项" 段引用模式)

## 9. 边界与异常

- **E-1**:`canStart = false`(无启动命令)→ 跳过复现动作,`复现方式 = 文本复现`,继续登记
- **E-2**:启动命令执行失败(exit code ≠ 0)→ 屏显 `⚠ 启动失败:<stderr 前 500 字符>` + 把失败原因写入"## 复现产物登记" 段,继续登记
- **E-3**:复现超时(> 60s)→ 终止进程(kill -SIGTERM 5s 后 SIGKILL)+ 屏显 `⚠ 启动超时` + 降级为文本复现
- **E-4**:复现未触发 bug(用户报告 500 但程序返回 200)→ 把"未触发"写入"### 复现结论" 子项,继续登记
- **E-5**:日志过大(> 10MB)→ 截断到前 1MB + 屏显 `⚠ 日志过大,已截断到前 1MB`
- **E-6**:截图工具不可用(`playwright` / `puppeteer` / `headless-chrome` 都不存在)→ 跳过截图,屏显 `⚠ 截图工具不可用,跳过截图产物`
- **E-7**:用户未给复现步骤(`### 复现步骤` 段空)→ 跳过复现动作,`复现方式 = 文本复现`
- **E-8**:`code-fix` 复跑已有 BUG(更新分支)→ 跳过复现动作(本需求只在"新建分支" 触发)
- **E-9**:`code-auto` 上下文 → 沿用既有 NFR-3 / NFR-4(不触发 `AskUserQuestion` + 失败降级不阻断)
- **E-10**:`reproduce/` 子目录已存在(用户预置)→ 沿用既有产物,`code-fix` 在目录后追加 `_2` / `_3` 等后缀
- **E-11**:`fix/<BUG-NNN>/` 目录被人工删除后复跑 → 沿用既有 `code-fix` 步骤 2 行为(自动 `mkdir -p`)

## 10. 验收标准 (AC)

### AC-1:FR-1 步骤 0 末尾"项目可启动性探测" 子节生效

- **对应需求**:FR-1
- **验证方式**:静态校验
- **步骤**:
 1. 读 `code-fix/SKILL.md` 步骤 0 末尾
 2. 检查"## 步骤 0 — 版本上下文检测" 小节末尾是否有"### X.项目可启动性探测" 子节
- **预期结果**:子节存在,含探测算法 6 步伪代码
- **优先级**:高

### AC-2:FR-2 步骤 6 末尾"复现动作触发" 子节生效

- **对应需求**:FR-2
- **验证方式**:静态校验
- **步骤**:
 1. 读 `code-fix/SKILL.md` 步骤 6 末尾
 2. 检查是否有"### X.复现产物登记" 子节,含触发条件 3 条 + 复现算法 9 步
- **预期结果**:子节存在,触发条件明确
- **优先级**:高

### AC-3:FR-3 3 类产物(日志 / 截图 / 交互数据)收集

- **对应需求**:FR-3
- **验证方式**:端到端测试
- **步骤**:
 1. 准备 1 个 Node.js 测试工程(端口 3000 的 web 服务,故意 500 错误)
 2. 调 `code-fix "用户报告:登录 API 返回 500"` + 复现步骤
 3. 检查 `fix/<BUG-NNN>/reproduce/` 目录是否含 `run.log` / `interaction-1.json` / `RESULT-meta.json`
- **预期结果**:3 个文件存在 + 各自内容符合 FR-3.1~3.3 规范
- **优先级**:高

### AC-4:FR-4 产物子目录设计

- **对应需求**:FR-4
- **验证方式**:静态校验
- **步骤**:
 1. 读 `code-fix/SKILL.md` 步骤 6 末尾子节
 2. 检查产物路径是否为 `fix/<BUG-NNN>/reproduce/`
 3. 检查 `RESULT-meta.json` 结构是否含 5 字段(bugNum / startCommand / startedAt / endedAt / exitCode / reproduceResult / artifacts / failureReason)
- **预期结果**:路径正确 + meta 字段完整
- **优先级**:中

### AC-5:FR-5 `bug.md` 新增"## 复现产物登记" 区段

- **对应需求**:FR-5
- **验证方式**:静态校验
- **步骤**:
 1. 读 `code-fix/templates/bug.md`
 2. 检查是否在"## 缺陷描述" 段后,"---" 分隔符 + "## 根因分析" 段前,新增"## 复现产物登记" 区段
 3. 检查区段结构含"### 产物清单" / "### 实际行为" / "### 复现结论" 3 个子项
- **预期结果**:区段存在 + 子项完整
- **优先级**:高

### AC-6:FR-6 文档头新增 2 字段

- **对应需求**:FR-6
- **验证方式**:静态校验
- **步骤**:
 1. 读 `bug.md` 文档头"## 文档头" 表
 2. 检查是否新增"复现方式" / "产物路径" 2 行
- **预期结果**:2 字段存在
- **优先级**:中

### AC-7:NFR-3 零规范变更

- **对应需求**:NFR-3
- **验证方式**:静态校验
- **步骤**:
 1. 读 `code-fix/SKILL.md` frontmatter L1-3,期望字节级未变
 2. 读既有"## 工作流程" 小节步骤 1~5,期望字节级未变(只追加步骤 0 / 6 末尾子节)
 3. 读"## 不要做的事" 小节,期望字节级未变
- **预期结果**:零破坏
- **优先级**:高

### AC-8:NFR-4 失败降级

- **对应需求**:NFR-4
- **验证方式**:端到端测试
- **步骤**:
 1. 准备 1 个故意启动失败的工程(Makefile target 不存在)
 2. 调 `code-fix "用户报告:XXX"` + 复现步骤
 3. 检查屏显是否含 `⚠ 启动失败`
 4. 检查 `fix/<BUG-NNN>/RESULT.md` 文档头"当前状态" 字段是否仍为 `待处理`
- **预期结果**:屏显警告 + 状态仍为 `待处理` + 继续登记
- **优先级**:高

### AC-9:NFR-5 历史 BUG 不追加

- **对应需求**:NFR-5
- **验证方式**:静态校验
- **步骤**:
 1. 检查 `BUG-00001 / 02 / 03 / 04 / 05` 的 `fix/<BUG-NNN>/RESULT.md`
 2. 验证**不**含"## 复现产物登记" 段
 3. 验证**不**含"复现方式" / "产物路径" 字段
- **预期结果**:历史 BUG 字节级保留
- **优先级**:中

### AC-10:NFR-7 看板不新增列

- **对应需求**:NFR-7
- **验证方式**:静态校验
- **步骤**:
 1. 读 `code-fix/templates/fix-registry.md` 总览表
 2. 检查 7 列(缺陷编号 / 严重度 / 标题 / 状态 / 报告时间 / 修复人 / 关联需求)未变
 3. 读 `version-RESULT.md` 看板"缺陷清单" 区段
 4. 检查列**不**含"复现方式" / "产物路径"
- **预期结果**:总览 / 看板列未变
- **优先级**:中

### AC-11:NFR-8 不引入开发痕迹

- **对应需求**:NFR-8
- **验证方式**:静态校验
- **步骤**:
 1. 读 `code-fix/SKILL.md` 全文
 2. `Grep` 关键词:"本需求 REQ-00040" / "沿用原 code-fix" / "Q-X 锁定"
 3. 期望**不**命中
- **预期结果**:零开发痕迹
- **优先级**:高

### AC-12:与 REQ-00037 协同(状态推进路径不破坏)

- **对应需求**:NFR-2
- **验证方式**:端到端测试
- **步骤**:
 1. 调 `code-fix "测试"` 登记新 BUG
 2. 检查文档头"当前状态" 字段 = `待处理`(沿用 REQ-00037)
 3. 调 `code-plan BUG-NNN` → 检查状态 = `待开发`(沿用 REQ-00037 FR-2)
 4. 调 `code-it TASK-BUG-NNN-00001` → 检查状态 = `开发中` / `待审查`(沿用 REQ-00037 FR-3/4)
- **预期结果**:状态推进路径字节级保留
- **优先级**:高

## 11. 关联需求

| 关联需求编码 | 关联点 | 影响 |
| --- | --- | --- |
| REQ-00037 | 优化 `code-fix` 技能及整个缺陷修复流程的状态推进 | **不**与本需求冲突;本需求在 REQ-00037 之上叠加"复现证据" 机制;**不**改 REQ-00037 已确定的初始态(`待处理`) |
| REQ-00027 | `code-fix` 改为纯登记型 + 下游接力 | 本需求**不**改纯登记型边界;复现动作 = 登记时的"证据附件",**不**触发 `code-plan` / `code-it` / `code-check` 任何状态推进 |
| REQ-00036 | 清理 SKILL.md + templates/ 中的开发痕迹 | 本需求**不**在 `code-fix/SKILL.md` / `bug.md` 中写"本需求 REQ-00040 新增" 等开发痕迹(沿用 `skill-conventions §规则 2`) |
| REQ-00033 | `code-require` 不做技术选型 | **不**涉及(本需求是 code-fix,非 code-require);启动命令探测是**操作步骤**而非"技术选型",**不**触发 §615 硬约束 |
| REQ-00022 | `code-review` → `code-check` 重命名 | 本需求**不**涉及 code-check |
| BUG-00001~05 | 既有 5 个缺陷 | **不**追加"## 复现产物登记" 段(沿用 NFR-5,字节级保留) |

## 12. 待澄清 / 未决项

- **Q-1**:截图工具选型(playwright vs puppeteer vs headless-chrome)具体偏好 — 默认首选 playwright(NFR-3 强约束**不**触发 `AskUserQuestion`,本轮**不**做用户选型,后续若 playwright 不可用再降级)
- **Q-2**:`reproduce/` 子目录命名是否需要带时间戳(避免同名 BUG 复跑覆盖) — 默认**不**带时间戳,沿用固定路径(便于 `code-plan` / `code-check` 引用);同名 BUG 沿用 E-10 降级方案
- **Q-3**:复现动作是否需要"沙箱环境"(避免污染本地数据库 / 文件系统) — 本轮**不**实现沙箱;沿用"在 cwd 下直接运行" 的简单方案;若用户后续需要,留作 follow-up
- **Q-4**:`reproduce/` 子目录是否需要 `.gitignore` 规则(产物是临时证据,不需进 git) — 留作 follow-up;默认**不**改 `.gitignore`

## 13. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-25 | v1 | 初始创建 | 完成首次需求澄清;6 FR / 10 NFR / 12 AC;1 轮 4 问 `AskUserQuestion`(启动判定 / 产物位置 / 状态触发 / 失败降级) | 用户 |
