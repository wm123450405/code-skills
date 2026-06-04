# 需求提示词文档 — REQ-00005(优化 `/code-require` / `/code-design` / `/code-plan`,增加"首步拉取最新代码"与"末步兜底提交")

- 需求编码:REQ-00005
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-04
- 最近更新:2026-06-04 13:33
- 当前版本:v1
- **主题**(来自用户输入):
  > 优化需求: 优化 `/code-require`、`/code-desgin`(笔误 → `/code-design`)、`/code-plan` 技能,增加技能开始第一步为拉去最新代码(`/core-require`(笔误 → `/code-require`)技能额外增加拉起代码后检查最新代码中的工作版本号是否与当前上下文中的工作版本号一致,不一致要中断后续操作并向用户确认具体应该选择的工作版本号,并利用 `/code-version` 技能切换工作版本号到上下文中),以及增加技能最后一步提交所有生成或修改的文件。

---

## 1. 需求概述

**为谁**:`code-skills` 仓库的 AI 协作者(在长会话/多设备/多副本之间),以及项目主导者(需要在每次技能调用前后保证"工作上下文"是新鲜的,且不遗漏任何生成文件)。

**解决什么问题**:当前 7 个 `code-*` 技能的工作流有两个**长期隐患**:

1. **未拉取最新代码就开干** — 用户在多设备/多副本之间切换时,本地的 `./assistants/.current-version` / 看板 / 模板可能落后于远端;若直接调 `code-require`,可能在"陈旧上下文"中工作,产生与远端已变更的需求冲突
2. **末尾可能漏提交** — 某些技能(如 `code-fix`、`code-review`)在执行过程中产生"过程文档"(`work-log.md` / `deviations.md` / `findings-no-task.md` 等),但内部不显式 `git commit`;若用户忘记在最后手动提交,会遗留 dirty tree
3. **`code-require` 特定问题** — 即使本地 `.current-version` 与远端一致,在"上下文陈旧"时也可能拉到一个**用户没注意到的版本切换**(例如:同事刚 `code-version V0.0.3`,但本机还停在 V0.0.2)

**带来什么价值**:
1. **新鲜保证**:每个技能启动时,先 `git pull` 拿到最新代码,再开始业务逻辑
2. **版本对齐**:`code-require` 额外检查 `.current-version` 一致性,不一致时主动澄清 + 切换,避免"在错误版本上工作"
3. **零遗漏**:末尾兜底提交确保"过程文件 + 结果文件"全部入库,不留 dirty tree

---

## 2. 背景与目标

### 2.1 背景
- `code-skills` 7 个技能的工作流管道:`code-version` → `code-require` → `code-design` → `code-plan` → `code-it` → `code-unit` → `code-review`
- **现状(从 V0.0.1 看板推断)**:每个任务显式 commit(`code-it` 内部 `git add` + `git commit`),但**过程文档**常不 commit(留 dirty tree)
- **现状(`code-require`)**:无首步拉取;无版本对齐检查;仅读本地 `.current-version`
- **现状(`code-design` / `code-plan`)**:无首步拉取;依赖 `code-require` 之后的"已拉取"假设(但**没有强制约束**)
- **风险 1:多设备/多副本**:用户在 A 设备切到 `V0.0.3`,在 B 设备仍停留 `V0.0.2`;B 设备调 `code-require` 会基于"过时上下文"工作
- **风险 2:过程文档遗漏**:`code-it` 的 `deviations.md` / `compile-and-run.md` / `test-results.md` 等常被遗漏 commit
- **风险 3:上下游污染**:`code-require` 写了 V0.0.2 的需求后,`code-design` 在 V0.0.3 上下文运行,会出现"需求不存在 / 路径找不到"

### 2.2 业务目标
- **G-1**:3 个技能(`code-require` / `code-design` / `code-plan`)在"步骤 0 版本上下文检测"**之前**新增"步骤 0a 拉取最新代码"
- **G-2**:`code-require` 在拉取后,新增"步骤 0b 工作版本号对齐检查",不一致时主动中断 + 询问用户 + 自动调 `code-version` 切换
- **G-3**:3 个技能在"末尾"新增"步骤 N 兜底提交",覆盖所有"过程文件 + 结果文件"
- **G-4**:`code-it` 内部 commit 行为**不变**(用户 Q-4 锁定 B);末尾兜底提交与之并存,聚焦"非 `code-it` 任务级 commit"覆盖的文件

