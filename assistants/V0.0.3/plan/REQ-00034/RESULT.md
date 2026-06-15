# 详细设计 — REQ-00034 移除 /code-unit 技能,能力整合进 /code-it(按需写单测/不适用工程跳过)

- 需求编码:REQ-00034
- 所属版本:V0.0.3
- 文档创建时间:2026-06-15 14:00
- 最近更新:2026-06-15 14:00
- 文档状态:已完成
- 上游需求:`./assistants/V0.0.3/require/REQ-00034/RESULT.md`
- 上游概要设计:`./assistants/V0.0.3/design/REQ-00034/RESULT.md`
- 遵循规范:`./assistants/rules/` 下 12 个文件(全沿用,无新增)
- 涉及技能:`code-unit`(整体删除) + `code-it`(接管守卫 + 按需写单测)+ `code-plan` / `code-auto` / `code-check`(适配)+ 2 JSON + 4 README + CLAUDE.md + 7 项目级规范 + 11 技能描述段

## 1. 设计目标

- **整体设计目标**:`--extensible`(沿用 `design/.../RESULT.md` §1;触发条件 2:29 个文件 ≥ 3;触发 5:整体=--extensible)
- **维度优先级**:功能性 = 中
- **沿用路径**:`code-plan` 步骤 0b 0 问(沿用 `design` 的"## 设计目标"小节)
- **按"## 设计目标"小节调整任务粒度**:
  - 整体=--extensible + 扩展性=高 → 加"扩展架构设计 / 抽象层"等任务(可省略,本需求是字面改写,无架构改造)
  - 封装性 / 可复用性 / 可读性 → 本仓库是 Markdown 自然语言 → **不适用** / **不适用** / **不适用**(不强制加任务)
  - 健壮性 / 可维护性 → 默认 `中` / `中`(不强制加任务)

## 2. 概述

本设计是"技能合并 + 行为接管"(删除 `code-unit` 整体 + `code-it` 接管守卫 7 项 + 按需写单测),**0 新增模块 / 0 新增接口(运行时)/ 0 新增数据结构**,**新增接口类** = `code-it` 步骤 8a + 步骤 8.5 行为接管。**唯一硬删除对象** = `code-unit/SKILL.md` (635 行) + `code-unit/templates/` 整体。涉及 29 个文件,净变化约 -600 ~ -800 行。

## 3. 模块详细化

### 3.1 唯一硬删除:`code-unit/SKILL.md` + `code-unit/templates/`

#### 3.1.1 删除路径
- `plugins/code-skills/skills/code-unit/SKILL.md`(635 行)
- `plugins/code-skills/skills/code-unit/templates/RESULT.md`
- `plugins/code-skills/skills/code-unit/templates/` 整体目录

#### 3.1.2 关键"代码"
**删除方式**:`rm -rf` 风格(整段删除,无字节级保留)

#### 3.1.3 与概要设计的对应
- `design/.../RESULT.md` §3 决策 D-1(激进删除)
- `design/.../RESULT.md` §8 修改文件定位表 第 1-2 行

#### 3.1.4 符合的规范
- `module-conventions.md`:资源目录可按需增减(本需求**删除** `code-unit/templates/`,符合)
- `commit-conventions.md`:`chore(code-unit):` 前缀(commit message 锁定)

### 3.2 行为接管:`code-it` 步骤 8a + 步骤 8.5

#### 3.2.1 步骤 8a — 项目可测性守卫(新增)

**位置**:`plugins/code-skills/skills/code-it/SKILL.md` 既有"## 步骤 8"之后,新增"## 步骤 8a — 项目可测性守卫"

**关键"代码"**(伪代码,字节级沿用 `code-unit` 步骤 0a):
```python
# 步骤 8a:项目可测性守卫(testable guard)
# 沿用 code-unit 步骤 0a.1 的 7 项检查(只检查项目根, 不递归子目录)
checks = [
  ("package.json 含 scripts.test",       file_exists_with_scripts_test),
  ("pyproject.toml 含 [tool.pytest*]",   file_exists_with_pytest_config),
  ("Cargo.toml",                          file_exists),
  ("go.mod",                              file_exists),
  ("pom.xml",                             file_exists),
  ("build.gradle / build.gradle.kts",     any_file_exists),
  ("test/ 目录",                          dir_exists),
]
testable = any(check for check in checks)
if testable:
  print("✓ code-it 守卫通过(项目可测)进入正常流程")
  # ... 屏显 7 项检查详情(沿用 code-unit 步骤 0a.4 模板)
else:
  print("⏭ code-it 跳过单测(项目不可测)")
  # ... 屏显 7 项检查详情(全部 ✗)
  # 看板"任务清单"本任务行"测试状态" = 不适用
  # exit 0
```

