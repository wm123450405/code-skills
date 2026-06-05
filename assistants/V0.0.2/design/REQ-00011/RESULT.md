# REQ-00011 概要设计 — code-design / code-plan 步骤 0b:设计目标确认

> 写入方:`code-design` 技能
> 上游:./assistants/V0.0.2/require/REQ-00011/RESULT.md
> 遵循规范:`./assistants/rules/` 下 13 个文件(详 `rule-compliance.md`)
> 创建时间:2026-06-05
> 状态:**已完成(概要设计)**

---

## 1. 设计目标与范围

### 1.1 目标

为 `code-design` 与 `code-plan` 两个技能增加 **"步骤 0b 设计目标确认"环节** — 在首步拉取(步骤 0a,沿用 REQ-00005)之后、设计产出之前,触发 `AskUserQuestion` 让用户对"功能性 / 扩展性 / 健壮性 / 可维护性"等维度做选择,把"设计目标"小节回写到 `design/.../RESULT.md` 与 `plan/.../RESULT.md` 顶部,并让 `code-plan` 据此调整任务拆分粒度。

具体 5 项设计目标:

- **D-1** `code-design` 在步骤 0a 之后新增"步骤 0b 设计目标确认",通过 `AskUserQuestion` 问 1-5 个问题(整体设计目标 + 4 维度)
- **D-2** `code-plan` 在步骤 0a 之后新增"步骤 0b 设计目标确认":先读 `design/.../RESULT.md` 的"## 设计目标"小节,存在则**沿用**,不存在则**退化**(问 1 个简化问题)
- **D-3** 用户回答后,屏幕打印"已回写至 design/<REQ>/RESULT.md '## 设计目标' 小节",并**实际写入**该小节
- **D-4** `code-plan` 读"## 设计目标"小节后,**调整**任务拆分粒度:扩展性高 → 加"扩展架构设计" / "设计模式使用"等任务;`--minimal` → 同类任务合并
- **D-5** 不修改其他 8 个 `code-*` 技能;不修改 `marketplace.json` / `plugin.json` / 看板(零规范变更)

### 1.2 范围

| 范围 | 包含 |
| --- | --- |
| 改动 | `/code-design` SKILL.md(在"步骤 0a"后增量追加"步骤 0b");`/code-plan` SKILL.md(在"步骤 0a"后增量追加"步骤 0b");2 个技能正文(NFR-2 强约束) |
| **不**改 | `/code-version` / `/code-require` / `/code-it` / `/code-unit` / `/code-review` / `/code-dashboard` / `/code-publish` / `/code-auto` 8 个 `code-*` 技能(FR-7.AC-7.1) |
| **不**改 | 任何 SKILL.md 的 frontmatter(`skill-conventions.md §规则 1` 强约束) |
| **不**改 | `./assistants/rules/` 13 个规范文件;`plugins/code-skills/CLAUDE.md`;`plugins/code-skills/skills/code-version/templates/version-RESULT.md`(NFR-4 强约束) |
| **不**改 | `marketplace.json` / `plugin.json`(FR-8.AC-8.1) |
| 模板 | `code-design/templates/design.md` 顶部 + `code-plan/templates/plan.md` 顶部预留"## 设计目标"占位小节 |
| 新增依赖 | 0 |
| 新增技能 | 0 |

### 1.3 不变量(强约束)

- **INV-1** `code-design/SKILL.md` 与 `code-plan/SKILL.md` 的 frontmatter(`name` + `description`)**字节级不变**(`skill-conventions.md §规则 1` + NFR-2)
- **INV-2** 2 个技能的"步骤 0" / "步骤 1" / ... / "末尾兜底"既有流程**完全不变**(增量追加"步骤 0b",不重写稳定章节)
- **INV-3** "## 设计目标"小节位置 = `design/.../RESULT.md` 顶部(在"文档头"之后,"## 1. 设计概述"之前);`plan/.../RESULT.md` 同位置
- **INV-4** `code-plan` 沿用 `design` "## 设计目标"小节时,**不**重新问用户(已问过);`code-plan` 找不到 `design` "## 设计目标"小节时,才退化问 1 个问题
- **INV-5** 多次执行 `code-design` / `code-plan` → "## 设计目标"小节**覆盖**前次内容(NFR-3 幂等)
- **INV-6** 整体设计目标 = `--extensible` 或 扩展性优先级 = `高` → `code-plan` 拆出的"任务总览"中**至少含 1 个**"扩展架构设计" / "设计模式使用"等扩展性任务
- **INV-7** `code-auto` 调 `code-design` / `code-plan` 步骤 0b 时,**总选推荐项**(沿用 `code-auto` 现行 Q-4 锁定 A,NFR-5 强约束);不感知"设计目标"概念的其他 8 个技能**0 改动**
- **INV-8** 不触发 `dashboard-conventions §规则 1` 3 处同步(`design/.../RESULT.md` 与 `plan/.../RESULT.md` 不是看板,只是技能产物;NFR-4)

