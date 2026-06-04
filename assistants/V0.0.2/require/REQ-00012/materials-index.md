# 材料登记 — REQ-00012

更新时间:2026-06-04 15:10

| 文件路径 | 类型 | 用途 | 读取状态 | 关键摘要 |
| --- | --- | --- | --- | --- |
| (无文件材料) | 用户口头描述 | 唯一需求来源 | 已读 | 见下方"原始材料"段 |
| 仓库根目录扫描 | Bash | 现状 | 已读 | 仓库根 `D:\Workspaces\wm\code-skills\` 无 `README.md` / `CLAUDE.md` |
| `plugins/code-skills/` | Bash | 现状 | 已读 | 含 `CLAUDE.md`(8,603 bytes)+ `README.md`(36,492 bytes)+ `README.en.md`(39,947 bytes) |

## 原始材料

> 来源:用户调用 `/code-skills:code-require` 时在 ARGUMENTS 中提供(2026-06-04 15:10)。
>
> **完整原文**:
> > 根目录下需要创建本项目使用说明文档,应该用极简的语言介绍本项目如何安装和使用的流程,然后再连接到内部具体的使用文档中,同时 CLAUDE.md 是 claude 工具的参考文档,应该放在根目录下。

## 关键信息抽取(供后续步骤使用)

### 1. 用户原文笔误纠正
- 本轮**无笔误**

### 2. 核心需求拆解
- **现状**(2026-06-04 15:10 扫描):
  - 仓库根 `D:\Workspaces\wm\code-skills\` 含: `.claude/` / `.claude-plugin/` / `.git/` / `.gitignore` / `assistants/` / `plugins/`
  - **无**根目录 `README.md` / **无**根目录 `CLAUDE.md`
  - `plugins/code-skills/` 已含: `CLAUDE.md`(8,603 bytes)+ `README.md`(36,492 bytes)+ `README.en.md`(39,947 bytes)
- **本需求**:
  - **本项目使用说明文档**:在根目录创建,**极简**语言,介绍"如何安装和使用的流程" + 链到内部具体使用文档
  - **`CLAUDE.md` 是 claude 工具的参考文档,应该放在根目录下**:用户明确要求 `CLAUDE.md` 在根目录
- **关键决策点**:
  - "根目录"指 `D:\Workspaces\wm\code-skills/`(仓库根)
  - `CLAUDE.md` 是移动(从 `plugins/code-skills/CLAUDE.md` → 仓库根)还是新建?
  - 现有 `plugins/code-skills/README.md` + `README.en.md` 的命运?

### 3. 关键边界
- **"本项目使用说明文档"的位置**:
  - 选项 A:仓库根 `./README.md` + `./README.en.md`(`doc-conventions §规则 1` 中英同次提交)
  - 选项 B:仓库根 `./README.md`(只英文) + 链到 `plugins/code-skills/README.md`
  - 选项 C:仓库根 `./README.md` + 链到内部所有 `code-*` 技能的 SKILL.md
- **"极简"的程度**:
  - 选项 A:仅 1 个安装命令 + 1 个使用命令(最短)
  - 选项 B:含 1 段简介 + 1 段安装 + 1 段使用 + 1 段"详细文档"链(中)
  - 选项 C:含 1 段简介 + 1 段快速开始 + 1 段 FAQ(长)
- **`CLAUDE.md` 在根目录的命运**:
  - 选项 A:从 `plugins/code-skills/CLAUDE.md` 移动到仓库根
  - 选项 B:在仓库根**新建** `CLAUDE.md`(包含与 `plugins/code-skills/CLAUDE.md` 相同内容或精简版)
  - 选项 C:`plugins/code-skills/CLAUDE.md` 保留 + 仓库根 `CLAUDE.md` 引用前者
- **现有 `plugins/code-skills/README.md` / `README.en.md` 的命运**:
  - 选项 A:保留(用户原话"再连接到内部具体的使用文档中"——可能指这些)
  - 选项 B:删除(被仓库根 README 替代)
  - 选项 C:仓库根 README 仅指向 `plugins/code-skills/README.md`,后者保留原样
- **与 `code-skills` 已有 `README.md` 的关系**:
  - 仓库根 README 是"门面",`plugins/code-skills/README.md` 是"详细"
  - 这是 GitHub 项目的标准两层 README 模式

### 4. 与现有规范/看板的关系
- **`doc-conventions.md §规则 1`**:中英 README 必须结构对仗,改一边需同步另一边
  - 本需求若**新建**仓库根 README,需同时新建 `README.md` + `README.en.md`
- **`code-rule` 维护项目级规范**:本需求**不**直接写新规范(留作 follow-up)
- **看板 `dashboard-conventions §规则 1`**:本需求**不**修改看板(零规范变更)

### 5. 待澄清(在 clarifications.md 中展开)
- Q-1:仓库根 README 是"全新内容"还是"指向 plugins/code-skills/README.md"?
- Q-2:"极简"程度(1-3 段)
- Q-3:`CLAUDE.md` 在根目录 = 移动 / 新建 / 引用
- Q-4:`plugins/code-skills/CLAUDE.md` 移动后是否保留副本
- Q-5:`plugins/code-skills/README.md` + `README.en.md` 保留 / 删除 / 被替代
