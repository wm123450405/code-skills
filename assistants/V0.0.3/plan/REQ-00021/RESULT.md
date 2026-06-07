# 详细设计 — REQ-00021(优化 3 技能 --result / --plan 模板参数,按用户模板格式输出填充后文档)

- 需求编码:REQ-00021
- 所属版本:V0.0.3
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06
- 最近更新:2026-06-07
- 当前版本:v1
- **上游需求**:`./assistants/V0.0.3/require/REQ-00021/RESULT.md`(v1,2026-06-06 17:00)
- **上游概要设计**:`./assistants/V0.0.3/design/REQ-00021/RESULT.md`(v1,2026-06-06 17:50)
- **遵循规范**:`./assistants/rules/` 下 13 个文件(本需求实际触发 9 个)
- **架构对象**:`code-skills` 仓库**自身**的 3 个 `code-*` 技能 SKILL.md(`code-require` / `code-design` / `code-plan`)+ 4 个模板产出物(REQUIRE / DESGIN × 2 / PLAN)

---

## 设计目标

> 本小节由 `code-plan` 步骤 0b 写入,沿用上游 `design/.../RESULT.md` 的设计目标。

- **回写时间**:2026-06-07
- **回写触发**:`code-plan` 步骤 0b(`code-auto` 上下文 NOT_DETECTED → 沿用 design 决策,不重新问)
- **整体目标**:`--extensible`(沿用上游概设;用户手动调,采纳 `--extensible` 拓展)
- **7 维度优先级**(本需求细化):

| 维度 | 优先级 | 依据 |
| --- | --- | --- |
| **功能性** | 高 | 沿用 design 决策;覆盖 FR-1 ~ FR-7 + 30 AC + 9 INV |
| **扩展性** | 高 | `--extensible` 目标:为后续二进制 follow-up 预留 CLI 接口 |
| **健壮性** | 中 | 模板文件不存在/二进制/路径穿越/通配符 4 种异常均降级处理 |
| **可维护性** | 中 | 15 个内置占位符的中央映射表,3 技能共用 |
| **封装性** | 不适用 | 模板填充逻辑是单文件函数,无重复代码;沿用既有 |
| **可复用性** | 高 | `code-require` / `code-design` 3 占位符子集 + `code-plan` 2 段占位符子集共用同一映射表 |
| **可读性** | 中 | 占位符风格 `{{...}}` 一目了然;屏显契约清晰 |

### 设计目标对本设计的影响(AC-4 沿用 + 扩展)

- 整体=`--extensible` + 扩展性=高 → 任务粒度:加"占位符扩展机制"任务(预留 `--map` / `--vars` / `--script` 扩展点)
- 整体=`--extensible` + 可复用性=高 → 任务粒度:加"占位符映射表中央化"任务(3 技能共用)
- **用户授权偏离 NFR-5.1**:SKILL.md 行数变化 -5% ~ +15% → 实际 +20% ~ +30%(沿用 design 决策,rule-compliance.md §4 记录)

---

## 1. 详细设计概述

本详细设计在概要设计的基础上,把"3 技能新增 CLI 参数 + 模板填充步骤"细化为**可直接编码的算法 / 接口 / 任务**。本需求是**回填式详细设计**(`code-require` 阶段已落 3 个 SKILL.md 实际修改 `d6be243`,`code-design` 阶段已落概要设计 `aaa63b4`),本步骤任务是"事后归档"详细设计意图,作为下游 `code-it` 任务的"已落地"参考。

**关键决策**(N=7,沿用 design 概设):
- D-1 参数解析锚点:工具使用约定段后 + 工作流程前
- D-2 模板填充锚点:末尾不要做的事前
- D-3 DESGIN 拼写:沿用用户原文(不纠正)
- D-4 二进制降级:屏显 `⚠ 跳过` 不报错
- D-5 路径安全:不允许 `../` 跳出
- D-6 屏显格式:3 段 `=== <技能名> 模板填充 ===`
- D-7 行数影响:接受 +20% ~ +30%(用户授权偏离 NFR-5.1)

**算法核心**:模板填充算法(FR-2 核心);**接口核心**:4 个 CLI 参数;**数据结构核心**:15 个内置占位符。

---

## 2. 上游引用