### 2.3 本次目标
- 修改 `plugins/code-skills/skills/code-require/SKILL.md` 正文(不改 frontmatter)
- 修改 `plugins/code-skills/skills/code-design/SKILL.md` 正文(不改 frontmatter)
- 修改 `plugins/code-skills/skills/code-plan/SKILL.md` 正文(不改 frontmatter)
- 严格遵循 `skill-conventions.md §规则 1`(frontmatter 不变)
- 严格遵循 `commit-conventions.md`(虽为占位,本需求**不**直接填充规则)
- 不修改 `marketplace.json` / `plugin.json` / 其他 4 个 `code-*` 技能的 SKILL.md(`code-version` / `code-it` / `code-unit` / `code-review`)
- 不修改 `code-it` 内部 commit 逻辑
- 不修改 `commit-conventions.md` 规则(留作 follow-up)
- 不修改 CLAUDE.md 的"AI 工作约定"小节(留作 follow-up)

---

## 3. 用户角色与场景

### 3.1 角色
- **R-1 多设备协作者**:在 A 设备切了 `V0.0.3`,在 B 设备停留 `V0.0.2` — 需要拉取 + 版本对齐
- **R-2 长会话 AI**:一次会话中调 `code-require` 多次,需要保证"每次都是最新上下文"
- **R-3 项目主导者**:每个工作日/会话开头,先调任一 `code-*` 技能,期望"git status 干净 + 远端已同步"

### 3.2 关键场景

#### S-1:多设备场景(主流程,`code-require`)
- 用户输入:`/code-require REQ-00006`(本机停留 V0.0.2,但远端已 V0.0.3)
- 技能执行:
  1. **步骤 0a**:`git pull`(成功)
  2. **步骤 0b**:对比远端 `.current-version` = `V0.0.3` 与本地(本机刚被 pull 覆盖 = V0.0.3),发现**实际**用户口头指定的 `REQ-00006` 在 V0.0.2 不存在
  3. 提示用户:
     ```
     ✗ 检测到上下文版本不一致
     本地(拉取后):V0.0.2
     远端:.current-version = V0.0.3
     需求 REQ-00006 在 V0.0.2 中不存在,但在 V0.0.3 中已存在
     ```
  4. 用 `AskUserQuestion` 提供选项:
     - A. 切到 V0.0.3 后继续(推荐)
     - B. 在 V0.0.2 中重新创建 REQ-00006
     - C. 取消
  5. 选 A → 调 `code-version V0.0.3` 切换 → 用户需重跑 `code-require`

#### S-2:本地与远端一致(主流程,`code-require`)
- 用户输入:`/code-require REQ-00005`(本机 V0.0.2,远端 V0.0.2)
- 技能执行:
  1. **步骤 0a**:`git pull`(no-op)
  2. **步骤 0b**:对比一致 → 直接进入步骤 1(收集需求编码)
  3. 正常完成需求分析
  4. **步骤 N**:末尾兜底提交
     - `git add` 所有"过程文件"(materials-index.md / clarifications.md / related-requirements.md)+ "结果文件"(RESULT.md)
     - 预览 commit message:
       ```
       chore(code-require): REQ-00005 需求分析完成
       
       新增 10 FR / 7 NFR / 30 AC,过程文档 3 文件,结果文件 1 文件
       ```
     - 用户确认 → `git commit`

#### S-3:`git pull` 冲突(边界)
- 用户输入:`/code-design REQ-00001`(本地有未推送的 V0.0.1 改动,远端有别人推的 V0.0.2 改动)
- 技能执行:
  1. **步骤 0a**:`git pull` → 冲突(用户原文未提的细节场景,但符合常识)
  2. **按 Q-2 锁定 A**:中断 + 报错退出
  3. 用户看到:
     ```
     ✗ git pull 失败:存在未解决的冲突
       冲突文件:<...>
       请手动解决冲突后,重跑该技能
     ```

#### S-4:`code-design` / `code-plan` 的简化首步
- 用户输入:`/code-design REQ-00005`(本机 V0.0.2,远端 V0.0.2)
- 技能执行:
  1. **步骤 0a**:`git pull`(no-op)— **不**做版本对齐(只有 `code-require` 专属)
  2. 直接进入原有"步骤 0 版本上下文检测"
  3. 后续流程不变
  4. **步骤 N**:末尾兜底提交(同 S-2)

