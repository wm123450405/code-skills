# 接口详细规格 — REQ-00038

版本:V0.0.3

## 接口 1:`code-it` 步骤 8a.0 模块识别(新增,内部)

- **形式**:函数(内部,`code-it` 步骤 8a.0 调用)
- **签名**(伪代码):
 ```ts
 function identifyModules(changedFiles: string[]): string[]
 ```
- **入参**:
 - `changedFiles: string[]`:`git diff --name-only` 输出,变更文件路径列表(相对 CWD)
 - 字符集:路径分隔符沿用 `path.posix` 规范化(Windows `\` / Unix `/` 一致)
- **出参**:
 ```ts
 {
 modules: string[] // 模块路径列表(相对 CWD);单模块工程 = ['.'];空数组理论不可能(E-7 兜底为 ['.'])
 }
 ```
- **错误码**:N/A(本步骤不抛异常,所有异常退化到 CWD 根,见 E-1 / E-2)
- **示例**:
 ```ts
 // monorepo:pnpm-workspace.yaml
 identifyModules(['packages/foo/src/index.ts', 'packages/foo/src/util.ts'])
 // → ['packages/foo', 'packages/bar', 'packages/baz'] // 来自 pnpm-workspace.yaml

 // monorepo:git diff 退化
 identifyModules(['packages/foo/src/index.ts'])
 // → ['packages/foo'] // 来自 LCP 推断

 // 单模块工程
 identifyModules(['src/index.ts', 'src/util.ts'])
 // → ['.'] // 无声明文件 + LCP = 'src' 但 'src' 无 package.json → 退化到 '.'

 // 理论不可能
 identifyModules([])
 // → ['.'] // E-7 兜底
 ```
- **版本策略**:N/A(本仓库为内部技能)
- **兼容策略**:
 - **不**修改既有 `code-it` 步骤 8a 逻辑(字节级沿用 REQ-00034)
 - 单模块工程 = 1 模块 = 1 整工程,模块目录 = CWD 根,**0 回归**(AC-4 锁定)
- **依据规范**:`encoding-conventions.md §规则 1`(编码格式)

## 接口 2:`code-it` 步骤 8a 守卫位置(修改 / 扩展,内部)

- **形式**:函数(内部,`code-it` 步骤 8a 调用)
- **签名**(伪代码):
 ```ts
 function guardCheck(modules: string[]): { testable: boolean; moduleTestable: Map<string, boolean> }
 ```
- **入参**:
 - `modules: string[]`:模块识别结果(沿用接口 1)
- **出参**:
 ```ts
 {
 testable: boolean, // 至少 1 个模块通过 → True
 moduleTestable: Map<string, boolean> // 每个模块的守卫结果
 }
 ```
- **7 项检查项字节级沿用 REQ-00034**:
 1. `package.json` 含 `scripts.test`(检查位置:模块目录)
 2. `pyproject.toml` 含测试配置(检查位置:模块目录)
 3. `Cargo.toml`(检查位置:模块目录)
 4. `go.mod`(检查位置:模块目录)
 5. `pom.xml`(检查位置:模块目录)
 6. `build.gradle` / `build.gradle.kts`(检查位置:模块目录)
 7. `test/` 目录(检查位置:模块目录)
- **错误码**:N/A(本步骤不抛异常,所有异常退化见 E-4)
- **示例**:
 ```ts
 // monorepo:根无守卫,子包有
 guardCheck(['packages/foo', 'packages/bar'])
 // → { testable: true, moduleTestable: { 'packages/foo': true, 'packages/bar': false } }

 // 单模块工程
 guardCheck(['.'])
 // → { testable: true, moduleTestable: { '.': true } } // 字节级沿用 REQ-00034

 // 全不命中
 guardCheck(['packages/foo', 'packages/bar'])
 // → { testable: false, moduleTestable: { 'packages/foo': false, 'packages/bar': false } }
 ```
- **屏显契约**(沿用既有 8a.4 字节级 + 扩展"模块级守卫检查详情"):
 ```
 ✓ code-it 守卫通过(项目可测)进入正常流程

 任务:<任务编码>
 守卫检查:
 模块 CWD 根:
 - package.json:✗
 - pyproject.toml:✗
 - Cargo.toml:✗
 - go.mod:✗
 - pom.xml:✗
 - build.gradle:✗
 - test/ 目录:✗
 模块 packages/foo:
 - package.json:✓ (含 scripts.test)
 - pyproject.toml:✗
 - Cargo.toml:✗
 - go.mod:✗
 - pom.xml:✗
 - build.gradle:✗
 - test/ 目录:✗
项目可测,继续按需写单测流程
 ```
- **依据规范**:`skill-conventions.md §规则 1/2`(frontmatter 字节级保留 + 既有章节字节级保留)

## 接口 3:`code-it` 步骤 8.5 单测输出位置(修改 / 扩展,内部)

- **形式**:函数(内部,`code-it` 步骤 8.5 调用)
- **签名**(伪代码):
 ```ts
 function identifyTestDir(module: string): string
 ```
- **入参**:
 - `module: string`:通过的模块路径(来自接口 2 `moduleTestable.get(m) === true` 的 m)
- **出参**:
 - `string`:测试目录路径(相对 CWD)
- **7 层优先级链**:
 1. 模块内 `package.json#scripts.test` 含 `jest` / `vitest` / `mocha` 配置 → 沿用 `testMatch` / `testRegex`
 2. 模块内 `pyproject.toml` 含 `[tool.pytest.ini_options]` → 沿用 `testpaths`
 3. 模块内 `Cargo.toml` → 约定 `src/` 同包 `#[cfg(test)]` 或 `tests/`
 4. 模块内 `go.mod` → 约定同包 `*_test.go`
 5. 模块内 `pom.xml` / `build.gradle` → 约定 `src/test/`
 6. 无约定 → 模块根 `test/` 目录
 7. 仍无 → CWD 根 `test/` 目录(原 REQ-00034 行为退化)
- **错误码**:N/A
- **示例**:
 ```ts
 // Node.js 模块
 identifyTestDir('packages/foo')
 // → 'packages/foo' (读 testMatch) 或 'packages/foo/test' (无 testMatch)

 // Go 模块
 identifyTestDir('go-services/api')
 // → 'go-services/api' (同包测试)

 // Python 模块
 identifyTestDir('packages/py-utils')
 // → 'packages/py-utils/tests' (读 testpaths) 或 'packages/py-utils/test' (无 testpaths)

 // 退化
 identifyTestDir('packages/foo')
 // → 'test' (CWD 根 test/)
 ```
- **依据规范**:`module-conventions.md §规则 1`(资源放 `templates/` 子目录)

## 接口 4:`code-it/templates/RESULT.md` "## 各模块单测结果" 小节(新增,模板)

- **形式**:Markdown 模板
- **签名**:N/A(模板)
- **位置**:`plugins/code-skills/skills/code-it/templates/RESULT.md`,在"## 9. 单元测试(由 code-it 内化,新增,"小节**后**追加
- **字段**(FR-4 锁定 7 字段):
 ```
 ## 各模块单测结果

 ### 模块 <path>
 - 守卫检查:✓ / ✗
 - 检查位置:<模块目录>
 - 测试框架:<Jest / Pytest / Go test / ...>
 - 新增/修改的测试文件:<...>
 - 跑通情况:<通过 N 个 / 失败 M 个>
 ```
- **错误码**:N/A
- **示例**:
 ```markdown
 ## 各模块单测结果

 ### 模块 packages/foo
 - 守卫检查:✓
 - 检查位置:packages/foo
 - 测试框架:Jest
 - 新增/修改的测试文件:packages/foo/src/foo.test.ts
 - 跑通情况:通过 5 个 / 失败 0 个

 ### 模块 packages/bar
 - 守卫检查:✗
 - 检查位置:packages/bar
 - 测试框架:N/A
 - 新增/修改的测试文件:无
 - 跑通情况:不适用
 ```
- **不修改**:`code-it/templates/RESULT.md` 既有"## 9. 单元测试"小节(字节级保留,NFR-4 沿用)
- **不修改**:`code-it/templates/RESULT.md` 其他既有章节(字节级保留)
- **不触发**:`dashboard-conventions.md §规则 1`(本需求**不**新增列)
- **依据规范**:`module-conventions.md §规则 1`(模板在 `code-it/templates/` 子目录)

## 接口 5:`code-plan` 任务粒度描述(修改 / 字面)

- **形式**:Markdown 文档字面
- **签名**:N/A
- **位置**:`plugins/code-skills/skills/code-plan/SKILL.md` L473 / L496,各字面改写 1 句
- **改写内容**:
 - L473:既有"由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)" → 改为"由 `code-it` 内化(`code-it` 步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按需写单测)"
 - L496:既有"...原 `code-unit` 另起流程 → `code-it` 步骤 8.5 产出 `code/<任务>/unit-test-results.md`" → 改为"...原 `code-unit` 另起流程 → `code-it` 步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按模块写单测 → 产出 `code/<任务>/unit-test-results.md`"
- **错误码**:N/A
- **示例**:N/A(纯字面改写)
- **不修改**:`code-plan` 其他既有章节
- **依据规范**:`skill-conventions.md §规则 2`(字面改写不引入开发痕迹)