### 2.1 上游需求
- `./assistants/V0.0.3/require/REQ-00021/RESULT.md`(v1)
- 关键摘录:**7 FR / 6 NFR / ~30 AC / 9 INV**
- 关键交叉点:
  - FR-1(参数解析)→ §3.1 CLI 参数接口
  - FR-2(模板填充)→ §4 模板填充算法
  - FR-3(二进制限制)→ §5.4 二进制格式降级
  - FR-4(屏显 + 看板)→ §4.2 屏显格式契约
  - FR-5(0 改其他 10 技能)→ §6 模块(INV-7 锁定)
  - FR-6(0 改 marketplace / 规范)→ §6 模块(INV-5 锁定)
  - FR-7(不变量)→ §6.3 INV 列表

### 2.2 上游概要设计
- `./assistants/V0.0.3/design/REQ-00021/RESULT.md`(v1)
- 关键摘录:**6 决策(D-1 ~ D-6) + 9 不变量(INV-1 ~ INV-9) + 字面量替换矩阵(已识别)**

### 2.3 规范引用(本需求实际触发 9 个,详 design/.../rule-compliance.md §1)
- `skill-conventions §规则 1`(FR-1 触发)
- `dashboard-conventions §规则 1`(INV-4 锁定 0 触发)
- `encoding-conventions §规则 1/3`(INV-6 锁定 0 触发)
- `marketplace-protocol §规则 1`(本需求 0 触发,无 marketplace 修改)
- `module-conventions §规则 1`(沿用)
- `commit-conventions`(末步提交沿用)
- `doc-conventions §规则 1`(本需求 0 触发,无 README 修改)
- `naming-conventions`(基本名 `REQUIRE` / `DESGIN` / `PLAN` 用户原文锁定)
- `dependency-conventions`(NFR-2.8 0 触发,二进制 follow-up 留作)

---

## 3. 模块详细化(对应概要设计 §3)

### 模块 1:`code-require` 技能(对应 FR-1 + FR-2)

#### 关键操作
- **步骤 0 之前**(新增小节"## 命令行参数解析"):
  - `Read` 用户输入 → 解析 `--result <路径>`
  - 校验模板文件存在性:不存在 → 屏显 `⚠ 模板文件不存在:<路径>`,跳过
  - 校验路径安全性:含 `../` → 屏显 `⚠ 模板路径不安全`,跳过
  - 校验路径通配符:`*.docx` → 屏显 `⚠ 模板路径不支持通配符`,跳过
  - 校验二进制格式:`.docx` / `.xlsx` / `.pdf` → 屏显 `⚠ 模板格式二进制,跳过填充`
  - 校验文件大小:> 1MB → 屏显 `⚠ 过大`,继续
  - 记录到 `analysis-notes.md` "## 命令行参数"节
- **主产出物完成后**(新增小节"## 模板填充步骤"):
  - `Read` 模板文件
  - 扫描 `{{...}}` 占位符
  - 从 `RESULT.md` 提取 8 类数据(REQ_ID / REQ_TITLE / 需求概述 / FR_LIST / NFR_LIST / AC_LIST / 关联需求 / 待澄清)
  - 按 15 个内置占位符映射表替换
  - `Write` 模板产出物 `REQUIRE.<ext>`(同目录)
  - 屏显 3 段格式:`=== code-require 模板填充 ===`
  - 在 `analysis-notes.md` 追加"模板填充结果"节

#### 关键决策
- **不动既有"## 工作流程"小节**(INV-2)
- **不修改 frontmatter**(INV-1)
- **不修改既有"## 衔接" + "## 不要做的事" 段**(INV-3)
- **不动其他 9 个 SKILL.md**(INV-7)

#### 错误处理
- `Read` 失败 → 透传 stderr,中断退出
- `Write` 失败 → 透传 stderr,中断退出

#### 依据规范
- `skill-conventions §规则 1` + `dashboard-conventions §规则 1`(INV-4) + `doc-conventions`(NFR-2.6)

### 模块 2:`code-design` 技能(对应 FR-1 + FR-2)

同模块 1,差异点:
- 模板产出物:`DESGIN.<ext>`(用户原文拼写,沿用)
- 占位符子集:`code-design` 用 4 个(`设计概述` / `模块列表` / `接口列表` / `数据结构`)
- 数据源:`design/.../RESULT.md`(模块拆分 / 接口概要 / 数据结构概要)
- 屏显:同 3 段格式

### 模块 3:`code-plan` 技能(对应 FR-1 + FR-2,2 段填充)

同模块 1,差异点:
- 2 个 CLI 参数:`--result` + `--plan`
- 2 个模板产出物:`DESGIN.<ext>`(详设) + `PLAN.<ext>`(开发计划)
- 占位符子集:`code-plan --result` 用 4 个(`设计概述` / `模块列表` / `接口列表` / `数据结构`);`code-plan --plan` 用 3 个(`任务列表` / `依赖图` / `里程碑`)
- 数据源:`plan/.../RESULT.md` + `plan/.../PLAN.md`
- 屏显:同 3 段格式(2 段屏显,各占 1 行)
- BUG 路径:模板填充对 BUG 路径同样生效,输出目录为 `fix/<BUG-NNN>/` 而非 `plan/<REQ>/`(沿用 REQ-00019)