#### S-5:末尾兜底提交"无文件变更"
- 用户输入:`/code-require REQ-00005`,过程中无任何写入(仅澄清 + 退出)
- 技能执行:
  - **步骤 N**:`git status --porcelain` 空 → 跳过 commit,打印 `无文件变更,跳过末尾提交`

#### S-6:commit 失败
- 用户输入:末尾提交时,git 因 pre-commit hook 失败
- 技能执行:
  - `git commit` 退出码非 0
  - 打印 stderr
  - **不重试**(可能阻塞用户)
  - 用户看到:
    ```
    ✗ 末尾提交失败,文件已暂存
      退出码:1
      错误:<...>
      请手动处理后,执行 git commit
    ```

---

## 4. 功能需求(FR)

### FR-1:3 个技能新增"步骤 0a 拉取最新代码"

- **描述**:`code-require` / `code-design` / `code-plan` 在原有"步骤 0 版本上下文检测"**之前**,新增"步骤 0a:拉取最新代码",执行 `git pull`
- **优先级**:必须
- **位置**:
  - `code-require/SKILL.md` 工作流管道"步骤 0 之前"
  - `code-design/SKILL.md` 工作流管道"步骤 0 之前"
  - `code-plan/SKILL.md` 工作流管道"步骤 0 之前"
- **AC**:
  - AC-1.1:3 个技能的 SKILL.md 在"步骤 0"前显式列出"步骤 0a:拉取最新代码"
  - AC-1.2:步骤 0a 的执行命令为 `git pull`(默认 upstream / tracking 分支)
  - AC-1.3:拉取失败的 3 种情况均按 Q-2 锁定 A 处理(中断 + 报错退出,见 §9 E-2/E-3/E-4)
  - AC-1.4:不修改 frontmatter;不修改"步骤 0"及之后的原有内容(增量追加,不重写)

### FR-2:`code-require` 新增"步骤 0b 工作版本号对齐检查"

- **描述**:仅 `code-require` 在"步骤 0a 拉取"之后,新增"步骤 0b 工作版本号对齐检查"
  - 对比"拉取后本地的 `.current-version`"与"用户口头指定/上下文中暗示的目标版本"
  - 不一致 → 中断 + 询问用户(Q-1 锁定 A)
  - 选 "切到远端" → 自动调 `code-version <远端版本>` 切换
  - 切换后,提示用户重跑 `code-require`(因 `code-version` 已执行完毕,不应再自动续跑 `code-require`)
- **优先级**:必须
- **AC**:
  - AC-2.1:`code-require/SKILL.md` 在"步骤 0a"后显式列出"步骤 0b"
  - AC-2.2:对比规则 = "拉取后本地的 `.current-version`" vs "用户原始需求中提到的目标版本(隐式为 `code-version` 读取的版本)"
  - AC-2.3:不一致时,3 选 1 用 `AskUserQuestion`(A 切到远端 / B 在本地版本中重新创建 / C 取消)
  - AC-2.4:选 A 时,执行 `code-version <远端版本>`,确认切换成功后**退出** `code-require`,提示"已切到 X,请重跑 `code-require`"
  - AC-2.5:选 B 时,继续原流程(在本地版本中创建新需求)
  - AC-2.6:选 C 时,退出 `code-require`,无任何文件变更

### FR-3:3 个技能新增"末尾兜底提交"

- **描述**:3 个技能在"原有最后一步"之后,新增"步骤 N 兜底提交"
  - 收集本技能**本次执行**生成或修改的所有"过程文件 + 结果文件"
  - **`code-it` 已内部 commit 的文件**:`code-require` 不会触达(职责分离),`code-design` / `code-plan` 涉及但应**不**包含 `code-it` 任务级代码(因 `code-design` / `code-plan` 不写代码)
  - 用 `git status --porcelain` 列出 dirty 文件
  - `git add` + 预览 commit message(Q-3 锁定 A)+ 用户确认 + `git commit`
