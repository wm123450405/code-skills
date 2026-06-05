# 设计笔记 — REQ-00009
更新时间:2026-06-05 17:10
版本:V0.0.2

## 关键设计问题清单

### Q-D1:守卫检查项的范围与深度
- **问题**:`code-unit` 守卫应检查哪些文件/目录来判定"项目可测"?
- **候选 A**:只检查 7 项(Q-1 锁定 A,详见 `require/REQ-00009/RESULT.md §FR-1`)
  - `package.json`(Node.js,需含 `scripts.test`)
  - `pyproject.toml`(Python,需含测试配置)
  - `Cargo.toml`(Rust)
  - `go.mod`(Go)
  - `pom.xml`(Java Maven)
  - `build.gradle` / `build.gradle.kts`(Java Gradle / Android)
  - `test/` 目录(通用兜底)
- **候选 B**:检查更多(如 `Gemfile` / `composer.json` / `mix.exs` / `deno.json` 等)
  - 优点:更全面
  - 缺点:增加复杂度,本需求范围内 NFR-1 锁零依赖 / NFR-7 锁 < 1 秒
- **选定**:A(Q-1 锁定 A,需求已明确)
- **否决理由**:B 超出本需求范围(可作 v2 增量追加,E-8 预留)

### Q-D2:守卫不通过时的行为
- **问题**:守卫不通过时,`code-unit` 应如何行为?
- **候选 A**:跳过 + 写看板"不适用"(Q-2 锁定 A)
- **候选 B**:报错退出 + 引导用户配置项目
  - 缺点:破坏"完全无人确认"约束(`code-auto` 失败)
  - 缺点:与 V0.0.1 看板"不适用"语义不匹配
- **选定**:A(Q-2 锁定 A,需求已明确)
- **否决理由**:B 触发 `code-auto` 中断 + 与既有"不适用"枚举冲突

### Q-D3:守卫不通过时是否写 `test/<任务编码>/RESULT.md`?
- **问题**:跳过流程中是否产生 RESULT.md?
- **候选 A**:**不**写(Q-3 锁定 A,零新增产物)
- **候选 B**:写一份"跳过说明"RESULT.md
  - 缺点:产生新文件,与 FR-3.AC-3.1 冲突
  - 缺点:`code-dashboard` 不知道如何处理"跳过"状态(混淆)
- **选定**:A(Q-3 锁定 A,需求已明确)
- **否决理由**:B 违反 FR-3 + 看板兼容性问题

### Q-D4:守卫不通过时的退出码
- **问题**:守卫不通过时 `code-unit` 退出码应为?
- **候选 A**:0(正常退出,Q-A 采纳默认,`code-auto` 据此继续)
- **候选 B**:非 0(失败,`code-auto` 据此中断)
  - 缺点:`code-auto` 任务循环在"无意义调用"时中断,违反 NFR-6
  - 缺点:与"跳过"语义不符(跳过 = 正常路径)
- **选定**:A(NFR-6 锁 0)
- **否决理由**:B 违反 NFR-6 兼容 `code-auto` 退出码

### Q-D5:守卫插入位置
- **问题**:"步骤 0a 项目可测性检查"应插入 SKILL.md 哪个位置?
- **候选 A**:在"步骤 0 版本上下文检测"**之前**(沿用 REQ-00005 / REQ-00010 的"步骤 0a"命名约定)
- **候选 B**:在"步骤 0"**之后**
  - 缺点:与既有"步骤 0a"模式命名冲突(REQ-00005 既有 `步骤 0a` 在 步骤 0 之前)
  - 缺点:破坏一致性
- **选定**:A(沿用既有约定)
- **否决理由**:B 破坏与 REQ-00005 / REQ-00010 的同位叠加模式

### Q-D6:`package.json` 是否需要验证 `scripts.test`?
- **问题**:`package.json` 存在但无 `scripts.test` 是否算"可测"?
- **候选 A**:**必须**含 `scripts.test`(避免误判)
  - 优点:更严格,避免"有 package.json 但无测试命令"的尴尬
  - 缺点:实现稍复杂(需 Read package.json 验证)
- **候选 B**:只要 `package.json` 存在就算
  - 优点:实现简单
  - 缺点:`code-unit` 守卫通过后跑 `npm test` 报错(更糟)