**判定逻辑**(字节级沿用 `code-unit` 步骤 0a.2):
- 命中任一 → testable = True → 进入步骤 8.5
- 全部不命中 → testable = False → 跳过步骤 8.5 → 看板"测试状态" = `不适用` → exit 0

**调用顺序**:
1. `code-it` 步骤 7 处理任务前置依赖
2. `code-it` 步骤 8 探索项目代码
3. **`code-it` 步骤 8a 项目可测性守卫**(本需求**新增**)
4. `code-it` 步骤 8.5 按需写单测(testable = True 时)
5. `code-it` 步骤 9 编译/运行(沿用既有)

**状态归属**:`testable`(本任务局部变量,内存级,**不**持久化)

**与概要设计的对应**:
- `design/.../RESULT.md` §3 决策 D-2(守卫接管)
- `design/.../RESULT.md` §8 修改文件定位表 `code-it/SKILL.md` 第 2 行

**符合的规范**:
- `skill-conventions.md` §规则 1(SKILL.md frontmatter 字节级保留)
- `module-conventions.md`(本仓库元技能仓库,无工程代码)

#### 3.2.2 步骤 8.5 — 按需写单测(新增)

**位置**:`code-it/SKILL.md` "## 步骤 8a"之后,新增"## 步骤 8.5 — 按需写单测"(testable = True 时执行)

**关键"代码"**(伪代码,自动判定,无用户问路):
```python
# 步骤 8.5:按需写单测(automatic, no AskUserQuestion)
# 仅在 testable = True 时执行

# 自动判定(沿用 design 决策 D-3)
task_type = read_task_type_from_plan(task_num)  # 读 plan/.../PLAN.md
has_function_level_changes = detect_function_level_changes(code_diff)

if task_type == "文档":
  # 跳过写单测
  write_unit_test_results(f"## 单元测试(由 code-it 内化)\n\n守卫判定: 可测\n任务类型: 文档\n本任务不涉及单元测试")
elif task_type in ("新增", "修改", "重构", "修复") and has_function_level_changes:
  # 写单测 + 跑通
  test_framework = detect_test_framework()  # Jest / Pytest / Go test / ...
  new_test_files = write_unit_tests(test_framework)  # 写测试到 CWD 下项目测试目录
  run_unit_tests(test_framework)  # 跑通(Bash)
  write_unit_test_results(f"## 单元测试(由 code-it 内化)\n\n守卫判定: 可测\n测试框架: {test_framework}\n新增/修改的测试文件: {new_test_files}\n跑通情况: 通过 N 个 / 失败 M 个")
else:
  # 任务类型 = 配置 / 类型定义, 跳过
  write_unit_test_results(f"## 单元测试(由 code-it 内化)\n\n守卫判定: 可测\n任务类型: {task_type}\n本任务不涉及单元测试")
```

**屏幕输出**(字节级沿用 `code-unit` 步骤 7):
```
=== code-it 按需写单测(守卫通过)===
任务:TASK-REQ-...-...
判定:写单测 / 跳过单测
测试框架:<Jest / Pytest / ...>
新增/修改的测试文件:<file1.test.ts, file2.test.ts>
```

**错误修复循环**(沿用原 `code-unit` 步骤 11):
- 写单测跑通失败 → 沿用 `code-it` 步骤 12 错误修复循环
- 最连续失败 5 次后必须停下询问用户(E-8 锁定)

**与概要设计的对应**:
- `design/.../RESULT.md` §3 决策 D-3 / D-4 / D-5 / D-6 / D-7
- `design/.../RESULT.md` §8 修改文件定位表 `code-it/SKILL.md` 第 3 行

#### 3.2.3 文档头 + L18/L795/L907-908 字面改写

**位置**:`code-it/SKILL.md` 文档头 ## 目标段 + L18 + L795 + L907-908

