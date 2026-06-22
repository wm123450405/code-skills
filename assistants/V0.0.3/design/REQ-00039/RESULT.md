# 概要设计 — 优化 /code-it、/code-check 等技能:代码行数限制仅统计实际逻辑行

- 需求编码:REQ-00039
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00039/RESULT.md (v1,2026-06-22 14:00)
- 遵循规范:./assistants/rules/ 下 13 个规范文件(详见 §"规范遵循")
- 状态:草稿
- 责任人:用户
- 创建:2026-06-22 14:30
- 最近更新:2026-06-22 14:30
- 当前版本:v1

## 设计目标

<!-- 本节由 code-design 步骤 0b 自动生成(写入或沿用),记录用户确认的设计目标;如需手动编辑,保留该注释以便步骤 0b 识别 -->

- 整体设计目标:`--balanced`(code-auto 上下文自动采纳)
- 维度优先级:
  - 功能性:高(沿用)
  - 扩展性:不适用(无新依赖 / 无新模块,沿用既有 tokei/cloc 系统命令)
  - 健壮性:高(tokei/cloc 检测 + 启发式回退保底,NFR-2 失败不阻断)
  - 可维护性:高(共享库 1 处定义,2 处引用;字节级沿用既有章节)
  - 封装性:不适用(本仓库 Markdown 自然语言)
  - 可复用性:不适用(无新工具 / 沿用既有 4 类工具)
  - 可读性:不适用(本仓库 Markdown 自然语言)

## 1. 详细设计概述

本概要设计把上游需求的 5 FR / 8 NFR / 8 AC **精确化**到代码字符集层面:明确 2 SKILL.md(`code-it` / `code-check`)+ 1 模板 + 2 共享库文档(`code-it/lib/logic-loc.md` + `logic-loc-defaults.md`)的**目标位置 / 已有结构 / 新增内容 / 相对位置**(语义化定位),并产出 5 条 `code-plan` 候选任务。

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

### 2.2 上游需求(REQ-00039 §6-§9 关联)

- AC-1 ~ AC-8:8 条验收标准(详 §10)

### 2.3 规范遵循

(详见 §3 规范遵循 + `rule-compliance.md`)

## 3. 规范遵循

### 3.1 适用的规范文件

| 规范文件 | 类别 | 关键约束 | 本概要设计对应章节 |
| --- | --- | --- | --- |
| `./assistants/rules/skill-conventions.md` §规则 1, §规则 2 | SKILL.md 编写 | frontmatter `name` + `description` 必含;不得包含开发痕迹 | §6 字节级保留 frontmatter;§6 新写段落不含开发痕迹 |
| `./assistants/rules/dashboard-conventions.md` §规则 1 | 看板字段约定 | 字段扩展需三方同步 | §3.2 论证:**不**触发(本需求**不**新增看板列) |
| `./assistants/rules/encoding-conventions.md` §规则 1, §规则 2, §规则 3, §规则 4 | 编码格式 | REQ/BUG/TASK 命名;5 位纯数字;接收端宽松正则 | §6(NFR-4 缺陷分支不触达,本设计**不**修改 BUG 编号格式) |
| `./assistants/rules/migration-mapping.md` §规则 1, §规则 4 | 编码迁移 | `EXISTING-NNN` 不追溯;新旧编码追溯表 | §6(NFR-3 历史 BUG 状态保留,本设计**不**引入新编码) |
| `./assistants/rules/directory-conventions.md` §规则 1 | 目录与模块 | `plugins/code-skills/skills/<name>/` 子目录布局 | §6(无冲突) |
| `./assistants/rules/doc-conventions.md` §规则 1, §规则 2 | 文档编写 | README 多语言对仗 + 主语言完整性 | §6(SKILL.md 不是 README,本规则不适用) |
| `./assistants/rules/naming-conventions.md` §规则 1 | 命名 | kebab-case | §5(模块名 `logic-loc` / `logic-loc-defaults` 符合) |
| `./assistants/rules/coding-style.md` §规则 1 | 代码风格 | (本设计是 Markdown 自然语言,沿用既有风格) | §6(无冲突) |
| `./assistants/rules/framework-conventions.md` §规则 1 | 框架 | (无框架变更) | §6(无冲突) |
| `./assistants/rules/dependency-conventions.md` §规则 1 | 依赖 | 沿用既有 tokei/cloc 系统命令,本设计**不**新增依赖 | §6(本设计无新增三方依赖) |
| `./assistants/rules/commit-conventions.md` §规则 1 | 提交 | `chore(code-<技能>):` 模式 | §6 任务实施策略(沿用既有 `chore(code-<技能>):` 模式) |
| `./assistants/rules/marketplace-protocol.md` §规则 1 | marketplace | 协议字段约束 | §6(本设计**不**动 `.claude-plugin/`) |
| `./assistants/rules/module-conventions.md` §规则 1 | 模块 | `templates/` 留作历史不删;新模块在 `lib/` | §5(本设计新模块在 `code-it/lib/` 而非 `templates/`) |

