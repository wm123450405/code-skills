# REQ-00026 需求分析 — 技能描述通用化

## 1. 需求概述

> 本项目是一套**通用的开发技能库**,但当前 10 个 SKILL.md 的描述性文字中混入了与本项目强关联的"专属内容"(典型为 `plugins/code-skills/...` 路径与"本项目 / 本仓库 / 本插件"指代)。本需求要求对**描述性段落**做一次"通用化"扫除:把"本项目专属"的指代替换为泛用表述(如 `<本仓库>`),同时**保留**所有项目级硬约束(不变量、验收命令、跨引用)。
>
> `./assistants/` 目录属本项目事实契约的一部分,**不**在本需求波及范围。
>
> (源自:用户 `code-require` args,2026-06-08)

## 2. 背景与目标

### 2.1 背景
本仓库 (`code-skills`) 是一套走完完整软件开发生命周期的 Claude Code 技能集合,以"Claude Code marketplace 协议"形式发布:

```
仓库根 (marketplace 仓库)
├── .claude-plugin/marketplace.json
└── plugins/<name>/                 ← 插件本体
    ├── .claude-plugin/plugin.json
    └── skills/<skill>/SKILL.md     ← 10 个技能入口
```

10 个技能的 SKILL.md 是用户/AI 实际**消费的契约文本**,应保持**泛用、可复用、可在他处借鉴**。

### 2.2 目标
1. **去专属化**:SKILL.md 的描述性文字中不再出现"本项目 / 本仓库 / 本插件"等强关联本仓库的指代。
2. **保留契约**:`./assistants/` 路径、不变量、验收命令、跨引用全部保留(它们是项目级硬约束)。
3. **不改元信息**:不修改 `marketplace.json` / `plugin.json` / 旧需求 RESULT.md / 仓库根 README / CLAUDE.md(本需求范围外)。

### 2.3 非目标
- **不**改插件元信息(`.claude-plugin/marketplace.json` / `plugin.json` 路径、关键词、description 等)
- **不**改仓库根 / 插件级 README(README.md / README.en.md)
- **不**改仓库根 CLAUDE.md
- **不**改 `./assistants/rules/`(项目级共享规范,`code-rule` 技能归属)
- **不**改旧需求的 `RESULT.md` / `auto-report.md` / `clarifications.md` / `analysis-notes.md` / `related-requirements.md`(历史档案,字面必须保留以保可追溯)
- **不**改本需求自身的产出文件(本文件 + 过程文档)

## 3. 用户角色与场景

### 3.1 用户角色
| 角色 | 关注点 |
| --- | --- |
| 技能使用者(他处借鉴者) | 在自家项目用 `<本仓库>/skills/.../SKILL.md` 模板时,不希望看到与本项目绑定的描述 |
| 项目维护者 | 维护 10 个 SKILL.md 时,不希望被"本项目专属表述"误导,只关心契约 |
| Claude Code 自身 | 执行 `code-*` 技能时,需要明确知道"哪些路径是约定"vs"哪些是字面命令" |

### 3.2 场景
1. **他处借鉴**:有团队 fork 本仓库,想去掉本项目名字/路径,但希望保留 SKILL.md 的所有工作流步骤。
2. **跨项目迁移**:有团队把 `code-require` 复制到自家项目,期望 SKILL.md 中的路径示例不绑死 `plugins/code-skills/`。
3. **本项目维护**:维护者 grep `plugins/code-skills` 时,只想看"不变量"和"验收命令",不希望被"本项目"措辞淹没。

## 4. 功能需求 (FR)

### FR-1:SKILL.md 描述性段落中 `plugins/code-skills/...` 路径替换为 `<本仓库>`
- **描述**:10 个 SKILL.md 描述性段落(功能描述、上下游衔接、适用场景、工作流步骤、注意事项)中,所有指代"该仓库内的某个文件"的 `plugins/code-skills/...` 路径,替换为 `<本仓库>/...` 形式。
- **范围**:
  - 命中文件:`code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-check` / `code-fix` / `code-publish` / `code-rule` / `code-init`(共 10 个 SKILL.md)
  - 替换规则:
    - `plugins/code-skills/skills/<skill>/SKILL.md` → `<本仓库>/skills/<skill>/SKILL.md`
    - `plugins/code-skills/.claude-plugin/plugin.json` → `<本仓库>/.claude-plugin/plugin.json`
    - `plugins/code-skills/CLAUDE.md` → `<本仓库>/CLAUDE.md`
- **保留**:
  - 不变量字面(如"不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件")—— 改为"不修改 `<本仓库>/skills/*/SKILL.md` 任何文件"也是接受的(更通用),但**保留**原字面也接受
  - 验收步骤中 `git diff plugins/code-skills/skills/...` 等可执行命令的字面路径(命令的字面必须保留)
  - 跨引用 SKILL.md 时的字面路径(用以确定跨引用关系)
