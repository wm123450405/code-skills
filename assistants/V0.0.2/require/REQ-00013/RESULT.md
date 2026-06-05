# 需求提示词文档 — REQ-00013(优化 `code-require` / `code-plan` / `code-fix` 等 6 技能,启用"编号+标题"显示)

- 需求编码:REQ-00013
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-04
- 最近更新:2026-06-04 15:25
- 当前版本:v1
- **主题**(来自用户输入):
  > 优化需求 `/code-require` / `/code-plan` / `/code-fix` 技能,为每个需求、任务、缺陷生成一个标题概述需求内容,30 字以内,并在和用户交互时不仅使用需求、任务、缺陷的编号,而是使用编号+标题的方式来方便用户理解。同时在记录相关看板和进度时除了编号也要附带这个标题,而不是仅编号或者`本需求`、`本任务`等字样。

---

## 1. 需求概述

**为谁**:`code-skills` 仓库的 AI 协作者 + 项目主导者(在屏幕输出/看板记录/进度报告中,期望"看到编号就理解是什么")。

**解决什么问题**:当前 6 个 `code-*` 技能在用户交互/报告/看板记录中,常用"编号"或"本需求"等指代词,无具体上下文:
- "正在处理 `TASK-REQ-00005-002`" — 不知道是做什么
- "本任务未完成" — 不知道哪个任务
- "派生自 `REQ-00001-002`" — 不知道派生自什么

**带来什么价值**:
1. **统一格式**:所有用户交互/报告用"REQ-00001 · Marketplace 改名落地"格式(Q-2 锁定 A)
2. **历史自动生效**:现有 12 个需求 + 19 个任务的"标题"**已存在**(在 `RESULT.md` 第 1 行 / `PLAN.md` 任务总览"标题"列),本需求落地后**显示环节自动启用**,无需手动回填
3. **零规范变更**:**不**新增字段(从已有内容派生,Q-1 锁定 A),不触发 `dashboard-conventions §规则 1`
4. **6 技能同时升级**:`code-require` / `code-plan` / `code-fix`(3 生成源)+ `code-it` / `code-unit` / `code-review` / `code-auto`(4 消费方,共 7 技能,但 `code-dashboard` 已含标题列,**0 改动**)

---

## 2. 背景与目标

### 2.1 背景
- 仓库实际有 **13 个 `code-*` 技能**(V0.0.0 共 10 个 + V0.0.2 新增 3 个)
- `code-fix` 是 V0.0.0 起的**真实存在**的技能,SKILL.md 17,878 bytes,本需求是**首次**改写它
- 现有 12 个需求(REQ-00001~00012)+ 19 个 V0.0.1 任务的"标题"**均已存在**(在 `RESULT.md` 第 1 行 / `PLAN.md` 任务总览"标题"列)
- 看板"任务清单"区段已含"标题"列(V0.0.1 起固定)
- V0.0.1 起派生任务(REQ-00001-005 / REQ-00002-009)由 `code-review` 写入 `PLAN.md`,有"标题"

### 2.2 业务目标
- **G-1**:6 技能用户交互/报告中统一启用"编号+标题"显示(Q-4 锁定 A)
- **G-2**:"标题"从已有内容派生,**不**新增字段(Q-1 锁定 A)
- **G-3**:格式 = `REQ-00001 · 标题`(Q-2 锁定 A)
- **G-4**:标题长度 ≤ 30 字符(Q-3 锁定 A)
- **G-5**:**不**触发 `dashboard-conventions §规则 1`(零字段变更)

### 2.3 本次目标
- 修改 `plugins/code-skills/skills/code-require/SKILL.md` 正文(不改 frontmatter)
- 修改 `plugins/code-skills/skills/code-plan/SKILL.md` 正文(不改 frontmatter)
- 修改 `plugins/code-skills/skills/code-fix/SKILL.md` 正文(不改 frontmatter)
- 修改 `plugins/code-skills/skills/code-it/SKILL.md` 正文(不改 frontmatter)
- 修改 `plugins/code-skills/skills/code-unit/SKILL.md` 正文(不改 frontmatter)
- 修改 `plugins/code-skills/skills/code-review/SKILL.md` 正文(不改 frontmatter)
- 修改 `plugins/code-skills/skills/code-auto/SKILL.md` 正文(不改 frontmatter)
- **不**修改 `code-dashboard` / `code-publish` / `code-version` / `code-rule` 4 个技能(Q-7 采纳默认)
- 严格遵循 `skill-conventions.md §规则 1`(frontmatter 不变)
- **不**修改 `marketplace.json` / `plugin.json`
- **不**修改 `assistants/rules/` 下任何规范文件(零规范变更)
- **不**修改 `plugins/code-skills/templates/`(从已有内容派生,不需新模板)

