# 详细设计 — 优化 /code-it、/code-check 等技能:代码行数限制仅统计实际逻辑行

- 需求编码:REQ-00039
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00039/RESULT.md (v1,2026-06-22 14:00)
- 上游概要设计:./assistants/V0.0.3/design/REQ-00039/RESULT.md (v1,2026-06-22 14:30)
- 遵循规范:./assistants/rules/ 下 13 个规范文件(详见 §"规范遵循")
- 状态:草稿
- 责任人:用户
- 创建:2026-06-22 15:00
- 最近更新:2026-06-22 15:00
- 当前版本:v1

## 设计目标

<!-- 本节由 code-plan 步骤 0b 自动生成(写入或沿用),记录用户确认的设计目标;如需手动编辑,保留该注释以便步骤 0b 识别 -->

- 整体设计目标:`--balanced`(沿用 `design/REQ-00039/RESULT.md` 的设计目标,code-auto 上下文自动采纳)
- 维度优先级:
  - 功能性:高(沿用)
  - 扩展性:不适用(无新依赖 / 无新模块,沿用既有 tokei/cloc 系统命令)
  - 健壮性:高(tokei/cloc 检测 + 启发式回退保底,NFR-2 失败不阻断)
  - 可维护性:高(共享库 1 处定义,2 处引用;字节级沿用既有章节)
  - 封装性:不适用(本仓库 Markdown 自然语言)
  - 可复用性:不适用(无新工具 / 沿用既有 4 类工具)
  - 可读性:不适用(本仓库 Markdown 自然语言)

## 1. 详细设计概述

本详细设计把概要设计的 5 FR / 8 NFR / 8 AC **精确化到代码字符集层面**:明确 2 SKILL.md(`code-it` / `code-check`)+ 1 模板 + 2 共享库文档的**目标位置 / 已有结构 / 新增内容 / 相对位置**(语义化定位)。

**核心机制**:
- **逻辑行计算函数**(FR-1):明确定义"逻辑行 = 总行 - 空行 - 注释行";4 类排除项字面定义
- **工具集成**(FR-2):首选 `tokei`(200+ 语言)/ 备选 `cloc`(50+)/ 回退启发式(无依赖,~95% 精度)
- **`code-it` 步骤 8 末尾 `calcLogicLoc` 子步骤**(FR-3):编码完成后收集逻辑行 metadata
- **`code-check` 步骤 8 评审新增"代码行数超标"发现**(FR-4):评审时读 metadata,超阈值派生发现(P3)
- **阈值配置**(FR-5):默认单文件 ≤ 500 行(总规模)/ ≤ 200 行(新增),用户可配置

**新增/复用/修改范围**:
- 新增:**2 模块**(`code-it/lib/logic-loc.md` + `code-it/lib/logic-loc-defaults.md`)+ **0 接口** + **0 数据结构** + **0 三方依赖**
- 复用既有:`code-it` 步骤 8a / 8.5(REQ-00034 + REQ-00038 改造) / `code-check` 步骤 8.1 ~ 8.12(字节级保留) / 既有 tokei/cloc 系统命令
- 修改既有:2 SKILL.md(`code-it` 步骤 8 末尾 + `code-check` 步骤 8.13)+ 1 模板(`code-it/templates/RESULT.md` "## 逻辑行统计"小节)+ 1 评审维度速查表(`code-check` 新增第 13 维度)

## 2. 上游引用

### 2.1 上游需求(REQ-00039 §4-§10)

- FR-1:逻辑行计算函数(共享定义)— §4 FR-1
- FR-2:工具集成 tokei/cloc/启发式回退 — §4 FR-2
- FR-3:`code-it` 步骤 8 末尾追加 `calcLogicLoc` 子步骤 — §4 FR-3
- FR-4:`code-check` 步骤 8 评审新增"代码行数超标"发现 — §4 FR-4
- FR-5:阈值配置(可选,默认 500/200)— §4 FR-5
- NFR-1(性能 < 3 秒)+ NFR-2(兼容性)+ NFR-3(零规范变更)+ NFR-4(精度)+ NFR-5(可追溯)+ NFR-6(幂等)+ NFR-7(不阻断)+ NFR-8(缺陷分支不触达)— §5 NFR