### 3.2 不触发 §规则 1(dashboard-conventions 三同步)的论证

(沿用上游 §2.5.2 论证 — 本需求**不**新增看板列,**不**修改 `code-it` / `code-check` 任务清单字段;`calcLogicLoc` metadata 写到 `code/<task>/RESULT.md` 而非看板)

### 3.3 不触发 `skill-conventions §规则 2`(SKILL.md 不含开发痕迹)的论证

(沿用上游 §2.5.2 论证 — 本设计新写段落**不**含"本需求 REQ-NNNNN 新增" / "原 code-it 状态机" / "Q-N 锁定" / "YYYY-MM-DD 起生效" / 退场文件名引用 等 6 类开发痕迹)

## 4. 数据结构

> 本节给出"概要化"层数据结构,展开字段类型 / 约束 / 索引 / 存储选型(沿用 `code-design` §4 职责,沿用 `code-require` §8 数据结构概要)。

### 4.1 逻辑行 metadata(本设计核心数据)

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| `filePath` | `string` | 相对 CWD 路径 | — | 变更文件路径 |
| `newLoc` | `number` | ≥ 0 | — | 本任务新增逻辑行(修改后 - 修改前,新建文件 = 修改后) |
| `totalLoc` | `number` | ≥ 0 | — | 修改后文件总逻辑行规模 |
| `detection` | `enum<string>` | 字面固定(不归一化) | — | 检测方式:`tokei` / `cloc` / `heuristic` |

### 4.2 实体关系(沿用既有 + 概要化)

| 实体 | 关系 | 存储选型 | 迁移需求 |
| --- | --- | --- | --- |
| `code/<TASK-...>/RESULT.md` | 1 个任务对应 1 个文件;新增"## 逻辑行统计"小节是该任务逻辑行 metadata 的**权威源** | Markdown 文件(沿用既有) | 无 |
| `code-it/lib/logic-loc.md` | 1 个共享库对应 4 个函数 | Markdown 文件(新建) | 无 |
| `code-it/lib/logic-loc-defaults.md` | 1 个默认值文件对应 2 个阈值 | Markdown 文件(新建) | 无 |

### 4.3 阈值字段(FR-5 可选)

| 字段 | 类型 | 约束 | 默认值 |
| --- | --- | --- | --- |
| `单文件逻辑行总规模阈值` | `number` | > 0 | 500 |
| `单文件逻辑行新增阈值` | `number` | > 0 | 200 |

## 5. 模块拆分

> 沿用 `code-design` §"步骤 9A 模块拆分"小节,5 列格式(模块名 / 路径 / 状态 / 职责 / 依赖)。
> 详 `module-breakdown.md` 完整内容;本节为概要复述。

| 模块名 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| `logic-loc.md` | `plugins/code-skills/skills/code-it/lib/logic-loc.md` | **新增** | 共享库:逻辑行计算函数(4 函数) | 无 |
| `logic-loc-defaults.md` | `plugins/code-skills/skills/code-it/lib/logic-loc-defaults.md` | **新增** | 阈值默认值(2 字段) | `logic-loc.md` |
| `code-it/SKILL.md` | `plugins/code-skills/skills/code-it/SKILL.md` | **修改既有** | 步骤 8 末尾追加 2 子步骤;屏显契约 | `logic-loc.md` |
| `code-check/SKILL.md` | `plugins/code-skills/skills/code-check/SKILL.md` | **修改既有** | 步骤 8.13 新增 + 评审维度速查表第 13 维度 | `logic-loc.md` |
| `code-it/templates/RESULT.md` | `plugins/code-skills/skills/code-it/templates/RESULT.md` | **修改既有** | "## 逻辑行统计"小节示例 | 无 |

**模块数 = 5**(≥ 2 → 满足 `module-breakdown.md` 生成准则)

## 6. 接口与数据结构概要

