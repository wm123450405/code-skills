# 开发日志 — TASK-REQ-00006-00005

开始时间:2026-06-04 17:54
版本:V0.0.2
任务标题:`[新增] 写 templates/qanda-README.md 模板(用途/命名/引用/维护)`
触发/来源:需求新增

## 项目现状(步骤 6 记录)

- **项目类型**:Claude Code Marketplace 插件(`code-skills`),纯文档型
- **既有 `code-publish/templates/`**(由 T-002/003/004 已就绪):
  - `DEPLOY.md` 245 行(全新部署手册)
  - `UPDATE.md` 365 行(升级手册)
  - `Q&A.md` 63 行(聚合占位)
  - `qanda-README.md` 即将创建(本任务)
- **既有 `code-fix/templates/bug.md` 等 README 范式**:
  - 任何技能的 README 都是 1 级标题 + 4~6 章节 + 无 checkbox
  - 短小精悍,**不**写具体业务流程

## 项目级规范要点(步骤 4 记录)

- `./assistants/rules/module-conventions.md` §规则 1:**强约束**
  - 路径必须在 `plugins/code-skills/skills/code-publish/templates/`
  - kebab-case `<用途>.md`
- 其他 12 个规范文件:占位或不相关

## 任务设计要点(步骤 5 记录)

### PLAN.md §3 任务详情(T-005 摘要)

- **类型**:新增
- **触发/来源**:需求新增
- **目标**:创建 `assistants/qanda/README.md` 的骨架(本需求顺带产物;QandaScaffolder 消费)
- **涉及文件**:新建 `plugins/code-skills/skills/code-publish/templates/qanda-README.md`
- **前置任务**:无
- **关键变更**:
  - 文首 `# assistants/qanda/ — 项目级 Q&A 长期沉淀目录`
  - `## 用途`:本目录用于沉淀发布部署相关的 Q&A 内容,被 `code-publish` 聚合到 `<版本号>/publish/Q&A.md`(AC-6.2 之一)
  - `## 文件命名建议`:`<主题>.md`,如 `deploy-faq.md` / `db-init-faq.md`(AC-6.2 之一)
  - `## 引用规范`:本目录是项目级共享(跨版本);文件命名建议 kebab-case;README.md 不被聚合(AC-6.2 + DD-6)
  - `## 维护方式`:暂时人工整理(Q-2 锁定);未来可由独立技能管理(v2)
- **依据规范**:`module-conventions.md §规则 1`

### 详细设计 §4 模块 11(本任务的主依据)

- **路径**:`plugins/code-skills/skills/code-publish/templates/qanda-README.md`
- **内容结构**:4 章节(用途 / 命名 / 引用 / 维护)
- **关键字段**:详 `data-changes.md §4.4`

### 与 T-004(Q&A.md 模板)的关系

- **Q&A.md 模板**(T-004)中的"4 步添加 Q&A 内容"指南**显式指向** `qanda/README.md`
- **qanda/README.md**(本任务)**详细说明** 4 步中的细节
- 两文档**相互引用**:
  - T-004 的 Q&A.md 模板:1 段简短引用
  - T-005 的 qanda/README.md:详细 4 章节

## 开发过程

### 2026-06-04 17:54
- **操作**:验证 PLAN.md + 准备目录 + 推进状态
- **结果**:成功
- **状态推进**:PLAN.md 中 T-005 "待开始" → "进行中"

### 2026-06-04 17:55
- **操作**:读 data-changes.md §4.4 + 引用 T-004 的 Q&A.md 模板(交叉验证引用关系)
- **结果**:成功(模板结构明确,与 Q&A.md 引用一致)

### 2026-06-04 17:56
- **操作**:写 `plugins/code-skills/skills/code-publish/templates/qanda-README.md`
- **结果**:成功
- **文件大小**:待写完后核实
- **关键自检**:
  - 4 章节齐全 ✓(用途 / 命名 / 引用 / 维护)
  - 命名建议含 2 个具体示例 ✓
  - 引用规范说明 README.md 不被聚合 ✓
  - 维护方式标注"暂时人工"(Q-2 锁定)✓

### 关键决策与权衡

