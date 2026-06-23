# 概要设计 — REQ-00038 优化 /code-it 技能单测判定(从工程粒度细化到模块粒度)

- 需求编码:REQ-00038
- 所属版本:V0.0.3
- 文档创建时间:2026-06-22 13:30
- 最近更新:2026-06-22 13:30
- 文档状态:已完成
- 上游:`./assistants/V0.0.3/require/REQ-00038/RESULT.md`
- 遵循规范:`./assistants/rules/` 下 12 个文件(全沿用,无新增)
- 涉及技能:`code-it`(主改造)+ `code-plan`(FR-5 字面改写)+ `code-check`(适配判定文件位置)
- 涉及模板:`code-it/templates/RESULT.md`(追加"## 各模块单测结果"小节)

## 1. 设计目标

- **整体设计目标**:`--balanced`(用户确认 2026-06-22)
- **维度优先级**:功能性 = 高(主流程行为扩展;不新增依赖)
- **设计目标确认路径**:用户手动调子技能,触发 1 个 `AskUserQuestion`(整体设计目标);扩展性判定 = 不触发(模块识别为**只读** monorepo 声明文件,不引入新三方依赖;详见 `rule-compliance.md` §3)

## 2. 设计概述

**核心决策**:**改造** `code-it` 步骤 8a 守卫位置(从 CWD 根 → 模块目录)+ **新增** 步骤 8a.0 模块识别子步骤 + **改造** `code-it/templates/RESULT.md` "## 单元测试"小节后追加"## 各模块单测结果"小节(支持多模块记录)+ **字面改写** `code-plan` 任务粒度描述(FR-5)。

**关键边界**:
- 7 项守卫**字节级沿用** REQ-00034(检查项本身 0 改,仅位置从 CWD 根改为模块目录)
- 单模块工程行为**字节级沿用** REQ-00034(无声明文件时退化为 CWD 根,1 模块 = 1 整工程,零回归)
- `unit-test-results.md` 模板"## 单元测试"小节**字节级保留**(NFR-4 沿用),仅**追加**"## 各模块单测结果"小节
- 模块识别优先级链:**声明文件**(7 套 monorepo 工具)→ git diff 公共子目录 → CWD 根(原 REQ-00034 行为退化)
- **不**触发 `AskUserQuestion`(NFR-3 强约束,模块识别全部自动)
- **不**新增 CLI 参数(NFR-3 强约束)

## 3. 关键设计决策(8 项,详见 `design-notes.md`)

### 决策 D-1:新增 `code-it` 步骤 8a.0 模块识别子步骤(FR-1 锁定)

**理由**:模块识别是模块级守卫的前置;识别结果(模块路径列表)直接喂给步骤 8a.1 守卫;`code-it` 步骤 8a.0 锚点 = "## 步骤 8"之后,"## 步骤 8a 守卫"之前

### 决策 D-2:模块识别优先级链 = 声明文件 > git diff 公共子目录 > CWD 根(FR-1 锁定)

**理由**:声明文件是 monorepo 工程最权威的模块划分依据(pnpm / npm workspace / lerna / nx / turbo / Maven / Cargo / Go);无声明文件 → git diff 退化(NFR-2 兼容性);无变更路径 → CWD 根退化(理论不可能但需兜底)

### 决策 D-3:7 项守卫字节级沿用 REQ-00034(检查项 0 改,仅位置从 CWD 根 → 模块目录)(FR-2 / NFR-4 锁定)

**理由**:7 项守卫是已落地的产品需求(REQ-00009);检查项本身不改避免行为漂移;**仅**改检查位置 = 模块目录(NFR-1 性能约束 < 2 秒)

### 决策 D-4:步骤 8a 判定逻辑扩展为"任一模块通过即 testable = True"(FR-2 锁定)

**理由**:原"工程根级单点判定"在 monorepo 下粒度过粗;新逻辑 = 对每个模块独立执行 7 项检查,至少 1 个模块命中 → testable = True;全部模块不命中 → testable = False(沿用原"全部不命中"行为)

