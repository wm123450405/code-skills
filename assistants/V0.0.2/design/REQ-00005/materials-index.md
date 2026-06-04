# 材料登记 — REQ-00005

更新时间:2026-06-04 16:00
版本:V0.0.2

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | 技能编写 | §规则 1 — SKILL.md 必须 YAML frontmatter 含 `name`+`description`,`name` 与目录名一致;**新增/扩展 frontmatter 需走 `dashboard-conventions §规则 1` 同步** |
| `./assistants/rules/dashboard-conventions.md` | 看板与模板 | §规则 1 — 看板/模板扩展需 `templates/version-RESULT.md` + `CLAUDE.md` + 本规范三方同步;**不**改 frontmatter 字段(本需求严格不触发) |
| `./assistants/rules/doc-conventions.md` | 文档编写 | §规则 1 — README 多语言对仗 + 同步提交;§规则 2 — 主语言 README 完整覆盖核心小节 |
| `./assistants/rules/marketplace-protocol.md` | Marketplace 协议 | §规则 1 — `$schema` / `name` / `version` 必填;plugin 与 marketplace version 同步;`source` 必须 `./` 开头;`skills` 必须是相对路径数组;**不**允许未知字段 |
| `./assistants/rules/encoding-conventions.md` | 编码格式 | §规则 1 — REQ/BUG 5 位纯数字;TASK 嵌套式 5+5 位;**权威源** |
| `./assistants/rules/migration-mapping.md` | 编码迁移 | §规则 1 — 已落地映射表;§规则 2 — 理论映射;§规则 3 — 通用公式;§规则 4 — EXISTING-NNN 不追溯 |
| `./assistants/rules/module-conventions.md` | 模块规划 | ⚠️ **DEPRECATED**,内容已迁到 `directory-conventions.md`;§规则 1 — 技能资源放 `templates/` / `checklists/` / `guidelines/`(本需求不触发) |
| `./assistants/rules/directory-conventions.md` | 目录结构 | §规则 1 — **占位**,等待填充(本需求不触发) |
| `./assistants/rules/coding-style.md` | 代码风格 | §规则 1 — **占位**(本需求不触发,本需求不写代码) |
| `./assistants/rules/commit-conventions.md` | 提交与合并 | §规则 1 — **占位**(本需求**不**直接填充规则,留作 follow-up);NFR-6 沿用 V0.0.1 实践 `chore(<scope>): <subject>` |
| `./assistants/rules/dependency-conventions.md` | 三方依赖 | §规则 1 — **占位**(本需求**零新增**运行时依赖) |
| `./assistants/rules/framework-conventions.md` | 框架选型 | §规则 1 — **占位**(本需求不触发) |
| `./assistants/rules/naming-conventions.md` | 命名风格 | §规则 1 — **占位**(本需求不触发) |

> 13 个规范文件中:**3 个有强约束**(skill / dashboard / doc / marketplace / encoding / migration 共 6 个),**7 个占位**待填充。**无任何规范**与本需求"末尾 commit 模板"直接冲突,因 `commit-conventions.md` 是占位。

## 上游需求

- **来源**:`./assistants/V0.0.2/require/REQ-00005/RESULT.md`
- **版本**:v1(2026-06-04 13:33)
- **状态**:已锁定
- **提取**:
  - **6 条 FR**:FR-1 步骤 0a 拉取最新代码(3 技能);FR-2 步骤 0b 版本对齐检查(仅 `code-require`);FR-3 末尾兜底提交(3 技能);FR-4 不改 `code-it` 内部 commit(Q-4 锁定 B);FR-5 不改 `code-version`;FR-6 不改 marketplace.json / plugin.json / CLAUDE.md
  - **8 条 NFR**:NFR-1 ~ NFR-8(零新增依赖 / 增量修改 / 硬中断 / 幂等 / 错误透明 / 不污染 commit-conventions / 与 code-it 边界严格 / 拉取后版本对比)
  - **~32 条 AC**:FR-1(4) + FR-2(6) + FR-3(6) + FR-4(3) + FR-5(2) + FR-6(3) + 8 NFR 各 1 = ~32
  - **6 个场景 S-1 ~ S-6**:S-1 多设备、 S-2 本地一致、 S-3 冲突、 S-4 简化首步、 S-5 无变更、 S-6 commit 失败
  - **13 个边界 E-1 ~ E-13**(Q-2 锁定 A:中断 + 报错退出)
  - **8 个澄清项 Q-1 ~ Q-8**:Q-1/Q-2/Q-3/Q-4 已锁定 A;Q-5/Q-7 未采用(留 follow-up);Q-6/Q-8 采纳默认
  - **关联需求**:REQ-00001/00002/00003/00004(详见 §related-requirements.md)