**关键"代码"**(Markdown 字面):
- 文档头:"本技能的职责是'编码 + 编译/运行成功';**不含**'编写单元测试'或'执行单元测试'" → 改写为"本技能的职责是'编码 + 编译/运行成功 + **按需写单测**(项目可测性守卫 7 项 + 写单测 + 跑通);**不**弹 `AskUserQuestion`(FR-3 锁定)"
- L18 "`code-unit` 不得修改生产代码" → 删除
- L795 "(可选)调 code-unit 补/验证单测" 步骤 3 → 删除
- L907-908 "`code-unit` 与 `code-check` 在本任务完成后对本次变更展开" → 改写为"`code-check` 在本任务完成后对本次变更展开"

### 3.3 字面改写:5 SKILL.md(除 `code-it` 外)

#### 3.3.1 `code-plan/SKILL.md` L368/431/445/454/1105

**关键"代码"**(Markdown 字面):
- "由 `code-unit` 另起流程" → "由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)"
- "code-unit 阶段记录到 `code/<任务>/test-results.md`" → "由 `code-it` 步骤 8.5 产出 `code/<任务>/unit-test-results.md`"

#### 3.3.2 `code-auto/SKILL.md` 整段删除 + 10 处字面改写

**位置**:L45 + L213-227(子技能调用表 4 行) + L388-411(步骤 4.b 整段) + L432-433 + L449 + L624-625 + L672 + L692 + L711 + L741 + L797 + L806 + L834

**关键"代码"**:`code-unit` 字面**全部删除**;屏幕日志减少 1 行/任务(原"code-unit ... ✓ (跳过,无需测试)"删除)

#### 3.3.3 `code-check/SKILL.md` 10 处字面改写

**位置**:L3 + L21 + L40-41 + L56 + L72 + L96 + L151 + L281 + L608 + L615

**关键"代码"**:
- "`./assistants/<版本号>/test/<任务编码>/RESULT.md`" → "`./assistants/<版本号>/code/<任务编码>/unit-test-results.md`(由 `code-it` 步骤 8.5 自含)"
- "`code-unit` 产出(只读,作为评审上下文)" → "`code-it` 自含的 `unit-test-results.md`"

### 3.4 字面删除:2 JSON

**位置**:
- `plugins/code-skills/.claude-plugin/plugin.json` L15
- `.claude-plugin/marketplace.json` L24 / L39

**关键"代码"**:
- plugin.json `keywords[]` 数组删除 `"code-unit"`
- marketplace.json `plugins[0].keywords[]` 数组删除 `"code-unit"`
- marketplace.json `plugins[0].skills[]` 数组删除 `"./skills/code-unit"`

### 3.5 字面改写:4 README + CLAUDE.md

**位置**:`README.md` + `README.en.md` + `plugins/code-skills/README.md` + `plugins/code-skills/README.en.md` + `CLAUDE.md`

**关键"代码"**:
- 技能表 / 工作流总览描述段:删除 `code-unit` 行
- 字面量`12 个 code-* 技能` → `11 个 code-* 技能`(具体计数由 `code-plan` 阶段重新扫描)
- 主流程图:`code-it → code-unit → code-check` → `code-it → code-check`

### 3.6 字面改写:7 项目级规范

**位置**:`./assistants/rules/*.md`(本仓库当前 12 个,本需求**仅**触及 7 个)

**关键"代码"**:`code-unit` 字面**全部删除**或改写为"`code-it` 内化";核心约束字节级保留(只改字面)

### 3.7 字面改写:11 技能描述段

**位置**:`plugins/code-skills/skills/{code-require, code-design, code-plan, code-fix, code-init, code-publish, code-version, code-rule, code-merge, code-answer, code-dashboard, code-auto, code-it}/SKILL.md` frontmatter `description` 字段

**关键"代码"**:`code-unit` 字面**全部删除**(`code-it` 描述段**改写**为"含按需写单测";`code-auto` 描述段**改写**为"不调 `code-unit`")

## 4. 算法与逻辑

### 4.1 `code-it` 步骤 8a + 步骤 8.5 状态机

