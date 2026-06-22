# REQ-00037 — 详细设计 — 优化 /code-fix 技能及整个缺陷修复流程的状态推进

- 需求编码:REQ-00037
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00037/RESULT.md (v1)
- 上游概要设计:./assistants/V0.0.3/design/REQ-00037/RESULT.md (v1)
- 遵循规范:./assistants/rules/(13 个规范文件,详见 §3)
- 状态:草稿
- 责任人:用户
- 创建:2026-06-22
- 最近更新:2026-06-22 09:28
- 当前版本:v1

## 设计目标

<!-- 本节由 code-design / code-plan 步骤 0b 自动生成(写入或沿用),记录用户确认的设计目标;如需手动编辑,保留该注释以便步骤 0b 识别 -->

- 整体设计目标:`--balanced`(沿用 `design/REQ-00037/RESULT.md`)
- 维度优先级:
  - 功能性:高(沿用)
  - 扩展性:不适用(无新依赖 / 无新模块)
  - 健壮性:高(NFR-2 状态推进失败回退是核心)
  - 可维护性:高(4 SKILL.md + 1 看板技能扩展需保持一致)
  - 封装性:不适用(本仓库 Markdown 自然语言)
  - 可复用性:不适用(沿用既有 `Edit` 工具,不引入新工具)
  - 可读性:不适用(本仓库 Markdown 自然语言)

## 1. 详细设计概述

本详细设计把概要设计的 6 个功能域**精确化到代码字符集层面**:明确每个 SKILL.md 修改的**目标位置 / 已有结构 / 新增内容 / 相对位置**(语义化定位,沿用 `code-plan` "## 修改文件定位的语义化约定"),并产出 7 条 `code-it` 任务。

**核心机制**:5 处"状态回写"子步骤(`code-fix` 步骤 6 + `code-plan` 步骤 27A/28A + `code-it` 步骤 21/24 + `code-check` 步骤 13),用既有 `Edit` 工具写 `fix/<BUG-NNN>/RESULT.md` 文档头"状态"字段 + 同步 `fix/RESULT.md` + 同步版本看板。每个子步骤都先读当前状态字面,按"新字面 vs 老字面"判定推进策略(沿用概设 §6.2 / §6.5 判定矩阵)。

**新增/复用/修改范围**(同概设,精确化):
- 新增:**0** 模块 / 0 接口 / 0 数据结构 / 0 三方依赖
- 复用既有:`Edit` / `Read` 工具 + `dashboard-conventions §规则 1` 锚点 + `encoding-conventions §规则 1` 正则
- 修改既有:4 个 SKILL.md(`code-fix` / `code-plan`(BUG 路径)/ `code-it`(BUG 路径)/ `code-check`)+ 1 个看板显示技能(`code-dashboard`)

## 2. 上游引用

### 2.1 上游需求(REQ-00037 §4-§10)

(本节是上游需求与本详细设计的交叉点,详见 `materials-index.md`)

### 2.2 上游概要设计(REQ-00037 §6)

(本节是上游设计与本详细设计的承接点,沿用概设的 6 功能域)

### 2.3 规范遵循

(详见 §3)

## 3. 规范遵循

### 3.1 适用的规范文件

| 规范文件 | 类别 | 关键约束 | 本详细设计对应章节 |
| --- | --- | --- | --- |
| `./assistants/rules/skill-conventions.md` §规则 1, §规则 2 | SKILL.md 编写 | frontmatter `name` + `description` 必含;不得包含开发痕迹 | §3.2 字节级保留 frontmatter;§6 / §7 新写段落不含开发痕迹 |
| `./assistants/rules/dashboard-conventions.md` §规则 1 | 看板字段约定 | 字段扩展需三方同步 | §3.3 论证:**不**触发(状态字段是自由字符串列) |
| `./assistants/rules/encoding-conventions.md` §规则 1, §规则 2, §规则 3, §规则 4 | 编码格式 | REQ/BUG/TASK 命名;5 位纯数字;接收端宽松正则 | §4 数据结构(NFR-4 不修改 BUG 编号格式) |
| `./assistants/rules/migration-mapping.md` §规则 1, §规则 4 | 编码迁移 | `EXISTING-NNN` 不追溯;新旧编码追溯表 | §4(NFR-3 历史 BUG 状态保留,本设计不引入新编码) |
| `./assistants/rules/directory-conventions.md` §规则 1 | 目录与模块 | (待添加,占位) | §6(无冲突) |
| `./assistants/rules/doc-conventions.md` §规则 1, §规则 2 | 文档编写 | README 多语言对仗 + 主语言完整性 | §6(SKILL.md 不是 README,本规则不适用) |
| `./assistants/rules/naming-conventions.md` §规则 1 | 命名 | (待添加,占位) | §6(无冲突) |
| `./assistants/rules/coding-style.md` §规则 1 | 代码风格 | (待添加,占位) | §6(无冲突) |
| `./assistants/rules/framework-conventions.md` §规则 1 | 框架 | (待添加,占位) | §6(无冲突) |
| `./assistants/rules/dependency-conventions.md` §规则 1 | 依赖 | (待添加,占位) | §10(本设计无新增三方依赖) |
| `./assistants/rules/commit-conventions.md` §规则 1 | 提交 | (待添加,占位) | §12 任务实施策略(沿用既有 `chore(code-<技能>):` 模式) |
| `./assistants/rules/marketplace-protocol.md` §规则 1 | marketplace | 协议字段约束 | §6(本设计不动 `.claude-plugin/`) |

