# 接口详细规格 — REQ-00003

更新时间:2026-06-04 09:15
版本:V0.0.1

> 本需求**无外部编程接口**(`code-rule` 是 Markdown 文件处理技能,无运行时 API)。但本文件记录"内部接口"—— `code-rule` 与其消费方(`code-design` / `code-plan` / `code-it` / `code-unit` / `code-review`)的契约。

## 接口:`./assistants/rules/<分类>.md` 规范文件(Type A)

- **形式**:Markdown 文件
- **路径**:`./assistants/rules/<分类>.md`
- **分类列表**(实施后 11 个):
  | 分类 | 文件 | 状态 | 默认/条件性 |
  | --- | --- | --- | --- |
  | C-1 框架 | `framework-conventions.md` | 新建(本需求) | 条件性 |
  | C-2 三方依赖 | `dependency-conventions.md` | 新建(本需求) | 条件性 |
  | C-3 语言与命名 | `naming-conventions.md` | 新建(本需求) | 默认 |
  | C-4 目录与模块 | `directory-conventions.md` | 新建(本需求) | 默认 |
  | C-5 代码书写 | `coding-style.md` | 新建(本需求) | 默认 |
  | C-6 提交与合并 | `commit-conventions.md` | 新建(本需求) | 条件性 |
  | (保留)看板 | `dashboard-conventions.md` | 保留 | — |
  | (保留)文档 | `doc-conventions.md` | 保留 | — |
  | (保留)marketplace | `marketplace-protocol.md` | 保留 | — |
  | (保留)技能 | `skill-conventions.md` | 保留 | — |
  | (弃用)模块 | `module-conventions.md` | 弃用(追加 DEPRECATED 标记) | — |
- **入参**:无(文件被消费方直接 `Read`)
- **出参**:文件内容(被 `code-*` 技能读取)
- **字段约定**(基于 `code-rule/templates/rule.md`):
  - 占位模式(本需求新增):仅含"分类标题 + 维护声明 + 1 个 ## 规则 1: (待添加) 占位"
  - 正常模式:8 字段规则小节(分类/规则简称/强制级别/适用范围/条款/正反示例/例外/关联规范/来源)
- **消费方契约**:
  - `code-design` / `code-plan` / `code-it` / `code-unit` / `code-review` 在执行时 `Glob "./assistants/rules/**/*"` 列出所有规范
  - 读取后视为**只读**的强约束输入
  - 任何修改必须通过 `code-rule` 技能,不可直接编辑
- **错误处理**:
  - 文件不存在 → 消费方视为"该分类暂无规范"(不影响执行)
  - 文件格式损坏 → 消费方应跳过该文件,记录警告
- **版本策略**:跨所有版本共享(`适用版本:跨所有版本共享(项目级)`)
- **依据规范**:`./assistants/rules/skill-conventions.md` §规则 1(SKILL.md 引用规范的格式)+ `module-conventions.md`(技能资源摆放)

## 接口:`plugins/code-skills/CLAUDE.md` 末尾"## AI 工作约定"小节(Type B)

