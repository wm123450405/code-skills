# 风险分析 — REQ-00038

版本:V0.0.3

## 异常处理

### 异常路径 1:声明文件解析失败

- **触发条件**:声明文件存在但格式异常(如 `pnpm-workspace.yaml` 解析失败 / `package.json#workspaces` 非数组)
- **检测手段**:`YAML.parse` / `JSON.parse` 抛异常
- **处理策略**:退化为 git diff 公共子目录(沿用优先级链第 2 层)
- **监控指标**:屏显 `⚠ code-it 模块识别:声明文件解析失败,退化为 git diff 公共子目录(<错误信息>)`
- **对应任务**:TASK-REQ-00038-00001

### 异常路径 2:git diff 失败(非 git 仓库)

- **触发条件**:CWD 不是 git 仓库 / `git` 命令不可用
- **检测手段**:`Bash: git diff --name-only` 退出码非 0
- **处理策略**:退化为 CWD 根(原 REQ-00034 行为)
- **监控指标**:屏显 `⚠ code-it 模块识别:git diff 失败,退化为 CWD 根`
- **对应任务**:TASK-REQ-00038-00001

### 异常路径 3:模块目录无法访问(权限/不存在)

- **触发条件**:模块路径存在但不可读(权限不足 / 路径失效)
- **检测手段**:`fs.access` 抛 EACCES / ENOENT
- **处理策略**:跳过该模块,屏显警告
- **监控指标**:屏显 `⚠ code-it 模块守卫:模块 <path> 不可访问,跳过`
- **对应任务**:TASK-REQ-00038-00002

### 异常路径 4:多模块通过但只有一个有变更

- **触发条件**:`moduleTestable` 中多个模块 `true`,但 `git diff` 变更文件只命中其中一个
- **检测手段**:对比 `changedFiles` 与 `moduleTestable` 真值集合
- **处理策略**:只给该模块写单测(沿用 FR-3 E-5 行为)
- **监控指标**:屏显 `=== code-it 按需写单测(守卫通过)===\n任务:<任务编码>\n判定:写单测(仅模块 <module>)`
- **对应任务**:TASK-REQ-00038-00003

### 异常路径 5:模块识别结果与变更路径不一致

- **触发条件**:模块识别返回 `['packages/foo', 'packages/bar']`,但 `git diff` 变更文件只命中 `'packages/foo'`
- **检测手段**:对每个模块的变更文件计数
- **处理策略**:仅对有变更的模块写单测
- **监控指标**:同异常路径 4
- **对应任务**:TASK-REQ-00038-00003

## 安全边界

- **鉴权要求**:N/A(`code-it` 是内部技能,不涉及外部鉴权)
- **输入校验**:`changedFiles` 路径必须为相对 CWD 的合法路径(由 `git diff` 保证)
- **敏感数据处理**:N/A(不涉及敏感数据)
- **审计日志**:`work-log.md` 追加"## 模块识别"小节,记录识别的模块列表(沿用 NFR-5)
- **依据规范**:`module-conventions.md §规则 1` + `skill-conventions.md §规则 1/2`

## 性能与资源

### 关键路径耗时目标

- **模块识别耗时**:典型 monorepo 100 模块 < 1 秒(8 套声明文件解析,本地 IO)
- **守卫检查耗时**:典型 100 模块 < 1 秒(每模块 7 项检查,本地 IO)
- **总耗时**:**< 2 秒**(NFR-1 强约束;典型 100 模块 monorepo)
- **单模块工程**:0 性能开销(模块识别退化到 CWD 根,7 项守卫 1 次执行)

### 资源限制

- **内存**:`modules` / `moduleTestable` / `moduleTestDir` 3 个数据结构,< 1MB(典型 100 模块)
- **文件 IO**:每次守卫检查 = 7 次 `fs.access` / `fs.readFile` × 模块数;典型 100 模块 = 700 次 IO,本机 < 100ms
- **网络 IO**:0(本需求纯本地文件操作)

### 缓存策略

- **任务级内存缓存**:`modules` / `moduleTestable` / `moduleTestDir` 缓存到 `code-it` 内部,任务生命周期内复用
- **不持久化**:任务边界之外模块可能已被删除/重命名,缓存失效