### 1.4 本次设计目标(由 code-auto 自动选推荐项)

> code-auto 模式下,`code-design` / `code-plan` 步骤 0b 触发 `AskUserQuestion` 时按"总选推荐项"作答。
> 推荐项 = `--balanced` / 功能性=中 / 扩展性=中 / 健壮性=中 / 可维护性=中。
> 因此本次 `code-plan` 后续任务拆分**按默认粒度产出**(无调整)。

---

## 2. 现状与改造点

### 2.1 当前 `code-design` SKILL.md(改造前)

```
[启动]
  ↓
[步骤 0a:git pull] ─────────┐ (REQ-00005 落地,2026-06-03)
  ↓ (成功)
[步骤 0:版本上下文检测]    ← 本需求前没有"步骤 0b"
  ↓
[步骤 1-?:原有设计流程]
  ↓
[末尾兜底提交]
  ↓
[退出]
```

**改造前**:`code-design` 在首步拉取 + 版本上下文检测后直接进入"步骤 1 收集需求编码"等设计流程;**无**"设计目标确认"环节,AI 默认按"最常见方式"产出(可能导致"设计过度"或"设计不足",见上游 REQ-00011 §2.1)。

### 2.2 当前 `code-plan` SKILL.md(改造前)

```
[启动]
  ↓
[步骤 0a:git pull] ─────────┐ (REQ-00005 落地)
  ↓ (成功)
[步骤 0:版本上下文检测]
  ↓
[步骤 1-?:原有计划流程(读 design/、拆任务、写 PLAN.md)]
  ↓
[末尾兜底提交]
  ↓
[退出]
```

**改造前**:`code-plan` 在拆任务时,任务粒度按"默认值"产出(无用户干预);**不感知** `design/.../RESULT.md` 的设计目标。

### 2.3 改造点

| 文件 | 改造前 | 改造后 |
| --- | --- | --- |
| `/code-design` SKILL.md | 步骤 0a → 步骤 0 | 步骤 0a → **步骤 0b 设计目标确认** → 步骤 0 → ... |
| `/code-design` 步骤 0b | (无) | 触发 `AskUserQuestion`(1-5 个问题)→ 用户回答 → 写 `design/.../RESULT.md` 顶部"## 设计目标"小节 → 屏幕打印"已回写" |
| `/code-plan` SKILL.md | 步骤 0a → 步骤 0 | 步骤 0a → **步骤 0b 设计目标确认** → 步骤 0 → ... |
| `/code-plan` 步骤 0b | (无) | 读 `design/.../RESULT.md` 的"## 设计目标"小节 → 存在 = 沿用,屏幕打印"沿用 design 的设计目标";不存在 = 退化,`AskUserQuestion` 1 问 → 写 `plan/.../RESULT.md` 顶部"## 设计目标"小节 |
| `/code-plan` 拆任务粒度 | 默认粒度(无调整) | **根据"## 设计目标"小节调整**(扩展性高 → 加扩展性任务;`--minimal` → 合并同类任务;`--balanced` → 默认粒度) |
| `/code-design` 模板 `templates/design.md` | 顶部"## 文档头" → "## 1. 设计概述" | 顶部"## 文档头" → **"## 设计目标"** → "## 1. 设计概述" |
| `/code-plan` 模板 `templates/plan.md` | 顶部"## 文档头" → "## 1. 任务总览"(等) | 顶部"## 文档头" → **"## 设计目标"** → "## 1. ..." |

### 2.4 与"步骤 0a"的位序关系

