# 概要设计 — REQ-00003(优化 `code-rule` 技能,增加不同类型的核心编码规范的解析或引导)

- 需求编码:REQ-00003
- 所属版本:V0.0.1
- 概要设计版本:v1
- 状态:已完成(首次)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-03 21:00
- **上游**:`./assistants/V0.0.1/require/REQ-00003/RESULT.md`(v1,已锁定)
- **下游**:`code-plan REQ-00003` 拆分任务 / `code-it REQ-00003-NN` 实施
- **遵循规范**:`./assistants/rules/` 下 5 个文件 + 5 个新分类文件将由本设计创建

---

## 1. 概述

### 1.1 目标

把 `code-rule` 技能从"只支持项目级规则(Type A)"扩展为"支持 3 种目标类型":
- **Type A:项目级规范条款** → 写入 `./assistants/rules/<分类>.md`
- **Type B:AI 工作指引** → 写入 `plugins/code-skills/CLAUDE.md` 的"## AI 工作约定"小节
- **Type C:模板内容提示** → 写入 `plugins/code-skills/skills/<技能>/templates/*.md` 末尾或内联

Type A 在原有 5 个文件基础上**扩展 6 类核心规范**(3 个默认 + 3 个条件性),并完成 1 个文件迁移(`module-conventions.md` → `directory-conventions.md`)。

### 1.2 范围

**修改对象**:
- `plugins/code-skills/skills/code-rule/SKILL.md`(扩展正文,不改 frontmatter)
- `plugins/code-skills/skills/code-rule/templates/rule.md`(扩展,加占位/引导模式说明)
- `assistants/rules/module-conventions.md`(追加 DEPRECATED 标记)

**新增对象**(共 7 个文件):
- `assistants/rules/framework-conventions.md`(C-1,空占位)
- `assistants/rules/dependency-conventions.md`(C-2,空占位)
- `assistants/rules/naming-conventions.md`(C-3,空占位)
- `assistants/rules/directory-conventions.md`(C-4,空占位 + 承载原 module-conventions 内容)
- `assistants/rules/coding-style.md`(C-5,空占位)
- `assistants/rules/commit-conventions.md`(C-6,空占位)
- `plugins/code-skills/CLAUDE.md` 末尾新增"## AI 工作约定(由 code-rule 维护)"小节(首次)

**零变更对象**(4 保留):
- `assistants/rules/dashboard-conventions.md`
- `assistants/rules/doc-conventions.md`
- `assistants/rules/marketplace-protocol.md`
- `assistants/rules/skill-conventions.md`

**严禁修改**(FR-9 边界):
- `.claude-plugin/marketplace.json`
- `plugins/code-skills/.claude-plugin/plugin.json`
- 其他 9 个 `code-*` 技能的 SKILL.md(包括 frontmatter)
- `plugins/code-skills/README.md` / `README.en.md`
- `assistants/V0.0.0/` / `assistants/V0.0.1/` 下的任何工作文件

### 1.3 与需求的关系

| 需求 FR | 本设计章节 | 关系 |
| --- | --- | --- |
| FR-1(3 种目标类型) | §3 核心架构 | **核心** — 本设计主线 |
| FR-2(6 类核心规范) | §3.2 Type A 模块 | **核心** — 分类识别 |
| FR-3(条件性占位) | §3.2.2 占位流程 | **核心** |
| FR-4(默认引导) | §3.2.3 引导流程 | **核心** |
| FR-5(Type B 结构) | §3.3 Type B 模块 | **核心** |
| FR-6(Type C 双位置) | §3.4 Type C 模块 | **核心** |
| FR-7(类型识别) | §3.5 类型识别引擎 | **核心** |
| FR-8(Type A 不变) | §3.2.1 现有流程继承 | **约束** — 向后兼容 |
| FR-9(不得修改) | §5 不变量 INV-5 | **约束** — 硬边界 |
| FR-10(不重写) | §5 不变量 INV-3 / INV-4 | **约束** — 硬边界 |

## 2. 上游引用

- 需求分析:`./assistants/V0.0.1/require/REQ-00003/RESULT.md`(v1,已锁定)
- 需求相关材料:
  - `require/REQ-00003/analysis-notes.md`
  - `require/REQ-00003/materials-index.md`
  - `require/REQ-00003/related-requirements.md`
  - `require/REQ-00003/clarifications.md`
