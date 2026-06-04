# 改修总结 — TASK-REQ-00004-00002

- 任务编码:TASK-REQ-00004-00002
- 标题:(可选)改 `plugins/code-skills/CLAUDE.md` 追加"指引 N: code-dashboard 行为约定"
- 需求编码:REQ-00004
- 所属版本:V0.0.2
- 类型:新增
- 触发/来源:需求新增
- 状态:**已完成**
- 责任人:wangmiao
- 创建:2026-06-04 16:50
- 完成:2026-06-04 16:55
- 最近更新:2026-06-04 16:55
- 当前版本:v1

---

## 1. 任务信息

| 字段 | 值 |
| --- | --- |
| 任务编号 | TASK-REQ-00004-00002 |
| 标题 | (可选)改 `plugins/code-skills/CLAUDE.md` 追加"指引 N: code-dashboard 行为约定" |
| 类型 | 新增(修改既有文件 1 段) |
| 触发/来源 | 需求新增 |
| 开发状态 | **已完成** |
| 测试状态 | **不适用**(纯 Markdown 文档) |
| 任务来源 | `./assistants/V0.0.2/plan/REQ-00004/PLAN.md` §3 |
| 设计依据 | `./assistants/V0.0.2/plan/REQ-00004/RESULT.md` §3 / `module-breakdown §3.4` 可选 M-3 |
| **用户授权依据** | PLAN.md 行 194 "用户在 `code-it` 阶段明确授权" 路径;用户主动调用 `code-it REQ-00004-002` 即为信号 |

---

## 2. 改修内容总览

### 2.1 改动文件清单
- **修改 1 个**:`plugins/code-skills/CLAUDE.md`(追加 8 行,134 → 142)

### 2.2 改动细节
- 位置:`### 指引 1: (待添加)` 之后(PLAN.md 行 163 锁定)
- 新增内容(7 行,含空行):
  ```markdown
  ### 指引 N: `code-dashboard` 行为约定
  - 展示策略:ASCII 进度表 + 文本柱状图(固定 12 字符 + `█` / `░` / `▓`)
  - 建议策略:5 类优先级(高/中/低/—)+ 最多 5 条;命令严格按既有 10 个 `code-*` SKILL.md 真实语法
  - 解析锚点:看板 3 区段(需求清单 / 任务清单 / 缺陷清单);按 `^## .*$` 定位 + 表格行 `^\| .* \|$` 匹配
  - 双格式兼容:任务编号新格式 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` 优先;旧格式 `^(REQ|BUG)-\d{5}-\d{5}$` 透传
  - 状态字面:严格按字面匹配(不归一化 `已完成(需求分析)` 到 `已完成`)
  - 工具集:仅 `Read` / `Glob` / `Grep`;禁用 `Write` / `Edit` / `Bash`
  ```

### 2.3 未改动文件清单(对照 NFR-6 严守)
- ❌ 未改 `marketplace.json`
- ❌ 未改 `plugin.json`
- ❌ 未改其他 10 个 `code-*` SKILL.md frontmatter
- ❌ 未改 `plugins/code-skills/CLAUDE.md` 任何已有行(git diff 验证)
- ❌ 未改 `plugins/code-skills/README.md` + `README.en.md`(T-003 仍"待开始",未授权)
- ❌ 未改 `./assistants/rules/` 下任何文件
- ❌ 未改 `./assistants/V0.0.2/require/` / `design/` / `plan/RESULT.md` 下任何文件

### 2.4 文档大小
- `CLAUDE.md`:134 → 142 行(+8)

---

## 3. 详细改动(CLAUDE.md 章节结构)

### 3.1 修改位置
- 段落:`## AI 工作约定(由 code-rule 维护)`(行 129)
- 子段:`### 指引 1: (待添加)`(行 134)
- **追加位置**:行 134 之后(原占位保留,新指引在其后)

