# 概要设计 — REQ-00040 · 优化 /code-fix 技能:登记缺陷时启动程序复现并登记证据

- 需求编码:REQ-00040
- 所属版本:V0.0.3
- 文档创建时间:2026-06-25
- 最近更新:2026-06-25
- 设计状态:草稿(待 code-plan 推进)
- 上游:`./assistants/V0.0.3/require/REQ-00040/RESULT.md`(v1,6 FR / 10 NFR / 12 AC)
- 遵循规范:`./assistants/rules/` 下 13 个文件(全沿用,无新增;`skill-conventions §规则 1-2` 字节级保留)
- 涉及技能:`code-fix`(主改造)+ `code-fix/templates/bug.md`(主改造)+ `code-fix/templates/assistants-layout.md`(辅助同步)
- 设计目标:`--balanced`(功能性=高,扩展性=低,健壮性=中,可维护性=中,封装性=不适用,可复用性=不适用,可读性=高)
- 关键决策数:10 项;不变量:8 条

## 1. 设计概述

本设计回答"在 `code-fix` 登记缺陷时,如何自动启动程序并收集证据"。

**核心架构**:在 `code-fix` 步骤 0 末尾追加"项目可启动性探测" 子节(自动判定 `canStart`),在步骤 6 末尾追加"复现产物登记" 子节(触发复现动作 + 收集 3 类产物)。产物放 `fix/<BUG-NNN>/reproduce/` 子目录,通过 `bug.md` 模板新增"## 复现产物登记" 区段登记。沿用 REQ-00037 状态推进路径,严守"code-fix 不阻断" 失败降级。

**与既有约束的协同**:
- **NFR-2 与 REQ-00037 协同**:`code-fix` 初始态 = `待处理`,状态推进路径字节级保留
- **NFR-3 零规范变更**:frontmatter / 既有"## 工作流程" / "## 不要做的事" 字节级保留;**不**触发 `dashboard-conventions §规则 1`(产物放子目录,**不**新增看板列)
- **NFR-8 不引入开发痕迹**:**不**在 `code-fix/SKILL.md` / `bug.md` 模板中写"本需求 REQ-00040 新增" 等字面
- **NFR-9 不修改项目源码**:复现动作只读运行,触发命令均不修改任何项目文件

## 2. 架构图

### 2.1 组件图

```
┌────────────────────────────────────────────────────────────────┐
│ code-fix 技能主流程(沿用 V0.0.3 REQ-00027 / REQ-00037)         │
│                                                                 │
│ 步骤 0 ──┐                                                      │
│ (版本检测)│                                                       │
│          ├─ 末尾追加:项目可启动性探测子节(本需求 FR-1)          │
│          │   检测 package.json / pyproject.toml / Makefile ...  │
│          │   输出:canStart: bool + startCommand: string         │
│          ↓                                                       │
│ 步骤 1 (收集缺陷描述 + 复现步骤)                                  │
│ 步骤 2 (创建 fix/<BUG-NNN>/ 目录)                                 │
│ 步骤 3 (读既有材料,仅更新分支)                                    │
│ 步骤 4 (询问本轮状态推进)                                         │
│ 步骤 5 (补充本轮信息)                                             │
│ 步骤 6 ──┐                                                      │
│ (写 RESULT.md)│                                                    │
│          ├─ 主体:写 fix/<BUG-NNN>/RESULT.md (沿用)              │
│          └─ 末尾追加:复现产物登记子节(本需求 FR-2)               │
│              触发条件:canStart=true ∧ 新建分支 ∧ 有复现步骤       │
│              执行:reproduceBug() → reproduce/ 4 类产物           │
│                   + 写 ## 复现产物登记 区段到 RESULT.md          │
│              失败降级:屏显 ⚠ + 继续登记(不阻断)                  │
│          ↓                                                       │
│ 步骤 7 (写 fix/RESULT.md 总览,沿用)                              │
│ 步骤 8 (同步版本看板,沿用)                                       │
│ 步骤 9 (引导下一步,沿用)                                         │
│ 步骤 10 (汇报,沿用)                                              │
└────────────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────────────┐
│ fix/<BUG-NNN>/ 子目录(本需求新增 reproduce/ 子目录)            │
│                                                                 │
│ fix/<BUG-NNN>/                                                  │
│ ├── RESULT.md                  ← 文档头新增 2 字段(FR-6)       │
│ │    复现方式 / 产物路径                                        │
│ ├── reproduce/                 ← 本需求新增子目录               │
│ │   ├── run.log                ← FR-3.1 日志(进程 stdout/stderr) │
│ │   ├── screenshot-1.png       ← FR-3.2 截图(UI 缺陷,可选)     │
│ │   ├── interaction-1.json     ← FR-3.3 交互数据(API 缺陷,可选)│
│ │   └── RESULT-meta.json       ← FR-4 元信息(运行时间/退出码)  │
│ ├── investigation.md           (由 code-it 写入,本技能只读)    │
│ ├── fix-plan.md                (由 code-plan 写入)              │
│ ├── fix-work-log.md            (由 code-it 写入)                │
│ ├── fix-compile-and-run.md     (由 code-it 写入)                │
│ ├── fix-test-results.md        (由 code-it 写入)                │
│ └── deviations.md              (由 code-it 写入)                │
└────────────────────────────────────────────────────────────────┘
```

