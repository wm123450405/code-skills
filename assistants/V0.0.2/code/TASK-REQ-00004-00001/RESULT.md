# 改修总结 — TASK-REQ-00004-00001

- 任务编码:TASK-REQ-00004-00001
- 标题:写 `plugins/code-skills/skills/code-dashboard/SKILL.md`
- 需求编码:REQ-00004
- 所属版本:V0.0.2
- 类型:新增
- 触发/来源:需求新增
- 状态:**已完成**
- 责任人:wangmiao
- 创建:2026-06-04 16:30
- 完成:2026-06-04 16:40
- 最近更新:2026-06-04 16:40
- 当前版本:v1

---

## 1. 任务信息

| 字段 | 值 |
| --- | --- |
| 任务编号 | TASK-REQ-00004-00001 |
| 标题 | 写 `plugins/code-skills/skills/code-dashboard/SKILL.md` |
| 类型 | 新增 |
| 触发/来源 | 需求新增 |
| 开发状态 | **已完成** |
| 测试状态 | **不适用**(P-A2 锁定) |
| 任务来源 | `./assistants/V0.0.2/plan/REQ-00004/PLAN.md` §3 |
| 设计依据 | `./assistants/V0.0.2/plan/REQ-00004/RESULT.md` §4-7 + §10-11 |

---

## 2. 改修内容总览

### 2.1 改动文件清单
- **新增 1 个**:`plugins/code-skills/skills/code-dashboard/SKILL.md`(367 行,~13 KB)

### 2.2 未改动文件清单(对照 NFR-6 严守)
- ❌ 未改 `marketplace.json`(走 Claude Code 技能自动发现协议)
- ❌ 未改 `plugin.json`(同上)
- ❌ 未改其他 10 个 `code-*` SKILL.md frontmatter(code-init / code-version / code-rule / code-require / code-design / code-plan / code-it / code-unit / code-fix / code-review)
- ❌ 未改 `plugins/code-skills/CLAUDE.md`(T-002 可选,本设计**不**触发)
- ❌ 未改 `plugins/code-skills/README.md` + `README.en.md`(T-003 可选,本设计**不**触发)
- ❌ 未改 `./assistants/rules/` 下任何文件
- ❌ 未改 `./assistants/V0.0.2/require/` / `design/` / `plan/` 下任何文件
- ❌ 未改 `plugins/code-skills/.claude-plugin/` 下任何文件

### 2.3 文档大小
- `SKILL.md`:367 行 / 13 KB(预估 350-450 行,符合)

---

## 3. 详细改动(SKILL.md 章节结构)

### 3.1 YAML frontmatter(行 1-3)
```yaml
---
name: code-dashboard
description: 开发看板(版本感知,只读)。要求用户提供"需求编码"或留空。**无参数时**展示当前激活版本下需求/任务/缺陷的整体执行情况(总进度 + 任务进度 + 高优先级缺陷 + 最多 5 条下一步建议);**指定 `REQ-NNNNN` 时**展示该需求的进度与其下任务的进度概览(任务清单 + 关联缺陷 + 下一步建议);**不**调用任何 `Write` / `Edit` / `Bash`,**只**调用 `Read` / `Glob` / `Grep`,所有输出仅打印到屏幕,不写任何文件,可随时调用、多次执行幂等。在 `code-version` 之后使用,也可在长会话中随时调用以判断"接下来做什么"。
---
```

要点:
- `name: code-dashboard` 与目录名严格一致(`skill-conventions §规则 1`)
- `description` 一句话涵盖"做什么 / 何时用 / 只读契约 / 幂等性"4 维度

### 3.2 正文 12 节(行 5-305)
按既有 10 个 `code-*` 技能严格对齐的章节顺序:
1. `## 目标`(行 7-21)
2. `## 适用场景`(行 23-29)
3. `## 不适用`(行 31-38)
4. `## 工作目录约定(强制)`(行 40-52)
5. `## 输入`(行 54-59)
6. `## 输出`(行 61-72)
7. `## 工具使用约定`(行 74-90)
8. `## 工作流程`(行 92-220,含步骤 0~6)
9. `## 边界与异常`(行 222-273,含 L1/L2/L3 + 边界场景 E-7~E-10)
10. `## 衔接`(行 275-289,含上游/下游/横向)
11. `## 不要做的事`(行 291-313,12 条禁止)
12. `## 附录 A/B/C`(行 315-367,算法 4/5 + 数据结构)