- **形式**:Markdown 文件内的小节
- **路径**:`plugins/code-skills/CLAUDE.md` §`## AI 工作约定(由 code-rule 维护)`
- **入参**:`code-rule` 收到 Type B 类型的用户描述
- **出参**:小节末尾追加 1 个"### 指引 N: <指引简称>"小节
- **字段约定**(5 字段,继承 design §3.3.2):
  - 指引简称(`### 指引 N: <指引简称>`)
  - 描述(#### 描述 标题,1-2 段)
  - 适用场景(#### 适用场景 标题,1 段)
  - 期望行为(#### 期望行为 标题,1 段)
  - 来源(#### 来源 标题,2 行:用户原始描述 + 添加时间戳)
- **示例**:
  ```markdown
  ### 指引 1: AI 写 RESULT.md 时必须先读 requirements 模板

  #### 描述
  AI 在使用 `code-require` / `code-design` / `code-plan` 等技能产出 RESULT.md 时,应先 Read 对应的 `requirements.md` / `plan.md` 模板,理解必填字段后再撰写。

  #### 适用场景
  AI 在 `code-require` / `code-design` / `code-plan` 阶段,被要求产出 RESULT.md 时。

  #### 期望行为
  - 先 `Read` `plugins/code-skills/skills/<技能>/templates/<name>.md` 模板
  - 再 `Read` 上游 RESULT.md(如已有),理解上下文
  - 最后按模板的字段顺序撰写

  #### 来源
  - 用户原始描述:"对 CLAUDE.md 增加:AI 写 RESULT.md 时必须先读 requirements 模板"
  - 添加时间:2026-06-04
  ```
- **消费方契约**:
  - Claude Code 在本仓库工作时,会 `Read` CLAUDE.md 全文
  - "AI 工作约定"小节内的指引是**行为指令**,AI 应遵守
- **错误处理**:
  - 小节不存在 → 首次创建时追加"小节标题 + 1 个空指引占位"
  - 已有 N 个指引 → 新指引编号 = N + 1
- **版本策略**:跨所有版本共享(CLAUDE.md 是仓库级文件)
- **兼容策略**:**仅追加**,不修改任何其他小节(INV-3)
- **依据规范**:`skill-conventions.md` §规则 1(本规则不约束 CLAUDE.md 字段,但约束其引用规范的方式)

## 接口:`plugins/code-skills/skills/<技能>/templates/<name>.md` 末尾"## 提示"小节或内联"### 提示"小节(Type C)

- **形式**:Markdown 文件内的小节(末尾或内联)
- **路径**:`plugins/code-skills/skills/<技能>/templates/<name>.md`
- **入参**:`code-rule` 收到 Type C 类型的用户描述
- **出参**:
  - **末尾模式**:模板文件末尾追加 `## 提示: <主题>` 二级小节
  - **内联模式**:目标二级小节末尾追加 `### 提示: <字段>` 三级小节
- **字段约定**(4 字段末尾 / 3 字段内联,继承 design §3.4.2):
  - 末尾模式:字段(主题)/必填/简明说明/错误示例(可选)
  - 内联模式:字段(字段名)/必填/简明说明
- **示例(末尾模式)**:
  ```markdown
  ## 提示: 任务依赖图

  - **字段**:任务依赖图
  - **必填**:是
  - **简明说明**:用 Mermaid `graph` 语法绘制任务依赖关系,节点用任务编号,箭头表示"前置"关系
  - **错误示例**:纯文本列表 / 仅画无节点 / 节点不含任务编号
  ```
- **示例(内联模式)**:
  ```markdown
  ### 提示: 依据规范

  - **字段**:依据规范
  - **必填**:是
  - **简明说明**:每条详细设计点必须标注"依据规范 §X",其中 X 是规范文件的规则编号
  ```
- **消费方契约**:
  - 消费模板的技能(`code-require` / `code-design` / `code-plan`)在执行时,`Read` 模板文件
  - "提示"小节作为**AI 撰写指引**,AI 应遵守
- **错误处理**:
  - 末尾模式:小节不存在 → 首次创建时追加"小节标题 + 1 个空提示占位"
  - 内联模式:目标小节不存在 → 追问用户(不自动推断,避免误插)
- **版本策略**:跨所有版本共享
- **兼容策略**:**仅追加**,不修改任何其他内容(INV-4)
- **依据规范**:`module-conventions.md` §规则 1(技能资源摆放在 `templates/` 子目录)

---

## 接口变更影响分析

| 接口 | 变更 | 影响范围 | 缓解措施 |
| --- | --- | --- | --- |
| 规范文件清单 | 5 → 11(6 新建 + 1 弃用) | 所有 `code-*` 技能 | `Glob` 动态列出,新增自动纳入 |
| `code-rule` 关键词表 | 11 旧 → 6 核心 + 5 专项 | `code-rule` 自身 | 保留旧关键词向后兼容(design D-DESIGN-1) |
| CLAUDE.md 末尾小节 | 0 → 1(新增"AI 工作约定") | Claude Code 自身行为 | 首次创建时为空,仅占位 |
| 模板末尾"提示"小节 | 0 → 0(本 plan 阶段不修改任何模板,仅扩展 templates/rule.md 支持该结构) | 消费模板的技能 | 本 plan 阶段无变更,后续 code-it 阶段按需追加 |