### 2.2 关键数据流

```
[用户报告] "登录 API 返回 500"
     ↓
[code-fix 步骤 1] 收集:复现步骤 = "POST /api/login 传错密码"
     ↓
[code-fix 步骤 0 末尾] detectStartability()
     ↓ 命中 package.json + scripts.start
     → canStart = true, startCommand = "npm start"
     ↓
[code-fix 步骤 6 主体] 写 fix/BUG-00006/RESULT.md
     ↓
[code-fix 步骤 6 末尾] reproduceBug(BUG-00006, "npm start", steps)
     ↓ 触发复现
     → mkdir -p fix/BUG-00006/reproduce/
     → 启动子进程:npm start > reproduce/run.stdout.log 2> reproduce/run.stderr.log
     → 等 5s(程序启动)
     → 执行步骤 1:curl -X POST http://localhost:3000/api/login -d '{"username":"test","password":"wrong"}'
        → 写入 reproduce/interaction-1.json (含 status 500)
     → 终止进程(graceful shutdown)
     → 合并 stdout + stderr → reproduce/run.log (加时间戳)
     → 写 reproduce/RESULT-meta.json (含 startedAt / endedAt / exitCode / reproduceResult)
     ↓
[code-fix 步骤 6 末尾] 写 fix/BUG-00006/RESULT.md 的"## 复现产物登记" 区段
     ↓ 含产物清单(日志/交互数据) + 实际行为(500 错误堆栈) + 复现结论(已复现)
     ↓
[code-fix 步骤 7/8/9/10] 沿用既有流程(总览 / 看板 / 引导)
     ↓
[code-plan BUG-00006] 读 reproduce/RESULT-meta.json 看到 500 + 读 run.log 看到堆栈
     ↓ 直接定位根因(无需重新跑)
```

## 3. 关键决策与依据

### 3.1 关键决策

| 决策 ID | 决策 | 依据 |
| --- | --- | --- |
| **D-1** | 启动能力**自动探测**,不弹 `AskUserQuestion` 不新增 CLI 参数 | NFR-3(零规范变更 + 不触发 `AskUserQuestion`) |
| **D-2** | 产物放 `fix/<BUG-NNN>/reproduce/` 子目录,**不** inline 进 RESULT.md | NFR-7(不污染总览 / 看板);子目录便于引用 |
| **D-3** | 复现动作**不**触发状态推进(初始态 = `待处理`,沿用 REQ-00037) | NFR-2(与 REQ-00037 协同) |
| **D-4** | 失败降级链:**任何失败都不阻断** `code-fix` 主流程 | NFR-4(失败降级不阻断);code-fix 是纯登记型 |
| **D-5** | 截图工具链式降级:playwright → puppeteer → headless-chrome | FR-3.2(失败降级);沿用 V0.0.1 工具链惯例 |
| **D-6** | `bug.md` 新区段插入位置:"## 缺陷描述" 段后 + "## 根因分析" 段前 | 沿用"用户原始 → 证据附件 → 分析" 阅读顺序 |
| **D-7** | 文档头新增 2 字段(复现方式 / 产物路径),便于字段筛选 | NFR-10(可追溯);便于 `code-plan` 引用 |
| **D-8** | 同步更新 `assistants-layout.md`(在 `fix/<BUG-NNN>/` 子目录列表追加 `reproduce/`) | 文档与实际一致(避免"目录说明"与实际不符) |
| **D-9** | **不**新建 `code-fix/lib/` 共享库(探测逻辑简单,SKILL.md 内联伪代码) | 沿用 `code-fix` 既有简洁结构;新建会破坏结构 |
| **D-10** | `reproduce/` 子目录**不**加 `.gitignore`(沿用既有 fix/RESULT.md 提交模式) | NFR-9(不修改项目配置);用户后续可手动调整 |

