# 需求提示词文档 — REQ-00011(优化 `/code-design` / `/code-plan`,增加"设计目标确认"环节)

- 需求编码:REQ-00011
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-04
- 最近更新:2026-06-04 14:57
- 当前版本:v1
- **主题**(来自用户输入):
  > 优化需求: `/code-desgin`(笔误 → `/code-design`)、`/code-plan`(无需纠正 — `/code-plan` 已正确)在做需求概设和详设过程中,在适当环节中需要用户确认开发修改的内容需要以**更少的代码改修**为目标、或以**更灵活的后期拓展**为目标等设计目标进行设计,就是让用户来确认一些当前需求在软件设计上的**功能性、扩展性、健壮性、可维护性**的程度。

---

## 1. 需求概述

**为谁**:`code-skills` 仓库的 AI 协作者 + 项目主导者(在 `code-design` / `code-plan` 实际产出设计时,期望"对设计目标做选择,避免 AI 自由裁量过度")。

**解决什么问题**:`code-design` / `code-plan` 现有流程**无**用户确认环节,AI 默认按"最常见方式"产出。在以下场景会导致问题:
- **设计过度**:用户希望"少改",AI 给出"灵活拓展"方案,代码复杂度过高
- **设计不足**:用户希望"灵活",AI 给出"够用就好"方案,后续需求改动时返工
- **设计目标不一致**:用户与 AI 对"功能性 / 扩展性 / 健壮性 / 可维护性"的优先级理解不同

**带来什么价值**:
1. **明确设计目标**:`code-design` 启动时(步骤 0b)问 1-N 个"设计目标/维度"问题
2. **回写到设计文档**:`design/.../RESULT.md` + `plan/.../RESULT.md` 顶部新增"## 设计目标"小节
3. **下游传导**:`code-plan` 读 `design/.../RESULT.md` 的"设计目标"小节 → 据此**调整**任务拆分粒度(扩展性高 → 加"扩展架构设计" / "设计模式使用"等任务)
4. **完全可独立执行**:不依赖 `code-auto` / `code-review` 等其他技能

---

## 2. 背景与目标

### 2.1 背景
- `code-design` / `code-plan` 是 V0.0.0 起就存在的 7 个 `code-*` 之二;V0.0.1 中所有设计/计划产物均由 AI 直接产出
- V0.0.2 REQ-00005 已为这 2 个技能加"首步拉取"与"末步兜底",本需求在 REQ-00005 之上**再**追加"步骤 0b 设计目标确认"
- V0.0.2 REQ-00009 / REQ-00010 已在其他 2 个技能加"步骤 0a 守卫",本需求采用同位叠加模式
- V0.0.1 起 `design/.../RESULT.md` / `plan/.../RESULT.md` 模板均**无**"设计目标"小节,本需求新增

### 2.2 业务目标
- **G-1**:`code-design` 启动时增加"步骤 0b 设计目标确认"环节(Q-1 锁定)
- **G-2**:`code-plan` 启动时增加"步骤 0b 设计目标确认"环节(可读 `design/.../RESULT.md` 的"设计目标"小节)
- **G-3**:`AskUserQuestion` 形态 = 多个问题(设计目标 + 设计维度,各 1 问题),可分开提问(Q-3 锁定)
- **G-4**:回写到 `design/.../RESULT.md` + `plan/.../RESULT.md` 顶部"## 设计目标"小节(Q-2 锁定)
- **G-5**:`code-plan` 据 `design/.../RESULT.md` 的"设计目标"小节**调整**任务拆分粒度(Q-2 补充)

### 2.3 本次目标
- 修改 `plugins/code-skills/skills/code-design/SKILL.md` 正文(不改 frontmatter)— 增加"步骤 0b"
- 修改 `plugins/code-skills/skills/code-plan/SKILL.md` 正文(不改 frontmatter)— 增加"步骤 0b"
- 修改 `plugins/code-skills/skills/code-design/templates/...` (若有)— 在模板顶部预留"## 设计目标"小节
- 修改 `plugins/code-skills/skills/code-plan/templates/...` (若有)— 在模板顶部预留"## 设计目标"小节
- 严格遵循 `skill-conventions.md §规则 1`(frontmatter 不变)
- 不修改 `marketplace.json` / `plugin.json` / 其他 8 个 `code-*` 技能
- **不**触发 `dashboard-conventions §规则 1`(因为不修改看板)