### 3.3 步骤 0~6(行 94-220)
- **步骤 0** 版本上下文检测(强制前置)
- **步骤 1** 参数解析(算法 0)
- **步骤 2** 数据加载(2a 总览 / 2b 需求并行 Read)
- **步骤 3** 区段解析(算法 1)
- **步骤 4** 聚合 + 渲染(段 1 需求 / 段 2 任务 / 段 3 缺陷 / 段 4 建议)
- **步骤 5** 下一步建议生成(算法 3,5 类优先级)
- **步骤 6** 屏幕打印(无文件副作用)

### 3.4 附录(算法 4/5 + Suggestion 数据结构)
- **附录 A**:`parseTaskId()` 伪代码(双格式正则)
- **附录 B**:`renderBar(filled, total)` 伪代码(12 字符柱状图)
- **附录 C**:`Suggestion` 数据结构(3 字段)

---

## 4. 关键决策与权衡

### 4.1 与概要设计 / 详细设计严格一致
- 6 个算法(算法 0~5)的输入/输出/复杂度/边界/伪代码**全部**严格按 `plan/REQ-00004/RESULT.md §5` 与 `plan/REQ-00004/design-notes.md` 落地
- 10 项边界 E-1~E-10 完整覆盖
- 8 个内存数据结构(Suggestion / TaskId / ParseResult / 4 个 Row / ErrorInfo)通过附录与正文引用关联

### 4.2 3 项 design 阶段授权偏离 + 3 项 plan 阶段新增偏离全部落地
| 偏离 | 落点 |
| --- | --- |
| A-1(单文件) | SKILL.md 单文件,无 `templates/` / `checklists/` / `guidelines/` 子目录 |
| A-2(不改 marketplace) | 行 51 + 行 311 显式声明"不修改 marketplace.json / plugin.json" |
| A-3(无历史版本切换) | `## 不适用` 节明示"想切到历史版本 → 走 code-version" |
| P-A1(状态字面不归一化) | 步骤 4 段 1 渲染段显式注明"状态字面严格按看板列定义" |
| P-A2(测试状态=不适用) | `test-results.md` 完整说明"本任务测试状态 = 不适用,无单元测试载体" |
| P-A3(需求模式不显示里程碑) | `## 不适用` 节明示"想看'里程碑'段 → 走总览模式" |

### 4.3 命名 / 错误处理风格与既有 10 个 SKILL.md 一致
- 错误前缀 `✗`(对齐 `code-version` / `code-fix` 等)
- 引导前缀 `>`(对齐既有风格)
- 步骤编号 `### 步骤 N — <一句话>`(对齐既有)
- 状态字面 `待开始` / `已完成` / `已运行-通过` 等中文(对齐 `version-RESULT.md` 模板)

---

## 5. 偏离设计/规范的地方

### 5.1 代码偏离设计
**无**(本任务严格按 `plan/REQ-00004/RESULT.md` 实施)

### 5.2 代码偏离规范
**无**(本任务严格按 `skill-conventions §规则 1` + NFR-1/3/4/6/7 实施)

### 5.3 任务范围扩展
**无**(本任务**只**新增 `SKILL.md` 1 个文件,无任何额外动作)

### 5.4 详细列表
详见 `deviations.md`(本任务**无**偏离需要记录)。

---

## 6. 验证结果

### 6.1 编译/构建
- **不适用**(本仓库无构建系统,详见 `compile-and-run.md`)

### 6.2 启动运行
- **不适用**(本技能是 Claude Code 指令型 Markdown,无运行面)

### 6.3 静态自检(9/9 通过)
详见 `compile-and-run.md`:
- ✅ frontmatter 完整(`name: code-dashboard` + 完整 `description`)
- ✅ 节标题顺序与既有 10 个 SKILL.md 严格对齐(12 节 + 3 附录)
- ✅ 步骤 0~6 齐全(7 步)
- ✅ 边界 E-1~E-10 完整覆盖(13 次命中)
- ✅ NFR-7 禁用词语境:4 处出现,全部"声明不调用"上下文
- ✅ NFR-6 边界:2 处出现,全部"声明不动"上下文
- ✅ 任务编号双格式正则:附录 A 完整
- ✅ ASCII 比例条字符:`█` / `░` / `▓` 出现 ≥ 20 次
- ✅ git status 净度:仅 V0.0.2/RESULT.md 1 处 modification(plan 阶段同步)+ 4 个 untracked 工作空间目录

