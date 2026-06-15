# 分析笔记 — REQ-00034

版本:V0.0.3
需求编码:REQ-00034
时间:2026-06-15 12:00

## 1. 需求本质判定

用户的输入是 1 段**技能合并 + 行为接管**声明:
- 删除 `code-unit` 技能(整体)
- 能力整合进 `code-it`
- 按需写单测(项目可测 + 任务性质 → 写;否则不写)
- 不适用工程 → 跳过(沿用原 `code-unit` 守卫 E-2)

**判定**:本需求是**技能合并 + 行为接管**(把独立技能 `code-unit` 删掉,职责由 `code-it` 接管),**非**新功能 / 新模块 / 跨版本需求。

## 2. 现状分析(隐含 vs 显式)

### 2.1 REQ-00031 的"分离" vs 本需求的"合并"

| 维度 | REQ-00031(已落地) | 本需求(待落地) |
| --- | --- | --- |
| `code-plan` 任务规划 | 不含"测试"类任务 | 沿用(不重做) |
| `code-it` 职责 | 编码 + 编译/运行(声明性"不含"单测) | 编码 + 编译/运行 + **含**单测(按需) |
| `code-unit` 职责 | 独立、可选(声明) | **退场** |
| `code-auto` 步骤 4.b | "恒等跳过"(屏幕日志冗余) | **删除**(不再调 `code-unit`,无"跳过"语义) |
| `code-unit` 技能本体 | 仍存在(635 行) | **删除** |
| `code-unit` 模板目录 | 仍存在 | **删除** |
| 任务"测试状态"字段 | `已运行-通过` / `不适用` 2 枚举 | 沿用(`code-it` 内部使用,不写 `code-unit` 步骤 14 的"测试状态推进"逻辑) |

### 2.2 候选改造方案权衡

#### 方案 1:**激进删除**(本需求锁定方案)
- **行为**:`code-unit` 整体删除(635 SKILL.md + 模板目录);`code-it` 接管"写单测 + 跑单测"职责;`code-auto` 删除步骤 4.b
- **优点**:
  - 技能数量从 12 减到 11
  - 职责单一化(用户原始输入的明确诉求)
  - `code-auto` 屏幕日志减少 1 行/任务(更清爽)
- **缺点**:
  - `code-it` SKILL.md 净增 ~200 行(守卫 + 按需写单测)
  - 5 个 SKILL.md + 2 JSON + 4 README + 7 项目级规范 + 11 技能描述段共 ~30 个文件需要改
- **风险**:
  - 跨 5 SKILL.md 改造,易引入回归
  - 既有 `code-unit` 文档结构需要审慎处理(模板目录删除是硬删除)
- **缓解**:
  - `code-it` 接管后,所有守卫 7 项 + 步骤 4 行为字节级保留(由 `code-it` 步骤 8.5 接管)
  - 历史档案 V0.0.2 / V0.0.3 全部 `test/` 目录 + `code-*/test-results.md` 字节级保留(NFR-2 沿用)

#### 方案 2:**保留 `code-unit` 仅做兼容壳**(拒)
- **行为**:`code-unit` 保留 SKILL.md 但内容改为"提示:已合并进 `code-it`"的占位
- **优点**:兼容旧用户路径(`/code-unit` 仍可调,只是行为变空)
- **缺点**:
  - 与用户原始输入"**移除**技能"字面冲突
  - 占位技能易引起混淆
  - 看板 / README / 文档清理更麻烦
- **判定**:拒

#### 方案 3:**改名而非删除**(拒)
- **行为**:`code-unit` 改名为 `code-test`,`code-it` 不接管
- **优点**:保持技能数量
- **缺点**:
  - 与用户"**移除**技能" + "**整合进** `code-it`"字面冲突
  - 只是换壳不解决根本问题
- **判定**:拒

**最终**:方案 1(激进删除 + `code-it` 接管)。

## 3. 改造点候选