---

## 3. 用户角色与场景

### 3.1 角色
- **R-1 严格"少改"主导者**:希望"最小化代码改动",AI 据此产出"够用就好"方案
- **R-2 "灵活"主导者**:希望"为未来留空间",AI 据此产出"扩展性高"方案,可能拆出更多任务
- **R-3 平衡主导者**:希望"中等投入 + 中等灵活",AI 据此产出"平衡"方案

### 3.2 关键场景

#### S-1:`code-design` 启动确认(主流程)
- 用户输入:`/code-design REQ-00010`
- 技能执行:
  1. **步骤 0a 拉取**(沿用 REQ-00005)
  2. **步骤 0b 设计目标确认**(新增)— 触发 `AskUserQuestion` 多个问题:
     - Q1:整体设计目标?(`--minimal` / `--extensible` / `--balanced`)
     - Q2:功能性优先级?(高/中/低)
     - Q3:扩展性优先级?(高/中/低)
     - Q4:健壮性优先级?(高/中/低)
     - Q5:可维护性优先级?(高/中/低)
  3. 用户选择 → **回写**到 `design/REQ-00010/RESULT.md` 顶部"## 设计目标"小节
  4. 进入原"步骤 0-N"流程,根据"设计目标"产出
- 用户看到:
  ```
  === code-design 设计目标确认 ===
  
  整体设计目标:
    选:更少代码改修(--minimal)
  
  维度优先级:
    功能性:中
    扩展性:低
    健壮性:高
    可维护性:高
  
  已回写至 design/REQ-00010/RESULT.md "## 设计目标" 小节
  ```

#### S-2:`code-plan` 读 `design` "设计目标"(主流程)
- 用户输入:`/code-plan REQ-00010`
- 技能执行:
  1. **步骤 0a 拉取**(沿用 REQ-00005)
  2. **步骤 0b 设计目标确认**(新增)
     - 读 `design/REQ-00010/RESULT.md` 的"## 设计目标"小节 → 存在
     - 沿用该小节的内容作为 `code-plan` 的设计目标
     - **不**重新问用户
  3. 进入原"步骤 0-N"流程,根据"设计目标"调整任务拆分粒度
- (用户**不**感知"步骤 0b"被触发,因为无需回答)

#### S-3:`code-plan` 读不到 `design` "设计目标"(边界)
- 假设 `code-plan` 启动时,`design/.../RESULT.md` 不存在(用户跳过了 `code-design`)
- 技能执行:
  1. **步骤 0b 设计目标确认** — 读 `design/.../RESULT.md` → 不存在
  2. 退化行为:**回退到用户手动确认**(Q-2 锁定 — 不写文档时不能传导)
  3. `AskUserQuestion` 问整体设计目标(简化版,只问 1 个问题)
  4. 写入 `plan/.../RESULT.md` 顶部"## 设计目标"小节(为下游留痕)
- 用户看到:
  ```
  === code-plan 设计目标确认(无 design 输入) ===
  
  ⚠ 未检测到 design/REQ-00010/RESULT.md
  请回答设计目标:
    整体设计目标?
  
  [用户回答]
  
  已回写至 plan/REQ-00010/RESULT.md "## 设计目标" 小节
  ```

#### S-4:大需求分开提问(Q-3 锁定)
- 用户输入:`/code-design REQ-00012`(假设是大需求)
- 技能执行:
  1. **步骤 0b 设计目标确认** — `code-design` 阶段可问 5 个问题(整体 + 4 维度)
  2. 进一步:`code-design` 可对"不同细节功能"分别问
  3. 多个 `AskUserQuestion` 调用
- 用户感知:多轮问答

#### S-5:`code-auto` 调 `code-design` / `code-plan`(边界)
- 用户输入:`/code-auto "添加登录功能"`
- 技能执行:
  1. `code-auto` 调 `code-design` → 步骤 0b 触发 `AskUserQuestion` → `code-auto` 据 FR-3 Q-4 锁定 A "总选推荐项" → 选"平衡"
  2. 回写"## 设计目标"小节(平衡)
  3. `code-auto` 调 `code-plan` → 读"## 设计目标"小节 → 沿用"平衡"
  4. 任务拆分按"平衡"产出