- 项目级规范:`./assistants/rules/` 下 5 个文件(Glob 命中)

## 3. 核心架构:单技能 + 3 子流程

### 3.1 架构概览

```
[用户调用 code-rule + 描述]
        │
        ▼
[类型识别引擎(新增步骤 3.5)]
   ├─→ 关键词命中 + 置信度高 ─→ 直接进入对应类型子流程
   └─→ 关键词模糊 / 多类型 ─→ AskUserQuestion 询问
        │
        ├────────────────┬────────────────┐
        ▼                ▼                ▼
[Type A 子流程]   [Type B 子流程]   [Type C 子流程]
   现有 9 步骤       新增 5 步骤       新增 5 步骤
   流程不变(FR-8)   末尾追加(FR-5)   末尾/内联(FR-6)
        │                │                │
        ▼                ▼                ▼
[./assistants/rules/] [CLAUDE.md]   [templates/*.md]
```

**关键设计决策**(详见 `design-notes.md`):
- **D-1**:单技能 + 3 子流程(非 3 技能) — 保持单一入口,FR-8 兼容
- **D-2**:类型识别作为**独立子流程**(在现有 9 步骤之前插入)
- **D-3**:Type A 现有 9 步骤流程**完全保持**(关键词表除外)
- **D-4**:Type B / Type C 各自独立子流程,但文档上**与 Type A 同级**列在 `code-rule/SKILL.md`

### 3.2 Type A 子流程(扩展)

#### 3.2.1 现有流程继承(FR-8 约束)

Type A 现有 9 步骤工作流(`code-rule/SKILL.md` L83-224):
- 步骤 0:不需要版本上下文
- 步骤 1:探查 `./assistants/` 现状
- 步骤 2:兜底创建目录
- 步骤 3:收集规范描述
- 步骤 4:拆分 + 初步归类
- 步骤 5:澄清规则细节
- 步骤 6:探测目标文件现状
- 步骤 7:写文件
- 步骤 8:汇报
- 步骤 9:多规则与迭代

**本需求变更**:
- 步骤 4 关键词表**扩展**(从 11 个旧 → 6 核心 + 5 保留专项,见 `design-notes.md` §候选分类关键词表)
- 步骤 4 后增加"条件性分类追问"分支
- 步骤 7 写文件增加"占位模式"分支
- **其余步骤字段不变**(NFR-1 向后兼容)

#### 3.2.2 占位模式(FR-3,条件性分类)

**触发条件**:
- 用户描述命中 C-1 / C-2 / C-6(条件性分类)
- 用户选择"未来占位"

**算法**:
1. 检测目标分类文件是否存在
2. **不存在** + 用户选"未来占位" → 走占位模式:
   - `Write` 创建文件,内容仅含:
     - 分类标题(中文 + 英文)
     - "本规范文件由 `code-rule` 技能维护"
     - "## 适用场景" 占位
     - "## 强制级别约定" 说明
     - "## 规则 1: (待添加)" 占位
3. **存在** → 走现有追加流程(不变)

**用户选择分支**:
- "现在需要" → 走 FR-4 引导模式
- "未来占位" → 走 FR-3 占位模式
- "跳过" → 不创建任何文件

**不变量**:
- INV-2:6 个新分类文件**仅含最小骨架**,无预填规则

#### 3.2.3 引导模式(FR-4,默认分类)

**触发条件**:
- 用户描述命中 C-3 / C-4 / C-5(默认分类)
- 用户**首次添加**该类规则(目标文件不存在)

**算法**:
1. 检测目标分类文件是否存在
2. **不存在** → 走引导模式:
   - 提示用户"是否同时补 1-2 条示例规则"
   - 用户同意 → 走"新建"流程 + 用户提供 1-2 条示例
   - 用户跳过 → 走"占位模式"创建空骨架
3. **存在** → 走现有追加流程(不变)

**用户选择分支**:
- "补 1-2 条示例" → 走标准流程(澄清字段 + 写文件)
- "暂不补" → 走占位模式(FR-3)

**不变量**:
- INV-2:即使引导模式,用户**未提供示例**时仍走占位模式

#### 3.2.4 分类映射表