| 步骤 | 来源 | 触发内容 | 失败行为 |
| --- | --- | --- | --- |
| 步骤 0a | REQ-00005 落地 | `Bash: git pull` | 失败 → 报错退出(沿用 REQ-00005 错误码) |
| **步骤 0b** | **本需求新增** | `AskUserQuestion` × 1-5 / 读 `design/.../RESULT.md` | `code-design`:用户取消 → 中止(回写空"## 设计目标"小节);`code-plan`:读不到 → 退化(1 问) |
| 步骤 0 | REQ-00005 落地 | 读 `.current-version` | 文件不存在 → 提示调 `code-version` |

---

## 3. 关键设计决策(8 项)

### D-1 步骤命名沿用"步骤 0a"模式,新增"步骤 0b"

- **位置**:`code-design` 步骤 0a(REQ-00005 拉取)**之后**,步骤 0(版本上下文检测)**之前**;`code-plan` 同位置
- **理由**:与既有"步骤 0a 守卫"模式(REQ-00005 / REQ-00009 / REQ-00010)同位叠加;**不**改既有边界(NFR-6 强约束)
- **NFR-2 落实**:增量追加,不重写稳定章节

### D-2 "## 设计目标"小节作为唯一回写位置

- **位置**:`design/.../RESULT.md` 顶部(在"文档头"之后,"## 1. 设计概述"之前);`plan/.../RESULT.md` 同位置
- **小节结构**(由 code-design / code-plan 自动生成):
  - 回写时间:`YYYY-MM-DD HH:mm`
  - 回写触发:`code-design` / `code-plan`
  - 整体设计目标:`--minimal` / `--extensible` / `--balanced`
  - 维度优先级:功能性 / 扩展性 / 健壮性 / 可维护性 各 `高/中/低`
- **下游消费方**:`code-plan` 读该小节(FR-2)
- **不**触发 `dashboard-conventions §规则 1` — `design/.../RESULT.md` / `plan/.../RESULT.md` 是技能产物,**不**是看板(NFR-4)

### D-3 `code-design` 触发 1-5 个 `AskUserQuestion`,自适应需求规模

- **典型问题清单**(Q-7 锁定):
  - Q1:整体设计目标?(`--minimal` / `--extensible` / `--balanced`)
  - Q2:功能性优先级?(高/中/低)
  - Q3:扩展性优先级?(高/中/低)
  - Q4:健壮性优先级?(高/中/低)
  - Q5:可维护性优先级?(高/中/低)
- **自适应策略**(S-4):
  - 小需求:1 个问题(只问整体设计目标)
  - 中等需求:3-5 个问题(整体 + 1-4 维度)
  - 大需求:可对不同细节功能**分开提问**(每问 1 个明确维度,**不**1 问 6 选项)
- **AC-6.5**:**不**与现有"子流程"询问混淆 — 本步骤**只**问设计目标,其他澄清询问(架构走向、部署形态等)在步骤 7A-10A 子流程中

### D-4 `code-plan` 读 `design` "## 设计目标"小节,沿用 or 退化

- **存在**(`design/.../RESULT.md` 含"## 设计目标"小节):
  - 屏幕打印"沿用 design 的设计目标:<摘要>"
  - **不**重新问用户
  - 把读到的内容**复制**到 `plan/.../RESULT.md` 顶部"## 设计目标"小节(回写触发=code-plan,继承回写时间)
- **不存在**(Q-2 锁定):
  - 屏幕打印"⚠ 未检测到 design/<REQ>/RESULT.md,请回答设计目标"
  - `AskUserQuestion` 1 问(整体设计目标 + 4 维度各 1 问,共 5 问,**简化版**可只问整体)
  - 写 `plan/.../RESULT.md` 顶部"## 设计目标"小节
  - **不**写 `design/.../RESULT.md`(因 `code-design` 未跑过,职责分离;FR-3.AC-3.3)
- **E-5 边界**:`code-plan` 读 `design/.../RESULT.md` 存在但**无**"## 设计目标"小节 → 视为"无 design 输入",退化

### D-5 `code-plan` 据"## 设计目标"小节调整任务拆分粒度(FR-4)

- **判定规则**:
  - 整体 = `--extensible` 或 扩展性 = `高` → 加"扩展架构设计" / "设计模式使用"等扩展性任务(整体 `--extensible` + 扩展性=`高` → 至少 3 个)
  - 整体 = `--minimal` → 同类任务合并,粒度粗化
  - 整体 = `--balanced` + 扩展性 ∈ {中, 低} → 默认粒度,无调整
