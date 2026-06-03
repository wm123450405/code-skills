# 材料登记 — REQ-00001
更新时间:2026-06-03 20:25
版本:V0.0.1

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `dashboard-conventions.md` | 看板/版本工作空间 | §规则 1:看板字段约定扩展需三处同步(模板 + CLAUDE.md + 本规范);本需求不改字段约定,不触发 |
| `doc-conventions.md` | 文档编写 | §规则 1:README 中英版本必须结构对仗,**同次提交**同步;§规则 2:README 中命令/路径必须反映仓库实际状态 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`$schema`/`name`/`version` 必填;`plugins[].name` 必须与 `plugin.json` name 同步;**允许**改根 `name`(kebab-case 保持),不影响 `plugins[].name` |
| `module-conventions.md` | 技能资源摆放 | §规则 1:技能资源放 `templates/` / `checklists/` / `guidelines/` 子目录;本需求不改任何资源,仅改根清单文件 |
| `skill-conventions.md` | 技能元信息 | §规则 1:SKILL.md frontmatter 必含 `name` + `description`,`name` 与目录名一致;本需求不改 SKILL.md,不触发 |

> 规范层面对本需求的约束总览:**唯一强触发**是 `doc-conventions.md §规则 1`(README 中英同次提交);其余规范仅"被读"以确认无副作用。

## 上游需求
- 来源:`./assistants/V0.0.1/require/REQ-00001/RESULT.md`
- 版本:v2(2026-06-03 20:20,含目录重命名记录)
- 提取的 FR / NFR / AC 数量:7 FR / 7 NFR / 9 AC
- 待澄清:3 项(Q-3 description / Q-4 迁移指引 / Q-5 version bump),均**非阻塞**且有合理默认值(全部"不改")

## 项目现状(本次扫描)

### 项目类型
- Claude Code marketplace + 单 plugin:`code-skills`
- 根协议清单:`.claude-plugin/marketplace.json`
- 插件本体:`plugins/code-skills/`
- 插件清单:`plugins/code-skills/.claude-plugin/plugin.json`
- 10 个 code-* 技能(`code-init` / `code-version` / `code-rule` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-fix` / `code-review`)
- 仓库**不包含**任何源代码、构建系统、测试框架、Lint、包管理(由 CLAUDE.md §"需与用户确认的约定"声明)

### 目录结构
```
code-skills/                                ← marketplace 仓库根
├── .claude-plugin/
│   └── marketplace.json                    # ⚠ 本需求改此文件根 `name`
├── plugins/
│   └── code-skills/                        # 插件本体(目录名保持)
│       ├── .claude-plugin/
│       │   └── plugin.json                 # ⚠ 本需求禁止修改
│       ├── README.md                       # ⚠ 本需求改此文件
│       ├── README.en.md                    # ⚠ 本需求改此文件
│       ├── CLAUDE.md                       # ⚠ 本需求 Grep 后决定是否改
│       └── skills/<10 个技能>/
└── assistants/                             # 项目工作空间(本需求不直接相关)
    ├── .current-version
    ├── rules/<5 个规范文件>               # ⚠ 本需求禁止修改
    └── V0.0.0/V0.0.1/...
```

### 已有模块 / 接口 / 数据模型
- **不适用**:本仓库无应用代码;唯一对外契约是 marketplace.json / plugin.json / README 的 install 命令。无数据库、无 API、无业务数据模型。
- 本需求是"协议清单字段 + 文档文本"层面的字符串替换,不涉及代码模块。

### 已有第三方依赖
- 0 个(本仓库无第三方依赖,纯文档/清单/技能定义)

### 编码与构建约定
- 无(本仓库无源代码/构建系统)
- 文档规范:`doc-conventions.md`(已加载)
- 协议规范:`marketplace-protocol.md`(已加载)

### 可复用资产
- 全部 10 个技能与 5 个规范文件均**完全可复用**,本需求不修改其中任何文件

## 关键观察
1. 本需求**范围极小**(< 5 个文件,1 个 JSON 字段 + 多处 Markdown 文本),但**风险中等**(breaking change,影响所有下游用户)
2. 真正的"技术性"决策是**编辑策略 + 提交粒度 + 验证范围**
3. 唯一必须强约束的是"中英 README 同次提交"(doc-conventions §规则 1)
4. 协议层(`marketplace.json` 根 name)与 plugin 标识(`plugins[].name` / `plugin.json` name)**解耦**,改名不会破坏约束