---

## 3. 用户角色与场景

### 3.1 角色
- **R-1 用户手动调技能**:在屏幕上看到"REQ-00001 · Marketplace 改名落地"格式
- **R-2 看板查看者**:看板"任务清单"区段已含"标题"列(0 改动)
- **R-3 AI 协作者**:在长会话中,所有报告/进度含"编号+标题"

### 3.2 关键场景

#### S-1:`code-require` 启动确认(主流程)
- 用户输入:`/code-require REQ-00013`
- 屏幕输出:
  ```
  正在处理: REQ-00013 · 优化 code-require/code-plan/code-fix 等 6 技能,启用"编号+标题"显示
  ```
- (本需求落地后)

#### S-2:`code-it` 前置任务守卫的中止报告(主流程)
- `code-it` 守卫不通过时,屏幕输出:
  ```
  ⛔ code-it 中止(存在未完成的前置任务)
  
  正在处理: REQ-00005 · 优化 code-require / code-design / code-plan,增加"首步拉取最新代码"与"末步兜底提交"
  
  前置任务状态:
    ✓ TASK-REQ-00005-001 · 同步 5 SKILL.md(只改正文)(开发状态=已完成)
    ✗ TASK-REQ-00005-002 · 同步 11 templates(改正文占位符+示例值)(开发状态=待开始)← 未完成
    ✗ TASK-REQ-00005-003 · 同步中英 README(同次 commit)(当前任务)
  
  推荐执行 /code-it TASK-REQ-00005-002 · 同步 11 templates(改正文占位符+示例值) 完成后,再执行 /code-it TASK-REQ-00005-003 · 同步中英 README(同次 commit)
  ```

#### S-3:`code-review` 派生任务(主流程)
- `code-review` 产生派生任务时:
  ```
  派生任务: TASK-REQ-00001-005 · 同步中英 README 中 GitHub URL 仓库名(审查派生)
  关联原任务: TASK-REQ-00001-002 · 同步中英 README
  ```
- (本需求落地后,派生任务的"标题"自动 < 30 字)

#### S-4:`code-auto` 进度报告(主流程)
- `code-auto` 每步打印:
  ```
  [code-auto] 步骤 1/6:code-require REQ-00007 · 增加 /code-auto 自动开发技能,驱动 6 子技能 + 评审循环 + 完全无人确认
  [code-auto]   → 产出 REQ-00007
  [code-auto] 步骤 2/6:code-design REQ-00007 · 同上
  [code-auto]   → 产出 design/REQ-00007/RESULT.md
  [code-auto] 步骤 3/6:code-plan REQ-00007 · 同上
  [code-auto]   → 拆 7 个任务
  [code-auto] 步骤 4/6:任务循环(7 个)
  [code-auto]   → 1/7:code-it TASK-REQ-00007-001 · 扩展 code-rule/SKILL.md 正文(类型识别 + Type A/B/C 文档化 + 工作目录约定) ✓
  ...
  ```

#### S-5:`code-publish` 前置检查报告(主流程)
- `code-publish` 不通过时:
  ```
  ✗ 发布前置检查未通过
  
  未完成项明细:
    - [需求] REQ-00005 · 优化 code-require / code-design / code-plan,增加"首步拉取最新代码"与"末步兜底提交" 状态=进行中(应该=已完成)
    - [任务] TASK-REQ-00005-005 · 扩展 code-unit 项目可测性守卫 开发状态=进行中(应该=已完成)
    - [缺陷] BUG-00003 · 修复某 X 函数崩溃 状态=待修复(应该=已修复)
  
  阻塞统计:
    - 需求:1 / 2 未完成
    - 任务:1 / N 未完成
    - 缺陷:1 / K 未修复
  ```

