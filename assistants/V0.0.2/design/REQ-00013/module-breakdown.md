# 模块拆分 — REQ-00013
更新时间:2026-06-05 21:00
版本:V0.0.2

## 总览

| 类别 | 数量 | 备注 |
| --- | --- | --- |
| 新增模块 | 0 | NFR-2 零规范变更 + NFR-7 frontmatter 不变 |
| 复用既有 | 13 | 全部 13 个 `code-*` 技能复用(NFR-6 4 个不改 + 7 个增量改 + 2 个协同)|
| 修改既有 | 7 | `code-require` / `code-plan` / `code-fix` / `code-it` / `code-unit` / `code-review` / `code-auto` 7 个 SKILL.md 增量追加(FR-3~9)|
| 修改既有(协同)| 1 | `code-publish` SKILL.md 增量追加(NFR-5 / FR-10.AC-10.2)|
| 不修改 | 5 | `code-dashboard` / `code-version` / `code-rule` / `code-init` / `code-merge` 5 个 SKILL.md(NFR-6 / Q-7)|
| 新增依赖 | 0 | NFR-1 零依赖 |
| 新增模板 | 0 | NFR-2 不修改 templates/(从已有内容派生)|

## 模块清单

### M-1:`code-require/SKILL.md` 增量追加"标题解析"段
- **路径**:`plugins/code-skills/skills/code-require/SKILL.md`
- **状态**:修改既有
- **职责**:在"步骤 0"后追加"## 标题解析(REQ-00013 新增)";解析 `require/.../RESULT.md` 第 1 行 → 提取"需求标题" → 截断到 30 字 → 在所有屏幕输出位置拼接"编号+标题"
- **对外接口**:
  - 启动输出:`正在处理: REQ-NNNNN · <需求标题>`
  - 完成输出:`完成: REQ-NNNNN · <需求标题>`
  - 中止输出:`⛔ code-require 中止: REQ-NNNNN · <需求标题>(<原因>)`
- **依赖**:无
- **关键决策**:锚点 = "## 工作流程"前的"## 工具使用约定"段后(沿用 REQ-00005 / REQ-00011 增量模式)
- **符合的规范条款**:`skill-conventions §规则 1` (frontmatter 字节级保留)+ `dashboard-conventions §规则 1` (字段不扩展)

### M-2:`code-plan/SKILL.md` 增量追加"标题解析"段
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **状态**:修改既有
- **职责**:在"步骤 0"后追加"## 标题解析(REQ-00013 新增)";解析 `require/.../RESULT.md` 第 1 行 → 提取"需求标题" + 解析 `plan/.../PLAN.md` 任务总览"标题"列 → 提取"任务标题" → 截断到 30 字 → 在所有屏幕输出位置拼接
- **对外接口**:
  - 启动输出:`正在处理: REQ-NNNNN · <需求标题>`
  - 拆分输出:`拆分: TASK-... · <任务标题>`
  - 完成输出:`完成: REQ-NNNNN · <需求标题>(拆 N 个任务)`
- **依赖**:无
- **关键决策**:锚点 = "## 工作流程"前
- **符合的规范条款**:同 M-1

### M-3:`code-fix/SKILL.md` 增量追加"缺陷标题解析"段
- **路径**:`plugins/code-skills/skills/code-fix/SKILL.md`
- **状态**:修改既有
- **职责**:在"步骤 1"末尾追加"## 缺陷标题生成(REQ-00013 新增)";用户输入缺陷描述时,自动生成"## 缺陷标题"小节(取用户原始描述前 30 字 + `...`);在所有屏幕输出位置拼接"BUG-NNNNN · <缺陷标题>"
- **对外接口**:
  - 启动输出:`正在处理: BUG-NNNNN · <缺陷标题>`(从 `fix/.../RESULT.md` "## 缺陷标题"读取)
  - 登记输出:`已创建: BUG-NNNNN · <缺陷标题>`
  - 完成输出:`已修复: BUG-NNNNN · <缺陷标题>`
- **依赖**:无
- **关键决策**:锚点 = "## 工作流程"前
- **符合的规范条款**:同 M-1

### M-4:`code-it/SKILL.md` 增量追加"任务标题解析"段
- **路径**:`plugins/code-skills/skills/code-it/SKILL.md`
- **状态**:修改既有
- **职责**:解析 `plan/.../PLAN.md` 任务总览"标题"列 → 提取"任务标题" → 截断到 30 字 → 在所有屏幕输出位置拼接
- **对外接口**:
  - 启动输出:`正在处理: TASK-... · <任务标题>`
  - 完成输出:`已完成: TASK-... · <任务标题>`
  - 中止输出(REQ-00010 守卫):含"REQ-NNNNN · 标题" + "TASK-... · 标题"
