# 分析笔记 — REQ-00041
更新时间:2026-06-29 13:50

## 当前理解

### 背景
当前 4 个技能(code-design/code-plan/code-it/code-check)的 SKILL.md 文件非常庞大:
- code-design: ~669 行
- code-plan: ~1187 行
- code-it: ~1551 行
- code-check: ~703 行
合计: ~4110 行

这些文件中混杂了大量与具体开发语言/项目结构绑定的内容(如构建命令检测、测试框架识别、monorepo 声明文件解析等),导致每次加载技能时消耗大量 token。

### 核心需求
1. SKILL.md 仅保留流程性内容(做什么、按什么顺序做)
2. 语言/项目结构差异内容独立到 `references/` 目录
3. 按语言(模块类型)建立各自差异说明文档
4. 运行时动态加载:只加载 SKILL.md + 实际项目环境对应的 references 文档
5. 简化内容,减少 token 消耗

### 已识别的"语言差异"内容(从 4 个 skills 中提取)
- 构建命令检测 (npm/pnpm/yarn vs cargo vs go build vs mvn/gradle vs pip)
- 测试框架识别 (Jest/Vitest/Mocha vs pytest vs cargo test vs go test vs JUnit)
- 项目结构识别 (package.json vs Cargo.toml vs go.mod vs pom.xml vs pyproject.toml)
- Monorepo 声明文件解析 (pnpm-workspace.yaml, lerna.json, nx.json, turbo.json, pom.xml modules, Cargo.toml workspace)
- 代码行数统计工具 (tokei/cloc/heuristic)
- 编码规范差异 (命名约定、文件组织、错误处理范式)

### 待澄清的关键问题
1. 需要支持哪些语言/模块类型? (Node.js, Python, Rust, Go, Java, 其他?)
2. references 目录结构: 每个技能独立? 还是共享?
3. 语言检测的触发时机和方式?
4. 简化到什么程度才算"够了"?