#### 决策 IT-1:H1 标题
- **选定**:`# assistants/qanda/ — 项目级 Q&A 长期沉淀目录`
- **理由**:与 needs §AC-6.2 严格一致
- **依据**:data-changes.md §4.4

#### 决策 IT-2:4 章节结构对齐设计
- **选定**:`## 用途` / `## 文件命名建议` / `## 引用规范` / `## 维护方式`
- **理由**:data-changes.md §4.4 显式要求 4 章节
- **依据**:data-changes.md §4.4

#### 决策 IT-3:文件命名示例用 2 个具体名字
- **选定**:`deploy-faq.md` + `db-init-faq.md`(而非"如 foo.md"这种抽象)
- **理由**:
  - 具体例子比抽象例子更可操作
  - `deploy-faq` + `db-init-faq` 是发布部署场景的**真实需求**
- **依据**:data-changes.md §4.4 的"如"示例 + NFR-9

#### 决策 IT-4:引用规范强调"README.md 不被聚合"
- **选定**:`code-publish` 聚合时**自动排除** `README.md`(避免把"目录说明"当 Q&A 内容)
- **理由**:
  - 排除规则是 FR-5 AC-5.1 隐含的"实现细节";**显式说明**让用户理解
  - 避免用户添加 "README 内容" 时被错误聚合
- **依据**:Q-2 锁定 A + FR-5

#### 决策 IT-5:维护方式写"暂时人工整理"
- **选定**:`目前由人工手动整理;未来 v2 可能由独立技能管理(如 code-qanda 技能)`
- **理由**:
  - Q-2 锁定 A:暂时人工
  - "未来 v2"提示可能的演进方向
- **依据**:Q-2

#### 决策 IT-6:不写"如何贡献"等元说明
- **选定**:**不**在 qanda/README.md 中写"如何提交 PR"等说明
- **理由**:
  - 本仓库**不**有 PR 流程(纯文档,本地编辑)
  - "维护方式"已隐含"暂时人工";额外元说明冗余
- **依据**:NFR-9

#### 决策 IT-7:不写"Q&A 内容应该 / 不应该"的内容政策
- **选定**:**不**写"敏感信息禁止"等政策
- **理由**:
  - 本项目**不**有内容审查(纯文档,无代码扫描)
  - 用户对自己写入的内容负责
  - 若未来需要审查,**新技能**可独立承担
- **依据**:NFR-5(简单优于复杂)

#### 决策 IT-8:不引用 SKILL.md(避免"反向依赖")
- **选定**:本 README **不**写"由 `code-publish` 创建"等反向引用
- **理由**:
  - `qanda/README.md` 是**项目级共享**,**不**应知道 `code-publish` 技能的存在
  - 反向引用 = 模块边界不清
- **依据**:模块边界清晰

### 验证手段

| 验证项 | 期望 | 实际 |
| --- | --- | --- |
| 4 章节齐全 | ✓ | 4 章节 |
| 命名建议含 2 个具体示例 | ✓ | `deploy-faq.md` + `db-init-faq.md` |
| 引用规范说明 README.md 不被聚合 | ✓ | 显式 |
| 维护方式标注"暂时人工" | ✓ | ✓ |
| 不修改其他 10 个 `code-*` 技能 | ✓(仅新文件) | ✓ |
| 不修改 `rules/` | ✓ | ✓ |
| 不修改 CLAUDE.md / README | ✓ | ✓ |

## qanda/README.md vs 其他 README 的对比

| 文档 | 位置 | 篇幅 | 主要读者 |
| --- | --- | --- | --- |
| `qanda/README.md`(本任务) | `assistants/qanda/`(项目级) | ~50 行 | 项目维护者(向 qanda/ 添加内容的人) |
| `publish/Q&A.md`(T-004 模板) | `plugins/.../code-publish/templates/Q&A.md`(技能级) | 63 行(动态聚合后更大) | 运维 / 现场支持(发布后查阅) |
| `plugins/.../code-publish/README.md`(标准) | `plugins/.../code-publish/`(项目级) | (由 T-006 复制范式) | 项目浏览者 |

**模块边界**:
- `qanda/README.md`:项目级共享,跨版本
- `publish/Q&A.md`:版本产物,本版本发布
- `code-publish/README.md`:项目级,描述技能本身