- (本需求主要面向"用户手动调"场景;`code-auto` 自动跑会"总选推荐项")

#### S-6:无激活版本(边界)
- 用户输入:`/code-design REQ-00010`,但 `.current-version` 不存在
- 技能执行:同其他 9 技能,提示调 `code-version`,退出

---

## 4. 功能需求(FR)

### FR-1:`code-design` 新增"步骤 0b 设计目标确认"

- **描述**:`code-design` 在"步骤 0a 拉取"**之后**,新增"步骤 0b 设计目标确认"
- **确认内容**:`AskUserQuestion` 多个问题
- **优先级**:必须
- **AC**:
  - AC-1.1:`code-design/SKILL.md` 在"步骤 0a"后显式列出"步骤 0b"
  - AC-1.2:至少 1 个 `AskUserQuestion` 调用(整体设计目标)
  - AC-1.3:可调用 1-5 个问题(整体 + 4 维度),由技能根据需求规模自适应
  - AC-1.4:用户回答后,屏幕打印"已回写至 design/<REQ>/RESULT.md '## 设计目标' 小节"
  - AC-1.5:不修改 frontmatter;不修改"步骤 0"及之后的原有内容(增量追加)

### FR-2:`code-plan` 新增"步骤 0b 设计目标确认"

- **描述**:`code-plan` 在"步骤 0a 拉取"**之后**,新增"步骤 0b 设计目标确认"
- **与 FR-1 区别**:
  - 若 `design/.../RESULT.md` 的"## 设计目标"小节**存在** → 沿用该小节,**不**重新问用户
  - 若**不**存在 → 退化(走 FR-3)
- **优先级**:必须
- **AC**:
  - AC-2.1:`code-plan/SKILL.md` 在"步骤 0a"后显式列出"步骤 0b"
  - AC-2.2:读 `design/REQ-NNNNN/RESULT.md` 的"## 设计目标"小节
  - AC-2.3:存在 → 屏幕打印"沿用 design 的设计目标:<摘要>"+ 进入原流程
  - AC-2.4:不存在 → 走 FR-3 退化
  - AC-2.5:不修改 frontmatter;不修改"步骤 0"及之后的原有内容

### FR-3:`code-plan` 退化行为(无 `design` 输入)

- **描述**:`code-plan` 步骤 0b 读不到 `design/.../RESULT.md` 时,退化到"用户手动确认"
- **退化流程**:
  - 触发 `AskUserQuestion` 1 个问题(整体设计目标)
  - 用户回答 → 写入 `plan/.../RESULT.md` 顶部"## 设计目标"小节
- **优先级**:必须
- **AC**:
  - AC-3.1:触发 `AskUserQuestion` 1 个问题(整体设计目标)
  - AC-3.2:用户回答后,写入 `plan/.../RESULT.md` 顶部"## 设计目标"小节
  - AC-3.3:**不**写 `design/.../RESULT.md`(因 `code-design` 未跑过,职责分离)

### FR-4:`code-plan` 根据"设计目标"调整任务拆分粒度

- **描述**:`code-plan` 读"设计目标"小节后,据此**调整**任务拆分粒度
- **调整规则**(用户原话):
  - 扩展性高 → 加"扩展架构设计" / "设计模式使用"等**更细致任务步骤**
  - 更少代码改修 → 任务粒度**较粗**(合并相关步骤)
  - 平衡 → 默认粒度
- **优先级**:必须
- **AC**:
  - AC-4.1:扩展性优先级 = `高` → 任务总览中含"扩展架构设计" / "设计模式使用"等任务(至少 1 个)
  - AC-4.2:整体设计目标 = `--minimal` → 任务粒度较粗(同类任务合并)
  - AC-4.3:整体设计目标 = `--balanced` → 默认粒度(无调整)
  - AC-4.4:其他维度优先级(功能性 / 健壮性 / 可维护性)作为参考,不强制加任务

### FR-5:回写文档"## 设计目标"小节(Q-2 锁定)

