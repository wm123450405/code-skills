# 概要设计 — 优化 /code-require 登记结束后报告(输出下一步建议)

- 需求编码:REQ-00032
- 所属版本:V0.0.3
- 文档创建时间:2026-06-12 16:15
- 最近更新:2026-06-12 16:32
- 文档状态:已完成
- 上游:`./assistants/V0.0.3/require/REQ-00032/RESULT.md`
- 遵循规范:`./assistants/rules/` 下 7 个核心规范文件(全沿用)
- 涉及技能:`code-require`(本需求唯一改造对象)

## 设计目标

整体设计目标 = `--minimal`(用户在小需求阶段锁定;元技能文字修订适用)
维度优先级:
  功能性:中

## 1. 设计概述

本概要设计回答"系统长什么样"——为 `code-require` 技能在登记结束后输出"下一步建议"给出**最小化改造方案**:

- **改造对象**:`plugins/code-skills/skills/code-require/SKILL.md`
- **改造范围**:步骤 10A(首次分析)/ 步骤 10B(增量更新) 段内文末各追加 1 段"### 下一步建议(本需求 REQ-00032 新增,2026-06-12 起生效)"
- **改造语义**:AI 在 code-require 步骤 10A / 10B 末尾,根据本轮需求材料数 + FR 数 + AC 数综合判定 `isTiny: boolean`,并按 FR-3.1 / FR-3.2 屏幕输出 1 组(2 行)"下一步建议"
- **零文档变更**:`require/<REQ>/RESULT.md` **不**追加"## 下一步建议"章节;`isTiny` 是内存变量,**不**持久化
- **零规范变更**:`code-require/templates/requirements.md` **不**修改;其他 9 个 `code-*` 技能 SKILL.md 0 改;7 个项目级规范 0 改

## 2. 上游引用

- **需求**:`./assistants/V0.0.3/require/REQ-00032/RESULT.md`
  - FR-1:AI 自主判定需求粒度
  - FR-2:不修改 RESULT.md 文档结构
  - FR-3:屏幕日志输出"下一步建议"
  - FR-4:不修改其他 8 个 code-* 技能 SKILL.md
  - NFR-1~NFR-9:零文档变更 / 零规范变更 / 字符数契约 / 幂等性 / 0 新增依赖 / INV 字节级保留 / 标题解析不涉及 / 与 REQ-00031 协同 / 与 code-dashboard 差异
  - AC-1~AC-4:18 条验收标准

## 3. 模块拆分

### 3.1 总体说明

本设计**只改造 1 个文件**:`plugins/code-skills/skills/code-require/SKILL.md`。

不新增模块,不修改模块边界,不修改目录结构。

### 3.2 模块清单

| # | 模块名 | 路径 | 状态 | 职责 | 关键决策 |
| --- | --- | --- | --- | --- | --- |
| 1 | code-require 屏幕日志建议段(步骤 10A 内) | `code-require/SKILL.md` > 步骤 10A 段内文末 | **修改既有** | 首次分析完成后输出"下一步建议" | D-2 段内文末追加 |
| 2 | code-require 屏幕日志建议段(步骤 10B 内) | `code-require/SKILL.md` > 步骤 10B 段内文末 | **修改既有** | 增量更新完成后输出"下一步建议" | D-2 段内文末追加 |

### 3.3 不修改的模块(INV 字节级保留)

- 既有 9 个 `code-*` 技能 SKILL.md(INV-4)
- `code-require/templates/requirements.md`(NFR-2)
- `code-require/SKILL.md` frontmatter L1-3(INV-1)
- 7 个项目级规范(INV-5)
- 既有 12 个 REQ 的 RESULT.md(INV-7)
- 4 个 README/marketplace/plugin/CLAUDE(INV-6)

## 4. 接口

### 4.1 屏幕日志输出接口(运行期)

| 接口 | 触发位置 | 入参 | 出参 | 错误码 |
| --- | --- | --- | --- | --- |
| 屏幕日志"→ 下一步建议:微小路径" | 步骤 10A / 10B 末尾,`isTiny = true` | 无(无参) | 2 行字符串 | 不适用(无异常) |
| 屏幕日志"→ 下一步建议:其他路径" | 步骤 10A / 10B 末尾,`isTiny = false` | 无(无参) | 2 行字符串 | 不适用 |

### 4.2 屏幕日志格式契约(NFR-3 字符数约束)

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

字符数:每条建议 ≤ 2 行,每行 ≤ 80 字(中点 `→` 起首,中文标点)

### 4.3 内部变量(非文档字段)