- **选定**:A(需求 FR-1 显式要求"含 scripts.test")
- **否决理由**:B 导致守卫通过后流程失败,违反 FR-2.AC-2.4

### Q-D7:`pyproject.toml` 是否需要验证测试配置?
- **问题**:`pyproject.toml` 存在但无测试配置是否算"可测"?
- **候选 A**:**必须**含测试配置(如 `[tool.pytest]` / `[tool.pytest.ini_options]`)
- **候选 B**:只要存在就算
- **选定**:A(需求 FR-1 显式要求"含测试配置")
- **否决理由**:B 同 Q-D6

## 候选方案

| 维度 | 选定方案 | 备选方案 | 选定理由 |
| --- | --- | --- | --- |
| 检查项范围 | 7 项固定(Q-1 锁定) | 动态检测 | NFR-1 锁零依赖 + 简单可维护 |
| 跳过行为 | 看板"不适用"(Q-2) | 报错退出 | FR-2 强约束 |
| 跳过产物 | **0** 新增(Q-3) | 写跳过说明 | FR-3 强约束 |
| 退出码 | 0(NFR-6) | ≠ 0 | 兼容 `code-auto` |
| 插入位置 | 步骤 0 之前(沿用约定) | 步骤 0 之后 | 与 REQ-00005/00010 同位叠加 |
| `package.json` 验证 | 含 `scripts.test` | 仅存在 | 避免"有 package.json 但无测试命令" |
| `pyproject.toml` 验证 | 含测试配置 | 仅存在 | 同上 |
| 性能约束 | < 1 秒(NFR-7) | 无约束 | 7 项文件检测 < 200 ms 即可达成 |
| `--force` 参数 | **不**提供(NFR-8) | 提供 | 留作 v2 |

## 选定方案与理由

**主方案**:在 `code-unit/SKILL.md` 增量追加"步骤 0a 项目可测性检查"守卫,7 项 Glob 检查 + 守卫判定 + 跳过流程。

**理由**:
1. **严格遵循需求 FR-1~FR-7 + NFR-1~NFR-8 全部条款**(需求已锁定 3 项 Q-1~Q-3 + 5 项默认 Q-4~Q-8)
2. **0 修改**其他 11 个 `code-*` 技能(FR-5 强约束)
3. **0 触发**`dashboard-conventions §规则 1` 三同步(沿用"不适用"既有枚举)
4. **0 新增**模块 / 0 新增依赖(NFR-1)
5. **性能 < 1 秒**(7 项 Glob + 必要时 Read 验证,~200 ms,NFR-7)
6. **与 `code-auto` 协同 0 冲突**(NFR-6 退出码 = 0,守卫不通过时 `code-auto` 继续)
7. **与 `code-publish` 协同 0 冲突**(NFR-5 沿用"测试∈{已运行-通过, 不适用}"判定)
8. **与 `code-dashboard` 协同 0 冲突**(NFR-4 复用"不适用"枚举,看板无改动)

**备选方案被否决的理由**:
- 候选 B(报错退出):违反 NFR-6 + 触发 `code-auto` 中断
- 候选 B(写跳过 RESULT.md):违反 FR-3 + 看板兼容性问题
- 候选 B(`package.json` 仅存在即可):守卫通过后跑 `npm test` 失败,违反 FR-2.AC-2.4

## 每条决策的规范依据

| 决策 | 规范依据 |
| --- | --- |
| 守卫插入步骤 0 之前 | 沿用 `skill-conventions.md` + 既有 11 个 `code-*` SKILL.md 的"步骤 0a"命名约定 |
| 7 项检查项范围 | `require/REQ-00009/RESULT.md §FR-1.AC-1.2`(Q-1 锁定 A) |
| 复用"不适用"枚举 | `require/REQ-00009/RESULT.md §NFR-3`(Q-2 锁定 A)+ `dashboard-conventions §规则 1`(0 触发) |
| 0 新增产物 | `require/REQ-00009/RESULT.md §NFR-3`(Q-3 锁定 A) |
| 退出码 = 0 | `require/REQ-00009/RESULT.md §NFR-6` |
| 0 修改其他 11 技能 | `require/REQ-00009/RESULT.md §FR-5` |
| 0 修改 marketplace / plugin | `require/REQ-00009/RESULT.md §FR-6` |
