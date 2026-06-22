# 设计笔记 — REQ-00039

更新时间:2026-06-22 14:30
版本:V0.0.3

## 1. 关键设计问题清单

| # | 问题 | 候选方案 | 选定 |
| --- | --- | --- | --- |
| Q-1 | 逻辑行计算函数放在哪? | A. `code-it/SKILL.md` 内嵌(伪代码)<br>B. `code-it/lib/logic-loc.md` 新建共享库<br>C. `code-check/SKILL.md` 内嵌(伪代码) | **B** — 共享避免重复 |
| Q-2 | tokei/cloc 检测逻辑在哪? | A. `code-it/SKILL.md` 步骤 8 内嵌<br>B. `code-it/lib/logic-loc.md` 共享库<br>C. `code-check/SKILL.md` 步骤 8 内嵌 | **B** — 与逻辑行计算函数同库 |
| Q-3 | heuristic 算法放哪? | A. `code-it/lib/logic-loc.md` 共享<br>B. `code-it/SKILL.md` 步骤 8 内嵌<br>C. `code-check/SKILL.md` 步骤 8 内嵌 | **A** — 与 tokei/cloc 检测同库 |
| Q-4 | 阈值默认值位置? | A. `code-it/lib/logic-loc-defaults.md` 新建<br>B. `code-check/SKILL.md` 步骤 8.13 内嵌<br>C. 需求 RESULT.md "## 阈值配置"小节 | **A + C** — 默认值在库,用户配置在需求 |
| Q-5 | `code-check` 步骤 8.13 派生发现格式? | A. 字节级沿用 8.12 的"行数比例警告"格式<br>B. 全新格式 | **A** — 字节级沿用减少学习成本 |
| Q-6 | "## 逻辑行统计"小节在 `code/<task>/RESULT.md` 位置? | A. 顶部(章节追加)<br>B. 末尾(章节追加)<br>C. 中间(沿用既有"## 单元测试"位置) | **C** — 沿用既有"## 单元测试"小节位置(模板内既有),便于 `code-check` 解析 |
| Q-7 | 缺陷分支是否完全跳过 `calcLogicLoc`? | A. 完全跳过(NFR-8)<br>B. 启发式 fallback<br>C. 仅跳过 tokei/cloc 调用,仍计算 | **A** — 用户原话:"缺陷分支(`^TASK-BUG-...`)**不**触达(沿用既有步骤 8a 守卫规则)" |

## 2. 候选方案对比

### 2.1 Q-1 逻辑行计算函数位置

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| A. `code-it/SKILL.md` 内嵌 | 1 文件搞定;`code-it` 自身可单读 | `code-check` 需重复定义;违反 DRY |
| B. `code-it/lib/logic-loc.md` 新建 | 共享避免重复;沿用既有 `module-conventions.md` `templates/` 留作历史不删 — 新建在 `lib/` 而非 `templates/` | 1 个新文件 |
| C. `code-check/SKILL.md` 内嵌 | `code-check` 自身可单读 | `code-it` 需重复定义;违反 DRY |

**选定 B**(共享避免重复 + `code-it/lib/` 沿用既有命名约定)。

### 2.2 Q-5 `code-check` 步骤 8.13 派生发现格式

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| A. 字节级沿用 8.12 | 学习成本低;屏显格式一致 | 略限制表达 |
| B. 全新格式 | 可定制 | 学习成本高 |

**选定 A**(字节级沿用,沿用 NFR-3 零规范变更)。

### 2.3 Q-7 缺陷分支跳过策略

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| A. 完全跳过 | 简单;与 REQ-00038 一致 | 缺陷路径完全无 metadata |
| B. 启发式 fallback | 仍能收集 metadata | 启发式精度 ~95% 不必要 |
| C. 仅跳过 tokei/cloc | 仍计算 | 复杂;无价值 |

**选定 A**(完全跳过,沿用 NFR-8)。

## 3. 选定方案字面

### 3.1 库设计:`plugins/code-skills/skills/code-it/lib/logic-loc.md`

