## 设计目标

整体设计目标 = `--minimal`(从 `design/REQ-00032/RESULT.md` 沿用,本需求不重复询问)
维度优先级:
  功能性:中

> 沿用 design 阶段:本需求是元技能文字修订,沿用 `--minimal` 避免过度拆分;按"## 设计目标"小节调整任务粒度,合并同类(只 1 个改造对象,无需多任务拆分)。

---

# 详细设计 — 优化 /code-require 登记结束后报告(输出下一步建议)

- 需求编码:REQ-00032
- 所属版本:V0.0.3
- 文档创建时间:2026-06-12 16:35
- 最近更新:2026-06-12 16:35
- 文档状态:已完成
- 上游:
  - 需求:`./assistants/V0.0.3/require/REQ-00032/RESULT.md`
  - 概设:`./assistants/V0.0.3/design/REQ-00032/RESULT.md`
- 遵循规范:`./assistants/rules/` 下 7 个核心规范文件(全沿用)
- 涉及技能:`code-require`(本需求唯一改造对象)
- 任务总数:1(单任务,沿用 `--minimal` 粒度粗化;P-D3 锁定:同文件同字段合并)

## 1. 概述

本详细设计把 `design/REQ-00032/RESULT.md` 的 2 个模块(步骤 10A / 10B 末尾追加"### 下一步建议"段)落地为 1 个**单任务**(`TASK-REQ-00032-00001`),实施时按"功能点 1" 整体完成:

- **任务**:`[修改] code-require 步骤 10A/10B 末尾追加下一步建议段`
- **触发/来源**:详细设计
- **类型**:修改
- **完成定义**:`code-require/SKILL.md` 步骤 10A / 10B 段内文末各追加 1 段"### 下一步建议(本需求 REQ-00032 新增,2026-06-12 起生效)",屏幕输出 2 类建议(微小/其他 二选一),并通过手工目检 18 AC(详 §11)。

## 2. 上游引用

- **需求**:`./assistants/V0.0.3/require/REQ-00032/RESULT.md`
  - FR-1:AI 自主判定需求粒度
  - FR-2:不修改 RESULT.md 文档结构
  - FR-3:屏幕日志输出"下一步建议"
  - FR-4:不修改其他 8 个 code-* 技能 SKILL.md
  - NFR-1~NFR-9(9 条)
  - AC-1~AC-4(18 条)
- **概设**:`./assistants/V0.0.3/design/REQ-00032/RESULT.md`
  - D-1:改造文件 `code-require/SKILL.md`
  - D-2:改造位置 步骤 10A / 10B 段内文末
  - D-3:isTiny 判定位置 步骤 10A / 10B 末尾
  - D-4:屏幕日志编号 `→ 下一步建议:` 起首
  - D-5:isTiny 不持久化
  - D-6:建议仅 2 条
  - D-7:不联动 /code-unit
  - D-8:`--minimal` + 功能性=中

## 3. 模块详细化

> 详细化内容见 `module-details.md`(本文件 §3 给出主索引)

### 3.1 模块 1:code-require 屏幕日志建议段(步骤 10A 内)

- **路径**:`plugins/code-skills/skills/code-require/SKILL.md` > §步骤 10A 段内文末
- **状态**:修改既有(纯追加,字节级保留既有"向用户汇报"段)
- **职责**:在 code-require 首次分析完成后,屏幕输出"下一步建议"
- **关键决策**:D-2(段内文末追加,不引入新步骤编号)
- **详细化**:见 `module-details.md §模块 1`

### 3.2 模块 2:code-require 屏幕日志建议段(步骤 10B 内)

- **路径**:`plugins/code-skills/skills/code-require/SKILL.md` > §步骤 10B 段内文末
- **状态**:修改既有(纯追加,字节级保留既有"向用户汇报"段)
- **职责**:在 code-require 增量更新完成后,屏幕输出"下一步建议"
- **关键决策**:D-2(段内文末追加,不引入新步骤编号)
- **详细化**:见 `module-details.md §模块 2`

## 4. 算法与逻辑

> 详细算法见 `module-details.md §算法 1 / §算法 2`(本节给出主索引)

### 4.1 isTiny 判定算法(FR-1)

详见 `module-details.md §算法 1 determineIsTiny`。要点:

- 输入:materials 数组、frs 数组、acs 数组
- 输出:`boolean`
- 推荐判据(同时满足 → true):materials.length ≤ 1 && frs.length ≤ 2 && acs.length ≤ 5
- 强制排除:frs.length ≥ 3 → false;acs.length ≥ 6 → false
- AI 综合判断:本判据中无法量化的部分(如"明显跨多个模块"),由 AI 决定
- 失败降级:异常 → false(走 /code-design 建议)