### 3.2 追加内容(6 个子项 + 1 标题)
| 子项 | 来源 | 引用 SKILL.md 章节 |
| --- | --- | --- |
| 展示策略 | PLAN.md 行 165 | 步骤 4 段 1 + 附录 B(`renderBar`) |
| 建议策略 | PLAN.md 行 166 | 步骤 5 + 算法 3(`generateSuggestions`) |
| 解析锚点 | PLAN.md 行 167 | 步骤 3 + 算法 1(`parseDashboard`) |
| 双格式兼容 | PLAN.md 行 168 | 附录 A(`parseTaskId`)+ NFR-3 |
| 状态字面 | PLAN.md 行 169 | 步骤 4 段 1(P-A1 锁定) |
| 工具集 | PLAN.md 行 170 | `## 工具使用约定`(NFR-7) |

### 3.3 与既有"指引 1"占位的关系
- `### 指引 1: (待添加)` **保留原样**(不替换,不变更)
- `### 指引 N: code-dashboard 行为约定` **追加**在"指引 1"之后
- 序号"N"的含义:由 `code-rule` 后续填充时决定具体编号;本任务**不**指定

---

## 4. 关键决策与权衡

### 4.1 严格按 PLAN.md 字面落地(零自由发挥)
- 6 个子项的内容、顺序、字符级一致
- 不引入新的格式约定 / 新的章节组织
- 保持与既有"指引 1"占位一致(3 级标题 + 列表)

### 4.2 关于"用户授权"的决策
- PLAN.md 行 193 "本设计**建议不**触发" — 提示性,不强制
- PLAN.md 行 194 "触发条件:用户在 `code-it` 阶段明确授权" — 触发条件
- 用户**主动调用** `code-it REQ-00004-002` 满足触发条件
- **执行决策**:覆盖 PLAN.md "建议不触发"提示,以用户命令为最终信号

### 4.3 关于"code-rule 覆盖"风险
- CLAUDE.md 行 131 显式声明:"本小节由 `code-rule` 技能维护;手动修改可能被 `code-rule` 覆盖"
- **本任务接受此风险**:用户授权明确,即使 `code-rule` 后续覆盖,本任务也已完成其历史使命
- 详细说明在 `deviations.md`

### 4.4 命名 / 错误处理风格与既有 SKILL.md 一致
- 子项格式:`- <字段名>:<内容>`(与既有 `code-dashboard` SKILL.md 节标题风格一致)
- 代码字面:用反引号包裹(`█` / `Read` / `Write` 等)
- 强调:`**` 双星号(本任务无强调)

---

## 5. 偏离设计/规范的地方

### 5.1 代码偏离设计
**无**(6 个子项字面与 PLAN.md 行 165-171 严格一致)

### 5.2 代码偏离规范
**无**(本任务严格按 NFR-6 边界实施,未触碰 `marketplace.json` / `plugin.json` / 其他 10 SKILL.md)

### 5.3 任务范围扩展
**无**(本任务**只**修改 `CLAUDE.md` 1 个文件,仅追加 8 行)

### 5.4 详细列表
详见 `deviations.md`(本任务**无**偏离需要记录;仅 1 项"用户授权决策"说明)

---

## 6. 验证结果

### 6.1 编译/构建
- **不适用**(本仓库无构建系统,详见 `compile-and-run.md`)

### 6.2 启动运行
- **不适用**(本任务是"修改 1 个 Markdown 文档",无运行面)

### 6.3 静态自检(7/7 通过)
详见 `compile-and-run.md`:
- ✅ 行数变化 134 → 142(纯追加 +8)
- ✅ 节标题顺序(`指引 1` 占位保留,`指引 N` 追加其后)
- ✅ Grep "指引 N" 命中 1 处
- ✅ 6 个子项完整(按 PLAN.md 字面落地)
- ✅ git diff 净度(仅 8 行纯追加,无任何已有行修改)
- ✅ 未触碰其他段(NFR-6 边界)
- ✅ `marketplace.json` / `plugin.json` / 其他 10 SKILL.md 全部未触碰

