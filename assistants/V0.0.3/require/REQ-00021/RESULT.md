# 需求提示词文档 — REQ-00021(优化 3 技能 --result / --plan 模板参数,按用户模板格式输出填充后文档)

- 需求编码:REQ-00021
- 所属版本:V0.0.3
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06
- 最近更新:2026-06-06 17:00
- 当前版本:v1
- **主题**(来自用户输入):
  > 优化 `/code-require`、`/code-design`、`/code-plan` 三个技能,允许增加参数对输出的需求设计(--result)、概要设计(--result)、详细设计(--result)、开发计划(--plan)指定一个模板文件,在最后输出的结果中包含一个按照对应模板文件填充相关内容的输出结果文件。例如 `/code-require --result xxxx.docx` 最后输出结果中将额外包含一个 `REQUIRE.docx` 文件,该文件是按照指定的模板文件 `xxxx.docx` 为基础,填充了所有需求设计相关内容后的需求设计文档。

---

## 1. 需求概述

**为谁**:`code-skills` 仓库的 AI 协作者 + 项目主导者(在 `code-require` / `code-design` / `code-plan` 实际产出时,期望"按用户提供的模板格式输出,便于归档/对接既有流程")。

**解决什么问题**(3 个子痛点):
- **P-1 输出格式单一**:3 技能目前只输出 Markdown(`RESULT.md` / `PLAN.md`),用户若需要 `.docx` / `.xlsx` / `.pdf` / `.html` 等格式,需手动复制粘贴并重新排版,效率低、易出错。
- **P-2 模板不灵活**:3 技能内置 `templates/` 目录(章节结构模板),但**不**支持用户传入自定义模板。若用户组织有"标准需求文档模板"或"项目开发计划模板",无法直接套用。
- **P-3 与既有流程脱节**:用户组织的"需求归档 / 概要设计归档 / 详设归档 / 开发计划归档"流程往往要求特定格式,3 技能当前无法一步到位。

**带来什么价值**:
1. **新增 4 个参数**:`code-require --result` / `code-design --result` / `code-plan --result` / `code-plan --plan`
2. **后缀和用户提供模板保持一致**:传 `.docx` 出 `.docx`、传 `.md` 出 `.md`、传 `.xlsx` 出 `.xlsx`、传 `.html` 出 `.html`...
3. **基本名固定**:REQUIRE(需求 + 概设 + 详设)/ DESGIN(用户原文拼写,沿用)/ PLAN(开发计划)
4. **完全可独立执行**:不依赖 `code-auto` / `code-review` 等其他技能;沿用既有"步骤 0a / 0b / 0 / 1-N"流程;新增参数为**可选**。

---

## 2. 背景与目标

### 2.1 背景

- 3 技能(REQ-00011 后)内置 `templates/` 目录(章节结构模板,如 `requirements.md` / `design.md` / `plan.md` / `task-plan.md`),但这是**技能内部使用的章节骨架**,不暴露给用户。
- 用户组织(以 wangmiao 为例)对"需求文档 / 设计文档 / 开发计划"的归档格式有特定要求(可能是公司标准的 .docx 模板、可能是 .xlsx 任务跟踪表),目前 3 技能无法一步产出。
- 现有 `RESULT.md` / `PLAN.md` 是"AI 协作者工作用的提示词文档"(含 FR/NFR/AC 等结构),与"组织归档文档"(可能含封面 / 目录 / 签字栏等)是不同维度的产物。

### 2.2 业务目标

- **G-1**:`code-require` 新增 `--result <模板文件>` 可选参数,产出 `REQUIRE.<ext>` 文件(后缀 = 用户传入模板的后缀)
- **G-2**:`code-design` 新增 `--result <模板文件>` 可选参数,产出 `DESGIN.<ext>` 文件(用户原文拼写,**不**纠正)
- **G-3**:`code-plan` 同时新增 `--result <模板文件>`(详设,产出 `DESGIN.<ext>`)+ `--plan <模板文件>`(开发计划,产出 `PLAN.<ext>`)
- **G-4**:模板支持多种格式(`.md` / `.html` / `.docx` / `.xlsx` / `.pdf` 等),输出文件后缀与模板保持一致
- **G-5**:**不**修改 3 技能既有 `RESULT.md` / `PLAN.md` 主产出物;新增模板产出物为**额外**文件
- **G-6**:严格遵循既有"步骤 0a / 0b / 0 / 1-N"流程;新增参数为**可选**(无 `--result` 时,3 技能按原行为执行);不触发 `dashboard-conventions §规则 1` 三同步

### 2.3 本次目标(本迭代范围)

1. 修改 `code-require/SKILL.md` 新增 `--result` 可选参数解析 + 模板填充步骤
2. 修改 `code-design/SKILL.md` 新增 `--result` 可选参数解析 + 模板填充步骤
3. 修改 `code-plan/SKILL.md` 新增 `--result` + `--plan` 2 个可选参数解析 + 模板填充步骤
4. **不**修改 3 技能 frontmatter(`name` / `description` 字段**字节级保留**,符合 `skill-conventions §规则 1`)
5. **不**修改其他 10 个 `code-*` 技能
6. **不**修改 `marketplace.json` / `plugin.json` / `./assistants/rules/` / 看板模板
7. **不**新增依赖(本需求纯文档与 SKILL.md 修改,无新代码模块)

