# 改修总结 — TASK-REQ-00035-00001

- 任务编码:TASK-REQ-00035-00001
- 任务标题:[修改] code-require 步骤 0a 过程文档判定 + 模板新增
- 需求:REQ-00035
- 触发/来源:详细设计
- 类型:修改
- 关联任务:—
- 状态:已完成
- 完成时间:2026-06-15 19:30
- 提交哈希:<待 commit>

## 1. 改修内容总览

| 改写 | 路径 | 行数变化 |
| --- | --- | --- |
| 修改 | `plugins/code-skills/skills/code-require/SKILL.md` | +45 行(在 L78 后插入"## 过程文档自适应判定"小节) |
| 新增 | `plugins/code-skills/skills/code-require/templates/process-doc-decisions.md` | +50 行(新文件) |
| 新增 | `assistants/V0.0.3/code/TASK-REQ-00035-00001/process-doc-decisions.md` | +32 行(本任务决策记录) |
| 新增 | `assistants/V0.0.3/code/TASK-REQ-00035-00001/work-log.md` | +50 行(本任务开发日志) |
| 新增 | `assistants/V0.0.3/code/TASK-REQ-00035-00001/deviations.md` | +8 行(无偏离) |

净变化:~+185 行,2 个文件修改/新增(主改),3 个任务过程文件

## 2. 详细改动

### `plugins/code-skills/skills/code-require/SKILL.md`

**锚点**:`## 工具使用约定` 段后(L78)+ `## 工作流程` 段前(L162)
**插入位置**:L78 的 `---` 与 L80 的 `## 标题解析` 之间
**新增内容**:"## 过程文档自适应判定(本需求 REQ-00035 新增,2026-06-15 起生效)"小节,包含:
- 适用过程文档清单(5 类:`materials-index` / `clarifications` / `related-requirements` / `analysis-notes` / 看板"变更记录")
- 执行流程(7 步)
- 边界与异常(E-1 / E-2 / E-3)
- 不变量(5 条:不修改 frontmatter / 不修改既有工作流程 / 不修改不要做的事 / 不触发 AskUserQuestion / 不新增 CLI 参数)

### `plugins/code-skills/skills/code-require/templates/process-doc-decisions.md`(新文件)

**章节结构**:
- 文档头(需求编码 / 版本 / 时间 / 技能)
- 决策结果(5 类过程文档判定 + 理由)
- 已生成的过程文档清单
- 变更记录

## 3. 关键决策与权衡

- **决策 1**:新小节插入位置选在 `## 工具使用约定` 之后(原锚点)而非"## 工作流程"之前(另一锚点)— 选前者因为:工具使用约定是元约定(与本节"过程文档决策"性质更接近)
- **决策 2**:`process-doc-decisions.md` 模板**只**用于 `code-require` — 其他 4 技能(code-design / code-plan / code-it / code-check)各自有独立模板(本需求拆分任务)
- **决策 3**:本节新增 3 个边界(E-1 / E-2 / E-3)与 5 个不变量,作为本节内嵌的"安全护栏",与 SKILL.md 末尾"## 不要做的事"互补

## 4. 偏离设计/规范

- 0 偏离(详见 `deviations.md`)

## 5. 验证结果

- 编译/启动/测试:**不适用**(本仓库为 markdown 文档,无构建/运行/测试)
- 静态验证:
  - `grep -c "^## 工具使用约定\|^## 过程文档自适应判定\|^## 标题解析\|^## 命令行参数解析\|^## 工作流程" code-require/SKILL.md` = 5(确认 5 个锚点小节齐全)
  - frontmatter L1-3 字节级保留(本任务仅追加,不修改顶部 frontmatter)
  - 既有"## 工作流程"小节字节级保留

## 6. 已知问题/未完成项

- 无

## 7. 关联任务与提交

- 关联任务:—
- 提交哈希:<待 commit>
- 下一任务:T-002 code-design 步骤 0a.5 过程文档判定 + 模板新增