### 3.2 不触发 §规则 1(dashboard-conventions 三方同步)的论证

(沿用概设 §2.5.2 详细论证 — 状态字段是"自由字符串列",字面变更**不**算"枚举值变更";本设计**不**新增列、**不**修改列名、**不**改字段语义)

### 3.3 不触发 `skill-conventions §规则 2`(SKILL.md 不含开发痕迹)的论证

(沿用概设 §2.5.2 论证 — 本设计新写段落**不**含"本需求 REQ-NNNNN 新增" / "原 code-fix 状态机" / "Q-N 锁定" / "YYYY-MM-DD 起生效" / 退场文件名引用 等 6 类开发痕迹)

## 4. 数据结构

> 本节给出"详细化"层数据结构,展开字段类型 / 约束 / 索引 / 存储选型(沿用 `code-plan` §4 职责,沿用 `code-design` §9 数据结构概要)。

### 4.1 BUG 状态机扩展(本设计核心数据)

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| 状态字面集合(共 15 个) | `enum<string>` | 字面字面固定(不归一化) | — | **新增 5 个**:`待处理` / `待开发` / `开发中` / `待审查` / `已完成`;既有 10 个老字面:`报告` / `调查中` / `修复规划中` / `修复编码中` / `已修复-待验证` / `已修复-已验证` / `已关闭` / `已关闭-非缺陷` / `已取消` / `阻塞` |
| 状态字段位置(3 处) | `string` | 3 处字面必须**一致**(沿用 `code-fix` 步骤 8 同步模式) | — | `fix/<BUG-NNN>/RESULT.md` 文档头"当前状态" / `fix/RESULT.md` 缺陷清单表"状态"列 / 看板"缺陷清单"区段"状态"列 |
| 状态推进归属(5 个新字面) | `enum<技能>` | 字面 → 推进技能一一对应 | — | `待处理` ← `code-fix`(新建入口);`待处理 → 待开发` ← `code-plan`(步骤 27A/28A 末尾);`待开发 → 开发中` ← `code-it`(步骤 21 末尾);`→ 待审查` ← `code-it`(步骤 24 末尾);`待审查 → 已完成` ← `code-check`(步骤 13 末尾) |

### 4.2 实体关系(沿用既有 + 详细化)

| 实体 | 关系 | 存储选型 | 迁移需求 |
| --- | --- | --- | --- |
| `fix/<BUG-NNN>/RESULT.md` | 1 个 BUG 对应 1 个文件;文档头"状态"字段是该 BUG 状态机当前值的**权威源** | Markdown 文件(沿用既有) | 无 |
| `fix/RESULT.md` | 1 个版本对应 1 个总览文件;缺陷清单表的"状态"列与 `fix/<BUG-NNN>/RESULT.md` 文档头"状态"字段必须一致 | Markdown 文件(沿用既有) | 无 |
| 看板"缺陷清单"区段(`./assistants/<版本号>/RESULT.md`) | 1 个版本对应 1 个区段;"状态"列与 `fix/RESULT.md` 缺陷清单表必须一致 | Markdown 文件(沿用既有) | 无 |

### 4.3 状态字段字面变更的兼容性(NFR-3 详细化)

| 旧 BUG 当前状态字面 | `code-plan` 推进时 | `code-it` 推进时 | `code-check` 推进时 |
| --- | --- | --- | --- |
| `待处理`(新) | 推进 `→ 待开发` | 若首条任务:推 `→ 开发中`;若全部完成:推 `→ 待审查` | 推 `→ 已完成` |
| `待开发`(新) | 跳过(已推进过) | 若首条任务:推 `→ 开发中`;若全部完成:推 `→ 待审查` | 推 `→ 已完成` |
| `开发中`(新) | 跳过 | 跳过;若全部完成:推 `→ 待审查` | 推 `→ 已完成` |
| `待审查`(新) | 跳过 | 跳过 | 推 `→ 已完成` |
| `已完成`(新) | 跳过 | 跳过 | 跳过 |
| `报告`(老) | 维持(走老路径推 `修复规划中`) | 维持(走老路径推 `修复编码中`) | 维持 |
| `调查中`(老) | 维持 | 维持 | 维持 |
| `修复规划中`(老) | 维持 | 维持 | 维持 |
| `修复编码中`(老) | 维持 | 维持 | 维持 |
| `已修复-待验证`(老) | 维持 | 维持 | 维持 |
| `已修复-已验证`(老) | 维持 | 维持 | 维持 |
| `已关闭`(老) | 维持 | 维持 | 维持 |
| `已关闭-非缺陷`(老) | 维持 | 维持 | 维持 |
| `已取消`(老) | 维持 | 维持 | 维持 |
| `阻塞`(老) | 维持 | 维持 | 维持 |