| 变量 | 类型 | 作用域 | 来源 | 备注 |
| --- | --- | --- | --- | --- |
| `isTiny` | `boolean` | 内存(本技能本轮) | AI 自主判定(FR-1) | **不**持久化到 `RESULT.md` |

## 5. 数据结构

本需求**不新增**任何数据结构(无实体 / 字段 / 表)。`isTiny` 是运行时内存变量,不参与任何持久化。

## 6. 算法与逻辑

### 6.1 微小需求判定算法(FR-1)

```
function determineIsTiny(materials, frs, acs):
  # 推荐判据(同时满足 → 微小)
  if materials.length <= 1 && frs.length <= 2 && acs.length <= 5:
    return true
  # FR 数 ≥ 3 或 AC 数 ≥ 6 → 非微小
  if frs.length >= 3:
    return false
  if acs.length >= 6:
    return false
  # AI 综合判断(本判据中无法量化)
  return AI 综合判断结果  # 不强制,允许 AI 基于上下文调整
```

### 6.2 失败降级

```
function determineIsTinySafe(materials, frs, acs):
  try:
    return determineIsTiny(materials, frs, acs)
  catch:
    return false  # E-5 退化:走 /code-design 建议
```

### 6.3 屏幕输出算法(FR-3)

```
function outputNextStepSuggestion(isTiny):
  if isTiny:
    log("→ 下一步建议:本需求判定为\"微小需求\",建议直接执行 `/code-auto` 完成开发任务")
    log("  提示:code-auto 会自动跳过独立的概设/详设步骤,直接进入编码+评审流水线")
  else:
    log("→ 下一步建议:本需求判定为\"非微小需求\",建议先执行 `/code-design` 概设")
    log("  提示:概设完成后,code-plan → code-it → code-check 仍按既有主流程推进")
```

## 7. 流程图

### 7.1 屏幕输出时序(步骤 10A / 10B 末尾)

```
[code-require 步骤 10A / 10B 既有"向用户汇报"段]
  ↓
[本需求新增]AI 判定 isTiny
  ├→ isTiny=true  → 输出 FR-3.1 建议
  └→ isTiny=false → 输出 FR-3.2 建议
  ↓
[完成]
```

### 7.2 微小需求判定状态机

```
[材料收集] → [材料数+FR+AC 综合评估] → {isTiny=true} → 输出 /code-auto 建议
                                          ↓
                                       {isTiny=false} → 输出 /code-design 建议
                                          ↓
                                       {判定失败} → 退化 isTiny=false → /code-design
```

## 8. 异常处理

| 异常 | 处理 |
| --- | --- |
| E-1 材料数为 0 | `isTiny = false` → 走 `/code-design` 建议 |
| E-2 FR 数为 0 | 沿用 code-require 既有"中止"逻辑(本需求不介入) |
| E-3 code-require 重入 | `isTiny` 不累积(沿用 NFR-4) |
| E-4 增量更新(步骤 5B) | 同样触发 FR-1 判定,输出 FR-3 建议 |
| E-5 判定失败 | `isTiny = false` 退化 |
| E-6 用户在建议前中断 | 屏幕日志建议不输出(沿用既有"中止"逻辑) |
| E-7 本仓库无项目级规范 | 沿用 code-require 既有 AskUserQuestion(本需求不介入) |

## 9. 安全要求

不适用(本需求无安全敏感操作)。

## 10. 性能与资源

- **总耗时**:< 1ms(纯字符串拼接)
- **内存**:+2 行字符串(单次输出)
- **文件大小**:`code-require/SKILL.md` +12 行(2 段各约 6 行)
- **副作用**:0(无网络 / 无 IO / 无跨技能调用)

## 11. 性能监控指标

不适用(本需求无监控需求)。

## 12. 测试要点

- **AC-1.x**(微小判定):覆盖 4 条(0/满足推荐判据/FR≥3/AC≥6)
- **AC-2.x**(屏幕日志):覆盖 5 条(2 路径各 1 + 二选一 + 不修改 RESULT.md + 不用指代词)
- **AC-3.x**(零变更):覆盖 6 条(INV-1~INV-4 / INV-5 / INV-6 / INV-7)
- **AC-4.x**(与既有规则协同):覆盖 4 条(沿用 REQ-00031 / 不收集单测偏好 / 不改模板 / 不增字段)

测试方法:**手工目检** + **git diff 校验**(因本仓库无测试框架,沿用 REQ-00031 NFR-2)。

## 13. 规范遵循

### 13.1 规范摘要