| 类别 | 改造范围 | 行数预估 |
| --- | --- | --- |
| 硬删除 | `code-unit/SKILL.md` (635) + `code-unit/templates/` (整体) | -635 ~ -700 行 |
| `code-it` 接管 | `code-it/SKILL.md` 净增守卫 7 项 + 按需写单测步骤 + 模板新增"## 单元测试"小节 | +150 ~ +250 行 |
| `code-plan` 微调 | 测试状态字段语义收窄为"`code-it` 内化"(L368 / L431 / L445 / L454 / L1105) | -10 ~ -20 行(原"由 code-unit 另起流程"改写为"由 code-it 内化") |
| `code-auto` 删除 | 步骤 4.b 整段 + 子技能调用表 4 行 + 衔接/不要做的事段 | -50 ~ -80 行 |
| `code-check` 微调 | `test/<任务编码>/` 引用全部改写为"`code-it` 自含的 `test-results.md`" | -10 ~ -20 行 |
| 2 JSON 文件 | plugin.json + marketplace.json keyword + skills 列表 | -2 行(精确) |
| 4 README + CLAUDE.md | 描述段去 `code-unit` 引用 | -10 ~ -30 行 |
| 7 项目级规范 | encoding-conventions + review-checklist 等去 `code-unit` 引用 | -5 ~ -15 行 |
| 11 技能描述段 | 11 SKILL.md frontmatter description 去 `code-unit` 引用 | -10 ~ -30 行 |
| **净变化** | | **约 -600 ~ -800 行**(技能合并) |

## 4. 候选 `code-it` 接管措辞

### 4.1 守卫接管(`code-it` 步骤 8.5 之前新增"## 步骤 8a — 项目可测性守卫")

候选措辞 1(完全沿用):
> 本步骤是 `code-it` 在"## 步骤 9-12 编译/运行"**之前**的**守卫**。沿用 `code-unit` 步骤 0a 既有 7 项检查(`package.json` 含 `scripts.test` / `pyproject.toml` 含测试配置 / `Cargo.toml` / `go.mod` / `pom.xml` / `build.gradle` / `test/` 目录)。
> - 命中任一 → testable = True → 进入"步骤 9"按需写单测
> - 全部不命中 → testable = False → 跳过单测,任务"测试状态"列 = `不适用`,屏幕输出"⏭ code-it 跳过单测(项目不可测)"

**锁定措辞 1**(字节级沿用 `code-unit` 步骤 0a)

### 4.2 按需写单测(`code-it` 步骤 8.5 新增)

候选措辞 1(自动判定):
> 本步骤在守卫通过(testable = True)时执行:
> - 任务涉及"纯函数 / 工具方法 / 业务逻辑"→ **写**单测
> - 任务涉及"配置 / 类型定义 / 文档"→ **不**写单测
> - 任务涉及"重构(无行为变更)" → 沿用既有单测 + 跑通
> 产出物:`code/<任务编码>/unit-test-results.md`(新模板,见下)

候选措辞 2(用户选):
> 守卫通过 → 屏幕输出"项目可测,是否需要写单测?(Y/N)",用户选 Y → 写;选 N → 跳过

**锁定措辞 1**(自动判定,Q-4 隐含答复 C)

## 5. 风险与权衡

### 5.1 风险

| 风险 | 等级 | 缓解 |
| --- | --- | --- |
| `code-it` 接管后,守卫 7 项检查与原 `code-unit` 步骤 0a 行为不一致 | 中 | 字节级沿用原 7 项检查 |
| `code-it` 净增 ~200 行,可能突破单 SKILL.md 加载阈值 | 低 | 沿用既有 SKILL.md 加载策略;`code-it` 当前 938 行,加 200 后 ~1138,仍在范围内 |
| 既有 11 个 REQ 的 `code/<TASK-...>/test-results.md` 是否受影响 | **无** | NFR-2 沿用,字节级保留 |
| V0.0.2 历史 `code/<TASK-...>/test-results.md` 是 `code-it` 既有产出还是 `code-unit` 产出? | 低 | 经 Grep 确认:**由 `code-it` 步骤 10 步骤 11 产出**(`code-unit` 步骤 10 / 11 也产 `test-results.md`);`code-it` 接管后路径不变 |
| `code-auto` 步骤 7 输出报告"单元测试(code-unit):N2 次"如何处理 | 中 | 字段**改写**为"单元测试(由 `code-it` 内化):N2 次" |
| 历史 `auto-report.md` 中"code-unit"日志字节级保留? | 低 | 字节级保留(NFR-2 沿用);**不**追溯重写 |

### 5.2 与既有规范的协同

