# 需求提示词文档 — REQ-00022(修改 `/code-review` 技能名称为 `/code-check`)

- 需求编码:REQ-00022
- 所属版本:V0.0.3
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-07
- 最近更新:2026-06-07
- 当前版本:v1
- **主题**(来自用户输入):
  > 修改 `/code-review` 技能名称为 `/code-check`

---

## 1. 需求概述

**为谁**:`code-skills` 仓库的 AI 协作者 + 项目主导者(在 `code-review` 技能使用场景中,希望"将技能名从 `code-review` 改为 `code-check`",语义更清晰,与 `code-unit` 单元测试 / `code-fix` 缺陷修复形成更明确的"检查类技能"语义)。

**解决什么问题**(3 个子痛点):
- **P-1 命名语义不清晰**:`code-review` 容易被误解为"对人的 review"(绩效评估),实际本技能是"对代码的 check"(代码静态/结构/规范检查)。`code-check` 更准确表达"AI 协作者对代码做系统性检查"
- **P-2 与既有命名不协调**:`code-unit`(单元测试) / `code-fix`(缺陷修复) / `code-it`(开发编码)都是"动作型"命名;`code-review` 偏"角色型"命名;`code-check` 回到"动作型",命名更一致
- **P-3 避免与外部"code review"流程冲突**:部分团队把 PR review 称为 "code review",本技能是"AI 自动化检查"而非"人 review",`code-check` 降低歧义

**带来什么价值**:
1. 1 个技能入口重命名:`/code-review` → `/code-check`
2. 11 类引用方全局同步:SKILL.md(自身) / 10 个其他 SKILL.md / marketplace.json / plugin.json / 4 个 README / CLAUDE.md / 13 份项目级规范 / 6 个技能模板
3. **不**追溯历史:V0.0.2/V0.0.3 历史 review 产物**不**重写,沿用 `migration-mapping §规则 5`
4. 0 新增依赖 / 0 新增文件 / 0 看板字段扩展

---

## 2. 背景与目标

### 2.1 背景

- `code-review` 技能自 V0.0.0 基线以来一直命名为 `code-review`(沿用 `migration-mapping §规则 4` 的 `EXISTING-010` 历史命名)
- 用户在 V0.0.3 周期内认为 `code-review` 命名与"动作型"命名习惯不协调,且与外部"code review"流程易混淆
- 仓库内 `code-review` 字面量出现 250+ 处,影响面广(11 类引用方),但**结构清晰**:
  - 1 个技能入口(`plugins/code-skills/skills/code-review/SKILL.md`)
  - 1 个目录名(`plugins/code-skills/skills/code-review/`)
  - 1 个 marketplace 清单(`skills[]` 路径 + 关键词)
  - 1 个 plugin 清单(关键词)
  - 4 个 README(中英 × 仓库内 / 仓库外)
  - 1 个 CLAUDE.md
  - 13 份项目级规范(`./assistants/rules/*.md` 中的引用)
  - 6 个技能模板(`plugins/code-skills/skills/*/templates/*.md` 中的引用)
  - V0.0.2/V0.0.3 历史 review 产物(`review/REQ-NNNN/*`)— **不**追溯

### 2.2 业务目标

- **G-1**:`code-review` 技能入口重命名为 `code-check`(目录 + frontmatter + H1 + 全文)
- **G-2**:`.claude-plugin/marketplace.json` 中 `code-review` 字面量全部 → `code-check`
- **G-3**:`plugins/code-skills/.claude-plugin/plugin.json` 中 `code-review` 字面量全部 → `code-check`
- **G-4**:10 个其他 SKILL.md 中"code-review"字面量(下游引用)全部 → `code-check`
- **G-5**:4 个 README(仓库内 / 仓库外,中英各 2)+ CLAUDE.md + 13 份项目级规范 + 6 个技能模板全部同步改
- **G-6**:V0.0.2/V0.0.3 历史 review 产物**不**追溯(沿用 `migration-mapping §规则 5`)
- **G-7**:用户输入 `/code-review` 报"未知技能"错误(硬重命名,**不**保留别名)
- **G-8**:`code-check` 技能的"产出物类型"目录仍叫 `review/`(目录名是"产出物类型"不是"技能名")

