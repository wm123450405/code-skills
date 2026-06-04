# 开发日志 — TASK-REQ-00006-00004

开始时间:2026-06-04 17:50
版本:V0.0.2
任务标题:`[新增] 写 templates/Q&A.md 模板(占位章节 + 提示)`
触发/来源:需求新增

## 项目现状(步骤 6 记录)

- **项目类型**:Claude Code Marketplace 插件(`code-skills`),纯文档型
- **既有 `code-publish/templates/`**(由 T-002 / T-003 已就绪):
  - `DEPLOY.md` 245 行
  - `UPDATE.md` 365 行
  - `Q&A.md` 即将创建(本任务)
- **DEPLOY.md / UPDATE.md 的共同风格**(本任务参照):
  - H1 用 `<本版本号>` 作自动替换位
  - 文首 `> ⚠` 警示段
  - 章节独立可执行
  - 每章节含 placeholder + 默认示例

## 项目级规范要点(步骤 4 记录)

- `./assistants/rules/module-conventions.md` §规则 1:**强约束**
  - 路径必须在 `plugins/code-skills/skills/code-publish/templates/`
  - kebab-case `<用途>.md`
- 其他 12 个规范文件:占位或不相关

## 任务设计要点(步骤 5 记录)

### PLAN.md §3 任务详情(T-004 摘要)

- **类型**:新增
- **触发/来源**:需求新增
- **目标**:创建 Q&A.md 手册的"占位 + 聚合就绪"模板
- **涉及文件**:新建 `plugins/code-skills/skills/code-publish/templates/Q&A.md`
- **前置任务**:无
- **关键变更**:
  - 文首 `# 发布部署 Q&A — <本版本号>`(自动填充)
  - 引言 `> 本手册聚合自 assistants/qanda/,供发布部署中遇到问题时查阅。`
  - 占位章节 `## 占位:常见问题(待补充)`
  - 占位提示 `请在 assistants/qanda/ 目录下添加 Q&A 内容(格式建议见 qanda/README.md),再重跑 code-publish`
- **依据规范**:`module-conventions.md §规则 1`

### 详细设计 §4 模块 10(本任务的主依据)

- **路径**:`plugins/code-skills/skills/code-publish/templates/Q&A.md`
- **内容结构**:见 needs §6.3 节选
- **关键字段**:详 `data-changes.md §4.3`

### 详细设计 §6.5 + QandaAggregator 渲染规则

- **占位模板原样使用场景**:QandaAggregator 找到 0 个非 README .md → 用本模板原样写入 `publish/Q&A.md`
- **聚合渲染场景**:QandaAggregator 找到 ≥ 1 个非 README .md → 在"占位章节之前"插入 N 个 `## <主题>(来源:qanda/<文件>)` 章节
- **本任务只写"占位模板"**;聚合渲染逻辑在 SKILL.md 步骤 2.6 已实现(QandaAggregator 算法)

## 开发过程

### 2026-06-04 17:50
- **操作**:验证 PLAN.md + 准备目录 + 推进状态
- **结果**:成功
- **状态推进**:PLAN.md 中 T-004 "待开始" → "进行中"

### 2026-06-04 17:51
- **操作**:读取 needs §6.3 + data-changes.md §4.3
- **结果**:成功(模板结构明确)

### 2026-06-04 17:52
- **操作**:写 `plugins/code-skills/skills/code-publish/templates/Q&A.md`
- **结果**:成功
- **文件大小**:待写完后核实(预计 ~50 行)
- **关键自检**:
  - 文首 H1 标题含 `<本版本号>` ✓
  - 引言段 ✓
  - 占位章节"## 占位:常见问题(待补充)" ✓
  - 占位提示(指向 qanda/README.md + 提示重跑 code-publish)✓
  - 末尾"附录"可选 ✓

### 关键决策与权衡

#### 决策 IT-1:H1 标题格式
- **选定**:`# 发布部署 Q&A — <本版本号>`
- **理由**:`code-publish` 替换后用户可见;与 DEPLOY.md 标题风格一致
- **依据**:data-changes.md §4.3