### 2.2 上游概要设计(REQ-00039 §5-§9 关联)

- 模块拆分:5 模块(详 §4)
- 接口概要:4 函数(详 §6)
- 数据结构概要:`logic-loc.md` 字段 + 阈值配置
- 关键决策:共享库位于 `code-it/lib/`(沿用 `module-conventions §规则 1`)
- 风险与回退:详 §9

### 2.3 规范遵循

(详见 §3 规范遵循 + `rule-compliance.md`)

## 3. 规范遵循

### 3.1 适用的规范文件

| 规范文件 | 类别 | 关键约束 | 本详细设计对应章节 |
| --- | --- | --- | --- |
| `./assistants/rules/skill-conventions.md` §规则 1, §规则 2 | SKILL.md 编写 | frontmatter `name` + `description` 必含;不得包含开发痕迹 | §6 / §7 字节级保留 frontmatter;§6 新写段落不含开发痕迹 |
| `./assistants/rules/dashboard-conventions.md` §规则 1 | 看板字段约定 | 字段扩展需三方同步 | §3.2 论证:**不**触发(本需求**不**新增看板列) |
| `./assistants/rules/encoding-conventions.md` §规则 1, §规则 2, §规则 3, §规则 4 | 编码格式 | REQ/BUG/TASK 命名;5 位纯数字;接收端宽松正则 | §6 / §8(NFR-8 缺陷分支不触达,本设计**不**修改 BUG 编号格式) |
| `./assistants/rules/migration-mapping.md` §规则 1, §规则 4 | 编码迁移 | `EXISTING-NNN` 不追溯;新旧编码追溯表 | §6(NFR-3 历史 BUG 状态保留,本设计**不**引入新编码) |
| `./assistants/rules/directory-conventions.md` §规则 1 | 目录与模块 | `plugins/code-skills/skills/<name>/` 子目录布局 | §4(模块路径生成沿用既有) |
| `./assistants/rules/doc-conventions.md` §规则 1, §规则 2 | 文档编写 | README 多语言对仗 + 主语言完整性 | §4(SKILL.md 不是 README,本规则不适用) |
| `./assistants/rules/naming-conventions.md` §规则 1 | 命名 | kebab-case | §4(模块名 `logic-loc` / `logic-loc-defaults` 符合) |
| `./assistants/rules/coding-style.md` §规则 1 | 代码风格 | (本设计是 Markdown 自然语言,沿用既有风格) | §6(无冲突) |
| `./assistants/rules/framework-conventions.md` §规则 1 | 框架 | (无框架变更) | §6(无冲突) |
| `./assistants/rules/dependency-conventions.md` §规则 1 | 依赖 | 沿用既有 tokei/cloc 系统命令,本设计**不**新增依赖 | §6(本设计无新增三方依赖) |
| `./assistants/rules/commit-conventions.md` §规则 1 | 提交 | `chore(code-<技能>):` 模式 | §8 任务实施策略(沿用既有 `chore(code-<技能>):` 模式) |
| `./assistants/rules/marketplace-protocol.md` §规则 1 | marketplace | 协议字段约束 | §6(本设计**不**动 `.claude-plugin/`) |
| `./assistants/rules/module-conventions.md` §规则 1 | 模块 | `templates/` 留作历史不删;新模块在 `lib/` | §4(本设计新模块在 `code-it/lib/` 而非 `templates/`) |

### 3.2 不触发 §规则 1(dashboard-conventions 三同步)的论证

(沿用上游 §2.5.2 论证 — 本需求**不**新增看板列,**不**修改 `code-it` / `code-check` 任务清单字段;`calcLogicLoc` metadata 写到 `code/<task>/RESULT.md` 而非看板)

### 3.3 不触发 `skill-conventions §规则 2`(SKILL.md 不含开发痕迹)的论证

