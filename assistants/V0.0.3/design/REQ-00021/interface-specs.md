# 接口与数据结构 — REQ-00021

更新时间:2026-06-06 17:25
版本:V0.0.3

## 1. 接口(本需求新增 CLI 参数 + 模板填充屏显协议)

### 1.1 新增 CLI 参数(本需求 4 个,跨 3 技能)

| 技能 | 参数 | 性质 | 取值 | 模板产出物 | 备注 |
| --- | --- | --- | --- | --- | --- |
| `code-require` | `--result <模板文件>` | 可选 | 路径字符串 | `REQUIRE.<ext>` | 后缀 = 模板后缀 |
| `code-design` | `--result <模板文件>` | 可选 | 路径字符串 | `DESGIN.<ext>` | 用户原文拼写(沿用) |
| `code-plan` | `--result <模板文件>` | 可选 | 路径字符串 | `DESGIN.<ext>` | 详设,DESGIN 拼写沿用 |
| `code-plan` | `--plan <模板文件>` | 可选 | 路径字符串 | `PLAN.<ext>` | 开发计划 |

**参数解析契约**:
- 解析位置:技能启动时(步骤 0a 拉取**前**)
- 优先级:取最后一个值(用户传 2 次时后者覆盖前者)
- 缺值(只写 `--result` 不写路径)→ 屏显 `⚠ --result 缺模板文件路径`,跳过填充
- 路径含通配符(`*.docx`)→ 屏显 `⚠ 模板路径不支持通配符`,跳过填充
- 路径含 `../` 跳出工作空间 → 屏显 `⚠ 模板路径不安全`,跳过填充
- 路径不存在 → 屏显 `⚠ 模板文件不存在:<路径>`,跳过填充
- 路径为二进制格式(.docx/.xlsx/.pdf/.pptx)→ 屏显 `⚠ 模板格式二进制,跳过填充`,不报错
- 路径 > 1MB → 屏显 `⚠ 模板文件过大(>1MB)`,继续
- `code-auto` 上下文:`code-auto` **不**传 `--result` / `--plan`(沿用 REQ-00007 Q-4 + E-4)

### 1.2 模板填充屏显协议

**完成时屏显**(沿用 REQ-00013 标题解析风格):

```
=== <code-require / code-design / code-plan> 模板填充 ===
  模板:<模板文件路径>
  输出:<输出文件路径>(<N> 个占位符已替换)
```

**跳过时屏显**(任一边界触发):

```
⚠ 模板文件不存在:<路径>,跳过
⚠ --result 缺模板文件路径,跳过
⚠ 模板路径不支持通配符,跳过
⚠ 模板路径不安全,跳过
⚠ 模板格式二进制,跳过填充
⚠ 模板文件过大(>1MB),可能影响性能
```

**code-plan 2 段屏显**(同时传 `--result` + `--plan`):

```
=== code-plan 模板填充 ===
  详细设计:<DESGIN.xlsx>(<N1> 个占位符已替换)
  开发计划:<PLAN.xlsx>(<N2> 个占位符已替换)
```

### 1.3 模板产出物路径(输出契约)

| 技能 | 参数 | 输出文件名 | 输出路径 |
| --- | --- | --- | --- |
| `code-require` | `--result` | `REQUIRE.<ext>` | `./assistants/<版本号>/require/<需求编码>/REQUIRE.<ext>` |
| `code-design` | `--result` | `DESGIN.<ext>` | `./assistants/<版本号>/design/<需求编码>/DESGIN.<ext>` |
| `code-plan` | `--result` | `DESGIN.<ext>` | `./assistants/<版本号>/plan/<需求编码>/DESGIN.<ext>` |
| `code-plan` | `--plan` | `PLAN.<ext>` | `./assistants/<版本号>/plan/<需求编码>/PLAN.<ext>` |

**注**:同版本同需求下,`code-design` 的 `DESGIN.<ext>` 与 `code-plan` 的 `DESGIN.<ext>` **不**冲突(路径不同)

### 1.4 模板文件支持格式(本需求实现范围)