---

## 3. 用户角色与场景

### 3.1 角色:wangmiao(项目负责人,4 合 1)

### 3.2 关键场景

#### S-1:`code-require --result` 需求归档(主流程)

- 用户输入:`/code-require REQ-00021 --result ./templates/requirement-template.docx`
- 技能执行:
  1. 步骤 0a-7A 既有流程(产出 `RESULT.md`)
  2. **步骤 8A+ 模板填充(本需求新增)**:
     - 解析 `--result ./templates/requirement-template.docx`
     - `Read` 模板 → 提取占位符 / 段落结构 / 样式
     - 按 `RESULT.md` 内容填充占位符
     - 写出 `REQUIRE.docx` 到 `require/REQ-00021/REQUIRE.docx`
  3. 步骤 9A-10A 既有流程(同步看板 + 过程文档)
- 屏显新增 1 行:
  ```
  === code-require 模板填充 ===
  模板:<./templates/requirement-template.docx>
  输出:<./assistants/V0.0.3/require/REQ-00021/REQUIRE.docx>
  ```

#### S-2:`code-design --result` 概要设计归档(主流程)

- 用户输入:`/code-design REQ-00021 --result ./templates/design-template.docx`
- 技能执行:同 S-1,但产出 `DESGIN.docx`(沿用用户原文拼写)

#### S-3:`code-plan --result` 详设归档 + `--plan` 开发计划归档(主流程)

- 用户输入:`/code-plan REQ-00021 --result ./templates/detail-design.docx --plan ./templates/dev-plan.xlsx`
- 技能执行:
  1. 既有流程产出 `RESULT.md` + `PLAN.md`
  2. 模板填充:
     - `--result` → `DESGIN.<ext>`(详细设计)
     - `--plan` → `PLAN.<ext>`(开发计划)
  3. 屏显 2 行:
     ```
     === code-plan 模板填充 ===
     详细设计:<DESGIN.xlsx>
     开发计划:<PLAN.xlsx>
     ```

#### S-4:不传模板参数(沿用既有)

- 用户输入:`/code-require REQ-00021`(无 `--result`)
- 技能执行:原行为,只产出 `RESULT.md`,**不**产出 `REQUIRE.<ext>`

#### S-5:`code-auto` 调 3 技能(沿用 REQ-00007)

- `code-auto` 调 3 技能时,默认**不**传 `--result` / `--plan`(保持原行为)
- 若用户希望 `code-auto` 自动套模板,可在 `code-auto` 调用前手动传入

#### S-6:模板文件格式限制(本需求澄清后边界)

- **支持的可文本化格式**:`.md` / `.txt` / `.html` / `.json` / `.xml` / `.csv` 等
- **二进制格式**(`.docx` / `.xlsx` / `.pdf` / `.pptx`):用户原文要求"按实际二进制(对应数据格式)内容填充",但本仓库无 Python/Node 工具链(CLAUDE.md 强约束),**当前仅支持可文本化格式**;二进制格式需用户后续提供 Python 脚本(本需求**不**做,留作 follow-up)
- **占位符约定**:`{{...}}` 风格,常见占位符:`{{REQ_ID}}` / `{{REQ_TITLE}}` / `{{需求概述}}` / `{{FR_LIST}}` / `{{NFR_LIST}}` / `{{AC_LIST}}` / `{{设计概述}}` / `{{模块列表}}` / `{{任务列表}}` / `{{依赖图}}` 等
- **填充规则**:技能读 `RESULT.md` / `PLAN.md` 内容 → 解析为结构化数据 → 按模板占位符位置填充 → 输出

#### S-7:无激活版本 / 无模板文件 / 模板无占位符(边界)

- **无 `.current-version`** → 沿用既有"提示调 `code-version`"错误(E-1)
- **`--result` 指定的模板文件不存在** → 屏幕输出 `⚠ 模板文件不存在:<路径>`,跳过模板填充,继续原流程
- **模板文件无占位符** → 直接把 `RESULT.md` 内容追加到模板(当作"参考文档"使用)
- **模板有占位符但技能无法解析(如 .docx zip)** → 屏幕输出 `⚠ 模板格式二进制,无法读取占位符,跳过填充`,继续原流程(本需求**仅**支持可文本化格式,二进制格式**不**报错,只是跳过)

#### S-8:大需求多模板(边界)

- 大需求可能需要 2-3 个不同模板(如"需求总览模板" + "技术附录模板" + "测试用例模板")
- 本需求**仅**支持每技能 1 个 `--result` + 1 个 `--plan`(共 2 参数)
- 多模板场景**不**支持(本需求范围外;留作 follow-up)

---

## 4. 功能需求(FR)

### FR-1:3 技能新增 `--result` / `--plan` 可选参数解析

- **描述**:`code-require` / `code-design` / `code-plan` 3 技能新增可选参数:
  - `code-require` `--result <模板文件>` → 产出 `REQUIRE.<ext>`
  - `code-design` `--result <模板文件>` → 产出 `DESGIN.<ext>`(用户原文拼写)
  - `code-plan` `--result <模板文件>` → 产出 `DESGIN.<ext>`(详细设计)
  - `code-plan` `--plan <模板文件>` → 产出 `PLAN.<ext>`(开发计划)
