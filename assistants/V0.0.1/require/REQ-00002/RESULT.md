# REQ-00002 — 编码格式统一(REQ/TASK/BUG 均 5 位)

- 需求编码:REQ-00002(新格式,提前采用)
- 所属版本:V0.0.1
- 状态:已澄清(Q-7 已锁定 v2;6 项 Q 待澄清细节 Q-6/Q-8/Q-9/Q-10/Q-11/Q-12)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-03 20:20
- 当前版本:v2

---

## 1. 需求概述
把项目内三类编码格式统一为纯数字、5 位、无年份段的形式:`REQ-NNNNN` / `TASK-(REQ|BUG)-NNNNN-NNNNN`(v2 锁定 G4 新嵌套式)/ `BUG-NNNNN`,并**追溯**覆盖到现有需求编码(REQ-2026-0001 → REQ-00001,2026-06-03 20:20 部分提前落地 — 仅目录+本工作空间引用)。范围横切全部 10 个 `code-*` 技能的 SKILL.md、模板、README/CLAUDE.md 与版本看板示例。本需求实施后,后续所有 `code-*` 技能在产出编码时一律遵守新规则;旧编码在历史目录与新编码间通过 `migration-mapping.md` 建立追溯关系。

## 2. 背景与目标
- **背景**:当前三类编码格式不一致:
  - REQ 含年份:`REQ-YYYY-NNNN`(如 `REQ-2026-0001`)
  - TASK 嵌套于 REQ:`<REQ>-<NN>`(如 `REQ-2026-0001-001`)
  - BUG 只有 3 位:`BUG-NNN`(如 `BUG-001`)
  > 视觉与编程上不一致,且容量上限不齐(BUG 仅 999、REQ 因含年份不易索引、TASK 编码过长)
- **业务目标**:让三类编码维度齐平、格式统一、易于排序与索引,降低使用者认知成本与未来工具自动化成本
- **本次目标**:
  1. 定义并落地新格式:REQ = `REQ-NNNNN`、BUG = `BUG-NNNNN`(5 位纯数字递增);TASK = `TASK-(REQ|BUG)-NNNNN-NNNNN`(v2 锁定 G4 新嵌套式,父级内独立递增)
  2. 同步 10 个 SKILL.md 与全部模板中的格式描述、占位符、示例值、解析 regex
  3. 同步 README.md / README.en.md / CLAUDE.md 中所有命令示例与流程说明
  4. 追溯重命名 V0.0.1 现有 REQ-2026-0001 → REQ-00001(目录 + 所有引用)
  5. EXISTING- 前缀(V0.0.0 基线特例)的处理待 Q-6 确认
  6. 推荐新建 `./assistants/rules/encoding-conventions.md` 作为强制约束源(待 Q-8 确认)
  7. 持久化新旧编码映射表 `migration-mapping.md`(待 Q-9 确认)

## 3. 用户角色与场景

### 角色
- **仓库维护者**(wangmiao):执行规则定义、文件批量更新、追溯重命名
- **AI 协同者**(Claude Code 调用各 `code-*` 技能时的执行体):需读取新规则,在产出新编码时严格遵守
- **下游使用者**(通过 `claude plugin install` 引入本插件的最终用户):受新格式影响,在交互式输入需求编码/任务编码/缺陷编码时使用新格式

### 场景

#### 场景 1:维护者实施规则统一(主流程)
- 作为 **仓库维护者**,我想要 **把三类编码格式统一为 5 位纯数字**,以便 **降低团队与 AI 在长期使用中的认知与解析成本**
- **前置条件**:V0.0.1 工作空间;REQ-00001(原 REQ-2026-0001,已重命名)已完成需求分析阶段(下游 design/plan/it/review 待开展);git working tree clean
- **主流程**:
  1. (推荐)先完成 REQ-00001 的全部下游阶段(避免追溯重命名分散)
  2. 实施 REQ-00002:批量改 SKILL.md / 模板 / README / CLAUDE.md
  3. ✅ 追溯重命名 REQ-2026-0001 → REQ-00001(目录 + 本工作空间引用)— 已于 2026-06-03 20:20 提前落地
  4. 写入 migration-mapping.md
  5. (可选,Q-8)新建 `./assistants/rules/encoding-conventions.md`
- **异常**:中途发现遗漏文件 → `code-it` 偏差日志记录;`code-review` 阶段穷举 Grep 兜底

#### 场景 2:AI 在新项目中按新规则产出编码
- 作为 **Claude Code(执行 code-require)**,我想要 **从规则文件读取新格式**,以便 **首次创建需求时使用 REQ-NNNNN 而非 REQ-YYYY-NNNN**
- **前置条件**:新规则已落地;`./assistants/rules/encoding-conventions.md`(若 Q-8 = a)或 `code-require` SKILL.md 已更新
- **主流程**:用户调 `code-require`,AI 提示"请输入需求编码(格式 REQ-NNNNN)",用户输入 `REQ-00001`,工作目录创建

