# 需求提示词文档 — REQ-00012(在仓库根目录创建极简 README + 移动 CLAUDE.md 到根)

- 需求编码:REQ-00012
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-04
- 最近更新:2026-06-04 15:11
- 当前版本:v1
- **主题**(来自用户输入):
  > 根目录下需要创建本项目使用说明文档,应该用极简的语言介绍本项目如何安装和使用的流程,然后再连接到内部具体的使用文档中,同时 CLAUDE.md 是 claude 工具的参考文档,应该放在根目录下。

---

## 1. 需求概述

**为谁**:`code-skills` 仓库的**新访问者**(GitHub 访客 / 第一次接触本项目的开发者 / Claude Code 用户)。

**解决什么问题**:`code-skills` 仓库根目录(2026-06-04 15:10 扫描)目前**无** `README.md` / `CLAUDE.md` / `README.en.md`。访客:
- 看到仓库**无门面**,第一印象差
- 不知道本项目"如何安装 / 如何使用"
- 找不到"详细文档"入口
- `CLAUDE.md`(claude 工具的参考文档)实际在 `plugins/code-skills/CLAUDE.md`,**非**根目录,位置"反直觉"

**带来什么价值**:
1. **门面级 README**:仓库根 `README.md` + `README.en.md`(中英同次提交,`doc-conventions §规则 1`),极简(< 50 行),仅含"简介 + 快速开始 + 详细文档链"
2. **CLAUDE.md 归位**:从 `plugins/code-skills/CLAUDE.md` **移动**到仓库根 `./CLAUDE.md`,符合用户"CLAUDE.md 是 claude 工具的参考文档,应该放在根目录下"的预期
3. **详细文档保留**:`plugins/code-skills/README.md` + `README.en.md` 保留原样,作为"详细技能文档"
4. **清晰两层结构**:仓库根 README = 门面,`plugins/code-skills/README.md` = 详细 — GitHub 项目的标准模式

---

## 2. 背景与目标

### 2.1 背景
- 仓库根 `D:\Workspaces\wm\code-skills/` 含: `.claude/` / `.claude-plugin/` / `.git/` / `.gitignore` / `assistants/` / `plugins/` — **无** `README.md` / `CLAUDE.md`
- `plugins/code-skills/` 已含:
  - `CLAUDE.md`(8,603 bytes,V0.0.1 起由 `code-rule` 维护)
  - `README.md`(36,492 bytes,中文,主语言版本)
  - `README.en.md`(39,947 bytes,英文)
- `assistants/rules/doc-conventions.md §规则 1` / `§规则 2` 是本需求的**强制约束**

### 2.2 业务目标
- **G-1**:在仓库根创建 `README.md` + `README.en.md`(中英同次提交,`§规则 1`)
- **G-2**:仓库根 README **极简**(< 50 行,只含"简介 + 快速开始 + 详细文档链")
- **G-3**:将 `plugins/code-skills/CLAUDE.md` **移动**到仓库根 `./CLAUDE.md`(git `mv` 操作)
- **G-4**:移动后 `plugins/code-skills/CLAUDE.md` **不保留**(用户原文强调"应该放在根目录下")
- **G-5**:`plugins/code-skills/README.md` + `README.en.md` 保留(作为"详细技能文档")

### 2.3 本次目标
- 创建 `./README.md`(仓库根,中文)
- 创建 `./README.en.md`(仓库根,英文,**同次提交**)
- 移动 `./plugins/code-skills/CLAUDE.md` → `./CLAUDE.md`(git `mv` 操作)
- **不**修改 `plugins/code-skills/README.md` / `README.en.md`
- **不**修改 `marketplace.json` / `plugin.json`
- **不**修改 `assistants/rules/` 下任何规范文件
- 严格遵循 `doc-conventions §规则 1`(中英对仗)和 `§规则 2`(README 核心小节)
- 严格遵循 `skill-conventions.md §规则 1`(本需求**不**涉及 SKILL.md,但 FR-2 移动 CLAUDE.md 时保留其 YAML frontmatter 若有)