### 降级策略

- **声明文件解析失败** → 退化到 git diff 公共子目录(优先级链第 2 层)
- **git diff 失败** → 退化到 CWD 根(原 REQ-00034 行为)
- **模块目录不可访问** → 跳过该模块(屏显警告,不阻断)
- **7 项守卫全不命中** → testable = False,跳过单测(沿用 REQ-00034 行为)

## 回退策略

### 触发条件

- 1:模块识别引入性能问题(实测 > 5 秒)
- 2:模块识别引入功能问题(7 项守卫位置错误 / 多模块判定错误)
- 3:`unit-test-results.md` 模板破坏 `code-check` 评审兼容性
- 4:回归测试失败(单模块工程守卫命中模式变化)

### 回退步骤

1. **紧急回退**:`git revert <commit>` 撤回本需求 3 任务
2. **部分回退**:
 - 触发 1:仅撤回 T-1(模块识别),保留 T-2(守卫位置) + T-3(模板)
 - 触发 3:仅撤回 T-3(模板),保留 T-1 + T-2
3. **数据修复**:回退后 `unit-test-results.md` 旧版本继续可用(既有"## 9. 单元测试"小节字节级保留)

### 验证

- `git diff HEAD~1` 检查文件改动
- `code-it` 单模块工程端到端测试(沿用 AC-4 字节级沿用验证)
- `code-check` 评审 `unit-test-results.md` 字面校验(沿用既有规则)

## 测试要点

### 单元测试

- **模块识别函数** `identifyModules`:
 - 单模块工程 → `['.']`
 - monorepo(pnpm-workspace.yaml) → packages 列表
 - monorepo(package.json#workspaces) → packages 列表
 - monorepo(lerna.json) → packages 列表
 - Maven(pom.xml#modules) → modules 列表
 - Cargo(Cargo.toml#workspace.members) → members 列表
 - Go(go.mod) → 约定式推断
 - 无声明文件 → git diff LCP
 - 空 `changedFiles` → `['.']` 兜底
- **守卫检查函数** `guardCheck`:
 - 单模块命中 → `testable = true`
 - 多模块部分命中 → `testable = true` + `moduleTestable` 真值集合
 - 全不命中 → `testable = false`
- **测试目录识别函数** `identifyTestDir`:
 - Node.js(Jest) → `testMatch`
 - Python(Pytest) → `testpaths`
 - Go → 同包
 - Rust → `src/`
 - Java(Maven/Gradle) → `src/test/`
 - 无约定 → 模块根 `test/`
 - 全退化 → CWD 根 `test/`

### 集成测试

- `code-it` 端到端:monorepo 工程下,变更 packages/foo → 模块识别 = `['packages/foo']` + 守卫命中 + 单测写到 `packages/foo`
- `code-it` 端到端:多模块工程下,变更跨 2 个模块 → 2 模块分别写单测
- `code-it` 端到端:单模块工程(AC-4)→ 字节级沿用 REQ-00034 行为

### 端到端测试

- **AC-1**:monorepo 工程子包识别正确(创建测试工程,验 `work-log.md` "## 模块识别"小节)
- **AC-2**:模块可测性守卫位置正确(根级无 `package.json#scripts.test`,子包有 → 整体 `testable = true`)
- **AC-3**:多模块单测写到各自测试目录(Go + Python 混合 monorepo)
- **AC-4**:单模块工程(非 monorepo)行为字节级沿用(回归测试)

### 性能/安全测试

- **AC-7**:性能 < 2 秒(100 模块 monorepo 下测步骤 8a.0 + 8a 总耗时)
- **安全**:N/A(本需求为本地文件操作,无外部接口)

### 回归测试

- `code-it` 步骤 8a 既有 7 项守卫字面 0 改(字节级校验)
- `code-it` 步骤 8.5 既有 3 类任务自动判定逻辑 0 改(字节级校验)
- `code-it/templates/RESULT.md` 既有"## 9. 单元测试"小节 0 改(字节级校验)
- `code-plan` 既有"测试类型已从本列表移除"段 0 改(仅字面增量)
- 单模块工程 0 回归(AC-4)