## 5. 算法与逻辑

> 本节给出"详细化"层算法,展开伪代码 / 流程图 / 状态机(沿用 `code-plan` §5 职责)。

### 5.1 `code-fix` 步骤 6 新建分支(状态回写入口)

**伪代码**:

```
// code-fix/SKILL.md §"步骤 6 — 写缺陷详情 RESULT.md"
// 新建分支(本设计修改点)

function writeFixDocNew(bugNum, severity, reporter, description, timestamp):
  // ... (既有字段写盘,沿用 code-fix 步骤 6 既有逻辑)

  // [本设计新增] 文档头"状态"字段写 "待处理"
  writeFrontmatter(bugDir, {
    "bugNum": bugNum,
    "severity": severity,
    "reporter": reporter,
    "reportTime": timestamp,
    "status": "待处理",  // ← 本设计:从 "报告" 改为 "待处理"
    "owner": reporter
  })

  // ... (既有修复日志 + 变更记录追加,沿用既有)
  appendFixLog(bugDir, `${timestamp} 登记 ${reporter} 报告缺陷:${description}`)
  appendChangeLog(bugDir, `${timestamp} 缺陷登记 code-fix 创建缺陷 ${bugNum}(严重度 ${severity},状态=待处理) ${bugNum}`)

  // [既有] 同步 fix/RESULT.md 缺陷清单
  syncFixRegistry(bugNum, "待处理")

  // [既有] 同步版本看板"缺陷清单"
  syncKanbanBugList(bugNum, "待处理")
```

**复杂度**:O(1)(不依赖其他读)

### 5.2 `code-plan` 步骤 27A 状态回写(`待处理 → 待开发`)

**伪代码**:

```
// code-plan/SKILL.md §"步骤 27A — 同步 fix/<BUG-NNN>/RESULT.md 与 fix/RESULT.md"
// 步骤 27A 末尾(本设计新增子步骤)

function planStateRollback(bugNum, timestamp):
  fixDocPath = `./assistants/${version}/fix/${bugNum}/RESULT.md`
  registryPath = `./assistants/${version}/fix/RESULT.md`

  // 1. 读 fix/<BUG-NNN>/RESULT.md 当前状态
  oldStatus = parseFrontmatterStatus(fixDocPath)  // 解析文档头"状态"字段

  // 2. 判定推进策略(沿用 §4.3 状态字段字面变更表)
  newStatus = determineNewStatus(oldStatus, "code-plan")
  // determineNewStatus 内部:
  //   oldStatus == "待处理" → return "待开发"
  //   oldStatus in ["报告", "调查中", "修复规划中"] → return oldStatus (维持)
  //   oldStatus in ["待开发", "开发中", "待审查", "已完成"] → return oldStatus (跳过)
  //   else → return oldStatus + warn(⚠)

  // 3. 幂等检查:若 newStatus == oldStatus,跳过
  if newStatus == oldStatus:
    log("✓ code-plan 状态回写:无变化,跳过(旧状态=" + oldStatus + ")")
    return

  // 4. 用 Edit 写新状态到 fix/<BUG-NNN>/RESULT.md 文档头
  editFrontmatter(fixDocPath, "status", newStatus)
  appendFixLog(fixDocPath, `${timestamp} 修复规划 code-plan 完成,状态推进`)
  appendChangeLog(fixDocPath, `${timestamp} 状态推进 ${bugNum} 状态"${oldStatus}"→"${newStatus}" ${bugNum}`)

  // 5. 同步 fix/RESULT.md 缺陷清单表本行"状态"列
  editRegistryRow(registryPath, bugNum, "状态", newStatus)
  appendRegistryLog(registryPath, `${timestamp} 状态推进 ${bugNum} 状态"${oldStatus}"→"${newStatus}" ${bugNum}`)

  // 6. [失败回退] 若任一同步失败,写回旧状态(沿用 NFR-2)
  // ... (实际实施在工具调用层做)
```

**复杂度**:O(1)(只读 1 个文件 + 写 2 个文件)

### 5.3 `code-it` 步骤 21 状态回写(`待开发 → 开发中`)

**伪代码**:

