# 详细设计 — REQ-00040 · 优化 /code-fix 技能:登记缺陷时启动程序复现并登记证据

## 设计目标

> 沿用 `design/REQ-00040/RESULT.md` "## 设计目标" 小节(--balanced)

- **整体设计目标**:`--balanced`
- **维度优先级**:
 - 功能性:高
 - 扩展性:低
 - 健壮性:中
 - 可维护性:中
 - 封装性:不适用(Markdown 自然语言)
 - 可复用性:不适用(无共享库)
 - 可读性:高(伪代码详细注释,便于 `code-it` 实施)

- 需求编码:REQ-00040
- 所属版本:V0.0.3
- 文档创建时间:2026-06-25
- 最近更新:2026-06-25
- 设计状态:草稿(待 code-it 推进)
- 上游:
 - 需求:`./assistants/V0.0.3/require/REQ-00040/RESULT.md`(v1,6 FR / 10 NFR / 12 AC)
 - 概要设计:`./assistants/V0.0.3/design/REQ-00040/RESULT.md`(v1,10 决策 / 8 不变量)
- 遵循规范:`./assistants/rules/` 下 13 个文件(全沿用,无新增;`skill-conventions §规则 1-2` 字节级保留)
- 涉及技能:`code-fix`(主改造)+ `code-fix/templates/bug.md`(主改造)+ `code-fix/templates/assistants-layout.md`(辅助同步)
- 关键决策数:18 项(10 沿用 + 8 新增 PD-1~PD-8);不变量:8 条(INV-1~INV-8)
- 任务数:6 个(PLAN.md 任务总览)

## 1. 概述

### 1.1 本详细设计的目标

把概设"系统长什么样" 落地为"可直接编码的细节":

- **算法**:每个伪代码函数给出完整可编码的逻辑(沿用概设 D-1~D-10 + 详设 PD-1~PD-8)
- **数据结构**:`fix/<BUG-NNN>/RESULT.md` 文档头新增 2 字段;`reproduce/RESULT-meta.json` 8 字段;`reproduce/interaction-N.json` 8 字段
- **接口**:5 个内部伪代码函数完整规格(签名 / 入参 / 出参 / 错误码 / 示例)
- **测试**:12 条 AC 全部降级为静态校验(本仓库 0 测试框架)

### 1.2 与概要设计的关系

| 维度 | 概设 | 详设 |
| --- | --- | --- |
| 模块拆分 | 5 模块(主改造 2 + 辅助 1 + 运行时 1 + 看板 1) | 5 模块细化到关键类/函数/调用顺序 |
| 接口概要 | 5 个内部伪代码接口 | 5 个完整规格(签名 / 入参 / 出参 / 错误码 / 示例) |
| 数据结构 | 3 数据结构(文档头字段 / 产物子目录结构 / meta 字段) | 3 数据结构细化到字段类型 + 约束 |
| 异常路径 | 11 边界 | 11 边界 + 1 复合边界 + 每个边界的处理策略 + 监控指标 |
| 测试 | 0(本仓库 0 框架) | 12 条 AC 全部降级为静态校验(完整清单) |

## 2. 上游引用

| 来源 | 路径 | 提取内容 |
| --- | --- | --- |
| 缺陷详情(无,本需求不是修复) | N/A | N/A |
| 需求 | `./assistants/V0.0.3/require/REQ-00040/RESULT.md` v1 | 6 FR / 10 NFR / 12 AC |
| 概要设计 | `./assistants/V0.0.3/design/REQ-00040/RESULT.md` v1 | 10 决策 / 8 不变量 / 4 模块 / 5 接口 / 3 数据结构 |
| 项目级规范 | `./assistants/rules/` × 13 | 强约束:`skill-conventions §规则 1-2` / `dashboard-conventions §规则 1`;其余 11 份对本详设**不**产生约束(0 触发) |
| 上游历史(RE界-00037) | 沿用 | 状态推进路径(`待处理 → 待开发 → 开发中 → 待审查 → 已完成`)字节级保留 |

## 3. 规范遵循

13 份项目级规范全部沿用,**0 违反**强约束,**0 触发** `dashboard-conventions §规则 1` 三同步,**0 新增** `code-rule` 介入。