**结构**:
```markdown
# 逻辑行计算 — 共享库(由 code-it / code-check 共用)

## 函数 1:detectLocTool()
- 输入:—
- 输出:"tokei" | "cloc" | "heuristic"
- 算法:
 1. Bash: tokei --version → exit 0 → return "tokei"
 2. Bash: cloc --version → exit 0 → return "cloc"
 3. 否则 return "heuristic"

## 函数 2:calcLogicLines(filePath, tool)
- 输入:文件路径 + 工具类型
- 输出:{ newLoc, totalLoc, detection }
- 算法:
 1. tool="tokei" → Bash: tokei <file> --output json
 2. tool="cloc" → Bash: cloc <file> --json
 3. tool="heuristic" → 启发式(读全文 + 过滤空行 + 过滤注释行)
 4. 解析输出 → { code, comments, blanks }
 5. totalLoc = code

## 函数 3:heuristicLoc(filePath, lang)
- 输入:文件路径 + 语言(默认从扩展名推断)
- 输出:逻辑行数
- 算法(5 主流语言):
 - Python: 过滤 `^\s*(#|""")`
 - JS/TS/Go/Java/Rust: 过滤 `^\s*(//|/\*|\*)`
 - Markdown: 过滤 `^\s*<!--`
 - 其他语言: 过滤 `^\s*$`(只去空行)

## 函数 4:code-check-exceed(file, totalLoc, newLoc, threshold)
- 输入:文件路径 + 逻辑行(总规模)+ 逻辑行(新增)+ 阈值
- 输出:发现描述(P3)
- 算法:
 1. 若 totalLoc > threshold:
 - 超 ≤10% → 级别 "可选"
 - 超 ≤50% → 级别 "建议改"
 - 超 >50% → 级别 "必须改"
 - 返回 "[代码行数超标] <file> ..."
 2. 若 newLoc > threshold:同上
```

### 3.2 `code-it` 步骤 8 末尾追加 2 子步骤

**子步骤 1:`detectLocTool`**(沿用 `lib/logic-loc.md` §函数 1)
**子步骤 2:`calcLogicLoc`**(沿用 `lib/logic-loc.md` §函数 2)

### 3.3 `code-check` 步骤 8 末尾追加 1 子步骤

**子步骤 13:`code-check-exceed`**(沿用 `lib/logic-loc.md` §函数 4)
+ 评审维度速查表新增第 13 维度

### 3.4 模板改造:`plugins/code-skills/skills/code-it/templates/RESULT.md`

新增"## 逻辑行统计(由 code-it 内化)"小节示例(沿用既有"## 单元测试"位置 + 格式)

### 3.5 阈值默认值:`plugins/code-skills/skills/code-it/lib/logic-loc-defaults.md`

```
单文件逻辑行总规模阈值:500
单文件逻辑行新增阈值:200
```

## 4. 不变量(NFR)

- **不**修改 `code-it` / `code-check` frontmatter(L1-3 字节级保留)
- **不**修改既有"## 工作流程"小节 / "## 不要做的事"小节
- **不**修改其他 9 个 `code-*` 技能 SKILL.md
- **不**修改 `code-check` 步骤 8.1 ~ 8.12 子步骤(字节级沿用)
- **不**修改 `code-it` 步骤 8a / 8.5(REQ-00038 改造范围)
- **不**修改 `code-it` 步骤 0a / 步骤 1 ~ 7(原有结构)
- **不**触发 `AskUserQuestion`
- **不**新增 CLI 参数
- **不**新增三方依赖(沿用既有 tokei/cloc 系统命令)

## 5. 风险与回退

### 5.1 风险

- **R-1**:tokei / cloc 在用户环境**未**安装 → 启发式 fallback(精度 ~95%) — 用户已接受(上游 RESULT.md §FR-2 字面)
- **R-2**:启发式不支持的语言(Swift / Kotlin / Scala 等)→ 退化到"统计非空非注释行"(纯字符串匹配) — 用户已接受
- **R-3**:跨平台路径分隔符(Windows `\` / Unix `/`)→ 沿用 `path.posix` 规范化
- **R-4**:`code-it` 步骤 8 末尾追加子步骤 → 与步骤 9 ~ 12 顺序保持 — `calcLogicLoc` 失败**不**阻断(沿用 NFR-7)
- **R-5**:`code-check` 步骤 8.13 新增子步骤 → 与既有 8.1 ~ 8.12 协同 — 8.13 派生发现走既有"必须改 / 建议改 / 可选"分级(字节级沿用 8.12 格式)

### 5.2 回退

- 若 `calcLogicLoc` 引发 `code-it` 步骤 9-12 异常 → `Bash: git revert HEAD`(单 commit 模式)
- 若 `code-check` 8.13 误触发 → 屏显 `⚠ 步骤 8.13 异常:...`,不阻断步骤 8.14(若有)或步骤 13 同步
- 若 tokei/cloc 检测失败 → 启发式回退自动生效,**不**需手动介入

## 6. 与上游 REQ-00038 / REQ-00037 / REQ-00034 的协同

- **REQ-00038**(模块粒度单测):`code-it` 步骤 8a / 8.5 — 本需求改步骤 8 末尾,**不冲突**
- **REQ-00037**(缺陷修复流程):`code-it` §缺陷分支 17-25 — 本需求缺陷分支不触达(NFR-8)
- **REQ-00034**(`code-unit` 整合进 `code-it`):步骤 8a / 8.5 — 本需求**不**修改 7 项检查 + 3 类任务判定

## 7. 任务粒度初判(5 任务)

- T-1:共享库 `logic-loc.md` + `logic-loc-defaults.md` 新建
- T-2:`code-it` 步骤 8 末尾追加 `detectLocTool` + `calcLogicLoc` 子步骤 + 屏显契约
- T-3:`code-check` 步骤 8.13 新增 + 评审维度速查表新增第 13 维度
- T-4:`code-it/templates/RESULT.md` 模板"## 逻辑行统计"小节新增示例
- T-5:端到端验证 + 末尾兜底提交

(待 `code-plan` 阶段细化,本笔记仅给粒度初判)