| 格式 | 支持 | 实现方式 |
| --- | --- | --- |
| `.md` | ✅ | 字符串替换 + Write |
| `.html` | ✅ | 字符串替换 + Write |
| `.txt` | ✅ | 字符串替换 + Write |
| `.json` | ✅ | 字符串替换 + Write(注:JSON 模板中 `{{...}}` 需在 JSON 字符串内,如 `"{{REQ_ID}}"`) |
| `.xml` | ✅ | 字符串替换 + Write |
| `.csv` | ✅ | 字符串替换 + Write |
| `.yaml` / `.yml` | ✅ | 字符串替换 + Write |
| `.docx` / `.xlsx` / `.pptx` | ❌(本需求) | 屏显 `⚠ 跳过`,follow-up |
| `.pdf` | ❌(本需求) | 屏显 `⚠ 跳过`,follow-up |

### 1.5 调用外部接口(本需求 0)

- 本需求**0**调用外部 API / 外部系统 / 外部脚本
- 屏显 0 个 + 文件 I/O 全部为本地 Read/Write 工具

## 2. 数据结构(本需求新增 1 类:占位符映射表)

### 2.1 占位符映射表(本需求内置 15 个,跨 3 技能)

| 占位符 | 来源 | 适用技能 |
| --- | --- | --- |
| `{{REQ_ID}}` | `require/.../RESULT.md` 文档头 | code-require |
| `{{REQ_TITLE}}` | `require/.../RESULT.md` 文档头 | code-require |
| `{{需求概述}}` | `require/.../RESULT.md` §1 | code-require |
| `{{FR_LIST}}` | `require/.../RESULT.md` §4 | code-require |
| `{{NFR_LIST}}` | `require/.../RESULT.md` §5 | code-require |
| `{{AC_LIST}}` | `require/.../RESULT.md` §10 | code-require |
| `{{关联需求}}` | `require/.../RESULT.md` §11 | code-require |
| `{{待澄清}}` | `require/.../RESULT.md` §12 | code-require |
| `{{设计概述}}` | `design/.../RESULT.md` §1 | code-design / code-plan |
| `{{模块列表}}` | `design/.../RESULT.md` §模块拆分 | code-design / code-plan |
| `{{接口列表}}` | `design/.../RESULT.md` §接口 | code-design / code-plan |
| `{{数据结构}}` | `design/.../RESULT.md` §数据结构 | code-design / code-plan |
| `{{任务列表}}` | `plan/.../PLAN.md` §任务总览 | code-plan |
| `{{依赖图}}` | `plan/.../PLAN.md` §任务依赖图 | code-plan |
| `{{里程碑}}` | `plan/.../PLAN.md` §里程碑 | code-plan |

**数据契约**:
- 占位符风格:`{{...}}`(双花括号)
- 模板中未在表中的占位符**不**替换(保留原样输出,便于用户手动补)
- code-require 用其中 8 个;code-design 用其中 4 个;code-plan 用其中 7 个(2 段:详设 4 + 开发计划 3)

### 2.2 模板产出物文件结构(伪代码)

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

### 2.3 模板填充算法(伪代码,FR-2 核心)

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

### 2.4 数据迁移(本需求 0)

- 本需求**0** 涉及数据库迁移 / 数据结构迁移
- 模板产出物是**新文件**,不修改既有 `RESULT.md` / `PLAN.md`

## 3. 接口与数据结构的自检

### 3.1 对照 `naming-conventions.md`(本需求 `规则 1` 待添加,本概设引用既有)

- ✅ 基本名 `REQUIRE` / `DESGIN` / `PLAN` 用户原文锁定(NFR-2.7)
- ✅ 文件名 kebab-case 沿用既有(`<basename>.<ext>` 单一文件名)
- ✅ 0 新增文件名前缀

### 3.2 对照 `module-conventions.md §规则 1`(已迁移到 `directory-conventions.md`)

- ✅ 模板产出物放在原主产出物同目录
- ✅ 0 新增子目录
- ✅ 0 改变既有目录结构

### 3.3 对照 `skill-conventions.md §规则 1`

- ✅ 模板产出物**不**是技能,**不**触发 frontmatter 约束
- ✅ 模板产出物**不**进 `skills/` 目录,放在 `assistants/<version>/<子目录>/<REQ>/`