#### 场景 3:在已有需求基础上派生任务
- 作为 **Claude Code(执行 code-plan)**,我想要 **为某需求(或缺陷)生成下一个 TASK 编码**,以便 **PLAN.md 中任务唯一标识**
- **前置条件**:Q-7 = G4(v2 锁定),父级编码已知
- **主流程**:
  1. 用户告知父级(REQ-NNNNN 或 BUG-NNNNN)
  2. 扫描该父级下 V0.0.1/plan/<父级>/PLAN.md 与 V0.0.1/code/TASK-(REQ|BUG)-<父级>-*/ 已有 TASK 编码
  3. 取该父级内最大 TASK 编号 + 1
  4. 拼装新编码 `TASK-REQ-<父级>-NNNNN` 或 `TASK-BUG-<父级>-NNNNN`,在 PLAN.md 追加任务行

## 4. 功能需求(FR)

### FR-1:定义新编码格式
- **描述**:正式约定三类编码新格式:
  - **需求**:`REQ-NNNNN`(N 为 0-9,正则 `^REQ-\d{5}$`)
  - **任务**:`TASK-(REQ|BUG)-NNNNN-NNNNN`(正则 `^TASK-(REQ|BUG)-\d{5}-\d{5}$`,**v2 已锁定为 G4 新嵌套式**):
    - 需求任务:`TASK-REQ-<REQ 数字段>-NNNNN`,如 `TASK-REQ-00001-00001`(REQ-00001 的第 1 个任务)
    - 修复任务:`TASK-BUG-<BUG 数字段>-NNNNN`,如 `TASK-BUG-00001-00001`(BUG-00001 的第 1 个修复任务)
    - 任务序号在**父级内**独立递增:REQ-00001 下的 TASK 从 00001 起,BUG-00001 下的 TASK 从 00001 起,二者不冲突
    - **Q-12 待确认**:"需求编码"在 TASK 编码中是否含 `REQ-` 前缀;默认采用 (a) 仅数字段
  - **缺陷**:`BUG-NNNNN`(正则 `^BUG-\d{5}$`)
  - 容量上限:每类 99999
  - 递增策略:REQ/BUG 全局连续;TASK 序号在父级内连续;跳号视为留白(不重用)
- **入口**:在规则源文件(SKILL.md / 新规则文件)中正式记录
- **前置条件**:Q-7 已锁定;Q-6 / Q-8 / Q-12 待决策
- **主流程**:把上述格式写入"权威定义源"(详见 FR-7)
- **数据变化**:仅文档定义,无运行时数据
- **来源**:M-2(澄清 Q3 选项 B,统一 5 位)+ M-16(v2 锁定 Q-7)+ 分析笔记 §v2 增量补充(G4 新嵌套式)

### FR-2:同步 10 个 SKILL.md 的格式描述
- **描述**:对下列 10 个 SKILL.md,把所有"编码格式"相关描述同步为新格式:
  - `plugins/code-skills/skills/code-init/SKILL.md`
  - `plugins/code-skills/skills/code-version/SKILL.md`
  - `plugins/code-skills/skills/code-rule/SKILL.md`
  - `plugins/code-skills/skills/code-require/SKILL.md`
  - `plugins/code-skills/skills/code-design/SKILL.md`
  - `plugins/code-skills/skills/code-plan/SKILL.md`(任务编号分配逻辑改为"在父级内查最大 TASK 编号 + 1",见 §7 交互 2)
  - `plugins/code-skills/skills/code-it/SKILL.md`(regex 改 `^TASK-(REQ|BUG)-\d{5}-\d{5}$`;**双路径解析**:先看 TASK 编码第 2 段是 REQ 还是 BUG,再按对应路径定位工作目录)
  - `plugins/code-skills/skills/code-unit/SKILL.md`
  - `plugins/code-skills/skills/code-fix/SKILL.md`(BUG-NNN 改 BUG-NNNNN)
  - `plugins/code-skills/skills/code-review/SKILL.md`(派生任务编码规则改写:派生任务仍属同一父级,在父级 TASK 序列内继续递增,如 `TASK-REQ-00001-00002`)
- **入口**:由 `code-it` 实施;`code-review` 复核
- **主流程**:
  1. 对每个 SKILL.md,Grep 关键短语(`REQ-YYYY`、`BUG-NNN`、`<任务编码>`、`<任务序号>`、`<需求编号>`、`^REQ-\d{4}-\d{4}-\d{3}$` 等)
  2. 逐处替换格式描述、示例值、占位符、regex
  3. 保留 frontmatter (`name`/`description`) 不变(skill-conventions §规则 1)