- **判定原则**:**只改"描述性段落"**(H1 标题、概述段、适用场景、工作流步骤中的引用示例);不改"硬约束 / 命令示例"段落(不变量、AC、INV)
- (源自:用户 `code-require` args)

### FR-2:SKILL.md 描述性段落中"本项目 / 本仓库 / 本插件"等强关联指代替换为泛用表述
- **描述**:SKILL.md 描述性段落中,以下指代改为泛用表述:
  | 原表述 | 替换为 |
  | --- | --- |
  | "本项目是一套..." | "本仓库是一套..." 或 "本技能库是一套..." |
  | "本仓库主动产出" | "本仓库主动产出" / "默认本仓库产出"(该表述已较通用,可不改) |
  | "本仓库纯文档,无可测载体" | "本仓库纯文档,无可测载体" / "若本仓库无代码载体,本字段不适用"(保持灵活性) |
  | "本技能市场清单中" | "本技能市场清单中"(已较通用) |
  | "本项目 / 本插件" | "本仓库 / 本插件目录" 或 "本套技能" |
- **范围**:10 个 SKILL.md 的描述性段落
- **保留**:硬约束(不变量、INV、AC)中以"本项目"为指代的不变量原文(字面保留以保可追溯)
- (源自:用户 `code-require` args)

### FR-3:`./assistants/` 路径在 SKILL.md 中**不**做修改
- **描述**:`./assistants/` 是本项目级别的事实契约(由 `code-version` 初始化,跨版本共享,所有 `code-*` 技能都强依赖),应保持原样。
- **范围**:10 个 SKILL.md 中的 `./assistants/...` 路径引用
- **理由**:
  1. 它是项目约定而非"项目专属内容",与 `plugins/code-skills/` 不同
  2. 用户的原话"`./assistants` 目录是本项目用来管理开发进度的重要目录,技能中是可以经常使用的"已明确表态
  3. 它是 SKILL.md 的**事实契约**,改了反而令技能不可用
- (源自:用户 `code-require` args 澄清记录 Q4)

### FR-4:附属文本(模板/规范/清单)同步去专属化
- **描述**:`code-publish/templates/DEPLOY.md` / `UPDATE.md` / `qanda-README.md` 头部的"由 `code-publish` 技能从 `plugins/code-skills/skills/code-publish/templates/...` 复制生成"等描述性字面,替换为"由 `code-publish` 技能从 `<本仓库>/skills/code-publish/templates/...` 复制生成"。
- **范围**:
  - `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` L3
  - `plugins/code-skills/skills/code-publish/templates/UPDATE.md` L3
  - `plugins/code-skills/skills/code-publish/templates/qanda-README.md` L133
  - `plugins/code-skills/skills/code-init/templates/INIT-REPORT.md` L3 / L8(将"本项目"指代改为"本仓库")
- (源自:扫描结果 `Grep` 命中)

### FR-5:`code-rule` SKILL.md 中"追加到 `plugins/code-skills/CLAUDE.md`"改为"追加到 `<本仓库>/CLAUDE.md`"
- **描述**:`code-rule` SKILL.md L336 / L363 / L370 三处描述性字面,从 `plugins/code-skills/CLAUDE.md` 改为 `<本仓库>/CLAUDE.md`。
- **范围**:
  - `plugins/code-skills/skills/code-rule/SKILL.md` L336
  - `plugins/code-skills/skills/code-rule/SKILL.md` L363
  - `plugins/code-skills/skills/code-rule/SKILL.md` L370
- (源自:扫描结果 `Grep` 命中)

## 5. 非功能需求 / 约束 (NFR)

### NFR-1:范围严格性
- **不**修改 `marketplace.json` / `plugin.json` / 仓库根 README / `CLAUDE.md` / `./assistants/rules/` / 旧需求档案
- **不**修改本需求自身的产出文件

### NFR-2:可追溯性
- 本次扫除涉及 13 个文件(10 个 SKILL.md + 3 个附属模板)的若干处替换,每处替换应在 git diff 中可逐条定位

### NFR-3:一致性
- 同一文件内的相同表述,要么全改要么全不改(避免半改半留)
- "描述性"与"约束性"段落必须严格区分,不可混淆

### NFR-4:可发布性
- 改动后,`marketplace.json` / `plugin.json` / `./assistants/rules/` 0 diff
- 改动后,旧需求档案 0 diff
- 改动后,10 个 SKILL.md 仍是有效的 SKILL 文件(frontmatter 不变)

## 6. 页面与界面

N/A(本需求不涉及 UI)

## 7. 交互逻辑

N/A(本需求不涉及交互)

## 8. 数据与状态

N/A(本需求不涉及数据建模)

## 9. 边界与异常

### 9.1 边界