```
[code-it 步骤 7 处理任务前置依赖]
  ↓
[code-it 步骤 8 探索项目代码]
  ↓
[code-it 步骤 8a 项目可测性守卫](本需求**新增**)
  ├─ 命中 7 项任一 → testable = True → 屏幕输出"✓ 守卫通过" → 进入步骤 8.5
  └─ 全部不命中 → testable = False → 屏幕输出"⏭ 守卫不通过" → 跳过步骤 8.5
                                                                     ↓
                                                              看板"测试状态"= 不适用
                                                                     ↓
                                                                  exit 0
  ↓
[code-it 步骤 8.5 按需写单测](testable = True 时, 本需求**新增**)
  ├─ 任务类型 = 文档 → 写 unit-test-results.md = "本任务不涉及单元测试"
  ├─ 任务类型 = 新增/修改/重构/修复 + 涉及"函数级"改动 → 写单测 + 跑通 + 写 unit-test-results.md
  └─ 任务类型 = 配置/类型定义 → 写 unit-test-results.md = "本任务不涉及单元测试"
  ↓
[code-it 步骤 9 编译/运行 + 步骤 10 跑测试 + 步骤 11 错误修复 + 步骤 12 覆盖率 + 步骤 13 RESULT.md]
```

### 4.2 复杂度分析

- 时间复杂度:O(1) per task(守卫 7 项检查是 O(7) ≈ O(1))
- 空间复杂度:O(1)(testable 局部变量,内存级)
- `code-auto` 步骤 4.b 删除:屏幕日志减少 1 行/任务(对 N 个任务总计减少 N 行)

## 5. 数据结构完整变更

**0 新增实体** / **0 修改实体**

| 实体名 | 状态 | 关键字段 | 关系 |
| --- | --- | --- | --- |
| — | — | — | — |

## 6. 接口细节

### 6.1 `code-it` 步骤 8a 守卫接口

- **形式**:函数(本技能内部,不暴露)
- **签名**:`def project_testable_guard() -> bool: ...`
- **入参**:**无**
- **出参**:`testable: boolean`(True = 项目可测,False = 不可测)
- **行为**:
  1. 顺序执行 7 项检查
  2. 命中任一 → 返回 True
  3. 全部不命中 → 返回 False
- **错误码**:**不适用**(本技能内部函数)
- **依据规范**:字节级沿用 `code-unit` 步骤 0a.1 + 0a.2

### 6.2 `code-it` 步骤 8.5 按需写单测接口

- **形式**:函数(本技能内部,不暴露)
- **签名**:`def write_unit_tests_on_demand(task_num: str) -> None: ...`
- **入参**:`task_num: str`(本任务编码,如 `TASK-REQ-00034-00003`)
- **出参**:**无**(副作用:写测试代码到 CWD + 写 `unit-test-results.md`)
- **行为**:
  1. 读 `plan/<需求>/PLAN.md` 任务详情,识别任务类型
  2. 自动判定(无 `AskUserQuestion`)
  3. 写单测 + 跑通(若是函数级代码类任务)
  4. 写 `code/<TASK-...>/unit-test-results.md`
- **错误码**:**不适用**
- **依据规范**:本需求 FR-3 锁定

### 6.3 `code-it` 模板新增"## 单元测试"小节

- **形式**:Markdown 模板
- **路径**:`plugins/code-skills/skills/code-it/templates/RESULT.md`
- **小节内容**:
  ```
  ## 单元测试(由 code-it 内化)
  - 守卫判定:可测 / 不可测
  - 测试框架:<Jest / Pytest / ...>
  - 新增/修改的测试文件:<...>
  - 跑通情况:<通过 N 个 / 失败 M 个>
  - 覆盖率(若可获得):<...>
  - 跳过的子任务:<...>(若有)
  - 发现的代码 bug:<...>(若有,转交 code-it 修复)
  ```
- **既有章节不修改**:字节级保留

### 6.4 `code-plan/SKILL.md` 测试状态字段语义改写

- **形式**:Markdown 字面改写
- **5 处**:`code-plan/SKILL.md` L368 / L431 / L445 / L454 / L1105
- **改写**:见 `plan/REQ-00034/design-notes.md` §3.3.1

### 6.5 `code-auto/SKILL.md` 步骤 4.b 删除

- **形式**:Markdown 整段删除
- **整段**:`code-auto/SKILL.md` L388-411
- **字面删除 10 处**:L213-227(子技能调用表 4 行) + L432-433 + L449 + L624-625 + L672 + L692 + L711 + L741 + L797 + L806 + L834

### 6.6 `code-check/SKILL.md` `test/<TASK-...>/` 引用收窄

- **形式**:Markdown 字面改写
- **10 处**:`code-check/SKILL.md` L3 + L21 + L40-41 + L56 + L72 + L96 + L151 + L281 + L608 + L615

### 6.7 plugin.json + marketplace.json 注册项删除

