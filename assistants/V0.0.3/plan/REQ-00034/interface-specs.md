# 接口详细规格 — REQ-00034

更新时间:2026-06-15 14:00
版本:V0.0.3

## 接口清单(本设计 0 新增对外接口,2 新增内部接口)

| 接口 | 形式 | 状态 | 职责 |
| --- | --- | --- | --- |
| `code-it.project_testable_guard()` | 函数(内部) | 新增 | 项目可测性守卫 7 项检查 |
| `code-it.write_unit_tests_on_demand(task_num)` | 函数(内部) | 新增 | 按需写单测(自动判定 3 类) |

## 接口:`code-it.project_testable_guard()`

- **形式**:Python 函数(本技能内部,不暴露给项目代码)
- **签名**:`def project_testable_guard() -> bool:`
- **入参**:**无**
- **出参**:`testable: bool` — True 表示项目可测,False 表示不可测
- **行为**:
  1. 顺序执行 7 项检查(`package.json` 含 `scripts.test` / `pyproject.toml` 含 `[tool.pytest*]` / `Cargo.toml` / `go.mod` / `pom.xml` / `build.gradle` / `test/` 目录)
  2. 命中任一 → 返回 True
  3. 全部不命中 → 返回 False
- **错误码**:**不适用**(本技能内部函数)
- **示例**:
  - 输入:CWD = Node.js 项目,`package.json` 含 `scripts.test`
  - 输出:True
- **版本策略**:**不适用**(本技能内部)
- **兼容策略**:**不适用**
- **依据规范**:字节级沿用 `code-unit` 步骤 0a.1 + 0a.2

## 接口:`code-it.write_unit_tests_on_demand(task_num)`

- **形式**:Python 函数(本技能内部,不暴露给项目代码)
- **签名**:`def write_unit_tests_on_demand(task_num: str) -> None:`
- **入参**:`task_num: str` — 本任务编码,如 `TASK-REQ-00034-00003`
- **出参**:**无**(副作用:写测试代码到 CWD + 写 `code/<任务>/unit-test-results.md`)
- **行为**:
  1. 读 `plan/<需求>/PLAN.md` 任务详情,识别任务类型
  2. 自动判定:
     - 任务类型 = 文档 → 跳过写单测,写 `unit-test-results.md` = "本任务不涉及单元测试"
     - 任务类型 ∈ {新增, 修改, 重构, 修复} + 涉及"函数级"改动 → 写单测 + 跑通 + 写 `unit-test-results.md`
     - 任务类型 ∈ {配置, 类型定义} → 跳过写单测,写 `unit-test-results.md` = "本任务不涉及单元测试"
  3. 屏幕输出:
     ```
     === code-it 按需写单测(守卫通过)===
     任务:<task_num>
     判定:写单测 / 跳过单测
     测试框架:<Jest / Pytest / ...>
     ```
- **错误码**:**不适用**
- **示例**:
  - 输入:`task_num = "TASK-REQ-00034-00003"`,任务类型 = 文档
  - 输出:写 `code/TASK-REQ-00034-00003/unit-test-results.md` = "## 单元测试(由 code-it 内化)\n\n守卫判定: 可测\n任务类型: 文档\n本任务不涉及单元测试"
- **版本策略**:**不适用**
- **兼容策略**:**不适用**
- **依据规范**:本需求 FR-3 锁定

## 接口:`code-it/templates/RESULT.md` 模板

- **形式**:Markdown 模板
- **路径**:`plugins/code-skills/skills/code-it/templates/RESULT.md`
- **小节内容**:
  ```markdown
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

## 接口:`code-plan/SKILL.md` 测试状态字段语义

- **形式**:Markdown 字面改写
- **5 处**:`code-plan/SKILL.md` L368 / L431 / L445 / L454 / L1105
- **改写**:见 `plan/REQ-00034/design-notes.md` §3.3.1

## 接口:`code-auto/SKILL.md` 步骤 4.b 删除

- **形式**:Markdown 整段删除
- **整段**:`code-auto/SKILL.md` L388-411
- **字面删除 10 处**:L213-227(子技能调用表 4 行) + L432-433 + L449 + L624-625 + L672 + L692 + L711 + L741 + L797 + L806 + L834

## 接口:`code-check/SKILL.md` test 引用收窄

- **形式**:Markdown 字面改写
- **10 处**:`code-check/SKILL.md` L3 + L21 + L40-41 + L56 + L72 + L96 + L151 + L281 + L608 + L615

## 接口:plugin.json + marketplace.json 注册项删除

- **形式**:JSON 字面删除
- **3 处**:`plugin.json` L15(`keywords[]` 1 项) + `marketplace.json` L24(`keywords[]` 1 项) + L39(`skills[]` 1 项)

## 接口:4 README + CLAUDE.md 字面改写

- **形式**:Markdown 字面改写
- **5 个文件**

## 接口:7 项目级规范字面改写

- **形式**:Markdown 字面改写(只改字面,核心约束保留)
- **7 个文件**

## 接口:11 技能描述段字面改写

- **形式**:YAML frontmatter 字面改写
- **11 个 SKILL.md** 的 `description` 字段
- **frontmatter L1-3 字节级保留**