- **数据变化**:10 个 SKILL.md 文本变更
- **来源**:M-3 + M-16(v2 锁定 Q-7)+ 关联需求 EXISTING-001 ~ EXISTING-010

### FR-3:同步全部模板文件
- **描述**:对 `plugins/code-skills/skills/*/templates/*.md` 与 `plugins/code-skills/skills/*/checklists/*.md` 中含编码示例值/占位符的所有文件,统一替换为新格式:
  - 占位符:`<REQ-YYYY-NNNN>` → `<REQ-NNNNN>`、`<BUG-NNN>` → `<BUG-NNNNN>`、`<任务编码>`(旧嵌套)→ `<TASK-REQ-NNNNN-NNNNN>` 或 `<TASK-BUG-NNNNN-NNNNN>`(视任务类型)
  - 示例值:`REQ-2026-0001` → `REQ-00001`、`BUG-001` → `BUG-00001`、`REQ-2026-0001-001` → `TASK-REQ-00001-00001`(需求任务示例)
  - **Q-12 待确认**:`TASK-REQ-` 后是否紧跟 `REQ-` 前缀(默认仅数字段)
- **入口**:由 `code-it` 实施;`code-review` 复核
- **主流程**:Glob 全部 templates / checklists → 逐文件 Grep + Edit
- **数据变化**:多个模板文本变更
- **来源**:M-4 + M-16(v2 锁定 Q-7)

### FR-4:同步 README.md / README.en.md
- **描述**:把中英文 README 中所有编码格式示例与命令示例同步为新格式:
  - `code-require <REQ-YYYY-NNNN>` → `code-require <REQ-NNNNN>`
  - `code-it REQ-YYYY-NNNN-001` → `code-it TASK-NNNNN`(视 Q-7)
  - `code-plan BUG-NNN` → `code-plan BUG-NNNNN`
  - "编码对照表"(若 README 有)同步
- **入口**:由 `code-it` 实施;**中英文同次提交**(doc-conventions §规则 1)
- **主流程**:同 FR-3
- **数据变化**:README.md 与 README.en.md 文本变更
- **来源**:M-5 + M-6 + 关联规范 doc-conventions §规则 1/2

### FR-5:同步 CLAUDE.md
- **描述**:CLAUDE.md 第 24/88/99/100 行等含 `BUG-NNN`、`REQ-YYYY-NNNN` 引用的文字,统一替换为新格式
- **入口**:由 `code-it` 实施
- **主流程**:同 FR-3
- **数据变化**:CLAUDE.md 文本变更
- **来源**:M-7

### FR-6:追溯重命名 REQ-2026-0001 → REQ-00001
- **描述**:把 V0.0.1 现有需求 REQ-2026-0001 完整重命名为 REQ-00001(目录 + 本工作空间引用):
  - 目录:`./assistants/V0.0.1/require/REQ-2026-0001/` → `./assistants/V0.0.1/require/REQ-00001/` ✅ 已于 2026-06-03 20:20 提前落地
  - 本需求(REQ-00002)所有文档中对 REQ-2026-0001 的"当前"引用同步更新(历史/审计字面值保留)
  - 版本看板 `./assistants/V0.0.1/RESULT.md` 同步:需求清单行 + 变更记录追加条目 ✅ 已完成
- **入口**:由 `code-it` 实施(本工作空间部分由 `code-require` 提前完成)
- **前置条件**:本工作空间维度已无前置
- **未完成维度**(本 FR 仍由 REQ-00002 `code-it` 阶段负责):
  - SKILL.md / 模板 / README / CLAUDE.md / V0.0.0 EXISTING-* 中"REQ-2026-0001"字符串的清理(由 FR-2/FR-3/FR-4/FR-5 覆盖)
  - `migration-mapping.md` 写入(取决于 Q-9)
- **主流程**:
  1. ✅ `mv REQ-2026-0001/ REQ-00001/`
  2. ✅ 本工作空间 + 看板中"当前"引用同步
  3. 后续:`code-it` 阶段在完成 FR-2/FR-3/FR-4/FR-5 时,自动清理其它文件中的旧编码
- **分支/异常**:若 REQ-2026-0001 下游(design/plan/it/review)已产出文件,一并重命名;若未启动,只改 require/ 目录
- **数据变化**:目录重命名 + 多个文件文本变更
- **来源**:M-2(澄清 Q2 = 追溯覆盖)+ M-8