### 4.2 屏幕输出算法(FR-3)

详见 `module-details.md §算法 2 outputNextStepSuggestion`。要点:

- 输入:`isTiny: boolean`
- 输出:屏幕日志 2 行
- 二选一:`isTiny=true` → FR-3.1 模板;`isTiny=false` → FR-3.2 模板
- 字符数:每行 ≤ 80 字,中点 `→` 起首

## 5. 数据结构完整变更

**不新增**任何数据结构;**不修改**任何既有数据结构。

| 操作 | 实体 | 变更 |
| --- | --- | --- |
| 新增 | (无) | — |
| 修改 | (无) | — |
| 删除 | (无) | — |

详细说明见 `data-changes.md`(空文档,声明本需求 0 数据变更)。

## 6. 接口细节

> 完整接口规格见 `interface-specs.md`(本节给出主索引)

### 6.1 屏幕日志输出接口(运行期,无 I/O 语义)

| 接口 | 触发位置 | 入参 | 出参 | 错误码 |
| --- | --- | --- | --- | --- |
| 屏幕日志"→ 下一步建议:微小路径" | 步骤 10A / 10B 末尾,`isTiny=true` | 无 | 2 行字符串 | 不适用 |
| 屏幕日志"→ 下一步建议:其他路径" | 步骤 10A / 10B 末尾,`isTiny=false` | 无 | 2 行字符串 | 不适用 |

### 6.2 屏幕日志格式契约(NFR-3 字符数约束)

**FR-3.1**(微小路径):
```
→ 下一步建议:本需求判定为"微小需求",建议直接执行 `/code-auto` 完成开发任务
  提示:code-auto 会自动跳过独立的概设/详设步骤,直接进入编码+评审流水线
```

**FR-3.2**(其他路径):
```
→ 下一步建议:本需求判定为"非微小需求",建议先执行 `/code-design` 概设
  提示:概设完成后,code-plan → code-it → code-check 仍按既有主流程推进
```

字符数校验:第 1 行 = 45 字 / 第 2 行 = 36 字(中文标点+路径串字节级保留)

### 6.3 内部变量(非文档字段,非公开 API)

| 变量 | 类型 | 作用域 | 来源 | 备注 |
| --- | --- | --- | --- | --- |
| `isTiny` | `boolean` | 内存(本技能本轮) | AI 自主判定 | **不**持久化 |

## 7. 异常处理

| 异常 | 处理 | 失败降级 |
| --- | --- | --- |
| 材料数为 0 | `isTiny = false` | 走 /code-design 建议 |
| FR 数为 0 | 沿用 code-require 既有"中止"逻辑(本需求不介入) | — |
| 增量更新(步骤 5B) | 同样触发 FR-1 判定,输出 FR-3 建议 | 沿用 |
| 判定失败 | `isTiny = false` 退化 | 走 /code-design 建议 |
| 用户在建议前中断 | 屏幕日志建议不输出(沿用既有"中止"逻辑) | — |
| 本仓库无项目级规范 | 沿用 code-require 既有 AskUserQuestion(本需求不介入) | — |

详细异常处理见 `risk-analysis.md §异常处理`。

## 8. 安全要求

不适用(本需求无安全敏感操作):
- 无网络 I/O
- 无文件写入
- 无跨技能调用
- 无用户输入处理(屏幕输出是单向)
- 无敏感数据处理

## 9. 状态机 / 流程

### 9.1 屏幕输出时序(步骤 10A / 10B 末尾)

```
[code-require 步骤 10A / 10B 既有"向用户汇报"段]
  ↓
[本需求新增]AI 判定 isTiny
  ├→ isTiny=true  → 输出 FR-3.1 建议
  └→ isTiny=false → 输出 FR-3.2 建议
  ↓
[完成]
```

### 9.2 微小需求判定状态机

```
[材料收集] → [材料数+FR+AC 综合评估] → {isTiny=true} → 输出 /code-auto 建议
                                          ↓
                                       {isTiny=false} → 输出 /code-design 建议
                                          ↓
                                       {判定失败} → 退化 isTiny=false → /code-design
```

## 10. 性能与资源

- **总耗时**:< 1ms(纯字符串拼接 + 内存变量判定)
- **内存**:+2 行字符串(单次输出)
- **文件大小**:`code-require/SKILL.md` +12 行(2 段各约 6 行)
- **副作用**:0
- **网络/磁盘 I/O**:0