详细自检见 `rule-compliance.md` §6(13 份规范自检结论表 + 0 冲突 + 0 偏离)。

## 4. 模块详细化

详见 `module-details.md`。简表:

| 模块 | 路径 | 状态 | 职责 |
| --- | --- | --- | --- |
| 1. 步骤 0 末尾子节 | `code-fix/SKILL.md` 步骤 0 末尾 | 修改既有 | `detectStartability(cwd)` 7 步探测算法 |
| 2. 步骤 6 末尾子节 | `code-fix/SKILL.md` 步骤 6 末尾 | 修改既有 | `reproduceBug()` 9 步算法 + 触发条件 3 条 |
| 3. 步骤采集 | 步骤 6 末尾子节内联 | 新增(伪代码) | `executeStep(step, reprodDir)` 3 类产物采集 |
| 4. `bug.md` 模板 | `code-fix/templates/bug.md` | 修改既有 | 文档头 2 字段 + 新区段 |
| 5. `assistants-layout.md` | `code-fix/templates/assistants-layout.md` | 修改既有 | 追加 `reproduce/` 子目录行 |
| 6. 版本看板 | `assistants/V0.0.3/RESULT.md` | 修改既有 | 4 区段同步 |

## 5. 算法与逻辑

### 5.1 `detectStartability(cwd)` 探测算法(7 步)

```typescript
function detectStartability(cwd: string): {
  canStart: boolean;
  startCommand: string | null;
} {
  let canStart = false;
  let startCommand: string | null = null;

  // 优先级 1:Node.js
  if (existsSync(`${cwd}/package.json`)) {
    const pkg = readJson(`${cwd}/package.json`);
    if (pkg.scripts?.start) {
      canStart = true;
      startCommand = existsSync(`${cwd}/pnpm-lock.yaml`) ? "pnpm start"
                   : existsSync(`${cwd}/yarn.lock`) ? "yarn start"
                   : "npm start";
    }
  }
  // 优先级 2:Python
  else if (existsSync(`${cwd}/pyproject.toml`) || existsSync(`${cwd}/setup.py`) || existsSync(`${cwd}/requirements.txt`)) {
    canStart = true;
    startCommand = "python -m <module>";  // 用户可在 step 5 调整
  }
  // 优先级 3-8:Makefile / Docker / Rust / Go / Java(同模式)
  // ...

  return { canStart, startCommand };
}
```

**复杂度**:O(1)~O(8) 个文件存在性检查,总耗时 < 500ms。
**错误处理**:文件不存在 / JSON 解析失败 → 跳过该优先级,继续下一优先级(不报错)。

### 5.2 `reproduceBug()` 复现算法(9 步)

```typescript
function reproduceBug(
  bugNum: string,
  startCommand: string,
  reproSteps: Step[],
  timeout: number = 60
): Meta {
  const reproduceDir = `./assistants/${version}/fix/${bugNum}/reproduce/`;
  mkdirSync(reproduceDir, { recursive: true });
  const startedAt = formatTimestamp(new Date());

  // 1. 启动子进程
  const childProcess = spawn(startCommand, {
    cwd,
    stdio: ['ignore', openSync(`${reproduceDir}/run.stdout.log`, 'w'), openSync(`${reproduceDir}/run.stderr.log`, 'w')],
    detached: false,
  });

  // 2. 等待启动
  await sleep(5000);

  let exitCode = 0;
  let reproduceResult: "已复现" | "未复现" | "复现失败" = "已复现";
  let failureReason: string | null = null;

  // 3. 执行复现步骤(超时控制)
  try {
    await Promise.race([
      Promise.all(reproSteps.map(step => executeStep(step, reproduceDir))),
      sleep(timeout * 1000).then(() => { throw new TimeoutError(); }),
    ]);
  } catch (e) {
    if (e instanceof TimeoutError) {
      exitCode = 124;
      reproduceResult = "复现失败(超时)";
      failureReason = `Timeout after ${timeout}s`;
    } else {
      exitCode = 1;
      reproduceResult = "复现失败";
      failureReason = e.message;
    }
  }

  // 4. 终止子进程
  if (childProcess.exitCode === null) {
    childProcess.kill('SIGTERM');
    await sleep(5000);
    if (childProcess.exitCode === null) {
      childProcess.kill('SIGKILL');
    }
  }

  const endedAt = formatTimestamp(new Date());

  // 5. 合并日志(带时间戳)
  mergeLogsWithTimestamp(`${reproduceDir}/run.stdout.log`, `${reproduceDir}/run.stderr.log`, `${reproduceDir}/run.log`);

  // 6. 写元信息
  const meta: Meta = { bugNum, startCommand, startedAt, endedAt, exitCode, reproduceResult, artifacts: listArtifacts(reproduceDir), failureReason };
  writeFileSync(`${reproduceDir}/RESULT-meta.json`, JSON.stringify(meta));  // 单行 JSON,沿用 PD-5

  // 7. 写"## 复现产物登记" 区段到 fix/<BUG-NNN>/RESULT.md
  writeReproSection(fixResultPath, meta, reproduceDir);

  return meta;
}
```