### 2.3 本次目标(本迭代范围)

1. 重命名 `plugins/code-skills/skills/code-review/` 目录为 `code-check/`
2. 改 `plugins/code-skills/skills/code-check/SKILL.md` 的 frontmatter `name: code-review` → `name: code-check`
3. 改 H1 标题 `# code-review — 代码评审(版本感知)` → `# code-check — 代码检查(版本感知)`
4. 改 `code-check/SKILL.md` 全文中"代码评审"语义可保留(用户中文表述可不变),但 frontmatter `name` 字段必须改
5. 改 `.claude-plugin/marketplace.json`:`skills[]` 路径 `./skills/code-review` → `./skills/code-check`;`keywords[]` 移除 `code-review` 加入 `code-check`;`description` 字符串中 `code-review` → `code-check`
6. 改 `plugins/code-skills/.claude-plugin/plugin.json`:`keywords[]` + `description` 同步改(本文件**不**含 `skills[]` 路径,沿用既有)
7. 改 10 个其他 SKILL.md 的 `description` 字段中"code-review"字面量 → `code-check`
8. 改仓库根 2 个 README(`README.md` / `README.en.md`)+ `plugins/code-skills/README.md` / `README.en.md` + `CLAUDE.md`(沿用 `doc-conventions §规则 1` 中英对仗同步)
9. 改 13 份项目级规范(`./assistants/rules/*.md`)中"code-review"字面量
10. 改 6 个技能模板(`plugins/code-skills/skills/*/templates/*.md`)中"code-review"字面量
11. 改 V0.0.3 当前激活看板(`assistants/V0.0.3/RESULT.md`)中"code-review"字面量(规范引用同步)
12. **不**改 V0.0.0/V0.0.1/V0.0.2 历史版本看板中"code-review"字面量(沿用 `migration-mapping §规则 5`)
13. **不**改 V0.0.2/V0.0.3 历史 review 产物(`assistants/<version>/review/REQ-NNNN/*`)中"code-review"字面量
14. **不**改 `plugins/code-skills/skills/code-fix/templates/bug.md` 中"code-review"字面量(本仓库**不**写代码,模板中示例沿用历史命名可保留)— 实际策略需在 `code-plan` 阶段决定(本需求 0 触发代码逻辑改动)

---

## 3. 用户角色与场景

### 3.1 角色:wangmiao(项目负责人,4 合 1)

### 3.2 关键场景

#### S-1:用户后续调 `/code-check`(主流程)

- 用户输入:`/code-check REQ-00023`
- 技能执行:沿用既有 `code-review` 流程(读取 `plan/<REQ>/PLAN.md` + 按规范评审 + 产出 `review/<REQ>/REVIEW-REPORT.md`)
- 屏显变更:启动时 `正在处理: REQ-00023 · <需求标题>(code-check)`

#### S-2:用户误用旧名 `/code-review`

- 用户输入:`/code-review REQ-00023`
- 技能执行:Claude Code 报"未知技能 `code-review`,请使用 `/code-check`"(由 Claude Code 路由层处理,本技能不感知)
- 后果:用户需主动改输入习惯

#### S-3:`code-auto` 调子技能时(沿用既有)

- `code-auto` 步骤 5 调 `code-check REQ-00023`(原 `code-review`)
- `code-auto` SKILL.md 同步改 `code-review` → `code-check`(FR-4)

#### S-4:历史 review 产物回溯(沿用既有)

- 用户读 `assistants/V0.0.2/review/REQ-00015/REVIEW-REPORT.md` 时,内容中仍含"code-review"字面量
- 不需改:沿用 `migration-mapping §规则 5` 历史快照不变更原则

---

## 4. 功能需求(FR)