#### 决策 IT-2:引言段措辞
- **选定**:`> 本手册聚合自 \`assistants/qanda/\`,供发布部署中遇到问题时查阅。`
- **理由**:简短说明"这是什么" + "什么时候用"
- **依据**:NFR-9(可读性)

#### 决策 IT-3:占位章节命名"占位:常见问题(待补充)"
- **选定**:`## 占位:常见问题(待补充)`
- **理由**:"占位"前缀明确告诉用户"这是占位,等 qanda/ 充实后会被替换";"(待补充)"强化"待办"语义
- **依据**:needs §6.3 + NFR-9

#### 决策 IT-4:占位提示指向 qanda/README.md
- **选定**:`请在 \`assistants/qanda/\` 目录下添加 Q&A 内容(格式建议见 \`qanda/README.md\`),再重跑 \`code-publish\``
- **理由**:
  - 指向 qanda/README.md(由 T-005 创建)说明"格式"
  - 提示"重跑 code-publish"说明"如何重生成本模板"
- **依据**:FR-5 + FR-6 + 模块间协作

#### 决策 IT-5:不预设"问题分类"或"目录索引"
- **选定**:不写"按主题分类"段(由 QandaAggregator 动态生成)
- **理由**:qanda/ 目录的具体内容由用户决定;模板不应预先假设分类
- **依据**:NFR-5 通用性

#### 决策 IT-6:不引入"如何提交 Q&A"等元说明
- **选定**:不写"如何向本手册贡献 Q&A";该说明**属于** qanda/README.md(由 T-005 处理)
- **理由**:
  - Q&A.md 是"产物";"如何贡献"属于"维护说明"
  - 维护说明应在 qanda/README.md(项目级共享)而非 publish/Q&A.md(本版本产物)
- **依据**:模块边界清晰

#### 决策 IT-7:不预设具体问题/答案
- **选定**:不写"Q: 服务启动失败怎么办?"等具体问答
- **理由**:
  - Q&A 内容**应当**来自 qanda/(用户管理)
  - 模板写"具体问答"会与用户真实问题不符,反而误导
- **依据**:Q-2 锁定 A(qanda/ 人工管理)

### 验证手段(本任务的"测试"等价物)

| 验证项 | 期望 | 实际 |
| --- | --- | --- |
| 模板路径 | `plugins/.../templates/Q&A.md` | 同 | ✓ |
| H1 含 `<本版本号>` 自动 placeholder | ✓ | ✓ |
| 引言段说明"聚合自 + 何时用" | ✓ | ✓ |
| 占位章节命名清晰 | ✓ | `## 占位:常见问题(待补充)` |
| 占位提示指向 qanda/README.md | ✓ | ✓ |
| 不修改其他 10 个 `code-*` 技能 | ✓(仅新文件) | ✓ |
| 不修改 `rules/` | ✓ | ✓ |
| 不修改 CLAUDE.md / README | ✓ | ✓ |

## Q&A.md 模板 vs DEPLOY.md / UPDATE.md 模板的差异

| 差异点 | DEPLOY.md | UPDATE.md | Q&A.md |
| --- | --- | --- | --- |
| 篇幅 | 245 行(8 章节 + 附录) | 365 行(8 章节 + 11 子节) | **~50 行(简洁)** |
| 章节数 | 8 | 8 | **1 (占位)** |
| 内容来源 | 全部硬编码 | 全部硬编码 | **动态聚合**(由 QandaAggregator 渲染) |
| placeholder 数 | 14 | 17+ | **1**(`<本版本号>`) |
| 验证 checkbox | 15 | 26 | **0** |
| 与 `code-publish` 集成 | 直接复制 + 替换 | 直接复制 + 替换 | **复制 + QandaAggregator 动态插入聚合章节** |

**为什么 Q&A.md 模板这么小?**
- **DEPLOY.md / UPDATE.md** 是"步骤手册",**每一步都需用户补全 placeholder** → 内容丰富
- **Q&A.md** 是"问答手册",**具体问答在 qanda/ 而非模板** → 模板只是"占位"
- 模板的"小"是**正确的设计选择**(data-changes.md §4.3 明确只要求"文首 + 引言 + 占位章节")
- QandaAggregator 负责把 qanda/ 内容**动态插入**,无需在模板中预设