**复杂度**:启动 5s + 步骤执行 < 55s = 总 < 60s(沿用 NFR-1)。
**错误处理**:所有异常**不**抛,均通过 `reproduceResult` + `failureReason` 字段记录(沿用 NFR-4 不阻断)。

### 5.3 `executeStep()` 步骤采集算法(3 类分发)

详见 `module-details.md §模块 3`;**核心**:
- `cli` 类型:执行命令(产物 = stdout/stderr 已通过子进程重定向)
- `http` 类型:curl 调 API + 写 `interaction-N.json`(沿用 PD-7)
- `browser` 类型:链式降级 playwright → puppeteer → headless-chrome(沿用 PD-6)

### 5.4 状态机(沿用 REQ-00037)

```
[code-fix 登记] 待处理
   ↓ code-fix 复跑(可选)
 报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞(前 5 段)
   ↓ code-plan 完成
 待开发
   ↓ code-it 第 1 任务开始
 开发中
   ↓ code-it 全部任务完成
 待审查
   ↓ code-check 完成
 已完成
```

**关键不变量(INV-6)**:`code-fix` 初始态 = `待处理`,状态推进路径字节级保留;**本需求的复现动作不触发任何状态推进**(NFR-2)。

## 6. 数据结构完整变更

### 6.1 `fix/<BUG-NNN>/RESULT.md` 文档头新增 2 字段

| 字段名 | 类型 | 值域 | 约束 | 默认值 | 来源 |
| --- | --- | --- | --- | --- | --- |
| 复现方式 | enum | `程序复现` / `文本复现` / `未复现` | 必填,沿用 FR-6 | `文本复现` | FR-6(本需求新增) |
| 产物路径 | string | `reproduce/` 或 空 | 必填,有产物时填 `reproduce/` | 空 | FR-6(本需求新增) |

**位置**:`bug.md` line 22 后(line 24 `### 状态枚举` 前)。
**不触发** `dashboard-conventions §规则 1`(字段在 `fix/<BUG-NNN>/RESULT.md` 内部,**不**进 `fix/RESULT.md` 总览 / 看板)。

### 6.2 `reproduce/RESULT-meta.json` 元信息(8 字段)

```json
{
  "bugNum": "string (BUG-NNNNN, 5位纯数字,encoding-conventions §规则 1)",
  "startCommand": "string (启动命令字面,可为 null)",
  "startedAt": "string (YYYY-MM-DD HH:mm:ss,24h 制)",
  "endedAt": "string (YYYY-MM-DD HH:mm:ss,24h 制)",
  "exitCode": "number (0=成功 / 1=异常 / 124=超时)",
  "reproduceResult": "enum (已复现 / 未复现 / 复现失败)",
  "artifacts": "Artifact[] (产物清单,每项含 type / path / size)",
  "failureReason": "string | null (失败原因,成功时 null)"
}
```

**Artifact** 子结构:
```json
{ "type": "log | screenshot | interaction", "path": "相对 reproduce/ 路径", "size": "数字(字节)" }
```

**存储选型**:`reproduce/RESULT-meta.json`(本仓库**不**用数据库;JSON 文件足够)。
**单行 JSON**(沿用 PD-5):减小文件大小,便于 `code-plan` / `code-check` 读。

### 6.3 `reproduce/interaction-N.json` 交互数据(8 字段)