- **依赖**:无
- **关键决策**:锚点 = "## 工作流程"前
- **符合的规范条款**:同 M-1

### M-5:`code-unit/SKILL.md` 增量追加"任务标题解析"段
- **路径**:`plugins/code-skills/skills/code-unit/SKILL.md`
- **状态**:修改既有
- **职责**:同 M-4
- **对外接口**:
  - 启动输出:`正在处理: TASK-... · <任务标题>`
  - 完成输出:`已运行-通过/失败: TASK-... · <任务标题>`
  - 守卫跳过输出(REQ-00009):`⏭ code-unit 跳过: TASK-... · <任务标题>(项目不可测)`
- **依赖**:无
- **关键决策**:锚点 = "## 工作流程"前
- **符合的规范条款**:同 M-1

### M-6:`code-review/SKILL.md` 增量追加"需求/任务标题解析"段
- **路径**:`plugins/code-skills/skills/code-review/SKILL.md`
- **状态**:修改既有
- **职责**:解析 `require/.../RESULT.md` 第 1 行 → 提取"需求标题" + 解析 `plan/.../PLAN.md` 任务总览 → 派生任务"标题"列写入时截断到 30 字
- **对外接口**:
  - 启动输出:`正在处理: REQ-NNNNN · <需求标题>`
  - 完成输出:`已评审: REQ-NNNNN · <需求标题>(N 条发现)`
  - 派生任务通知:`派生任务: TASK-... · <任务标题>(审查派生)`
- **依赖**:无
- **关键决策**:锚点 = "## 工作流程"前
- **符合的规范条款**:同 M-1

### M-7:`code-auto/SKILL.md` 增量追加"子技能标题预读"段
- **路径**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **状态**:修改既有
- **职责**:在调子技能前,自读"标题"源(`require/.../RESULT.md` 第 1 行 / `PLAN.md` 任务总览 / `fix/.../RESULT.md` "## 缺陷标题"),拼接到进度日志
- **对外接口**:
  - 步骤日志:`[code-auto] 步骤 1/6:code-require REQ-NNNNN · <需求标题>`
  - 任务循环日志:`[code-auto]   → 1/N:code-it TASK-... · <任务标题> ✓`
  - 派生循环日志:`[code-auto]   → code-review 第 2 轮:无"必须改" → 结束`
  - 报告:`✓ code-auto 完成: REQ-NNNNN · <需求标题>`
- **依赖**:无
- **关键决策**:锚点 = "## 屏幕报告格式"小节前(增量追加"## 标题预读"段)
- **符合的规范条款**:同 M-1

### M-8:`code-publish/SKILL.md` 增量追加"未完成项格式升级"段
- **路径**:`plugins/code-skills/skills/code-publish/SKILL.md`
- **状态**:修改既有(协同)
- **职责**:PreflightChecker 输出"未完成项"行时,拼接"编号+标题";解析 `require/.../RESULT.md` 第 1 行 / `PLAN.md` 任务总览"标题"列 / `fix/.../RESULT.md` "## 缺陷标题"
- **对外接口**:
  - 报告:`[需求] REQ-NNNNN · <需求标题> 状态=进行中(应该=已完成)`
  - 报告:`[任务] TASK-... · <任务标题> 开发状态=进行中(应该=已完成)`
  - 报告:`[缺陷] BUG-NNNNN · <缺陷标题> 状态=待修复(应该=已修复)`
- **依赖**:无
- **关键决策**:锚点 = "PreflightChecker" 章节末尾
- **符合的规范条款**:NFR-5;FR-10.AC-10.2

## 不修改的 5 个 SKILL.md
- `code-dashboard/SKILL.md` — NFR-2 看板"任务清单"区段已含"标题"列,0 改动
- `code-version/SKILL.md` — NFR-6 不改
- `code-rule/SKILL.md` — NFR-6 不改
- `code-init/SKILL.md` — 项目级一次性,本需求无关
- `code-merge/SKILL.md` — NFR-6 不改

## 自检:`module-conventions.md` 逐条检查
- ✅ 资源放 `templates/` / `checklists/` / `guidelines/` 子目录(本轮 0 新增资源)
- ✅ `SKILL.md` 放技能根目录(沿用既有 13 个技能)
- ✅ 命名风格 kebab-case(沿用既有)
- ✅ 0 循环依赖(0 新增模块)
- ✅ 目录结构清晰(增量追加,既有目录不变)