| 需求分类 | 文件名 | 关键词 | 条件性 | 与现有关系 |
| --- | --- | --- | --- | --- |
| C-1 框架规范 | `framework-conventions.md` | 框架 / 架构 / 框架选型 / framework | 条件性 | **新建**(空占位) |
| C-2 三方依赖规范 | `dependency-conventions.md` | 依赖 / 第三方 / 库 / 包 / dependency | 条件性 | **新建**(空占位) |
| C-3 语言与命名规范 | `naming-conventions.md` | 命名 / camelCase / snake_case / naming | 默认 | **新建**(空占位) |
| C-4 目录与模块规范 | `directory-conventions.md` | 目录 / 模块 / 包结构 / directory | 默认 | **新建**(空占位 + 承载 module-conventions 内容) |
| C-5 代码书写规范 | `coding-style.md` | 代码风格 / 注释 / 错误处理 / coding-style | 默认 | **新建**(空占位) |
| C-6 提交与合并规范 | `commit-conventions.md` | 提交 / commit / 合并 / merge | 条件性 | **新建**(空占位) |
| 保留:看板 | `dashboard-conventions.md` | 看板 / 仪表盘 / dashboard | — | **保留** |
| 保留:文档 | `doc-conventions.md` | README / 中英 / doc | — | **保留** |
| 保留:marketplace | `marketplace-protocol.md` | marketplace / plugin | — | **保留** |
| 保留:技能 | `skill-conventions.md` | SKILL.md / frontmatter | — | **保留** |
| 弃用:模块 | `module-conventions.md` | — | — | **弃用**(追加 DEPRECATED 标记) |

### 3.3 Type B 子流程(新增)

#### 3.3.1 触发与识别

- 用户描述含以下关键词之一:
  - `CLAUDE.md` / `AI 工作` / `AI 约定` / `AI 写` / `AI 读` / `AI 应` / `AI 协作者`
- 关键词命中 + 高置信度 → 直接进入 Type B 子流程
- 用户可显式覆盖:`"对 CLAUDE.md 增加 X"`

#### 3.3.2 Type B 数据结构(5 字段)

```markdown
### 指引 N:<指引简称>

#### 描述
<一句话或一段说明该指引做什么>

#### 适用场景
<什么情况下 AI 应遵守>

#### 期望行为
<AI 应如何行动,可含"读哪个文件/调哪个技能/避免什么">

#### 来源
- 用户原始描述:"<用户最初说的话>"
- 添加时间:YYYY-MM-DD HH:mm
```

**字段决策**(基于 Q-6):不加"正面示例"/"反面示例"字段(由本设计默认)

#### 3.3.3 插入位置与算法

- **目标文件**:`plugins/code-skills/CLAUDE.md`
- **目标小节**:`## AI 工作约定(由 code-rule 维护)`(若不存在则首次创建)
- **插入位置**:目标小节末尾追加(若小节不存在 → 在文件末尾追加小节 + 1 个空"指引 1"占位)

**算法**:
1. `Read plugins/code-skills/CLAUDE.md` 全文
2. `Grep "## AI 工作约定(由 code-rule 维护)"` 检测小节是否存在
3. **不存在** → 在文件末尾追加:
   ```
   <空行确保分隔>
   ## AI 工作约定(由 code-rule 维护)

   > 本小节由 `code-rule` 技能维护;手动修改可能被 `code-rule` 覆盖。
   > 适用对象:Claude Code 在本仓库工作时

   ### 指引 1: (待添加)
   ```
4. **存在** → 在该小节末尾追加新的"指引 N"小节(N = 现有编号 + 1)
5. **绝不**修改 CLAUDE.md 其它任何小节

**不变量**:
- INV-3:仅追加,不改 / 不删

### 3.4 Type C 子流程(新增)

#### 3.4.1 触发与识别

- 用户描述含以下关键词之一:
  - `模板` / `template` / `templates/` / 具体模板文件名(如 `plan.md` / `requirements.md`)
- 关键词命中 + 高置信度 → 直接进入 Type C 子流程
- 用户可显式覆盖:`"对 templates/plan.md 增加 X"`

#### 3.4.2 Type C 数据结构(4 字段)

**末尾追加模式**(`## 提示: <主题>`):
```markdown
## 提示: <主题>

- **字段**:<主题>
- **必填**:是 / 否
- **简明说明**:<1-2 句话>
- **错误示例**(可选):<错误填法>
```

**内联模式**(`### 提示: <字段>` 或 `#### 提示: <字段>`):
```markdown
### 提示: <字段>

- **字段**:<字段>
- **必填**:是 / 否
- **简明说明**:<1-2 句话>
```