(沿用上游 §2.5.2 论证 — 本设计新写段落**不**含"本需求 REQ-NNNNN 新增" / "原 code-it 状态机" / "Q-N 锁定" / "YYYY-MM-DD 起生效" / 退场文件名引用 等 6 类开发痕迹)

## 4. 模块详细化

> 完整版见 `module-details.md`(沿用既有 5 列字段:模块名 / 路径 / 状态 / 职责 / 依赖 + 关键类/函数/调用顺序/状态归属/错误处理范式/日志埋点)。

### 4.1 模块 1:`logic-loc.md`(共享库,新增)

- **路径**:`plugins/code-skills/skills/code-it/lib/logic-loc.md`
- **职责**:逻辑行计算函数(4 个)+ 检测机制 + 启发式算法
- **依赖**:无

### 4.2 模块 2:`logic-loc-defaults.md`(默认值,新增)

- **路径**:`plugins/code-skills/skills/code-it/lib/logic-loc-defaults.md`
- **职责**:阈值默认值(2 字段)
- **依赖**:`logic-loc.md`

### 4.3 模块 3:`code-it/SKILL.md` 步骤 8 末尾(修改既有)

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md`
- **职责**:实施开发末尾追加 `detectLocTool` + `calcLogicLoc` 子步骤
- **依赖**:`logic-loc.md`

### 4.4 模块 4:`code-check/SKILL.md` 步骤 8.13(修改既有)

- **路径**:`plugins/code-skills/skills/code-check/SKILL.md`
- **职责**:评审派生"代码行数超标"发现 + 评审维度速查表第 13 维度
- **依赖**:`logic-loc.md`

### 4.5 模块 5:`code-it/templates/RESULT.md`(修改既有)

- **路径**:`plugins/code-skills/skills/code-it/templates/RESULT.md`
- **职责**:模板示例展示逻辑行 metadata 格式
- **依赖**:无

## 5. 算法与逻辑

### 5.1 函数 1:`detectLocTool()`

**伪代码**:

```
function detectLocTool():
 1. Bash: tokei --version → exit 0 → return "tokei"
 2. Bash: cloc --version → exit 0 → return "cloc"
 3. 否则 return "heuristic"
```

**复杂度**:O(1)(2 次 Bash 调用)

### 5.2 函数 2:`calcLogicLines(filePath, tool)`

**伪代码**:

```
function calcLogicLines(filePath, tool):
 1. tool="tokei" → Bash: tokei <filePath> --output json
 2. tool="cloc" → Bash: cloc <filePath> --json
 3. tool="heuristic" → return heuristicLoc(filePath, lang)
 4. 解析输出 → { code, comments, blanks }
 5. totalLoc = code
 6. return { newLoc: <从 git diff 计算>, totalLoc, detection: tool }
```

**复杂度**:O(N),N = 文件行数(单文件)

### 5.3 函数 3:`heuristicLoc(filePath, lang)`

**伪代码**:

```
function heuristicLoc(filePath, lang):
 1. 读文件全部行
 2. 过滤空行(`^\s*$`)
 3. 过滤注释行(正则,按语言):
 - Python: `^\s*(#|""")`
 - JS/TS/Go/Java/Rust: `^\s*(//|/\*|\*)`
 - Markdown: `^\s*<!--`
 - 其他语言:仅过滤空行
 4. return 剩余行数
```

**复杂度**:O(N),N = 文件行数(单文件)

### 5.4 函数 4:`code-check-exceed(file, totalLoc, newLoc, threshold)`

**伪代码**:

```
function code-check-exceed(file, totalLoc, newLoc, threshold):
 1. 若 totalLoc > threshold.total:
 - 超出比例 = (totalLoc - threshold.total) / threshold.total
 - 级别:
 - ≤10% → "可选"
 - ≤50% → "建议改"
 - >50% → "必须改"
 - return "[代码行数超标] <file> 逻辑行(总规模)=<totalLoc> 阈值=<threshold.total> 超<P>%(级别:<级别>) 建议拆分..."
 2. 若 newLoc > threshold.new:同上(级别判断 + 文案)
 3. 若无超标 → return null