### FR-1:`code-review` 技能入口硬重命名为 `code-check`

- **描述**:重命名 `plugins/code-skills/skills/code-review/` 目录为 `code-check/`;改 `SKILL.md` 的 frontmatter `name: code-review` → `name: code-check`;改 H1 标题 `# code-review — 代码评审(版本感知)` → `# code-check — 代码检查(版本感知)`;SKILL.md 全文中"code-review"字面量 → "code-check"(中文表述"代码评审"可保留或改为"代码检查",**不强求**)
- **优先级**:必须
- **主流程**:
  1. `git mv plugins/code-skills/skills/code-review plugins/code-skills/skills/code-check`(保留 git 历史)
  2. `Edit` SKILL.md frontmatter `name: code-review` → `name: code-check`
  3. `Edit` SKILL.md H1 标题
  4. 全文 `Grep` + `Edit` 替换 "code-review" 字面量
- **分支/异常**:
  - **E-1**:`skill-conventions §规则 1`:`name` 与目录名**必须**一致;违反即视为不通过
- **数据变化**:
  - 1 个目录名 `code-review/` → `code-check/`
  - 1 个文件 SKILL.md(frontmatter + H1 + 全文字面量)
- **来源**:Q-1 用户采纳硬重命名

### FR-2:marketplace.json + plugin.json 全部同步改

- **描述**:`.claude-plugin/marketplace.json` + `plugins/code-skills/.claude-plugin/plugin.json` 中所有"code-review"字面量 → "code-check",包括:
  - `marketplace.json` `plugins[].skills[]` 路径 `./skills/code-review` → `./skills/code-check`
  - `marketplace.json` `plugins[].keywords[]` 移除 `code-review` 加入 `code-check`
  - `marketplace.json` `plugins[].description` 中 `code-review` → `code-check`
  - `plugin.json` `keywords[]` 移除 `code-review` 加入 `code-check`
  - `plugin.json` `description` 中 `code-review` → `code-check`
- **优先级**:必须
- **主流程**:`Read` 2 个 JSON + `Edit` 字面量 + `Bash: jq .` 校验 JSON 合法性
- **分支/异常**:
  - **E-2**:`marketplace-protocol §规则 1`:`skills[]` 路径必须指向实际目录;路径改了但目录未重命名 → 报错
- **数据变化**:
  - 1 个 marketplace.json(根)
  - 1 个 plugin.json(子插件)
- **来源**:Q-2 用户采纳全部同步改

### FR-3:10 个其他 SKILL.md 的 `description` 字段同步改

- **描述**:`code-auto` / `code-design` / `code-require` / `code-plan` / `code-it` / `code-unit` / `code-fix` / `code-publish` / `code-dashboard` / `code-version` / `code-rule` 共 11 个 SKILL.md(实际 10 个,因 `code-check` 自身在 FR-1 已改)的 `description` 字段中"code-review"字面量 → "code-check"
- **优先级**:必须
- **主流程**:`Grep "code-review"` + 定位各 SKILL.md `description` 字段 + `Edit` 字面量
- **分支/异常**:
  - **E-3**:`skill-conventions §规则 1`:frontmatter `name` 字段**不**可改(其他 SKILL.md 的 `name` 字段是各自的,本需求不涉及)
- **数据变化**:
  - 10 个其他 SKILL.md(只改 `description` 字段中字面量,**不**改 `name` 字段)
- **来源**:Q-3 用户采纳全部同步改

### FR-4:仓库级 README + CLAUDE.md + 13 份项目级规范 + 6 个技能模板全部同步改

- **描述**:
  - 仓库根 `README.md` / `README.en.md`
  - `plugins/code-skills/README.md` / `README.en.md`
  - 仓库根 `CLAUDE.md`
  - 13 份项目级规范(`./assistants/rules/*.md`)
  - 6 个技能模板(`plugins/code-skills/skills/*/templates/*.md`)
  - V0.0.3 当前激活看板(`assistants/V0.0.3/RESULT.md`)中"code-review"字面量
  - 全部"code-review"字面量 → "code-check"
