# 模块拆分 — REQ-00019
更新时间:2026-06-06 15:00
版本:V0.0.2

## 模块总览

| 模块名 | 路径 | 状态 | 职责 | 对外接口 | 依赖 |
| --- | --- | --- | --- | --- | --- |
| `code-plan/步骤 19-28A+1` | `plugins/code-skills/skills/code-plan/SKILL.md` L588-735 | **修改既有** | BUG 路径产出 9 份文档 + 同步看板 2 区段 | §RESULT.md §5 接口 1 | 0 依赖新增 |
| `code-plan/templates/plan.md` | `plugins/code-skills/skills/code-plan/templates/plan.md` | **复用既有** | 14 章节详细设计模板 | — | — |
| `code-plan/templates/task-plan.md` | `plugins/code-skills/skills/code-plan/templates/task-plan.md` | **复用既有** | 8 章节任务计划模板 | — | — |
| `code-plan/templates/fix-plan.md` | `plugins/code-skills/skills/code-plan/templates/fix-plan.md` | **复用既有**(留作历史) | 旧 BUG 路径模板 | — | — |
| `code-it/步骤 17-25` | `plugins/code-skills/skills/code-it/SKILL.md` L638-800 | **修改既有** | BUG 路径消费 9 份文档 | §RESULT.md §5 接口 2-3 | 0 依赖新增 |
| `code-it/步骤 0b.0` | `plugins/code-skills/skills/code-it/SKILL.md` §"code-auto 上下文检测" | **复用既有**(沿用 BUG-00001) | 步骤 0b 触发前 `code-auto` 上下文检测 | — | — |
| `code-fix/SKILL.md` | `plugins/code-skills/skills/code-fix/SKILL.md` | **不修改**(FR-8 强约束) | BUG 登记 | §RESULT.md §5 接口 4 | — |
| `V0.0.2/RESULT.md` "任务清单"区段 | `assistants/V0.0.2/RESULT.md` | **修改既有** | 接收 BUG 任务行追加 | — | — |

## 新增模块

无(本需求 0 新增模块;沿用既有 `code-plan` / `code-it` / `code-fix` / `code-review` / `code-dashboard` 5 个技能)。

## 复用既有模块

### 模块:`code-plan/templates/plan.md`
- **复用方式**:直接作为 BUG 路径的 `RESULT.md` 模板(沿用 REQ 路径的 14 章节结构)
- **引用位置**:`plugins/code-skills/skills/code-plan/SKILL.md` L436-441 "步骤 14A — 撰写 RESULT.md"
- **关键决策**:BUG 路径的 `RESULT.md` 14 章节与 REQ 路径**完全一致**;**关键差异**:第 2 章"上游引用"写 `fix/<BUG-NNN>/RESULT.md`(缺陷详情) + `fix/<BUG-NNN>/investigation.md`(若有) + 项目级规范,而不是 `require/<REQ>/RESULT.md` + `design/<REQ>/RESULT.md`

### 模块:`code-plan/templates/task-plan.md`
- **复用方式**:直接作为 BUG 路径的 `PLAN.md` 模板(沿用 REQ 路径的 8 章节结构)
- **引用位置**:`plugins/code-skills/skills/code-plan/SKILL.md` L453-461 "步骤 15A — 撰写 PLAN.md"
- **关键决策**:BUG 路径的 `PLAN.md` 8 章节与 REQ 路径**完全一致**;**关键差异**:
  - 任务总览"触发/来源"列 = `缺陷修复`(沿用既有 13 枚举之一)
  - 任务编号前缀 = `TASK-BUG-`(新格式)
  - 任务总览"需求"列 = `BUG-NNN`(3 位)

### 模块:`code-fix/SKILL.md`
- **复用方式**:沿用既有(0 改动)
- **引用位置**:`plugins/code-skills/skills/code-fix/SKILL.md` L185-200 "步骤 0-1"
- **关键决策**:`code-fix` 是上游登记方,登记后状态推进由 `code-fix` 自己负责(FR-8 强约束)

### 模块:`code-it/SKILL.md` 步骤 21
- **复用方式**:沿用既有(0 改动)
- **引用位置**:`plugins/code-skills/skills/code-it/SKILL.md` L677-686
- **关键决策**:处理缺陷状态与本轮起点(沿用既有);`修复规划中` → `修复编码中` 推进逻辑不变

### 模块:`code-dashboard/SKILL.md`
- **复用方式**:沿用既有(0 改动)
- **关键决策**:`code-dashboard` 解析既有"任务清单"区段;BUG 任务行格式与 REQ 任务行**同构**,解析器自然支持

## 修改既有模块