```json
{
  "step": "number (步骤序号,从 1 起)",
  "method": "string (HTTP 方法)",
  "url": "string (URL)",
  "headers": "object (HTTP headers)",
  "requestBody": "any (请求体)",
  "responseStatus": "number | null (HTTP 状态码;失败时 null)",
  "responseBody": "any (响应体;失败时 null)",
  "responseHeaders": "object (HTTP response headers)"
}
```

**命名**:`interaction-{N}.{json|txt}`(N 从 1 起;type=http 时用 .json,type=cli 时可能用 .txt)。
**触发条件**:`step.type == "http"`(沿用 PD-7);N=0 时跳过。

### 6.4 既有数据结构(不修改)

- `code-fix` 状态机(15 字面共存,5 新 + 10 老) — 字节级保留
- `bug.md` 既有 9 区段 — 字节级保留(INV-4)
- `fix/RESULT.md` 总览表 7 列 — 字节级保留
- 看板"缺陷清单" 区段 8 列 — 字节级保留

### 6.5 不触发 `data-changes.md` 文档生成

本设计**不**涉及数据库 / 缓存 / 状态字段变更,纯 Markdown 文档结构(沿用 `code-plan` 过程文档判定:`data-changes.md` "纯 UI / 配置 / 文档类 → 不生成")。

## 7. 接口细节

5 个内部伪代码函数,完整规格见 `interface-specs.md`:

| 接口 | 签名 | 形式 | 状态 |
| --- | --- | --- | --- |
| 1. `detectStartability` | `(cwd: string) => {canStart, startCommand}` | 函数(伪代码) | 新增 |
| 2. `reproduceBug` | `(bugNum, startCommand, reproSteps, timeout=60) => Meta` | 函数(伪代码) | 新增 |
| 3. `executeStep` | `(step: Step, reproduceDir: string) => void` | 函数(伪代码) | 新增 |
| 4. `mergeLogsWithTimestamp` | `(stdout, stderr, outputPath) => void` | 函数(伪代码) | 新增 |
| 5. `terminate` | `(childProcess, signal="SIGTERM", waitTime=5, fallback="SIGKILL") => void` | 函数(伪代码) | 新增 |

**0 项外部接口变更**(本设计**不**修改任何 `code-*` 技能的对外接口)。

## 8. 异常处理

11 边界 + 1 复合边界,详见 `risk-analysis.md §1`。**关键原则**:**任何失败都不阻断 `code-fix` 主流程**(NFR-4)。

## 9. 安全要求

本需求**不**涉及鉴权 / 加密 / 审计(纯本地命令执行)。

- **输入校验**:用户输入的"复现步骤" 在 `code-fix` 步骤 1 / 5 阶段已校验;本子节**不**重复校验
- **敏感数据处理**:复现产物**不**视为"敏感数据"(本仓库是开发工具);放 `fix/<BUG-NNN>/reproduce/` 子目录,**不**自动清理
- **审计日志**:每次复现动作在 `fix/<BUG-NNN>/RESULT.md` 文档头"修复日志" 段追加 1 条;`RESULT-meta.json` 记录完整运行时间 / 退出码

## 10. 状态机/流程

**严守 REQ-00037 状态推进路径**(INV-6):本需求的复现动作**不**触发任何状态推进(沿用 NFR-2)。

详见 §5.4 状态机图。

## 11. 性能与资源

| 指标 | 限制 | 触发降级 |
| --- | --- | --- |
| 探测耗时 | < 500ms | N/A(快速降级) |
| 子进程总耗时 | < 60s(超时) | E-3(终止进程) |
| 日志大小 | < 10MB(> 截断) | E-5(截断到 1MB) |
| 子进程数 | 1(本需求不并发) | N/A |

详见 `risk-analysis.md §3`。

## 12. 测试要点

12 条 AC 全部降级为静态校验(本仓库 0 测试框架 + 0 可启动项目,沿用 NFR-7 + 仓库"无源代码"约定)。