### 决策 D-5:步骤 8a.4 屏显格式扩展为"模块级守卫检查详情"(FR-2 锁定)

**理由**:`code-auto` 编排者期望看到"模块级守卫检查结果"而非"工程根级"(需求 §3.1 角色);屏显契约 0 触发其他字段扩展(沿用既有 `code-check` 8 维度屏显格式)

### 决策 D-6:`unit-test-results.md` 模板新增"## 各模块单测结果"小节,既有"## 单元测试"小节字节级保留(FR-4 / NFR-4 锁定)

**理由**:既有"## 单元测试"小节是工程根级单结果记录的产物;新增"## 各模块单测结果"小节专门记录多模块结果;既有 0 改 + 新增 1 小节 = 100% 兼容 REQ-00034 既有 RESULT.md 字段(NFR-4)

### 决策 D-7:`code-plan` 任务粒度描述字面改写 1 句(FR-5 锁定)

**理由**:既有"由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)" → 改为"由 `code-it` 内化(`code-it` 步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按模块写单测)";**仅**字面增量,不新增/删除字段;沿用既有"测试状态"语义(2 状态)

### 决策 D-8:不修改其他 11 个 `code-*` 技能 SKILL.md 核心工作流(沿用 REQ-00034 INV-4)

**理由**:`code-require` / `code-design` / `code-fix` / `code-init` / `code-publish` / `code-version` / `code-rule` / `code-merge` / `code-answer` / `code-dashboard` / `code-check` 11 个 SKILL.md 的核心工作流 0 改;`code-check` 仅适配判定文件位置(读 `unit-test-results.md` 时按模块拆结果)

## 4. 模块拆分(本设计 1 主改造 + 1 模板改造 + 1 文档字面改写)

| 模块名 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| `code-it` 步骤 8a.0 模块识别 | `plugins/code-skills/skills/code-it/SKILL.md > ### 步骤 8a.0 — 模块识别`(新增) | 新增 | 综合多源识别模块路径列表 | 无(只读声明文件) |
| `code-it` 步骤 8a 守卫位置改造 | `plugins/code-skills/skills/code-it/SKILL.md > ### 步骤 8a` 守卫检查项 / 判定逻辑 / 屏显格式(扩展) | 修改(扩展) | 守卫检查位置从 CWD 根 → 模块目录 | `code-it` 步骤 8a.0 |
| `code-it` 步骤 8.5 单测输出位置扩展 | `plugins/code-skills/skills/code-it/SKILL.md > ### 步骤 8.5` 单测输出位置(扩展) | 修改(扩展) | 多模块单测写到各自测试目录 | `code-it` 步骤 8a.0 / 8a |
| `code-it/templates/RESULT.md` 多模块支持 | `plugins/code-skills/skills/code-it/templates/RESULT.md > ## 单元测试(由 code-it 内化)` 小节后追加"## 各模块单测结果" | 修改(追加 1 小节) | 多模块单测结果记录 | 无 |
| `code-plan` 任务粒度描述字面改写 | `plugins/code-skills/skills/code-plan/SKILL.md > ## 步骤 10A 任务拆分 > ## 测试状态字段语义` 1 句字面改写 | 修改(字面) | 任务粒度描述对齐 REQ-00038 模块识别 | 无 |

**自检**(`module-conventions.md §规则 1`):
- ✅ 所有资源文件均在 `plugins/code-skills/skills/<name>/` 子目录内(SKILL.md / templates/ 既有结构 0 改)
- ✅ 命名符合 kebab-case 约定

## 5. 接口(本设计 0 新增对外接口,1 类内部行为扩展)