#### S-6:`code-fix` 缺陷登记(主流程)
- 用户输入:`/code-fix "用户报告:某 X 函数崩溃"`
- 屏幕输出:
  ```
  正在处理: BUG-00001 · 修复某 X 函数崩溃
  
  已创建 fix/RESULT.md:
    - 缺陷标题:某 X 函数崩溃
    - 严重度:P1
    - 关联任务:CODE-XYZ
  ```

#### S-7:历史 V0.0.1 任务自动显示
- V0.0.1 现有 19 个任务的"标题"在 `plan/.../PLAN.md` 第 3+ 行
- 本需求落地后,用户在 `code-it` 报告 / `code-dashboard` 输出中**自动**看到"编号+标题"格式
- **不**需手动回填

#### S-8:看板"任务清单"区段(0 改动)
- 看板"任务清单"区段已含"标题"列(V0.0.1 起固定)
- 本需求**不**触发 `dashboard-conventions §规则 1`

---

## 4. 功能需求(FR)

### FR-1:3 个生成源在产物中保留"标题"字段(Q-1 锁定 A)

- **描述**:`code-require` / `code-plan` / `code-fix` 产物的"标题"字段**已存在**(从已有内容派生),本需求不新增字段,只在生成时**显式声明**"标题已存在 + 长度 ≤ 30 字"
- **优先级**:必须
- **AC**:
  - AC-1.1:`code-require` 产物 `require/.../RESULT.md` 第 1 行(`# 需求提示词文档 — <需求标题>`)的"需求标题"长度 ≤ 30 字
  - AC-1.2:`code-plan` 产物 `plan/.../PLAN.md` 任务总览"标题"列所有任务标题长度 ≤ 30 字
  - AC-1.3:`code-fix` 产物 `fix/.../RESULT.md` 顶部"## 缺陷标题"或类似字段的"缺陷标题"长度 ≤ 30 字
  - AC-1.4:超 30 字时,`code-require` / `code-plan` / `code-fix` 截断到 30 字并加 `...`(Q-3 锁定 A)
  - AC-1.5:不修改 `RESULT.md` 模板 / `PLAN.md` 模板(Q-1 零规范变更)

### FR-2:6 技能用户交互/报告中启用"编号+标题"格式(Q-2 锁定 A)

- **描述**:6 技能(`code-require` / `code-plan` / `code-fix` / `code-it` / `code-unit` / `code-review` / `code-auto`)在所有用户可见的输出中,使用`REQ-00001 · 标题` / `TASK-... · 标题` / `BUG-00001 · 标题` 格式
- **优先级**:必须
- **AC**:
  - AC-2.1:**需求**显示格式 = `REQ-NNNNN · <需求标题>`
  - AC-2.2:**任务**显示格式 = `TASK-REQ-NNNNN-NNNNN · <任务标题>`(新格式)/ `REQ-NNNNN-NNNNN · <任务标题>`(旧格式透传)
  - AC-2.3:**缺陷**显示格式 = `BUG-NNNNN · <缺陷标题>`
  - AC-2.4:**不**使用"本需求" / "本任务" / "本缺陷"等指代词 — 替换为"编号+标题"
  - AC-2.5:屏幕输出 / 报告 / 看板记录 / 错误信息 / 派生任务通知**全部**用"编号+标题"格式

### FR-3:`code-require` 升级细节(Q-4 锁定 A)

- **描述**:`code-require` 启动时屏幕输出"正在处理: REQ-NNNNN · <标题>"
- **AC**:
  - AC-3.1:`code-require` 启动输出"正在处理: REQ-NNNNN · <需求标题>"
  - AC-3.2:`code-require` 完成输出"完成: REQ-NNNNN · <需求标题>"
  - AC-3.3:`code-require` 任何中间报告含"REQ-NNNNN · <需求标题>"
  - AC-3.4:`code-require` 输出的需求标题**截断**到 30 字(Q-3 锁定 A)

### FR-4:`code-plan` 升级细节(Q-4 锁定 A)

- **描述**:`code-plan` 启动时屏幕输出"正在处理: REQ-NNNNN · <需求标题>";每个任务拆分时输出"TASK-... · <任务标题>"
- **AC**:
  - AC-4.1:`code-plan` 启动输出"正在处理: REQ-NNNNN · <需求标题>"
  - AC-4.2:`code-plan` 拆分每个任务时输出"TASK-... · <任务标题>"
  - AC-4.3:`code-plan` 任何中间报告含"编号+标题"
  - AC-4.4:`code-plan` 任务总览中**所有**任务标题**截断**到 30 字