- **描述**:用户回答设计目标后,写入 `design/.../RESULT.md` + `plan/.../RESULT.md` 顶部"## 设计目标"小节
- **小节结构**:
  - **整体设计目标**:`--minimal` / `--extensible` / `--balanced`
  - **维度优先级**:功能性 / 扩展性 / 健壮性 / 可维护性 各 `高/中/低`
  - **回写时间**:`YYYY-MM-DD HH:mm`
  - **回写触发**:`code-design` / `code-plan` 步骤 0b
- **优先级**:必须
- **AC**:
  - AC-5.1:`code-design` 完成后,`design/.../RESULT.md` 顶部含"## 设计目标"小节
  - AC-5.2:`code-plan` 完成后,`plan/.../RESULT.md` 顶部含"## 设计目标"小节
  - AC-5.3:小节内容含 4 个字段(整体 + 3 个维度优先级)
  - AC-5.4:不破坏 `RESULT.md` 原有章节(增量追加顶部)
  - AC-5.5:多次执行 → 覆盖前次内容(NFR-3 幂等)

### FR-6:`AskUserQuestion` 多个问题(Q-3 锁定)

- **描述**:`code-design` 步骤 0b 触发多个 `AskUserQuestion`
- **典型问题清单**:
  - Q1:整体设计目标?(`--minimal` / `--extensible` / `--balanced`)
  - Q2:功能性优先级?(高/中/低)
  - Q3:扩展性优先级?(高/中/低)
  - Q4:健壮性优先级?(高/中/低)
  - Q5:可维护性优先级?(高/中/低)
- **灵活性**:`code-design` 阶段可对不同细节功能**分开提问**(大需求场景)
- **优先级**:必须
- **AC**:
  - AC-6.1:至少 1 个 `AskUserQuestion` 调用
  - AC-6.2:可调用 1-5 个问题
  - AC-6.3:大需求可对不同细节功能分开问
  - AC-6.4:每问 1 个明确的设计维度(避免 1 问 6 选项)
  - AC-6.5:**不**与现有"子流程"询问混淆(本步骤**只**问设计目标,其他询问在子流程中)

### FR-7:不修改 8 个其他 `code-*` 技能

- **描述**:本需求**只**修改 `code-design` / `code-plan` 2 个技能
- **优先级**:必须
- **AC**:
  - AC-7.1:`code-version` / `code-require` / `code-it` / `code-unit` / `code-review` / `code-dashboard` / `code-publish` / `code-auto` **不**被本需求修改
  - AC-7.2:`code-auto` 现行 Q-4 锁定 A "总选推荐项"**不**变
  - AC-7.3:`code-dashboard` / `code-publish` / `code-review` 现有逻辑**不**变

### FR-8:不修改 marketplace 与 plugin 与规范

- **描述**:本需求**不**修改看板 / 规范文件
- **优先级**:必须
- **AC**:
  - AC-8.1:`marketplace.json` / `plugin.json` **不**被本需求修改
  - AC-8.2:`dashboard-conventions.md` **不**被本需求修改
  - AC-8.3:`commit-conventions.md` 规则 1 **不**被本需求填充
  - AC-8.4:中英 README 若需更新,按 `doc-conventions §规则 1` 同次提交中英 — 但本需求**不**主动写 README(由 `code-rule` 沉淀)

### FR-9:报告与建议

- **描述**:`code-design` / `code-plan` 步骤 0b 完成时向用户报告
- **优先级**:必须
- **AC**:
  - AC-9.1:完成后,屏幕输出"已回写至 design/<REQ>/RESULT.md '## 设计目标' 小节"
  - AC-9.2:`code-plan` 沿用 `design` 时,屏幕输出"沿用 design 的设计目标:<摘要>"
  - AC-9.3:`code-plan` 退化时,屏幕输出"未检测到 design/<REQ>/RESULT.md,请回答设计目标"
  - AC-9.4:**不**生成独立报告文件(屏幕输出即全部内容)

---

## 5. 非功能需求 / 约束(NFR)

### NFR-1:零新增依赖
- **描述**:不引入新依赖;复用现有 `Bash` / `Read` / `Edit` / `Write` / `AskUserQuestion` 工具
- **强制级别**:必须

### NFR-2:增量修改 SKILL.md
- **描述**:`code-design/SKILL.md` + `code-plan/SKILL.md` 修改方式为 **Edit 工具追加"步骤 0b"**,不重写稳定章节
- **强制级别**:必须
- **理由**:避免破坏现有 frontmatter / 既有"无设计目标"流程

