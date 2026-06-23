# 模块详细化 — REQ-00038

版本:V0.0.3

## 模块 1:`code-it` 步骤 8a.0 — 模块识别(新增)

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md > ### 步骤 8a.0 — 模块识别`(新增,位于"## 步骤 8 实施开发"**之后**、"## 步骤 8a — 项目可测性守卫"**之前**)
- **关键类/函数**(内部,伪代码):
 ```ts
 function identifyModules(changedFiles: string[]): string[] {
 // 1. 声明文件检测(高优先级)
 if (exists('pnpm-workspace.yaml')) return readPnpmWorkspaces()
 if (exists('package.json') && hasWorkspaces('package.json')) return readNpmWorkspaces()
 if (exists('lerna.json')) return readLernaPackages()
 if (exists('nx.json') || exists('turbo.json')) return readNxTurboWorkspace()
 if (exists('pom.xml')) return readMavenModules()
 if (exists('Cargo.toml') && hasWorkspace('Cargo.toml')) return readCargoWorkspace()
 if (exists('go.mod')) return inferGoModules() // 约定式

 // 2. git diff 退化
 if (changedFiles.length > 0) {
 return [longestCommonPrefix(changedFiles)]
 }

 // 3. CWD 根退化
 return ['.']
 }
 ```
- **调用顺序**:
 1. `code-it` 步骤 8 实施开发完成 → 拿到 `git diff --name-only` 输出
 2. 步骤 8a.0 调 `identifyModules(changedFiles)` → 返回 `modules: string[]`
 3. 步骤 8a 守卫读 `modules` → 对每个模块独立执行 7 项检查
 4. 步骤 8.5 单测输出读 `modules` → 对每个通过的模块识别测试目录
- **状态归属**:任务级内存缓存(模块 1 缓存到 `code-it` 内部,任务生命周期内复用)
- **与概要设计的对应**:design §4 模块 1
- **符合的规范**:
 - `encoding-conventions.md §规则 1`(编码格式)
 - `module-conventions.md §规则 1`(资源放 `templates/` / `checklists/` / `guidelines/` 子目录 — 本步骤不创建新文件,沿用既有 SKILL.md)
 - `skill-conventions.md §规则 1/2`(frontmatter 字节级保留 + 不包含开发痕迹)
- **关键决策**:
 - 不引入用户问路(NFR-3 强约束)
 - 0 新增三方依赖(沿用 REQ-00034 NFR-3)
 - 7 套声明文件解析手写(无 npm 库,典型 < 50 行)

## 模块 2:`code-it` 步骤 8a — 守卫位置改造(修改 / 扩展)

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md > ### 步骤 8a > 步骤 8a.1 / 8a.2 / 8a.4`(原 L563-L633,**仅字面改写**)
- **关键类/函数**(内部,扩展既有):
 ```ts
 function guardCheck(modules: string[]): { testable: boolean; moduleTestable: Map<string, boolean> } {
 const moduleTestable = new Map()
 for (const module of modules) {
 // 对每个模块独立执行 7 项检查(字节级沿用 REQ-00034)
 const checkPath = module === '.' ? '.' : module
 const hit = any([
 check1: exists(`${checkPath}/package.json`) && hasScriptsTest(`${checkPath}/package.json`),
 check2: exists(`${checkPath}/pyproject.toml`) && hasTestConfig(`${checkPath}/pyproject.toml`),
 check3: exists(`${checkPath}/Cargo.toml`),
 check4: exists(`${checkPath}/go.mod`),
 check5: exists(`${checkPath}/pom.xml`),
 check6: exists(`${checkPath}/build.gradle`) || exists(`${checkPath}/build.gradle.kts`),
 check7: isDirectory(`${checkPath}/test`)
 ])
 moduleTestable.set(module, hit)
 }
 const testable = Array.from(moduleTestable.values()).some(v => v)
 return { testable, moduleTestable }
 }
 ```
- **调用顺序**:
 1. 模块 1 返回 `modules`
 2. 步骤 8a.1 对每个模块独立执行 7 项检查
 3. 步骤 8a.2 聚合:`testable = 至少 1 个模块命中`
 4. 步骤 8a.4 屏显契约:每个模块独立显示
- **状态归属**:任务级内存缓存(`moduleTestable: Map<string, boolean>`)
- **与概要设计的对应**:design §4 模块 2
- **符合的规范**:
 - `skill-conventions.md §规则 1/2`(frontmatter + 既有章节字节级保留)
 - NFR-4:7 项检查项字节级沿用 REQ-00034,仅位置从 CWD 根 → 模块目录
- **关键决策**:
 - 7 项守卫检查项本身 0 改(字节级沿用 REQ-00034)
 - 判定逻辑扩展为"任一模块通过即 testable = True"(原"工程根级单点判定"细化)
 - 屏显契约扩展为"模块级守卫检查详情"