```
// code-it/SKILL.md §"步骤 21 — 处理缺陷状态与本轮起点"
// 步骤 21 末尾(本设计新增子步骤)

function itStartStateRollback(taskNum, bugNum, timestamp):
  fixDocPath = `./assistants/${version}/fix/${bugNum}/RESULT.md`
  planDocPath = `./assistants/${version}/fix/${bugNum}/PLAN.md`
  registryPath = `./assistants/${version}/fix/RESULT.md`

  // 1. 读 fix/<BUG-NNN>/RESULT.md 当前状态
  oldStatus = parseFrontmatterStatus(fixDocPath)

  // 2. 读 fix/<BUG-NNN>/PLAN.md 任务总览首条
  firstTaskNum = parseFirstTaskNum(planDocPath)  // 沿用 dashboard-conventions §规则 1 锚点 ^## 任务总览$

  // 3. 判定推进策略
  if taskNum != firstTaskNum:
    // 不是首条任务,状态维持
    log("✓ code-it 状态回写:本任务非首条,状态维持(旧状态=" + oldStatus + ")")
    return

  if oldStatus != "待开发":
    // 状态已推进过 或 老字面,跳过
    log("✓ code-it 状态回写:状态非 '待开发',跳过(旧状态=" + oldStatus + ")")
    return

  newStatus = "开发中"

  // 4. 写状态 + 同步(沿用 §5.2 同构)
  editFrontmatter(fixDocPath, "status", newStatus)
  appendFixLog(fixDocPath, `${timestamp} 修复开始 code-it 第 1 个任务开始,状态推进`)
  appendChangeLog(fixDocPath, `${timestamp} 状态推进 ${bugNum} 状态"${oldStatus}"→"${newStatus}" ${bugNum}`)
  editRegistryRow(registryPath, bugNum, "状态", newStatus)
  syncKanbanBugList(bugNum, newStatus)
```

**复杂度**:O(1)

### 5.4 `code-it` 步骤 24 状态回写(`→ 待审查`)

**伪代码**:

```
// code-it/SKILL.md §"步骤 24 — 同步 fix/<缺陷编号>/RESULT.md 与看板"
// 步骤 24 末尾(本设计新增子步骤)

function itEndStateRollback(taskNum, bugNum, timestamp):
  fixDocPath = `./assistants/${version}/fix/${bugNum}/RESULT.md`
  planDocPath = `./assistants/${version}/fix/${bugNum}/PLAN.md`
  registryPath = `./assistants/${version}/fix/RESULT.md`

  // 1. 读 fix/<BUG-NNN>/RESULT.md 当前状态
  oldStatus = parseFrontmatterStatus(fixDocPath)

  // 2. 读 fix/<BUG-NNN>/PLAN.md 任务总览,统计"已完成 + 已取消"任务数
  totalTasks, completedOrCanceled = countTasksByStatus(planDocPath)
  // countTasksByStatus 内部:
  //   totalTasks = 表格行数 - 表头行数 - 分隔行数
  //   completedOrCanceled = 表格行中"开发状态"列 ∈ {"已完成", "已取消"} 的行数

  // 3. 判定推进策略
  if completedOrCanceled != totalTasks:
    // 还有任务未完成,状态维持
    log("✓ code-it 状态回写:仍有任务未完成,状态维持(已完成=" + completedOrCanceled + "/" + totalTasks + ")")
    return

  // 全部任务都已结束
  if oldStatus not in ["待开发", "开发中"]:
    // 状态已推进过 或 老字面,跳过
    log("✓ code-it 状态回写:状态非 '待开发/开发中',跳过(旧状态=" + oldStatus + ")")
    return

  newStatus = "待审查"

  // 4. 写状态 + 同步(沿用 §5.2 同构)
  editFrontmatter(fixDocPath, "status", newStatus)
  appendFixLog(fixDocPath, `${timestamp} 修复完成 code-it 全部任务完成,状态推进`)
  appendChangeLog(fixDocPath, `${timestamp} 状态推进 ${bugNum} 状态"${oldStatus}"→"${newStatus}" ${bugNum}`)
  editRegistryRow(registryPath, bugNum, "状态", newStatus)
  syncKanbanBugList(bugNum, newStatus)
```

**复杂度**:O(N),N = `PLAN.md` 任务总览行数(典型 1-20,<< 1 秒)

### 5.5 `code-check` 步骤 13 状态回写(`待审查 → 已完成`)

**伪代码**:

```
// code-check/SKILL.md §"步骤 13 — 同步版本看板"
// 步骤 13 末尾新增"状态回写"子步骤(本设计新增)

function checkStateRollback(bugNum, timestamp):
  fixDocPath = `./assistants/${version}/fix/${bugNum}/RESULT.md`
  registryPath = `./assistants/${version}/fix/RESULT.md`

  // 1. 读 fix/<BUG-NNN>/RESULT.md 当前状态
  oldStatus = parseFrontmatterStatus(fixDocPath)

  // 2. 判定推进策略
  if oldStatus != "待审查":
    // 状态不是 待审查(已推进过 或 老字面),跳过
    log("✓ code-check 状态回写:状态非 '待审查',跳过(旧状态=" + oldStatus + ")")
    return

  newStatus = "已完成"

  // 3. 写状态 + 同步(沿用 §5.2 同构)
  editFrontmatter(fixDocPath, "status", newStatus)
  appendFixLog(fixDocPath, `${timestamp} 评审完成 code-check 评审通过,状态推进`)
  appendChangeLog(fixDocPath, `${timestamp} 状态推进 ${bugNum} 状态"${oldStatus}"→"${newStatus}" ${bugNum}`)
  editRegistryRow(registryPath, bugNum, "状态", newStatus)
  // [既有] 同步版本看板"缺陷清单"区段(沿用 code-check 步骤 13 第 5 款)
```

**复杂度**:O(1)

### 5.6 状态机总览(本设计产出)

```
                                    code-fix(登记入口)
                                          ↓
                                       待处理(新)
                                          ↓ code-fix 复跑(可选,前 5 段)
              ┌──────────┬──────────┬──────────┬──────────┬──────────┐
              ↓          ↓          ↓          ↓          ↓
            报告        调查中   已关闭-非缺陷 已取消      阻塞
            (老)        (老)      (老/终)    (老/终)     (老)
              ↓
        code-plan 完成
              ↓
          待开发(新)
              ↓ code-it 第 1 任务开始
         开发中(新)
              ↓ code-it 全部完成
         待审查(新)
              ↓ code-check 完成
          已完成(新/终)
```

## 6. 模块详细化

> 本节展开每个 SKILL.md 修改的**目标位置 / 已有结构 / 新增内容 / 相对位置**(语义化定位,沿用 `code-plan` "## 修改文件定位的语义化约定")。

### 6.1 模块:`code-fix` SKILL.md

#### 6.1.1 模块信息

- **路径**:`plugins/code-skills/skills/code-fix/SKILL.md`
- **职责**:缺陷登记与跟踪(纯登记型,沿用 REQ-00027)
- **与概要设计的对应**:§6.1 功能域 1
- **符合的规范**:`skill-conventions §规则 1, §规则 2`

#### 6.1.2 关键类/函数(本设计新增)

| 函数名 | 职责 | 签名(伪代码) | 错误处理范式 |
| --- | --- | --- | --- |
| `writeFixDocNew`(修改) | 写新 BUG 详情,文档头"状态" = `待处理` | `writeFixDocNew(bugNum, severity, reporter, description, timestamp)` | 沿用既有 `Write` + `Edit` 流程;失败回退(写回旧状态)+ 屏显 `⚠` |
| `codeFixUpdate`(既有扩展) | 复跑 BUG 时,判定是否推进状态(E-4) | `codeFixUpdate(bugNum)` | 若是 `待开发 / 开发中 / 待审查` → 屏显警告 + 跳过;否则沿用前 5 段逻辑 |

#### 6.1.3 调用顺序

- `code-fix` 步骤 6 → `writeFixDocNew` → 步骤 7 → 步骤 8(同步看板)
- `code-fix` 步骤 6(更新分支) → `codeFixUpdate` → 步骤 7 → 步骤 8

#### 6.1.4 状态归属

- 文档头"状态"字段 = `待处理`(新建) / `报告` / `调查中` / `已关闭-非缺陷` / `已取消` / `阻塞`(复跑前 5 段)

#### 6.1.5 关键变更(语义化定位)

| 变更点 | 目标位置 | 已有结构 | 新增内容 |
| --- | --- | --- | --- |
| C-fix-1 | 步骤 6 "新建分支" → "文档头" 字段写盘(line 281) | `状态: <reportState>`(`reportState` 由 `code-fix` 步骤 6 决定,当前默认 `报告`) | `reportState = "待处理"`(字面替换) |
| C-fix-2 | 步骤 4 状态推进表(line 247-251) | 6 行候选目标状态(`报告 / 调查中 / 已关闭-非缺陷 / 已取消 / 阻塞 / 修复规划中 / 修复编码中 / 已修复-待验证 等`)| **新增 1 行** `(新建) → 待处理 / 报告 / 调查中`;**新增 4 行** `待开发 / 开发中 / 待审查 / 已完成` 字面,候选目标 = `(本技能不推进;由 code-plan / code-it / code-check 推进)` |
| C-fix-3 | 步骤 5 注脚(line 269) | `注:本技能不再推进"修复规划中 / 修复编码中 / 已修复-待验证 / 已修复-已验证"等状态` | 字面替换为:`注:本技能不推进"待开发 / 开发中 / 待审查 / 已完成"等状态 — 这些由 code-plan / code-it / code-check 自动推进` |
| C-fix-4 | 步骤 9 引导下一步表(line 347-354) | 8 行引导(`报告 → 调 code-fix` 等) | 字面替换为:4 行(`待开发 / 开发中 / 待审查 / 已完成`)的"下一步建议" = `(由 ... 推进,本技能不参与)` |
| C-fix-5 | ## 衔接 段"典型完整流程"(line 356-362) | 10 步流程 | 字面替换为:4 步流程(沿用 FR-8 期望结果) |
| C-fix-6 | ## 不要做的事 段(line 433-434) | `不推进"修复规划中 / 修复编码中 / 已修复-待验证 / 已修复-已验证"等状态` | 字面追加:**不**推进`待开发 / 开发中 / 待审查 / 已完成`等状态 — 这些由 `code-plan` / `code-it` / `code-check` 自动推进 |