### FR-7(条件 — Q-8):新建 `./assistants/rules/encoding-conventions.md`
- **描述**:**若 Q-8 = (a)**:由 `code-rule` 技能在本需求实施阶段创建该规则文件,作为"编码格式"的**权威约束源**:
  - 三类编码格式定义(正则、位数、容量、递增策略)
  - 适用范围(所有 `code-*` 技能在产出编码时强制读取)
  - 历史编码兼容策略(EXISTING- 前缀如何处理,取决于 Q-6)
  - 与各 SKILL.md 的关系(各 SKILL.md 不再硬编码格式,改为引用本规则)
- **入口**:本需求**不直接写入** `./assistants/rules/`;实施阶段(`code-it`)由用户调 `code-rule` 创建
- **若 Q-8 = (b)**:不新建规则文件,格式定义散布在 10 个 SKILL.md 中,FR-2 必须穷尽
- **数据变化**:`./assistants/rules/encoding-conventions.md` 新增(若 Q-8 = a)
- **来源**:M-2(部分)+ 分析笔记 §假设 A4

### FR-8(条件 — Q-9):持久化新旧编码映射表
- **描述**:**若 Q-9 = (a)**:在 `./assistants/V0.0.1/require/REQ-00002/migration-mapping.md` 中记录:
  - 表:旧编码 → 新编码、改名时间、涉及文件清单
  - 已知映射:`REQ-2026-0001` → `REQ-00001`
  - (取决于 Q-6)EXISTING-001~010 是否纳入
- **入口**:由 `code-it` 实施
- **数据变化**:新增 `migration-mapping.md`
- **来源**:分析笔记 §假设 A5

### FR-9:版本看板与变更记录同步
- **描述**:
  - V0.0.1 版本看板"需求清单"行 REQ-2026-0001 重命名为 REQ-00001;追加 REQ-00002 行
  - V0.0.1 "变更记录"追加多条:本需求新增、REQ-2026-0001 重命名、(若 Q-6 = H2)EXISTING- 重命名
  - V0.0.0 版本看板:若 Q-6 决定 EXISTING- 一并改名,同步更新;否则不动 V0.0.0
- **入口**:由本技能(`code-require`)在收尾时执行(本需求"新增"行的同步);REQ-2026-0001 重命名条目由 `code-it` 阶段执行
- **数据变化**:V0.0.1/RESULT.md(本轮); 后续 V0.0.0/RESULT.md(取决于 Q-6)
- **来源**:M-15

### FR-10:不修改 marketplace.json / plugin.json / 仓库目录 / git 远端
- **描述**:严格不动:
  - `.claude-plugin/marketplace.json`
  - `plugins/code-skills/.claude-plugin/plugin.json`
  - 文件系统目录(`plugins/code-skills/`)
  - git 远端仓库名
- **入口**:作为反向约束,全程
- **数据变化**:无
- **来源**:本需求范围限定为"编码格式",不重叠 REQ-00001 范围

## 5. 非功能需求 / 约束(NFR)

### NFR-1(可维护性 — 单一事实源)
- **强烈建议**(Q-8 = a 时强制):编码格式定义有唯一权威源(规则文件);各 SKILL.md 引用该规则,不硬编码

### NFR-2(协议合规)
- **doc-conventions §规则 1**:README.md / README.en.md 中所有编码示例必须**同次提交**同步;任何中文版改动必须有对应英文版改动
- **doc-conventions §规则 2**:README 中所有命令示例必须与改后实际状态一致;旧格式命令必须 0 残留
- **dashboard-conventions §规则 1**(条件触发):若改动 `version-RESULT.md` 模板或字段语义说明,必须同时改三处(模板 + CLAUDE.md + 本规范)
- **skill-conventions §规则 1**:本需求不改 SKILL.md frontmatter,仅改正文 → 不触发,但仍需保持 frontmatter 完整

### NFR-3(可观测性 / 追溯)
- 改动可追溯到本需求 REQ-00002;在 V0.0.1 版本看板"变更记录"区段保留完整时间线
- (条件)`migration-mapping.md` 提供长期查询

### NFR-4(向后兼容)
- 本仓库内 git 历史 commit log 中残留旧编码视为正常(不可改),禁止 `git rebase` 重写历史
- 实施完成后 cache 副本由用户执行 `/reload-plugins` 自动同步;不在本需求范围(README 提示即可)

### NFR-5(最小化与避免过度设计)
- 不引入编码"自动校验脚本"(本仓库无 lint 体系,加脚本超范围)
- 不引入"编码自动生成器"(沿用 AI + 人工方式)
- Q-9 选 (a) 时,migration-mapping.md 字段仅必要项;不引入数据库/JSON 索引