> 沿用 `code-design` §"步骤 10A 接口与数据结构"小节,接口与数据结构**概要**呈现。
> 接口签名 / 数据格式 / 错误码 / 完整入参出参**下沉**到 `code-plan` 的 `interface-specs.md` / `data-changes.md`。

### 6.1 接口概要

| 接口名 | 形式 | 状态 | 一句话职责 |
| --- | --- | --- | --- |
| `detectLocTool()` | 函数(Markdown 伪代码) | **新增** | 检测本机可用工具(`tokei` / `cloc` / `heuristic`) |
| `calcLogicLines(filePath, tool)` | 函数(Markdown 伪代码) | **新增** | 计算单文件逻辑行(`newLoc` + `totalLoc` + `detection`) |
| `heuristicLoc(filePath, lang)` | 函数(Markdown 伪代码) | **新增** | 启发式回退算法(5 主流语言) |
| `code-check-exceed(file, totalLoc, newLoc, threshold)` | 函数(Markdown 伪代码) | **新增** | `code-check` 派生"代码行数超标"发现 |

**接口约束**(FR-1 / FR-2 字节级沿用):
- `detectLocTool()` 输出: `"tokei" | "cloc" | "heuristic"`
- `calcLogicLines()` 输出: `{ newLoc: number, totalLoc: number, detection: string }`
- `heuristicLoc()` 输出: `number`(逻辑行)
- `code-check-exceed()` 输出: `[代码行数超标] <file> ...` 描述

### 6.2 数据结构概要

| 实体 | 状态 | 关键字段 | 一句话关系 |
| --- | --- | --- | --- |
| 逻辑行 metadata | **新增** | `filePath` / `newLoc` / `totalLoc` / `detection` | 1 个变更文件对应 1 条 metadata |
| 阈值配置 | **新增**(可选) | `单文件逻辑行总规模阈值` / `单文件逻辑行新增阈值` | 1 个需求对应 1 份阈值配置(无配置走默认 500/200) |

## 7. 三方依赖评估

(本设计**不**新增三方依赖,详见 `process-doc-decisions.md` §"不生成"详情。沿用既有 tokei/cloc 系统命令,本仓库不安装。)

## 8. 架构图(Mermaid / ASCII)

### 8.1 组件图

```
┌────────────────────────────────────────────────────────┐
│ code-it 步骤 8 末尾                                     │
│                                                        │
│  1. detectLocTool()                                    │
│     ├─ Bash: tokei --version ✓ → return "tokei"        │
│     ├─ Bash: cloc --version ✓ → return "cloc"          │
│     └─ both ✗ → ⚠ + return "heuristic"                │
│                                                        │
│  2. calcLogicLoc(taskNum)                              │
│     ├─ git diff --numstat → 变更文件列表                │
│     ├─ per-file: detect + calc → {newLoc, totalLoc}    │
│     ├─ write code/<task>/RESULT.md "## 逻辑行统计"     │
│     └─ screen: === code-it 逻辑行统计 ===              │
└────────────────┬───────────────────────────────────────┘
                 │ shared lib
                 ▼
┌────────────────────────────────────────────────────────┐
│ code-it/lib/logic-loc.md (共享库)                       │
│                                                        │
│  - detectLocTool()    : tokei / cloc / heuristic         │
│  - calcLogicLines()   : { newLoc, totalLoc, detection } │
│  - heuristicLoc()     : 5 主流语言                       │
│  - code-check-exceed(): 派生"代码行数超标"             │
└────────────────┬───────────────────────────────────────┘
                 │ shared lib
                 ▼
┌────────────────────────────────────────────────────────┐
│ code-check 步骤 8.13 (新)                              │
│                                                        │
│  1. 读 code/<task>/RESULT.md "## 逻辑行统计"           │
│  2. 读阈值(默认 500 / 200)                            │
│  3. per-file: code-check-exceed → 派生发现              │
│  4. 评审维度速查表新增第 13 维度(P3)                  │
└────────────────────────────────────────────────────────┘
```