| AC | 验证方式 | 关键步骤 |
| --- | --- | --- |
| AC-1 | 静态校验 | `Read code-fix/SKILL.md` 步骤 0 末尾,检查"### X.项目可启动性探测" 子节 |
| AC-2 | 静态校验 | `Read code-fix/SKILL.md` 步骤 6 末尾,检查"### X.复现产物登记" 子节 |
| AC-3 | 端到端降级为静态 | 检查"## 复现产物登记" 模板的子项完整性 + `RESULT-meta.json` 结构 |
| AC-4 | 静态校验 | 验证产物路径 + meta 字段 |
| AC-5 | 静态校验 | `Read bug.md` 检查新区段结构 |
| AC-6 | 静态校验 | `Read bug.md` 文档头表新增 2 行 |
| AC-7 | 静态校验 | `git diff` 校验 L1-3 + 既有"## 工作流程" + "## 不要做的事" 字节级未变 |
| AC-8 | 端到端降级为静态 | 检查失败降级逻辑字面(`⚠` 屏显 + `复现方式 = 文本复现` 字面) |
| AC-9 | 静态校验 | 验证历史 5 个 BUG RESULT.md **不**含"## 复现产物登记" 段 |
| AC-10 | 静态校验 | 验证 7 列表格 + 看板列未变 |
| AC-11 | 静态校验 | `Grep` 关键词("本需求 REQ-00040" / "沿用原 code-fix" / "Q-X 锁定"),期望不命中 |
| AC-12 | 端到端降级为静态 | 检查 `code-fix` 步骤 4 状态推进表字面(沿用 REQ-00037) |

详见 `risk-analysis.md §5`。

## 13. 关联

| 关联项 | 关联方式 |
| --- | --- |
| `code-fix/SKILL.md §工作流程` | 步骤 0 / 步骤 6 末尾追加 2 子节(本详设主改造) |
| `code-fix/templates/bug.md` | 新增"## 复现产物登记" 区段 + 文档头 2 字段(本详设主改造) |
| `code-fix/templates/assistants-layout.md` | 追加 `reproduce/` 子目录行(本详设辅助同步) |
| `CLAUDE.md §版本感知工作空间约定` | 上游权威源(定义 `code-*` 技能 → 工作空间目录映射) |
| `V0.0.3/require/REQ-00040/RESULT.md` v1 | 需求上游(本详设的输入) |
| `V0.0.3/design/REQ-00040/RESULT.md` v1 | 概设上游(本详设的输入) |
| `V0.0.3/fix/RESULT.md` | 缺陷总览(本需求**不**新增列) |
| `V0.0.3/RESULT.md` §任务清单 | 6 任务首次登记(由 `code-plan` 步骤 16A 同步) |
| `V0.0.3/RESULT.md` §里程碑 | M1-REQ-00040 首次登记 |
| `V0.0.3/fix/BUG-00001~05/RESULT.md` | 历史 5 个 BUG,字节级保留(NFR-5) |
| `skill-conventions §规则 1-2` | 强约束:frontmatter 保留 + 不引入开发痕迹 |
| `dashboard-conventions §规则 1` | 强约束:本需求**0 触发**(产物放子目录) |
| `encoding-conventions §规则 1-4` | 沿用 BUG-NNNNN 5 位纯数字 |
| REQ-00037 | 状态推进路径字节级保留(INV-6 / NFR-2) |

## 14. 待澄清 / 未决项

(已从上游 `require/REQ-00040/RESULT.md §12` 沿用,本详设不增加新澄清)

- **Q-1**:截图工具选型具体偏好 — 默认首选 playwright,降级链见 PD-6
- **Q-2**:`reproduce/` 子目录命名是否带时间戳 — 默认**不**带,沿用固定路径
- **Q-3**:复现动作是否需要沙箱环境 — 本轮**不**实现,留作 follow-up
- **Q-4**:`reproduce/` 子目录是否需要 `.gitignore` — 留作 follow-up,默认**不**改 `.gitignore`

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-25 | v1 | 初始创建 | 完成首次详细设计与编码计划;6 任务(全部 `触发/来源=详细设计`);18 项决策(10 沿用 + 8 新增 PD-1~PD-8);8 条不变量(INV-1~INV-8);5 份过程文档生成(materials-index / design-notes / module-details / interface-specs / risk-analysis + rule-compliance + process-doc-decisions 共 6 份);2 份不生成(data-changes 0 / clarifications 0);0 关联设计;0 规范冲突;0 新增三方依赖;12 条 AC 全部降级为静态校验 | 用户 |