### 模块 4:占位符映射表(中央化,FR-2 内核)

- **15 个内置占位符**,跨 3 技能共用
- 分配:
  - `code-require` 用 8 个:REQ_ID / REQ_TITLE / 需求概述 / FR_LIST / NFR_LIST / AC_LIST / 关联需求 / 待澄清
  - `code-design` / `code-plan --result` 用 4 个:设计概述 / 模块列表 / 接口列表 / 数据结构
  - `code-plan --plan` 用 3 个:任务列表 / 依赖图 / 里程碑
- 编码:`{{...}}` 风格(双花括号)
- 模板中未在表中的占位符**不**替换(保留原样输出)

---

## 4. 算法与逻辑(本需求核心)

### 算法 1:模板填充算法(FR-2 核心)

```
function fillTemplate(templatePath, outputPath, sourceData):
  # 1. 读取模板
  if not exists(templatePath):
    log("⚠ 模板文件不存在,跳过")
    return

  if isBinaryFormat(templatePath):
    log("⚠ 模板格式二进制,跳过")
    return

  template = read(templatePath)  # 字符串

  # 2. 提取占位符
  placeholders = scanPlaceholders(template)  # {{...}} 风格
  if placeholders is empty:
    # 模板无占位符 → 追加源数据
    output = template + "\n\n---\n\n" + sourceData
    write(outputPath, output)
    log(f"模板无占位符,追加源数据 → {outputPath}")
    return

  # 3. 替换占位符
  filled = template
  filledCount = 0
  unfilledList = []
  for ph in placeholders:
    phKey = ph.strip("{{}}").strip()
    if phKey in PLACEHOLDER_MAP:
      filled = filled.replace(ph, PLACEHOLDER_MAP[phKey])
      filledCount++
    else:
      unfilledList.append(ph)

  # 4. 写出
  write(outputPath, filled)
  log(f"模板填充完成:{filledCount}/{len(placeholders)} 个占位符已替换")
  if unfilledList:
    log(f"⚠ 未识别的占位符:{unfilledList}")
```

**复杂度**:时间 O(N*M)(N = 占位符数,M = 模板长度);空间 O(M)(字符串复制)
**依赖**:本地 Read / Write 工具;无外部依赖
**关键决策**:
- 用字符串 `replace` 而非正则(简单直接)
- 占位符未识别**保留原样**(用户可手动补)
- 模板无占位符 → 把源数据追加到模板后(E-5 边界)

### 算法 2:CLI 参数解析(FR-1 核心)

```
function parseArgs(args):
  result = { --result: null, --plan: null }
  for i in 0..len(args):
    if args[i] == '--result':
      if i+1 >= len(args):
        log("⚠ --result 缺模板文件路径,跳过")
        result['--result'] = SKIP
      else:
        result['--result'] = args[i+1]
    elif args[i] == '--plan':
      if i+1 >= len(args):
        log("⚠ --plan 缺模板文件路径,跳过")
        result['--plan'] = SKIP
      else:
        result['--plan'] = args[i+1]
  return result
```

**复杂度**:时间 O(N);空间 O(1)
**关键决策**:
- 取最后一个值(用户传 2 次时后者覆盖前者)
- 缺值 → 屏显跳过,**不**报错
- 通配符 / `../` 跳出 / 二进制格式 → 屏显跳过,**不**报错(INV-9 + NFR-3.2)

### 算法 3:占位符提取(`{{...}}` 风格)

```
function scanPlaceholders(template):
  matches = regex.findall(r"\{\{[^}]+\}\}", template)
  return unique(matches)
```

**关键决策**:
- 正则非贪婪(`\{\{[^}]+\}\}`)
- 去重(同一占位符多次出现只算 1 个)
- 占位符 key = `strip("{{}}").strip()`

### 算法 4:占位符映射表(中央化)

```
PLACEHOLDER_MAP = {
  "REQ_ID": ...,        # code-require
  "REQ_TITLE": ...,     # code-require
  "需求概述": ...,      # code-require
  "FR_LIST": ...,       # code-require
  "NFR_LIST": ...,      # code-require
  "AC_LIST": ...,       # code-require
  "关联需求": ...,      # code-require
  "待澄清": ...,        # code-require
  "设计概述": ...,      # code-design / code-plan
  "模块列表": ...,      # code-design / code-plan
  "接口列表": ...,      # code-design / code-plan
  "数据结构": ...,      # code-design / code-plan
  "任务列表": ...,      # code-plan --plan
  "依赖图": ...,        # code-plan --plan
  "里程碑": ...,        # code-plan --plan
}
```