```

**复杂度**:O(1)

### 5.5 `calcLogicLoc` 任务级聚合

**伪代码**(在 `code-it/SKILL.md` 步骤 8 末尾执行):

```
function calcLogicLoc(taskNum, timestamp):
 1. detectLocTool() → tool
 2. git diff --numstat HEAD~1 -- <task 涉及文件> → changedFiles[]
 3. 对每个 changedFile:
 - Bash: git show HEAD~1:<file> → oldContent(若文件存在)
 - newContent = 当前文件内容
 - oldLoc = calcLogicLines(oldContent, tool).totalLoc(若 oldContent 存在)
 - newLoc = calcLogicLines(newContent, tool).totalLoc
 - delta = newLoc - oldLoc(若 oldContent 存在)
 - newLoc = newLoc(若新建文件)
 4. 累计本任务逻辑行(新增)= Σ delta
 5. 累计本任务逻辑行(总规模)= Σ newLoc
 6. 写 code/<task>/RESULT.md 新增"## 逻辑行统计"小节:
 | 文件 | 逻辑行(新增) | 逻辑行(总规模) | 检测方式 |
 | --- | --- | --- | --- |
 | src/foo.ts | 25 | 80 | tokei |
 | src/bar.py | 10 | 30 | tokei |
 | **本任务汇总** | **35** | **110** | — |
 7. 屏显契约:
 === code-it 逻辑行统计(步骤 8 末尾)===
 任务:<taskNum>
 变更文件:N 个
 逻辑行(新增):<Σ>
 逻辑行(总规模):<Σ>
 检测方式:tokei / cloc / heuristic
 8. 失败 → 屏显 ⚠ + 跳过(不阻断 code-it)
```

**复杂度**:O(M × N),M = 变更文件数(典型 1-20),N = 单文件行数(典型 50-500);总耗时 < 3 秒

### 5.6 `code-check-exceed` 评审级聚合

**伪代码**(在 `code-check/SKILL.md` 步骤 8.13 执行):

```
function checkCodeLocExceed(taskNum, threshold):
 1. 读 code/<task>/RESULT.md 的"## 逻辑行统计"小节
 2. 阈值:默认 500 / 200(沿用 logic-loc-defaults.md)
 3. 对每个变更文件:
 - 调 code-check-exceed(file, totalLoc, newLoc, threshold)
 - 若返回非 null → 追加到评审发现清单
 4. 派生发现格式(沿用 8.12 屏显契约):
 [代码行数超标] <file> 逻辑行(总规模)=<N> 阈值=<M> 超<P>%(级别:<级别>) 建议拆分...
