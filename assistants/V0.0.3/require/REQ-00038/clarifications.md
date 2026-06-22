# 澄清记录 — REQ-00038

## 2026-06-22 13:00

### 问题 1:模块识别策略

- **问题**:`code-it` 应如何识别"改修代码属于哪个模块"?
- **选项**:
 - A. 基于 git diff 自动识别(推荐)— 从变更文件路径取最长公共子目录
 - B. 基于 monorepo workspace 配置 — 检测 pnpm-workspace.yaml / package.json workspaces
 - C. 两种都支持 + 用户可选
- **用户回答**:综合判定 — 根据工程上下文和目录结构分析各子模块,也可根据代码规范中的子模块说明作为依据,也可分析不同类型工程的子模块功能(如 pnpm 的 workspace 或 pom.xml 等项目声明文件)
- **影响**:RESULT.md §FR-1(模块识别机制)需综合多源 — git diff + 声明文件(pnpm-workspace.yaml / pom.xml / Cargo workspace 等)+ 目录结构 + 规范说明
- **细化**:模块识别按以下优先级链匹配:
 1. 声明文件(pnpm-workspace.yaml / package.json#workspaces / pom.xml#modules / Cargo.toml#workspace.members / lerna.json / nx.json / turbo.json 等)
 2. 若无声明文件 → 退化为 git diff 变更路径的最长公共子目录
 3. 若无变更路径(理论不可能)→ 退化为 CWD 根

### 问题 2:模块可测性守卫

- **问题**:原 7 项检查应如何适配模块粒度?
- **选项**:
 - A. 模块级守卫 + 7 项(推荐)— 原 7 项检查细化到模块目录
 - B. 保留根级 + 新增模块级 — 双层判定
 - C. 只新增最常用 1 项(子级 package.json)
- **用户回答**:A. 模块级守卫 + 7 项(推荐)
- **影响**:RESULT.md §FR-2(模块可测性守卫)需将原 7 项检查扩展为"对每个识别出的模块独立执行 7 项检查"
- **细化**:
 - 每个模块独立执行 7 项检查
 - 至少 1 个模块通过 → 整体 testable = True
 - 全部模块不通过 → 整体 testable = False,任务"测试状态"列 = `不适用`
 - 单测只写到"通过的模块"的测试目录

### 问题 3:单测输出位置

- **问题**:按需写单测应写到哪个测试目录?
- **选项**:
 - A. 每模块独立测试目录(推荐)— 识别模块的测试目录约定
 - B. 统一写到工程根 test/
 - C. 根据模块类型自动判定
- **用户回答**:A. 每模块独立测试目录(推荐)
- **影响**:RESULT.md §FR-3(单测输出位置)需为每个模块识别其约定测试目录
- **细化**:测试目录识别优先级:
 1. 模块内 `package.json#scripts.test` 含 `jest` / `vitest` / `mocha` → 沿用其 `testMatch` 配置
 2. 模块内 `pyproject.toml` 含 `[tool.pytest.ini_options]` → 沿用 `testpaths`
 3. 模块内 `Cargo.toml` → 约定 `src/` 同包 `#[cfg(test)]` 或 `tests/`
 4. 模块内 `go.mod` → 约定同包 `*_test.go`
 5. 模块内 `pom.xml` / `build.gradle` → 约定 `src/test/`
 6. 无约定 → 退化到模块根 `test/` 目录
 7. 仍无 → 退化到 CWD 根 `test/` 目录(原 REQ-00034 行为)