### NFR-6(范围隔离)
- 本需求**不重叠** REQ-00001(原 REQ-2026-0001)的 marketplace 改名范围
- 本需求**不**修改 `.claude-plugin/`、`plugins/code-skills/.claude-plugin/`、git 远端
- 本需求**不**修改 V0.0.0/EXISTING-NNN 文件内文本(除非 Q-6 = H2 → 触发 FR-9 扩展)

### NFR-7(安全)
- 无新增安全面;仅文档与格式约定文本变更

## 6. 页面与界面
- **不适用**:纯文档/规则约定变更,无 GUI

## 7. 交互逻辑

### 交互 1:本需求与 REQ-00001(原 REQ-2026-0001)的实施顺序
- **触发**:用户决定何时进入 `code-design` / `code-plan` / `code-it`
- **推荐流程**:
  ```
  REQ-2026-0001(原)
  → code-design → code-plan → code-it → code-unit → code-review
  → 全部完成(marketplace 改名落地)
  → 切换:用户调 code-design REQ-00002 → ... → code-it
  → 实施中:把 require/REQ-2026-0001/ 与下游 design/plan/code/test/review 全部重命名为 REQ-00001
  → migration-mapping.md 记录映射
  ```
- **关键规则**:
  - REQ-2026-0001 实施期间,新编码尚未生效 — 仍用 REQ-2026-0001
  - REQ-00002 实施期间(最后一步)统一重命名
- **空状态/异常**:若用户选择反向顺序(先 REQ-00002 后 REQ-2026-0001),需手动处理 REQ-2026-0001 → REQ-00001 重命名的 propagation 到 REQ-2026-0001 的下游阶段;增量更新本需求 FR-6 范围

### 交互 2:`code-plan` 在 Q-7 = G4 下分配 TASK 编号
- **触发**:`code-plan` 拆分任务
- **前置**:用户明确任务所属父级(REQ-NNNNN 或 BUG-NNNNN)
- **流程**:
  1. 解析父级编码类型(从 TASK 编码第 2 段 `REQ` / `BUG` 推断,或用户显式告知)
  2. `Glob ./assistants/V0.0.1/plan/<父级>/PLAN.md` 与 `./assistants/V0.0.1/code/TASK-<父类型>-<父级>-*/` 同父级下的所有 TASK 编码
  3. `Grep ^TASK-(REQ|BUG)-<父级数字段>-\d{5}` 取父级内已用最大值
  4. 新任务 = 父级内 max + 1,格式化为 5 位
  5. 拼装新编码:`TASK-REQ-<父级>-NNNNN` 或 `TASK-BUG-<父级>-NNNNN`
  6. 在 PLAN.md 中追加任务行(无需"所属需求"列 — 编码已自描述)
- **关键规则**:
  - 父级内递增;不同父级的 TASK 编号互不冲突,各自从 00001 起
  - 跳号视为留白(不重用)
  - 派生任务(code-review 派生的"审查改修")仍在原任务所属父级内继续递增
- **异常**:
  - 并发拆分(两次 code-plan 同时跑)— 本仓库为单用户单线程,暂不考虑
  - 父级编码不合法 → `code-plan` 报错,要求用户确认父级(REQ / BUG + 5 位数字)

## 8. 数据与状态

### 核心实体
- **需求(REQ)**:编码 `REQ-NNNNN`、标题、状态、所属版本
- **任务(TASK)**(v2 锁定 G4 新嵌套式):
  - 需求任务:`TASK-REQ-<REQ 数字段>-NNNNN`,如 `TASK-REQ-00001-00001`
  - 修复任务:`TASK-BUG-<BUG 数字段>-NNNNN`,如 `TASK-BUG-00001-00001`
  - 包含字段:标题、状态(开发/测试双轴)、所属父级(从编码可解析,无需"所属需求"列)
- **缺陷(BUG)**:编码 `BUG-NNNNN`、严重度、状态

### 实体关系
- REQ 1:N TASK(需求任务)— 关联通过 TASK 编码第 2、3 段
- BUG 1:N TASK(修复任务)— 关联通过 TASK 编码第 2、3 段
- TASK 编码自带父子关系,无需 PLAN.md 加"所属需求"列
- REVIEW 派生的"审查改修"任务:在原任务的父级(REQ 或 BUG)内继续递增,如原任务 `TASK-REQ-00001-00001` 的派生改修任务为 `TASK-REQ-00001-00002`
- REQ / BUG 各自独立全局计数(容量各 99999);TASK 序号在父级内独立计数(每父级容量 99999)

### 状态生命周期
- 编码本身无状态;编码所属实体的状态在 SKILL.md / 模板中各自描述
- TASK 状态双轴:开发(`待开始` / `进行中` / `已完成`)与 测试(`未编写` / `已编写` / `已运行-通过` / `已运行-失败` / `不适用` / `阻塞`)

