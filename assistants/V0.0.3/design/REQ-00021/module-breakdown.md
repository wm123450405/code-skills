# 模块拆分 — REQ-00021

更新时间:2026-06-06 17:20
版本:V0.0.3

## 模块总览

本需求改造 `code-skills` 仓库的 **3 个 code-* 技能 SKILL.md**(code-require / code-design / code-plan)。**不**新增独立子目录或文件。

| 模块 | 路径 | 状态 | 职责 | 对外接口 | 依赖 |
| --- | --- | --- | --- | --- | --- |
| code-require | plugins/code-skills/skills/code-require/SKILL.md | **修改既有** | 需求分析 + 模板参数 `--result` 解析 + 模板填充 | CLI `--result <模板>`;输出 `REQUIRE.<ext>` | Read + Write + Grep |
| code-design | plugins/code-skills/skills/code-design/SKILL.md | **修改既有** | 概要设计 + 模板参数 `--result` 解析 + 模板填充 | CLI `--result <模板>`;输出 `DESGIN.<ext>` | Read + Write + Grep |
| code-plan | plugins/code-skills/skills/code-plan/SKILL.md | **修改既有** | 详细设计 + 模板参数 `--result` + `--plan` 解析 + 模板填充(2 段) | CLI `--result <模板>` `--plan <模板>`;输出 `DESGIN.<ext>` + `PLAN.<ext>` | Read + Write + Grep |

## 修改既有模块

### 模块名:`code-require`
- **路径**:`plugins/code-skills/skills/code-require/SKILL.md`
- **修改点**:
  1. **新增** "## 命令行参数解析(本需求 REQ-00021 新增,FR-1)" 小节(锚点 = "## 工具使用约定" 段后 + "## 工作流程" 前)
  2. **新增** "## 模板填充步骤(本需求 REQ-00021 新增,FR-2)" 小节(锚点 = 末尾 "## 不要做的事" 前)
- **职责(改后)**:
  - 原有职责:需求分析(步骤 0a-0b-0-1-N 流程),产出 `require/<REQ>/RESULT.md`
  - 新增职责(可选):解析 `--result <模板>` 参数;主产出物完成后执行模板填充;产出 `REQUIRE.<ext>` 附加文件
- **对外接口(改后)**:
  - **新增** CLI 参数:`--result <模板文件>`(可选,无值/不存在/二进制/路径穿越 → 屏显 `⚠` 跳过,沿用 INV-9)
- **依赖(改后)**:
  - 沿用既有:Read / Write / Grep / Glob
  - **0** 新增工具依赖
- **变更对既有调用方的影响**:
  - **0 改变**主流程(无 `--result` 时按原行为执行,NFR-3 幂等)
  - **0 改变**既有产出物(`require/<REQ>/RESULT.md` 字节级保留)
  - **0 改变**既有步骤(步骤 0a / 0b.0 / 0 / 1-N 字节级保留)
  - **0 改变**看板(`code-require` 写"需求清单" + "变更记录" 区段;模板产出物**不**触发看板)
- **符合的规范条款**:
  - `skill-conventions.md §规则 1`:`name` 与目录名 `code-require` 一致 + 字节级保留
  - `skill-conventions.md §规则 1`:frontmatter `name` 字段**字节级保留**
  - `dashboard-conventions.md §规则 1`:**0 触发**三同步(模板产出物**不**是任务;不新增列/枚举/区段)
  - `module-conventions.md §规则 1`(已迁移到 `directory-conventions.md`):过程文档摆放在 `<version>/require/<REQ>/` 根目录;**不**新增子目录
  - `commit-conventions.md`:沿用既有 `chore(<scope>): <subject>` 格式
  - `doc-conventions.md`:0 改中英 README
  - `naming-conventions.md`:基本名 `REQUIRE` 用户原文锁定(NFR-2.7)
  - `dependency-conventions.md`:0 新增依赖

### 模块名:`code-design`
- **路径**:`plugins/code-skills/skills/code-design/SKILL.md`
- **修改点**:
  1. **新增** "## 命令行参数解析(本需求 REQ-00021 新增,FR-1)" 小节(锚点 = "## 工具使用约定" 段后 + "## 工作流程" 前)
  2. **新增** "## 模板填充步骤(本需求 REQ-00021 新增,FR-2)" 小节(锚点 = 末尾 "## 不要做的事" 前)
- **职责(改后)**:
  - 原有职责:概要设计(步骤 0a-0b-0b.0-0-1-N 流程),产出 `design/<REQ>/RESULT.md`
  - 新增职责(可选):解析 `--result <模板>` 参数;主产出物完成后执行模板填充;产出 `DESGIN.<ext>` 附加文件
