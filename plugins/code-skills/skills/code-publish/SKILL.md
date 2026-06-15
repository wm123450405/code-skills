---
name: code-publish
description: 发布部署(版本感知)。要求用户提供可选位置参数"版本号"(缺省时取 `./assistants/.current-version`);先做发布前置检查(全检查最严:需求状态=已完成 ∧ 任务 开发状态=已完成 ∧ 测试状态∈{已运行-通过, 不适用} ∧ 缺陷状态=已修复);通过后在 `./assistants/<版本号>/publish/` 下生成 `DEPLOY.md`(全新部署,始终生成) + `UPDATE.md`(从上一版升级,基线版本跳过) + `Q&A.md`(从 `assistants/qanda/` 聚合,空时为占位);3 份手册均为"通用发布部署骨架 + 最常见部署方式默认示例 + placeholder",用户**必须**手动补全 `<本版本号>` 之外的占位符才能按手册执行;本技能顺带在项目级创建 `assistants/qanda/` 目录与 `README.md`(供长期 Q&A 沉淀)。本技能**纯只读消费看板 + 不自动 commit + 不参与 REQ-00005 的"首步拉取+末步提交"**;在 `code-check` 完成后,长开发周期末使用;基线版本可直接调用归档。
---

# code-publish — 发布部署(版本感知)

## 目标