```

**复杂度**:O(M),M = 变更文件数

## 6. 数据结构完整变更

> 本需求**不**涉及数据库/缓存/状态字段变更(沿用 `process-doc-decisions.md` §"`data-changes.md` 不生成")。逻辑行 metadata 存储在 Markdown 文本(`code/<task>/RESULT.md` 的"## 逻辑行统计"小节)。

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| `filePath` | `string` | 相对 CWD 路径 | — | 变更文件路径 |
| `newLoc` | `number` | ≥ 0 | — | 本任务新增逻辑行 |
| `totalLoc` | `number` | ≥ 0 | — | 修改后文件总逻辑行规模 |
| `detection` | `enum<string>` | 字面固定(不归一化) | — | 检测方式:`tokei` / `cloc` / `heuristic` |

## 7. 接口细节

> 完整版见 `interface-specs.md`(沿用既有 4 接口:入参/出参/错误码/示例/版本策略)。

### 7.1 接口 1:`detectLocTool()`

- **形式**:Bash 命令包装函数
- **签名**:`function detectLocTool(): "tokei" | "cloc" | "heuristic"`
- **错误处理**:N/A(纯函数,失败返回 `"heuristic"` + 屏显 `⚠`)

### 7.2 接口 2:`calcLogicLines(filePath, tool)`

- **形式**:Bash 命令包装函数 + 启发式 fallback
- **签名**:`function calcLogicLines(filePath, tool): { newLoc, totalLoc, detection }`
- **错误处理**:失败返回 `{ newLoc: 0, totalLoc: 0, detection: "error" }` + 屏显 `⚠`

### 7.3 接口 3:`heuristicLoc(filePath, lang)`

- **形式**:纯函数(读文件 + 正则过滤)
- **签名**:`function heuristicLoc(filePath, lang): number`
- **错误处理**:失败返回 `0` + 屏显 `⚠`

### 7.4 接口 4:`code-check-exceed(file, totalLoc, newLoc, threshold)`

- **形式**:派生发现生成函数
- **签名**:`function code-check-exceed(...): string | null`
- **错误处理**:无超标 → return `null`

## 8. 异常处理 / 安全要求 / 性能

(详见 `risk-analysis.md`)

### 8.1 异常处理(8 种)

- tokei 不存在 + cloc 不存在 → 屏显 `⚠` + 启发式回退
- git diff 失败(非 git 仓库)→ 屏显 `⚠` + 跳过
- 变更文件无法访问 → 跳过该文件 + 屏显警告
- 单文件过大(> 10MB)→ 跳过该文件 + 屏显警告(性能)
- 无 `code/<task>/RESULT.md` 的"## 逻辑行统计"小节 → `code-check` 步骤 8.13 跳过
- 阈值配置缺失 → 默认 500 / 200
- 缺陷分支(`^TASK-BUG-...`)**不**触达(NFR-8)
- 启发式不支持的语言 → 退化到"仅过滤空行"

### 8.2 安全要求

N/A(本需求是 Markdown 技能定义,无运行时鉴权/审计)

### 8.3 性能

- `calcLogicLoc` 总耗时 < 3 秒(典型 100 文件下)
- tokei/cloc 调一次 < 1 秒
- 启发式 < 2 秒
- 单文件 > 10MB 跳过

## 9. 状态机 / 流程

```
[code-it 步骤 8 实施开发]
  ↓
[Bash: git diff --numstat] → 变更文件列表
  ↓
[detectLocTool] → "tokei" / "cloc" / "heuristic"
  ↓
[per-file: calcLogicLines] → {newLoc, totalLoc, detection}
  ↓
[write code/<task>/RESULT.md "## 逻辑行统计"]
  ↓
[code-check 步骤 8.13] → 读 metadata → 派生发现
  ↓
[code-checkexceed] → [代码行数超标] <file> ...
```

## 10. 测试要点

(详见 `risk-analysis.md` §"测试要点")

- 单元测试:**不适用**(沿用 `code-it` 步骤 8.5 自含按需写单测守卫判定;本仓库无 `package.json` 含 `scripts.test` 等 → 守卫不通过 → 任务"测试状态"列 = `不适用`)
- 集成测试:AC-1 ~ AC-8(沿用上游 §10)
- 性能:NFR-1 < 3 秒
- 安全:N/A

## 11. 关联需求

| 关联需求 | 关联点 | 影响 |
| --- | --- | --- |
| REQ-00038 | 模块粒度单测 | 本需求**不**修改 `code-it` 步骤 8a / 8.5 |
| REQ-00037 | 缺陷修复流程 | 本需求**不**涉及缺陷路径 |
| REQ-00034 | `code-unit` 整合 | 本需求沿用既有 `code-it` 步骤 8a / 8.5 |
| REQ-00022 | `code-review` → `code-check` 重命名 | 本需求沿用既有 `code-check` SKILL.md |

## 12. 待澄清 / 未决项

(无 — code-auto 上下文,1 轮 `AskUserQuestion` 全部跳过,采纳 `--balanced` 默认)

## 13. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 15:00 | v1 | 初始创建 | 完成首次详细设计;5 模块详细化 + 4 函数伪代码 + 1 算法聚合 + 8 异常路径;`--balanced` + 功能性=高 + 健壮性=高 + 可维护性=高;code-auto 上下文自动采纳默认;0 偏离 / 0 冲突 / 0 用户授权偏离;15 条规范全部满足 | 用户 |