**关键决策**:
- 中央化(3 技能共用同一映射表,便于维护)
- 占位符 key **完全**为中文(沿用本仓库中文约定,符合 `naming-conventions` 用户原文锁定)

---

## 5. 数据结构完整变更(本需求 0 新增实体)

### 5.1 新增实体
- (无)本需求**0**新增实体

### 5.2 修改实体
- (无)本需求**0**修改实体

### 5.3 数据迁移
- (无)本需求**0**数据迁移

### 5.4 数据产出物结构(伪代码)

```ts
type TemplateOutput = {
  skillName: "code-require" | "code-design" | "code-plan",
  templatePath: string,          // 模板源文件
  outputPath: string,            // 输出文件 = 主产出物同目录 + <BASENAME>.<ext>
  basename: "REQUIRE" | "DESGIN" | "PLAN",
  ext: string,                   // 后缀 = 模板后缀
  filledCount: number,           // 已替换占位符数
  unfilledList: string[],        // 未识别占位符列表(原样保留)
  source: {
    // code-require 用
    reqId?: string,              // REQ-00021
    reqTitle?: string,           // 需求标题
    reqSummary?: string,         // 需求概述
    frList?: string,             // FR 列表(Markdown 表格或列表)
    nfrList?: string,            // NFR 列表
    acList?: string,             // AC 列表
    relatedReqs?: string,        // 关联需求列表
    pendingItems?: string,       // 待澄清项
    // code-design / code-plan --result 用
    designSummary?: string,      // 设计概述
    moduleList?: string,         // 模块列表
    interfaceList?: string,      // 接口列表
    dataStructure?: string,      // 数据结构
    // code-plan --plan 用
    taskList?: string,           // 任务列表
    depGraph?: string,           // 依赖图(Mermaid)
    milestones?: string,         // 里程碑列表
  }
}
```

---

## 6. 接口细节(对应概要设计 §4)

### 6.1 CLI 参数(本需求 4 个,跨 3 技能)

| 技能 | 参数 | 性质 | 模板产出物 | 备注 |
| --- | --- | --- | --- | --- |
| `code-require` | `--result <模板文件>` | 可选 | `REQUIRE.<ext>` | 后缀 = 模板后缀 |
| `code-design` | `--result <模板文件>` | 可选 | `DESGIN.<ext>` | 用户原文拼写 |
| `code-plan` | `--result <模板文件>` | 可选 | `DESGIN.<ext>` | 详设 |
| `code-plan` | `--plan <模板文件>` | 可选 | `PLAN.<ext>` | 开发计划 |

### 6.2 屏显格式契约(沿用 REQ-00013 NFR-4.1)

**完成时屏显**:
```
=== <code-require / code-design / code-plan> 模板填充 ===
  模板:<模板文件路径>
  输出:<输出文件路径>(<N> 个占位符已替换)
```

**code-plan 2 段屏显**:
```
=== code-plan 模板填充 ===
  详细设计:<DESGIN.xlsx>(<N1> 个占位符已替换)
  开发计划:<PLAN.xlsx>(<N2> 个占位符已替换)
```

### 6.3 模板产出物路径(输出契约)

| 技能 | 参数 | 输出文件名 | 输出路径 |
| --- | --- | --- | --- |
| `code-require` | `--result` | `REQUIRE.<ext>` | `./assistants/<版本号>/require/<需求编码>/REQUIRE.<ext>` |
| `code-design` | `--result` | `DESGIN.<ext>` | `./assistants/<版本号>/design/<需求编码>/DESGIN.<ext>` |
| `code-plan` | `--result` | `DESGIN.<ext>` | `./assistants/<版本号>/plan/<需求编码>/DESGIN.<ext>` |
| `code-plan` | `--plan` | `PLAN.<ext>` | `./assistants/<版本号>/plan/<需求编码>/PLAN.<ext>` |

### 6.4 模板支持格式(本需求实现范围)