- **优先级**:必须
- **主流程**:`Grep -l "code-review"` 列出所有命中文件 + 逐文件 `Edit` 替换 + `Grep "code-review"` 校验无残留(本需求范围内)
- **分支/异常**:
  - **E-4**:`doc-conventions §规则 1`:中英 README 同步改,不允许漂移
  - **E-5**:`migration-mapping §规则 5`:V0.0.0 / V0.0.1 / V0.0.2 / V0.0.3 历史版本**不**追溯(除 V0.0.3 当前激活看板)
- **数据变化**:
  - 4 个 README(中英 × 2 组)
  - 1 个 CLAUDE.md
  - 13 份项目级规范
  - 6 个技能模板
  - 1 个 V0.0.3 当前激活看板
  - 共 **25 个文件**
- **来源**:Q-3 + Q-4 用户采纳全部同步改 + 历史不追溯

### FR-5:V0.0.0 / V0.0.1 / V0.0.2 历史版本内容不追溯

- **描述**:`assistants/V0.0.0/` / `V0.0.1/` / `V0.0.2/` 目录下**所有**文件中"code-review"字面量**不**追溯替换;V0.0.3 历史 review 产物(`assistants/V0.0.3/review/REQ-NNNN/*`)**不**追溯替换
- **优先级**:必须
- **主流程**:**不**执行任何替换操作
- **分支/异常**:
  - **E-6**:`migration-mapping §规则 5`:`EXISTING-010` 在 migration-mapping.md L156 中**保留**旧名(规范"映射表"段落);本需求**不**改 migration-mapping.md 的"`EXISTING-010` → 代码评审(`code-review`)"行(沿用历史快照)
- **数据变化**:**0**(无文件改动)
- **来源**:Q-4 用户采纳历史不追溯

### FR-6:不修改其他 10 个 `code-*` 技能的行为

- **描述**:本需求**只**改字面量(目录名 / frontmatter / description / 文档中"code-review"字面量),**不**改任何技能的"## 工作流程" / "## 衔接" / "## 不要做的事" 章节
- **优先级**:必须
- **AC**:
  - AC-6.1:11 个 SKILL.md(包括 `code-check` 自身)的"## 工作流程"小节**字节级保留**
  - AC-6.2:11 个 SKILL.md 的"## 衔接" / "## 不要做的事" 段**字节级保留**
  - AC-6.3:11 个 SKILL.md 的 frontmatter `name` 字段中,只有 `code-check` 自身从 `code-review` → `code-check`,其余 10 个**0 改**
- **来源**:本需求强约束

### FR-7:不变量自检(INV)

- **描述**:本需求完成后,既有 frontmatter(除 `code-check` 自身)/ 步骤 / 看板 / 规范(除"code-review"字面量)的字节级保留
- **优先级**:必须
- **AC**:
  - **INV-1**:11 个 SKILL.md(除 `code-check` 自身)的 frontmatter `name` 字段**字节级保留**;`code-check` 自身的 `name` 字段**必须**从 `code-review` 改为 `code-check`
  - **INV-2**:11 个 SKILL.md 的既有"## 工作流程"小节**不**被破坏
  - **INV-3**:11 个 SKILL.md 的"## 衔接" + "## 不要做的事"段**不**改
  - **INV-4**:V0.0.3 看板"任务清单"区段字段**0 新增**(本需求 0 派生任务)
  - **INV-5**:本需求**0** 修改 `marketplace.json` / `plugin.json` 之外的其他 JSON 配置
  - **INV-6**:本需求**0**派生"更新看板"任务(REQ-00017 强约束)
  - **INV-7**:本需求**0**触发 `dashboard-conventions §规则 1` 三同步(看板字段 0 新增)
  - **INV-8**:本需求**0**触发 `dependency-conventions`(0 新增依赖;硬重命名无需新工具)
  - **INV-9**:本需求后 `code-check` 技能的行为与 `code-review` 技能**完全一致**(NFR-1 强约束)— 改名**不**改行为
