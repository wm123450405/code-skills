# 材料登记 — REQ-00005

更新时间:2026-06-04 13:32

| 文件路径 | 类型 | 用途 | 读取状态 | 关键摘要 |
| --- | --- | --- | --- | --- |
| (无文件材料) | 用户口头描述 | 唯一需求来源 | 已读 | 见下方"原始材料"段 |

## 原始材料

> 来源:用户调用 `/code-skills:code-require` 时在 ARGUMENTS 中提供(2026-06-04 13:32)。
>
> **完整原文**:
> > 优化需求: 优化 `/code-require`、`/code-desgin`、`/code-plan` 技能,增加技能开始第一步为拉去最新代码(`/core-require` 技能额外增加拉起代码后检查最新代码中的工作版本号是否与当前上下文中的工作版本号一致,不一致要中断后续操作并向用户确认具体应该选择的工作版本号,并利用 `/code-version` 技能切换工作版本号到上下文中),以及增加技能最后一步提交所有生成或修改的文件。

## 关键信息抽取(供后续步骤使用)

### 1. 用户原文中的笔误纠正
- `/code-desgin` → **`/code-design`**(用户原文笔误)
- `/core-require` → **`/code-require`**(用户原文笔误)
- 确认范围:**`code-require` / `code-design` / `code-plan` 三个技能**(对应"上游→中游→下游"管道的前三步)

### 2. 核心需求拆解
- **步骤 0(新增,所有 3 技能通用)**:
  - 拉取最新代码(默认从 `git pull` / 类似机制)
  - **位于现有"版本上下文检测"步骤之前**
- **步骤 0a(`code-require` 额外专属)**:
  - 拉取后,检查最新代码中的工作版本号(`.current-version` 文件)是否与"当前上下文"中的工作版本号一致
  - 不一致 → **中断后续操作** + 向用户确认目标版本
  - 用 `/code-version` 技能切换到"上下文中"的版本
- **步骤 N(新增,所有 3 技能通用,位于末尾)**:
  - 提交所有生成或修改的文件

### 3. "拉取最新代码"边界
- **底层命令**:`git pull`(默认 upstream/tracking 分支)
- **失败处理**:冲突 / 网络失败 / 无 remote 等异常需明文处理
- **本地 dirty 树**:已有未提交修改时,git pull 会失败或冲突 — 需明确策略(用户原文未提)

### 4. "提交所有生成或修改的文件"边界
- **底层命令**:`git add` + `git commit`
- **commit message 生成**:与 `commit-conventions.md`(当前为空占位)的关系
- **与现有流程的关系**:现有 7 个 `code-*` 技能中,部分任务已有"提交"动作(`code-it` 显式 commit,`code-fix` 等不显式),需统一为"末尾必做"
- **`.gitignore` / 不应提交的文件**:需明确

### 5. "code-require 额外的中断"边界
- **中断 = 不继续后续步骤**:退出"步骤 0a"后不再进入"步骤 1 收集需求编码"
- **恢复路径**:用户用 `code-version` 切版本后,需重跑 `code-require`
- **歧义点**:用户原话"利用 `/code-version` 技能切换工作版本号到上下文中" — 这里的"上下文中"指:
  - (a) 启动 `code-require` 时用户口头指定的版本?
  - (b) 拉取后远端实际指向的版本?
  - (c) 用户当下应选择的目标?
  - 见 clarifications.md Q-1

### 6. 受影响技能的范围
- **直接修改**:`code-require/SKILL.md` + `code-design/SKILL.md` + `code-plan/SKILL.md`
- **可能影响**:
  - `code-version/SKILL.md`(被复用,需保证对外接口稳定)
  - `commit-conventions.md`(若需求落地,需补"自动 commit 信息"规则)
  - `code-it` / `code-unit` / `code-review` 的现有 commit 行为(避免冲突)
- **不修改**:`marketplace.json` / `plugin.json` / 其他 SKILL.md frontmatter

### 7. 待澄清(在 clarifications.md 中展开)
- Q-1:`code-require` 检测到版本不一致时,目标版本如何选?
- Q-2:`git pull` 失败时的处理策略?
- Q-3:`git pull` 时本地 dirty 树的处理?
- Q-4:末尾"提交"步骤的 commit message 生成方式?
- Q-5:末尾提交与已有"代码改修正文"(如 `code-it` 的 work-log/deviations)的提交是否合并?