### FR-5:`code-fix` 升级细节(Q-4 锁定 A)

- **描述**:`code-fix` 启动时屏幕输出"正在处理: BUG-NNNNN · <缺陷标题>";产出 `fix/.../RESULT.md` 顶部"## 缺陷标题"小节
- **AC**:
  - AC-5.1:`code-fix` 启动输出"正在处理: BUG-NNNNN · <缺陷标题>"
  - AC-5.2:`fix/.../RESULT.md` 顶部含"## 缺陷标题"小节(本需求**新增**)
  - AC-5.3:`code-fix` 完成输出"已修复: BUG-NNNNN · <缺陷标题>"
  - AC-5.4:`code-fix` 任何中间报告含"编号+标题"
  - AC-5.5:`code-fix` 输出的缺陷标题**截断**到 30 字

### FR-6:`code-it` 升级细节(Q-4 锁定 A)

- **描述**:`code-it` 启动时屏幕输出"正在处理: TASK-... · <任务标题>";所有报告含"编号+标题"
- **AC**:
  - AC-6.1:`code-it` 启动输出"正在处理: TASK-... · <任务标题>"
  - AC-6.2:`code-it` 中止报告(REQ-00010 守卫)含"REQ-NNNNN · 标题" + "TASK-... · 标题"
  - AC-6.3:`code-it` 完成输出"已完成: TASK-... · <任务标题>"
  - AC-6.4:`code-it` 任何报告**不**使用"本任务"等指代词

### FR-7:`code-unit` 升级细节(Q-4 锁定 A)

- **描述**:`code-unit` 启动时屏幕输出"正在处理: TASK-... · <任务标题>";报告含"编号+标题"
- **AC**:
  - AC-7.1:`code-unit` 启动输出"正在处理: TASK-... · <任务标题>"
  - AC-7.2:`code-unit` 守卫跳过(REQ-00009 项目不可测)报告含"TASK-... · 标题"
  - AC-7.3:`code-unit` 完成输出"已运行-通过/失败: TASK-... · <任务标题>"

### FR-8:`code-review` 升级细节(Q-4 锁定 A)

- **描述**:`code-review` 启动时屏幕输出"正在处理: REQ-NNNNN · <需求标题>";派生任务的"标题"截断到 30 字
- **AC**:
  - AC-8.1:`code-review` 启动输出"正在处理: REQ-NNNNN · <需求标题>"
  - AC-8.2:`code-review` 派生任务写入 `PLAN.md` 时,"标题"列 ≤ 30 字
  - AC-8.3:`code-review` 评审发现报告中"派生任务"列含"编号+标题"
  - AC-8.4:`code-review` 完成输出"已评审: REQ-NNNNN · <需求标题>"

### FR-9:`code-auto` 升级细节(Q-4 锁定 A)

- **描述**:`code-auto` 调子技能时,所有打印 / 报告 / `auto-report.md` 含"编号+标题"
- **AC**:
  - AC-9.1:`code-auto` 每步打印含"编号+标题"(例:`[code-auto] 步骤 1/6:code-require REQ-00007 · 增加 /code-auto 自动开发技能...`)
  - AC-9.2:`code-auto` 完整报告(`require/REQ-NNNNN/auto-report.md`)含"编号+标题"
  - AC-9.3:`code-auto` 派生任务循环输出含"编号+标题"

### FR-10:不修改 4 个其他 `code-*` 技能(Q-7 采纳默认)

- **描述**:`code-dashboard` / `code-publish` / `code-version` / `code-rule` **不**被本需求修改
- **AC**:
  - AC-10.1:`code-dashboard` 现有"任务清单"区段已含"标题"列 — **不**触发
  - AC-10.2:`code-publish` **本轮**升级"前置检查报告"中"未完成项"用"REQ-NNNNN · 标题" / "TASK-... · 标题" / "BUG-NNNNN · 标题"
  - AC-10.3:`code-version` / `code-rule` **不**被本需求修改

### FR-11:不修改 marketplace 与 plugin 与规范