---

## 3. 用户角色与场景

### 3.1 角色
- **R-1 新访客**:第一次访问 `code-skills` GitHub 仓库,期望"快速了解项目 + 安装使用"
- **R-2 Claude Code 用户**:期望 `CLAUDE.md` 在仓库根,以便 Claude Code 自动读取
- **R-3 详细研究者**:需要看每个技能的详细说明,会跳到 `plugins/code-skills/README.md`

### 3.2 关键场景

#### S-1:新访客浏览仓库(主流程)
- 场景:R-1 访问 `https://github.com/wm123450405/code-skills`
- 期望:
  - GitHub 自动渲染根目录的 `README.md` → 用户立即看到"项目是什么 + 怎么用"
- 本需求落地后:
  - 仓库根有 `README.md`(中文)+ `README.en.md`(英文)
  - 极简(< 50 行)
  - 含"简介 / 快速开始 / 详细文档链"

#### S-2:Claude Code 自动读取 CLAUDE.md(主流程)
- 场景:R-2 在 `code-skills` 仓库目录下用 Claude Code
- 期望:Claude Code 自动读根目录 `./CLAUDE.md`
- 本需求落地后:
  - 仓库根 `./CLAUDE.md` 存在
  - 内容与原 `plugins/code-skills/CLAUDE.md` 一致(8,603 bytes)
  - Claude Code 自动发现并使用

#### S-3:详细研究者跳到子文档
- 场景:R-3 在根 README 看到"详细文档"链,跳到 `plugins/code-skills/README.md`
- 期望:详细文档完整(36,492 bytes)
- 本需求落地后:
  - `plugins/code-skills/README.md` **保留**原样
  - 仓库根 README 链到它:`📖 详细文档:./plugins/code-skills/README.md`

#### S-4:git 移动 CLAUDE.md(主流程)
- 操作:
  ```bash
  git mv plugins/code-skills/CLAUDE.md CLAUDE.md
  git commit -m "chore(repo): move CLAUDE.md to repo root (REQ-000012)"
  ```
- 效果:
  - git 历史显示 move(而非 delete + add)
  - blame 信息保留

#### S-5:中英 README 对仗同步
- 场景:本需求**同时**创建 `README.md`(中文)+ `README.en.md`(英文)
- 遵循 `doc-conventions §规则 1`:两个文件章节结构**对仗**

#### S-6:无激活版本(边界)
- 场景:用户输入 `/code-require REQ-00012`,但 `.current-version` 不存在
- 处理:同其他 11 个技能,提示调 `code-version`

---

## 4. 功能需求(FR)

### FR-1:创建仓库根 `README.md`(中文)

- **描述**:在仓库根 `./README.md` 创建极简中文 README
- **优先级**:必须
- **AC**:
  - AC-1.1:文件路径 = `./README.md`(仓库根)
  - AC-1.2:文件长度 < 50 行
  - AC-1.3:含核心小节(简介 / 快速开始 / 详细文档链)(`§规则 2` 强制约束)
  - AC-1.4:不复制 `plugins/code-skills/README.md` 的详细内容(Q-1 锁定 A)
  - AC-1.5:含"📖 详细文档"链指向 `./plugins/code-skills/README.md`

### FR-2:创建仓库根 `README.en.md`(英文)

- **描述**:在仓库根 `./README.en.md` 创建极简英文 README
- **优先级**:必须
- **AC**:
  - AC-2.1:文件路径 = `./README.en.md`(仓库根)
  - AC-2.2:与 `README.md` **同时**创建(`§规则 1` 同次提交)
  - AC-2.3:与 `README.md` 章节结构**对仗**(`§规则 1`)
  - AC-2.4:文件长度 < 50 行

### FR-3:移动 `plugins/code-skills/CLAUDE.md` → `./CLAUDE.md`

