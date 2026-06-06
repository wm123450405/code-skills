# 材料登记 — REQ-00010

更新时间:2026-06-06 12:00
版本:V0.0.2
需求编码:REQ-00010

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` §规则 1 | SKILL.md 元信息 | frontmatter 必含 `name` + `description`;`name` 与目录名一致;**修改 SKILL.md 时不破坏 frontmatter** |
| `dashboard-conventions.md` §规则 1 | 看板字段 | 字段扩展需 `templates/version-RESULT.md` + `CLAUDE.md` + 本规范三方同步;**零字段变更 ⇒ 不触发本规则** |
| `encoding-conventions.md` §规则 1/2/3 | 编码格式 | 需求 `^REQ-\d{5}$`、缺陷 `^BUG-\d{5}$`、任务 `^TASK-(REQ|BUG)-\d{5}-\d{5}$`;本需求使用**任务编号正则**反推所属需求 |
| `module-conventions.md` | 模块 | 技能资源(模板/指南/清单)放 `skills/<name>/{templates,guidelines,checklists}/` |
| `coding-style.md` | 编码 | (本需求不写代码,但要确保产出的 SKILL.md 修改贴合既有风格 — 参见 `code-it/SKILL.md` §标题解析) |
| `doc-conventions.md` | 文档 | (本需求不改 README,故不触发) |
| `commit-conventions.md` | 提交 | (由 `code-it` 步骤 N 末尾兜底提交遵循;本设计不展开) |
| `framework-conventions.md` | 框架 | (本需求不涉及) |
| `dependency-conventions.md` | 依赖 | (本需求零新增依赖) |
| `naming-conventions.md` | 命名 | 任务编码与 SKILL.md 内引用遵循既有命名 |
| `migration-mapping.md` | 编码追溯 | (本需求不涉及) |
| `marketplace-protocol.md` | 插件市场 | (本需求不动 `marketplace.json` / `plugin.json`) |

## 上游需求
- 来源:`./assistants/V0.0.2/require/REQ-00010/RESULT.md`
- 版本:v1(2026-06-04 14:36 锁定)
- FR 数量:6(FR-1 ~ FR-6)
- NFR 数量:8(NFR-1 ~ NFR-8)
- AC 数量:约 22(FR-1:8 + FR-2:7 + FR-3:4 + FR-4:3 + FR-5:6 + FR-6:3)
- 关键约束:
  - **零规范变更**(NFR-3 强约束)
  - **不修改 frontmatter**(NFR-7 / `skill-conventions §规则 1`)
  - **不修改 9 个其他 `code-*` 技能**(FR-4)
  - **不修改 PLAN.md 模板 / 看板"(none) 任务清单"区段**(FR-5)

## 项目现状(本次扫描)

### 项目类型
- **类型**:Claude Code 插件市场仓库(`code-skills` marketplace)
- **语言/框架**:Markdown 文档 + YAML frontmatter(无源码,无构建系统)
- **关键依赖**:无(纯文档)

### 目录结构
```
code-skills/                              ← marketplace 仓库根
├── .claude-plugin/marketplace.json
└── plugins/code-skills/                  ← 插件本体
    ├── .claude-plugin/plugin.json
    ├── README.md / README.en.md
    ├── CLAUDE.md                         ← 项目指引(已含看板字段约定)
    └── skills/
        ├── code-init/ code-version/ code-rule/
        ├── code-require/ code-design/ code-plan/
        ├── code-it/ code-unit/ code-fix/ code-review/
        ├── code-dashboard/ code-publish/ code-auto/
        └── (各技能内部)
            ├── SKILL.md                  ← 技能入口
            ├── templates/                ← 模板(可选)
            ├── guidelines/               ← 强制规则(可选)
            └── checklists/               ← 校验清单(可选)
```

### 已有模块 — 目标修改模块
| 模块/路径 | 职责 | 是否可复用 | 本次处理 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-it/SKILL.md` | 开发编码技能入口(版本感知) | 复用既有 | **修改** — 在"工具使用约定"段后追加"步骤 0a 前置任务守卫"小节(沿用 REQ-00013 标题解析追加模式) |
| `plugins/code-skills/skills/code-it/SKILL.md` 既有"步骤 7 检查前置任务" | 原有的"显式前置任务"字段检查 | 保留原状 | **不修改** — 本需求是更前置的"步骤 0a 守卫"(按 PLAN.md 登记顺序,无字段依赖),与原"步骤 7 显式字段检查"并存(职责正交) |

### 已有模块 — 参照模块
| 模块/路径 | 职责 | 参照点 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-unit/SKILL.md` | 单元测试技能入口 | §"标题解析(REQ-00013 新增)"小节追加模式 |
| `plugins/code-skills/skills/code-it/SKILL.md` 自身 §"标题解析" | REQ-00013 追加的"工具函数" + "屏幕输出格式契约"段 | 锚点参照(本需求在中段插入"步骤 0a 守卫"小节) |
| `plugins/code-skills/skills/code-it/SKILL.md` §"工作流程" 步骤 0 | 既有"版本上下文检测"(强制前置) | 锚点参照(本需求在其**前**插入"步骤 0a") |
| `plugins/code-skills/skills/code-require/SKILL.md` | 需求分析技能 | 解析 `^## 任务清单$` / `^## 概要设计清单$` 模式(本需求按类似锚点解析 PLAN.md) |

### 已有接口(本需求不新增)
- 无新增 API;本需求仅改技能行为语义,不引入新对外接口

### 已有数据模型
- 不涉及;本需求**不**修改 `PLAN.md` 模板、不修改看板"(none) 任务清单"区段(零字段变更)
- **复用**:`PLAN.md` 任务总览区段的**文件行序**作为"前置关系"信息源(零新增字段)

### 已有第三方依赖
- 无(本需求 NFR-1 零新增依赖)

### 编码与构建约定
- 既有 `code-it/SKILL.md` 已含 22 个一级章节(目标 / 适用场景 / 不适用 / 工作目录约定 / 输入 / 输出 / 工具使用约定 / 修改文件前必须重读最新内容 / **标题解析(REQ-00013 新增)** / 工作流程 / 缺陷分支 / 过程文档格式 / 衔接 / 不要做的事)
- 新增小节的"语义化定位"沿用既有:`## 标题解析(REQ-00013 新增)` 段后 / `## 工作流程` 段前 之间的"流程概览"位置
- 修改方式:`Edit` 工具**追加**(NFR-2 强约束:不重写稳定章节,不修改 frontmatter)
- 提交:由 `code-it` 步骤 N 末尾兜底提交遵循(本设计不展开)

### 可复用资产
- `parsePlanTaskTitle()` 工具函数(REQ-00013 已沉淀,可直接复用取任务标题)
- `formatTaskTitle()` / `truncateTitle()` 工具函数(REQ-00013 已沉淀)
- `code-dashboard` NFR-3 任务编码双格式正则(本设计**不**直接调用,但参照其解析语义)