### 8.2 关键数据流

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
```

## 9. 边界与异常

> 本节给出"概要化"层边界与异常,展开伪代码 / 详细处理**下沉**到 `code-plan` 详设阶段。

### 9.1 退化路径

- **tokei 不存在 + cloc 不存在** → 屏显 `⚠ 建议安装 tokei/cloc 以获得准确逻辑行统计;本次回退到启发式`,使用启发式算法
- **git diff 失败(非 git 仓库)** → 屏显 `⚠ 非 git 仓库,无法获取变更文件列表;本次跳过 calcLogicLoc`
- **变更文件无法访问(权限/不存在)** → 跳过该文件,屏显警告
- **单文件过大(> 10MB)** → 跳过该文件,屏显警告(性能)
- **无 `code/<task>/RESULT.md` 的"## 逻辑行统计"小节(老任务 / REQ-00039 之前)** → `code-check` 步骤 8.13 跳过该任务,不派生发现
- **阈值配置缺失** → 默认 500 / 200

### 9.2 缺陷分支跳过(NFR-8)

- 缺陷路径(`^TASK-BUG-...`)**不**触达 `calcLogicLoc`(沿用既有步骤 8a 守卫规则)
- 缺陷路径的 `code/<TASK-BUG-...>/RESULT.md` **不**新增"## 逻辑行统计"小节

### 9.3 失败不阻断(NFR-7)

- `calcLogicLoc` 失败 → 屏显 `⚠` + 跳过,**不**阻断 `code-it` 主流程
- `code-check` 步骤 8.13 失败 → 屏显 `⚠` + 跳过,**不**阻断 `code-check` 主流程

## 10. 性能与资源

- **逻辑行计算总耗时** < 3 秒(典型 100 文件下 < 3 秒)
- tokei/cloc 调一次耗时: < 1 秒(100 文件典型)
- 启发式耗时: < 2 秒(100 文件典型)
- 单文件 > 10MB 跳过,避免内存压力

## 11. 测试要点

(本设计是 SKILL.md 行为变更,**不**写单元测试;沿用既有 `code-it` 步骤 8.5 自含按需写单测守卫判定:`code-it` 步骤 8a 7 项检查**不**命中(本仓库无 `package.json` 含 `scripts.test` 等) → 守卫不通过 → 跳过单测 → 任务"测试状态"列 = `不适用`)

## 12. 安全要求

不适用(本设计是 SKILL.md 行为变更,无安全边界)

## 13. 任务实施策略

> 任务粒度由 `code-plan` 步骤 10A 决定(本节给实施策略,不重复任务拆分)。

### 13.1 任务粒度(5 任务)

| 任务 | 范围 | 估算 | 触发/来源 |
| --- | --- | --- | --- |
| T-1 | 共享库 `logic-loc.md` + `logic-loc-defaults.md` 新建 | 0.5 天 | 详细设计 |
| T-2 | `code-it` 步骤 8 末尾追加 `detectLocTool` + `calcLogicLoc` 子步骤 + 屏显契约 | 0.5 天 | 详细设计 |
| T-3 | `code-check` 步骤 8.13 新增 + 评审维度速查表第 13 维度 | 0.5 天 | 详细设计 |
| T-4 | `code-it/templates/RESULT.md` 模板"## 逻辑行统计"小节示例 | 0.25 天 | 详细设计 |
| T-5 | 端到端验证 + 末尾兜底提交 | 0.5 天 | 详细设计 |

**合计**:约 2-3 天工作量(5 个任务)

### 13.2 任务实施顺序

- T-1 → T-2 → T-3 → T-4 → T-5(顺序依赖:T-2 / T-3 / T-4 依赖 T-1 的共享库;T-5 验证全部 4 任务)

### 13.3 实施关键约束

- **不修改 frontmatter**(沿用 C-2 / `skill-conventions §规则 1`)
- **不重排"## 工作流程"既有小节**(沿用 C-3)
- **不引入开发痕迹**(沿用 `skill-conventions §规则 2`)
- **每次 commit 沿用既有 `chore(code-<技能>):` 模式**(沿用 `commit-conventions §规则 1` 占位)
- **不触发 `AskUserQuestion`**(沿用 `code-plan` NFR-3;在实施细节上 AI 自主判断)

## 14. 关联

- 上游需求:`./assistants/V0.0.3/require/REQ-00039/RESULT.md`
- 关联设计:REQ-00038(模块粒度单测)/ REQ-00037(缺陷修复流程)/ REQ-00034(`code-unit` 整合)/ REQ-00022(`code-review` → `code-check` 重命名)
- 共享库:无(本设计新建 2 个共享库:`code-it/lib/logic-loc.md` + `code-it/lib/logic-loc-defaults.md`)

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 14:30 | v1 | 初始创建 | 完成首次概要设计;5 模块详细化 + 4 函数伪代码 + 1 阈值配置 + 1 架构图;`--balanced` + 功能性=高 + 健壮性=高 + 可维护性=高;code-auto 上下文自动采纳默认;0 偏离 / 0 冲突 / 0 用户授权偏离 | 用户 |