为 `code-skills` 6 个开发周期技能(`code-version` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-check`)补足"开发完成 → 部署上线"这**最后一步**:调用一次,即可知道"本版本是否可发布",并在通过时自动产出 3 份(基线版本 2 份)通用的发布/升级/Q&A 手册骨架到 `publish/`,供运维 / 现场支持按手册执行。**纯只读检查 + 不自动提交 + 通用性优先**(本仓库不绑定具体被发布的"软件",手册留给用户补全)。

## 适用场景

- 长开发周期末,准备将本版本发布到生产环境
- 多个并行版本中,需要归档发布某个历史版本
- 运维 / 部署工程师需要 3 份"按步骤可执行"的手册
- 现场支持需要 Q&A 手册查阅常见问题
- 基线版本(V0.0.0 或项目最初版本)需要单独发布并跳过"从上一版升级"

## 不适用

- 当前**没有激活的版本工作空间**(请先调 `code-version`)
- 需求/任务/缺陷**有未解决项**;必须先解决后才能调本技能
- 紧急线上修复(走 hotfix 流程)
- 实际"执行"部署(本技能只生成"步骤手册",不执行 SSH / Docker / SQL 等命令)
- `--force` 强制发布:v1 不实现(留作 v2)
- 由 `code-auto` 驱动:`code-auto` 仅驱动开发 6 技能,不调本技能;用户在 `code-auto` 完成后手动调

## 工作目录约定(强制)

**版本工作空间**:`./assistants/<版本号>/`(由 `./assistants/.current-version` 决定,本技能允许位置参数覆盖)。
本技能的目录粒度是**版本**(不像其他 7 技能按"需求")。

```
./assistants/
├── rules/                              # 项目级规范(跨版本共享,本技能只读)
├── qanda/                              # 项目级 Q&A 长期沉淀(本技能顺带创建,跨版本共享)
│   ├── README.md                       # 目录用途说明(本技能首次创建)
│   └── (用户后续添加的 Q&A .md 文件)
├── .current-version                    # 当前激活版本标记(本技能读)
└── <版本号>/
    ├── RESULT.md                       # 版本看板(本技能只读消费 3 区段)
    ├── ...
    └── publish/                        # 本技能产出(可写)
        ├── DEPLOY.md                   # 全新部署手册骨架(始终生成)
        ├── UPDATE.md                   # 升级部署手册骨架(基线版本跳过)
        └── Q&A.md                      # Q&A 手册(从 qanda/ 聚合)
```

- 路径以**当前工作目录(CWD)**为基准
- `rules/` **不**在版本下,跨版本共享,本技能**只读**
- `qanda/` **不**在版本下,跨版本共享;本技能首次调用时**顺带创建** + 写入 `README.md`(本需求顺带产物)
- `.current-version` 由 `code-version` 写入;本技能**只读**(不切换版本)
- `publish/` 在本技能首次调用时由 `mkdir -p` 创建
- 本技能**不修改** `./assistants/rules/` 下任何文件(FR-8.AC-8.3)
- 本技能**不修改** `<版本号>/RESULT.md`(NFR-2 纯只读)
- 本技能**不修改** `./assistants/<其他版本号>/` 下任何文件

## 输入

- **位置参数**(可选):版本号字符串,如 `V0.0.2` / `V0.0.0`(基线)
  - 缺省时:从 `./assistants/.current-version` 读取
  - 校验:不允许含 `/` / `\` / `..`(防路径穿越)
- **上游版本看板**:`./assistants/<版本号>/RESULT.md`(必须存在,否则提示用户确认版本号或先 `code-version`)
- **项目级 Q&A**:`./assistants/qanda/*.md`(可选;本技能首次调用时若无此目录则顺带创建)
- **模板**(本技能自带,在同技能 `templates/` 子目录):
  - `<本仓库>/skills/code-publish/templates/DEPLOY.md`
  - `<本仓库>/skills/code-publish/templates/UPDATE.md`
  - `<本仓库>/skills/code-publish/templates/Q&A.md`
  - `<本仓库>/skills/code-publish/templates/qanda-README.md`
  - `<本仓库>/skills/code-publish/templates/assistants-layout.md`

## 输出

主产出物:
- `./assistants/<版本号>/publish/DEPLOY.md`(**始终生成**)
- `./assistants/<版本号>/publish/UPDATE.md`(**仅当本版本非基线**)
- `./assistants/<版本号>/publish/Q&A.md`(**始终生成**)
- 顺带:`./assistants/qanda/README.md`(仅当本技能首次调用且 `qanda/` 不存在)

辅助过程文档:无(技能本身的"日志"=用户终端报告;3 份手册是交付物)

**版本看板同步**:本技能**不修改**版本看板(纯只读消费 3 区段;不追加任何区段;`dashboard-conventions.md §规则 1` 0 触发)。

## 工具使用约定

- 读激活版本:`Read "./assistants/.current-version"`(仅当无位置参数)
- 读版本看板:`Read "./assistants/<版本号>/RESULT.md"`(整文件读取)
- 列版本目录:`Glob "./assistants/*/"`(基线识别)
- 列 qanda 内容:`Glob "./assistants/qanda/*.md"`(Q&A 聚合)
- 建目录:`Bash: mkdir -p ...`
- 探测 publish/ 已有文件:`Bash: ls -1 .../publish/ 2>/dev/null | grep -E '\.md$'`
- 写文件:`Write ...`
- 与用户澄清:本技能**不**主动用 `AskUserQuestion`(行为已由需求锁定 Q-1~Q-4);仅在用户传非法版本号时报错

---

## 工作流程

本技能按"步骤 0 → 步骤 3"顺序执行;每步**独立可恢复**(若用户中断,重新调技能从步骤 0 重新走)。

### 步骤 0:版本上下文检测(强制前置)

> **目的**:确定本技能操作的"目标版本号"。

1. **解析位置参数**:
   - 若用户提供 `<版本号>` 参数(如 `/code-publish V0.0.2`)→ **使用该参数**为目标版本
   - 若用户未提供参数 → 读取 `./assistants/.current-version`:
     ```bash
     Read: ./assistants/.current-version
     ```
   - **校验**:版本号字符串不允许为空、不允许含 `/` / `\` / `..`(防路径穿越)
2. **验证版本工作空间**:
   ```bash
   Bash: ls -la ./assistants/<版本号>/RESULT.md
   ```
   - 不存在 → **报错退出**:
     > ✗ 版本 `<版本号>` 的看板不存在。请确认版本号(无参数时会自动取 `.current-version`),或先调 `/code-version <版本号>` 创建。
3. **进入步骤 1**

**异常路径**:
- E-5(无 `.current-version` ∧ 无参数):报错 + 提示调 `code-version` + 退出
- E-2-版本不存在(变体):如上"不存在"分支

### 步骤 1:发布前置检查(PreflightChecker)

> **目的**:解析 `<版本号>/RESULT.md` 的 3 大区段(需求清单 / 任务清单 / 缺陷清单),判定"是否全部已解决"。

> **判定规则**(Q-1 锁定 A — 全检查最严):
> - 需求:状态 = `已完成`(容忍后缀如"已完成(需求分析)")
> - 任务:开发状态 = `已完成` ∧ 测试状态 ∈ {`已运行-通过`, `不适用`}
> - 缺陷:状态 = `已修复`

#### 1.1 读取看板

```bash
Read: ./assistants/<版本号>/RESULT.md
```

#### 1.2 解析 3 区段(算法 1 — PreflightChecker)

对每个区段 `^## 需求清单` / `^## 任务清单` / `^## 缺陷清单`:

1. **定位区段**:提取从 `^## <区段名>$` 到下一个 `^## ` 之间的内容
2. **解析首行(列名行)**:取第一个 `| ... |` 起始的行 + 紧邻的 `|---|...|` 分隔行
   - 提取列名 → 列序号映射:`parse_header_row(section_text) → {列名: 列号}`
3. **解析数据行**:
   - 跳过 `|---|...|` 分隔行
   - 跳过 `**统计**:...` 段落
   - 对其他 `| ... |` 起始行:按列号 split `|` + trim,得到每行字段列表
4. **逐行判定**(算法 `is_resolved`):
   - 需求:`row[列名["状态"]]` startswith `已完成` → 解决
   - 任务:`row["开发状态"] == "已完成"` AND `row["测试状态"] ∈ {"已运行-通过", "不适用"}` → 解决
   - 缺陷:`row["状态"] == "已修复"` → 解决
5. **累积未完成项**:`{类型, 编码, 标题, 当前状态, 期望状态}`

**关键决策**(DD-2):**用列名识别而非列号位置**,这样未来即使看板新增列(如 `dashboard-conventions.md §规则 1` 触发的扩展),也不破坏本技能解析。

#### 1.3 退化处理

- **区段不存在**(看板被破坏)→ 该区段视为"全未解决"(不阻塞技能,继续累积 undone)
- **列名缺失**(看板表格缺少关键列如"状态")→ 该行视为"未解决"(保守判定)
- **空看板 / 0 数据行**→ 该区段 `0/0`(通过)

#### 1.4 决策

- `累积未完成项非空` → **不通过分支**(跳到步骤 3 输出失败报告,退出)
- `累积未完成项空` → **通过**,进入步骤 2.0

**异常路径**:
- E-1:不通过(打印未完成项明细 + 阻塞统计,不写手册,退出)
- E-2:看板缺区段(报告中显式标注"看板不完整",仍不通过)

#### 1.5 报告格式升级 — 未完成项"编号+标题"(REQ-00013 新增)

> 适用对象:PreflightChecker 输出"未完成项"明细行的格式
> 依据规范:FR-10.AC-10.2(`code-publish` 前置检查报告"未完成项"用"编号+标题")+ NFR-3 字符数 ≤ 30

**工具函数**(伪代码):

```ts
function truncateTitle(title: string, maxLen: number = 30): string {
  if ([...title].length <= maxLen) return title
  return [...title].slice(0, maxLen).join('') + '...'
}

function formatReqTitle(reqNum: string, title: string): string {
  return `${reqNum} · ${truncateTitle(title)}`
}

function formatTaskTitle(taskNum: string, title: string): string {
  return `${taskNum} · ${truncateTitle(title)}`
}

function formatBugTitle(bugNum: string, title: string): string {
  return `${bugNum} · ${truncateTitle(title)}`
}
```

**标题解析入口**:

```ts
function parseResultTitle(filePath: string): string {
  const content = require('fs').readFileSync(filePath, 'utf-8')
  const match = content.match(/^# 需求提示词文档 — (.+)$/m)
  return match ? match[1] : ''
}

function parsePlanTaskTitle(planPath: string, taskNum: string): string {
  const content = require('fs').readFileSync(planPath, 'utf-8')
  const lines = content.split('\n').filter(l => l.startsWith('|') && l.includes(taskNum))
  for (const line of lines) {
    const cols = line.split('|').map(c => c.trim())
    if (cols[1] === taskNum && cols[5]) return cols[5]
  }
  return ''
}

function parseFixTitle(fixPath: string): string {
  const content = require('fs').readFileSync(fixPath, 'utf-8')
  const match = content.match(/^## 缺陷标题\s*\n+(.+?)$/m)
  return match ? match[1] : ''
}
```

**报告"未完成项"行格式升级**(FR-10.AC-10.2 强约束):

```
原格式(改造前):
  - [需求] REQ-NNNNN 状态=进行中(应该=已完成)
  - [任务] TASK-... 开发状态=进行中(应该=已完成)
  - [缺陷] BUG-NNNNN 状态=待修复(应该=已修复)

新格式(改造后):
  - [需求] REQ-NNNNN · <需求标题> 状态=进行中(应该=已完成)
  - [任务] TASK-... · <任务标题> 开发状态=进行中(应该=已完成)
  - [缺陷] BUG-NNNNN · <缺陷标题> 状态=待修复(应该=已修复)
```

**解析源**(与 `code-require` / `code-plan` / `code-fix` 同):

| 类型 | 解析源 |
| --- | --- |
| 需求 | `./assistants/<版本号>/require/<需求编号>/RESULT.md` 第 1 行 |
| 任务 | `./assistants/<版本号>/plan/<需求编号>/PLAN.md` 任务总览"标题"列 |
| 缺陷 | `./assistants/<版本号>/fix/<缺陷编号>/RESULT.md` "## 缺陷标题"小节 |

**边界与异常**:
- E-10:`code-publish` 报告标题解析失败 → 退化"REQ-NNNNN 状态=..."(无标题)

**约束**:
- **不**修改看板"任务清单" / "需求清单" / "缺陷清单" 3 区段解析(沿用既有"用列名识别"逻辑)
- **不**修改 `ReportFormatter` 既有"未通过"模板的字段,仅在"未完成项明细"行嵌入"编号+标题"
- **不**修改 `code-publish` 自身的 0 commit 行为(NFR-3 `code-publish` 自身不 commit)

### 步骤 2.0:基线识别(BaselineDetector)

> **目的**:判定本版本是否是基线(规则 1 — NFR-7 锁定);基线版本跳过 UPDATE.md。

#### 2.0.1 列出所有版本

```bash
Glob: ./assistants/*/
```

过滤:
- 排除 `rules`(它是项目级目录,非版本)
- 排除隐藏文件

得到所有版本号列表。

#### 2.0.2 字典序排序

```bash
Bash: ls -1d ./assistants/*/ | sed 's|.*/\(.*\)/|\1|' | grep -vE '^rules$' | sort
```

取最小 = `min_version`(字典序最小)。

#### 2.0.3 比较

- `target_version == min_version` → **是基线** → 跳过 UPDATE.md
- `target_version != min_version` → **非基线** → 生成 UPDATE.md;`previous_version = 字典序中 target_version 的前一个版本号`

**异常路径**:
- `target_version` 不在所有版本列表中 → 报错(严重不一致)+ 退出

### 步骤 2:生成手册(ManualBuilder)

> **目的**:把"通过的版本"物化为可执行的 2 或 3 份手册骨架。

#### 2.1 创建 publish/ 目录

```bash
Bash: mkdir -p ./assistants/<版本号>/publish/
```

- 失败(权限 / 磁盘满等)→ **报错退出**(E-7,**不**进入后续步骤,**不**留半成品)

#### 2.2 探测已有文件(覆盖预检 — DD-5)

```bash
Bash: ls -1 ./assistants/<版本号>/publish/ 2>/dev/null | grep -E '(DEPLOY|UPDATE|Q&A)\.md$'
```

- 记录 `existing` 列表(0 ~ 3 项)
- 步骤 3 报告中标注"已覆盖 N 个文件"

#### 2.3 写 DEPLOY.md(始终生成)

```bash
Read: <本仓库>/skills/code-publish/templates/DEPLOY.md
Write: ./assistants/<版本号>/publish/DEPLOY.md
```

- **placeholder 替换**(DD-4):Claude 在 Write 时直接渲染,无需 sed
  - `<本版本号>` → `target_version`
  - 其他 placeholder( `<打包方式>` / `<output>` / `<server>` / 等)**保留**(用户手动补全)

#### 2.4 写 UPDATE.md(仅当非基线)

若步骤 2.0 判定"非基线":

```bash
Read: <本仓库>/skills/code-publish/templates/UPDATE.md
Write: ./assistants/<版本号>/publish/UPDATE.md
```

- placeholder 替换:
  - `<本版本号>` → `target_version`
  - `<源版本>` → `previous_version`
  - 其他保留

若基线版本 → 跳过此步骤。

#### 2.5 标记覆盖

对每个"已存在"的文件,把文件路径记入 `overwritten` 列表(供步骤 3 报告)。

**异常路径**:
- E-6:`publish/` 已存在 + 含 `DEPLOY.md` → **覆盖** + 报告中标注
- E-7:`Write` 失败 → 报错 + 立即退出(已写成功的文件保留;**不**尝试写下一个;不留半成品模板未替换的 placeholder)

### 步骤 2.5:创建 qanda/ 骨架(QandaScaffolder,条件)

> **目的**:本需求顺带在项目级创建 `assistants/qanda/` 骨架(Q-2 锁定 A)。

#### 2.5.1 探测 qanda/ 是否存在

```bash
Bash: ls -la ./assistants/qanda/ 2>/dev/null
```

- 存在 → 跳过
- 不存在 → 走 2.5.2

#### 2.5.2 创建目录 + README.md(若需要)

```bash
Bash: mkdir -p ./assistants/qanda/
Read: <本仓库>/skills/code-publish/templates/qanda-README.md
Write: ./assistants/qanda/README.md
```

- 失败(权限等)→ **不阻塞**(FR-7.AC-7.4),标记 `qanda_status = "创建失败"`,继续步骤 2.6
- 成功 → 标记 `qanda_status = "本次创建"`

**异常路径**:
- E-4:`qanda/` 创建失败 → 跳过占位 + 报告中标注 ⚠,整体流程不阻塞

### 步骤 2.6:聚合 Q&A 内容(QandaAggregator)

> **目的**:把 `assistants/qanda/*.md` 全部聚合(排除 README.md)到 `Q&A.md` 内容。

#### 2.6.1 列出 qanda 文件

```bash
Glob: ./assistants/qanda/*.md
```

- 过滤:排除 `README.md`(大小写不敏感)
- 排序:按文件名字典序(确保幂等)

#### 2.6.2 渲染 Q&A.md 内容

- 若 `source_files` 列表为空 → 渲染**占位模板**(从 `templates/Q&A.md` 原样读取)
- 若 `source_files` 非空 → 渲染:
  ```markdown
  # 发布部署 Q&A — <本版本号>
  
  > 本手册聚合自 `assistants/qanda/`,供发布部署中遇到问题时查阅。
  
  ## 1. <主题 1>(来源:qanda/<文件 1>)
  <文件 1 全文>
  
  ## 2. <主题 2>(来源:qanda/<文件 2>)
  <文件 2 全文>
  
  ...
  
  ## 占位:常见问题(待补充)
  请在 `assistants/qanda/` 目录下添加 Q&A 内容(格式建议见 `qanda/README.md`),再重跑 `code-publish`。
  ```

#### 2.6.3 写 Q&A.md

把渲染后的内容交给步骤 2 的写流程,`Write: ./assistants/<版本号>/publish/Q&A.md`

**异常路径**:
- 单文件读取失败 → 跳过该文件 + 在 Q&A.md 中加 `> ⚠ 警告:无法读取 qanda/<文件>`,不阻塞整体
- 占位场景(空 / 仅 README)→ 报告中显式提示"⚠ qanda/ 目录为空,Q&A.md 仅为占位"

### 步骤 3:报告(ReportFormatter)

> **目的**:把整个执行结果以**纯文本 + 少量 ✓/✗/⚠ 图标**输出到 stdout,供用户即时反馈。

> **报告格式**详"## 报告模板"小节;**不**写入任何文件。

#### 3.1 汇总前 6 模块结果

收集:
- `preflight_result`(passed / undone / stats)
- `baseline_result`(is_baseline / previous_version)
- `manual_result`(written / overwritten)
- `qanda_result`(scaffold_status / aggregated_count)

#### 3.2 选择报告模板并渲染

根据 `preflight_result.passed` + `baseline_result.is_baseline` + `qanda_result` 状态,选择 4 种模板之一:
- 通过 + 非基线 + qanda 有内容 → 通过模板
- 通过 + 非基线 + qanda 空 → 通过模板(含 qanda 空提示)
- 通过 + 基线 → 基线模板
- 不通过 → 不通过模板

#### 3.3 输出到 stdout

直接由 Claude 在终端输出。**不**写文件。

---

## 报告模板

> 4 种场景;每种含图标 + 统计 + 下一步建议。

### 通过(非基线,qanda 有内容)

```
✓ 发布前置检查通过(需求 N/N, 任务 M/M, 缺陷 0/0)

已生成 3 份手册:
  - assistants/<版本号>/publish/DEPLOY.md  (全新部署)
  - assistants/<版本号>/publish/UPDATE.md  (从 <源版本> 升级)
  - assistants/<版本号>/publish/Q&A.md     (常见问题,聚合自 qanda/ 的 K 个文件)

[若已覆盖]
⚠ 已覆盖 N 个文件:[file1, file2, ...]

⚠ 提示: 3 份手册均为通用骨架,请手动补全 <软件名>、<服务器地址> 等占位符后再按手册执行
⚠ 提示: 本技能不自动提交,补全后请手动 git add + commit
```

### 通过(基线)

```
✓ 发布前置检查通过(本版本 <版本号> 是基线)

已生成 2 份手册(基线无 UPDATE.md):
  - assistants/<版本号>/publish/DEPLOY.md
  - assistants/<版本号>/publish/Q&A.md

[已覆盖提示同上]
[占位提示若有]
```

### 不通过

```
✗ 发布前置检查未通过

未完成项明细:
  - [需求] REQ-NNNNN <标题> 状态=<当前>(应该=已完成)
  - [任务] TASK-REQ-NNNNN-NNNNN <标题> 开发状态=<当前>(应该=已完成)
  - [任务] TASK-REQ-NNNNN-NNNNN <标题> 测试状态=<当前>(应该 ∈ {已运行-通过, 不适用})
  - [缺陷] BUG-NNNNN <标题> 状态=<当前>(应该=已修复)

阻塞统计:
  - 需求:N / N 未完成
  - 任务:M / M 未完成
  - 缺陷:K / K 未修复

✗ 未生成任何手册。请先解决上述项后重试。
```

### qanda 空(常见,搭配通过/基线模板)

```
... (上面通过/基线报告)

⚠ assistants/qanda/ 目录为空(仅有 README.md),Q&A.md 仅为占位
请先在 assistants/qanda/ 中添加 Q&A 内容,再重跑 code-publish
```

### 无激活版本(无参数 + 无 .current-version)

```
✗ 未检测到激活版本(./assistants/.current-version 不存在)
请先调 /code-version <版本号> 创建或切换版本。
```

---

## 看板字段约定(只读消费)

`<版本号>/RESULT.md` 是本技能**只读**消费的对象。3 区段的解析锚点:

| 区段 | 锚点 | 解析字段 | 解决判定 |
| --- | --- | --- | --- |
| **需求清单** | `^## 需求清单$` | `需求编码` / `标题` / `状态` | 状态 startswith `已完成` |
| **任务清单** | `^## 任务清单$` | `任务编号` / `开发状态` / `测试状态` | 开发 = `已完成` ∧ 测试 ∈ {`已运行-通过`, `不适用`} |
| **缺陷清单** | `^## 缺陷清单$` | `缺陷编号` / `标题` / `状态` | 状态 = `已修复` |

**关键**:本技能的"解决判定"必须**等于或严于** `code-dashboard` 的"真正可发布"概念(NFR-8);解析锚点与 `code-dashboard` 共用同一份结构。任何 `dashboard-conventions.md §规则 1` 触发的字段扩展(新增列 / 新增区段),本技能通过**列名识别**(而非列号位置)自动兼容。

**本技能不写入** `RESULT.md` 任何区段;不触发 `dashboard-conventions.md §规则 1` 的 3 处同步约束。

---

## 衔接

- **下游**:
  - 运维 / 部署工程师:`DEPLOY.md` + `UPDATE.md`
  - 现场支持:`Q&A.md`
  - 用户(发布者):手动 `git add` + `git commit` 补全后的 3 份手册
- **上游**:
  - `code-version`(必须先有激活版本)
  - `code-require` / `code-design` / `code-plan` / `code-it` / `code-check`(开发周期内全部完成 → 看板 3 区段全部"已解决")
  - 项目级规范 `./assistants/rules/`(本技能只读)
- **横向**:
  - 与 `code-dashboard`(REQ-00004)共用看板 3 区段解析;用户可先 `code-dashboard` 看进度,再 `code-publish` 决定发布
  - 与 `code-auto`(REQ-00007)**不联动**:`code-auto` 不调本技能,用户在 `code-auto` 完成后手动调

## 不要做的事

- 不要在没有 `./assistants/.current-version` + 无参数的情况下继续执行
- 不要修改 `./assistants/rules/` 下的任何规范(FR-8.AC-8.3)
- 不要修改其他 10 个 `code-*` 技能的任何文件(FR-8.AC-8.2)
- 不要修改 `<版本号>/RESULT.md` 任何区段(NFR-2 纯只读)
- 不要修改 `marketplace.json` / `plugin.json`(FR-8.AC-8.1)— 注:这意味着本技能不会自动注册到 marketplace,留作 v2 follow-up(Q-D-1)
- 不要自动 `git commit`(NFR-3 + Q-9 默认)
- 不要在手册中"自动填充"除 `<本版本号>` / `<源版本>` 之外的 placeholder(用户必须手动补全)
- 不要使用 `AskUserQuestion` 询问"是否强制发布"(v1 不实现 `--force`)
- 不要实现"自动抽取"内容(从 git history / 代码扫描)— Q-6 默认不实现
- 不要把"基线识别"用规则 2 / 规则 3 替代规则 1(NFR-7 锁定)
- 不要在前置检查通过前进入步骤 2(任何文件都不写)
- 不要把本技能加入 `code-auto` 驱动的 6 技能链(Q-7 默认)
- 不要追加 `<本仓库>/CLAUDE.md` "AI 工作约定"小节(Q-8 默认)
- 不要把 qanda/ 创建失败当成致命错误(FR-7.AC-7.4)