- **描述**:将 `plugins/code-skills/CLAUDE.md` **移动**到仓库根,原位置**不保留**
- **优先级**:必须
- **AC**:
  - AC-3.1:使用 `git mv` 操作(保留 git blame)
  - AC-3.2:仓库根 `./CLAUDE.md` 存在
  - AC-3.3:`plugins/code-skills/CLAUDE.md` **不**存在(Q-3 锁定 A)
  - AC-3.4:仓库根 `./CLAUDE.md` 内容与原 `plugins/code-skills/CLAUDE.md` **完全一致**(8,603 bytes)
  - AC-3.5:若有 YAML frontmatter,完整保留(`skill-conventions §规则 1`)

### FR-4:保留 `plugins/code-skills/README.md` + `README.en.md`

- **描述**:`plugins/code-skills/README.md` + `README.en.md` 保留原样,作为"详细技能文档"
- **优先级**:必须
- **AC**:
  - AC-4.1:`plugins/code-skills/README.md` **不**被本需求修改
  - AC-4.2:`plugins/code-skills/README.en.md` **不**被本需求修改
  - AC-4.3:仓库根 README "📖 详细文档"链指向它们

### FR-5:不修改其他文件

- **描述**:本需求**只**新建 2 个文件 + 移动 1 个文件;其他文件**不**被本需求修改
- **优先级**:必须
- **AC**:
  - AC-5.1:`marketplace.json` / `plugin.json` **不**被本需求修改
  - AC-5.2:`assistants/rules/` 下任何规范文件**不**被本需求修改
  - AC-5.3:`plugins/code-skills/skills/*/SKILL.md` **不**被本需求修改
  - AC-5.4:中英 README 创建**同次提交**(`doc-conventions §规则 1`)
  - AC-5.5:`CLAUDE.md` 移动**与** README 创建**可同次提交或分次提交**(不强求)

### FR-6:`doc-conventions §规则 1` / `§规则 2` 强制约束

- **描述**:本需求**严格**遵循 `doc-conventions.md`
- **优先级**:必须
- **AC**:
  - AC-6.1:中英 README 同次提交(`§规则 1`)
  - AC-6.2:中英 README 章节结构对仗(`§规则 1`)
  - AC-6.3:仓库根 README 必含"简介 / 安装 / 使用 / 能力"等核心小节(`§规则 2`)
  - AC-6.4:引用命令/路径/版本号与仓库实际状态一致(`§规则 2`)

### FR-7:报告与建议

- **描述**:`code-require` 完成时向用户报告
- **优先级**:必须
- **AC**:
  - AC-7.1:完成时,屏幕输出"REQ-00012 需求分析完成"
  - AC-7.2:汇报新建文件路径(根 README + 根 README.en.md)
  - AC-7.3:汇报移动文件(`plugins/code-skills/CLAUDE.md` → `./CLAUDE.md`)

---

## 5. 非功能需求 / 约束(NFR)

### NFR-1:零新增依赖
- **描述**:不引入新依赖
- **强制级别**:必须

### NFR-2:极简(< 50 行)
- **描述**:仓库根 README 文件长度 < 50 行
- **强制级别**:必须
- **理由**:用户原话"极简的语言"

### NFR-3:git mv 保留历史
- **描述**:`CLAUDE.md` 移动用 `git mv` 操作,保留 git blame 历史
- **强制级别**:必须
- **理由**:避免历史 commit 的 blame 断裂

### NFR-4:不破坏现有结构
- **描述**:本需求不修改现有 `plugins/code-skills/CLAUDE.md` 的内容(只是移动位置)
- **强制级别**:必须

### NFR-5:与 9 个 `code-*` 技能协同 0 冲突
- **描述**:本需求不修改任何 `code-*` 技能
- **强制级别**:必须

### NFR-6:不修改 `doc-conventions.md`
- **描述**:本需求**不**修改 `doc-conventions.md`(虽强制遵循,但**不**改规则文件本身)
- **强制级别**:必须