### 数据来源
- 编码值由 AI / 用户在 `code-require` / `code-plan` / `code-fix` 阶段交互式分配
- TASK 编码的父级由用户在调 `code-plan` 时显式指定;`code-it` 通过第 2 段(REQ/BUG)反推工作目录路径
- 规则定义源:本次实施的 `encoding-conventions.md`(若 Q-8 = a)或各 SKILL.md(b)

### 数据保留
- 历史编码与新编码的映射保留在 `migration-mapping.md`(若 Q-9 = a)
- git 历史无限期保留

## 9. 边界与异常

| 场景 | 处理方式 |
| --- | --- |
| 编号超过 99999 | 当前不可预见(超出本仓库可见用量);若必要,扩展至 6 位需新建独立 REQ |
| 重命名时漏掉某文件的旧编码字符串 | `code-review` 阶段穷举 Grep `REQ-2026-0001`、`BUG-NNN`(无后续 5 位)、`REQ-YYYY` 等 |
| Q-6 选 H1 后,用户重跑 code-init 期望按新格式生成 EXISTING- 失败 | code-init SKILL.md 明确"EXISTING- 不参与本次编码统一,保留 3 位前缀 NNN";若用户希望新项目按 REQ-NNNNN 起步,可直接调 code-require 而非 code-init(本需求不强制改 code-init) |
| TASK 全局计数与 PLAN.md 中"所属需求"列脱钩 | v2 锁定 G4 后,TASK 编码自带父子关系(`TASK-REQ-<REQ>-NNNNN`),PLAN.md **无需**"所属需求"列;原风险项(v1 假设 G1 时的强制约束)失效 |
| 实施过程中 REQ-2026-0001 与 REQ-00002 工作目录并存 | 文档内显式标注"过渡期:见 migration-mapping.md" |
| cache 副本未及时刷新导致 AI 仍按旧规则产出 | README 提示"实施后必须 /reload-plugins";不在本仓库可控范围 |
| git 历史 commit log 含旧编码 | 不修改 git 历史;新提交 commit message 注明"格式变更见 REQ-00002" |
| 用户在过渡期同时跑 REQ-2026-0001 与 REQ-00002 的下游阶段 | 推荐 related-requirements.md §实施顺序建议;若坚持并行,FR-6 范围需手动扩展 |

## 10. 验收标准(AC)

### AC-1:新格式正则与定义已写入权威源
- **对应需求**:FR-1, FR-7
- **验证方式**:Read 权威源文件
- **步骤**:
  1. **Q-8 = a 时**:`Read ./assistants/rules/encoding-conventions.md`,确认含三类正则 + 位数 + 容量 + 递增策略 + 适用范围
  2. **Q-8 = b 时**:各 SKILL.md 中"格式"段一致(任选 2 个交叉验证)
- **预期结果**:权威源明确无歧义
- **优先级**:高

### AC-2:10 个 SKILL.md 中旧格式 0 残留
- **对应需求**:FR-2
- **验证方式**:Grep
- **步骤**:
  1. `Grep "REQ-YYYY"` 在 plugins/code-skills/skills/**/SKILL.md → 0 命中
  2. `Grep "BUG-NNN[^NN]"` → 0 命中(确保不留 3 位 BUG)
  3. `Grep "^REQ-\\d{4}-\\d{4}-\\d{3}\$"` → 0 命中(code-it 旧 regex)
  4. `Grep "<任务编码>" + "格式 `<需求编号>-<任务序号>`"` → 0 命中(旧嵌套式占位符)
  5. `Grep "^TASK-\\d{5}\$"` → 0 命中(旧的全局独立计数假设 G1,确认未残留)
  6. `Grep "^TASK-(REQ|BUG)-\\d{5}-\\d{5}\$"` → 命中(确认 v2 新 regex 已落地)
- **预期结果**:步骤 1-5 全部 0 命中,步骤 6 命中
- **优先级**:高

### AC-3:全部模板与 checklists 中旧格式 0 残留
- **对应需求**:FR-3
- **验证方式**:Grep
- **步骤**:
  1. 同 AC-2 步骤 1-4 的关键短语,在 `plugins/code-skills/skills/*/templates/**/*.md` 与 `plugins/code-skills/skills/*/checklists/**/*.md` 范围
  2. `Grep "REQ-2026-0001-001"` → 0 命中(旧任务示例)
  3. `Grep "TASK-REQ-00001-00001"` 或 `TASK-BUG-00001-00001` → 命中(新任务示例已替换)
- **预期结果**:旧格式 0 残留,新格式示例已落地(除非示例语境必须保留旧格式说明,均改为新格式)
- **优先级**:高