### 3.2 不变量(INV)

- **INV-1**:`code-fix/SKILL.md` frontmatter L1-3 字节级保留(NFR-3)
- **INV-2**:`code-fix/SKILL.md` 既有"## 工作流程" 小节步骤 0 主体 / 步骤 1~10 主体字节级保留;**只**在步骤 0 末尾 + 步骤 6 末尾追加子节(NFR-3)
- **INV-3**:`code-fix/SKILL.md` "## 不要做的事" 小节字节级保留(NFR-3)
- **INV-4**:`bug.md` 既有 9 区段(文档头/缺陷描述/根因分析/修复方案/修复实施/验证结果/修复日志/关联项/变更记录)字节级保留;**只**在文档头表追加 2 行 + 在"## 缺陷描述" 段后插入"## 复现产物登记" 区段(NFR-3)
- **INV-5**:历史 5 个 BUG(BUG-00001~05)的 `fix/<BUG-NNN>/RESULT.md` 字节级保留;新区段仅对未来新登记 BUG 生成(NFR-5)
- **INV-6**:`code-fix` 初始态 = `待处理`,状态推进路径 = `待处理 → 待开发 → 开发中 → 待审查 → 已完成`(沿用 REQ-00037,NFR-2)
- **INV-7**:`fix/RESULT.md` 总览表 7 列(缺陷编号/严重度/标题/状态/报告时间/修复人/关联需求)字节级保留;版本看板"缺陷清单" 区段 8 列字节级保留(NFR-7)
- **INV-8**:`code-fix/SKILL.md` / `bug.md` 模板**不**含"本需求 REQ-00040 新增" / "沿用原 code-fix" / "Q-X 锁定" 等 6 类开发痕迹字面(NFR-8,沿用 `skill-conventions §规则 2`)

## 4. 模块拆分

详见 `module-breakdown.md`。简表:

| 模块 | 路径 | 状态 | 职责 |
| --- | --- | --- | --- |
| `code-fix` 技能入口 | `plugins/code-skills/skills/code-fix/SKILL.md` | 修改既有 | 步骤 0 / 步骤 6 末尾追加 2 子节 |
| `bug.md` 模板 | `plugins/code-skills/skills/code-fix/templates/bug.md` | 修改既有 | 新增"## 复现产物登记" 区段 + 文档头 2 字段 |
| `assistants-layout.md` 模板 | `plugins/code-skills/skills/code-fix/templates/assistants-layout.md` | 修改既有 | 追加 `reproduce/` 子目录说明 |
| `reproduce/` 产物子目录 | `fix/<BUG-NNN>/reproduce/` | 新增(运行时) | 存放 4 类产物 |

## 5. 接口概要

### 5.1 内部接口(伪代码)

| 接口名 | 形式 | 状态 | 职责 |
| --- | --- | --- | --- |
| `detectStartability(cwd)` | 函数 | 新增 | 探测项目可启动性;返回 `canStart: bool` + `startCommand: string \| null`(伪代码内联到 SKILL.md,**不**作为代码模块) |
| `reproduceBug(bugNum, startCommand, reproSteps, timeout=60s)` | 函数 | 新增 | 执行复现动作;返回 `RESULT-meta.json` 数据(伪代码内联到 SKILL.md) |
| `collectLogArtifact(stdout, stderr, outputPath)` | 函数 | 新增 | 合并 stdout + stderr → `run.log`,加时间戳(伪代码) |
| `collectScreenshotArtifact(step, projectType, outputPath)` | 函数 | 新增 | 截图采集(playwright → puppeteer → headless-chrome 链式降级)(伪代码) |
| `collectInteractionArtifact(step, request, response, outputPath)` | 函数 | 新增 | 交互数据采集(JSON 格式)(伪代码) |