- **优先级**:必须
- **AC**:
  - AC-3.1:3 个技能 SKILL.md 末尾显式列出"步骤 N 兜底提交"
  - AC-3.2:收集文件范围:`git status --porcelain` 输出
  - AC-3.3:commit message 模板(由技能自动生成,附预览):
    - `code-require`:`chore(code-require): REQ-NNNNN <subject>`(subject = 需求标题)
    - `code-design`:`chore(code-design): REQ-NNNNN <subject>`(subject = 设计标题)
    - `code-plan`:`chore(code-plan): REQ-NNNNN <subject>`(subject = 计划标题)
  - AC-3.4:用户可用 `AskUserQuestion` 确认 / 修改 / 取消
  - AC-3.5:`git status --porcelain` 空 → 跳过 commit,打印 `无文件变更,跳过末尾提交`
  - AC-3.6:`git commit` 失败(非 0 退出码)→ 打印 stderr,**不重试**

### FR-4:不修改 `code-it` 内部 commit(Q-4 锁定 B)

- **描述**:`code-it` 现有的"每个任务显式 commit"行为**不变**;本需求的"末尾兜底提交"与之并存
- **优先级**:必须
- **AC**:
  - AC-4.1:`code-it/SKILL.md` 不被本需求修改
  - AC-4.2:末尾兜底提交不"补 commit" `code-it` 内部已 commit 的文件
  - AC-4.3:本需求不修改 `commit-conventions.md`(留作 follow-up)

### FR-5:不修改 `code-version` 内部行为

- **描述**:`code-require` 在 FR-2.AC-2.4 中**调用** `code-version`,但本需求**不**修改 `code-version/SKILL.md`
- **优先级**:必须
- **AC**:
  - AC-5.1:`code-version/SKILL.md` 不被本需求修改
  - AC-5.2:`code-require` 调 `code-version` 时,以"独立技能调用"形式(不在同一上下文),保证隔离

### FR-6:不修改 `marketplace.json` / `plugin.json` / CLAUDE.md

- **描述**:本需求不触发 `marketplace-protocol.md` 任何规则,不触发 `dashboard-conventions.md §规则 1`(CLAUDE.md 修改需走 `code-rule`)
- **优先级**:必须
- **AC**:
  - AC-6.1:`marketplace.json` / `plugin.json` 不被本需求修改
  - AC-6.2:`plugins/code-skills/CLAUDE.md` 的"AI 工作约定"小节**不**被本需求修改(留作 follow-up)
  - AC-6.3:中英 README 若需更新"3 个技能步骤变化",按 `doc-conventions §规则 1` 同次提交中英 — 但本需求**不**主动写 README(由 `code-rule` 沉淀)

---

## 5. 非功能需求 / 约束(NFR)

### NFR-1:零新增依赖
- **描述**:本需求不引入新依赖;`git pull` / `git status` / `git add` / `git commit` 全部为已存在的 `Bash` 工具
- **强制级别**:必须

### NFR-2:增量修改 SKILL.md,不重写
- **描述**:3 个技能 SKILL.md 的修改方式为 **Edit 工具追加新步骤**,不重写稳定章节
- **强制级别**:必须
- **理由**:避免破坏现有 frontmatter / 既有步骤描述

### NFR-3:`code-require` 额外步骤的中断语义
- **描述**:FR-2 的"中断 + 询问"是**硬中断** — 不进入原有"步骤 1 收集需求编码",不写任何文件
- **强制级别**:必须

### NFR-4:末尾兜底提交的"幂等性"
- **描述**:`git status --porcelain` 空时必须跳过 commit,不产生空 commit
- **强制级别**:必须
- **理由**:避免 commit 历史被"无变更"条目污染

### NFR-5:错误透明
- **描述**:`git pull` / `git commit` 任何非 0 退出码,**不**静默吞掉,必须 stderr 透传给用户
- **强制级别**:必须

### NFR-6:不污染 `commit-conventions.md`
- **描述**:本需求不直接修改 `commit-conventions.md` 规则 1(留作 follow-up);本需求**自动生成的 commit 信息格式**与 V0.0.1 既有实践保持一致(`chore(<scope>): <subject>`)
- **强制级别**:必须

### NFR-7:与 `code-it` 边界严格
- **描述**:`code-it` 的内部 commit 行为**完全独立**,本需求不感知 `code-it` 任务的 commit 状态
- **强制级别**:必须
- **理由**:Q-4 锁定 B;`code-design` / `code-plan` 末尾兜底提交只覆盖"自身产生的过程文件 + 结果文件",不重复 `code-it` 已 commit 的代码

