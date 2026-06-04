# 开发日志 — TASK-REQ-00004-00003

开始时间:2026-06-04 17:05
版本:V0.0.2
任务编号:TASK-REQ-00004-00003
触发/来源:需求新增

---

## 项目现状(步骤 6 记录)

### 项目类型
- 类型:Claude Code marketplace 仓库(单插件 `code-skills`)
- 主体:10 个 `code-*` 技能 + README 中英对仗 + 文档
- 构建/运行/测试:**无**

### 既有 README 结构(中英对仗,883 行 / 883 行)
- **行 1~23**:头部(标题 / 简介 / 安装)
- **行 24~38**:"技能概览 / Skills Overview" 表格(5 列:技能 / 用途 / 读取 / 写入 / 下游)
  - 已有 10 行(对应 10 个 `code-*` 技能:code-init / code-version / code-rule / code-require / code-design / code-plan / code-it / code-unit / code-fix / code-review)
  - **末行(中文行 37)**: `| [\`code-review\`](skills/code-review/SKILL.md) | ... | (空)| (空) | (空)|`
  - 表格紧接空行(行 38)
- **行 39~48**:"工作流管道 / Pipeline"(含 ASCII art)
- **行 49~62**:关于 `code-rule` / `code-init` / `code-fix` 的说明
- **行 63~136**:"仓库结构 / Repository Structure"(含 ASCII art)
- **行 137~203**:"核心概念 / Key Concepts" + "使用说明 / How to Use"
- **行 205~298**:"完整工作流程 / Complete Workflow"(含 Mermaid + ASCII)
- **行 300~718**:"命令参考 / Command Reference"(4 大类 × 10 个命令)
- **行 720~839**:"典型场景 / Common Scenarios"(6 个)
- **行 841~858**:"速查表 / Quick Reference"
- **行 860~883**:"详细文档 / Detailed Documentation"

### 命名 / 风格
- 表格风格:无 `:---:`(左对齐)
- 链接:`[\`code-X\`](skills/code-X/SKILL.md)`(反引号包裹技能名 + 相对路径链接)
- 中文文档使用全角标点(,/。/()/— 等);英文使用半角(`,`/`.`/`()`/`—` 等)
- 中英**严格对仗**:每个章节名一一对应(用 `##` 同级)

### 关键约束
- **必须中英同次提交**(`doc-conventions §规则 1`):两文件**同步**修改,**不**能"中文版有 X 章节,英文版无 X 章节"
- **结构对仗**:中英同数量 + 同顺序的二级标题
- **追加位置**:PLAN.md 行 213-216 锁定,在"技能概览 / Skills Overview"末行(`code-review`)之后
- **不**触发 `skill-conventions` / `module-conventions` 严守(NFR-6 限定为"不动 SKILL.md frontmatter",README 改动允许)
- **不**改 `marketplace.json` / `plugin.json`(NFR-6 严守)

---

## 项目级规范要点(步骤 4 记录)

| 规范文件 | 关键条款 | 对本任务的约束 |
| --- | --- | --- |
| `doc-conventions.md` §规则 1 | README 中英同次提交 + 结构对仗 | **直接约束**:两文件**同步**修改 |
| `doc-conventions.md` §规则 2 | 核心小节必覆盖(简介 / 安装 / 核心流程 / 主要能力) | **直接约束**:本任务改的"技能概览"段属于"主要能力"小节 |
| `marketplace-protocol.md` §规则 1 | 不动 marketplace.json / plugin.json | **直接约束** |
| `commit-conventions.md` §规则 1 占位 | 提交规范 | V0.0.1 既有 commit 走 conventional 风格,本任务 commit 走 `chore(...)` 风格 |
| `skill-conventions.md` §规则 1 | frontmatter 必含 name + description | 不适用(改 README,不动 SKILL.md frontmatter) |

---

## 任务设计要点(步骤 5 记录)