- **任务粒度调整表**(REQ-00011 §8.3):

| 整体设计目标 | 扩展性优先级 | 任务粒度调整 |
| --- | --- | --- |
| `--minimal` | * | 合并同类任务,粒度粗化 |
| `--balanced` | 高/中/低 | 默认粒度 |
| `--extensible` | * | 加"扩展架构设计" / "设计模式使用"等任务(至少 1 个) |
| `--extensible` | 高 | 至少 3 个扩展性相关任务 |

- **AC-4.4**:其他维度优先级(功能性 / 健壮性 / 可维护性)作为参考,**不**强制加任务

### D-6 "## 设计目标"小节幂等性(NFR-3)

- **多次执行**:`code-design` 多次执行 → 顶部"## 设计目标"小节**覆盖**前次内容
- **同时性**:`code-plan` 既读 `design/.../RESULT.md` 的小节,又写 `plan/.../RESULT.md` 的小节(独立位置,无冲突)
- **回写时间字段**:每次执行都更新为最新时间

### D-7 与 `code-auto` 的协同(NFR-5 强约束)

- `code-auto` 现行 FR-3 / Q-4 锁定 A "总选推荐项"**不**变
- `code-auto` 调 `code-design` / `code-plan` 步骤 0b → `AskUserQuestion` 触发 → `code-auto` 选"推荐项" → 无人确认实际发生
- **本需求主要面向"用户手动调"场景**;`code-auto` 场景下"总选推荐项"已是 V0.0.2 既定行为
- **不**触发 `code-auto` 升级;**建议派生**"`code-auto` 升级:识别'设计目标确认'类询问时回传"任务(由用户决定,本需求不阻塞)

### D-8 模板顶部预留"## 设计目标"占位小节

- **目的**:让 `code-design` / `code-plan` 产出 RESULT.md 时,有"固定位置"写"## 设计目标"小节
- **方式**:`code-design/templates/design.md` 顶部"## 文档头"模板区段后 + "## 1. 设计概述"前,加占位注释(说明"本节由 `code-design` 步骤 0b 自动生成")
- **同样**:`code-plan/templates/plan.md` 顶部"## 文档头"模板区段后 + "## 1. ..."前,加占位注释
- **不改**模板其他内容;**不改** `code-version/templates/version-RESULT.md`(`code-design` 步骤 0b **不**写看板)

---

## 4. 模块拆分

### 4.1 复用既有模块(只改 SKILL.md 正文,不改 frontmatter)

| 模块 | 路径 | 状态 | 职责 | 本次涉及 |
| --- | --- | --- | --- | --- |
| `/code-design` | `plugins/code-skills/skills/code-design/SKILL.md` | 修改(正文) | 概要设计 | 步骤 0a 后**增量追加**"步骤 0b 设计目标确认"小节 |
| `/code-design/templates/design.md` | 修改(顶部预留位) | 概要设计模板 | 顶部"## 文档头"与"## 1. 设计概述"之间预留"## 设计目标"占位 |
| `/code-plan` | `plugins/code-skills/skills/code-plan/SKILL.md` | 修改(正文) | 详细设计 + 任务计划 | 步骤 0a 后**增量追加**"步骤 0b 设计目标确认"小节;**任务拆分准则**处加"按设计目标调整粒度"段 |
| `/code-plan/templates/plan.md` | 修改(顶部预留位) | 详细设计模板 | 顶部"## 文档头"与"## 1. ..."之间预留"## 设计目标"占位 |
| `/code-require` | `plugins/code-skills/skills/code-require/SKILL.md` | **不**修改 | 需求分析 | (本需求不触发升级) |
| `/code-it` | `plugins/code-skills/skills/code-it/SKILL.md` | **不**修改 | 代码改写 | (本需求不触发升级) |
| `/code-unit` | `plugins/code-skills/skills/code-unit/SKILL.md` | **不**修改 | 单元测试 | (本需求不触发升级) |
| `/code-review` | `plugins/code-skills/skills/code-review/SKILL.md` | **不**修改 | 代码评审 | (本需求不触发升级) |
| `/code-dashboard` | `plugins/code-skills/skills/code-dashboard/SKILL.md` | **不**修改 | 看板展示 | (本需求不触发升级) |
| `/code-publish` | `plugins/code-skills/skills/code-publish/SKILL.md` | **不**修改 | 发布部署 | (本需求不触发升级) |
| `/code-version` | `plugins/code-skills/skills/code-version/SKILL.md` | **不**修改 | 版本管理 | (本需求不触发升级) |
| `/code-auto` | `plugins/code-skills/skills/code-auto/SKILL.md` | **不**修改 | 自动开发编排 | (本需求不触发升级;沿用现行"总选推荐项"行为) |

