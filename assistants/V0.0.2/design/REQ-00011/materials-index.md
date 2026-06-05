# 材料登记 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 | 本设计对应章节 |
| --- | --- | --- | --- |
| skill-conventions.md | 技能编写 | SKILL.md 必含 name + description,frontmatter 不变;name 与目录名一致 | §4.1, §4.4(INV-1) |
| module-conventions.md(已 DEPRECATED) | 模块规划(已弃用) | 资源放技能子目录 `templates/` / `checklists/` / `guidelines/` | §4.4 |
| directory-conventions.md | 目录与模块 | (规则 1 待添加);替代 module-conventions.md | §4.4 |
| dashboard-conventions.md | 看板与模板 | 看板字段约定扩展需 3 处同步(本需求**不**触发) | §1.2(不变), §7(不集成看板) |
| encoding-conventions.md | 编码格式 | 3 类编码权威源(本需求**不**产生新编码) | §6(无新增依赖) |
| migration-mapping.md | 编码迁移 | 旧 → 新编码追溯(本需求**不**涉及) | — |
| commit-conventions.md | 提交与合并 | (规则 1 待添加) | — |
| doc-conventions.md | 文档编写 | README 多语言对仗 + 主语言版本完整性(本需求**不**改 README) | §1.2(不变) |
| marketplace-protocol.md | Marketplace 协议 | $schema / name / version 必填,plugins[].version 同步(本需求**不**改) | §1.2(不变) |
| coding-style.md | 代码书写 | (规则 1 待添加) | — |
| framework-conventions.md | 框架选型 | (规则 1 待添加) | — |
| dependency-conventions.md | 三方依赖 | (规则 1 待添加);本需求 NFR-1 零新增依赖 | §6 |
| naming-conventions.md | 语言与命名 | (规则 1 待添加) | — |

## 上游需求

- 来源:./assistants/V0.0.2/require/REQ-00011/RESULT.md
- 版本:v1(2026-06-04 14:57)
- 提取的 FR / NFR / AC 数量:9 FR / 8 NFR / ~30 AC
- 关键 FR 映射到本设计章节:
  - FR-1 `code-design` 新增步骤 0b → §1.1(D-1), §3(D-1, D-2, D-3), §5.3
  - FR-2 `code-plan` 新增步骤 0b → §1.1(D-2), §3(D-4), §5.3
  - FR-3 `code-plan` 退化行为 → §3(D-4), §5.3
  - FR-4 `code-plan` 据设计目标调整粒度 → §3(D-5), §5.4
  - FR-5 回写文档 §3(D-2), §5.2
  - FR-6 `AskUserQuestion` 多个问题 → §3(D-3)
  - FR-7 不修改 8 个其他 `code-*` 技能 → §1.2, §4.1
  - FR-8 不修改 marketplace 与 plugin 与规范 → §1.2
  - FR-9 报告与建议 → §5.3(屏幕打印), §3(D-2)
- 关键 NFR:NFR-1 零新增依赖 / NFR-2 增量修改 / NFR-3 幂等 / NFR-4 不触发 dashboard / NFR-5 与 code-auto 协同 0 冲突 / NFR-6 步骤命名一致 / NFR-7 不提供跳过参数 / NFR-8 性能

## 项目现状(本次扫描)

### 项目类型
- 类型:Claude Code marketplace 仓库(插件 + 技能集合)
- 语言/框架:Markdown(技能定义) + JSON(协议清单);无运行时技术栈声明(`plugins/code-skills/CLAUDE.md` §需与用户确认的约定)

### 目录结构(顶层)
```
code-skills/
├── .claude-plugin/marketplace.json     # marketplace 根清单
├── plugins/code-skills/                # 插件本体
│   ├── .claude-plugin/plugin.json
│   ├── README.md / README.en.md
│   ├── CLAUDE.md
│   └── skills/
│       ├── code-init / code-version / code-rule
│       ├── code-require / code-design / code-plan
│       ├── code-it / code-unit / code-fix
│       ├── code-review / code-dashboard / code-publish
│       └── code-auto                    # 本需求不触发升级
└── assistants/                          # 版本感知工作空间
    ├── rules/                           # 项目级规范,跨版本共享
    ├── .current-version                 # V0.0.2
    └── V0.0.2/
        ├── RESULT.md
        └── require/ design/ plan/ code/ test/ review/
```

### 已有模块(本需求涉及)
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-design/SKILL.md` | 概要设计 SKILL 定义 | 需修改(增量追加"步骤 0b") |
| `plugins/code-skills/skills/code-design/templates/design.md` | 概要设计 RESULT.md 模板 | 需修改(顶部预留位) |
| `plugins/code-skills/skills/code-plan/SKILL.md` | 详细设计 SKILL 定义 | 需修改(增量追加"步骤 0b" + 任务粒度调整) |
| `plugins/code-skills/skills/code-plan/templates/plan.md` | 详细设计 RESULT.md 模板 | 需修改(顶部预留位) |

### 已有接口
- 无对外 API 变更(`code-design` / `code-plan` 内部流程调整)
- `code-plan` 内部新增加"读 `design/.../RESULT.md` '## 设计目标' 小节"调用(同文件 Read,无 IPC)

### 已有数据模型
- 看板"任务清单"区段表格列:沿用 V0.0.2 既有 8 列,本需求**不**改(`dashboard-conventions §规则 1` 不触发)
- `design/.../RESULT.md` / `plan/.../RESULT.md` 顶部新增"## 设计目标"小节(D-2)

### 已有第三方依赖
- 0(本项目是 Claude Code 技能集合,无运行时技术栈)

### 编码与构建约定
- SKILL.md 必含 frontmatter `name` + `description`(`skill-conventions §规则 1`)
- 资源放技能子目录 `templates/` / `checklists/` / `guidelines/`(`module-conventions §规则 1`,已 DEPRECATED 但仍参考)
- 目录布局沿用 `directory-conventions.md`(替代 module-conventions)
- 零新增依赖(NFR-1)

## 现状与规范的偏离
- **无**:`code-design` / `code-plan` 现行 SKILL.md **完全合规**所有适用规范(因规范大多为"待添加"状态)
