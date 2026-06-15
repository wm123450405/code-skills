# 模块详细化 — REQ-00034

更新时间:2026-06-15 14:00
版本:V0.0.3

## 模块清单(本设计 0 新增)

| 模块名 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| — | — | — | (本设计是 SKILL.md 文字改造 + 1 目录删除,无模块新增) | — |

## 行为接管:`code-it` 步骤 8a + 步骤 8.5

### 步骤 8a — 项目可测性守卫

#### 关键"代码"
字节级沿用 `code-unit` 步骤 0a.1(7 项检查) + 0a.2(判定逻辑) + 0a.4(屏幕报告格式)。详见 `plan/REQ-00034/RESULT.md` §3.2.1。

#### 调用顺序
1. `code-it` 步骤 7 处理任务前置依赖
2. `code-it` 步骤 8 探索项目代码
3. `code-it` 步骤 8a 项目可测性守卫(本需求**新增**)
4. `code-it` 步骤 8.5 按需写单测(testable = True 时)
5. `code-it` 步骤 9 编译/运行(沿用既有)

#### 状态归属
`testable`(本任务局部变量,内存级,**不**持久化)

#### 与概要设计的对应
- `design/.../RESULT.md` §3 决策 D-2(守卫接管)
- `design/.../RESULT.md` §8 修改文件定位表 `code-it/SKILL.md` 第 2 行

#### 符合的规范
- `skill-conventions.md` §规则 1(SKILL.md frontmatter 字节级保留)

### 步骤 8.5 — 按需写单测

#### 关键"代码"
自动判定 3 类,无 `AskUserQuestion`。详见 `plan/REQ-00034/RESULT.md` §3.2.2。

#### 调用顺序
紧跟步骤 8a(testable = True 时)

#### 状态归属
无(产出物路径 = `code/<任务>/unit-test-results.md`)

#### 与概要设计的对应
- `design/.../RESULT.md` §3 决策 D-3 / D-4 / D-5 / D-6 / D-7

#### 符合的规范
- `skill-conventions.md` §规则 1
- `module-conventions.md`(本仓库元技能仓库,无工程代码)