### 4.2 新增模块

无。

### 4.3 修改既有模块(0 个"业务"模块,仅文档/SKILL.md 调整)

仅 4 个文件改动:
- `plugins/code-skills/skills/code-design/SKILL.md`(正文增量追加"步骤 0b")
- `plugins/code-skills/skills/code-design/templates/design.md`(顶部预留位)
- `plugins/code-skills/skills/code-plan/SKILL.md`(正文增量追加"步骤 0b" + 任务拆分准则调整)
- `plugins/code-skills/skills/code-plan/templates/plan.md`(顶部预留位)

### 4.4 自检:对照 `module-conventions.md` / `directory-conventions.md` / `skill-conventions.md`

| 规范条款 | 本次涉及 | 满足情况 |
| --- | --- | --- |
| `skill-conventions.md §规则 1`:SKILL.md 必含 name + description,且与目录名一致 | 2 个技能 SKILL.md frontmatter 不动 | ✅ INV-1 强约束 |
| `module-conventions.md §规则 1`:资源放技能子目录(`templates/` / `checklists/` / `guidelines/`) | 2 个 `templates/*.md` 顶部预留位 | ✅ 已在子目录内,不改位置 |
| `directory-conventions.md §规则 1`:(待添加) | 不涉及 | N/A |

---

## 5. 接口与数据结构

### 5.1 接口(本设计无对外 API;`code-design` / `code-plan` 内部流程调整)

无对外 API 变更。

### 5.2 数据结构:"## 设计目标"小节

**位置**:
- `design/.../RESULT.md` 顶部(在"文档头"之后,"## 1. 设计概述"之前)
- `plan/.../RESULT.md` 顶部(在"文档头"之后,"## 1. ..."之前)

**小节 Markdown 结构**(步骤 0b 实际写入的内容):

```markdown
## 设计目标

> 本小节由 `code-design` / `code-plan` 步骤 0b 自动生成,记录用户确认的设计目标。

- **回写时间**:2026-06-05 17:00
- **回写触发**:code-design

### 整体设计目标
`--balanced`

### 维度优先级

| 维度 | 优先级 |
| --- | --- |
| 功能性 | 中 |
| 扩展性 | 中 |
| 健壮性 | 中 |
| 可维护性 | 中 |
```

**字段类型**(参考 REQ-00011 §8.1):

```ts
{
  writeTime: string,         // "YYYY-MM-DD HH:mm"
  writeTrigger: "code-design" | "code-plan"
  overallGoal: "--minimal" | "--extensible" | "--balanced"
  dimensionPriority: {
    functionality: "高" | "中" | "低"
    extensibility: "高" | "中" | "低"
    robustness: "高" | "中" | "低"
    maintainability: "高" | "中" | "低"
  }
}
```

### 5.3 SKILL.md 正文增量追加(锚点)

`code-design/SKILL.md` 在"步骤 0a:git pull"**小节末尾**追加:

```markdown
### 步骤 0b:设计目标确认(本需求新增)

1. 触发 `AskUserQuestion`,1-5 个问题:
   - Q1:整体设计目标?(`--minimal` / `--extensible` / `--balanced`)
   - Q2:功能性优先级?(高/中/低)
   - Q3:扩展性优先级?(高/中/低)
   - Q4:健壮性优先级?(高/中/低)
   - Q5:可维护性优先级?(高/中/低)
2. 大需求可对不同细节功能**分开提问**(S-4)
3. 用户回答后,写 `design/.../RESULT.md` 顶部"## 设计目标"小节
4. 屏幕打印"已回写至 design/<REQ>/RESULT.md '## 设计目标' 小节"
5. 用户取消 → 中止,回写空"## 设计目标"小节(E-3)
```

`code-plan/SKILL.md` 在"步骤 0a:git pull"**小节末尾**追加:

```markdown
### 步骤 0b:设计目标确认(本需求新增)

1. 读 `design/.../RESULT.md` 的"## 设计目标"小节:
   - 存在 → 屏幕打印"沿用 design 的设计目标:<摘要>" → 复制到 `plan/.../RESULT.md` 顶部"## 设计目标"小节
   - 不存在 → 屏幕打印"⚠ 未检测到 design/<REQ>/RESULT.md" → 触发 `AskUserQuestion` 1-5 问(简化版可只问整体) → 写 `plan/.../RESULT.md` 顶部"## 设计目标"小节(**不**写 `design/.../RESULT.md`)
2. 据"## 设计目标"小节**调整**任务拆分粒度(见 D-5 / FR-4)
```

### 5.4 任务粒度调整判定表(D-5 落地)

`code-plan/SKILL.md` 步骤 X"任务拆分准则"处**追加 1 段**:

```markdown
#### 按"## 设计目标"小节调整任务粒度(FR-4)

读取本需求步骤 0b 写入的"## 设计目标"小节,据此调整任务总览:

| 整体设计目标 | 扩展性优先级 | 任务粒度调整 |
| --- | --- | --- |
| `--minimal` | * | 合并同类任务,粒度粗化 |
| `--balanced` | 高/中/低 | 默认粒度(无调整) |
| `--extensible` | * | 加"扩展架构设计" / "设计模式使用"等任务(至少 1 个) |
| `--extensible` | 高 | 至少 3 个扩展性相关任务 |
```

---

## 6. 三方依赖

无新增。无复用既有依赖(NFR-1 强约束)。本需求不引入任何 npm/pip/cargo 等依赖,仅使用既有工具:
- `Bash` / `Read` / `Edit` / `Write` / `AskUserQuestion` / `Glob` / `Grep`

---

## 7. 集成点

| 集成点 | 类型 | 描述 |
| --- | --- | --- |
| `code-design` → `code-plan` | **数据传递** | `code-plan` 步骤 0b 读 `design/.../RESULT.md` 的"## 设计目标"小节;沿用作为 `code-plan` 自身的"## 设计目标"小节 |
| `code-design` → `code-auto` | **行为兼容** | `code-auto` 调 `code-design` 步骤 0b 时,`AskUserQuestion` 触发 → `code-auto` 选"推荐项" → 无人确认实际发生(NFR-5) |
| `code-plan` → `code-auto` | **行为兼容** | `code-auto` 调 `code-plan` 步骤 0b 时,若 `design/.../RESULT.md` 存在,`code-plan` 沿用,`code-auto` 不感知;若不存在,`code-plan` 退化,`AskUserQuestion` 触发 → `code-auto` 选"推荐项" |
| `code-design` / `code-plan` → 看板 | **无影响** | 本需求**不**写看板;`code-design` / `code-plan` 末尾兜底照常同步"概要设计清单" / "任务清单" / "变更记录"(NFR-4) |
| `code-design` / `code-plan` → 模板 | **顶部预留** | `code-design/templates/design.md` + `code-plan/templates/plan.md` 顶部预留"## 设计目标"占位(模板固定位置,D-8) |
| `code-design` / `code-plan` → `code-review` | **无影响** | `code-review` 不感知"设计目标"概念;`code-review` 评审清单**不**变(FR-7.AC-7.3) |
| `code-design` / `code-plan` → `code-dashboard` | **无影响** | `code-dashboard` 不感知"设计目标"概念;看板 3 区段解析锚点**不**变(NFR-4) |

---

## 8. 风险与缓解

| 风险 | 可能性 | 影响 | 缓解措施 | 回退方案 |
| --- | --- | --- | --- | --- |
| R-1 `code-auto` 调 `code-design` / `code-plan` 步骤 0b 触发 `AskUserQuestion` 但 `code-auto` 拦截不到(场景回退) | 中 | 中 | `code-auto` 现行 Q-4 锁定 A "总选推荐项"已覆盖本场景(NFR-5);不触发 `code-auto` 升级 | 派生"code-auto 升级:识别设计目标确认类询问"任务 |
| R-2 `code-plan` 读 `design/.../RESULT.md` 时,小节位置漂移(格式被改) | 低 | 中 | D-2 锁定"## 设计目标"小节位置 = 顶部"## 文档头"之后;模板(D-8)固定该位置 | 修复模板,`code-plan` 仍按退化路径走(读不到 → 退化) |
| R-3 多次执行 `code-design` / `code-plan` → "## 设计目标"小节**未覆盖**前次内容 | 低 | 低 | NFR-3 幂等性 + D-6 明确"覆盖"语义 | 手动 `Edit` 工具覆盖 |
| R-4 `code-plan` 步骤 0b 读 `design` "## 设计目标"小节,**延迟 IO 失败** | 低 | 低 | 退化路径 D-4 已覆盖(读不到 → 退化) | — |
| R-5 `code-design` 步骤 0b 用户取消 `AskUserQuestion`(E-3) | 低 | 低 | E-3 锁定"中止,回写空 ## 设计目标 小节" | 用户重跑 |