### AC-4:README.md 与 README.en.md 同步,旧格式 0 残留
- **对应需求**:FR-4
- **验证方式**:Grep + 并列对比 + git log
- **步骤**:
  1. Grep 关键短语在两个 README → 0 命中
  2. 二级标题并列对仗(doc-conventions §规则 1)
  3. `git log --oneline -- README.md README.en.md` 确认同一 commit 同步
- **预期结果**:无命中 + 结构对仗 + 单次 commit
- **优先级**:高

### AC-5:CLAUDE.md 已同步,旧格式 0 残留
- **对应需求**:FR-5
- **验证方式**:Grep
- **步骤**:Grep 关键短语在 CLAUDE.md
- **预期结果**:无命中
- **优先级**:中

### AC-6:REQ-2026-0001 已完整重命名为 REQ-00001(本工作空间维度)
- **对应需求**:FR-6
- **验证方式**:目录列举 + 本工作空间 Grep
- **步骤**:
  1. ✅ `ls ./assistants/V0.0.1/require/` → 含 `REQ-00001/`,不再含 `REQ-2026-0001/`
  2. ✅ V0.0.1 看板"需求清单"行已使用 `REQ-00001`
  3. ✅ REQ-00001 工作空间内"当前"引用 0 残留 REQ-2026-0001(历史/审计字面值保留)
  4. **剩余**(由 `code-it` 阶段在 FR-2/FR-3/FR-4/FR-5 实施时自动完成):`Grep "REQ-2026-0001"` 在 SKILL.md / 模板 / README / CLAUDE.md / V0.0.0 EXISTING-* → 0 命中
- **预期结果**:0 残留
- **优先级**:高

### AC-7(条件 — Q-8 = a):`encoding-conventions.md` 已新建并被各 SKILL.md 引用
- **对应需求**:FR-7
- **验证方式**:Read + Grep
- **步骤**:
  1. Read `./assistants/rules/encoding-conventions.md`
  2. 每个 SKILL.md "编码"段含一句引用"详见 `./assistants/rules/encoding-conventions.md`"
- **预期结果**:权威源 + 各 SKILL.md 引用齐全
- **优先级**:高(若 Q-8 = a)/ 不适用(若 b)

### AC-8(条件 — Q-9 = a):`migration-mapping.md` 已写入并完整
- **对应需求**:FR-8
- **验证方式**:Read
- **步骤**:Read `./assistants/V0.0.1/require/REQ-00002/migration-mapping.md`,确认:
  - 表头清晰(旧编码 / 新编码 / 改名时间 / 涉及文件)
  - 至少含 `REQ-2026-0001 → REQ-00001` 一行
  - (Q-6 = H2 时)含 EXISTING- 全部 10 行
- **预期结果**:映射完整,可追溯
- **优先级**:中

### AC-9:版本看板已同步
- **对应需求**:FR-9
- **验证方式**:Read
- **步骤**:
  1. `Read ./assistants/V0.0.1/RESULT.md`,"需求清单"含 REQ-00001 + REQ-00002 行(不再含 REQ-2026-0001)
  2. "变更记录"含本需求新增、重命名、(可选)规则文件新建
  3. (Q-6 = H2 时)V0.0.0/RESULT.md 同步
- **预期结果**:看板与目录文件一致
- **优先级**:高

### AC-10:不触动 marketplace.json / plugin.json / 仓库目录 / git 远端
- **对应需求**:FR-10
- **验证方式**:`git diff --stat`
- **步骤**:
  1. diff 中不含 `.claude-plugin/marketplace.json`(除非 REQ-00001 共同 commit)
  2. 不含 `plugins/code-skills/.claude-plugin/plugin.json`
  3. `git remote -v` 无重命名
- **预期结果**:0 不预期变更
- **优先级**:高

### AC-11(条件):所有 SKILL.md frontmatter (name + description) 完整且 name 与目录一致
- **对应需求**:NFR-2(skill-conventions §规则 1)
- **验证方式**:Grep frontmatter
- **步骤**:对每个 SKILL.md,确认 `name: <kebab-case>` 与目录名一致;`description` 非空
- **预期结果**:全部合规
- **优先级**:高

## 11. 关联需求

| 关联需求编码 | 关联点 | 对本需求的影响 | 链接 |
| --- | --- | --- | --- |
| REQ-00001(原 REQ-2026-0001,已重命名) | 同版本(V0.0.1)的另一活跃需求,本需求 FR-6 部分已提前落地(目录 + 本工作空间引用);两需求实施顺序见 related-requirements.md | 强(必须协调实施顺序) | [RESULT.md](../REQ-00001/RESULT.md) |
| EXISTING-001 ~ EXISTING-010(V0.0.0) | 10 个技能的"现有功能"基线;本需求横切影响这 10 个技能的 SKILL.md | 强 | 详见 `related-requirements.md` |