- **参数性质**:**可选**(无参时 3 技能按原行为执行)
- **优先级**:必须
- **主流程**:
  1. 技能启动时(步骤 0 之前)解析用户输入,识别 `--result <路径>` / `--plan <路径>` 参数
  2. 校验模板文件存在性:不存在 → 屏显 `⚠ 模板文件不存在:<路径>`,**跳过**模板填充(不阻断)
  3. 记录参数到过程文档(`work-log.md` 或 `analysis-notes.md`),便于追溯
- **分支/异常**:
  - **E-1**:`--result` 缺值(只写 `--result` 不写路径)→ 屏显 `⚠ --result 缺模板文件路径`,跳过填充
  - **E-2**:`--result` 路径含通配符(`*.docx`)→ 屏显 `⚠ 模板路径不支持通配符`,跳过填充
  - **E-3**:`--result` 与 `--plan` 同时不传 → 原行为执行,**不**屏显
  - **E-4**:用户传 2 个 `--result`(重复)→ 取最后一个
- **数据变化**:
  - 3 技能 SKILL.md 步骤 0 之前新增"## 命令行参数解析"小节(纯追加,不修改既有)
  - **不**修改 frontmatter(INV-1)
- **来源**:本需求 v1 锁定

### FR-2:模板填充步骤(本需求新增核心)

- **描述**:3 技能在主产出物(`RESULT.md` / `PLAN.md`)完成后,执行"模板填充"步骤,产出 `REQUIRE.<ext>` / `DESGIN.<ext>` / `PLAN.<ext>`
- **优先级**:必须
- **主流程**:
  1. **读取模板**:`Read <模板文件路径>`
     - 可文本化格式(.md / .html / .txt / .json / .xml / .csv)→ 完整读取
     - 二进制格式(.docx / .xlsx / .pdf / .pptx)→ 屏显 `⚠ 模板格式二进制,无法读取占位符,跳过填充`,**不**尝试读取(避免乱码)
  2. **占位符提取**:
     - 可文本化格式 → 扫描 `{{...}}` 风格占位符
     - 二进制格式 → 跳过
  3. **结构化数据准备**:从 `RESULT.md` / `PLAN.md` 提取:
     - 需求 ID / 标题 / 描述 / FR 列表 / NFR 列表 / AC 列表 / 关联需求 / 待澄清
     - 设计概述 / 模块列表 / 接口列表 / 数据结构 / 风险与回退
     - 任务列表(任务编号 / 标题 / 类型 / 状态 / 负责人)
     - 任务依赖图(Mermaid) / 里程碑
  4. **占位符替换**:
     - `{{REQ_ID}}` → `REQ-00021`
     - `{{REQ_TITLE}}` → `优化 3 技能 --result / --plan 模板参数...`
     - `{{需求概述}}` → 从 `RESULT.md` §1 提取
     - `{{FR_LIST}}` → 从 `RESULT.md` §4 提取(Markdown 表格或列表)
     - `{{任务列表}}` → 从 `PLAN.md` §任务总览提取
     - **占位符映射表**:本需求后置(由技能维护一份常用占位符 → 文档章节的映射)
  5. **写出文件**:
     - 路径:`<原主产出物同目录>/REQUIRE.<ext>`(后缀 = 模板后缀)
     - 例:`require/REQ-00021/RESULT.md` + `require/REQ-00021/REQUIRE.docx`
- **分支/异常**:
  - **E-5**:模板无占位符 → 把 `RESULT.md` 完整内容追加到模板(当作"参考文档")
  - **E-6**:模板有占位符但技能无法全部填充 → 已填充的占位符替换,未填充的占位符保留(原样输出,便于用户手动补)
  - **E-7**:二进制格式模板 → 屏显 `⚠ 跳过`(不报错)
  - **E-8**:模板文件大小 > 1MB → 屏显 `⚠ 模板文件过大(>1MB),可能影响性能`,继续
- **数据变化**:
  - 3 技能目录新增 `REQUIRE.<ext>` / `DESGIN.<ext>` / `PLAN.<ext>` 模板产出物
  - 模板产出物与主产出物并列(都参与 git 跟踪)
- **来源**:本需求 v1 锁定

### FR-3:二进制格式限制(本需求范围外,留作 follow-up)

- **描述**:用户原文要求"按实际二进制(对应数据格式)内容填充",但本仓库无 Python/Node 工具链(CLAUDE.md 强约束),当前**仅**支持可文本化格式
- **优先级**:本需求**不**实现
- **主流程**(follow-up):
  1. 用户提供 Python 脚本(如 `fill_docx.py`),放在 `./assistants/rules/` 或 `.claude-plugin/` 下
  2. 技能调 `Bash: python fill_docx.py <模板> <输出> <数据 json>`,把 `RESULT.md` 转为 JSON,传给脚本
  3. 脚本返回 .docx 二进制文件
- **分支/异常**:
  - **E-9**:脚本未提供 → 屏显 `⚠ 模板格式二进制,需要用户提供 <format> 填充脚本`,跳过
