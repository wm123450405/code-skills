# 逻辑行计算 — 共享库(由 code-it / code-check 共用)

- 所属技能:`code-it` / `code-check`
- 创建时间:2026-06-22 15:00
- 适用版本:V0.0.3
- 来源:REQ-00039 详细设计 §5(4 个函数伪代码)

## 函数 1:`detectLocTool()`

### 用途

检测本机可用的代码行统计工具,用于"实际代码逻辑行"计算。

### 签名

```
function detectLocTool(): "tokei" | "cloc" | "heuristic"
```

### 算法

```
1. Bash: tokei --version → exit 0 → return "tokei"
2. Bash: cloc --version → exit 0 → return "cloc"
3. 否则 return "heuristic"
```

### 屏显契约

```
=== code-it 逻辑行统计(步骤 8 末尾)===
检测方式:tokei / cloc / heuristic
```

### 错误处理

- 工具检测失败(Bash 退出码非 0)→ 屏显 `⚠ 建议安装 tokei/cloc 以获得准确逻辑行统计;本次回退到启发式` + 返回 `"heuristic"`

### 性能

O(1)(2 次 Bash 调用,每次 < 0.1 秒)

## 函数 2:`calcLogicLines(filePath, tool)`

### 用途

计算单文件的"实际代码逻辑行"(`newLoc` + `totalLoc` + `detection`)。

### 签名

```
function calcLogicLines(filePath: string, tool: "tokei" | "cloc" | "heuristic"): { newLoc: number, totalLoc: number, detection: string }
```

### 算法

```
1. tool="tokei" → Bash: tokei <filePath> --output json
2. tool="cloc" → Bash: cloc <filePath> --json
3. tool="heuristic" → return heuristicLoc(filePath, lang)
4. 解析输出 → { code, comments, blanks }
5. totalLoc = code
6. return { newLoc: 0, totalLoc, detection: tool } // newLoc 由调用方根据 git diff 计算
```

### 输出示例

```json
{
  "newLoc": 25,
  "totalLoc": 80,
  "detection": "tokei"
}
```

### 错误处理

- 工具调用失败(Bash 退出码非 0)→ 返回 `{ newLoc: 0, totalLoc: 0, detection: "error" }` + 屏显 `⚠`
- 文件不存在 → 返回 `{ newLoc: 0, totalLoc: 0, detection: "error" }` + 屏显 `⚠`
- 文件过大(> 10MB)→ 跳过 + 屏显 `⚠`

### 性能

O(N),N = 文件行数(单文件,典型 50-500 行)

## 函数 3:`heuristicLoc(filePath, lang)`

### 用途

启发式回退算法,用于工具不可用时(无 tokei / cloc)的逻辑行统计。

### 签名

```
function heuristicLoc(filePath: string, lang: string): number
```

### 算法

```
1. 读文件全部行
2. 过滤空行(`^\s*$`)
3. 过滤注释行(正则,按语言):
   - Python: `^\s*(#|""")`
   - JS/TS/Go/Java/Rust: `^\s*(//|/\*|\*)`
   - Markdown: `^\s*<!--`
   - 其他语言:仅过滤空行
4. 返回剩余行数
```

### 语言检测(从扩展名推断)

| 扩展名 | 语言 |
| --- | --- |
| `.py` | `python` |
| `.js` / `.ts` / `.jsx` / `.tsx` | `javascript` |
| `.go` | `go` |
| `.java` | `java` |
| `.rs` | `rust` |
| `.md` / `.markdown` | `markdown` |
| 其他 | `unknown`(仅过滤空行) |

### 输出示例

```
Python 文件 100 行 / 30 空行 / 40 注释 / 30 逻辑 → 返回 30
JS 文件 50 行 / 5 空行 / 10 注释 / 35 逻辑 → 返回 35
```

### 精度

- 主流 5 语言(JS/TS/Go/Java/Python):~95%
- Markdown:~90%(文档字符串识别有限)
- 其他语言:~85%(仅过滤空行,字符串内注释符号不特殊处理)

### 性能

O(N),N = 文件行数(单文件,典型 50-500 行)

## 函数 4:`code-check-exceed(file, totalLoc, newLoc, threshold)`

### 用途

`code-check` 步骤 8.13 派生"代码行数超标"发现(评审用)。

### 签名

```
function code-check-exceed(file: string, totalLoc: number, newLoc: number, threshold: { total: number, new: number }): string | null
```

### 算法

```
1. 若 totalLoc > threshold.total:
   - 超出比例 = (totalLoc - threshold.total) / threshold.total
   - 级别:
     - ≤10% → "可选"
     - ≤50% → "建议改"
     - >50% → "必须改"
   - return "[代码行数超标] <file> 逻辑行(总规模)=<totalLoc> 阈值=<threshold.total> 超<P>%(级别:<级别>) 建议拆分..."
2. 若 newLoc > threshold.new:同上(级别判断 + 文案)
3. 若无超标 → return null
```

### 输出示例

```json
{
  "finding": "[代码行数超标] src/foo.ts 逻辑行(总规模)=600 阈值=500 超 20%(级别:建议改) 建议拆分..."
}
```

### 性能

O(1)

## 调用方约定

### `code-it` 步骤 8 末尾(`calcLogicLoc` 子步骤)

```
function calcLogicLoc(taskNum, timestamp):
 1. tool = detectLocTool()
 2. changedFiles = Bash: git diff --name-only HEAD~1
 3. per-file:
 - oldContent = Bash: git show HEAD~1:<file>(若存在)
 - newContent = 当前文件内容
 - oldLoc = calcLogicLines(oldContent, tool).totalLoc(若 oldContent 存在)
 - newLoc = calcLogicLines(newContent, tool).totalLoc
 - delta = newLoc - oldLoc
 4. 累计本任务逻辑行(新增) = Σ delta
 5. 累计本任务逻辑行(总规模) = Σ newLoc
 6. 写入 code/<task>/RESULT.md "## 逻辑行统计(由 code-it 内化)" 小节
```

### `code-check` 步骤 8.13

```
function checkCodeLocExceed(taskNum, threshold):
 1. 读 code/<task>/RESULT.md 的"## 逻辑行统计"小节
 2. 阈值 = 默认 500 / 200(沿用 logic-loc-defaults.md)
 3. per-file:
 - finding = code-check-exceed(file, totalLoc, newLoc, threshold)
 - 若 finding 非 null → 追加到评审发现清单
```

## 依赖

- `tokei` / `cloc` 系统命令(本仓库**不**安装,用户环境可选)
- 启发式无外部依赖(纯文件读取 + 正则)
