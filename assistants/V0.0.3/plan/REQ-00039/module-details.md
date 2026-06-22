# 模块详细化 — REQ-00039

更新时间:2026-06-22 15:00
版本:V0.0.3

## 模块 1:`logic-loc.md`(共享库)

- **路径**:`plugins/code-skills/skills/code-it/lib/logic-loc.md`
- **状态**:**新增**
- **关键类/函数**(伪代码):

```markdown
## 函数 1:detectLocTool()
- 输入:—
- 输出:"tokei" | "cloc" | "heuristic"
- 算法:
 1. Bash: tokei --version → exit 0 → return "tokei"
 2. Bash: cloc --version → exit 0 → return "cloc"
 3. 否则 return "heuristic"

## 函数 2:calcLogicLines(filePath, tool)
- 输入:文件路径 + 工具类型
- 输出:{ newLoc: number, totalLoc: number, detection: string }
- 算法:
 1. tool="tokei" → Bash: tokei <file> --output json
 2. tool="cloc" → Bash: cloc <file> --json
 3. tool="heuristic" → heuristicLoc(filePath, lang)
 4. 解析输出 → { code, comments, blanks }
 5. totalLoc = code

## 函数 3:heuristicLoc(filePath, lang)
- 输入:文件路径 + 语言(默认从扩展名推断)
- 输出:逻辑行数
- 算法(5 主流语言):
 1. 读文件全部行
 2. 过滤空行(`^\s*$`)
 3. 过滤注释行(正则,按语言):
 - Python: `^\s*(#|""")`
 - JS/TS/Go/Java/Rust: `^\s*(//|/\*|\*)`
 - Markdown: `^\s*<!--`
 - 其他语言:仅过滤空行
 4. 返回剩余行数

## 函数 4:code-check-exceed(file, totalLoc, newLoc, threshold)
- 输入:文件路径 + 逻辑行(总规模)+ 逻辑行(新增)+ 阈值
- 输出:发现描述(string)
- 算法:
 1. 若 totalLoc > threshold:
 - 超 ≤10% → return "[代码行数超标] <file> 逻辑行(总规模)=<N> 阈值=<M> 超<P>%(级别:可选)"
 - 超 ≤50% → return "... (级别:建议改)"
 - 超 >50% → return "... (级别:必须改)"
 2. 若 newLoc > threshold:同上
 3. 若无超标 → return null
```

- **调用顺序**:
 1. `code-it` 步骤 8 末尾 → `detectLocTool` → `calcLogicLines`
 2. `code-check` 步骤 8.13 → `code-check-exceed`
- **状态归属**:无状态(纯函数)
- **并发模型**:无(同步执行)
- **错误处理范式**:`Bash` 命令失败 → 返回 `"heuristic"` + 屏显 `⚠`;文件读取失败 → 跳过该文件 + 屏显警告
- **日志埋点**:无(纯函数)
- **与概要设计的对应**:§5 模块拆分(`logic-loc.md`)
- **符合的规范**:`module-conventions §规则 1`(新建在 `lib/` 而非 `templates/`)+ `naming-conventions §规则 1`(kebab-case)

## 模块 2:`logic-loc-defaults.md`(默认值)

- **路径**:`plugins/code-skills/skills/code-it/lib/logic-loc-defaults.md`
- **状态**:**新增**
- **关键字段**:
 ```
 单文件逻辑行总规模阈值:500
 单文件逻辑行新增阈值:200
 ```
- **调用顺序**:`code-check` 步骤 8.13 读默认值 → 用户配置覆盖(FR-5)
- **状态归属**:无状态(纯文本)
- **与概要设计的对应**:§5 模块拆分(`logic-loc-defaults.md`)
- **符合的规范**:`module-conventions §规则 1`

## 模块 3:`code-it/SKILL.md` 步骤 8 末尾(修改既有)

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md`
- **状态**:**修改既有**(在 §"## 步骤 8 实施开发"末尾追加 2 子步骤)
- **关键子步骤**:

```markdown
### 步骤 8.X — 逻辑行统计(由 code-it 内化)
1. detectLocTool()(沿用 `lib/logic-loc.md` §函数 1)
 屏显契约:
 === code-it 逻辑行统计(步骤 8 末尾)===
 检测方式:tokei / cloc / heuristic
2. calcLogicLoc(taskNum, timestamp):
 a. git diff --numstat HEAD~1 -- <task 涉及文件> → 变更文件列表
 b. 对每个变更文件:
 - calcLogicLines(filePath, detectLocTool())
 - 若修改前可获取 → newLoc = totalLoc - 修改前逻辑行
 - 若新建文件 → newLoc = totalLoc
 c. 累计本任务逻辑行(新增)= Σ newLoc
 d. 累计本任务逻辑行(总规模)= Σ totalLoc
 e. 写 code/<task>/RESULT.md 新增"## 逻辑行统计"小节
 f. 失败 → 屏显 ⚠ + 跳过(不阻断 code-it)
```

- **屏显契约**(沿用既有 `code-it` 步骤 8a.4 / 8.5.3 模式):
 ```
 === code-it 逻辑行统计(步骤 8 末尾)===
 任务:<任务编码>
 变更文件:N 个
 逻辑行(新增):<Σ>
 逻辑行(总规模):<Σ>
 检测方式:tokei / cloc / heuristic
 ```
- **触发条件**:`code-it` 步骤 1 判定为任务分支(`^TASK-REQ-\d{5}-\d{5}$` 5+5 位嵌套式);缺陷分支(`^TASK-BUG-...`)**不**触达(NFR-8)
- **不修改**:`code-it` 既有步骤 8 子步骤结构 / frontmatter / 既有"## 工作流程"小节 / "## 不要做的事"小节
- **与概要设计的对应**:§5 模块拆分(`code-it/SKILL.md`)
- **符合的规范**:`skill-conventions §规则 1 + §规则 2`

## 模块 4:`code-check/SKILL.md` 步骤 8.13(修改既有)

- **路径**:`plugins/code-skills/skills/code-check/SKILL.md`
- **状态**:**修改既有**(在 §"## 步骤 8 逐任务评审"末尾追加 1 子步骤 + 评审维度速查表新增第 13 维度)
- **关键子步骤**:

```markdown
### 步骤 8.13 — 代码行数超标检查
1. 读 code/<task>/RESULT.md 的"## 逻辑行统计"小节
2. 读阈值配置:
 - 默认:500(总规模)/ 200(新增)(沿用 `lib/logic-loc-defaults.md`)
 - 用户配置:`require/<需求>/RESULT.md` "## 阈值配置"小节(FR-5 可选)
3. 对每个变更文件:
 - 若 totalLoc > 阈值 → code-check-exceed(file, totalLoc, newLoc, threshold)
 - 若 newLoc > 阈值 → code-check-exceed(file, totalLoc, newLoc, threshold)
4. 派生发现入评审发现清单
```

- **评审维度速查表新增**:
 | 优先级 | 维度 | 不通过时一般标 |
 | --- | --- | --- |
 | P3 | 代码行数超标 | 可选 / 建议改 / 必须改(按超标百分比) |
- **不修改**:`code-check` 既有步骤 8.1 ~ 8.12 子步骤(字节级沿用)
- **与概要设计的对应**:§5 模块拆分(`code-check/SKILL.md`)
- **符合的规范**:`skill-conventions §规则 1 + §规则 2`

## 模块 5:`code-it/templates/RESULT.md`(修改既有)

- **路径**:`plugins/code-skills/skills/code-it/templates/RESULT.md`
- **状态**:**修改既有**(在既有章节中新增"## 逻辑行统计(由 code-it 内化)"小节示例)
- **新增小节内容**(示例):
 ```markdown
 ## 逻辑行统计(由 code-it 内化)

 | 文件 | 逻辑行(新增) | 逻辑行(总规模) | 检测方式 |
 | --- | --- | --- | --- |
 | src/foo.ts | 25 | 80 | tokei |
 | src/bar.py | 10 | 30 | tokei |
 | **本任务汇总** | **35** | **110** | — |
 ```
- **不修改**:`code-it/templates/RESULT.md` 既有章节(字节级保留)
- **与概要设计的对应**:§5 模块拆分(`code-it/templates/RESULT.md`)
- **符合的规范**:`skill-conventions §规则 1` + `template-conventions`(沿用既有)