## 模块 3:`code-it` 步骤 8.5 — 单测输出位置扩展(修改 / 扩展)

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md > ### 步骤 8.5 > 步骤 8.5.2 / 8.5.5`(原 L657-L699,**仅字面改写**)
- **关键类/函数**(内部,扩展既有):
 ```ts
 function identifyTestDir(module: string, framework: string): string {
 // 7 层测试目录识别优先级链
 if (hasJestConfig(module)) return readJestTestMatch(module)
 if (hasPytestConfig(module)) return readPytestTestpaths(module)
 if (exists(`${module}/Cargo.toml`)) return `${module}/src` // Rust 约定
 if (exists(`${module}/go.mod`)) return module // Go 同包测试
 if (exists(`${module}/pom.xml`) || exists(`${module}/build.gradle`)) return `${module}/src/test`
 // 7. 无约定 → 模块根 test/
 if (isDirectory(`${module}/test`)) return `${module}/test`
 // 8. 仍无 → CWD 根 test/(原 REQ-00034 行为退化)
 return 'test'
 }
 ```
- **调用顺序**:
 1. 模块 1 返回 `modules` + 模块 2 返回 `moduleTestable`
 2. 步骤 8.5.2 任务性质自动判定(沿用既有 3 类:文档 / 函数级代码类 / 配置类型定义)
 3. 步骤 8.5 对每个 `moduleTestable.get(m) === true` 的模块调 `identifyTestDir`
 4. 多模块分别写单测到各自测试目录
 5. 步骤 8.5.5 产出物 = `code/<任务>/unit-test-results.md`,既有"## 9. 单元测试"小节字节级保留 + 新增"## 各模块单测结果"小节(沿用模块 5 模板改造)
- **状态归属**:任务级内存缓存(`moduleTestDir: Map<string, string>`)
- **与概要设计的对应**:design §4 模块 3
- **符合的规范**:
 - `module-conventions.md §规则 1`(模板在 `code-it/templates/RESULT.md`)
 - `skill-conventions.md §规则 1/2`
- **关键决策**:
 - 7 层优先级链覆盖主流语言(Node/Python/Rust/Go/Java)
 - 无约定 → CWD 根 `test/` 退化(NFR-2 兼容性)
 - 多模块通过 → 多模块分别写单测(FR-3 锁定)
 - 模板"## 9. 单元测试(由 code-it 内化)"小节**字节级保留**,仅追加"## 各模块单测结果"

## 模块 4:`code-plan` 任务粒度描述字面改写(修改 / 字面)

- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md > ## 步骤 10A 任务拆分 > ## 测试状态字段语义`(原 L473 / L496,各字面改写 1 句)
- **关键类/函数**:N/A(纯文档字面改写)
- **调用顺序**:
 1. L473:既有"由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)" → 改为"由 `code-it` 内化(`code-it` 步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按需写单测)"
 2. L496:既有"由 `code-it` 步骤 8.5 接管(沿用,原 `code-unit` 另起流程 → `code-it` 步骤 8.5 产出 `code/<任务>/unit-test-results.md`)" → 改为"由 `code-it` 步骤 8.5 接管(沿用,原 `code-unit` 另起流程 → `code-it` 步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按模块写单测 → 产出 `code/<任务>/unit-test-results.md`)"
- **状态归属**:N/A(纯字面)
- **与概要设计的对应**:design §4 模块 5
- **符合的规范**:
 - `skill-conventions.md §规则 2`(字面改写不引入开发痕迹)
- **关键决策**:
 - **仅**字面改写,不新增字段(FR-5 锁定)
 - 与 V0.0.3 REQ-00031 任务粒度原则正交(任务粒度是 `code-plan` 抽象,模块识别是 `code-it` 内部细节)

## 模块 5:`code-it/templates/RESULT.md` 多模块支持(修改 / 追加)

- **路径**:`plugins/code-skills/skills/code-it/templates/RESULT.md > ## 9. 单元测试(由 code-it 内化,新增,`(L138-L153)小节**后**追加"## 各模块单测结果"小节`
- **关键类/函数**:N/A(模板改造,字节级追加 1 小节)
- **调用顺序**:
 1. `code-it` 步骤 8.5.5 写 `unit-test-results.md` 时**直接复制**模板"## 9. 单元测试(由 code-it 内化)"小节 + 新"## 各模块单测结果"小节 + 填实际值
 2. 既有"## 9. 单元测试"小节(L138-L153)**字节级保留**(NFR-4 锁定)
 3. "## 10. 逻辑行统计(由 code-it 内化,新增)"小节(L155-L174)章节顺序 +1
 4. "## 11. 变更记录"小节章节顺序 +1
- **状态归属**:N/A(模板改造)
- **与概要设计的对应**:design §4 模块 4
- **符合的规范**:
 - `module-conventions.md §规则 1`(模板在 `code-it/templates/` 子目录,位置合规)
 - `skill-conventions.md §规则 2`(既有 0 改 + 不包含开发痕迹)
- **关键决策**:
 - "## 各模块单测结果"字段:模块路径 / 守卫检查 / 检查位置 / 测试框架 / 测试文件 / 跑通情况(FR-4 锁定 7 字段)
 - 既有 8 个章节(L28-L106)字节级保留
 - 既有"## 9. 单元测试"小节(L138-L153)字节级保留
 - 章节顺序:既有章节 +1(因新增 1 小节)