| 规范 | 类别 | 与本设计关联 |
| --- | --- | --- |
| skill-conventions.md | 技能 | INV-1 字节级保留 frontmatter |
| commit-conventions.md | 提交 | INV-3 `chore(<skill>):` 前缀 |
| dashboard-conventions.md | 看板 | 沿用看板字段约定;本需求不修改 |
| naming-conventions.md | 命名 | 沿用 kebab-case;本需求不新增命名 |
| encoding-conventions.md | 编码 | 沿用 5 位纯数字;本需求不涉及编号生成 |
| module-conventions.md | 模块 | 沿用目录结构;本需求不新增模块 |
| doc-conventions.md | 文档 | 不直接相关 |

### 13.2 INV 字节级保留校验(本设计)

- **INV-1**:`code-require/SKILL.md` frontmatter L1-3 字节级保留 ✅
- **INV-2**:`code-require/SKILL.md` 既有"## 工作流程"小节 0 改 ✅
- **INV-3**:`chore(<skill>):` 前缀沿用 ✅
- **INV-4**:既有 9 个 `code-*` 技能 SKILL.md 0 改 ✅
- **INV-5**:既有 7 个项目级规范 0 改 ✅
- **INV-6**:4 个 README/marketplace/plugin/CLAUDE 0 改 ✅
- **INV-7**:既有 12 个 REQ 的 RESULT.md 0 改 ✅
- **INV-8**:0 新增三方依赖 ✅
- **INV-9**:看板字段三方同步 0 触发 ✅
- **INV-10**(本需求新增):屏幕日志格式字节级保留(字符数 ≤ 80 字 / 行数 ≤ 2 行 / 路径串字节级)✅

### 13.3 偏离

无。本设计**0**规范偏离。

## 14. 关键变更

| 文件 | 锚点 | 变更类型 | 变更描述 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-require/SKILL.md` | 步骤 10A 段内文末(329 行后) | **纯追加** | 新增 1 段"### 下一步建议(本需求 REQ-00032 新增,2026-06-12 起生效)" |
| `plugins/code-skills/skills/code-require/SKILL.md` | 步骤 10B 段内文末(409 行后) | **纯追加** | 新增 1 段"### 下一步建议(本需求 REQ-00032 新增,2026-06-12 起生效)" |
| `plugins/code-skills/skills/code-require/SKILL.md` | 步骤 N(末尾兜底提交,331-401 行) | **不修改** | 职责分离:步骤 N 是 commit 流程,不是用户汇报流程 |
| `plugins/code-skills/skills/code-require/SKILL.md` | 其他步骤(0a / 0b / 0b.0 / 1-9 / 步骤 0) | **不修改** | INV-2 字节级保留 |

## 15. 关键决策(本设计阶段)

| 决策 | 内容 | 依据 |
| --- | --- | --- |
| **D-1** | 改造文件:`code-require/SKILL.md` | Q1 选定 A;屏幕日志建议是步骤说明的一部分 |
| **D-2** | 改造位置:步骤 10A / 10B 段内文末各追加 1 段 | Q2 选定 A;最小化变更,字节级保留既有"向用户汇报"段 |
| **D-3** | isTiny 判定位置:步骤 10A / 10B 末尾(与建议输出合并) | Q3 选定 B;判定与使用同处,降低跨步骤变量传递风险 |
| **D-4** | 屏幕日志编号:`→ 下一步建议:` 起首 | Q4 选定 A;沿用既有风格 |
| **D-5** | isTiny 不持久化 | Q5 选定 B;FR-2 锁定;用户 Q-2 锁定 |
| **D-6** | 建议仅 2 条(微小 / 其他) | 用户 Q-3 锁定 A |
| **D-7** | 不联动 /code-unit | 用户 Q-4 锁定 A;沿用 REQ-00031 |
| **D-8** | 整体设计目标 `--minimal` + 功能性=中 | 用户在 code-design 步骤 0b 锁定;元技能文字修订适用 |

## 16. 待澄清 / 未决项

无新增。本需求的需求阶段 4 项 follow-up(留作后续)沿用:
- Q-1:加 /code-rule 等更多建议类型(留作 follow-up)
- Q-2:追加"## 下一步建议"到 RESULT.md(留作 follow-up)
- Q-3:isTiny 持久化(留作 follow-up)
- Q-4:`code-dashboard` 5 类优先级是否套用(留作 follow-up)

## 17. 变更记录

```
2026-06-12 16:32  设计新增  REQ-00032 概要设计完成(7 模块 + 0 接口 + 0 数据结构 + 0 三方依赖 + 10 INV),整体=--minimal + 功能性=中(元技能文字修订适用);0 触发 §规则 1 三同步;0 派生"更新看板"任务;0 用户授权偏离  REQ-00032
```