监控指标:不适用(本需求无监控需求)。

## 11. 测试要点

> 完整测试要点见 `risk-analysis.md §测试要点`(本节给出主索引)

### 11.1 单元测试范围

不适用(本仓库无测试框架,沿用 REQ-00031 NFR-2)。

### 11.2 手工目检范围(本需求实际测试方法)

- **AC-1.x**(微小判定):4 条(0/满足推荐判据/FR≥3/AC≥6)
- **AC-2.x**(屏幕日志):5 条(2 路径各 1 + 二选一 + 不修改 RESULT.md + 不用指代词)
- **AC-3.x**(零变更):6 条(INV-1~INV-4 / INV-5 / INV-6 / INV-7)
- **AC-4.x**(与既有规则协同):4 条

合计 19 条目检项;每条 1 次手工目检 = < 5 分钟。

### 11.3 集成测试范围

不适用(本需求是 1 个单文件文字追加,无跨模块集成)。

### 11.4 端到端测试范围

不适用(本需求无端到端流程)。

### 11.5 性能/安全测试

不适用(无性能 / 安全考量)。

## 12. 规范遵循

### 12.1 规范摘要

| 规范 | 类别 | 关键约束 | 与本设计关联 |
| --- | --- | --- | --- |
| skill-conventions.md | 技能 | frontmatter L1-3 字节级保留 | INV-1 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀 | INV-3 |
| module-conventions.md | 模块 | 资源放 templates/ | 沿用 |
| dashboard-conventions.md | 看板 | 字段三方同步 | 沿用 |
| encoding-conventions.md | 编码 | 5 位纯数字 | 沿用 |
| naming-conventions.md | 命名 | kebab-case | 沿用 |
| doc-conventions.md | 文档 | README 中英版对仗 | 不直接相关 |

### 12.2 INV 字节级保留校验(本设计)

- **INV-1**:`code-require/SKILL.md` frontmatter L1-3 字节级保留 ✅
- **INV-2**:`code-require/SKILL.md` 既有"## 工作流程"小节 0 改 ✅
- **INV-3**:`chore(<skill>):` 前缀沿用 ✅
- **INV-4**:既有 9 个 `code-*` 技能 SKILL.md 0 改 ✅
- **INV-5**:既有 7 个项目级规范 0 改 ✅
- **INV-6**:4 个 README/marketplace/plugin/CLAUDE 0 改 ✅
- **INV-7**:既有 12 个 REQ 的 RESULT.md 0 改 ✅
- **INV-8**:0 新增三方依赖 ✅
- **INV-9**:看板字段三方同步 0 触发 ✅
- **INV-10**(本需求新增):屏幕日志格式字节级保留 ✅

### 12.3 偏离

无。本设计**0**规范偏离。

## 13. 关联

| 需求 | 关联点 | 影响 |
| --- | --- | --- |
| REQ-00013 | 屏显格式契约(中点 `·`、≤ 30 字) | 沿用 |
| REQ-00023 | code-dashboard 5 类优先级 + 后续操作建议 | 借鉴风格(本需求简化为 2 条) |
| REQ-00026 | 技能描述通用化 | 沿用(本需求不修改 description) |
| REQ-00029 | 屏显精简 | 借鉴"屏显精简"思路 |
| REQ-00030 | 概设/详设职责分离 + 12 维度评审 | 沿用 INV 校验 |
| REQ-00031 | 元技能改路径(本需求同构) | 沿用"步骤末尾追加"模式 |
| REQ-00007 | code-auto 整版本流水线 | 本需求"微小→/code-auto"路径依赖 code-auto 既有功能 |

## 14. 待澄清 / 未决项

无新增(沿用需求阶段 4 项 follow-up):
- Q-1:加 /code-rule 等更多建议类型(留作 follow-up)
- Q-2:追加"## 下一步建议"到 RESULT.md(留作 follow-up)
- Q-3:isTiny 持久化(留作 follow-up)
- Q-4:`code-dashboard` 5 类优先级是否套用(留作 follow-up)

## 15. 变更记录

```
2026-06-12 16:35  设计新增  REQ-00032 详细设计完成(2 模块 + 0 接口 + 0 数据结构 + 0 三方依赖 + 10 INV),整体=--minimal + 功能性=中(沿用 design);1 个单任务(沿用 --minimal 粒度粗化);0 派生"更新看板"任务;0 用户授权偏离  REQ-00032
```