### PLAN.md §3 T-003(行 203~244 区域)
- **类型**:新增(修改 2 个文件各 1 行)
- **目标**:在 `plugins/code-skills/README.md` 与 `README.en.md` 的"主要能力"或"技能清单"段各追加 1 行,登记 `code-dashboard` 技能
- **关键变更**:
  - 中文版追加(PLAN.md 行 207):
    ```markdown
    | code-dashboard | 开发看板(只读) | 展示当前版本需求/任务/缺陷进度 + 下一步建议 | `/code-dashboard` 或 `/code-dashboard REQ-NNNNN` |
    ```
  - 英文版追加(PLAN.md 行 211):
    ```markdown
    | code-dashboard | Dev Dashboard (read-only) | Show version req/task/bug progress + next-step suggestions | `/code-dashboard` or `/code-dashboard REQ-NNNNN` |
    ```

### **关键发现**:本 README 没有"主要能力"小节
- 既有 10 个 `code-*` 技能在"技能概览 / Skills Overview"段(行 26-37)
- PLAN.md 行 207/211 给出的字面是**简化版**(4 列:技能 / 用途 / 命令)— 与既有"技能概览"表的 5 列结构(技能 / 用途 / 读取 / 写入 / 下游)**不一致**
- **本任务决策**:
  - **保留 5 列结构**(与既有 10 行严格对仗,`doc-conventions §规则 1` "结构对仗"精神)
  - 列填充对齐既有风格:
    - 技能:`[\`code-dashboard\`](skills/code-dashboard/SKILL.md)`(反引号 + 相对路径链接)
    - 用途:"开发看板(只读)— 展示当前版本需求/任务/缺陷进度 + 最多 5 条下一步建议"(对齐 code-fix 行的"简介 — 说明"风格)
    - 读取:无(`code-dashboard` 不读任何外部输入;只读 `.current-version` + 看板是"读取"列的内容,实际等价于"无")
    - 写入:"(屏幕输出,无文件)"(对齐 code-version 行的"(无)"风格)
    - 下游:"(引导用户调 code-require / code-design / code-plan / code-it / code-unit / code-fix / code-version)"

### 关键约束
- **必须保持 5 列结构 + 10 行既有行严格对仗**(`doc-conventions §规则 1`)
- 不得**修改**其他任何行
- 必须**同一消息块**完成两文件 Edit(中英同次提交)

---

## 开发过程

### 2026-06-04 17:05
- **操作**:读取 .current-version(确认 V0.0.2)+ plan/REQ-00004/PLAN.md(找 T-003 状态="待开始")+ plan/REQ-00004/RESULT.md(详细设计对应章节)+ plugins/code-skills/README.md(883 行)+ plugins/code-skills/README.en.md(883 行)
- **目的**:准备实施 T-003
- **结果**:全部就绪;code/TASK-REQ-00004-00003/ 目录已创建
- **关键发现**:本 README 没有"主要能力"小节,实际"技能清单"是"技能概览"段(行 26-37);且 PLAN.md 给出的字面是 4 列,与既有 5 列不一致 → 本任务决策"保留 5 列结构,扩展 PLAN.md 字面以匹配"

### 2026-06-04 17:08
- **操作**:用 `Edit` 在 `plugins/code-skills/README.md` 行 37(`code-review` 行)之后追加 1 行(`code-dashboard` 行)
- **目的**:实施 T-003 中文侧
- **结果**:见后续静态自检

### 2026-06-04 17:10
- **操作**:用 `Edit` 在 `plugins/code-skills/README.en.md` 行 37(`code-review` 行)之后追加 1 行(`code-dashboard` 行)
- **目的**:实施 T-003 英文侧(中英同次提交)
- **结果**:见后续静态自检

### 2026-06-04 17:12
- **操作**:静态自检(Read 两文件 + Grep 关键字 + 列数核对 + git diff)
- **目的**:中英对仗 + NFR-6 严守 + doc-conventions §规则 1
- **结果**:待执行(下一步骤)