- **来源**:本需求强约束

---

## 5. 非功能需求 / 约束(NFR)

### 5.1 行为一致性(NFR-1)
- 重命名后,`code-check` 技能的所有工作流步骤 / 屏显格式 / 错误码 / 边界异常 / 屏显契约**与 `code-review` 完全一致**
- 唯一的差异是:技能入口名(`code-review` → `code-check`)、目录名(同样改)、H1 标题(同样改)
- 验证手段:对照 `code-check/SKILL.md` 全文与 `code-review/SKILL.md` 的 git diff,**应**只有字面量差异,无语义差异

### 5.2 兼容性(NFR-2)
- **NFR-2.1**:`dashboard-conventions §规则 1` 0 触发(看板字段 0 新增)
- **NFR-2.2**:`encoding-conventions §规则 1/3` 0 触发(本需求 0 改编号)
- **NFR-2.3**:`skill-conventions §规则 1`:**仅** `code-check` 自身 `name` 字段必须改;其余 10 个 SKILL.md 的 `name` 字段**0 改**
- **NFR-2.4**:`marketplace-protocol §规则 1` 触发(路径改 / 关键词改 / description 改)
- **NFR-2.5**:`commit-conventions` 沿用既有(`chore(<scope>): <subject>`)
- **NFR-2.6**:`doc-conventions §规则 1` 触发(中英 README 同步)
- **NFR-2.7**:`naming-conventions`:基本名 `code-check` 用户原文锁定
- **NFR-2.8**:`dependency-conventions` 0 触发(0 新增依赖)
- **NFR-2.9**:`module-conventions §规则 1` 0 触发(模板摆放在原位,只是字面量改)
- **NFR-2.10**:`migration-mapping §规则 5` 沿用(V0.0.0 / V0.0.1 / V0.0.2 / V0.0.3 历史 review 产物不追溯)

### 5.3 可靠性(NFR-3)
- **NFR-3.1**:`git mv` 保留历史(不丢失 git blame)
- **NFR-3.2**:`Edit` 替换后 `Grep "code-review"` 在本需求范围内**应**无残留
- **NFR-3.3**:`jq .` 校验 2 个 JSON 合法性(`marketplace.json` + `plugin.json`)
- **NFR-3.4**:`code-auto` 调子技能时,子技能名从 `code-review` 改为 `code-check`(FR-3 同步改 `code-auto/SKILL.md`)

### 5.4 可观测性(NFR-4)
- **NFR-4.1**:屏显格式沿用 REQ-00013(从已有内容派生,不新增字段)
- **NFR-4.2**:`analysis-notes.md` 记录本次重命名的"全局字符串替换影响面 + 不追溯范围"
- **NFR-4.3**:`clarifications.md` 记录 4 项用户回答(已落)

### 5.5 可维护性(NFR-5)
- **NFR-5.1**:本需求涉及约 25-30 个文件改动(11 SKILL.md + 1 目录重命名 + 2 JSON + 4 README + 1 CLAUDE.md + 13 规范 + 6 模板 + 1 看板);**单次** commit(避免拆分);commit message 沿用 `chore(<scope>): <subject>` 格式
- **NFR-5.2**:硬重命名后,`code-review` 字面量在本仓库(除历史产物)**应**完全消失
- **NFR-5.3**:`code-rule` 可后续沉淀"技能重命名"规范(本需求**不**主动写 `assistants/rules/`)

### 5.6 安全性(NFR-6)
- **NFR-6.1**:`git mv` 失败(权限/文件占用)→ 透传 stderr,中断退出
- **NFR-6.2**:`Edit` 失败(文件被改 / 行号漂移)→ 透传 stderr,中断退出
- **NFR-6.3**:`jq` 校验失败(JSON 语法错误)→ 透传 stderr,中断退出