- **用户原文笔误**:已纠正(`/code-desgin` → `/code-design`、`/core-require` → `/code-require`)

## 项目现状(本次扫描)

### 项目类型
- **仓库类型**:Claude Code marketplace 仓库(由 `marketplace.json` + `plugin.json` 描述)
- **本仓库无应用源代码**:无 Node.js / Python / Go 等运行时;无 build/lint/test 工具链(`CLAUDE.md` 显式说明)
- **唯一"代码"载体**:`plugins/code-skills/skills/<10 个技能>/SKILL.md`(Markdown 文本)
- **唯一"运行时"**:Claude Code 解释执行 SKILL.md 中描述的工作流,工具集 = Read / Write / Edit / Glob / Grep / Bash / Skill / AskUserQuestion

### 目录结构
```
code-skills/                                # marketplace 仓库根
├── .claude-plugin/marketplace.json         # 协议清单(本需求严禁修改,FR-6)
├── plugins/code-skills/
│   ├── .claude-plugin/plugin.json          # 子插件清单(严禁修改)
│   ├── CLAUDE.md                           # 项目说明(本需求**未授权**修改,留 follow-up)
│   ├── README.md                           # 中文 README(doc-conventions §规则 1 约束)
│   ├── README.en.md                        # 英文 README(同上)
│   └── skills/
│       ├── code-init/                      # 工程初始化(本需求不触发)
│       ├── code-version/                   # 版本管理(本需求**调用**但不修改)
│       ├── code-rule/                      # 规范管理(本需求不触发)
│       ├── code-require/                   # 需求分析 ⭐ 本需求修改
│       ├── code-design/                    # 概要设计 ⭐ 本需求修改
│       ├── code-plan/                      # 详细设计 ⭐ 本需求修改
│       ├── code-it/                        # 开发编码(本需求不修改,Q-4 锁定 B)
│       ├── code-unit/                      # 单元测试(本需求不修改)
│       ├── code-fix/                       # 缺陷登记(本需求不修改)
│       └── code-review/                    # 代码评审(本需求不修改)
└── assistants/                             # 项目级工作空间
    ├── rules/                              # 13 个规范文件(本设计只读)
    ├── .current-version                    # 激活版本标记(本技能首步读取)
    ├── V0.0.0/                             # 基线版本(本需求不触发)
    ├── V0.0.1/                             # 历史版本(本需求不触发)
    └── V0.0.2/                             # 当前激活版本
        ├── RESULT.md                       # 看板(本技能追加"概要设计清单")
        ├── require/                        # 需求分析产物
        ├── design/                         # 概要设计产物(本技能产出)
        ├── plan/                           # 详细设计产物(下游)
        ├── code/                           # 任务实施产物(下游)
        ├── test/                           # 测试产物(下游)
        ├── review/                         # 评审产物(下游)
        └── fix/                            # 缺陷产物(下游)
```

### 已有模块