### 5.2 外部接口

**0 项外部接口变更**。本需求**不**修改 `code-plan` / `code-it` / `code-check` / 其他 9 个 `code-*` 技能的任何接口。

## 6. 数据结构

### 6.1 文档头新增字段(`fix/<BUG-NNN>/RESULT.md`)

| 字段名 | 类型 | 值域 | 来源 |
| --- | --- | --- | --- |
| 复现方式 | enum | `程序复现` / `文本复现` / `未复现` | FR-6(本需求新增) |
| 产物路径 | 字符串 | `reproduce/` 或 空 | FR-6(本需求新增) |

### 6.2 产物子目录结构(`fix/<BUG-NNN>/reproduce/`)

| 文件 | 字段 | 必选? | 说明 |
| --- | --- | --- | --- |
| `run.log` | 时间戳 + 进程 stdout + stderr | 必 | FR-3.1(> 10MB 截断) |
| `screenshot-N.png` | PNG 二进制 | 可选 | FR-3.2(UI 缺陷) |
| `interaction-N.{json\|txt}` | JSON / 文本 | 可选 | FR-3.3(API 缺陷) |
| `RESULT-meta.json` | 元信息 JSON | 必 | FR-4(8 字段) |

### 6.3 `RESULT-meta.json` 结构(FR-4)

```json
{
  "bugNum": "BUG-00006",
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

## 7. 三方依赖评估

**0 项新增三方依赖**。

| 评估项 | 结论 |
| --- | --- |
| 新增依赖数量 | 0 |
| 运行时探测工具 | playwright / puppeteer / headless-chrome(运行时探测,链式降级,**不**作为项目级依赖) |
| 项目级影响 | 仓库**不**改 `package.json` / `pyproject.toml` / 任何依赖清单 |
| 必要性 | — |
| 替代评估 | 沿用 V0.0.3 既有"运行时探测 + 链式降级"模式(参 `code-it` FR-2 `tokei/cloc/heuristic` 模式) |

## 8. 关联设计

**0 项关联设计**。

- 本需求改造仅限 `code-fix` 技能 + 2 个模板;其他 `code-*` 技能(14 个)无"复现证据" 相关设计
- 跨版本扫描:0 个 V0.0.1 / V0.0.2 / V0.0.3 关联设计

## 9. 规范遵循

**0 项冲突**;**0 项偏离**。

- 详细自检见 `rule-compliance.md` §6(13 份规范自检结论表)
- 严守 `skill-conventions §规则 1-2`(frontmatter 保留 + 不引入开发痕迹)
- 严守 `dashboard-conventions §规则 1` 0 触发(产物放子目录,**不**新增看板列)
- 严守 `module-conventions §规则 1`(资源放 `templates/` 子目录;本设计仅修改既有模板,**不**新增子目录)
- 严守 NFR-3 / NFR-7 / NFR-8 / NFR-9(零规范变更 / 不污染总览 / 不引入开发痕迹 / 不修改项目源码)

## 10. 待澄清 / 未决项

(已从上游 `require/REQ-00040/RESULT.md §12` 沿用,本设计不增加新澄清)

- **Q-1**:截图工具选型具体偏好(playwright / puppeteer / headless-chrome)— 默认首选 playwright,降级链见 FR-3.2
- **Q-2**:`reproduce/` 子目录命名是否带时间戳 — 默认**不**带,沿用固定路径
- **Q-3**:复现动作是否需要沙箱环境 — 本轮**不**实现,留作 follow-up
- **Q-4**:`reproduce/` 子目录是否需要 `.gitignore` — 留作 follow-up,默认**不**改 `.gitignore`

## 11. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-25 | v1 | 初始创建 | 完成首次概要设计;10 项关键决策 + 8 条不变量;模块数 2(SKILL.md + bug.md)+ 1 辅助(assistants-layout.md);0 关联设计;0 规范冲突;0 新增三方依赖;4 份过程文档(materials-index / design-notes / module-breakdown / rule-compliance)+ 0 份过程文档(dependencies 0 / related-designs 0 / clarifications 0) | 用户 |