| 接口 | 形式 | 状态 | 职责 |
| --- | --- | --- | --- |
| `code-it` 步骤 8a.0 模块识别 | 函数(内部) | 新增 | 综合多源识别模块路径列表,返回 `modules: string[]` |
| `code-it` 步骤 8a 守卫位置 | 函数(内部) | 修改(位置扩展) | 守卫检查位置从 CWD 根 → 模块目录,对每个模块独立执行 7 项检查 |
| `code-it` 步骤 8.5 单测输出位置 | 函数(内部) | 修改(位置扩展) | 多模块单测写到各自测试目录 |
| `code-it/templates/RESULT.md` "## 各模块单测结果" 小节 | Markdown | 新增(模板) | 多模块单测结果记录字段 |
| `code-plan` 任务粒度描述 | Markdown | 字面改写 | 任务粒度描述对齐模块识别 |

## 6. 数据结构(本设计 0 新增数据库/缓存,3 个运行时数据)

| 字段 | 类型 | 生命周期 | 说明 |
| --- | --- | --- | --- |
| `modules: string[]` | 字符串数组(模块路径,相对 CWD) | `code-it` 步骤 8a.0 一次执行,缓存到内部 | 模块识别结果 |
| `moduleTestable: Map<string, boolean>` | 字典(模块路径 → 是否可测) | `code-it` 步骤 8a.1 一次执行,缓存到内部 | 每个模块的守卫结果 |
| `moduleTestDir: Map<string, string>` | 字典(模块路径 → 测试目录) | `code-it` 步骤 8.5.2 一次执行,缓存到内部 | 每个通过模块的测试目录 |

## 7. 三方依赖(本设计 0 新增)

| 依赖名 | 用途 | 必要性 | 替代评估 |
| --- | --- | --- | --- |
| — | — | — | (NFR-3 0 新增,只读 monorepo 声明文件) |

## 8. 修改文件定位(语义化锚点,本设计 4 个文件)

| 路径 | 锚点 | 改造内容 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-it/SKILL.md` | §"## 步骤 8a" 之后(锚点 = `### 步骤 8a — 项目可测性守卫` 之前,作为 8a 的子节前序) | 新增 `### 步骤 8a.0 — 模块识别` 小节 |
| `plugins/code-skills/skills/code-it/SKILL.md` | §"### 步骤 8a.1 守卫检查项清单"(原 L563) | 改写"仅检查项目根" → "仅检查模块目录(对每个识别的模块独立执行 7 项检查)" |
| `plugins/code-skills/skills/code-it/SKILL.md` | §"### 步骤 8a.2 守卫判定逻辑"(原 L575) | 改写判定逻辑 = 对每个模块独立执行 7 项检查 + 至少 1 个模块命中 → testable = True |
| `plugins/code-skills/skills/code-it/SKILL.md` | §"### 步骤 8a.4 屏幕报告格式"(原 L599) | 增加"模块级守卫检查详情",每个模块独立显示 |
| `plugins/code-skills/skills/code-it/SKILL.md` | §"### 步骤 8.5.2 任务性质自动判定"(原 L657) | 改写"写到 CWD 下项目测试目录" → "对每个通过的模块识别其约定测试目录,多模块分别写单测" |
| `plugins/code-skills/skills/code-it/SKILL.md` | §"### 步骤 8.5.5 产出物格式"(原 L699) | 改写"沿用 code-it/templates/RESULT.md 模板新增 ## 单元测试 小节" → "沿用 code-it/templates/RESULT.md 模板 ## 单元测试(由 code-it 内化) 小节 + ## 各模块单测结果 小节" |
| `plugins/code-skills/skills/code-it/templates/RESULT.md` | §"## 9. 单元测试(由 code-it 内化)" 小节后(L153 末尾) | 新增 `## 各模块单测结果` 小节 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | §"## 步骤 10A 任务拆分 > ## 测试状态字段语义"(原既有 1 句) | 字面改写:"由 `code-it` 内化(`code-it` 步骤 8a 守卫 + 步骤 8.5 按需写单测)" → "由 `code-it` 内化(`code-it` 步骤 8a.0 模块识别 + 步骤 8a 守卫 + 步骤 8.5 按模块写单测)" |

## 9. 不变量(共 8 条,INV-1 ~ INV-8)