---

## 9. 备选方案

### 备选 A(已否决):把"设计目标确认"放在 `code-require` 阶段

- **否决理由**:`code-require` 阶段需求尚未分析完,用户对"设计目标"的理解也未成熟;放到 `code-design` 阶段更合理(已有需求上下文,用户对功能边界有概念)

### 备选 B(已否决):不写"## 设计目标"小节,仅在 SKILL.md 内部变量中保留

- **否决理由**:`code-plan` 读不到 SKILL.md 内部变量;**必须**回写到 `design/.../RESULT.md` 顶部,D-2 锁定

### 备选 C(已否决):用单选问题(只问整体设计目标)代替多问题

- **否决理由**:Q-3 锁定"问多个问题";"功能性 / 扩展性 / 健壮性 / 可维护性"是 4 个独立维度,1 个问题 6 选项过于抽象;大需求场景下应分开提问(D-3)

### 备选 D(已否决):让 `code-review` 也读"## 设计目标"小节

- **否决理由**:`code-review` 不感知"设计目标"概念;FR-7.AC-7.3 强约束"不修改 8 个其他 code-* 技能";`code-review` 评审清单**不**变

---

## 10. 关联概要设计

| 关联设计编码 | 关联点 | 对本设计的影响 | 链接 |
| --- | --- | --- | --- |
| REQ-00017(V0.0.2) | `code-plan` 步骤 4A 拆任务 + `code-it` 末尾兜底 P-1 推进看板 | 本需求在 `code-plan` SKILL.md 中"步骤 0a"后**再**追加一节,与其现有"步骤 4A 拆任务"位置不重叠;任务粒度调整段叠加在"步骤 4A"前/后均可 | [RESULT](../REQ-00017/RESULT.md) |
| REQ-00016(V0.0.2) | 看板字段约定 / `code-auto` 步骤 0a 守卫 | 本需求不触发 `dashboard-conventions §规则 1`;`code-auto` 沿用"总选推荐项" | [RESULT](../REQ-00016/RESULT.md) |
| REQ-00009(V0.0.2) | `code-unit` 步骤 0a 守卫 | 与本需求"步骤 0b"模式同位叠加;`code-unit` 不变 | [RESULT](../REQ-00009/RESULT.md) |
| REQ-00010(V0.0.2) | `code-it` 步骤 0a 守卫 | 与本需求"步骤 0b"模式同位叠加;`code-it` 不变 | [RESULT](../REQ-00010/RESULT.md) |
| REQ-00005(V0.0.2) | "首步拉取"位置 = 步骤 0a | NFR-6 锁定:本需求"步骤 0b"叠加在 REQ-00005 之上,首步拉取**仍**为步骤 0a | [RESULT](../REQ-00005/RESULT.md) |

---

## 11. 待澄清 / 未决项

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-1 | `code-design` 步骤 0b 是否对所有需求都触发 5 问? | §5.3, §D-3 | 用户 | 后续调 `code-design` 时观察 |
| Q-2 | `code-plan` 步骤 0b 退化时,`AskUserQuestion` 1 问还是 5 问? | §5.3, §D-4 | 用户 | 后续调 `code-plan` 时观察 |
| Q-3 | `code-review` 是否应感知"## 设计目标"小节(在评审清单中加 1 项)? | §7, §10 | 用户 | 后续版本(本需求**不**触发) |

---

## 12. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-05 | v1 | 初始创建 | 完成首次概要设计:8 项决策(D-1~D-8) + 5 项设计目标(D-1~D-5) + 8 项不变量(INV-1~INV-8);沿用 REQ-00005 "步骤 0a"模式新增"步骤 0b";模板顶部预留"## 设计目标"占位;零新增依赖,4 个文件改动 | wangmiao |