- **AC**:
  - AC-11.1:`marketplace.json` / `plugin.json` **不**被本需求修改
  - AC-11.2:`dashboard-conventions.md` **不**被本需求修改(Q-1 零规范变更)
  - AC-11.3:`commit-conventions.md` 规则 1 **不**被本需求填充
  - AC-11.4:中英 README 若需更新,按 `doc-conventions §规则 1` 同次提交中英 — 但本需求**不**主动写 README(由 `code-rule` 沉淀)

---

## 5. 非功能需求 / 约束(NFR)

### NFR-1:零新增依赖
- **描述**:不引入新依赖
- **强制级别**:必须

### NFR-2:零规范变更(Q-1 锁定)
- **描述**:**不**修改 `RESULT.md` 模板 / `PLAN.md` 模板 / 看板"任务清单"区段 / `dashboard-conventions.md`
- **强制级别**:必须
- **理由**:"标题"从已有内容派生,无需新增字段

### NFR-3:字符数 ≤ 30
- **描述**:标题长度 ≤ 30 字符(Q-3 锁定 A)
- **强制级别**:必须
- **理由**:用户原话"30 字以内"
- **实现侧**:`code-require` / `code-plan` / `code-fix` 检测标题长度,超 30 字截断到 30 字 + `...`

### NFR-4:历史自动生效
- **描述**:现有 12 个 V0.0.0~V0.0.2 需求 + 19 个 V0.0.1 任务的"标题"**已存在**,本需求落地后**显示环节自动启用**
- **强制级别**:必须
- **理由**:本需求**不**需手动回填

### NFR-5:`code-publish` 前置检查报告升级
- **描述**:`code-publish` 前置检查报告中"未完成项"用"REQ-NNNNN · 标题" / "TASK-... · 标题" / "BUG-NNNNN · 标题" 格式
- **强制级别**:必须

### NFR-6:不修改 4 个其他技能
- **描述**:`code-dashboard` / `code-version` / `code-rule` **不**被本需求修改;`code-publish` 升级范围有限(仅报告格式)
- **强制级别**:必须

### NFR-7:frontmatter 不变
- **描述**:7 个 `code-*` 技能 SKILL.md 的 frontmatter `name` + `description` **不**变
- **强制级别**:必须
- **理由**:遵循 `skill-conventions.md §规则 1`

### NFR-8:增量修改
- **描述**:7 个 `code-*` 技能 SKILL.md 修改方式为 **Edit 工具追加**"显示格式"逻辑,不重写稳定章节
- **强制级别**:必须
- **理由**:避免破坏现有 frontmatter / 既有流程

### NFR-9:与 `code-auto` 退出码兼容
- **描述**:本需求**不**改变 `code-auto` 退出码语义(子技能退出码 ≠ 0 才中断)
- **强制级别**:必须

### NFR-10:派生任务标题同样受 30 字限制
- **描述**:`code-review` 派生任务的"标题"列 ≤ 30 字(本需求 FR-8.AC-8.2 覆盖)
- **强制级别**:必须

---

## 6. 页面与界面(显示模板)

### 6.1 启动输出格式

| 技能 | 启动输出 |
| --- | --- |
| `code-require` | `正在处理: REQ-NNNNN · <需求标题>` |
| `code-plan` | `正在处理: REQ-NNNNN · <需求标题>`(后续每任务:`拆分: TASK-... · <任务标题>`) |
| `code-fix` | `正在处理: BUG-NNNNN · <缺陷标题>` |
| `code-it` | `正在处理: TASK-... · <任务标题>` |
| `code-unit` | `正在处理: TASK-... · <任务标题>` |
| `code-review` | `正在处理: REQ-NNNNN · <需求标题>` |
| `code-auto` | `[code-auto] 步骤 N/M:code-require REQ-NNNNN · <需求标题>` |

### 6.2 完成输出格式

| 技能 | 完成输出 |
| --- | --- |
| `code-require` | `完成: REQ-NNNNN · <需求标题>` |
| `code-plan` | `完成: REQ-NNNNN · <需求标题>(拆 N 个任务)` |
| `code-fix` | `已修复: BUG-NNNNN · <缺陷标题>` |
| `code-it` | `已完成: TASK-... · <任务标题>` |
| `code-unit` | `已运行-通过/失败: TASK-... · <任务标题>` |
| `code-review` | `已评审: REQ-NNNNN · <需求标题>(N 条发现)` |
| `code-auto` | `✓ code-auto 完成: REQ-NNNNN · <需求标题>` |