---

## 6. 页面与界面(本需求不涉及)

> 本需求**不**新增 / 不修改任何用户可见页面(本仓库是 meta-skills 工具集,无 UI)。
> 屏显输出见 §7 交互逻辑。

---

## 7. 交互逻辑

### 7.1 屏显格式契约(沿用 REQ-00013 NFR-4.1)

| 场景 | 格式 | 备注 |
| --- | --- | --- |
| 启动(本需求后) | `正在处理: REQ-NNNNN · <需求标题>(code-check)` | "code-check" 替代原 "code-review" |
| 完成(本需求后) | `完成: REQ-NNNNN · <需求标题>` | 沿用既有 |
| 错误:用户输入 `/code-review` | `✗ 未知技能: code-review(请使用 /code-check)` | 由 Claude Code 路由层处理 |

### 7.2 命名一致性(本需求后)

| 命名 | 旧 | 新 | 备注 |
| --- | --- | --- | --- |
| 技能入口(目录) | `code-review/` | `code-check/` | 硬重命名(FR-1) |
| 技能 frontmatter `name` | `code-review` | `code-check` | 硬重命名(FR-1) |
| H1 标题 | `# code-review — 代码评审(版本感知)` | `# code-check — 代码检查(版本感知)` | 硬重命名(FR-1) |
| 中文表述 | 代码评审 | 代码检查(可保留"代码评审"沿用) | 不强求 |
| 产出物类型目录 | `review/` | `review/`(**不**改) | 目录名是"产出物类型",沿用既有 |
| `code-auto` 子技能调用 | `code-review REQ-NNNNN` | `code-check REQ-NNNNN` | 同步改(FR-3) |

---

## 8. 数据与状态

### 8.1 重命名范围(本需求一次性改动)

| 类别 | 文件/目录 | 数量 | 处理 |
| --- | --- | --- | --- |
| 技能入口 | `code-review/SKILL.md` | 1 | `git mv` + 改 frontmatter + 改 H1 + 改全文 |
| 其他 SKILL.md(只改 description) | `code-{auto,design,require,plan,it,unit,fix,publish,dashboard,version,rule}/SKILL.md` | 10-11 | 改 description 字段字面量 |
| marketplace 清单 | `.claude-plugin/marketplace.json` | 1 | 改 skills[] + keywords[] + description |
| plugin 清单 | `plugins/code-skills/.claude-plugin/plugin.json` | 1 | 改 keywords[] + description |
| 仓库根 README | `README.md` / `README.en.md` | 2 | 改全文字面量 |
| 仓库内 README | `plugins/code-skills/README.md` / `README.en.md` | 2 | 改全文字面量 |
| CLAUDE.md | `CLAUDE.md` | 1 | 改全文字面量 |
| 项目级规范 | `assistants/rules/*.md` | 13 | 改引用字面量 |
| 技能模板 | `plugins/code-skills/skills/*/templates/*.md` | 6 | 改引用字面量 |
| 当前激活看板 | `assistants/V0.0.3/RESULT.md` | 1 | 改规范引用字面量 |
| **总计** | — | **约 38-39 个文件 + 1 个目录重命名** | — |

### 8.2 不追溯范围(本需求 0 改动)

| 类别 | 路径 | 备注 |
| --- | --- | --- |
| V0.0.0 历史 | `assistants/V0.0.0/**` | 沿用 `migration-mapping §规则 5` |
| V0.0.1 历史 | `assistants/V0.0.1/**` | 同上 |
| V0.0.2 历史 | `assistants/V0.0.2/**` | 同上 |
| V0.0.3 历史 review 产物 | `assistants/V0.0.3/review/REQ-NNNN/*` | 同上 |
| V0.0.3 其他历史产物 | `assistants/V0.0.3/{code,test,plan}/...` | 同上(与 `code-review` 相关的字面量保留) |

### 8.3 状态机(本需求 0 状态变更)

- 技能行为无变化,仅名字变化
- `code-check` 沿用 `code-review` 的全部状态机