| INV | 约束 | 范围 |
| --- | --- | --- |
| INV-1 | frontmatter L1-3 字节级保留 | `code-it` / `code-plan` |
| INV-2 | "## 不要做的事" 既有小节 0 改 | `code-it` / `code-plan` |
| INV-3 | "## 工作流程" 既有步骤字节级保留 | `code-it` 步骤 0a/0-8/8a/8.5/8.6/8.7/9-16;`code-plan` 既有步骤字节级保留 |
| INV-4 | `code-it` "## 单元测试(由 code-it 内化)" 既有小节 0 改 | `code-it/templates/RESULT.md` L138-153 字节级保留(沿用 NFR-4) |
| INV-5 | 11 个其他 `code-*` 技能 SKILL.md 核心工作流 0 改 | `code-require` / `code-design` / `code-fix` / `code-init` / `code-publish` / `code-version` / `code-rule` / `code-merge` / `code-answer` / `code-dashboard` / `code-check`(仅适配判定文件位置,不破坏既有结构) |
| INV-6 | 12 个项目级规范 0 改核心约束 | `./assistants/rules/*.md`(本需求仅消费规范,不修改) |
| INV-7 | 既有 15 个 REQ 的 `code/<TASK-...>/RESULT.md` + `plan/<需求>/PLAN.md` 0 改 | 历史档案 |
| INV-8 | 0 新增三方依赖 | NFR-3 锁定(只读 monorepo 声明文件,不引入新依赖) |

## 10. 边界与异常

- **E-1**(声明文件不存在):退化为 git diff 公共子目录(沿用 FR-1 优先级链)
- **E-2**(git diff 失败 / 非 git 仓库):退化为 CWD 根(原 REQ-00034 行为)
- **E-3**(变更路径跨越多个模块):多个模块分别写单测(沿用 FR-3 判定逻辑)
- **E-4**(模块目录无法访问 / 权限):跳过该模块,屏显警告(沿用既有降级范式)
- **E-5**(多模块通过但只有一个有变更):只给该模块写单测(沿用 FR-3 判定逻辑)
- **E-6**(多模块通过且多个有变更):每个模块分别写单测(沿用 FR-3 判定逻辑)
- **E-7**(单模块识别失败 / 理论不可能):退化为 CWD 根(原 REQ-00034 行为)
- **E-8**(历史 `code-unit` 行为已退场):沿用 REQ-00034 NFR-2(本需求不涉及)
- **E-9**(跨平台路径分隔符 Windows `\` / Unix `/`):沿用 `path.posix` 规范化(沿用既有约定)

## 11. 衔接

- **下游**:`code-plan` 消费本设计做实施计划(候选 3 任务;实际由 `code-plan` 阶段细化)
- **上游**:`code-require` 的 `RESULT.md`(本设计只读)
- **横向**:
  - 与 REQ-00034(`code-unit` 整合进 `code-it`,7 项守卫工程根级框架)协同 — 本需求在其基础上细化到模块粒度;100% 兼容 + 扩展
  - 与 REQ-00031(`code-unit` 退场为可选)协同 — 本需求不涉及 `code-unit` 退场逻辑(已由 REQ-00034 落地)
  - 与 REQ-00037(缺陷修复流程的状态推进)协同 — 本需求不涉及缺陷路径(沿用既有 `code-it` §缺陷分支 17-25)
  - 与 BUG-00001("不修改 SKILL.md")协同 — NFR-3 锁定(本需求仅消费既有 SKILL.md,不修改 frontmatter)

## 12. 变更记录

```
2026-06-22 13:30  设计新增  REQ-00038 概要设计完成(8 决策 / 8 不变量 / 1 主改造 + 1 模板改造 + 1 文档字面改写 / 0 新增模块 / 1 新增接口类 / 3 运行时数据 / 0 依赖);整体=--balanced,功能性=高(用户手动 1 问确认);0 触发扩展性问路(只读 monorepo 声明文件,不引入新依赖);0 冲突;候选 3 任务(由 code-plan 阶段细化)  REQ-00038
```