### 6.4 动态实测(0 项,本任务无动态可验)
- 本任务**只**修改 1 个 Markdown 文档,无运行时行为
- 所有验证均为"静态自检"

---

## 7. 已知问题/未完成项

### 7.1 本任务无已知问题
- 静态自检 7/7 通过
- 与 T-001 落地的 SKILL.md 行为**完全一致**
- 无任何"留给后续任务或 PR 评审"的项目

### 7.2 留给后续 follow-up(非本任务范围)
- T-003(可选):改 `README.md` + `README.en.md` 技能清单(用户未授权,**不**触发)
- `code-rule` 后续沉淀:可能覆盖本段(本任务**接受**此风险)
- F-1:`code-review/SKILL.md` frontmatter `<version>` 笔误(超出 REQ-00004 范围)

---

## 8. 关联任务与提交

### 8.1 关联任务
- **关联任务**:无
- **横向关联**:T-001(`code-dashboard/SKILL.md`)`code-it` 已完成;本任务的"指引 N"内容与 T-001 落地的 SKILL.md 行为**完全一致**
- **后续任务**:T-003(可选)由用户授权才落地

### 8.2 git 提交
- **本任务暂未提交**(本工作空间是 git worktree,用户后续可一次性 `git add` + `git commit`)
- **建议 commit message**:
  ```
  chore(code-dashboard): 在 CLAUDE.md 追加"指引 N"约定 (REQ-00004-002)
  
  - 修改 plugins/code-skills/CLAUDE.md(+8 行:指引 N 标题 + 6 子项)
  - 触发条件:用户主动调用 code-it REQ-00004-002(覆盖 PLAN.md "建议不触发"提示)
  - 内容:展示策略 / 建议策略 / 解析锚点 / 双格式兼容 / 状态字面 / 工具集
  - 来源:与 TASK-REQ-00004-00001 落地的 SKILL.md 行为严格一致
  - 接受 code-rule 后续覆盖本段的风险(由 CLAUDE.md 显式声明)
  - 不修改 marketplace.json / plugin.json / 其他 10 SKILL.md frontmatter
  ```
- **提交人**:wangmiao
- **Co-Authored-By**:Claude Opus 4.8 (1M context) `<noreply@anthropic.com>`

---

## 9. 同步的文件清单

| 文件 | 操作 | 说明 |
| --- | --- | --- |
| `plugins/code-skills/CLAUDE.md` | **修改 1 段**(追加 8 行) | 本任务主产出物 |
| `assistants/V0.0.2/code/TASK-REQ-00004-00002/RESULT.md` | **新增** | 本文档(改修总结) |
| `assistants/V0.0.2/code/TASK-REQ-00004-00002/work-log.md` | **新增** | 开发日志 |
| `assistants/V0.0.2/code/TASK-REQ-00004-00002/compile-and-run.md` | **新增** | 编译与启动验证(静态自检 7 项) |
| `assistants/V0.0.2/code/TASK-REQ-00004-00002/deviations.md` | **新增** | 偏离记录(本任务**无**偏离;含"用户授权"决策说明) |
| `assistants/V0.0.2/code/TASK-REQ-00004-00002/test-results.md` | **新增** | 测试结果(测试状态 = `不适用`) |
| `assistants/V0.0.2/plan/REQ-00004/PLAN.md` | **下一步修改**(由 `code-it` 步骤 14 推进) | T-002 行:开发状态=已完成 / 完成时间 / 完成人 / 提交哈希 / 变更记录 |
| `assistants/V0.0.2/RESULT.md` | **下一步修改**(由 `code-it` 步骤 15 同步) | "任务清单"中 T-002 行推进 + "执行的开发命令记录"追加 + "变更记录"追加 |