### 模块:`code-plan/SKILL.md` 步骤 19-28A+1(L588-735)
- **变更点**:
  1. 步骤 19-22 既有内容**保留**,文字微调(标注"沿用 REQ 步骤 3/5")
  2. 步骤 23 — 增加 E-1 边界(检测历史 `fix-plan.md`):"若 `fix-plan.md` 存在(仅 BUG-00001 历史)→ 提示'检测到历史 fix-plan.md,本需求已不再生成该文件;是否继续以本缺陷的 fix-plan.md 为参考?' + 3 选 1(继续/手动迁移/中止)"
  3. 步骤 24A(首次规划) — **重写**为"产出 `RESULT.md` + `PLAN.md` + 7 份过程文档"(关键决策旁标注"依据规范:`encoding-conventions §规则 1/3`"等)
  4. 步骤 25A(用户对齐) — 既有内容**保留**
  5. 步骤 26A(撰写文档) — 改"按 `templates/fix-plan.md` 的章节结构生成" → "按 `templates/plan.md` + `templates/task-plan.md` 同构产出"
  6. 步骤 27A(同步 `fix/<BUG>/RESULT.md` 与 `fix/RESULT.md`) — 既有内容**保留**
  7. 步骤 28A(同步版本看板"缺陷清单") — 既有内容**保留**
  8. **步骤 28A+1(本需求新增)**:同步版本看板"任务清单"区段(从 `PLAN.md` 任务总览批量登记,**触发/来源**=**缺陷修复**)
- **变更对既有调用方的影响**:
  - `code-it` 步骤 17 消费方联动改造(见下文)
  - `code-review` 评审 — 沿用既有解析 `PLAN.md` 任务总览;0 修改
  - `code-dashboard` 看板 — 沿用既有解析"任务清单"区段;0 修改
  - `code-auto` 编排 — 沿用既有子技能调用表;0 修改

### 模块:`code-it/SKILL.md` 步骤 17-25 + frontmatter L5(L638-800)
- **变更点**:
  1. **frontmatter L5 description** — 改"从 `fix-plan.md` 读取修复方案" → "从 `PLAN.md` 读取修复任务列表"
  2. **步骤 17**(校验缺陷与修复方案存在)— 改为读 `PLAN.md` + `RESULT.md`,**不**读 `fix-plan.md`;**新增 E-7 边界**:"`fix-plan.md` 存在(仅 BUG-00001 历史)→ 步骤 17 退化(若 `PLAN.md` 缺失但 `fix-plan.md` 存在,提示用户'检测到历史 fix-plan.md;请先用 `code-plan` 产出 `PLAN.md`')"
  3. **步骤 22**(实施修复)— 过程记录改为追加到 `code/<TASK-BUG-...>/work-log.md`(原 `fix-work-log.md`);**新增 E-9 边界**:"`fix-work-log.md` 存在(仅 BUG-00001 历史)→ 步骤 22 检测到,提示'检测到历史 fix- 前缀过程文档;本次为新结构 TASK-BUG- 任务编号,过程文档不再使用 fix- 前缀;是否手动迁移?推荐不迁移'"
  4. **步骤 23**(编译/启动/测试)— 改为 `code/<TASK-BUG-...>/compile-and-run.md` / `test-results.md`
  5. **步骤 24**(同步)— **不**再写 `fix-plan.md`;**新增 E-11 边界**(同 E-7);仍同步 `fix/<BUG>/RESULT.md` + `fix/RESULT.md` + 看板"缺陷清单"
  6. **步骤 25**(汇报)— 改"同步的文件"字段描述:"`fix/<缺陷>/RESULT.md` / `fix/RESULT.md` / `fix/<缺陷>/PLAN.md`(若状态推进) / 版本看板'缺陷清单'+'任务清单'"
- **变更对既有调用方的影响**:
  - `code-auto` 调 `code-it TASK-BUG-...` 时,新路径触发(BUG-00001 修复方案 A3 脏标记文件继续生效,0 修改)
  - `code-fix` 步骤 2-3 维护的"缺陷清单"区段**不变**

### 模块:`assistants/V0.0.2/RESULT.md` "任务清单"区段
- **变更点**:`code-plan` 步骤 28A+1 在"任务清单"区段追加 BUG 任务行(每条 BUG 任务一行)
- **变更对既有调用方的影响**:
  - `code-dashboard` 看板 — 沿用既有解析;**0** 修改(区段 + 字段 + 枚举值**不**变)
  - `code-publish` 前置检查 — 沿用既有(从 RESULT.md 读取所有需求 + 任务 + 缺陷状态);**0** 修改
  - `code-review` 评审 — 沿用既有(从 `PLAN.md` 任务总览读取);**0** 修改