### 6.2 模块:`code-plan` SKILL.md §"缺陷分支"

#### 6.2.1 模块信息

- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §"缺陷分支(从步骤 1.2 判定为 BUG-NNN 时走)"
- **职责**:为 BUG 制定修复方案(产 RESULT.md + PLAN.md + 7 份过程文档,与 REQ 路径同构)
- **与概要设计的对应**:§6.2 功能域 2
- **符合的规范**:`skill-conventions §规则 1, §规则 2`

#### 6.2.2 关键类/函数(本设计新增)

| 函数名 | 职责 | 签名(伪代码) |
| --- | --- | --- |
| `planStateRollback`(新增) | 步骤 27A 末尾追加"状态回写:推进 → 待开发" | `planStateRollback(bugNum, timestamp)` |

#### 6.2.3 关键变更(语义化定位)

| 变更点 | 目标位置 | 已有结构 | 新增内容 |
| --- | --- | --- | --- |
| C-plan-1 | 步骤 27A "用 Edit 更新" 段尾(line 820-837) | 既有逻辑 `状态:报告 / 调查中 → 修复规划中` | **追加子步骤** `planStateRollback`(详 §5.2);改写为 `状态:待处理 → 待开发 / 其他 → 维持 / 已推进过 → 跳过` |
| C-plan-2 | 步骤 28A 末尾(line 839-848) | 既有逻辑 `状态 → 修复规划中` | **追加子步骤** 同步看板"缺陷清单"区段本行"状态"列(沿用既有 `syncKanbanBugList` 调用) |
| C-plan-3 | ## 不要做的事 段 | 既有 4 条 `不` | 字面追加:`不修改 fix/<BUG-NNN>/RESULT.md 的"缺陷描述" 等稳定章节 — 只更新状态字段、修复日志、变更记录(沿用)` |

### 6.3 模块:`code-it` SKILL.md §"缺陷分支"(17-25)