### NFR-3:幂等性
- **描述**:`code-design` / `code-plan` 多次执行结果**幂等**("设计目标"小节覆盖)
- **强制级别**:必须

### NFR-4:不触发 `dashboard-conventions §规则 1`
- **描述**:本需求**不**修改看板
- **强制级别**:必须
- **理由**:"设计目标"信息写在 `design/.../RESULT.md` 顶部小节,不在看板

### NFR-5:与 `code-auto` 协同 0 冲突
- **描述**:`code-auto` 现行"总选推荐项"**不**变
- **强制级别**:必须
- **理由**:`code-auto` 在 `code-design` / `code-plan` 步骤 0b 触发 `AskUserQuestion` 时仍按既定行为选"推荐项"

### NFR-6:与 REQ-00005 / REQ-00009 / REQ-00010 步骤命名一致
- **描述**:本需求步骤命名为"步骤 0b",与既有"步骤 0a"模式同位
- **强制级别**:必须
- **理由**:保持代码风格统一

### NFR-7:不提供"跳过"参数
- **描述**:本需求**不**提供 `--skip-design-goals` 等强制跳过参数
- **强制级别**:必须
- **理由**:用户已主动调 `code-design` / `code-plan`,期望参与设计目标选择

### NFR-8:性能
- **描述**:`AskUserQuestion` 多次调用(1-5 次)耗时 < 5 分钟(用户感知)
- **强制级别**:必须

---

## 6. 页面与界面(输出形态)

### 6.1 `code-design` 步骤 0b 确认(S-1)

```
=== code-design 设计目标确认 ===

整体设计目标:
  选:更少代码改修(--minimal)

维度优先级:
  功能性:中
  扩展性:低
  健壮性:高
  可维护性:高

已回写至 design/REQ-00010/RESULT.md "## 设计目标" 小节
```

### 6.2 `code-plan` 步骤 0b 沿用 design(S-2)

```
=== code-plan 设计目标确认 ===

沿用 design 的设计目标:
  整体:平衡(--balanced)
  功能性:中
  扩展性:中
  健壮性:中
  可维护性:中

已读取 design/REQ-00010/RESULT.md "## 设计目标" 小节
```

### 6.3 `code-plan` 步骤 0b 退化(S-3)

```
=== code-plan 设计目标确认(无 design 输入) ===

⚠ 未检测到 design/REQ-00010/RESULT.md
请回答设计目标:
  整体设计目标?(--minimal / --extensible / --balanced)

[用户回答]

已回写至 plan/REQ-00010/RESULT.md "## 设计目标" 小节
```

### 6.4 "## 设计目标" 小节结构(回写)

```markdown
## 设计目标

> 本小节由 `code-design` / `code-plan` 步骤 0b 自动生成,记录用户确认的设计目标。

- **回写时间**:<YYYY-MM-DD HH:mm>
- **回写触发**:<code-design / code-plan>

### 整体设计目标
`--minimal` / `--extensible` / `--balanced`(由用户选择)

### 维度优先级

| 维度 | 优先级 |
| --- | --- |
| 功能性 | 高 / 中 / 低 |
| 扩展性 | 高 / 中 / 低 |
| 健壮性 | 高 / 中 / 低 |
| 可维护性 | 高 / 中 / 低 |
```

---

## 7. 交互逻辑

### 7.1 `code-design` 启动流程(改后)

```
[启动]
  ↓
[步骤 0a:git pull] ─────────┐
  ↓ (成功)                  │ (失败 → 沿用 REQ-00005 错误处理)
[步骤 0b:设计目标确认] ────┤
  ↓ (用户回答)             │
  ↓                          │
[回写至 design/.../RESULT.md 顶部"## 设计目标" 小节] │
  ↓                          │
[步骤 0:版本上下文检测]    │
  ↓                          │
[步骤 1-?:原有设计流程]    │
  ↓                          │
[末尾兜底提交]              │
  ↓                          │
[退出]                       │
```

### 7.2 `code-plan` 启动流程(改后)

