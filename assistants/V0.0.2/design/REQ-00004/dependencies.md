# 三方依赖评估 — REQ-00004

更新时间:2026-06-04 15:50
版本:V0.0.2

## 1. 结论先行

**本需求零新增三方依赖**(0 npm / 0 pip / 0 系统工具 / 0 Claude Code MCP)。

## 2. 锁定依据

### 2.1 需求侧锁定
- NFR-1(必须):`code-dashboard` 不引入新的 npm/pip 依赖
  > 描述:`code-dashboard` 不引入新的 npm/pip 依赖;所有输出基于 `Read` / `Glob` / `Grep` 工具 + Markdown/ASCII 字符构造

### 2.2 既有规范一致性
- `./assistants/rules/dependency-conventions.md` §规则 1(占位,`2026-06-04 10:45` 创建)尚无细则;**但**既有 10 个 `code-*` 技能的 `plugin.json` 实际声明均为"零运行时依赖":
  - `plugins/code-skills/.claude-plugin/plugin.json` 未声明 `dependencies` 字段(`marketplace-protocol §规则 1` 要求字段约束,但不强制声明 dependencies)
  - 10 个 `code-*` 技能均为"指令型 + 文档产出型",无编程语言运行时
- `./assistants/plugins/code-skills/CLAUDE.md` 显式声明:
  > 本仓库**不包含任何源代码、构建系统、测试框架、Lint 工具或包管理配置**

## 3. 评估过程(逐项排查)

### 3.1 Markdown 解析
- **需求**:解析 `RESULT.md` / `PLAN.md` 中的表格与区段
- **方案对比**:
  | 方案 | 依赖 | 评价 |
  | --- | --- | --- |
  | `marked` / `markdown-it`(npm) | +1 | ❌ 违反 NFR-1 |
  | `python-markdown` | +1 | ❌ 违反 NFR-1,且本仓库无 Python 运行时 |
  | **自实现**:用 `Read` 读全文 + 行号定位 `## 标题` + 正则匹配表格行 | 0 | ✅ 字符数 < 200,实现简单 |
- **选定**:**自实现**;依据 NFR-1 + NFR-4 性能

### 3.2 ASCII 比例条渲染
- **需求**:构造 `[████████████] 100%` 形式的固定宽度柱状图
- **方案对比**:
  | 方案 | 依赖 | 评价 |
  | --- | --- | --- |
  | `cli-progress`(npm) | +1 | ❌ 违反 NFR-1;且 cli-progress 设计为"流式进度条",本需求是"渲染静态字符" |
  | `text-progressbar` | +1 | ❌ 违反 NFR-1 |
  | **自实现**:`Math.round(percent / 100 * BAR_WIDTH)` + `█` × N + `░` × (BAR_WIDTH - N) | 0 | ✅ BAR_WIDTH = 12(Q-D3 锁定) |
- **选定**:**自实现**;字符操作,无依赖必要

### 3.3 任务编号解析
- **需求**:同时识别 `TASK-REQ-NNNNN-NNNNN` 与旧 `REQ-NNNNN-NNNNN` 两种字面
- **方案对比**:
  | 方案 | 依赖 | 评价 |
  | --- | --- | --- |
  | 第三方正则库 | +1 | ❌ 违反 NFR-1 |
  | **自实现**:2 条正则 + `match` / `exec` 内置 | 0 | ✅ JavaScript 正则原生支持 |
- **选定**:**自实现**;2 条正则各 1 行,无依赖必要
- **规范依据**:`encoding-conventions.md §规则 3` 嵌套式正则权威

### 3.4 终端彩色 / 样式
- **需求**:P0 / P1 缺陷的"醒目标记"
- **方案对比**:
  | 方案 | 依赖 | 评价 |
  | --- | --- | --- |
  | ANSI 转义码(`\x1b[31m`) | 0 | ⚠️ Windows 终端兼容性问题 |
  | `chalk`(npm) | +1 | ❌ 违反 NFR-1 |
  | **纯字符标记**:`█`(实心,P0) + `▓`(半实心,P1) | 0 | ✅ Q-3 锁定此方案 |
- **选定**:**纯字符标记**;Q-3 已锁定

### 3.5 时间格式化
- **需求**:显示"创建时间" / "完成时间"(可选,V0.0.2 看板"任务清单"已有此列)
- **方案对比**:
  | 方案 | 依赖 | 评价 |
  | --- | --- | --- |
  | `date-fns` / `moment` | +1 | ❌ 违反 NFR-1 |
  | **原样透传**(读看板时保留 `YYYY-MM-DD` 字面) | 0 | ✅ 看板已用 ISO 日期格式 |
- **选定**:**原样透传**;需求总览模式不显式显示时间(在 §6.2 段 1 布局中未含时间字段);需求粒度模式按字面显示

## 4. 依赖矩阵(与既有 10 个技能对比)

| 技能 | 运行时依赖 | 文档产出 |
| --- | --- | --- |
| `code-init` | 0 | `INIT-REPORT.md` |
| `code-version` | 0 | `RESULT.md` |
| `code-rule` | 0 | `rules/*.md` |
| `code-require` | 0 | `require/<REQ>/RESULT.md` 等 |
| `code-design` | 0 | `design/<REQ>/RESULT.md` 等 |
| `code-plan` | 0 | `plan/<REQ>/PLAN.md` + `RESULT.md` |
| `code-it` | 0 | `code/<TASK>/RESULT.md` |
| `code-unit` | 0 | `test/<TASK>/RESULT.md` |
| `code-fix` | 0 | `fix/<BUG>/RESULT.md` |
| `code-review` | 0 | `review/<REQ>/REVIEW-REPORT.md` 等 |
| **`code-dashboard`** | **0** | **无**(屏幕输出,NFR-7 幂等) |

> **新技能延续了"零运行时依赖"的项目惯例**;`code-dashboard` 是首个"无文档产出"的技能,这是其与既有技能的本质差异。

## 5. 工具集(`code-dashboard` 实际使用的 Claude Code 工具)
- `Read`:读 `.current-version` / `RESULT.md` / `require/<REQ>/RESULT.md` / `plan/<REQ>/PLAN.md`
- `Glob`:列需求目录(边界 E-3 时)
- `Grep`:区段内行号定位 + 表格行匹配
- **不使用**:`Write` / `Edit` / `Bash`(NFR-7 严守纯只读;FR-7 AC-7.1 验证 `git status` clean)
- **不使用**:`WebFetch` / `WebSearch` / `Task` / `Agent`(与 `code-review` 行为一致)

## 6. 锁定结论
| 维度 | 锁定 |
| --- | --- |
| 新增依赖 | **0** |
| 使用工具 | `Read` / `Glob` / `Grep`(NFR-7) |
| 文档产出 | **0**(屏幕输出,NFR-7 幂等) |
| 规范触发 | `dependency-conventions §规则 1`(占位)无冲突;NFR-1 直接锁 |

## 7. 后续(若 `code-rule` 在 `dependency-conventions §规则 1` 中添加细则)
若未来 `code-rule` 沉淀新的"三方依赖准入"规则(例如"新增依赖必须先经 `code-design` 评审"或"必须锁定到具体 minor 版本"),本需求**不**需要追溯(因 0 新增);但下游 `code-plan` 拆任务时,需将"零依赖验证"作为 T-1 子任务的 AC 之一。