- **对外接口(改后)**:
  - **新增** CLI 参数:`--result <模板文件>`(可选,沿用 INV-9)
- **依赖(改后)**:
  - 沿用既有:Read / Write / Grep / Glob
  - **0** 新增工具依赖
- **变更对既有调用方的影响**:
  - **0 改变**主流程
  - **0 改变**既有产出物(`design/<REQ>/RESULT.md` 字节级保留)
  - **0 改变**既有步骤(步骤 0a / 0b / 0b.0 / 0 / 1-N 字节级保留)
  - **0 改变**看板(`code-design` 写"概要设计清单" + "变更记录" 区段;模板产出物**不**触发看板)
- **符合的规范条款**:同 `code-require`

### 模块名:`code-plan`
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **修改点**:
  1. **新增** "## 命令行参数解析(本需求 REQ-00021 新增,FR-1)" 小节(锚点 = "## 工具使用约定" 段后 + "## 工作流程" 前)
  2. **新增** "## 模板填充步骤(本需求 REQ-00021 新增,FR-2)" 小节(锚点 = 末尾 "## 不要做的事" 前)
- **职责(改后)**:
  - 原有职责:详细设计 + 任务计划(步骤 0a-0b-0b.0-0-1-N 流程),产出 `plan/<REQ>/RESULT.md` + `plan/<REQ>/PLAN.md`
  - 新增职责(可选):解析 `--result <模板>` + `--plan <模板>` 2 参数;主产出物完成后执行 2 段模板填充;产出 `DESGIN.<ext>`(详设)+ `PLAN.<ext>`(开发计划) 2 个附加文件
- **对外接口(改后)**:
  - **新增** CLI 参数:`--result <模板文件>` + `--plan <模板文件>`(2 个独立可选参数,可同时传 / 单独传 / 都不传;沿用 INV-9)
- **依赖(改后)**:
  - 沿用既有:Read / Write / Grep / Glob
  - **0** 新增工具依赖
- **变更对既有调用方的影响**:
  - **0 改变**主流程
  - **0 改变**既有产出物(`plan/<REQ>/RESULT.md` + `plan/<REQ>/PLAN.md` 字节级保留)
  - **0 改变**既有步骤(步骤 0a / 0b / 0b.0 / 0 / 1-N 字节级保留)
  - **0 改变**看板(`code-plan` 写"详细设计与任务计划汇总" + "任务清单" + "变更记录" 区段;模板产出物**不**触发看板)
  - BUG 路径(REQ-00019):模板填充对 BUG 路径同样生效,但输出目录为 `fix/<BUG-NNN>/` 而非 `plan/<REQ>/` — 由 `code-plan` 内部路径决定
- **符合的规范条款**:同 `code-require`

## 复用既有模块(本需求 0 复用既有能力)

- `code-auto`:**不**修改;`code-auto` 调 3 技能时**不**传 `--result` / `--plan`(沿用 REQ-00007 Q-4 + E-4)
- `code-dashboard` / `code-publish` / `code-review`:本需求**0** 触发

## 新增模块(本需求 0)

- 无
- 模板产出物(`REQUIRE.<ext>` / `DESGIN.<ext>` / `PLAN.<ext>`)是**附加文件**,**不**是独立模块
- 模板产出物路径沿用"主产出物同目录"原则(沿用 `module-conventions §规则 1`)

## 自检:对照 `module-conventions.md §规则 1`(已迁移到 `directory-conventions.md`)

- ✅ 命名符合规范:`REQUIRE` / `DESGIN` / `PLAN` 用户原文锁定(NFR-2.7)
- ✅ 目录位置符合规范:模板产出物放在原主产出物同目录
- ✅ 依赖方向:本需求 0 新增依赖;0 改变 3 技能既有依赖
- ✅ 0 触发禁止模式:0 跨层调用;0 循环依赖

## 自检:对照 `skill-conventions.md §规则 1`

- ✅ frontmatter `name` 字段**字节级保留**(3 技能 L1-3 验证通过)
- ✅ `description` 字段允许小幅扩展(本需求**不**修改)
- ✅ 既有"## 工作流程"小节**0**被破坏(INV-2 验证通过)
- ✅ 既有步骤 0a / 0b / 0 / 1-N **0**被破坏(INV-3 验证通过)
- ✅ "## 衔接" + "## 不要做的事" 段**0**改(INV-4 验证通过)