| 类别 | 在本需求范围 | 不在本需求范围 |
| --- | --- | --- |
| 10 个 SKILL.md 描述性段落 | ✓ | |
| 10 个 SKILL.md 硬约束段落(不变量、AC、INV) | | ✓(字面保留) |
| 10 个 SKILL.md 验收命令示例 | | ✓(字面保留) |
| `code-publish/templates/*.md` | ✓(部分) | |
| `code-init/templates/INIT-REPORT.md` | ✓(部分) | |
| `code-rule/SKILL.md` 描述性段落 | ✓ | |
| `marketplace.json` / `plugin.json` | | ✓ |
| 仓库根 README / `CLAUDE.md` | | ✓ |
| `./assistants/rules/` | | ✓ |
| 旧需求 `RESULT.md` 等档案 | | ✓ |
| 本需求自身的产出文件 | | ✓(自指) |

### 9.2 异常 / 风险
- **风险 1**:若 `code-it` / `code-unit` SKILL.md 中"不修改 `plugins/code-skills/skills/*/SKILL.md` 任何文件"这种不变量被改为"不修改 `<本仓库>/skills/*/SKILL.md` 任何文件",可能影响后续 `code-check` 评审时的字面断言。
  - **缓解**:评审时通过 `git log` / `git blame` 判断当时实际仓库名,断言需兼容"两种字面"。
- **风险 2**:`grep "plugins/code-skills"` 是后续 `code-check` 评审的常用命令,改动后命令本身不变(只改 SKILL.md 内容),不会影响评审。

## 10. 验收标准 (AC)

### AC-1:`plugins/code-skills` 在 10 个 SKILL.md 的描述性段落中不再出现
- **AC-1.1**:`Grep "plugins/code-skills" plugins/code-skills/skills/*/SKILL.md` 命中行**只**属于"不变量" / "验收命令" / "INV" 类硬约束段落
- **AC-1.2**:10 个 SKILL.md 的 H1 标题、概述段、适用场景、工作流步骤中的引用示例中,`plugins/code-skills` 0 命中

### AC-2:13 个文件的描述性段落完成替换
- **AC-2.1**:`git diff --stat plugins/code-skills/skills/` 列出 10 个 SKILL.md + 3 个 templates 文件
- **AC-2.2**:`git diff plugins/code-skills/skills/code-rule/SKILL.md` 显示 L336 / L363 / L370 替换为 `<本仓库>`

### AC-3:本需求范围内 + 范围外泾渭分明
- **AC-3.1**:`git diff .claude-plugin/marketplace.json` 0 diff
- **AC-3.2**:`git diff plugins/code-skills/.claude-plugin/plugin.json` 0 diff
- **AC-3.3**:`git diff README.md README.en.md` 0 diff
- **AC-3.4**:`git diff plugins/code-skills/README.md plugins/code-skills/README.en.md` 0 diff
- **AC-3.5**:`git diff plugins/code-skills/CLAUDE.md` 0 diff
- **AC-3.6**:`git diff assistants/rules/` 0 diff
- **AC-3.7**:`git diff assistants/V0.0.3/require/` 仅含本需求 `REQ-00026/` 新增文件,无其他需求档案改动

### AC-4:契约保持
- **AC-4.1**:10 个 SKILL.md 的 frontmatter(`name` / `description`)**不**变
- **AC-4.2**:`./assistants/` 路径在 10 个 SKILL.md 中**不**被替换
- **AC-4.3**:`code-publish/templates/*.md` 的 `qanda-README.md` L133 等"草稿区"指引不变(语义保持)

### AC-5:过程文件完整
- **AC-5.1**:`assistants/V0.0.3/require/REQ-00026/RESULT.md` 存在且覆盖 §1-§13
- **AC-5.2**:`materials-index.md` / `clarifications.md` / `related-requirements.md` / `analysis-notes.md` 完整

## 11. 关联需求

- **无强关联需求**(扫描 `assistants/V0.0.3/require/*/RESULT.md` 未发现"技能通用化"主题)
- 旧需求 REQ-00022 / REQ-00024 / REQ-00025 的 RESULT.md 中含 `plugins/code-skills/...` 路径,均为"不变量 / 验收命令"类硬约束字面,属正确用法,**不**被本需求波及(详见 `related-requirements.md`)

## 12. 待澄清 / 未决项

| 编号 | 待澄清项 | 状态 |
| --- | --- | --- |
| Q5 | 10 个 SKILL.md 的"硬约束段落"是否也应统一替换为 `<本仓库>`?(用户当前选"保留字面") | 已决策:保留字面 |
| Q6 | 若后续 `code-check` 评审发现某 SKILL.md 描述与本需求"通用化"原则冲突,如何裁决? | 留待 `code-check` 阶段处理 |

## 13. 变更记录

- `2026-06-08 11:48` 需求初始,材料登记完成(共 1 条 args 输入)
- `2026-06-08 11:50` 澄清 4 项:波及范围 / 描述性 vs 约束性 / 路径替代 / `./assistants` 定位(详见 `clarifications.md`)
- `2026-06-08 11:55` 需求分析完成:5 FR / 4 NFR / 3 类 AC(共 12 条 AC)