**字段决策**(基于 Q-7):末尾用 `## 提示:` 二级 / 内联用 `### 提示:` 三级,两者并存

#### 3.4.3 插入位置与算法

**模式选择**:
1. `AskUserQuestion` 询问:末尾追加 / 内联
2. **末尾追加**:
   - 检测模板文件末尾是否含 `## 提示` 二级小节
   - **不存在** → 在模板文件末尾追加小节标题 + 1 个空"提示 1"占位
   - **存在** → 在该小节末尾追加新"提示 N"小节
3. **内联**:
   - 用户指定目标二级小节(精确匹配 `## N. <小节名>`)
   - **指定** → 在该小节末尾追加 `### 提示: <字段>` 三级小节
   - **未指定** → 追问用户(不自动推断,避免误插)

**不变量**:
- INV-4:仅追加,不改 / 不删

### 3.5 类型识别引擎(FR-7)

#### 3.5.1 关键词扫描

| 类型 | 关键词 |
| --- | --- |
| Type A | `规则` / `规范` / `约定` / `命名` / `提交` / `代码风格` / `依赖` / `框架` / `目录` / `模块` / `package` / `architecture` / `naming` / `commit` / `dependency` |
| Type B | `CLAUDE.md` / `AI 工作` / `AI 约定` / `AI 写` / `AI 读` / `AI 应` / `AI 协作者` |
| Type C | `模板` / `template` / `templates/` / 具体模板文件名(如 `plan.md` / `requirements.md`) |

#### 3.5.2 置信度评估

| 命中情况 | 置信度 | 处理 |
| --- | --- | --- |
| 1 个类型 + 1+ 关键词 + 目标文件明确 | **高** | 跳过追问,直接进入子流程 |
| 1 个类型 + 0 关键词 + 语义提示模糊 | **中** | `AskUserQuestion` 确认 |
| 多类型 / 0 类型 / 0 关键词 | **低** | `AskUserQuestion` 列出候选 |

#### 3.5.3 显式覆盖

用户可用 `"对 X 文件加 Y"` 形式显式指定:
- `X = CLAUDE.md` → Type B
- `X = templates/<file>` → Type C
- `X = <其他>` → Type A + 按 X 推断分类

## 4. 数据结构(本设计范围内)

### 4.1 规则条目(已有,不变)

- 路径:`./assistants/rules/<分类>.md`
- 字段(8 个):分类 / 规则简称 / 强制级别 / 适用范围 / 条款 / 正面示例 / 反面示例 / 例外 / 关联规范 / 来源
- 来源:`code-rule/templates/rule.md` 模板
- **本需求变更**:模板头部追加"占位模式" + "引导模式"说明(不修改 8 字段结构)

### 4.2 指引条目(新增)

- 路径:`plugins/code-skills/CLAUDE.md` §"AI 工作约定"
- 字段(5 个):指引简称 / 描述 / 适用场景 / 期望行为 / 来源
- 模板:见 §3.3.2

### 4.3 提示条目(新增)

- 路径:`plugins/code-skills/skills/<技能>/templates/<name>.md`
- 字段(4 个,末尾模式;3 个,内联模式):字段/小节名 / 必填 / 简明说明 / 错误示例(末尾可选)
- 模板:见 §3.4.2

## 5. 不变量(本设计 9 条)

| # | 不变量 | 验证手段 |
| --- | --- | --- |
| INV-1 | 现有 Type A 9 步骤流程字段(关键词表除外)完全不变 | `git diff code-rule/SKILL.md` 仅关键词表扩展,无流程字段变更 |
| INV-2 | 6 个新分类文件仅含最小骨架 | `Grep "规则 1" 新建文件` 命中"## 规则 1: (待添加)"占位 |
| INV-3 | Type B 仅追加到 CLAUDE.md 末尾的"AI 工作约定"小节 | `git diff CLAUDE.md` 仅显示"+"行,无"-"行 |
| INV-4 | Type C 仅追加到模板末尾或内联 | `git diff templates/*.md` 仅显示"+"行 |
| INV-5 | 不得修改 `marketplace.json` / `plugin.json` / 其他 9 个 SKILL.md frontmatter / `CLAUDE.md` 其他小节 | `git status` 仅显示预期文件 |
| INV-6 | 4 个保留文件 0 变更 | `git diff dashboard-conventions.md doc-conventions.md marketplace-protocol.md skill-conventions.md` clean |
| INV-7 | `module-conventions.md` 仅追加 DEPRECATED 标记 | `git diff module-conventions.md` 仅显示 DEPRECATED 段 |
| INV-8 | `code-rule/SKILL.md` 步骤 0 工作目录约定更新为 11 个新分类列表 | `Read SKILL.md §工作目录约定` 验证 |
| INV-9 | 5 个 commit 顺序:SKILL.md → 6 占位 + 1 弃用 → CLAUDE.md → 模板扩展 → SKILL.md 工作目录约定 | `git log --oneline -5` |