---

## 9. 边界与异常

| ID | 场景 | 处理 |
| --- | --- | --- |
| **B-1** | `git mv` 失败(权限/文件占用) | 透传 stderr,中断退出 |
| **B-2** | `Edit` 替换失败(文件被改) | 透传 stderr,中断退出 |
| **B-3** | `jq .` 校验失败(JSON 语法) | 透传 stderr,中断退出 |
| **B-4** | `Grep "code-review"` 残留(本需求范围内) | 屏幕输出未替换列表,提示手动处理 |
| **B-5** | 用户输入 `/code-review` | Claude Code 报"未知技能"错误(由路由层处理) |
| **B-6** | `code-check` 技能的行为与 `code-review` 不一致 | 校验 `git diff` 应只有字面量差异,无语义差异 |
| **B-7** | 历史产物中"code-review"字面量 | **不**追溯替换(沿用 `migration-mapping §规则 5`) |
| **B-8** | `code-fix/templates/bug.md` 中"code-review"字面量 | 沿用历史,可在 `code-plan` 阶段决定是否改 |

---

## 10. 验收标准(AC 总览)

按 FR 编号归类,合计 ~30 条:

- **FR-1**(4 条):AC-1.1 ~ AC-1.4
- **FR-2**(4 条):AC-2.1 ~ AC-2.4
- **FR-3**(3 条):AC-3.1 ~ AC-3.3
- **FR-4**(8 条):AC-4.1 ~ AC-4.8
- **FR-5**(2 条):AC-5.1 ~ AC-5.2
- **FR-6**(3 条):AC-6.1 ~ AC-6.3
- **FR-7**(9 条):INV-1 ~ INV-9

**总计**:约 33 条 AC + 9 条 INV。

### 10.1 FR-1 验收(技能入口重命名)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-1.1** | `ls plugins/code-skills/skills/` | 不再含 `code-review/` 目录;含 `code-check/` 目录 |
| **AC-1.2** | `Read plugins/code-skills/skills/code-check/SKILL.md` frontmatter L1-3 | `name: code-check`(字节级) |
| **AC-1.3** | `Read plugins/code-skills/skills/code-check/SKILL.md` H1 | `# code-check — ...` |
| **AC-1.4** | `Grep "code-review" plugins/code-skills/skills/code-check/SKILL.md` | 无匹配 |

### 10.2 FR-2 验收(JSON 同步)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-2.1** | `Bash: jq . .claude-plugin/marketplace.json` | JSON 合法 |
| **AC-2.2** | `Grep "code-review" .claude-plugin/marketplace.json` | 无匹配(除注释外) |
| **AC-2.3** | `Bash: jq . plugins/code-skills/.claude-plugin/plugin.json` | JSON 合法 |
| **AC-2.4** | `Grep "code-review" plugins/code-skills/.claude-plugin/plugin.json` | 无匹配(除注释外) |

### 10.3 FR-3 验收(10 个其他 SKILL.md)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-3.1** | `Grep -l "code-review" plugins/code-skills/skills/*/SKILL.md` | 仅匹配 `code-check/SKILL.md` |
| **AC-3.2** | 10 个其他 SKILL.md 的 frontmatter `name` 字段 | 字节级保留(未改) |
| **AC-3.3** | 10 个其他 SKILL.md 的 `description` 字段 | 不含 `code-review` 字面量 |

### 10.4 FR-4 验收(README + 规范 + 模板 + 看板)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-4.1** | `Grep "code-review" README.md README.en.md` | 无匹配 |
| **AC-4.2** | `Grep "code-review" plugins/code-skills/README.md plugins/code-skills/README.en.md` | 无匹配 |
| **AC-4.3** | `Grep "code-review" CLAUDE.md` | 无匹配(本需求范围内) |
| **AC-4.4** | `Grep "code-review" assistants/rules/*.md` | 无匹配(本需求范围内) |
| **AC-4.5** | `Grep "code-review" plugins/code-skills/skills/*/templates/*.md` | 无匹配(本需求范围内) |
| **AC-4.6** | `Grep "code-review" assistants/V0.0.3/RESULT.md` | 无匹配(本需求范围内;规范引用) |
| **AC-4.7** | 中英 README 对仗校验(`doc-conventions §规则 1`) | 一致 |
| **AC-4.8** | `Grep "code-review" plugins/code-skills/skills/code-check/templates/*.md` | 无匹配 |