### NFR-7:`commit-conventions.md` 兼容
- **描述**:本需求 commit 消息遵循 `commit-conventions.md` 既有 1 行习惯
- **强制级别**:必须
- **示例**:`chore(repo): move CLAUDE.md to repo root (REQ-00012)`

### NFR-8:不提供"自动重定向"逻辑
- **描述**:`plugins/code-skills/CLAUDE.md` 移动后**不**新建"重定向"文件(如软链 / 占位)
- **强制级别**:必须
- **理由**:Claude Code 在 `plugins/code-skills/` 目录工作时**不应**误读根目录的 `CLAUDE.md`

---

## 6. 页面与界面(模板节选)

### 6.1 仓库根 `README.md` 模板(中文,< 50 行)

```markdown
# code-skills

> 面向 AI 协作的项目管理 + 编码工作流工具集(基于 Claude Code)。

## 简介

`code-skills` 是一组 Claude Code 技能,覆盖需求分析 → 概要设计 → 详细设计 → 编码 → 单测 → 评审 → 发布的完整开发周期。

## 快速开始

1. 添加 marketplace:
   ```
   claude plugin marketplace add https://github.com/wm123450405/code-skills.git
   ```
2. 安装插件:
   ```
   claude plugin install code-skills@code-skills
   ```
3. 在项目中调用首个技能:
   ```
   /code-version V0.0.0
   /code-require "添加用户登录功能"
   ```

## 主要能力

| 技能 | 用途 |
| --- | --- |
| `code-version` | 版本工作空间管理 |
| `code-require` | 需求分析 |
| `code-design` | 概要设计 |
| `code-plan` | 详细设计 + 任务拆分 |
| `code-it` | 任务编码 |
| `code-unit` | 单元测试 |
| `code-review` | 代码评审 |
| `code-dashboard` | 开发看板 |
| `code-publish` | 发布部署 |
| `code-auto` | 自动开发(编排) |
| `code-rule` | 编码规范管理 |

## 📖 详细文档

完整技能说明、安装细节、版本管理:[./plugins/code-skills/README.md](./plugins/code-skills/README.md)

## 许可证

[MIT](LICENSE)
```

### 6.2 仓库根 `README.en.md` 模板(英文,< 50 行)

```markdown
# code-skills

> A suite of Claude Code skills for AI-assisted project management and development workflow.

## Introduction

`code-skills` is a set of Claude Code skills covering the full development cycle: requirements → design → planning → coding → unit tests → review → release.

## Quick Start

1. Add the marketplace:
   ```
   claude plugin marketplace add https://github.com/wm123450405/code-skills.git
   ```
2. Install the plugin:
   ```
   claude plugin install code-skills@code-skills
   ```
3. Invoke the first skill in your project:
   ```
   /code-version V0.0.0
   /code-require "Add user login feature"
   ```

## Main Capabilities

| Skill | Purpose |
| --- | --- |
| `code-version` | Version workspace management |
| `code-require` | Requirements analysis |
| `code-design` | High-level design |
| `code-plan` | Detailed design + task breakdown |
| `code-it` | Task coding |
| `code-unit` | Unit tests |
| `code-review` | Code review |
| `code-dashboard` | Dev dashboard |
| `code-publish` | Release deployment |
| `code-auto` | Automated development (orchestrator) |
| `code-rule` | Coding conventions |

## 📖 Detailed Documentation

Full skill descriptions, installation details, version management:[./plugins/code-skills/README.md](./plugins/code-skills/README.md)

## License

[MIT](LICENSE)
```

### 6.3 `CLAUDE.md` 移动

```bash
# 单次 commit 内可同时执行:
git mv plugins/code-skills/CLAUDE.md CLAUDE.md
git add README.md README.en.md
git commit -m "chore(repo): add root README/README.en.md, move CLAUDE.md to root (REQ-00012)"
```

---