## 6. 测试要点(本设计专属)

| # | 测试 | 验证内容 | 通过条件 |
| --- | --- | --- | --- |
| T-1 | Type A 现有流程回归 | 旧 `code-rule` 调用("函数命名用 camelCase")仍归类到命名相关 | ✅ 流程与 v0 一致 |
| T-2 | Type A 6 分类识别 | 6 描述各命中 6 类 | ✅ 6 规则落到 6 文件 |
| T-3 | Type A 条件性追问 | 描述触发"现在需要/未来占位/跳过" | ✅ 3 选项呈现 |
| T-4 | Type A 占位模式 | 选"未来占位" → 创建空骨架 | ✅ 文件仅含分类标题 + 占位 |
| T-5 | Type B 末尾追加 | 触发 Type B → CLAUDE.md 末尾新增"AI 工作约定" | ✅ 纯追加,无删除 |
| T-6 | Type C 末尾追加 | 触发 Type C + 末尾 → 模板末尾新增"## 提示" | ✅ 纯追加 |
| T-7 | Type C 内联 | 触发 Type C + 内联 + 指定小节 | ✅ 精确插入 |
| T-8 | 类型识别 | 3 类典型 + 1 类模糊 | ✅ 高置信度自动,低置信度追问 |
| T-9 | 边界 | 跑完整流程,`git status` 仅显示预期文件 | ✅ 不触及 marketplace.json / plugin.json / 其他 SKILL.md |

**自动化测试**:本需求无编程逻辑,上述测试均为**手工** + `git diff` 验证

## 7. 实施计划(概要)

| Commit | 范围 | commit message | 文件数 |
| --- | --- | --- | --- |
| 1 | M-2 + M-1 + M-9 | `feat(code-rule): add 6 new classification categories (REQ-00003 FR-2)` | 1 |
| 2 | M-5 + M-6 | `feat(rules): add 6 placeholder rule files + deprecate module-conventions (REQ-00003 H2)` | 6 新 + 1 修改 |
| 3 | M-7 | `feat(CLAUDE.md): add "AI 工作约定" section (REQ-00003 FR-5)` | 1 |
| 4 | M-8 | `feat(code-rule): extend templates/rule.md with placeholder/bootstrap modes (REQ-00003 FR-3+FR-4)` | 1 |

**后续**(`code-plan` 阶段):基于本设计拆分更细的 `code-it` 任务

## 8. 规范遵循

详见 `rule-compliance.md`。本设计:
- 严格遵循 FR-9 不得修改边界(marketplace.json / plugin.json / 9 SKILL.md / CLAUDE.md 其他小节 / 工作文件)
- 严格遵循 FR-10 Type B/C 不重写既有内容
- 严格遵循 NFR-1 Type A 向后兼容(关键词表扩展但流程不变)
- 创新:本设计**不引入**任何第三方依赖(NFR-4 最小化)
- 创新:本设计**不创建**任何"自动化测试代码"(本需求是技能扩展,无运行时)

## 9. 待澄清 / 未决项

**无遗留**。所有 REQU 待澄清(Q-1 ~ Q-8)已确认或采纳默认;design 阶段 5 项澄清已与用户确认(Q-4/Q-5/Q-8)或采纳默认(Q-6/Q-7)。

## 10. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-03 21:00 | v1 | 设计新增 | 完成首次概要设计:核心架构(单技能 + 3 子流程);9 个模块(M-1 ~ M-9);Type A 6 分类 + 4 保留 + 1 弃用(H2 决策);Type B/C 数据结构(5/4 字段);9 条不变量;5 commit 实施计划;Q-4/Q-5/Q-8 与用户确认,Q-6/Q-7 采纳默认;无遗留待澄清;无新增依赖 | wangmiao |
