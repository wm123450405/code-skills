# 材料登记 — REQ-00032

更新时间:2026-06-12 16:15
版本:V0.0.3

## 1. 项目级规范

> 本次参考 `./assistants/rules/` 下 7 个核心规范文件(其他 5 个不直接相关)

| 规范文件 | 类别 | 关键约束摘要 | 与本需求关联 |
| --- | --- | --- | --- |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留;`name` 与目录名一致;`description` 必填 | **INV-1 字节级保留**(本需求) |
| doc-conventions.md | 文档 | README 中英版对仗;仓库级 README 持续维护 | 不直接相关(本需求不涉及 README) |
| naming-conventions.md | 命名 | 变量/函数/类命名;kebab-case 目录 | 沿用(目录名 `code-require` 不变) |
| encoding-conventions.md | 编码 | 5 位纯数字生成端;接收端宽松正则;前缀固定 | 沿用(需求编码 `REQ-00032` 5 位) |
| module-conventions.md | 模块 | 资源文件放 templates/ 子目录;目录结构 | 沿用(本需求不新增 templates) |
| dashboard-conventions.md | 看板 | 看板字段三方同步;`^## 需求清单$` 锚点 | 沿用(本需求同步"概要设计清单") |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀 | **INV-3**(本需求) |
| directory-conventions.md | 目录 | 顶层目录职责;Kebab-case | 沿用 |
| framework-conventions.md | 框架 | 框架选型偏好 | 不适用(本仓库无框架代码) |
| dependency-conventions.md | 依赖 | 依赖管理 | 沿用(本需求 0 新增依赖) |
| coding-style.md | 编码风格 | 风格约定 | 沿用(本需求不涉及源码改动) |
| marketplace-protocol.md | 协议 | marketplace.json 协议 | 不适用(本需求不涉及 marketplace 改动) |
| migration-mapping.md | 迁移 | 迁移映射 | 不适用 |

## 2. 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00032/RESULT.md`
- 版本:V0.0.3(2026-06-12 16:10)
- 提取:4 FR / 9 NFR / 18 AC / 4 已澄清 / 4 留作 follow-up
- 用户原始输入:
  > 优化 `/code-require` 技能,在技能登记结束后的报告中,输出下一步建议是,针对微小需求建议直接使用 `/code-auto` 技能直接完成开发任务,其他的需求才建议先进行 `/code-design` 进行概设并继续后续任务。

## 3. 项目现状(本次扫描)

### 3.1 项目类型

- 仓库类型:Claude Code 插件市场(marketplace)
- 语言/框架:无(本仓库仅含 Markdown 文档 + YAML/JSON 配置,无编程语言)
- 关键依赖:无

### 3.2 目录结构(顶层)

```
code-skills/                          ← marketplace 仓库根
├── .claude-plugin/
│   └── marketplace.json              # 插件市场清单
└── plugins/
    └── code-skills/                  ← 插件本体
        ├── .claude-plugin/
        │   └── plugin.json
        ├── README.md / README.en.md
        ├── CLAUDE.md
        └── skills/
            ├── code-init/            # 工程初始化
            ├── code-version/         # 版本管理
            ├── code-rule/            # 编码规范管理
            ├── code-require/         # 需求分析 ← 本需求唯一改造对象
            ├── code-design/          # 概要设计
            ├── code-plan/            # 详细设计
            ├── code-it/              # 开发编码
            ├── code-unit/            # 单元测试
            ├── code-fix/             # 缺陷登记
            └── code-check/           # 代码评审
```

### 3.3 已有模块(与本需求直接相关)

| 模块/路径 | 职责 | 是否可复用 | 改造范围 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-require/SKILL.md` | 需求分析 | 是 | **修改**(步骤 10A / 10B 末尾追加"下一步建议"段) |
| `plugins/code-skills/skills/code-require/templates/requirements.md` | 需求文档模板 | 是 | **不修改**(NFR-2 零规范变更) |

### 3.4 既有 code-require 步骤 10A / 10B 末尾(锚点)

- **步骤 10A**(首次分析):
  ```
  ### 步骤 10A — 完善过程文档
  - 收尾 `materials-index.md` / `clarifications.md` / `related-requirements.md` / `analysis-notes.md`
  - 向用户汇报:本次新增了哪些 FR/AC、哪些被列为待澄清、关联了哪些需求、版本看板的更新点
  ```
- **步骤 10B**(增量更新):
  ```
  ### 步骤 10B — 汇报
  向用户汇报本次增量更新:
  - **新增**了哪些内容(章节/FR 编号)
  - **修改**了哪些内容(章节/FR 编号)
  - **未变**的内容(简述)
  - **新增的待澄清项**
  - **版本看板的同步情况**
  ```
- **步骤 N**(末尾兜底提交):在 步骤 10A / 10B **之后**,**不**在步骤 N 内插入新建议段

### 3.5 既有项目级规范要点(本需求相关)

- **`skill-conventions.md`**:SKILL.md frontmatter L1-3 字节级保留(INV-1)
- **`commit-conventions.md`**:`chore(<skill>):` 前缀(INV-3)
- **既有 12 个 REQ 的 RESULT.md 0 改**(INV-7)
- **其他 9 个 `code-*` 技能 SKILL.md 0 改**(INV-4)
- **7 个项目级规范 0 改**(INV-5)
- **4 个 README/marketplace/plugin/CLAUDE 0 改**(INV-6)
- **`code-auto` 步骤 4.b 沿用 REQ-00031 FR-6 恒等跳过**(NFR-8)