### NFR-8:多设备场景的"拉取后,本机即新"
- **描述**:`git pull` 成功后,本机的工作树已与远端同步;`.current-version` 也已被覆盖 — FR-2 的对比逻辑必须基于"**拉取后**"的状态,不是"拉取前"
- **强制级别**:必须
- **关键实现**:`git pull` 完成后立即 `Read .current-version`,记录为"拉取后版本",再与"用户意图"对比

---

## 6. 页面与界面(交互式输出)

本需求**不**新增任何 UI 元素;输出是纯文本 + `AskUserQuestion` 弹窗。关键交互点:

### 6.1 FR-2 的"询问用户"弹窗(Q-1 锁定 A)
```
✗ 检测到上下文版本不一致
  本地(拉取后):V0.0.2
  远端:.current-version = V0.0.3
  需求 REQ-00006 在 V0.0.2 中不存在

请选择后续动作:
  A. 切到 V0.0.3 后继续(推荐)
  B. 在 V0.0.2 中重新创建 REQ-00006
  C. 取消
```

### 6.2 FR-3 的"预览 commit"弹窗(Q-3 锁定 A)
```
预览 commit message:
  chore(code-require): REQ-00005 优化 /code-require 技能
  
  需求分析完成:10 FR / 7 NFR / 30 AC
  过程文件 3 + 结果文件 1 = 4 文件待提交

请选择:
  A. 确认提交(推荐)
  B. 修改 commit message
  C. 取消提交
```

---

## 7. 交互逻辑

### 7.1 `code-require` 完整工作流(改后)

```
[启动]
  ↓
[步骤 0a:git pull] ─────────────┐
  ↓ (成功)                       │ (失败 → E-2/E-3/E-4,中断退出)
[读取 .current-version 拉取后版本] │
  ↓                              │
[步骤 0b:版本对齐检查] ────┐      │
  ↓ (一致)                  │ (不一致 → FR-2.AC-2.3 询问)
[步骤 0:版本上下文检测]    │      │
  ↓                        │      │
[步骤 1:收集需求编码]      │      │
  ↓                        │      │
[步骤 2-9:原有流程]        │      │
  ↓                        │      │
[步骤 N:末尾兜底提交]      │      │
  ↓                        │      │
[退出]                     │      │
                            │      │
[选 A 切版本并退出] ←──┘      │
[选 B 在本地版本中继续] ←─┘      │
[选 C 取消退出] ←────────┘──────┘
```

### 7.2 `code-design` / `code-plan` 完整工作流(改后)

```
[启动]
  ↓
[步骤 0a:git pull] ─────────────┐
  ↓ (成功)                       │ (失败 → E-2/E-3/E-4,中断退出)
[步骤 0:版本上下文检测]        │
  ↓                              │
[步骤 1-?:原有流程]             │
  ↓                              │
[步骤 N:末尾兜底提交] ──┐       │
  ↓ (无变更)             │       │
  ↓ (有变更)             │       │
[预览 + 询问]            │       │
  ↓ (确认)               │       │
[git commit]            │       │
  ↓                      │       │
[退出]                   │       │
                         │       │
[跳过 commit 直接退出] ←─┘──────┘
```

### 7.3 末尾兜底提交流程(FR-3 细化)

```
[收集 git status --porcelain 输出]
  ↓ (空)
[跳过 commit,打印 "无文件变更"]
  ↓
[退出]
  ↓ (非空)
[git add <所有文件>]
  ↓
[生成 commit message 预览]
  ↓
[AskUserQuestion:确认/修改/取消]
  ↓ (确认) (修改) (取消)
[git commit] [重新预览] [不 commit,退出]
  ↓ (成功) (失败)
[打印 commit hash] [打印 stderr,提示手动处理]
  ↓
[退出]
```

---

## 8. 数据与状态

### 8.1 关键数据源

| 数据 | 路径 | 读取时机 |
| --- | --- | --- |
| `.current-version` | `./assistants/.current-version` | 步骤 0a 之后(FR-2)、步骤 0(原有) |
| `git status` | 整仓库 | 步骤 0a 之后、步骤 N 之前 |
| `git pull` 结果 | 整仓库 | 步骤 0a |
| `git commit` 结果 | 整仓库 | 步骤 N |