- **形式**:JSON 字面删除
- **3 处**:`plugin.json` L15(`keywords[]` 1 项) + `marketplace.json` L24(`keywords[]` 1 项) + L39(`skills[]` 1 项)

### 6.8 4 README + CLAUDE.md 字面改写

- **形式**:Markdown 字面改写
- **5 个文件**

### 6.9 7 项目级规范字面改写

- **形式**:Markdown 字面改写(只改字面,核心约束保留)
- **7 个文件**

### 6.10 11 技能描述段字面改写

- **形式**:YAML frontmatter 字面改写
- **11 个 SKILL.md** 的 `description` 字段
- **frontmatter L1-3 字节级保留**

## 7. 异常处理

| 异常场景 | 处理 | 监控 |
| --- | --- | --- |
| E-1(本仓库无项目级规范) | 沿用 `code-require` 既有 `AskUserQuestion` | 屏显 |
| E-2(项目不可测) | `code-it` 步骤 8a 守卫不通过 → 跳过步骤 8.5 → 看板"测试状态"= `不适用` → exit 0 | 屏显 |
| E-3(任务类型 = `文档`) | `code-it` 步骤 8.5 跳过写单测 → 写 `unit-test-results.md` = "本任务不涉及单元测试" | 屏显 |
| E-4(`code-unit` 老用户手动调) | 不可用,屏幕输出"⛔ code-unit 已退场" | 屏显 |
| E-5(历史 `test/<TASK-...>/RESULT.md` 存在) | 字节级保留;`code-check` 评审时**仍**读历史路径 | git diff |
| E-6(历史 `auto-report.md` 含 `code-unit` 跳过日志) | 字节级保留(NFR-2 沿用) | git diff |
| E-7(`code-it` 步骤 8.5 自动判定失败) | 沿用既有"失败 → 屏显 → 中断"逻辑 | 屏显 |
| E-8(`code-it` 步骤 8.5 写单测跑通失败) | 沿用原 `code-unit` 步骤 11 错误修复循环;最连续失败 5 次后必须停下询问用户 | `work-log.md` |

## 8. 安全要求

**不适用**(本需求是元技能改造,无安全变更)

## 9. 状态机 / 流程

```
+-------------------------+        +-------------------------+
|     code-unit(退场)     |        |     code-design(沿用)   |
|  - 7 项守卫 → code-it  | -----> |  - 技术选型            |
|  - 写单测 → code-it     |  交接  |  - 架构风格            |
|  (本需求,FR-1)         |        |  - 接口风格            |
+-------------------------+        +-------------------------+

+-------------------------+        +-------------------------+
|     code-it(接管)       |        |     code-plan(沿用)    |
|  - 步骤 8a 守卫 7 项     |        |  - 任务粒度             |
|  - 步骤 8.5 按需写单测  |        |  - 任务类型 6 枚举     |
|  - 步骤 9-12 沿用       |        |  - 测试状态 2 枚举     |
|  (本需求,FR-2/3)       |        |  (沿用 REQ-00031)      |
+-------------------------+        +-------------------------+
```

## 10. 性能与资源

**不适用**(本需求是元技能改造,无运行时性能变更)

## 11. 测试要点

### 11.1 单元测试范围

- **不适用**(`code-plan` 不规划单元测试任务,沿用 REQ-00031 FR-2;`code-unit` 退场后 `code-it` 接管)
- 本设计无 `code-unit` 任务(测试状态 = `不适用`)
- 9 项校验要点(由 `code-it` 末尾兜底负责 + `code-check` 评审时校验):
  - AC-1.1 ~ AC-1.4 `code-unit` 硬删除(`test -f` / `test -d` 校验 NOT_EXISTS)
  - AC-2.1 ~ AC-2.4 `code-it` 步骤 8a 接管(7 项守卫字节级沿用)
  - AC-3.1 ~ AC-3.5 `code-it` 步骤 8.5 接管(自动判定 3 类)
  - AC-4.1 ~ AC-4.3 `code-it` 模板新增"## 单元测试"小节
  - AC-5.1 ~ AC-5.3 `code-plan` 字面改写
  - AC-6.1 ~ AC-6.5 `code-auto` 步骤 4.b 删除
  - AC-7.1 ~ AC-7.3 `code-check` 字面改写
  - AC-8.1 ~ AC-8.4 2 JSON 注册项删除
  - AC-9.1 ~ AC-9.6 4 README + CLAUDE.md 字面改写
  - AC-10.1 ~ AC-10.8 7 项目级规范字面改写
  - AC-11.1 ~ AC-11.5 11 技能描述段字面改写
  - AC-12.1 ~ AC-12.8 零变更校验(历史档案字节级保留)
  - AC-13.1 ~ AC-13.4 看板同步
  - AC-14.1 ~ AC-14.6 与既有规则协同