- **`skill-conventions.md`**:SKILL.md frontmatter L1-3 字节级保留(INV-1) — 本需求 5 SKILL.md 改造**仍**保留 frontmatter
- **`module-conventions.md`**:资源文件放 templates/ 子目录 — 本需求**删除** `code-unit/templates/` 目录
- **`commit-conventions.md`**:`chore(<skill>):` 前缀(INV-3) — 本需求 commit message 候选 1:`chore(code-unit): REQ-00034 移除 code-unit 技能`(虽然 `code-unit` 退场,commit 仍按被删除技能命名);候选 2:`chore(code-it): REQ-00034 接管 code-unit`(按接管方命名)
- **`dashboard-conventions.md`**:看板字段三方同步 — 本需求触发 1 次(`V0.0.3/RESULT.md` §"需求清单" + §"变更记录" 同步)
- **`plugin-conventions.md`**:plugin.json / marketplace.json 同步 — 本需求触发 1 次(2 JSON 文件 keyword + skills 列表)

### 5.3 后续 follow-up(本需求不实现)

- 候选 follow-up 1:把 `code-it` 拆成 `code-it-coder` + `code-it-tester` 两个内部子步骤
  - 本需求**不**实现(用户原始输入是"整合进 `code-it`",不拆)
- 候选 follow-up 2:在 `code-it/templates/RESULT.md` 新增"## 单元测试"小节
  - 本需求**包含**此 follow-up(FR-4 锁定)
- 候选 follow-up 3:在 `code-check/checklists/review-checklist.md` §8.7 测试质量维度**收窄**为"`code-it` 内化"语义
  - 本需求**包含**此 follow-up(FR-5 锁定)
- 候选 follow-up 4:在 `code-rule` 沉淀 `testing-conventions.md`(单测规范)
  - 本需求**不**实现(避免越界 `code-rule` 改造);留作后续

## 6. 候选任务拆分(本需求下游 `code-plan` 候选)

| 候选任务 | 涉及文件 | 行数变化 | 备注 |
| --- | --- | --- | --- |
| T-001:`code-unit` 硬删除 | `code-unit/SKILL.md` + `code-unit/templates/` | -635 ~ -700 | `rm -rf` 风格 |
| T-002:`code-it` 接管守卫 7 项 | `code-it/SKILL.md` 步骤 8a 新增 | +50 ~ +80 | 字节级沿用 `code-unit` 步骤 0a |
| T-003:`code-it` 接管按需写单测 | `code-it/SKILL.md` 步骤 8.5 新增 | +80 ~ +120 | 新增"## 单元测试"小节 |
| T-004:`code-it` 文档头 + 描述段去 `code-unit` 引用 | `code-it/SKILL.md` 文档头 + L14 + L18 | -3 ~ -5 | 反向声明改写 |
| T-005:`code-plan` 测试状态字段语义改写 | `code-plan/SKILL.md` L368/431/445/454/1105 | -10 ~ -20 | "由 `code-unit` 另起流程" → "由 `code-it` 内化" |
| T-006:`code-auto` 步骤 4.b 删除 | `code-auto/SKILL.md` L388-411 + 衔接 + 不要做的事 | -50 ~ -80 | 整段删除 |
| T-007:`code-auto` 子技能调用表减 4 行 | `code-auto/SKILL.md` L213-227 + L432-433 | -10 | 删 `code-unit` 4 行 |
| T-008:`code-check` `test/<TASK-...>/` 引用收窄 | `code-check/SKILL.md` L3/21/40-41/56/72/96/151/281/608/615 | -10 ~ -20 | 改写为"`code-it` 自含" |
| T-009:plugin.json + marketplace.json 注册项删除 | 2 JSON 文件 | -2 ~ -3 行 | 减 keyword + skills |
| T-010:11 技能 SKILL.md 描述段去 `code-unit` 引用 | 11 SKILL.md frontmatter description | -10 ~ -30 | 字节级保留 description 字段名 + 顺序,只改字面 |
| T-011:4 README + CLAUDE.md 去 `code-unit` 引用 | 4 README + CLAUDE.md | -10 ~ -30 | 描述段去 `code-unit` |
| T-012:7 项目级规范去 `code-unit` 引用 | `assistants/rules/*.md` | -5 ~ -15 | 字面替换 |
| T-013:看板同步 | `V0.0.3/RESULT.md` §需求清单 + §变更记录 | +1 + +1 | 1 项任务"更新看板" |
| T-014:`code-it` 模板新增"## 单元测试"小节 | `code-it/templates/RESULT.md` | +20 ~ +40 | 新增小节 |
| **总计** | | **约 -600 ~ -800 行** | |

**说明**:本需求下游 `code-plan` 阶段**不**强制按上表拆分,本表只是候选;实际拆分由 `code-design` 决定(按"既改 1 个文件 = 1 任务"原则)。
