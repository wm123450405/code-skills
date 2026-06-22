# 需求提示词文档 — 优化 /code-it 技能单测判定(从工程粒度细化到模块粒度)

- 需求编码:REQ-00038
- 所属版本:V0.0.3
- 文档创建时间:2026-06-22 13:00
- 最近更新:2026-06-22 13:00
- 文档状态:草稿(待 code-design 推进)
- 上游:用户口头/文本输入(2026-06-22 12:30)
- 遵循规范:`./assistants/rules/` 下 8 个文件(全沿用,无新增)
- 涉及技能:`code-it`(主改造)+ `code-plan`(适配任务粒度描述)+ 后续 `code-design` / `code-plan` / `code-it` / `code-check` 4 技能流水线

## 1. 需求概述

**优化** `/code-it` 技能的单测判定逻辑:从**工程粒度**细化到**模块粒度**。识别改修代码所属模块(子目录 / 子包 / monorepo workspace),对每个模块独立执行 7 项可测性守卫检查,单测写到该模块的约定测试目录(而非工程根)。

**核心机制**:
- **模块识别**(FR-1):综合多源识别 — 声明文件(pnpm-workspace.yaml / package.json#workspaces / pom.xml#modules / Cargo.toml#workspace.members / lerna.json / nx.json / turbo.json 等)+ git diff 变更路径的公共子目录 + 规范说明
- **模块可测性守卫**(FR-2):沿用原 7 项检查(字节级沿用 REQ-00034),但检查位置从 CWD 根改为**每个模块目录**
- **模块级单测输出**(FR-3):每个通过守卫的模块独立识别其约定测试目录,单测写到正确位置
- **`unit-test-results.md` 多模块支持**(FR-4):模板新增"## 各模块单测结果"小节,每个通过的模块独立记录

涉及 1 SKILL.md(`code-it`)+ 1 模板(`unit-test-results.md` 改造),共约 2 个文件,净变化约 +100 ~ +200 行(扩展,不删除)。

## 2. 背景与目标

### 2.1 背景

V0.0.3 期间(2026-06-15)通过 REQ-00034 已将 `code-unit` 删除并整合进 `code-it`,落地了"按需写单测"框架。但该框架的判定粒度是**工程根级**:

| 维度 | REQ-00034 落地后(本需求前) | 现状痛点 |
| --- | --- | --- |
| 守卫粒度 | CWD 根 7 项 | monorepo 工程根无 `package.json` 的 `scripts.test` → 整工程跳过 → 子模块单测需求被忽略 |
| 单测输出 | CWD 根 `test/` | 多模块单测挤到根 → 模块边界破坏 |
| 多语言 | 单一框架 | Node.js + Go + Python 混合工程单测框架混乱 |

**用户原始输入(verbatim)**:
> 现有的 `/code-it` 技能在判断是否需要编写单元测试的逻辑上存在遗漏,有些工程下的子模块需要单独编写单元测试;优化 `/code-it` 技能,判断逻辑不能以整个工程为为主,而是要判断改修的代码属于哪个模块的,单独判断模块是否应该编写单元测试。

### 2.2 业务目标

- 显式扩展 `code-it` 单测判定为模块粒度
- 支持 monorepo / 多语言 / 多模块工程
- 守卫检查位置从 CWD 根改为模块目录
- 单测输出位置从 CWD 根 `test/` 改为模块约定测试目录
- 100% 兼容 REQ-00034 工程根级行为(无声明文件时退化)
- `unit-test-results.md` 模板支持多模块结果记录

### 2.3 本次目标

- **范围**:**改造** `code-it` 步骤 8a / 8.5 + **改造** 1 模板(`unit-test-results.md`)+ **适配** `code-plan` 任务粒度描述
- **不涉及**:`code-it` frontmatter / 既有"## 工作流程"小节 / "## 不要做的事"小节
- **不涉及**:其他 10 个 `code-*` 技能 SKILL.md / rules/ 目录
- **不涉及**:历史 V0.0.2 / V0.0.3 既有 `test/<TASK-...>/` 目录(字节级保留)
- **不涉及**:BUG-00001 "不修改 SKILL.md"硬约束(本需求不冲突)
- 触发 1 次看板同步:`assistants/V0.0.3/RESULT.md` §需求清单 追加 1 行 + §变更记录 追加 1 条

## 3. 用户角色与场景

### 3.1 角色

- **monorepo 工程开发者**:在 monorepo 子包下写代码,期望该子包的单测自动写上
- **多语言工程开发者**:在 Node.js + Go + Python 混合工程中,期望各语言单测写到各自测试目录
- **元技能维护者**:希望 `code-it` 单测判定更精细,避免 monorepo 下整工程跳过的尴尬
- **code-auto 编排者**:任务循环步骤 4 中,期望看到"模块级守卫检查结果"而非"工程根级"

### 3.2 场景

| 场景 | 现状体验(REQ-00034 落地后) | 改造后体验(本需求) |
| --- | --- | --- |
| monorepo 工程子包写代码 | 整工程跳过单测(`code-it` 步骤 8a 不通过) | 子包独立守卫通过 → 单测写到子包测试目录 |
| 多语言混合工程 | 单一框架(只看工程根 `package.json`) | 每个语言模块独立判定(Go 模块写 Go 测试,Python 模块写 pytest) |
| library 子项目 | 整工程跳过(根无 `package.json` 的 `scripts.test`) | library 子目录独立判定 |
| `unit-test-results.md` 输出 | 单模块结果(工程根) | 多模块结果(每个通过的模块独立记录) |
| 单工程(非 monorepo) | 1 模块 = 1 整工程,行为字节级沿用 | 1 模块 = 1 整工程,行为字节级沿用(零回归) |

## 4. 功能需求(FR)

### FR-1:`code-it` 步骤 8a 之前新增"模块识别"子步骤

- **位置**:`plugins/code-skills/skills/code-it/SKILL.md` 在既有"## 步骤 8 实施开发"**之后**、"## 步骤 8a 项目可测性守卫"**之前**新增"## 步骤 8a.0 — 模块识别"
- **输入**:`code-it` 步骤 8 实施开发的变更文件列表(`git diff --name-only` 输出)
- **输出**:`modules: string[]`(模块路径列表,相对 CWD)
- **识别优先级链**(从高到低):
 1. **声明文件**(monorepo workspace):
 - `pnpm-workspace.yaml` → 读 `packages` 字段
 - `package.json` 的 `workspaces` 字段 → 枚举 `packages` / `nohoist`
 - `lerna.json` 的 `packages` 字段
 - `nx.json` / `turbo.json` 的 workspace 配置
 - `pom.xml` 的 `<modules>` 字段(Maven 多模块)
 - `Cargo.toml` 的 `[workspace] members` 字段
 - `go.mod` 的 `module` 路径 + 子目录(约定)
 2. **git diff 退化**:无声明文件 → 取变更文件路径的最长公共子目录
 3. **CWD 根退化**:无变更路径(理论不可能)→ 退化为 `[CWD]`
- **不引入用户问路**:**不**弹 `AskUserQuestion`(NFR-3 强约束)
- **依据规范**:`./assistants/rules/encoding-conventions.md` §规则 1(沿用)+ `./assistants/rules/coding-style.md`(待读取子模块定义相关条款)

### FR-2:`code-it` 步骤 8a 守卫位置从 CWD 根改为模块目录

- **位置**:`plugins/code-skills/skills/code-it/SKILL.md` §"步骤 8a.1 守卫检查项清单"+ §"步骤 8a.2 守卫判定逻辑" + §"步骤 8a.4 屏幕报告格式"
- **改造内容**:
 - **8a.1 检查位置**:`CWD 根` → `模块目录`(对每个识别的模块独立执行 7 项检查)
 - **8a.2 判定逻辑**:
 - 原:命中任一(根级 7 项之一)→ testable = True
 - 新:对每个模块独立执行 7 项检查,至少 1 个模块命中 → testable = True;全部模块不命中 → testable = False
 - **8a.4 屏显格式**:增加"模块级守卫检查详情",每个模块独立显示
- **7 项检查字节级沿用 REQ-00034**(不修改检查项本身):
 1. `package.json` 含 `scripts.test`(检查位置:**模块目录**)
 2. `pyproject.toml` 含测试配置(检查位置:**模块目录**)
 3. `Cargo.toml`(检查位置:**模块目录**)
 4. `go.mod`(检查位置:**模块目录**)
 5. `pom.xml`(检查位置:**模块目录**)
 6. `build.gradle` / `build.gradle.kts`(检查位置:**模块目录**)
 7. `test/` 目录(检查位置:**模块目录**)

### FR-3:`code-it` 步骤 8.5 单测输出位置从工程根改为模块级测试目录

- **位置**:`plugins/code-skills/skills/code-it/SKILL.md` §"步骤 8.5.2 任务性质自动判定" + §"步骤 8.5.5 产出物格式"
- **改造内容**:
 - **8.5.2 判定逻辑扩展**:
 - 每个通过的模块独立识别其约定测试目录
 - 多个模块通过 → 每个模块分别写单测
 - 1 个模块通过 → 该模块测试目录
 - 全部不通过 → 跳过(已由步骤 8a 判定)
 - **8.5.5 产出物格式**:`unit-test-results.md` 模板新增"## 各模块单测结果"小节,每个通过的模块独立记录
- **测试目录识别优先级链**(每个通过的模块独立):
 1. 模块内 `package.json#scripts.test` 含 `jest` / `vitest` / `mocha` 配置 → 沿用 `testMatch` / `testRegex`
 2. 模块内 `pyproject.toml` 含 `[tool.pytest.ini_options]` → 沿用 `testpaths`
 3. 模块内 `Cargo.toml` → 约定 `src/` 同包 `#[cfg(test)]` 或 `tests/`
 4. 模块内 `go.mod` → 约定同包 `*_test.go`
 5. 模块内 `pom.xml` / `build.gradle` → 约定 `src/test/`
 6. 无约定 → 模块根 `test/` 目录
 7. 仍无 → CWD 根 `test/` 目录(原 REQ-00034 行为退化路径)

### FR-4:`unit-test-results.md` 模板多模块支持

- **位置**:`plugins/code-skills/skills/code-it/templates/RESULT.md` §"## 单元测试(由 code-it 内化)"小节
- **改造内容**:
 - 原小节"## 单元测试(由 code-it 内化)"字节级保留
 - **新增**"## 各模块单测结果"小节,字段:
 ```
 ## 各模块单测结果

 ### 模块 <path>
 - 守卫检查:✓ / ✗
 - 检查位置:<模块目录>
 - 测试框架:<Jest / Pytest / Go test / ...>
 - 新增/修改的测试文件:<...>
 - 跑通情况:<通过 N 个 / 失败 M 个>

 ### 模块 <path>
 ...
 ```
- **不修改**:`code-it/templates/RESULT.md` 既有"## 单元测试"小节(字节级保留)
- **不修改**:`code-it/templates/RESULT.md` 其他既有章节(字节级保留)
- **不触发**:`./assistants/rules/dashboard-conventions.md` §规则 1(本需求**不**新增列)

### FR-5:`code-plan` 任务粒度描述适配(可选)

- **位置**:`plugins/code-skills/skills/code-plan/SKILL.md` §"步骤 10A 任务拆分" → "## 测试状态字段语义"
- **改造内容**(可选,字面新增 1 句):
 - 既有"由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)" → 改为"由 `code-it` 内化(`code-it` 步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按模块写单测)"
- **不修改**:`code-plan` 其他既有章节

## 5. 非功能需求 / 约束(NFR)

- **NFR-1(性能)**:模块识别 + 守卫检查总耗时 < 2 秒(典型 monorepo 100 模块下 < 2 秒)
- **NFR-2(兼容性)**:
 - 100% 兼容 REQ-00034 工程根级行为(无声明文件时退化为 CWD 根)
 - 单模块工程 = 单模块识别 = 字节级沿用原 REQ-00034
 - `code-unit` 退场后所有单测能力仍通过 `code-it` 接管
- **NFR-3(零规范变更)**:
 - **不**修改 `code-it` frontmatter(L1-3 字节级保留)
 - **不**修改 `code-it` 既有"## 工作流程"小节
 - **不**修改 `code-it` "## 不要做的事"小节
 - **不**触发 `AskUserQuestion`(NFR-3 强约束,模块识别全部自动)
 - **不**新增 CLI 参数(无 `--module` 等)
- **NFR-4(不归一化)**:
 - 15 字面兼容性(沿用 REQ-00037 / PD-2 锁定):不归一化既有单测字面
 - 既有 7 项检查项字节级保留(仅检查位置从 CWD 根 → 模块目录)
- **NFR-5(可追溯)**:
 - `unit-test-results.md` 模板记录每个模块的检查位置 / 守卫详情 / 跑通情况
 - `work-log.md` 追加"## 模块识别"小节,记录识别的模块列表
- **NFR-6(幂等)**:多次执行 `code-it` 同任务,模块识别 + 守卫检查结果一致

## 6. 页面与界面

不适用(本需求是 Markdown 技能行为变更,无 UI 改动)

## 7. 交互逻辑

不适用(无状态机变更;沿用 REQ-00034 既有"按需写单测"3 类任务自动判定)

## 8. 数据与状态

- **输入数据**:
 - `git diff --name-only` 输出(变更文件列表,字符串数组)
 - 声明文件字面(pnpm-workspace.yaml / package.json#workspaces / pom.xml#modules 等)
- **输出数据**:
 - `modules: string[]`(模块路径列表,相对 CWD)
 - `moduleTestable: Map<string, boolean>`(每个模块的守卫结果)
 - `moduleTestDir: Map<string, string>`(每个通过模块的测试目录)
- **数据生命周期**:
 - 模块识别:步骤 8a.0 一次执行,缓存到 `code-it` 内部
 - 守卫检查:步骤 8a.1 一次执行,缓存到 `code-it` 内部
 - 单测输出:步骤 8.5 一次执行,产物写到 `code/<任务>/unit-test-results.md`

## 9. 边界与异常

- **E-1**:声明文件不存在 → 退化为 git diff 公共子目录
- **E-2**:git diff 失败(非 git 仓库)→ 退化为 CWD 根
- **E-3**:变更路径跨越多个模块 → 多个模块分别写单测
- **E-4**:模块目录无法访问(权限/不存在)→ 跳过该模块,屏显警告
- **E-5**:多模块通过但只有一个有变更 → 只给该模块写单测
- **E-6**:多模块通过且多个有变更 → 每个模块分别写单测
- **E-7**:单模块识别失败(理论不可能)→ 退化为 CWD 根(原 REQ-00034 行为)
- **E-8**:历史 `code-unit` 行为已退场(沿用 REQ-00034 NFR-2)

## 10. 验收标准 (AC)

### AC-1:monorepo 工程子包识别正确

- **对应需求**:FR-1
- **验证方式**:端到端测试
- **步骤**:
 1. 创建 1 个 monorepo 测试工程(根级 `pnpm-workspace.yaml` 含 `packages: [packages/*]`)
 2. 在 `packages/foo/` 下写 1 个测试文件
 3. 调 `code-it TASK-REQ-NNNNN-NNNNN`
 4. 检查 `work-log.md` "## 模块识别"小节,应识别到 `packages/foo/` 模块
- **预期结果**:模块识别 = `[packages/foo]`
- **优先级**:高

### AC-2:模块可测性守卫位置正确(模块目录非 CWD 根)

- **对应需求**:FR-2
- **验证方式**:端到端测试
- **步骤**:
 1. 创建 1 个 monorepo,根级**不**含 `package.json` 的 `scripts.test`,子包 `packages/bar/` 含 `package.json` 的 `scripts.test`
 2. 调 `code-it`(无 monorepo 守卫命中)
 3. 检查屏显"守卫检查详情",应显示"模块 packages/bar: ✓"和"模块 CWD 根: ✗"
- **预期结果**:整体 testable = True(子包通过即可)
- **优先级**:高

### AC-3:多模块单测写到各自测试目录

- **对应需求**:FR-3
- **验证方式**:端到端测试
- **步骤**:
 1. 创建 1 个 monorepo 含 2 子包(Go + Python),各含独立测试配置
 2. 在 2 子包下分别写代码 + 调 `code-it`
 3. 检查 `unit-test-results.md` "## 各模块单测结果"小节,应分别记录 2 模块结果
 4. 检查实际生成的单测文件位置:Go 单测在子包 `*_test.go`,Python 单测在子包 `test_*.py`
- **预期结果**:单测文件位置符合各模块约定
- **优先级**:高

### AC-4:单模块工程(非 monorepo)行为字节级沿用

- **对应需求**:NFR-2 兼容性
- **验证方式**:回归测试
- **步骤**:
 1. 创建 1 个单模块工程(根级 `package.json` 含 `scripts.test`)
 2. 调 `code-it`
 3. 检查守卫检查详情,应与 REQ-00034 落地结果字节级一致
- **预期结果**:零回归
- **优先级**:高

### AC-5:`unit-test-results.md` 模板多模块支持

- **对应需求**:FR-4
- **验证方式**:静态校验
- **步骤**:
 1. 读 `plugins/code-skills/skills/code-it/templates/RESULT.md`
 2. 检查"## 单元测试(由 code-it 内化)"小节字节级保留
 3. 检查"## 各模块单测结果"小节新增,字段完整
- **预期结果**:既有 0 改 + 新增 1 小节
- **优先级**:中

### AC-6:模块识别无 `AskUserQuestion` 问路

- **对应需求**:FR-1 + NFR-3
- **验证方式**:静态校验
- **步骤**:
 1. 读 `code-it/SKILL.md` §"步骤 8a.0 模块识别"
 2. 检查流程中**无** `AskUserQuestion` 调用
- **预期结果**:零问路
- **优先级**:高

### AC-7:性能 < 2 秒

- **对应需求**:NFR-1
- **验证方式**:性能测试
- **步骤**:
 1. 在 1 个 100 模块的 monorepo 下调 `code-it`
 2. 测量步骤 8a.0 + 8a 总耗时
- **预期结果**:总耗时 < 2 秒
- **优先级**:中

## 11. 关联需求

| 关联需求编码 | 关联点 | 影响 |
| --- | --- | --- |
| REQ-00034 | FR-2 / FR-3 定义了"按需写单测"工程根级框架 | 本需求在其基础上细化到模块粒度;100% 兼容 + 扩展 |
| REQ-00031 | `code-unit` 退场为可选 | 本需求不涉及 `code-unit` 退场逻辑(已由 REQ-00034 落地) |
| REQ-00037 | 缺陷修复流程的状态推进 | 本需求不涉及缺陷路径(沿用既有 `code-it` §缺陷分支 17-25) |

## 12. 待澄清 / 未决项

- **Q-1**:monorepo 工具覆盖范围 — 已确认支持 pnpm / npm workspace / lerna / nx / turbo / Maven / Cargo / Go(约定)
- **Q-2**:模块内无 `git` 可用 → 退化为 CWD 根
- **Q-3**:跨平台路径分隔符(Windows `\` / Unix `/`)— 沿用 `path.posix` 规范化

## 13. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-22 13:00 | v1 | 初始创建 | 完成首次需求分析;5 FR / 6 NFR / 7 AC;1 轮 `AskUserQuestion` 澄清;FR-1 ~ FR-5 字面定义 + 模块识别优先级链 + 7 项守卫字节级沿用 + 测试目录识别优先级链 + 模板多模块支持 | 用户 |