### 11.2 集成测试范围

- **不适用**

### 11.3 端到端测试范围

- **不适用**

### 11.4 性能/安全测试

- **不适用**

## 12. 规范遵循

- `skill-conventions.md` §规则 1:**遵守**(不碰 frontmatter)
- `module-conventions.md`:**遵守**(删除 `code-unit/templates/` 整体)
- `doc-conventions.md`:**遵守**(4 README 中英版本对仗;主语言版本完整)
- `dashboard-conventions.md`:**遵守**(仅追加 1 行 + 1 条;不触发字段扩展)
- `commit-conventions.md`:**遵守**(`chore(<skill>):` 前缀)
- `encoding-conventions.md`:**遵守**(本需求编号沿用 5 位纯数字)
- `marketplace-protocol.md`:**遵守**(plugin.json / marketplace.json 引用一致)
- 其他 5 个规范:本设计不涉及

## 13. 任务依赖图(10 任务,无依赖)

不适用(本设计拆 10 任务,均**无前置依赖**;沿用 `code-it` 末尾兜底 P-1 推进看板的"按 PLAN.md 任务总览行序"路径)

```
T-001 → T-002 → T-003 → T-004 → T-005 → T-006 → T-007 → T-008 → T-009 → T-010
(0 前置)  (0 前置)  (0 前置)  (0 前置)  (0 前置)  (0 前置)  (0 前置)  (0 前置)  (0 前置)  (0 前置)
```

## 14. 关联计划

| 需求 | 关联点 |
| --- | --- |
| REQ-00031 | "外移单元测试"+"任务粒度收窄"(5 任务已落地) — **前置依赖** |
| REQ-00009 | `code-unit` 守卫 7 项 — **强继承** |
| BUG-00001 | 5 技能加"不修改 SKILL.md"硬约束 — **兼容性** |
| REQ-00026 | SKILL.md 描述通用化扫除 — 最小化变更原则 |
| REQ-00030 | 元技能改 + 12 维度评审 + INV 字节级保留 — 沿用 INV-1 ~ INV-12 |
| REQ-00032 | `code-require` 屏显契约 |
| REQ-00033 | `code-require` 不涉及技术选型 |
| REQ-00020 | 元技能改首条需求 |

## 15. 待澄清 / 未决项(沿用需求 Q-1 ~ Q-8)

- **Q-1**(`code-auto` 步骤 4 屏幕日志格式自动接管):本需求**不**实现(沿用 description 段改写)
- **Q-2**(`code-rule` 沉淀 `testing-conventions.md`):本需求**不**实现(避免越界)
- **Q-3**(`code-it` 步骤 8.5 自动判据表细化):FR-3 锁定 3 大类(函数级 / 文档 / 配置)
- **Q-4**(`code-it` 步骤 8.5 是否接管 `code-unit` 步骤 12 详细覆盖率分析):本需求**不**接管(避免 `code-it` 净增过多行;覆盖率由 `code-check` 评审时按需补)
- **Q-5**(`code-check` 评审清单 §8.7 新增"按需写单测"校验点):本需求**不**实现(避免越界)
- **Q-6**(`code-it` 接管守卫后"不写 test/<任务>/RESULT.md"语义):本需求**统一**改为"不写 `code/<任务>/unit-test-results.md`(或写 '不适用' 占位)"
- **Q-7**(5 测试状态映射):本需求**简化**为 2 状态(`已运行-通过` / `不适用`,沿用 REQ-00031 FR-3)
- **Q-8**(`code-it` 步骤 8.5 是否承担 `code-unit` 步骤 9 错误修复循环):本需求**包含**(FR-3 锁定;E-8 沿用"最连续失败 5 次"语义)

## 16. 变更记录

```
2026-06-15 14:00  详细设计与编码计划完成  REQ-00034(共 10 任务,候选 14 合并;整体=--extensible,功能性=中;5 SKILL.md 改造 + 2 JSON 字面 + 4 README 字面 + 7 规范字面 + 11 描述段字面 + 1 目录删除;净变化约 -600 ~ -800 行)  REQ-00034
```