| 模块/路径 | 职责 | 是否可复用 | 复用方式 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-require/SKILL.md` | 需求分析(13.7KB) | 是 | **修改** — 在"步骤 0 之前"插入"步骤 0a 拉取 + 步骤 0b 版本对齐";"末尾"插入"步骤 N 兜底提交" |
| `plugins/code-skills/skills/code-design/SKILL.md` | 概要设计(19.7KB) | 是 | **修改** — 在"步骤 0 之前"插入"步骤 0a 拉取";"末尾"插入"步骤 N 兜底提交" |
| `plugins/code-skills/skills/code-plan/SKILL.md` | 详细设计(33.0KB) | 是 | **修改** — 在"步骤 0 之前"插入"步骤 0a 拉取";"末尾"插入"步骤 N 兜底提交" |
| `plugins/code-skills/skills/code-version/SKILL.md` | 版本管理(被 `code-require` FR-2 调用) | 是 | **不修改**(FR-5 显式);以"独立技能调用"形式被复用 |
| `plugins/code-skills/skills/code-it/SKILL.md` | 开发编码(内部 commit 行为) | 是 | **不修改**(FR-4 显式,Q-4 锁定 B);本需求末尾兜底提交与之并存 |
| `plugins/code-skills/.claude-plugin/plugin.json` | 插件清单 | — | **严禁修改**(FR-6 / `marketplace-protocol.md §规则 1.3`) |
| `.claude-plugin/marketplace.json` | marketplace 清单 | — | **严禁修改**(FR-6) |
| `plugins/code-skills/CLAUDE.md` | 项目说明 | — | **不修改**(本需求**未授权**触达 `dashboard-conventions §规则 1`,留 follow-up) |
| `plugins/code-skills/README.md` / `README.en.md` | 工作流总览(中英) | — | **不修改**(本需求**不主动**写 README 同步"3 个技能步骤变化",由后续 `code-rule` 沉淀) |
| `assistants/V0.0.2/RESULT.md` | 版本看板 | 是 | **追加** — 在"概要设计清单"区段追加本条 + "变更记录"区段追加条目 |

### 已有接口
- **本仓库无运行时 API**:`SKILL.md` 是 Markdown 文档,被 Claude Code 解释为自然语言工作流
- **"对外接口" = 工作流步骤描述**:每个技能定义"步骤 0 → 步骤 1 → ... → 步骤 N"的执行序列
- **"接口契约" = 工作流前置/后置条件 + 错误处理**

### 已有数据模型
- **无运行时数据模型**;本仓库**只有"文件级产物"**(Markdown 文档)
- **核心数据载体**:
  - `assistants/.current-version`(单行版本号字符串,如 `V0.0.2`)
  - `assistants/V<版本号>/RESULT.md`(版本看板,Markdown 表格)
  - `assistants/V<版本号>/<阶段>/<需求编码>/...` 树状目录

### 已有第三方依赖
- **运行时**:0(无代码,无 Node.js / Python / Go)
- **构建工具**:0
- **测试框架**:0
- **Lint 工具**:0
- **Claude Code 协议依赖**:2(隐式)— `marketplace.json` + `plugin.json` 的 `$schema` 字段
- **工具链**:`git`(FR-1 / FR-3 步骤的底层命令)— **Bash 工具内置**,无新增依赖

### 编码与构建约定
- **Markdown 是唯一代码**:所有"代码"在 `SKILL.md` / `RESULT.md` / `*.md`
- **frontmatter 不可变**:`SKILL.md` 顶部 YAML 元数据(`name` / `description`)**严禁修改**(`skill-conventions.md §规则 1` + FR-6)
- **增量修改优先**:NFR-2 显式要求用 Edit 工具追加新步骤,不重写稳定章节
- **commit message 格式**:`chore(<scope>): <subject>`,沿用 V0.0.1 实践(NFR-6),scope 选用 `code-require` / `code-design` / `code-plan`
- **同次提交**:中英 README 必须同步(`doc-conventions.md §规则 1`)— 本需求**不**触发(本需求不写 README)
- **三文件同步**:看板字段约定扩展时,`templates/version-RESULT.md` + `CLAUDE.md` + `dashboard-conventions.md` 必须同次提交 — 本需求**不**触发(不扩展字段)

### 可复用资产
- **CLAUDE.md §"双状态任务模型" / §"触发/来源"**:虽与本需求无直接关联,但展示了"已有约定"的稳定性 — 本需求**不**触达该小节
- **V0.0.1 看板"执行的开发命令记录"区**:本需求末尾兜底提交的"commit 失败"处理可参考其记录风格(透明化)
- **V0.0.1 既有实践"chore(<scope>): <subject>"**:NFR-6 直接采用,无需新增规范

### 与规范的交叉验证
- ✅ **`skill-conventions.md §规则 1`**:NFR-2 + FR-1.AC-1.4 + FR-6 显式要求"不改 frontmatter",本设计 100% 合规
- ✅ **`dashboard-conventions.md §规则 1`**:本需求**不**扩展看板字段,**不**触发三方同步
- ✅ **`marketplace-protocol.md §规则 1`**:FR-6 显式禁止修改 `marketplace.json` / `plugin.json`,本设计 100% 合规
- ✅ **`doc-conventions.md §规则 1`**:本需求**不**修改 README,**不**触发中英同次提交(留 follow-up)
- ⚠️ **`commit-conventions.md`**:占位文件,本需求 NFR-6 显式不直接填充规则,留作 follow-up
- ✅ **`encoding-conventions.md`**:本需求不生成新 REQ/BUG/TASK 编码(0 新增),不触发