## 7. 交互逻辑

### 7.1 本需求落地流程

```
[code-require REQ-00012 完成]
  ↓
[code-design REQ-00012(后续)]
  ↓
[code-plan REQ-00012(后续)]
  ↓
[code-it(用户手动 / code-auto 编排)执行]
  ↓
  ├─ 创建 ./README.md(Q-1 锁定 A,极简)
  ├─ 创建 ./README.en.md(同次提交)
  ├─ git mv plugins/code-skills/CLAUDE.md → ./CLAUDE.md
  └─ git commit(同次或分次)
  ↓
[code-review REQ-00012]
  ↓
[code-publish 或后续]
```

### 7.2 git 操作序列

```
[工作树:plugins/code-skills/CLAUDE.md 存在,根目录无 CLAUDE.md]
  ↓
[git mv plugins/code-skills/CLAUDE.md CLAUDE.md]
  ↓
[git status]
  ├─ renamed: plugins/code-skills/CLAUDE.md → CLAUDE.md
  └─ (新文件:README.md, README.en.md 待 add)
  ↓
[git add README.md README.en.md]
  ↓
[git commit -m "..."]
  ↓
[git log --follow CLAUDE.md]  # 可见历史(因 git mv 保留)
```

---

## 8. 数据与状态

### 8.1 仓库根目录文件结构(本需求落地后)

```
D:\Workspaces\wm\code-skills\  # 仓库根
├── .claude/
├── .claude-plugin/
├── .git/
├── .gitignore
├── assistants/
├── plugins/
├── CLAUDE.md            # 本需求移动自 plugins/code-skills/CLAUDE.md
├── README.md            # 本需求新建
└── README.en.md         # 本需求新建
```

### 8.2 plugins/code-skills/ 文件结构(本需求落地后,**CLAUDE.md 消失**)

```
D:\Workspaces\wm\code-skills\plugins\code-skills\
├── .claude-plugin/
├── CLAUDE.md            # ← 本需求移动走(原位置不再保留)
├── README.md            # 保留(详细技能文档)
├── README.en.md         # 保留
└── skills/
    └── ...
```

### 8.3 `doc-conventions §规则 1` 同步约束

| 中文 README | 英文 README | 必须同步 |
| --- | --- | --- |
| `# code-skills` | `# code-skills` | 标题 |
| `## 简介` | `## Introduction` | 1 级章节 |
| `## 快速开始` | `## Quick Start` | 2 级章节 |
| `## 主要能力` | `## Main Capabilities` | 3 级章节 |
| `## 📖 详细文档` | `## 📖 Detailed Documentation` | 4 级章节 |
| `## 许可证` | `## License` | 5 级章节 |

---

## 9. 边界与异常

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | 无 `.current-version` | 提示调 `code-version`,退出 |
| **E-2** | `plugins/code-skills/CLAUDE.md` 不存在(被前置需求删除) | 报错,"无 CLAUDE.md 可移动" |
| **E-3** | 仓库根 `./CLAUDE.md` 已存在 | 报错,"目标已存在,无法移动" |
| **E-4** | 仓库根 `./README.md` 已存在 | 报错,"目标已存在,无法新建" |
| **E-5** | 仓库根 `./README.en.md` 已存在 | 报错,"目标已存在,无法新建" |
| **E-6** | `git mv` 失败(权限等) | 报错退出,用户手动处理 |
| **E-7** | 用户希望"移动 + 软链"组合(根 + 软链) | **不**支持(NFR-8 锁定)— 单一来源 |
| **E-8** | 中英 README 章节不对仗 | `code-review` 应发现(`§规则 1` 强制) |
| **E-9** | 仓库根 README 超 50 行 | `code-review` 应发现(NFR-2 强制) |

---

## 10. 验收标准(AC 总览)

按 FR 编号归类,合计 ~25 条:

- **FR-1**(5 条):AC-1.1 ~ AC-1.5
- **FR-2**(4 条):AC-2.1 ~ AC-2.4
- **FR-3**(5 条):AC-3.1 ~ AC-3.5
- **FR-4**(3 条):AC-4.1 / AC-4.2 / AC-4.3
- **FR-5**(5 条):AC-5.1 ~ AC-5.5
- **FR-6**(4 条):AC-6.1 ~ AC-6.4
- **FR-7**(3 条):AC-7.1 / AC-7.2 / AC-7.3
- **NFR-1**(1 条):零依赖
- **NFR-2**(1 条):极简 < 50 行
- **NFR-3**(1 条):git mv 保留历史
- **NFR-4**(1 条):不破坏现有结构
- **NFR-5**(1 条):与 9 技能 0 冲突
- **NFR-6**(1 条):不修改 doc-conventions
- **NFR-7**(1 条):commit 消息遵循规范
- **NFR-8**(1 条):不提供重定向

**总计**:约 25 条 AC。

---

## 11. 关联需求

| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| **REQ-00001**(V0.0.1) | `plugins/code-skills/README.md` 是 V0.0.1 主语言版本 | 本需求落地后:**仓库根 README 是新主语言版本** | `./assistants/V0.0.1/require/REQ-00001/RESULT.md` |
| **REQ-00003**(V0.0.1) | `code-rule` 维护 `doc-conventions.md` | FR-6 强制遵循 §规则 1 / §规则 2 | `./assistants/rules/doc-conventions.md` |
| **REQ-00004~00011**(V0.0.2) | 8 个 V0.0.2 需求 | FR-4 + FR-5:**不**触发这些需求修改 | `./assistants/V0.0.2/require/REQ-*/RESULT.md` |
| **REQ-00002**(V0.0.1) | `encoding-conventions.md` | 不影响 | `./assistants/V0.0.1/require/REQ-00002/RESULT.md` |

详细关联分析见 `related-requirements.md`。

---

## 12. 待澄清 / 未决项(本轮未处理 / 留作默认)

### Q-4:与 `doc-conventions.md` 协同
- **状态**:采纳默认(§规则 1 / §规则 2 强制)

### Q-5:"极简"的具体含义
- **状态**:采纳默认(< 50 行,只含"简介 + 快速开始 + 详细文档链")

### Q-6:与 REQ-00003 / REQ-00005~00011 协同
- **状态**:采纳默认(不触发 `code-rule` 升级,不修改 SKILL.md)

### Q-7:与 9 个 `code-*` 技能的关系
- **状态**:采纳默认(根 README 简述 9 技能,详细指向子 README)

### Q-8:`.gitignore` 是否需要更新
- **状态**:采纳默认(不需更新)

### Q-9(新增):派生任务预警
- **建议派生**:
  - "用 `code-rule` 沉淀 '仓库根 README 与子目录 README 关系' 约定"(由 `code-review` 决定)
  - "`code-design` 升级:在 §6 页面与界面 中说明 '仓库门面 README' 模板"(由 `code-review` 决定)
- **状态**:本需求不阻塞

---

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-04 15:11 | v1 | 初始创建:7 FR / 8 NFR / ~25 AC / 9 个边界场景;Q-1/Q-2/Q-3 锁定,Q-4~Q-8 留默认/未采用;用户原文**无笔误**;Q-1 锁定"**只极简概览 + 链到详情**"(仓库根 README 是门面,`plugins/code-skills/README.md` 是详细);Q-2 锁定"**移动到根目录**"(`plugins/code-skills/CLAUDE.md` → `./CLAUDE.md`);Q-3 锁定"**不保留原位置**";FR-3 AC-3.1 显式 `git mv` 保留 git blame;FR-6 严格遵循 `doc-conventions §规则 1` (中英同次提交 + 章节对仗) / `§规则 2` (核心小节覆盖);NFR-2 < 50 行;NFR-3 git mv 保留历史;NFR-8 不提供重定向/软链 | wangmiao |