- **数据变化**:本需求**不**修改 SKILL.md 的二进制填充逻辑(由 follow-up 需求添加)
- **来源**:本需求 v1 锁定(本需求**仅**实现可文本化格式;二进制格式**不**在本需求范围)

### FR-4:屏显 + 看板同步

- **描述**:模板填充完成后,屏显 + 看板同步
- **优先级**:必须
- **主流程**:
  1. 屏显(沿用 REQ-00013 标题解析):
     ```
     === <code-require / code-design / code-plan> 模板填充 ===
     模板:<模板文件路径>
     输出:<输出文件路径>(<占位符数>)
     ```
  2. 看板同步:**不**追加新行(模板产出物**不**是任务,仅是附加文件;沿用 `dashboard-conventions §规则 1` 0 触发)
  3. 过程文档追加:在 `analysis-notes.md` 记录"模板填充结果"(模板路径 / 输出路径 / 占位符填充数 / 失败占位符列表)
- **数据变化**:
  - 屏显新增 1-2 行(模板填充段)
  - 看板**不**改
  - `analysis-notes.md` 追加 1 节
- **来源**:本需求 v1 锁定

### FR-5:不修改其他 10 个 `code-*` 技能

- **描述**:本需求**只**修改 `code-require` / `code-design` / `code-plan` 3 个技能
- **优先级**:必须
- **AC**:
  - AC-5.1:`code-fix` / `code-unit` / `code-review` / `code-auto` / `code-version` / `code-init` / `code-merge` / `code-publish` / `code-dashboard` / `code-rule` 10 个 SKILL.md **不**被本需求修改
  - AC-5.2:`code-auto` 现行"调 3 技能时**不**传 `--result` / `--plan`"(保持原行为;若用户希望自动套模板,在 `code-auto` 提示中显式传)
  - AC-5.3:`code-dashboard` / `code-publish` / `code-review` 现有逻辑**不**变
- **来源**:本需求 v1 锁定(强约束)

### FR-6:不修改 marketplace / plugin / 规范

- **描述**:本需求**不**修改 marketplace / plugin 元信息 / 看板 / 规范文件
- **优先级**:必须
- **AC**:
  - AC-6.1:`marketplace.json` / `plugin.json` **不**被本需求修改
  - AC-6.2:`./assistants/rules/` 下的所有规范文件**不**被本需求修改
  - AC-6.3:`./assistants/V0.0.3/RESULT.md` 看板**不**被本需求修改(只追加 1 条"需求清单"行,沿用既有写法)
  - AC-6.4:中英 README 若需更新,按 `doc-conventions §规则 1` 同次提交中英 — 但本需求**不**主动写 README(由 `code-rule` 沉淀)
- **来源**:本需求 v1 锁定(强约束)

### FR-7:不变量自检(INV)

- **描述**:本需求完成后,既有 frontmatter / 步骤 / 看板 / 规范的字节级保留
- **优先级**:必须
- **AC**:
  - **INV-1**:3 技能 SKILL.md frontmatter `name` 字段**字节级保留**;`description` 字段允许小幅扩展(本需求不修改)
  - **INV-2**:3 技能 SKILL.md 既有"## 工作流程"小节**不**被破坏;**只**追加新锚点("## 命令行参数解析"小节 + "## 模板填充步骤"小节)
  - **INV-3**:3 技能既有步骤 0a / 0b / 0 / 1-N 字节级保留
  - **INV-4**:3 技能"## 衔接" + "## 不要做的事"段**不**改
  - **INV-5**:3 技能看板"任务清单"区段字段**0 新增**
  - **INV-6**:本需求**0** 修改 `marketplace.json` / `plugin.json` / `./assistants/rules/` / 看板模板
  - **INV-7**:本需求**0** 派生"更新看板"任务(REQ-00017 强约束)
  - **INV-8**:本需求**0** 修改其他 10 个 `code-*` SKILL.md
  - **INV-9**:本需求后 `--result` / `--plan` 参数为**可选**,无参时 3 技能按原行为执行(NFR-3 幂等)
- **来源**:本需求 v1 锁定

---

## 5. 非功能需求 / 约束(NFR)

### 5.1 性能(NFR-1)
- 模板填充耗时 < 5 秒(可文本化格式,1MB 以内)
- 屏显新增 1-2 行,**不**影响整体性能

### 5.2 兼容性(NFR-2)
- **NFR-2.1**:`dashboard-conventions §规则 1` 0 触发(模板产出物**不**是任务;看板**不**追加新行)
- **NFR-2.2**:`encoding-conventions §规则 1/3` 0 触发(模板产出物无编号,沿用现有命名)
- **NFR-2.3**:`skill-conventions §规则 1` 0 触发(3 技能 SKILL.md frontmatter 字节级保留;只有新增"## 命令行参数解析" + "## 模板填充步骤"小节)
- **NFR-2.4**:`marketplace-protocol` 0 触发(0 改 `marketplace.json` / `plugin.json`)
- **NFR-2.5**:`commit-conventions` 0 触发(沿用既有 `chore(<scope>): <subject>` 格式)
- **NFR-2.6**:`doc-conventions` 0 触发(0 改中英 README)
- **NFR-2.7**:`naming-conventions` 0 触发(本需求基本名 REQUIRE / DESGIN / PLAN 用户原文锁定)
- **NFR-2.8**:`dependency-conventions` 0 触发(0 新增依赖;二进制格式填充**留作 follow-up**)
- **NFR-2.9**:`module-conventions §规则 1` 0 触发(模板产出物放在原主产出物同目录,与既有 `RESULT.md` / `PLAN.md` 摆放规则一致)