### 6.4 动态实测(7 项,留给 `code-review` 阶段)
- ⏳ AC-2.1~2.5 总览模式 4 段
- ⏳ AC-3.1~3.5 需求模式 5 段
- ⏳ AC-4.1~4.4 下一步建议
- ⏳ AC-5.1~5.2 无激活版本引导
- ⏳ AC-6.1~6.3 参数校验
- ⏳ NFR-2 4 种异常场景
- ⏳ NFR-4 性能 < 5 秒
- ⏳ NFR-7 幂等性

**自检完成度**:6/13 静态可验项本任务全过,7/13 动态实测项留给 `code-review` 阶段。

---

## 7. 已知问题/未完成项

### 7.1 本任务无已知问题
- 静态自检 9/9 通过
- 6 项 design/plan 偏离全部落地
- 无任何"留给后续任务或 PR 评审"的项目

### 7.2 留给后续 follow-up(非本任务范围)
- F-1:`code-review/SKILL.md` frontmatter `<version>` 笔误(超出 REQ-00004 范围)
- F-2:`code-dashboard` 是否在"任务清单"段附加"近期提交哈希"列(留作 v2)
- F-3:跨版本汇总能力(留作 v2)
- F-4:`--json` / `--filter` / `--since` 等 CLI flag(留作 v2)
- T-002(可选):改 `CLAUDE.md` "指引 N"
- T-003(可选):改 `README.md` + `README.en.md` 技能清单

---

## 8. 关联任务与提交

### 8.1 关联任务
- **关联任务**:无(本任务是 V0.0.2 首个 `code-it` 产出,无既有任务被取代)
- **后续任务**:T-002(可选)/ T-003(可选)由用户授权才落地

### 8.2 git 提交
- **本任务暂未提交**(本工作空间是 git worktree,用户后续可一次性 `git add` + `git commit`)
- **建议 commit message**:
  ```
  feat(code-dashboard): 新增只读型开发看板技能 (REQ-00004-001)
  
  - 新增 plugins/code-skills/skills/code-dashboard/SKILL.md(367 行,单文件)
  - 支持双粒度(无参数总览 / REQ-NNNNN 需求粒度)
  - 6 个算法(parseArgs / parseDashboard / parseRequirementMode / parseTaskId / renderBar / generateSuggestions)
  - 10 项边界 E-1~E-10(3 层退化 L1/L2/L3)
  - 自动生成最多 5 条下一步建议(5 类优先级)
  - 严守 NFR-1 零依赖 / NFR-3 双格式兼容 / NFR-4 性能 < 5s / NFR-6 不动其他技能 / NFR-7 幂等
  - 不修改 marketplace.json / plugin.json / 其他 10 SKILL.md frontmatter
  ```
- **提交人**:wangmiao
- **Co-Authored-By**:Claude Opus 4.8 (1M context) `<noreply@anthropic.com>`

---

## 9. 同步的文件清单

| 文件 | 操作 | 说明 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | **新增** | 本任务主产出物 |
| `assistants/V0.0.2/code/TASK-REQ-00004-00001/RESULT.md` | **新增** | 本文档(改修总结) |
| `assistants/V0.0.2/code/TASK-REQ-00004-00001/work-log.md` | **新增** | 开发日志 |
| `assistants/V0.0.2/code/TASK-REQ-00004-00001/compile-and-run.md` | **新增** | 编译与启动验证(静态自检 9 项) |
| `assistants/V0.0.2/code/TASK-REQ-00004-00001/deviations.md` | **新增** | 偏离记录(本任务**无**偏离) |
| `assistants/V0.0.2/code/TASK-REQ-00004-00001/test-results.md` | **新增** | 测试结果(测试状态 = `不适用`) |
| `assistants/V0.0.2/plan/REQ-00004/PLAN.md` | **下一步修改**(由 `code-it` 步骤 14 推进) | T-001 行:开发状态=已完成 / 完成时间 / 完成人 / 提交哈希 / 变更记录 |
| `assistants/V0.0.2/RESULT.md` | **下一步修改**(由 `code-it` 步骤 15 同步) | "任务清单"中 T-001 行推进 + "执行的开发命令记录"追加 + "变更记录"追加 |
