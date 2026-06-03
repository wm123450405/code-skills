# 模块拆分 — REQ-00003
版本:V0.0.1

## 模块总览

| 模块 | 路径 | 状态 | 职责 | 涉及文件 |
| --- | --- | --- | --- | --- |
| M-1:类型识别引擎 | `code-rule/SKILL.md` §步骤 4 之前 | 新增 | 识别用户描述的目标类型(Type A/B/C) | SKILL.md |
| M-2:Type A 子流程(扩展) | `code-rule/SKILL.md` §步骤 4-9 | 修改 | 6 类核心规范识别 + 占位模式 + 引导模式 | SKILL.md + 6 个新分类文件 + 1 弃用标记 |
| M-3:Type B 子流程(新增) | `code-rule/SKILL.md` §"Type B 子流程" | 新增 | AI 工作指引追加到 CLAUDE.md | SKILL.md + CLAUDE.md |
| M-4:Type C 子流程(新增) | `code-rule/SKILL.md` §"Type C 子流程" | 新增 | 模板内容提示追加(末尾/内联) | SKILL.md + templates/*.md |
| M-5:占位文件创建 | `assistants/rules/*.md` × 6 | 新增 | 6 个空骨架文件 | 6 个新文件 |
| M-6:迁移与弃用标记 | `assistants/rules/module-conventions.md` | 修改 | 追加 DEPRECATED 标记 | 1 个文件 |
| M-7:CLAUDE.md 新小节 | `plugins/code-skills/CLAUDE.md` | 新增 | 末尾追加"## AI 工作约定"小节(首次) | 1 个文件 |
| M-8:模板扩展 | `code-rule/templates/rule.md` | 修改 | 占位模式 + 引导模式说明 | 1 个文件 |
| M-9:工作目录约定更新 | `code-rule/SKILL.md` §工作目录约定 | 修改 | 11 个新分类文件名 | SKILL.md |

---

## 模块详情

### M-1:类型识别引擎

- **路径**:`plugins/code-skills/skills/code-rule/SKILL.md`(步骤 3 后插入"类型识别"步骤 3.5)
- **状态**:新增(模块化插入)
- **职责**:识别用户描述属于 Type A / B / C 中的哪一类
- **关键设计**:
  - 关键词扫描(见 `design-notes.md` §Q-5)
  - 置信度评估(高/中/低)
  - `AskUserQuestion` 显式追问(中/低置信度时)
- **依赖**:M-2 / M-3 / M-4(根据识别结果路由)
- **符合的规范**:NFR-2 可扩展性(未来新增 Type D 只需扩展关键词表)

### M-2:Type A 子流程(扩展)

- **路径**:`plugins/code-skills/skills/code-rule/SKILL.md`(步骤 4-9 整体)
- **状态**:修改(扩展,不重写)
- **职责**:
  1. 6 类核心规范识别(C-1 ~ C-6)+ 4 个保留专项
  2. 条件性分类的"占位"模式(C-1/C-2/C-6)
  3. 默认分类的"引导"模式(C-3/C-4/C-5)
- **关键决策**(详见 `design-notes.md`):
  - 步骤 4 关键词表更新(从 11 个旧 → 6 核心 + 5 专项)
  - 步骤 4 后插入"分类确认"细分(条件性 → 追问"现在需要/未来占位/跳过")
  - 步骤 5 澄清字段不变(向后兼容)
  - 步骤 7 写文件增加"占位模式"分支
- **涉及文件**:`SKILL.md` + 6 个新分类文件 + 1 弃用标记
- **依赖**:M-1(类型识别结果)
- **符合的规范**:FR-8(现有流程不变)+ NFR-1(向后兼容)

### M-3:Type B 子流程(新增)

- **路径**:`plugins/code-skills/skills/code-rule/SKILL.md`(新插入"Type B 子流程"小节)
- **状态**:新增
- **职责**:把 AI 工作指引追加到 CLAUDE.md 末尾"## AI 工作约定"小节
- **关键算法**:
  1. 检测 CLAUDE.md 是否含"## AI 工作约定(由 code-rule 维护)"小节
  2. 不存在 → `Edit` 在文件末尾追加小节标题 + 1 个空"### 指引 1: (待添加)"占位
  3. 存在 → 在该小节末尾追加新"指引 N"小节
  4. **绝不**修改 CLAUDE.md 其它任何小节
- **Type B 数据结构**(5 字段):
  - 指引简称(`### 指引 N: <指引简称>`)
  - 描述(一段)
  - 适用场景(一句话)
  - 期望行为(可含"读哪个文件/调哪个技能/避免什么")
  - 来源(用户原始描述 + 时间戳)
- **依赖**:M-1(类型识别)
- **符合的规范**:FR-5 + FR-10 + INV-3

### M-4:Type C 子流程(新增)

- **路径**:`plugins/code-skills/skills/code-rule/SKILL.md`(新插入"Type C 子流程"小节)
- **状态**:新增
- **职责**:把模板内容提示追加到目标模板(末尾或内联)
- **关键算法**:
  1. 询问用户:插入位置(末尾追加 / 内联)
  2. **末尾追加**:在模板文件末尾追加 `## 提示: <主题>` 二级小节(若不存在则新建"## 提示"作为内容提示区)
  3. **内联**:用户指定目标二级小节(精确匹配 `## N. <小节名>`),在该小节末尾追加 `### 提示: <字段>` 三级小节
  4. **绝不**修改模板其他内容
- **Type C 数据结构**(4 字段):
  - 字段/小节名(末尾:主题;内联:字段名)
  - 必填(是/否)
  - 简明说明(1-2 句话)
  - 错误示例(可选)
- **依赖**:M-1(类型识别)
- **符合的规范**:FR-6 + FR-10 + INV-4

### M-5:占位文件创建(6 个新分类)

- **路径**:`assistants/rules/*.md` × 6
- **状态**:新增
- **涉及文件**:
  - `framework-conventions.md`(C-1,条件性)
  - `dependency-conventions.md`(C-2,条件性)
  - `naming-conventions.md`(C-3,默认)
  - `directory-conventions.md`(C-4,默认)
  - `coding-style.md`(C-5,默认)
  - `commit-conventions.md`(C-6,条件性)
- **内容结构**(基于 `templates/rule.md` 简化):
  ```markdown
  # <分类中文名>规范(<分类英文名>)

  > 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
  > 最后更新:2026-06-03 21:00
  > 适用版本:跨所有版本共享(项目级)

  ## 适用场景
  <本规范文件覆盖什么范围>

  ## 强制级别约定
  本文件中各规则的强制级别逐条标注。

  ---

  ## 规则 1: (待添加)

  <本条规则等待用户在后续调 `code-rule` 时填充。>
  ```
- **符合的规范**:FR-3 + INV-2

### M-6:迁移与弃用标记

- **路径**:`assistants/rules/module-conventions.md`
- **状态**:修改(仅追加标记)
- **变更内容**:
  - 在文件头部添加:
    ```markdown
    > ⚠️ **DEPRECATED(已弃用)**:本文件内容已迁移到 `directory-conventions.md`(2026-06-03 REQ-00003 H2 决策)。本文件保留作为历史参考,新规则请追加到 `directory-conventions.md`。
    ```
  - **不删除**任何现有内容
  - **不修改**任何现有小节
- **符合的规范**:Q-8=H2 + INV-7

### M-7:CLAUDE.md 新小节

- **路径**:`plugins/code-skills/CLAUDE.md`
- **状态**:新增(末尾追加)
- **变更内容**:
  - 在文件末尾追加:
    ```markdown

    ## AI 工作约定(由 code-rule 维护)

    > 本小节由 `code-rule` 技能维护;手动修改可能被 `code-rule` 覆盖。
    > 适用对象:Claude Code 在本仓库工作时

    ### 指引 1: (待添加)
    ```
- **关键决策**:
  - **不修改**任何现有小节(FR-10 边界)
  - **首次创建**该小节时,内容仅含"小节标题 + 1 个空指引占位"
  - 后续 `code-rule` 调用会在该小节内追加"指引 N"
- **符合的规范**:FR-5 + FR-10 + INV-3

### M-8:模板扩展

- **路径**:`plugins/code-skills/skills/code-rule/templates/rule.md`
- **状态**:修改(扩展)
- **变更内容**:
  - 在文件头部添加"占位模式"说明:
    ```markdown
    ## 占位模式(本文件可作为空占位使用)

    若用户选择"未来占位"模式,可省略"规则 1"及之后小节,仅保留:
    - 分类标题
    - "本规范由 code-rule 维护"声明
    - 1 个"## 规则 1: (待添加)"空小节(可选)
    ```
  - 在文件头部添加"引导模式"说明(默认分类首次添加时使用)
- **符合的规范**:FR-3 + FR-4

### M-9:工作目录约定更新

- **路径**:`plugins/code-skills/skills/code-rule/SKILL.md` §工作目录约定
- **状态**:修改
- **变更内容**:
  - L32-44 目录树更新为 11 个新分类文件名:
    ```diff
    - architecture.md
    - module-conventions.md
    - naming.md
    - error-handling.md
    - api-standards.md
    - data-modeling.md
    - security.md
    - performance.md
    - testing.md
    - observability.md
    - git-conventions.md
    + framework-conventions.md      # C-1(本需求新建)
    + dependency-conventions.md    # C-2(本需求新建)
    + naming-conventions.md         # C-3(本需求新建)
    + directory-conventions.md      # C-4(本需求新建,替代 module-conventions)
    + coding-style.md              # C-5(本需求新建)
    + commit-conventions.md        # C-6(本需求新建)
    + dashboard-conventions.md     # 保留
    + doc-conventions.md           # 保留
    + marketplace-protocol.md      # 保留
    + skill-conventions.md         # 保留
    ```
  - `module-conventions.md` **不再列出**(已弃用)
- **符合的规范**:FR-2 + Q-4 + Q-8

---

## 模块依赖图

```
            [M-1: 类型识别引擎]
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
  [M-2: Type A] [M-3: Type B] [M-4: Type C]
       │         │         │
       ├─→ M-5 (6 占位)
       ├─→ M-6 (迁移)
       │         └─→ M-7 (CLAUDE.md 新小节)
       │                   └─→ 模板 *.md
       └─→ M-8 (模板扩展)
       └─→ M-9 (工作目录约定更新)
```

**关键路径**:
- M-1 → M-2/M-3/M-4:类型识别路由
- M-2 → M-5/M-6/M-9:Type A 实施(6 占位 + 1 弃用 + 工作目录约定更新)
- M-3 → M-7:Type B 实施(CLAUDE.md 新小节)
- M-4:Type C 实施(模板 *.md,本设计阶段无具体模板改动,在 code-it 阶段按需追加)
- M-8:模板扩展(支持 M-2 的占位模式)

## 实施顺序(commit 顺序)

| Commit # | 模块 | commit message | 涉及文件数 |
| --- | --- | --- | --- |
| 1 | M-2 + M-1 + M-9 | `feat(code-rule): add 6 new classification categories (REQ-00003 FR-2)` | 1(SKILL.md) |
| 2 | M-5 + M-6 | `feat(rules): add 6 placeholder rule files + deprecate module-conventions (REQ-00003 H2)` | 6 新 + 1 修改 |
| 3 | M-7 | `feat(CLAUDE.md): add "AI 工作约定" section (REQ-00003 FR-5)` | 1 |
| 4 | M-8 | `feat(code-rule): extend templates/rule.md with placeholder/bootstrap modes (REQ-00003 FR-3+FR-4)` | 1 |
| 5 | M-3 + M-4(文档化) | `docs(code-rule): document Type B + Type C sub-flows (REQ-00003 FR-5+FR-6)` | 1(SKILL.md 章节插入) |

> 注:本设计只产生 commit 1-4 的实施(commit 5 在 code-it 阶段由 `code-rule` 自身运行时触发,本技能不预先写 Type B/C 文档)