### 5.3 可靠性(NFR-3)
- **NFR-3.1**:`--result` / `--plan` 多次执行(模板相同)→ 输出文件**覆盖**(幂等)
- **NFR-3.2**:`--result` / `--plan` 缺值 / 文件不存在 / 二进制格式 → **不**报错,屏显 `⚠` 后继续
- **NFR-3.3**:`code-auto` 调 3 技能时**不**传 `--result` / `--plan`(沿用 REQ-00007 Q-4 锁定 A "总选推荐项",推荐项**不**含模板参数)
- **NFR-3.4**:模板填充步骤在主产出物完成后才执行(顺序保证:主产出物 → 模板填充 → 看板同步 → 末尾兜底提交)

### 5.4 可观测性(NFR-4)
- **NFR-4.1**:模板填充屏显新增 1-2 行(沿用 REQ-00013 标题解析风格)
- **NFR-4.2**:`analysis-notes.md` 追加"模板填充结果"节(模板路径 / 输出路径 / 占位符填充数 / 失败占位符列表)
- **NFR-4.3**:`work-log.md` 记录 `--result` / `--plan` 参数解析(便于回溯)

### 5.5 可维护性(NFR-5)
- **NFR-5.1**:3 技能 SKILL.md 行数变化 -5% ~ +15%(允许小幅增长,因新增"命令行参数解析" + "模板填充步骤"小节)
- **NFR-5.2**:占位符映射表(本需求内置 12 个常用占位符:REQ_ID / REQ_TITLE / 需求概述 / FR_LIST / NFR_LIST / AC_LIST / 关联需求 / 待澄清 / 设计概述 / 模块列表 / 接口列表 / 数据结构 / 任务列表 / 依赖图 / 里程碑)
- **NFR-5.3**:`code-rule` 可后续沉淀"占位符约定"规范(本需求**不**主动写 `assistants/rules/`)

### 5.6 安全性(NFR-6)
- **NFR-6.1**:模板路径校验(防止路径穿越 — 不允许 `../` 跳出工作空间)
- **NFR-6.2**:模板文件大小限制(1MB;过大屏显 `⚠` 但继续)
- **NFR-6.3**:`--result` / `--plan` **不**写工作空间外文件(路径前缀必须 `./assistants/<版本号>/...`)

---

## 6. 页面与界面(本需求不涉及)

> 本需求**不**新增 / 不修改任何用户可见页面(本仓库是 meta-skills 工具集,无 UI)。
> 屏显输出见 §7 交互逻辑。

---

## 7. 交互逻辑

### 7.1 3 技能启动流程(本需求改后)

```
[启动 / 用户输入]
  ↓
[步骤 0a:git pull] ─────────┐ (沿用 REQ-00005)
  ↓ (成功)
[命令行参数解析(本需求新增)]
  - 解析 --result <模板文件>  --plan <模板文件>
  - 校验文件存在性
  - 记录到 work-log.md / analysis-notes.md
  ↓
[步骤 0b:code-auto 检测 / 设计目标确认 / 步骤 0b.0] (沿用既有)
  ↓
[步骤 0:版本上下文检测] (沿用既有)
  ↓
[步骤 1-N:原有流程(产出 RESULT.md / PLAN.md)]
  ↓
[模板填充步骤(本需求新增,主产出物完成后)]
  - 读模板 → 提取占位符 → 结构化数据准备 → 占位符替换 → 写出
  - 屏显:=== <技能名> 模板填充 ===
  ↓
[步骤 9A / 9B:同步版本看板] (沿用既有;模板产出物不触发看板变更)
  ↓
[末尾兜底提交]
  ↓
[退出]
```

### 7.2 占位符映射表(内置 12 个常用占位符)

| 占位符 | 来源 | 用途 |
| --- | --- | --- |
| `{{REQ_ID}}` | `RESULT.md` 文档头 | 需求编号 |
| `{{REQ_TITLE}}` | `RESULT.md` 文档头 | 需求标题 |
| `{{需求概述}}` | `RESULT.md` §1 | 1 段简介 |
| `{{FR_LIST}}` | `RESULT.md` §4 | FR 列表(Markdown 表格) |
| `{{NFR_LIST}}` | `RESULT.md` §5 | NFR 列表 |
| `{{AC_LIST}}` | `RESULT.md` §10 | AC 列表 |
| `{{关联需求}}` | `RESULT.md` §11 | 关联需求编码列表 |
| `{{待澄清}}` | `RESULT.md` §12 | 待澄清项 |
| `{{设计概述}}` | `design/.../RESULT.md` §1 | 设计概述 |
| `{{模块列表}}` | `design/.../RESULT.md` §模块拆分 | 模块名 / 路径 / 职责 |
| `{{接口列表}}` | `design/.../RESULT.md` §接口 | 接口签名 / 入参 / 出参 |
| `{{数据结构}}` | `design/.../RESULT.md` §数据结构 | 实体 / 字段 / 索引 |
| `{{任务列表}}` | `plan/.../PLAN.md` §任务总览 | 任务编号 / 标题 / 状态 |
| `{{依赖图}}` | `plan/.../PLAN.md` §任务依赖图 | Mermaid 流程图 |
| `{{里程碑}}` | `plan/.../PLAN.md` §里程碑 | 里程碑列表 |