```
[启动]
  ↓
[步骤 0a:git pull] ─────────┐
  ↓ (成功)                  │
[步骤 0b:设计目标确认] ────┤
  ↓                          │
[读 design/.../RESULT.md]  │
  ↓                          │
[存在"## 设计目标"?]       │
  ├─ 是 → [沿用] → [屏幕打印"沿用 design 的设计目标"] → [进入原流程]
  └─ 否 → [退化:AskUserQuestion 1 问] → [回写至 plan/.../RESULT.md] → [进入原流程]
  ↓
[步骤 0:版本上下文检测]
  ↓
[步骤 1-?:原有计划流程]
  ↓
[末尾兜底提交]
  ↓
[退出]
```

### 7.3 任务拆分粒度调整(FR-4)

```
[读"## 设计目标" 小节]
  ↓
[提取整体设计目标 + 扩展性优先级]
  ↓
[判定]
  ├─ 整体 = "--extensible" 或 扩展性 = "高" → [加"扩展架构设计" / "设计模式使用" 等任务]
  ├─ 整体 = "--minimal" → [同类任务合并,粒度粗化]
  └─ 整体 = "--balanced" + 扩展性 ∈ {中, 低} → [默认粒度,无调整]
  ↓
[写 plan/.../PLAN.md 任务总览]
```

---

## 8. 数据与状态

### 8.1 "## 设计目标" 小节数据结构

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

### 8.2 "## 设计目标" 小节位置

- `design/REQ-NNNNN/RESULT.md`:顶部(在"文档头"之后,"## 1. 需求概述"之前)
- `plan/REQ-NNNNN/RESULT.md`:顶部(在"文档头"之后,"## 1. 需求概述"之前)

### 8.3 任务粒度调整规则

| 整体设计目标 | 扩展性优先级 | 任务粒度调整 |
| --- | --- | --- |
| `--minimal` | * | 合并同类任务,粒度粗化 |
| `--balanced` | 高/中/低 | 默认粒度 |
| `--extensible` | * | 加"扩展架构设计" / "设计模式使用"等任务(至少 1 个) |
| `--extensible` | 高 | 至少 3 个扩展性相关任务 |

---

## 9. 边界与异常

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | 无 `.current-version` | 提示调 `code-version`,退出 |
| **E-2** | `git pull` 失败(步骤 0a) | 沿用 REQ-00005 错误处理 |
| **E-3** | 用户取消 `AskUserQuestion`(`code-design` 步骤 0b) | 中止,回写空"## 设计目标"小节,后续按"空目标"产出 |
| **E-4** | `code-plan` 读 `design/.../RESULT.md` 不存在 | 退化(FR-3) |
| **E-5** | `code-plan` 读 `design/.../RESULT.md` 存在但**无**"## 设计目标"小节 | 退化(FR-3)— 视为"无 design 输入" |
| **E-6** | `code-plan` 读 `design/.../RESULT.md` 存在 + "## 设计目标"小节 | 沿用(FR-2.AC-2.3) |
| **E-7** | `code-auto` 调 `code-design` / `code-plan` 步骤 0b | `code-auto` 选"推荐项"(REQ-00007 Q-4 锁定 A) |
| **E-8** | 多次执行 `code-design` | "## 设计目标"小节**覆盖**(NFR-3 幂等) |
| **E-9** | 大需求要拆细 | `code-design` 步骤 0b 问 5 个问题(Q-3 锁定) |
| **E-10** | 用户希望"回退"已确认的设计目标 | 手动编辑 `RESULT.md` 的"## 设计目标"小节(不提供 CLI 参数) |

---

## 10. 验收标准(AC 总览)

按 FR 编号归类,合计 ~30 条:

- **FR-1**(5 条):AC-1.1 ~ AC-1.5
- **FR-2**(5 条):AC-2.1 ~ AC-2.5
- **FR-3**(3 条):AC-3.1 / AC-3.2 / AC-3.3
- **FR-4**(4 条):AC-4.1 / AC-4.2 / AC-4.3 / AC-4.4
- **FR-5**(5 条):AC-5.1 ~ AC-5.5
- **FR-6**(5 条):AC-6.1 ~ AC-6.5
- **FR-7**(3 条):AC-7.1 / AC-7.2 / AC-7.3
- **FR-8**(4 条):AC-8.1 ~ AC-8.4
- **FR-9**(4 条):AC-9.1 ~ AC-9.4

**总计**:约 30 条 AC。

---

## 11. 关联需求

| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| **REQ-00007**(V0.0.2) | `code-auto` 调 `code-design` / `code-plan` | NFR-5:`code-auto` 选"推荐项" | `./assistants/V0.0.2/require/REQ-00007/RESULT.md` §FR-3 / §NFR-4 |
| **REQ-00005**(V0.0.2) | "首步拉取"位置 = 步骤 0a | NFR-6:本需求"步骤 0b"叠加在 REQ-00005 之上 | `./assistants/V0.0.2/require/REQ-00005/RESULT.md` §FR-1 |
| **REQ-00009**(V0.0.2) | `code-unit` 守卫 = "步骤 0a"模式 | NFR-6:与本需求"步骤 0b"模式协同 | `./assistants/V0.0.2/require/REQ-00009/RESULT.md` §FR-1 |
| **REQ-00010**(V0.0.2) | `code-it` 守卫 = "步骤 0a"模式 | NFR-6:与本需求"步骤 0b"模式协同 | `./assistants/V0.0.2/require/REQ-00010/RESULT.md` §FR-1 |
| **REQ-00004**(V0.0.2) | `code-dashboard` 现有统计逻辑 | NFR-4:不修改看板 | `./assistants/V0.0.2/require/REQ-00004/RESULT.md` §NFR-5 |
| **REQ-00006**(V0.0.2) | `code-publish` 前置检查 | 不影响 | `./assistants/V0.0.2/require/REQ-00006/RESULT.md` §FR-1 |
| **REQ-00008**(V0.0.2) | `code-review` 整版本模式 | 不影响 | `./assistants/V0.0.2/require/REQ-00008/RESULT.md` |
| **REQ-00003**(V0.0.1) | `code-rule` 维护项目级规范 | 本需求**不**直接写规范 | `./assistants/V0.0.1/require/REQ-00003/RESULT.md` §FR-7 |
| **REQ-00001**(V0.0.1) | `design/.../RESULT.md` / `plan/.../RESULT.md` 模板 | 本需求新增"## 设计目标"小节 | `./assistants/V0.0.1/design/REQ-NNNNN/RESULT.md`(历史样本) |

详细关联分析见 `related-requirements.md`。

---

## 12. 待澄清 / 未决项(本轮未处理 / 留作默认)

### Q-4:与 `code-auto` 的协同
- **状态**:采纳默认(`code-auto` 不升级,本需求守卫作为"双保险")

### Q-5:与 REQ-00005 协同
- **状态**:采纳默认(增量追加"步骤 0b")

### Q-6:`commit-conventions.md` 与 CLAUDE.md 追加
- **状态**:采纳默认(不追加,留作 follow-up)

### Q-7:"设计目标"选项的预设清单
- **状态**:采纳默认(整体 3 选项 + 4 维度各 1 问题)

### Q-8:`code-plan` 读 `design` "设计目标"小节
- **状态**:采纳默认(`code-plan` 步骤 0b 读 + 据此调整任务拆分粒度)

### Q-9(新增):派生任务预警
- **建议派生**:
  - "用 `code-rule` 沉淀 '设计目标' 字段约定"
  - "`code-auto` 升级:识别'设计目标确认'类询问时回传"
- **状态**:本需求不阻塞

---

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-04 14:57 | v1 | 初始创建:9 FR / 8 NFR / ~30 AC / 10 个边界场景;Q-1~Q-3 锁定,Q-4~Q-8 留默认/未采用;用户原文 1 处笔误已纠正(`/code-desgin` → `/code-design`);Q-1 锁定"**都走步骤 0b**"(首步拉取之后、设计产出之前,与 REQ-00005 / REQ-00009 / REQ-00010 的"步骤 0a"模式同位叠加);Q-2 锁定"**回写** `RESULT.md` 顶部'## 设计目标' 小节"且**关键补充**"扩展性高的方法需要拆出'扩展架构设计' / '设计模式使用'等更细致任务步骤"(FR-4 据此设计);Q-3 锁定"**问多个问题**"(设计目标 + 4 维度,可分开提问,大需求场景);NFR-3 幂等;NFR-4 不触发 `dashboard-conventions §规则 1`;NFR-5 与 `code-auto` 协同 0 冲突(`code-auto` 仍按"总选推荐项") | wangmiao |