## 12. 待澄清 / 未决项

| 编号 | 状态 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- | --- |
| Q-6 | 待澄清 | V0.0.0 下的 EXISTING-001 ~ EXISTING-010 是否一并纳入"追溯覆盖"?H1=保留 / H2=改 REQ-NNNNN / H3=折中 | 影响 FR-9 范围、code-init SKILL.md 是否需重写、`migration-mapping.md` 行数 | 用户 | `code-design` 前 |
| Q-7 | **已锁定**(2026-06-03 20:18) | TASK 编码结构 → 采纳 G4 新嵌套式 `TASK-(REQ\|BUG)-NNNNN-NNNNN`(详见 FR-1、§7 交互 2、§8) | — | — | — |
| Q-8 | 待澄清 | 是否新建 `./assistants/rules/encoding-conventions.md` 作为权威源?a=是 / b=否(散在各 SKILL.md) | 影响 FR-7 是否落地、AC-7 是否适用 | 用户 | `code-design` 前 |
| Q-9 | 待澄清 | 是否持久化 `migration-mapping.md`?a=写入 / b=仅 commit message / c=不记录 | 影响 FR-8 是否落地、AC-8 是否适用 | 用户 | `code-design` 前 |
| Q-10 | 待澄清 | cache 同步是否需要在 README 增加显式提示?a=加 / b=不加(本仓库默认 b) | 影响 README 是否再加一句 | 用户 | `code-it` 前 |
| Q-11 | 待澄清 | 本需求与 REQ-2026-0001(REQ-00001)的实施顺序是否采用推荐顺序(REQ-00001 先全程,REQ-00002 最后)? | 影响 FR-6 范围(若反序,需扩展 FR-6 至 REQ-00001 下游各阶段产出物) | 用户 | `code-design` 前 |
| Q-12 | **待澄清**(v2 新增) | "需求编码"在 TASK 编码中是否含 `REQ-` 前缀?a=仅数字段(默认采用,如 `TASK-REQ-00001-00001`)/ b=含 `REQ-` 前缀(如 `TASK-REQ-REQ-00001-00001`) | 影响 FR-1 正则字面量、FR-2 各 SKILL.md 文本、FR-3 模板示例、AC-2/AC-3 Grep 模式 | 用户 | `code-design` 前 |

## 13. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-03 20:14 | v1 | 初始创建 | 完成首次需求澄清:确定本需求编码 REQ-00002(新格式提前采用)、追溯覆盖范围、三类编码统一 5 位;产出 10 条 FR / 7 条 NFR / 11 条 AC / 6 项待澄清(Q-6 ~ Q-11) | wangmiao |
| 2026-06-03 20:18 | v2 | 增量更新 | 用户回答 Q-7:TASK 编码锁定为 G4 新嵌套式 `TASK-REQ-<REQ 数字段>-NNNNN`(需求任务)/ `TASK-BUG-<BUG 数字段>-NNNNN`(修复任务)。同步更新:FR-1(新 regex `^TASK-(REQ\|BUG)-\d{5}-\d{5}$`)、FR-2(code-it 双路径解析、code-review 派生规则、code-plan 父级内分配)、FR-3(模板示例 `TASK-REQ-00001-00001`)、AC-2/AC-3(新增 G1 反向校验 + 新 regex 正向校验)、§7 交互 2(父级内分配流程)、§8 数据与状态(实体关系自描述)、§9 边界与异常(去除"所属需求"列约束)。新增 Q-12 待澄清:"需求编码"在 TASK 编码中是否含 `REQ-` 前缀;默认采用 (a) 仅数字段 | wangmiao |
| 2026-06-03 20:20 | v3 | 增量更新 | **FR-6 部分提前落地**:按用户指令,`REQ-2026-0001/` → `REQ-00001/`(本工作空间维度);REQ-00001 目录内 RESULT.md / 5 个过程文档同步;V0.0.1 看板同步;本需求(REQ-00002)RESULT.md §场景 1、§11 关联需求、related-requirements.md §实施顺序建议、materials-index.md M-8、analysis-notes.md §F 表相应更新为"已完成"或"已发生"时态。**未触动**:SKILL.md / 模板 / README / CLAUDE.md / V0.0.0 EXISTING-* — 仍由本需求 `code-it` 阶段统一清理(FR-2/FR-3/FR-4/FR-5)。同步更新:FR-6 描述(标 ✅ 已落地部分 + 剩余维度)、AC-6 步骤(本工作空间维度标 ✅)、§1 概述加注提前落地日期、Q-11 措辞(原"先后实施"顾虑部分消解) | wangmiao |
