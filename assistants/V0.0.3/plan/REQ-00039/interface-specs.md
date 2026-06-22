# 接口详细规格 — REQ-00039

更新时间:2026-06-22 15:00
版本:V0.0.3

## 接口 1:`detectLocTool()`

- **形式**:Bash 命令包装函数(Markdown 伪代码 + 实际 Bash 调用)
- **路径/签名**:
 ```
 function detectLocTool(): "tokei" | "cloc" | "heuristic"
 ```
- **入参**:—
- **出参**:
 ```json
 {
 "tool": "tokei" | "cloc" | "heuristic"
 }
 ```
- **错误码**:N/A(纯函数,失败返回 `"heuristic"` + 屏显 `⚠`)
- **示例**:
 - 正常 1:`tokei --version` exit 0 → 返回 `"tokei"`
 - 正常 2:`cloc --version` exit 0 → 返回 `"cloc"`
 - 退化:两者都不存在 → 返回 `"heuristic"` + 屏显 `⚠ 建议安装 tokei/cloc`
- **版本策略**:N/A
- **依据规范**:`./assistants/rules/skill-conventions.md §规则 1`

## 接口 2:`calcLogicLines(filePath, tool)`

- **形式**:Bash 命令包装函数 + 启发式 fallback
- **路径/签名**:
 ```
 function calcLogicLines(filePath: string, tool: "tokei" | "cloc" | "heuristic"): { newLoc: number, totalLoc: number, detection: string }
 ```
- **入参**:
 ```json
 {
 "filePath": "src/foo.ts",
 "tool": "tokei"
 }
 ```
- **出参**:
 ```json
 {
 "newLoc": 25,
 "totalLoc": 80,
 "detection": "tokei"
 }
 ```
- **错误码**:N/A(失败返回 `{ newLoc: 0, totalLoc: 0, detection: "error" }` + 屏显 `⚠`)
- **示例**:
 - `tokei src/foo.ts --output json`:
 ```json
 {
 "TypeScript": {
 "code": 80,
 "comments": 25,
 "blanks": 15
 }
 }
 ```
 → `{ newLoc: 0, totalLoc: 80, detection: "tokei" }`(新建文件)
 - `cloc src/foo.ts --json`:类似 tokei
 - `heuristicLoc`:返回 `{ newLoc: <计算>, totalLoc: <计算>, detection: "heuristic" }`
- **版本策略**:N/A
- **依据规范**:`./assistants/rules/skill-conventions.md §规则 1`

## 接口 3:`heuristicLoc(filePath, lang)`

- **形式**:纯函数(读文件 + 正则过滤)
- **路径/签名**:
 ```
 function heuristicLoc(filePath: string, lang: string): number
 ```
- **入参**:
 ```json
 {
 "filePath": "src/foo.py",
 "lang": "python"
 }
 ```
- **出参**:
 ```json
 {
 "logicLoc": 30
 }
 ```
- **错误码**:N/A(失败返回 `0` + 屏显 `⚠`)
- **示例**:
 - Python 文件 100 行 / 30 空行 / 40 注释 / 30 逻辑 → 返回 `30`
 - JS 文件 50 行 / 5 空行 / 10 注释 / 35 逻辑 → 返回 `35`
- **语言检测**:从扩展名推断
 - `.py` → `python`
 - `.js` / `.ts` / `.jsx` / `.tsx` → `javascript`
 - `.go` → `go`
 - `.java` → `java`
 - `.rs` → `rust`
 - `.md` / `.markdown` → `markdown`
 - 其他 → `unknown`(仅过滤空行)
- **依据规范**:`./assistants/rules/skill-conventions.md §规则 1`

## 接口 4:`code-check-exceed(file, totalLoc, newLoc, threshold)`

- **形式**:派生发现生成函数(纯函数)
- **路径/签名**:
 ```
 function code-check-exceed(file: string, totalLoc: number, newLoc: number, threshold: { total: number, new: number }): string | null
 ```
- **入参**:
 ```json
 {
 "file": "src/foo.ts",
 "totalLoc": 600,
 "newLoc": 250,
 "threshold": { "total": 500, "new": 200 }
 }
 ```
- **出参**(超标时):
 ```json
 {
 "finding": "[代码行数超标] src/foo.ts 逻辑行(总规模)=600 阈值=500 超 20%(级别:建议改) 建议拆分..."
 }
 ```
- **出参**(无超标时):`null`
- **级别判定**:
 - 超 ≤10% → `可选`
 - 超 ≤50% → `建议改`
 - 超 >50% → `必须改`
- **示例**:
 - totalLoc=550(超 10%)→ 级别 `可选`
 - totalLoc=700(超 40%)→ 级别 `建议改`
 - totalLoc=800(超 60%)→ 级别 `必须改`
- **依据规范**:`./assistants/rules/skill-conventions.md §规则 1`