### 6.3 `code-it` 中止报告模板(REQ-00010 升级)

```
⛔ code-it 中止(存在未完成的前置任务)

正在处理: REQ-NNNNN · <需求标题>(任务 TASK-... · <任务标题>)

前置任务状态:
  ✓ TASK-... · <任务标题>(开发状态=已完成)
  ✗ TASK-... · <任务标题>(开发状态=待开始)← 未完成
  ✗ TASK-... · <任务标题>(当前任务)

推荐执行 /code-it TASK-... · <任务标题> 完成后,再执行 /code-it TASK-... · <任务标题>
```

### 6.4 `code-publish` 前置检查报告(REQ-00006 升级)

```
✗ 发布前置检查未通过

未完成项明细:
  - [需求] REQ-NNNNN · <需求标题> 状态=进行中(应该=已完成)
  - [任务] TASK-... · <任务标题> 开发状态=进行中(应该=已完成)
  - [缺陷] BUG-NNNNN · <缺陷标题> 状态=待修复(应该=已修复)

阻塞统计:
  - 需求:1 / 2 未完成
  - 任务:1 / N 未完成
  - 缺陷:1 / K 未修复
```

### 6.5 标题截断规则(NFR-3)

| 原文 | 字符数 | 截断后 |
| --- | --- | --- |
| `优化 code-require / code-design / code-plan,增加"首步拉取最新代码"与"末步兜底提交"` | 47 字 | `优化 code-require / code-design / code-plan...` |
| `增加 /code-dashboard 开发看板技能,展示当前版本需求/任务/缺陷的整体执行情况` | 41 字 | `增加 /code-dashboard 开发看板技能...` |
| `Marketplace 改名落地` | 9 字 | `Marketplace 改名落地`(无需截断) |

---

## 7. 交互逻辑

### 7.1 启动流程(以 `code-require` 为例)

```
[启动]
  ↓
[步骤 0:版本上下文检测]
  ↓
[屏幕打印: 正在处理: REQ-NNNNN · <需求标题>]  ← 本需求升级
  ↓
[步骤 1-?:原有流程]
  ↓
[屏幕打印: 完成: REQ-NNNNN · <需求标题>]  ← 本需求升级
  ↓
[退出]
```

### 7.2 标题截断算法(NFR-3)

```
[读取标题]
  ↓
[len(标题) > 30?]
  ├─ 否 → [原样使用]
  └─ 是 → [截断到 30 字 + "..."]
          (例: "优化 3 技能,增加首..."(30 字符))
  ↓
[显示]
```

### 7.3 标题字段来源解析

```
[code-require 解析]
  ↓
[读 require/.../RESULT.md 第 1 行]
  ↓
[正则: # 需求提示词文档 — <需求标题>]
  ↓
[提取 <需求标题>]
  ↓
[截断到 30 字]
  ↓
[显示]
```

```
[code-plan 解析]
  ↓
[读 plan/.../PLAN.md 任务总览]
  ↓
[定位当前任务行]
  ↓
[提取"标题"列]
  ↓
[截断到 30 字]
  ↓
[显示]
```

```
[code-fix 解析]
  ↓
[读 fix/.../RESULT.md 顶部"## 缺陷标题"小节]
  ↓
[提取缺陷标题]
  ↓
[截断到 30 字]
  ↓
[显示]
```

---

## 8. 数据与状态

### 8.1 标题字段位置

| 技能 | 标题位置 |
| --- | --- |
| `code-require` | `require/.../RESULT.md` 第 1 行(`# 需求提示词文档 — <标题>`) |
| `code-plan` | `plan/.../PLAN.md` 任务总览"标题"列 |
| `code-fix` | `fix/.../RESULT.md` 顶部"## 缺陷标题"小节(**本轮新增**) |

### 8.2 标题格式数据

```ts
{
  // 启动输出
  startLog: {
    codeRequire: (reqNum: string, title: string) => `正在处理: ${reqNum} · ${title}`,
    codePlan: (reqNum: string, title: string) => `正在处理: ${reqNum} · ${title}`,
    codeFix: (bugNum: string, title: string) => `正在处理: ${bugNum} · ${title}`,
    codeIt: (taskNum: string, title: string) => `正在处理: ${taskNum} · ${taskTitle}`,
    codeUnit: (taskNum: string, title: string) => `正在处理: ${taskNum} · ${taskTitle}`,
    codeReview: (reqNum: string, title: string) => `正在处理: ${reqNum} · ${title}`,
    codeAuto: (step: number, total: number, skillName: string, reqNum: string, title: string) => `[code-auto] 步骤 ${step}/${total}:${skillName} ${reqNum} · ${title}`
  }
}
```