### 10.5 FR-5 验收(历史不追溯)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-5.1** | `Grep "code-review" assistants/V0.0.0/ assistants/V0.0.1/ assistants/V0.0.2/` | 命中(历史字面量保留) |
| **AC-5.2** | `Grep "code-review" assistants/V0.0.3/review/` | 命中(历史 review 产物保留) |

### 10.6 FR-6 验收(行为不变)

| AC | 验证手段 | 判定条件 |
| --- | --- | --- |
| **AC-6.1** | `git diff` 对照 `code-check/SKILL.md` 与 `code-review/SKILL.md`(原) | 仅字面量差异,无语义差异 |
| **AC-6.2** | 11 个 SKILL.md 的"## 工作流程"小节 | 字节级保留 |
| **AC-6.3** | 11 个 SKILL.md 的"## 衔接" / "## 不要做的事" 段 | 字节级保留 |

### 10.7 FR-7 验收(INV)

- **INV-1 ~ INV-9**:9 条不变量自检(沿用 FR-7 INV 列表)

---

## 11. 关联需求

| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| **REQ-00007**(V0.0.2) | `code-auto` 自动开发技能 | `code-auto/SKILL.md` 同步改 `code-review` → `code-check`(FR-3) | `./assistants/V0.0.2/require/REQ-00007/RESULT.md` |
| **REQ-00017**(V0.0.2) | `code-plan` 不再为"更新看板"拆派生任务 | 本需求 0 派生任务(INV-6) | `./assistants/V0.0.2/require/REQ-00017/RESULT.md` |
| **REQ-00019**(V0.0.2) | `code-plan` BUG 模式同构 | BUG 路径评审仍走 `review/` 目录(目录名是"产出物类型") | `./assistants/V0.0.2/require/REQ-00019/RESULT.md` |
| **REQ-00020**(V0.0.3) | 架构设计目标重新归位 + 3 新维度 | 本需求 0 涉及步骤 0b 设计目标;0 冲突 | `./assistants/V0.0.3/require/REQ-00020/RESULT.md` |
| **REQ-00021**(V0.0.3) | 优化 3 技能 --result / --plan 模板参数 | 本需求 0 涉及模板参数;0 冲突 | `./assistants/V0.0.3/require/REQ-00021/RESULT.md` |
| **REQ-00013**(V0.0.2) | 6 技能启用"编号+标题" 显示 | 屏显格式契约沿用(NFR-4.1) | `./assistants/V0.0.2/require/REQ-00013/RESULT.md` |

---

## 12. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本需求**0** 待澄清;4 项用户回答全部已锁定:Q-1 硬重命名 / Q-2 全部同步改 / Q-3 全部同步改 / Q-4 历史不追溯;7 FR / 6 NFR / ~33 AC / 9 INV 全部已锁定 | 0 待澄清 |

---

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-07 | v1 | 初始创建:7 FR / 6 NFR / ~33 AC / 9 INV 全部锁定;4 项 Q-locked(硬重命名 + JSON 全部同步 + docs 全部同步 + 历史不追溯);影响约 38-39 个文件 + 1 个目录重命名;**0** 触发 `dashboard-conventions §规则 1` 三同步;**0** 派生"更新看板"任务 REQ-00017 强约束;**0** 修改其他技能行为(仅字面量);**0** 触发 `encoding-conventions`;**0** 触发 `dependency-conventions`;`code-check` 行为与 `code-review` 完全一致 | wangmiao |