> 本需求**内置** 15 个常用占位符;用户可在模板中**自定义**占位符,未在表中的占位符技能**不**替换(保留原样输出)

### 7.3 模板填充算法(伪代码)

```python
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

### 7.4 屏显格式契约

| 场景 | 格式 |
| --- | --- |
| 启动(无模板) | (沿用既有) `正在处理: REQ-NNNNN · <需求标题>` |
| 启动(有模板) | (新增) `正在处理: REQ-NNNNN · <需求标题>(--result <模板>)` |
| 模板填充完成 | (新增) `=== <code-require / code-design / code-plan> 模板填充 ===\n  模板:<路径>\n  输出:<路径>(<N> 个占位符已替换)` |
| 模板跳过 | (新增) `⚠ 模板文件不存在:<路径>,跳过` |
| 完成 | (沿用既有) `完成: REQ-NNNNN · <需求标题>(含 <REQUIRE / DESGIN / PLAN>.<ext>)` |
| 中止 | (沿用既有) `⛔ code-require 中止: REQ-NNNNN · <需求标题>(<原因>)` |
| 错误 | (沿用既有) `✗ 错误: REQ-NNNNN · <需求标题>(<错误信息>)` |

### 7.5 异常处理

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | `--result` 缺值 | 屏显 `⚠ --result 缺模板文件路径`,跳过 |
| **E-2** | `--result` 路径含通配符 | 屏显 `⚠ 模板路径不支持通配符`,跳过 |
| **E-3** | 无 `.current-version` | 沿用既有(提示调 `code-version`) |
| **E-5** | 模板无占位符 | 把 `RESULT.md` 完整内容追加到模板 |
| **E-6** | 占位符未识别 | 已识别的替换,未识别的保留原样 |
| **E-7** | 二进制格式模板 | 屏显 `⚠ 跳过`,不报错 |
| **E-8** | 模板文件 > 1MB | 屏显 `⚠ 过大`,继续 |
| **E-9** | 模板路径 `../` 跳出工作空间 | 屏显 `⚠ 模板路径不安全`,跳过 |
| **E-10** | `--result` / `--plan` 与 `code-auto` 协同 | `code-auto` 不传(沿用 REQ-00007 Q-4) |

---

## 8. 数据与状态

### 8.1 模板产出物路径

| 技能 | 参数 | 输出文件名 | 输出路径 |
| --- | --- | --- | --- |
| `code-require` | `--result <模板>` | `REQUIRE.<ext>` | `./assistants/<版本号>/require/<需求编码>/REQUIRE.<ext>` |
| `code-design` | `--result <模板>` | `DESGIN.<ext>`(用户原文拼写) | `./assistants/<版本号>/design/<需求编码>/DESGIN.<ext>` |
| `code-plan` | `--result <模板>` | `DESGIN.<ext>`(用户原文拼写) | `./assistants/<版本号>/plan/<需求编码>/DESGIN.<ext>` |
| `code-plan` | `--plan <模板>` | `PLAN.<ext>` | `./assistants/<版本号>/plan/<需求编码>/PLAN.<ext>` |

> 注:同版本同需求下,`code-design` 的 `DESGIN.<ext>` 与 `code-plan` 的 `DESGIN.<ext>` **不**冲突(路径不同:`design/<REQ>/DESGIN.<ext>` vs `plan/<REQ>/DESGIN.<ext>`)

### 8.2 占位符映射表(本需求内置 15 个)

| 占位符 | 来源 | 备注 |
| --- | --- | --- |
| `{{REQ_ID}}` | `require/.../RESULT.md` 文档头 | 需求编号 |
| `{{REQ_TITLE}}` | `require/.../RESULT.md` 文档头 | 需求标题 |
| `{{需求概述}}` | `require/.../RESULT.md` §1 | 1 段简介 |
| `{{FR_LIST}}` | `require/.../RESULT.md` §4 | FR 列表 |
| `{{NFR_LIST}}` | `require/.../RESULT.md` §5 | NFR 列表 |
| `{{AC_LIST}}` | `require/.../RESULT.md` §10 | AC 列表 |
| `{{关联需求}}` | `require/.../RESULT.md` §11 | 关联需求编码列表 |
| `{{待澄清}}` | `require/.../RESULT.md` §12 | 待澄清项 |
| `{{设计概述}}` | `design/.../RESULT.md` §1 | 设计概述 |
| `{{模块列表}}` | `design/.../RESULT.md` §模块拆分 | 模块名 / 路径 / 职责 |
| `{{接口列表}}` | `design/.../RESULT.md` §接口 | 接口签名 / 入参 / 出参 |
| `{{数据结构}}` | `design/.../RESULT.md` §数据结构 | 实体 / 字段 / 索引 |
| `{{任务列表}}` | `plan/.../PLAN.md` §任务总览 | 任务编号 / 标题 / 状态 |
| `{{依赖图}}` | `plan/.../PLAN.md` §任务依赖图 | Mermaid 流程图 |
| `{{里程碑}}` | `plan/.../PLAN.md` §里程碑 | 里程碑列表 |

> 模板中未在表中的占位符**不**替换(保留原样输出)

### 8.3 模板文件支持格式(本需求实现范围)

| 格式 | 支持 | 实现方式 |
| --- | --- | --- |
| `.md` | ✅ | 字符串替换 + Write |
| `.html` | ✅ | 字符串替换 + Write |
| `.txt` | ✅ | 字符串替换 + Write |
| `.json` | ✅ | 字符串替换 + Write(注意:JSON 模板中 `{{...}}` 需转义) |
| `.xml` | ✅ | 字符串替换 + Write |
| `.csv` | ✅ | 字符串替换 + Write |
| `.yaml` / `.yml` | ✅ | 字符串替换 + Write |
| `.docx` / `.xlsx` / `.pptx` | ❌(本需求) | 屏显 `⚠ 跳过`,follow-up 由用户提供 Python 脚本 |
| `.pdf` | ❌(本需求) | 屏显 `⚠ 跳过`,follow-up |

### 8.4 状态机:模板填充(无新增状态)

模板填充是**附加步骤**,不修改 3 技能既有状态机。流程:主产出物 → 模板填充 → 看板同步 → 末尾兜底提交。

---

## 9. 边界与异常

| ID | 场景 | 处理 |
| --- | --- | --- |
| **B-1** | 无 `.current-version` | 沿用既有(提示调 `code-version`) |
| **B-2** | `git pull` 失败(步骤 0a) | 沿用既有 |
| **B-3** | `--result` 缺值 | 屏显 `⚠ --result 缺模板文件路径`,跳过 |
| **B-4** | `--result` 路径含通配符 | 屏显 `⚠ 模板路径不支持通配符`,跳过 |
| **B-5** | 模板文件不存在 | 屏显 `⚠ 模板文件不存在:<路径>`,跳过 |
| **B-6** | 模板文件 > 1MB | 屏显 `⚠ 模板文件过大`,继续 |
| **B-7** | 模板路径 `../` 跳出工作空间 | 屏显 `⚠ 模板路径不安全`,跳过 |
| **B-8** | 模板无占位符 | 把 `RESULT.md` 完整内容追加到模板 |
| **B-9** | 占位符未识别 | 已识别的替换,未识别的保留原样 |
| **B-10** | 二进制格式模板 | 屏显 `⚠ 跳过`,不报错 |
| **B-11** | 多次执行(`--result` 模板相同) | 输出文件**覆盖**(幂等) |
| **B-12** | `code-auto` 调 3 技能 | `code-auto` 不传(沿用 REQ-00007 Q-4) |
| **B-13** | 大需求多模板(2+ 模板) | 本需求**不**支持(留作 follow-up) |

---

## 10. 验收标准(AC 总览)

按 FR 编号归类,合计 ~30 条:

- **FR-1**(5 条):AC-1.1 ~ AC-1.5
- **FR-2**(8 条):AC-2.1 ~ AC-2.8
- **FR-3**(3 条):AC-3.1 ~ AC-3.3
- **FR-4**(3 条):AC-4.1 ~ AC-4.3
- **FR-5**(3 条):AC-5.1 ~ AC-5.3
- **FR-6**(4 条):AC-6.1 ~ AC-6.4
- **FR-7**(9 条):INV-1 ~ INV-9

**总计**:约 30 条 AC + 9 条 INV。

### 10.1 FR-1 ~ FR-2 验收(--result / --plan 参数 + 模板填充)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-1.1** | 调 `code-require REQ-00021 --result ./tmpl.md` | 步骤 0 之前新增"## 命令行参数解析"小节;识别 `--result ./tmpl.md` 并记录到 `analysis-notes.md` |
| **AC-1.2** | 调 `code-design REQ-00021 --result ./tmpl.docx` | 解析 `--result ./tmpl.docx`(二进制格式)→ 屏显 `⚠ 跳过` |
| **AC-1.3** | 调 `code-plan REQ-00021 --result ./det.md --plan ./plan.xlsx` | 解析 2 个参数,分别填充 → 产出 `DESGIN.md` + `PLAN.xlsx` |
| **AC-1.4** | 调 3 技能不传 `--result` | 原行为执行,**不**产出模板文件 |
| **AC-1.5** | 验证 `--result` 缺值 | 屏显 `⚠ --result 缺模板文件路径`,跳过 |
| **AC-2.1** | 模板为 `.md`,含 `{{REQ_ID}}` 占位符 | 占位符替换为 `REQ-00021`;输出文件后缀为 `.md` |
| **AC-2.2** | 模板为 `.html`,含 `{{需求概述}}` 占位符 | 占位符替换;输出文件后缀为 `.html` |
| **AC-2.3** | 模板为 `.docx`(二进制) | 屏显 `⚠ 模板格式二进制,跳过`;**不**产出 .docx |
| **AC-2.4** | 模板无占位符 | 把 `RESULT.md` 完整内容追加到模板;输出文件 = 模板 + 源数据 |
| **AC-2.5** | 模板有占位符但未识别 | 已识别的替换,未识别的保留原样 |
| **AC-2.6** | 模板文件不存在 | 屏显 `⚠ 模板文件不存在`,跳过 |
| **AC-2.7** | 模板文件 > 1MB | 屏显 `⚠ 模板文件过大`,继续 |
| **AC-2.8** | 模板路径 `../` 跳出工作空间 | 屏显 `⚠ 模板路径不安全`,跳过 |

### 10.2 FR-3 验收(二进制格式限制)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-3.1** | 模板为 `.docx` | 屏显 `⚠ 跳过`,**不**尝试读取二进制(避免乱码) |
| **AC-3.2** | 模板为 `.xlsx` | 屏显 `⚠ 跳过` |
| **AC-3.3** | 模板为 `.pdf` | 屏显 `⚠ 跳过` |

### 10.3 FR-4 验收(屏显 + 看板)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-4.1** | 模板填充完成 | 屏显 `=== <技能名> 模板填充 ===\n  模板:<路径>\n  输出:<路径>(<N> 个占位符已替换)` |
| **AC-4.2** | 看板同步 | 看板**不**追加新行(模板产出物**不**是任务) |
| **AC-4.3** | 过程文档 | `analysis-notes.md` 追加"模板填充结果"节(模板路径 / 输出路径 / 占位符填充数) |

### 10.4 FR-5 ~ FR-8 验收(沿用 REQ-00019 / REQ-00020 强约束)

- AC-5.1 ~ AC-5.3:10 个其他 `code-*` SKILL.md 0 改动
- AC-6.1 ~ AC-6.4:marketplace / plugin / 规范 / 看板 0 改动
- INV-1 ~ INV-9:9 条不变量自检

---

## 11. 关联需求

| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| **REQ-00005**(V0.0.2) | 首步拉取最新代码 + 末步兜底提交 | 沿用"步骤 0a"位置;`--result` / `--plan` 在步骤 0 之前解析 | `./assistants/V0.0.2/require/REQ-00005/RESULT.md` |
| **REQ-00007**(V0.0.2) | `code-auto` 自动开发技能 | `code-auto` 调 3 技能时**不**传 `--result` / `--plan` | `./assistants/V0.0.2/require/REQ-00007/RESULT.md` |
| **REQ-00011**(V0.0.2) | `code-design` / `code-plan` 步骤 0b 设计目标确认 | 沿用步骤 0b;`--result` / `--plan` 解析在步骤 0 之前 | `./assistants/V0.0.2/require/REQ-00011/RESULT.md` |
| **REQ-00013**(V0.0.2) | 6 技能启用"编号+标题" 显示 | 模板填充屏显沿用 `formatReqTitle` 风格 | `./assistants/V0.0.2/require/REQ-00013/RESULT.md` |
| **REQ-00017**(V0.0.2) | `code-plan` 不再为"更新看板"拆派生任务 | INV-7 沿用;模板产出物**不**是任务 | `./assistants/V0.0.2/require/REQ-00017/RESULT.md` |
| **REQ-00019**(V0.0.2) | `code-plan` BUG 模式同构 | 模板填充对 BUG 路径同样生效(沿用既有) | `./assistants/V0.0.2/require/REQ-00019/RESULT.md` |
| **REQ-00020**(V0.0.3) | 架构设计目标重新归位 + 3 新维度 | 沿用 V0.0.3 工作空间;无架构设计目标冲突 | `./assistants/V0.0.3/require/REQ-00020/RESULT.md` |

---

## 12. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本需求**0** 待澄清;5 FR / 6 NFR / ~30 AC / 9 INV 全部已锁定;**Q-1** 模板格式采纳用户回答"按实际用户给定的模板格式输出"(.docx/.xlsx/.pdf 按二进制,但本需求**仅**实现可文本化格式,二进制**不**报错只跳过);**Q-2** 文件命名采纳用户回答"后缀名和用户提供的文件名保持一直,基本名 REQUIRE / DESGIN(详设、概设都是)/ PLAN";**Q-3** 二进制格式填充**留作 follow-up**(本仓库无 Python/Node 工具链);**Q-4** 大需求多模板**不**支持(留作 follow-up) | 0 待澄清 |

---

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-06 17:00 | v1 | 初始创建:7 FR / 6 NFR / ~30 AC / 9 INV / 4 项 Q-locked;锁定 4 参数(`code-require --result` / `code-design --result` / `code-plan --result` / `code-plan --plan`)+ 15 个内置占位符 + 3 个可文本化格式支持(.md / .html / .txt 等);**0** 触发 `dashboard-conventions §规则 1` 三同步;**0** 派生"更新看板"任务 REQ-00017 强约束;**0** 修改其他 10 个 `code-*` SKILL.md;**0** 触发 `encoding-conventions §规则 1/3`;**0** 触发 `marketplace-protocol`;**0** 触发 `module-conventions §规则 1`;3 个 SKILL.md 修改(`code-require` / `code-design` / `code-plan`);**DESGIN 拼写锁定**(用户原文) | wangmiao |