### 8.3 标题截断算法

```ts
function truncateTitle(title: string, maxLen: number = 30): string {
  // 字符数计算(汉字/字母/数字/标点 = 1 字)
  if ([...title].length <= maxLen) return title
  return [...title].slice(0, maxLen).join('') + '...'
}
```

### 8.4 任务编号解析(沿用既有规范)

```text
新格式: ^TASK-(REQ|BUG)-(\d{5})-(\d{5})$
旧格式: ^(REQ|BUG)-(\d{5})-(\d{5})$
```

---

## 9. 边界与异常

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | 无 `.current-version` | 提示调 `code-version`,退出(同其他 12 技能) |
| **E-2** | 标题 > 30 字符 | 截断到 30 字符 + `...`(NFR-3) |
| **E-3** | 标题字段缺失(理论不可能) | 退化:用"编号"占位,屏幕输出"编号+(无标题)" |
| **E-4** | 历史任务(REQ-00001~00003 旧格式) | 透传旧格式 + 拼接标题(同 `code-dashboard` NFR-3) |
| **E-5** | `code-fix` 产出无"## 缺陷标题"小节 | 退化:用 `BUG-NNNNN` 占位 |
| **E-6** | `code-review` 派生任务标题 > 30 字 | 截断到 30 字 + `...` |
| **E-7** | `code-auto` 调子技能时标题解析失败 | 退化:用"编号"占位,屏幕输出"编号+(无标题)" |
| **E-8** | 用户希望"不截断"标题 | 手动编辑 `RESULT.md` 第 1 行(本需求**不**提供 CLI 参数) |
| **E-9** | 多次执行 `code-require` / `code-plan` / `code-fix` | 标题覆盖(NFR-4 幂等) |

---

## 10. 验收标准(AC 总览)

按 FR 编号归类,合计 ~30 条:

- **FR-1**(5 条):AC-1.1 ~ AC-1.5
- **FR-2**(5 条):AC-2.1 ~ AC-2.5
- **FR-3**(4 条):AC-3.1 ~ AC-3.4
- **FR-4**(4 条):AC-4.1 ~ AC-4.4
- **FR-5**(5 条):AC-5.1 ~ AC-5.5
- **FR-6**(4 条):AC-6.1 ~ AC-6.4
- **FR-7**(3 条):AC-7.1 / AC-7.2 / AC-7.3
- **FR-8**(4 条):AC-8.1 ~ AC-8.4
- **FR-9**(3 条):AC-9.1 / AC-9.2 / AC-9.3
- **FR-10**(3 条):AC-10.1 / AC-10.2 / AC-10.3
- **FR-11**(4 条):AC-11.1 ~ AC-11.4
- **NFR-1**(1 条):零依赖
- **NFR-2**(1 条):零规范变更
- **NFR-3**(1 条):字符数 ≤ 30
- **NFR-4**(1 条):历史自动生效
- **NFR-5**(1 条):publish 报告升级
- **NFR-6**(1 条):不改 4 技能
- **NFR-7**(1 条):frontmatter 不变
- **NFR-8**(1 条):增量修改
- **NFR-9**(1 条):与 code-auto 退出码兼容
- **NFR-10**(1 条):派生任务标题同样受 30 字限制

**总计**:约 30 条 AC。

---

## 11. 关联需求

| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| **REQ-00004**(V0.0.2) | `code-dashboard` 看板"标题"列已存在 | NFR-2:零规范变更,**不**触发 | `./assistants/V0.0.2/require/REQ-00004/RESULT.md` |
| **REQ-00005**(V0.0.2) | `code-require` / `code-plan` 已有"首步拉取+末步提交" | NFR-8:本需求"显示格式"叠加在 REQ-00005 之上 | `./assistants/V0.0.2/require/REQ-00005/RESULT.md` |
| **REQ-00006**(V0.0.2) | `code-publish` 前置检查报告 | NFR-5:`code-publish` 报告升级"未完成项"用"编号+标题" | `./assistants/V0.0.2/require/REQ-00006/RESULT.md` |
| **REQ-00007**(V0.0.2) | `code-auto` 调 6 子技能 | FR-9:`code-auto` 进度报告用"编号+标题" | `./assistants/V0.0.2/require/REQ-00007/RESULT.md` |
| **REQ-00008**(V0.0.2) | `code-review` 派生任务 | FR-8.AC-8.2:派生任务标题 ≤ 30 字 | `./assistants/V0.0.2/require/REQ-00008/RESULT.md` |
| **REQ-00009**(V0.0.2) | `code-unit` 守卫跳过报告 | FR-7.AC-7.2:报告含"编号+标题" | `./assistants/V0.0.2/require/REQ-00009/RESULT.md` |
| **REQ-00010**(V0.0.2) | `code-it` 中止报告 | FR-6.AC-6.2:中止报告含"编号+标题" | `./assistants/V0.0.2/require/REQ-00010/RESULT.md` |
| **REQ-00011**(V0.0.2) | `code-plan` 步骤 0b | 不影响 | `./assistants/V0.0.2/require/REQ-00011/RESULT.md` |
| **REQ-00012**(V0.0.2) | 仓库根 README/CLAUDE.md | 不影响 | `./assistants/V0.0.2/require/REQ-00012/RESULT.md` |
| **REQ-00001**(V0.0.1) | V0.0.1 任务的"标题"已存在 | NFR-4:历史自动生效 | `./assistants/V0.0.1/plan/REQ-00001/PLAN.md` 任务总览 |
| **REQ-00003**(V0.0.1) | `code-rule` 维护项目级规范 | 本需求**不**直接写规范,留作 follow-up | `./assistants/V0.0.1/require/REQ-00003/RESULT.md` |

详细关联分析见 `related-requirements.md`。

---

## 12. 待澄清 / 未决项(本轮未处理 / 留作默认)

### Q-5:历史回填
- **状态**:采纳默认(自动生效)

### Q-6:与 `code-review` 派生任务的"标题"
- **状态**:采纳默认(本轮 `code-review` 升级)

### Q-7:与 `code-publish` / `code-dashboard` 协同
- **状态**:采纳默认(`code-publish` 升级报告;`code-dashboard` 不变)

### Q-8:与 `code-fix` 的关系
- **状态**:采纳默认(本轮首次升级 `code-fix`)

### Q-9:与 REQ-00005 协同
- **状态**:采纳默认(独立新增)

### Q-10:`commit-conventions.md` 与 CLAUDE.md 追加
- **状态**:采纳默认(不追加,留作 follow-up)

### Q-11(新增):派生任务预警
- **建议派生**:
  - "用 `code-rule` 沉淀 '标题字段约定' "< 30 字
  - "`code-fix` 增加 '缺陷标题' 字段约定" 任务
- **状态**:本需求不阻塞

---

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-04 15:25 | v1 | 初始创建:11 FR / 10 NFR / ~30 AC / 9 个边界场景;Q-1/Q-2/Q-3/Q-4 锁定,Q-5~Q-10 留默认/未采用;用户原文 5 处笔误已纠正(3 个 `/code-X` → `/code-X` + "缺编" → "缺陷" + 2 处 "是" → "时");Q-1 锁定"**从已有内容派生,不新增字段**"(零规范变更 — `RESULT.md` 第 1 行 + `PLAN.md` 任务总览"标题"列已存在);Q-2 锁定"**`REQ-00001 · 标题`**"(中点 `·` 格式);Q-3 锁定"**字符数 ≤ 30**";Q-4 锁定"**本轮升级 6 技能**"(3 生成源 + 4 消费方,`code-dashboard` 不变因看板标题列已存在);用户原话"30 字以内"按现代 UI 习惯解读为"30 个字符";`code-fix` 是 V0.0.0 起的真实存在技能(SKILL.md 17,878 bytes),本轮首次升级;NFR-4 历史自动生效(现有 12 需求 + 19 V0.0.1 任务的"标题"已存在,本轮仅启用"显示"环节);NFR-5 `code-publish` 报告升级;NFR-6 不改 4 技能(`code-dashboard` / `code-version` / `code-rule` + `code-publish` 仅报告部分) | wangmiao |