| 格式 | 支持 | 实现方式 |
| --- | --- | --- |
| `.md` | ✅ | 字符串替换 + Write |
| `.html` | ✅ | 字符串替换 + Write |
| `.txt` | ✅ | 字符串替换 + Write |
| `.json` | ✅ | 字符串替换 + Write |
| `.xml` | ✅ | 字符串替换 + Write |
| `.csv` | ✅ | 字符串替换 + Write |
| `.yaml` / `.yml` | ✅ | 字符串替换 + Write |
| `.docx` / `.xlsx` / `.pptx` | ❌(本需求) | 屏显 `⚠ 跳过`,follow-up |
| `.pdf` | ❌(本需求) | 屏显 `⚠ 跳过`,follow-up |

---

## 7. 异常处理 / 安全 / 状态机

### 7.1 异常处理(本需求 11 条 E-边界)

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | `--result` / `--plan` 缺值 | 屏显 `⚠ 缺模板文件路径`,跳过 |
| **E-2** | 路径含通配符 | 屏显 `⚠ 模板路径不支持通配符`,跳过 |
| **E-3** | 无 `.current-version` | 沿用既有(提示调 `code-version`) |
| **E-5** | 模板无占位符 | 把 `RESULT.md` 完整内容追加到模板 |
| **E-6** | 占位符未识别 | 已识别的替换,未识别的保留原样 |
| **E-7** | 二进制格式模板 | 屏显 `⚠ 跳过`,不报错 |
| **E-8** | 模板文件 > 1MB | 屏显 `⚠ 过大`,继续 |
| **E-9** | 模板路径 `../` 跳出工作空间 | 屏显 `⚠ 模板路径不安全`,跳过 |
| **E-10** | `--result` / `--plan` 与 `code-auto` 协同 | `code-auto` 不传(沿用 REQ-00007 Q-4) |
| **E-11** | 多次执行(`--result` 模板相同) | 输出文件**覆盖**(幂等) |
| **E-12** | `--result` / `--plan` 同时传 | 独立处理(各占 1 行屏显) |

### 7.2 安全

- **NFR-6.1**:模板路径校验(防止路径穿越 — 不允许 `../` 跳出工作空间)
- **NFR-6.2**:模板文件大小限制(1MB;过大屏显 `⚠` 但继续)
- **NFR-6.3**:`--result` / `--plan` **不**写工作空间外文件(输出路径前缀必须 `./assistants/<版本号>/...`)

### 7.3 状态机

- 沿用既有"## 工作流程"状态机(本需求**不**引入新状态)
- 模板填充是**附加步骤**,不修改 3 技能既有状态机
- 流程:主产出物 → 模板填充 → 看板同步 → 末尾兜底提交(NFR-3.4 顺序保证)

### 7.4 性能 / 资源

- 模板填充耗时 < 5 秒(可文本化格式,1MB 以内)(NFR-1)
- 屏显新增 1-2 行,**不**影响整体性能
- BUG 路径:`code-plan` BUG 模式模板填充输出目录为 `fix/<BUG-NNN>/` 而非 `plan/<REQ>/`(沿用 REQ-00019)

---

## 8. 测试要点

- **AC-1.x**:3 技能 `--result` / `--plan` 参数解析(5 条)
- **AC-2.x**:模板填充(8 条)
- **AC-3.x**:二进制格式限制(3 条)
- **AC-4.x**:屏显 + 看板(3 条)
- **AC-5.x**:0 改其他 10 技能(3 条)
- **AC-6.x**:0 改 marketplace / plugin / 规范(4 条)
- **INV-1 ~ INV-9**:9 条不变量自检

---

## 9. 关联编码计划

`./assistants/V0.0.3/plan/REQ-00021/PLAN.md` 中本详细设计对应的所有任务编号 + 关键任务与本节设计的对应关系(详 PLAN.md)。

---

## 10. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本需求**0**待澄清;7 决策 + 9 不变量 + 7 FR / 6 NFR / ~30 AC / 9 INV 全部已锁定;5 项澄清全部已落(`clarifications.md`);1 项用户授权偏离(NFR-5.1 SKILL.md 行数增长 +20% ~ +30%) | 0 待澄清 |

---

## 11. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-07 | v1 | 初始创建 | 完成首次详细设计:7 决策(D-1 ~ D-7)+ 9 不变量(INV-1 ~ INV-9)+ 7 FR / 6 NFR / ~30 AC / 9 INV 全部锁定;整体=`--extensible` + 7 维度优先级已确认(功能性=高,扩展性=高,可复用性=高,健壮性=中,可维护性=中,可读性=中,封装性=不适用);0 触发 `dashboard-conventions §规则 1` 三同步;0 派生"更新看板"任务(沿用 REQ-00017 强约束);**回填式详细设计**(SKILL.md 已落地 `d6be243` + 概设已落 `aaa63b4`) | wangmiao |