#### 6.3.1 模块信息

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md` §"缺陷分支(从步骤 1.2 判定为 BUG-NNN 时走)"
- **职责**:实施缺陷修复(产 code/<TASK-BUG-...>/RESULT.md 等)
- **与概要设计的对应**:§6.3 功能域 3
- **符合的规范**:`skill-conventions §规则 1, §规则 2`

#### 6.3.2 关键类/函数(本设计新增)

| 函数名 | 职责 | 签名(伪代码) |
| --- | --- | --- |
| `itStartStateRollback`(新增) | 步骤 21 末尾追加"状态回写:推进 → 开发中" | `itStartStateRollback(taskNum, bugNum, timestamp)` |
| `itEndStateRollback`(新增) | 步骤 24 末尾追加"状态回写:推进 → 待审查" | `itEndStateRollback(taskNum, bugNum, timestamp)` |

#### 6.3.3 关键变更(语义化定位)

| 变更点 | 目标位置 | 已有结构 | 新增内容 |
| --- | --- | --- | --- |
| C-it-1 | 步骤 21 "处理缺陷状态与本轮起点" 末尾(line 891-900) | 既有逻辑 `修复规划中 → 修复编码中` | **追加子步骤** `itStartStateRollback`(详 §5.3);改写判定逻辑:本任务 = PLAN.md 首条 + 当前状态 = `待开发` → 推 `开发中` |
| C-it-2 | 步骤 24 "同步 fix/<缺陷编号>/RESULT.md 与看板" 末尾(line 955-985) | 既有逻辑 `修复编码中 → 已修复-待验证` | **追加子步骤** `itEndStateRollback`(详 §5.4);改写判定逻辑:全部任务已完成+已取消==总任务数 + 当前状态 ∈ {`开发中`, `待开发`} → 推 `待审查` |
| C-it-3 | ## 不要做的事 段 | 既有 4 条 `不` | 字面追加:`不修改 fix/<BUG-NNN>/RESULT.md 的"缺陷描述" 等稳定章节 — 只更新状态字段、修复日志、变更记录(沿用)` |

### 6.4 模块:`code-check` SKILL.md

#### 6.4.1 模块信息

- **路径**:`plugins/code-skills/skills/code-check/SKILL.md`
- **职责**:代码评审(REQ 路径 + BUG 路径)
- **与概要设计的对应**:§6.4 功能域 4
- **符合的规范**:`skill-conventions §规则 1, §规则 2`

#### 6.4.2 关键类/函数(本设计新增)

| 函数名 | 职责 | 签名(伪代码) |
| --- | --- | --- |
| `checkStateRollback`(新增) | 步骤 13 末尾追加"状态回写:推进 → 已完成" | `checkStateRollback(bugNum, timestamp)` |

#### 6.4.3 关键变更(语义化定位)

| 变更点 | 目标位置 | 已有结构 | 新增内容 |
| --- | --- | --- | --- |
| C-check-1 | 步骤 1.5 "模式选择"(line 230-239) | 3 态机:无参 / REQ-NNNNN / 其他 | **新增 1 态**:`^BUG-\d{5}$` → BUG 路径 |
| C-check-2 | 步骤 5-12(评审 8.1 ~ 8.13) | REQ 路径骨架 | **字节级沿用**(BUG 路径复用 REQ 路径骨架;不展开 BUG 特化规则) |
| C-check-3 | 步骤 13 "同步版本看板"(line 498-512) | 既有 5 款同步 | **追加第 6 款** "状态回写:推进 → 已完成"(沿用 §5.5) |
| C-check-4 | ## 不要做的事 段 | 既有 N 条 `不` | 字面追加:`不修改 fix/<BUG-NNN>/RESULT.md 的"缺陷描述" 等稳定章节 — 只更新状态字段、修复日志、变更记录(沿用)` |

### 6.5 模块:`code-dashboard` SKILL.md

#### 6.5.1 模块信息

- **路径**:`plugins/code-skills/skills/code-dashboard/SKILL.md`
- **职责**:开发看板(只读,无副作用)
- **与概要设计的对应**:§6.6 功能域 6
- **符合的规范**:`skill-conventions §规则 1, §规则 2`

#### 6.5.2 关键类/函数(本设计新增)

| 函数名 | 职责 | 签名(伪代码) |
| --- | --- | --- |
| `classifyState`(修改) | 步骤 4 段 3 "高优先级缺陷" 判定逻辑扩展 | `classifyState(bug): "P0 待修复" \| "P1 待修复" \| "已修复" \| "其他"` |

#### 6.5.3 关键变更(语义化定位)

| 变更点 | 目标位置 | 已有结构 | 新增内容 |
| --- | --- | --- | --- |
| C-dash-1 | 步骤 4 段 3 "高优先级缺陷"(line 229-240) | `bugs.filter(b => b.severity === "P0" && b.status !== "已修复")` | 字面集合扩展:`b.status !== "已修复" → b.status !== "已完成" && b.status !== "已修复-已验证" && b.status !== "已关闭"`(不归一化;新增 4 字面 + 老字面都算"待修复") |

## 7. 接口细节

> 本节沿用 `code-plan` §6 职责 — 接口形式 / 路径 / 入参 / 出参 / 错误码(本节给出概要级,完整 schema 下沉到实施阶段)。

### 7.1 接口:"状态回写"子步骤(`code-fix` 步骤 6)

- **形式**:Markdown 子步骤
- **路径**:`plugins/code-skills/skills/code-fix/SKILL.md` §"步骤 6 — 写缺陷详情 RESULT.md"
- **入参**:`bugNum` / `severity` / `reporter` / `description` / `timestamp`
- **出参**:`fix/<BUG-NNN>/RESULT.md`(文档头"状态" = `待处理`)+ `fix/RESULT.md` 同步行 + 看板"缺陷清单"同步行
- **错误处理**:失败回退(沿用既有 `Write` 错误处理范式)+ 屏显 `⚠`
- **版本策略**:不适用(本地 Markdown 文件)
- **依据规范**:`skill-conventions §规则 1` + `dashboard-conventions §规则 1`(自由字符串列字面变更)

### 7.2 接口:"状态回写"子步骤(`code-plan` 步骤 27A)

- **形式**:Markdown 子步骤
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §"步骤 27A — 同步 fix/<BUG-NNN>/RESULT.md 与 fix/RESULT.md"
- **入参**:`bugNum` / `timestamp`
- **出参**:`fix/<BUG-NNN>/RESULT.md`(文档头"状态" 可能推进)+ `fix/RESULT.md` 同步行
- **错误处理**:失败回退(NFR-2)+ 屏显 `⚠`

### 7.3 接口:"状态回写"子步骤(`code-it` 步骤 21 / 24)

- **形式**:Markdown 子步骤 × 2
- **路径**:`plugins/code-skills/skills/code-it/SKILL.md` §"缺陷分支" 步骤 21 / 24
- **入参**:`taskNum` / `bugNum` / `timestamp`
- **出参**:`fix/<BUG-NNN>/RESULT.md`(文档头"状态" 可能推进)+ `fix/RESULT.md` 同步行 + 看板"缺陷清单"同步行
- **错误处理**:失败回退(NFR-2)+ 屏显 `⚠`

### 7.4 接口:`code-check` 步骤 1.5 模式选择(三态机)

- **形式**:Markdown 步骤
- **路径**:`plugins/code-skills/skills/code-check/SKILL.md` §"步骤 1.5 — 模式选择"
- **入参**:用户命令参数(string)
- **出参**:`mode`(无参 / `^REQ-\d{5}$` / `^BUG-\d{5}$` 新增 / 其他)
- **错误处理**:无效参数 → 整版本模式 + 警告(沿用既有)
- **示例**:
  - `code-check` → mode=`总览`
  - `code-check REQ-NNNNN` → mode=`单需求`
  - `code-check BUG-NNNNN`(本设计新增)→ mode=`单缺陷`
  - `code-check invalid` → mode=`总览` + `⚠ 忽略参数: invalid`

### 7.5 接口:`code-dashboard` 步骤 4 段 3 判定逻辑

- **形式**:Markdown 步骤
- **路径**:`plugins/code-skills/skills/code-dashboard/SKILL.md` §"步骤 4 段 3"
- **入参**:看板"缺陷清单"区段数据(只读)
- **出参**:屏显"P0 待修复: N | P1 待修复: M"(沿用既有)
- **错误处理**:不适用(只读)

## 8. 状态机 / 流程

(详见 §5.6 状态机总览;各推进点的伪代码见 §5.1 ~ §5.5)

## 9. 性能与资源

(沿用 `risk-analysis.md` §"性能与资源")

## 10. 测试要点

(沿用 `risk-analysis.md` §"测试要点")

## 11. 安全要求

不适用(本设计是 SKILL.md 行为变更,无安全边界)

## 12. 任务实施策略

> 任务粒度由 `code-plan` 步骤 10A 决定(本节给实施策略,不重复任务拆分)。

### 12.1 任务粒度(7 任务)

| 任务 | 范围 | 估算 | 触发/来源 |
| --- | --- | --- | --- |
| T-1 | `code-fix` SKILL.md 步骤 4 / 步骤 6 / ## 衔接 / ## 不要做的事 段同步 | 1 天 | 详细设计 |
| T-2 | `code-plan` SKILL.md §"缺陷分支" 步骤 27A / 28A 末尾追加"状态回写" | 0.5 天 | 详细设计 |
| T-3 | `code-it` SKILL.md §"缺陷分支" 步骤 21 末尾追加"状态回写:开发中" | 0.5 天 | 详细设计 |
| T-4 | `code-it` SKILL.md §"缺陷分支" 步骤 24 末尾追加"状态回写:待审查" | 0.5 天 | 详细设计 |
| T-5 | `code-check` SKILL.md 步骤 1 入口增加"BUG-NNN 识别" + 步骤 13 状态回写 | 1 天 | 详细设计 |
| T-6 | `code-dashboard` SKILL.md 步骤 4 段 3 扩展"待修复 / 已修复"分类规则 | 0.5 天 | 详细设计 |
| T-7 | 端到端验证(AC-1 ~ AC-10) + 末尾兜底提交 | 1 天 | 详细设计 |

**合计**:约 5-6 天工作量(7 个任务)

### 12.2 任务实施顺序

- T-1 → T-2 → T-3 → T-4 → T-5 → T-6 → T-7(顺序依赖:T-2 / T-3 / T-4 / T-5 都依赖 T-1 的状态字段约定;T-7 验证全部 6 个任务)

### 12.3 实施关键约束

- **不修改 frontmatter**(沿用 C-2 / `skill-conventions §规则 1`)
- **不重排"## 工作流程"既有小节**(沿用 C-3)
- **不引入开发痕迹**(沿用 `skill-conventions §规则 2`)
- **每次 commit 沿用既有 `chore(code-<技能>):` 模式**(沿用 `commit-conventions §规则 1` 占位)
- **不触发 `AskUserQuestion`**(沿用 `code-plan` NFR-3;在实施细节上 AI 自主判断)

## 13. 关联

- 上游需求:`./assistants/V0.0.3/require/REQ-00037/RESULT.md`
- 上游概要设计:`./assistants/V0.0.3/design/REQ-00037/RESULT.md`
- 关联设计:REQ-00027 / REQ-00022 / REQ-00034 / REQ-00036(详见 `materials-index.md`)

## 14. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 09:28 | v1 | 初始创建 | 完成首次详细设计;6 模块详细化 + 7 关键变更 + 5 伪代码算法;`--balanced` + 功能性=高 + 健壮性=高 + 可维护性=高 | 用户 |