### 8.2 末尾兜底提交的文件范围

| 技能 | 兜底覆盖文件(示例) |
| --- | --- |
| `code-require` | `require/<REQ>/{RESULT,materials-index,clarifications,related-requirements}.md` + V0.0.2/RESULT.md 看板 |
| `code-design` | `design/<REQ>/{RESULT,clarifications,...}.md` + V0.0.2/RESULT.md 看板 |
| `code-plan` | `plan/<REQ>/{RESULT,PLAN,materials-index,...}.md` + V0.0.2/RESULT.md 看板 |

**显式不含**:`code-it` 内部 commit 的代码文件 / `code-unit` 内部 commit 的测试文件 / `code-review` 内部 commit 的评审文件

### 8.3 commit message 模板

```
chore(code-require): REQ-00005 <需求标题>

需求分析完成:10 FR / 7 NFR / 30 AC
过程文件 3 + 结果文件 1 = 4 文件待提交
```

```
chore(code-design): REQ-00005 <设计标题>

概要设计完成:<关键决策数> 项决策,<不变量数> 条不变量
过程文件 N + 结果文件 1
```

```
chore(code-plan): REQ-00005 <计划标题>

详细设计与编码计划完成:<任务数> 个任务
过程文件 N + 结果文件 2(PLAN.md + RESULT.md)
```

### 8.4 FR-2 版本对齐的数据结构

```ts
{
  pulledVersion: string,    // git pull 后 .current-version
  intendedVersion: string,  // 用户的"上下文"版本(隐式 = 拉取前读取的版本,或用户口头指定)
  isConsistent: boolean,
  // 若不一致:
  recommendation: string,   // "切到 pulledVersion"(默认推荐)
  alternatives: string[]    // [intendedVersion, "取消"]
}
```

---

## 9. 边界与异常

| ID | 场景 | 触发条件 | 处理(Q-2 锁定 A) |
| --- | --- | --- | --- |
| **E-1** | FR-2 检测到版本不一致 | `pulledVersion ≠ intendedVersion` | 走 FR-2.AC-2.3 询问 |
| **E-2** | `git pull` 冲突 | 工作树有未解决冲突 | 中断 + `✗ git pull 失败:存在未解决的冲突` + 提示手动处理 |
| **E-3** | `git pull` 网络失败 | remote 不可达 | 中断 + `✗ git pull 失败:网络/remote 不可达` + 提示检查网络 |
| **E-4** | `git pull` 权限失败 | 凭据失效 | 中断 + `✗ git pull 失败:权限/凭据` + 提示检查凭据 |
| **E-5** | `git pull` no-op(已是最新) | 无新提交 | 静默成功(不打印) |
| **E-6** | FR-2 选 A(切版本) | 用户选择 | 调 `code-version <pulledVersion>` + 提示"已切到 X,请重跑 `code-require`" |
| **E-7** | FR-2 选 C(取消) | 用户选择 | 直接退出,无文件变更 |
| **E-8** | FR-3 末尾无文件变更 | `git status --porcelain` 空 | 跳过 commit,打印 `无文件变更,跳过末尾提交` |
| **E-9** | FR-3 用户选 C(取消提交) | 用户选择 | 跳过 commit,打印 `已取消提交,文件保持暂存/工作区状态` |
| **E-10** | FR-3 `git commit` 失败 | pre-commit hook / 其他原因 | 打印 stderr,**不重试**,提示手动处理 |
| **E-11** | FR-2 询问时用户不回答 | 异常超时 | 不发生(Claude Code 总会问必答) |
| **E-12** | 末尾兜底时,git 不存在 | 系统无 git | 中断 + 提示 `未检测到 git,本需求需要 git` |
| **E-13** | `code-design` / `code-plan` 末尾兜底时,本版本未拉取(用户在 0a 之前已部分写入) | 不可能(0a 已拉) | 防御性代码:若 .current-version 与"步骤 0 读取"不一致,重新走 FR-2 |

---

## 10. 验收标准(AC 总览)

按 FR 编号归类,合计 ~32 条:

- **FR-1**(4 条):AC-1.1 / AC-1.2 / AC-1.3 / AC-1.4
- **FR-2**(6 条):AC-2.1 ~ AC-2.6
- **FR-3**(6 条):AC-3.1 ~ AC-3.6
- **FR-4**(3 条):AC-4.1 / AC-4.2 / AC-4.3
- **FR-5**(2 条):AC-5.1 / AC-5.2
- **FR-6**(3 条):AC-6.1 / AC-6.2 / AC-6.3
- **NFR-1**(1 条):零新增依赖
- **NFR-2**(1 条):增量修改,frontmatter 完整保留
- **NFR-3**(1 条):FR-2 硬中断
- **NFR-4**(1 条):空 commit 跳过
- **NFR-5**(1 条):stderr 透传
- **NFR-6**(1 条):commit 格式与 V0.0.1 实践一致
- **NFR-7**(1 条):与 `code-it` 边界严格
- **NFR-8**(1 条):版本对比基于"拉取后"

**总计**:约 32 条 AC。

---

## 11. 关联需求

| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| **REQ-00004**(V0.0.2) | 范围并列:`code-dashboard` 纯只读,本需求修改型 | 不冲突;`code-dashboard` NFR-7"幂等"不受末尾提交影响(末尾提交不在 `code-dashboard` 范围) | `./assistants/V0.0.2/require/REQ-00004/RESULT.md` §NFR-6/§NFR-7 |
| **REQ-00003**(V0.0.1) | `commit-conventions.md` 占位文件 | 本需求**不**直接填充规则;末尾 commit 沿用 V0.0.1 实践格式 | `./assistants/V0.0.1/require/REQ-00003/RESULT.md` + `./assistants/rules/commit-conventions.md` |
| **REQ-00002**(V0.0.1) | 3 类编码权威源 | 末尾 commit 信息中 `REQ-NNNNN` 引用必须严格符合 `encoding-conventions.md` 规范 | `./assistants/V0.0.1/require/REQ-00002/RESULT.md` |
| **REQ-00001**(V0.0.1) | "每个任务显式 commit"实践 | 本需求**不**取代 `code-it` 内部 commit;二者并存(Q-4 锁定 B) | `./assistants/V0.0.1/require/REQ-00001/RESULT.md` + V0.0.1 看板"执行的开发命令记录"段 |
| **REQ-00001-005 / REQ-00002-009** | review 派生任务"留 dirty tree"模式 | 本需求在"无变更"时跳过 commit,**不**强制 review 派生任务也走末尾提交(由 `code-review` 阶段决定) | V0.0.1 看板"派生任务记录"段 |

详细关联分析见 `related-requirements.md`。

---

## 12. 待澄清 / 未决项(本轮未处理 / 留作默认)

### Q-5:`commit-conventions.md` 规则沉淀
- **状态**:**未采用**(不直接在本需求中写规则,留作 follow-up)
- **回退路径**:用户后续可调 `code-rule` 触发该规则填充

### Q-6:`.gitignore` 与"不应提交的文件"
- **状态**:采纳默认(严格遵循项目根 `.gitignore`)
- **回退路径**:若 `.gitignore` 缺失,采用 `git status --porcelain` 全量纳入(无排除规则)

### Q-7:`plugins/code-skills/CLAUDE.md` 的"AI 工作约定"小节追加
- **状态**:**未采用**(不触发 `dashboard-conventions §规则 1`)
- **回退路径**:用户后续可调 `code-rule` 沉淀

### Q-8:`commit-conventions.md` 规则未填充(占位)如何处理
- **状态**:采纳默认(沿用 V0.0.1 实践,`chore(<scope>): <subject>`,subject 含 `REQ-NNNNN`)

### Q-9(新增):本需求完成后,是否派生"用 `code-rule` 沉淀 commit 规则"任务
- **建议**:可派生(由 `code-review` 在评审本需求时决定,类似 REQ-00001-005 / REQ-00002-009 的派生模式)
- **状态**:本需求不阻塞

---

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-04 13:33 | v1 | 初始创建:6 FR / 8 NFR / ~32 AC / 13 边界场景;Q-1/Q-2/Q-3/Q-4 锁定,Q-5/Q-6/Q-7/Q-8 留默认/未采用;用户原文 2 处笔误已纠正(`/code-desgin` → `/code-design`,`/core-require` → `/code-require`) | wangmiao |
