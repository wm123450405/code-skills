# 需求提示词文档 — REQ-00007(增加 `/code-auto` 自动开发技能)

- 需求编码:REQ-00007
- 所属版本:V0.0.2
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-04
- 最近更新:2026-06-04 13:59
- 当前版本:v1
- **主题**(来自用户输入):
  > 增加需求: 增加`/code-auto` 自动开发技能,技能接收一个需求内容,然后自动按照 `/code-require`、`/code-desgin`(笔误 → `/code-design`)、`/code-plan` 的技能顺序逐步的拆解成开发任务,并自动使用 `/code-it`、`/code-unit` 技能逐个去完成代码和单元测试(如需要)的编写工作,最后自动执行 `/code-review` 对开发内容进行审查,若发现问题产生了修改任务后,自动使用 `/code-it`、`/code-unit` 技能完成修改任务,后再执行 `/code-review`,依次循环往复,直到代码审查结果中没有需要必须修改的内容再结束。所有使用其他技能完成任务的过程中若遇到需要用户确认的场景,均使用推荐的方式自动完成,整个过程不再需要用户确认,所有事项都自动完成完整的流程。

---

## 1. 需求概述

**为谁**:`code-skills` 仓库的 AI 协作者 + 项目主导者(在希望"从需求到代码 + 单测 + 评审全自动跑通"的场景)。

**解决什么问题**:`code-skills` 现有 9 个 `code-*` 技能中,`code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-review` 是**开发周期的 6 个步骤**;但每次都需要**用户手动**调,且过程中遇到 `AskUserQuestion` 时需用户决策。这导致:
- **机械性工作**:每个需求都重复"调 6 次技能 + 看结果"
- **上下文割裂**:每调一次技能,用户需重述需求背景
- **评审循环低效**:`code-review` 产生派生任务后,用户需手动调 `code-it` 完成,再 `code-review` — 反复

**带来什么价值**:
1. **一键全自动**:调一次 `/code-auto "<需求内容>"`,从需求到"代码 + 单测 + 评审无必须改"全自动跑通
2. **完全无人确认**:所有 `AskUserQuestion` 场景总选"推荐项"(Q-4 锁定 A)
3. **评审循环自动化**:`code-review` 派生任务 → 自动 `code-it` / `code-unit` → 再 `code-review`,直到无"必须改"(Q-1 锁定 A)
4. **可中止**:用户可随时 `Ctrl+C`,本技能输出报告(剩余可恢复信息)

---

## 2. 背景与目标

### 2.1 背景
- `code-skills` 9 个技能中,8 个是"单步"技能;`code-auto` 是**编排者**,8 个是**被驱动**
- 现有 REQ-00005 已为 `code-require` / `code-design` / `code-plan` 加了"首步拉取 + 末步提交",本需求**不**引入"批量模式"(Q-5 锁定 A)
- 现有 REQ-00006 提供了"开发完成 → 发布"的下游衔接;本需求**不**触发 `code-publish`(Q-6 采纳默认)
- 现有 REQ-00004 提供了"开发状态可视化";`code-auto` 完成时,看板数据应与 `code-dashboard` 显示一致

### 2.2 业务目标
- **G-1**:新增第 10 个 `code-*` 技能 `code-auto`,**编排者**角色
- **G-2**:`code-auto` 串行驱动 6 个子技能(`code-require` → `code-design` → `code-plan` → `code-it`+`code-unit` 循环 → `code-review` 循环)
- **G-3**:`code-review` 循环终止条件 = "无必须改发现"(Q-1 锁定 A)
- **G-4**:完全无人确认(Q-4 锁定 A:总选推荐项)
- **G-5**:异常立即中断 + 报告(Q-2 锁定 A)
- **G-6**:用户可随时 `Ctrl+C` 中止,中止时输出报告(Q-3 锁定 A)

### 2.3 本次目标
- 新增 `plugins/code-skills/skills/code-auto/SKILL.md` 技能目录
- **不**修改其他 9 个 `code-*` 技能(Q-5 锁定 A — 不引入批量模式,子技能不变)
- **不**修改 `marketplace.json` / `plugin.json`
- **不**修改 `commit-conventions.md` / CLAUDE.md "AI 工作约定"(留作 follow-up)
- 若需要,在 `plugins/code-skills/README.md` + `README.en.md` 的"主要能力"中追加一行(同次提交,遵循 `doc-conventions §规则 1`)

---

## 3. 用户角色与场景

### 3.1 角色
- **R-1 全自动用户**:希望"一键需求 → 一键代码 + 单测 + 评审通过"
- **R-2 现场工程师**:可随时 `Ctrl+C` 中止(中止时输出报告)
- **R-3 项目主导者**:`code-auto` 完成后,看到报告,可选调 `code-dashboard` / `code-publish`

### 3.2 关键场景

#### S-1:全流程顺利(主流程,无必须改)
- 用户输入:`/code-auto "添加用户登录功能,支持手机号+密码"`
- 技能执行(伪时序):
  1. 调 `/code-require "<原内容>"` → 产出 `require/REQ-00008/RESULT.md`
  2. 调 `/code-design REQ-00008` → 产出 `design/REQ-00008/RESULT.md`
  3. 调 `/code-plan REQ-00008` → 产出 `plan/REQ-00008/{RESULT,PLAN}.md` + 拆 N 个任务
  4. **任务循环**:对每个任务调 `/code-it` + `/code-unit`(若需要)
  5. 调 `/code-review REQ-00008` → 评审报告
  6. `code-review` 结果 = "无必须改" → **结束**
- 用户看到:
  ```
  ✓ code-auto 完成
  
  执行摘要:
    需求分析(code-require):1 次
    概要设计(code-design):1 次
    详细设计(code-plan):1 次
    代码实现(code-it):5 次
    单元测试(code-unit):3 次
    代码审查(code-review):1 次
    总计:12 次子技能调用
  
  最终状态:
    REQ-00008:已完成(需求分析)
    任务:TASK-REQ-00008-001 ~ 005,均已完成
    缺陷:0
    派生任务:0
  
  后续建议:
    > 执行 /code-dashboard 查看完整状态
    > 执行 /code-publish 生成发布手册
  ```

#### S-2:评审循环 1 轮(派生任务被自动修复)
- 用户输入:`/code-auto "添加用户登录功能"`,假设 `code-review` 产生 2 个"必须改"任务
- 技能执行:
  1. ~ 5. 同 S-1
  6. `code-review` 第 1 轮 → "必须改"任务:`F-1`(修复 X 函数)+ `F-2`(补充 Y 测试)
  7. **派生任务循环**:
     - 调 `code-it F-1` → 完成派生任务 1
     - 调 `code-it F-2` → 完成派生任务 2
     - 调 `code-unit F-2` → 补充测试(若 F-2 涉及)
  8. 调 `code-review REQ-00008` → 第 2 轮 → "无必须改" → **结束**
- 用户看到:
  ```
  ✓ code-auto 完成(含 1 轮评审循环)
  
  执行摘要:
    code-require:1 | code-design:1 | code-plan:1
    code-it:7(5 需求任务 + 2 派生任务)| code-unit:4 | code-review:2
    总计:16 次子技能调用
  
  派生任务:2(均已完成)
  ```

#### S-3:异常中断(子技能崩溃)
- 用户输入:`/code-auto "添加 X"`,假设 `code-it` 在第 3 个任务时崩溃
- 技能执行:
  1. ~ 5. 顺利
  6. 调 `code-it TASK-REQ-00008-003` → 退出码非 0
  7. **立即中断**(Q-2 锁定 A)
- 用户看到:
  ```
  ✗ code-auto 中断(子技能异常)
  
  中断位置:code-it TASK-REQ-00008-003
  错误信息:<stderr 内容>
  退出码:1
  
  已完成工作(已保留):
    REQ-00008 需求分析:✓
    REQ-00008 概要设计:✓
    REQ-00008 详细设计:✓
    任务 001 ~ 002:已完成
    任务 003:~ 中断
  
  用户可重跑 code-auto 以从中断处恢复(注:本版本不实现增量恢复,重跑会从头开始)
  ```

#### S-4:用户 `Ctrl+C` 中止
- 用户输入:`/code-auto "大型需求"`,跑到第 7 个子技能时按 `Ctrl+C`
- 技能执行:
  1. ~ 7. 顺利
  8. 收到 SIGINT → 输出报告 → 退出
- 用户看到(同 S-3 格式):
  ```
  ⏹ code-auto 用户中止
  
  中断位置:code-unit TASK-REQ-00008-004
  已完成子技能调用:9 次
  剩余工作:<同上>
  ```

#### S-5:用户确认场景自动选择
- 用户输入:`/code-auto "..."`,假设 `code-require` 内部触发 `AskUserQuestion`("需求 Q-1:Q-1 默认 A 还是 B?")
- 技能执行:
  - `code-auto` 检测到 `AskUserQuestion` 触发 → 选"推荐项"(Q-4 锁定 A,通常是第一个选项)
  - 继续执行
- 用户**全程无感知**(除非显式查看日志)

#### S-6:无激活版本
- 用户输入:`/code-auto "..."`,但 `.current-version` 不存在
- 技能执行:
  1. **步骤 0**:检测失败 → 提示用户调 `code-version`
  2. 退出(同其他 9 个技能)

#### S-7:`code-review` 出现"必须改"但子技能无法完成(理论边界)
- 假设 `code-review` 产生"必须改"任务 F-N,但 `code-it` 无法完成(如依赖外部资源)
- 技能执行:
  1. 调 `code-it F-N` → 退出码非 0
  2. 立即中断 + 报告(同 S-3)

---

## 4. 功能需求(FR)

### FR-1:`code-auto` 技能定义与元信息

- **描述**:新增 `plugins/code-skills/skills/code-auto/SKILL.md`,遵循 `skill-conventions.md §规则 1`:
  - YAML frontmatter 含 `name: code-auto` + 一句完整 `description`
- **优先级**:必须
- **AC**:
  - AC-1.1:`SKILL.md` 顶部 YAML 含 `name: code-auto`
  - AC-1.2:`SKILL.md` 顶部 YAML 含 `description`,内容涵盖"自动驱动 6 个子技能跑通开发周期 + 评审循环 + 完全无人确认"
  - AC-1.3:`name` 与目录名完全一致

### FR-2:接收需求内容 + 启动编排

- **描述**:`code-auto` 接收 1 个字符串参数(需求内容,自然语言)
- **优先级**:必须
- **AC**:
  - AC-2.1:无参数 → 提示用法示例,退出
  - AC-2.2:有 1 个参数 → 视为需求内容
  - AC-2.3:有 >1 个参数 → 视为"参数拼接"(`$arg1 $arg2 ...`)

### FR-3:子技能调用顺序与依赖

- **描述**:`code-auto` 按固定顺序串行调子技能(Q-7 采纳默认)
- **优先级**:必须
- **调用序列**:
  1. `/code-require "<需求内容>"` → 产生 REQ-NNNNN
  2. `/code-design REQ-NNNNN` → 产生 design/
  3. `/code-plan REQ-NNNNN` → 产生 plan/ + 拆任务
  4. **任务循环**(对 plan/PLAN.md 中每个任务):
     - `/code-it TASK-...`(或 `REQ-...-...` 旧格式)
     - `/code-unit TASK-...`(若需要测试)
  5. `/code-review REQ-NNNNN` → 评审
  6. **评审循环**(若"必须改"存在):
     - 对每个"必须改"任务 → `/code-it F-N` + `/code-unit F-N`(若需要)
     - 回到步骤 5
- **AC**:
  - AC-3.1:严格串行(Q-7),不并发
  - AC-3.2:每步等待子技能**完全完成**后,才进入下一步
  - AC-3.3:子技能**完整失败**(退出码 ≠ 0)→ 中断(Q-2 锁定 A)
  - AC-3.4:子技能**部分失败**(输出有效但有警告)→ 继续(Q-2 锁定 A 不适用此情形)
  - AC-3.5:从子技能输出中解析"REVIEW-REPORT.md" / 派生任务列表,作为循环判定的输入

### FR-4:任务循环(对每个 plan/PLAN.md 中的任务)

- **描述**:`code-auto` 对 `plan/REQ-NNNNN/PLAN.md` 中**所有**任务,按顺序调 `/code-it` + `/code-unit`
- **优先级**:必须
- **AC**:
  - AC-4.1:从 `PLAN.md` "任务总览"区段解析所有任务编码(`TASK-...` 新格式 + `REQ-...-...` 旧格式,均支持 — 沿用 `code-dashboard` NFR-3 兼容策略)
  - AC-4.2:对每个任务:
     - 调 `code-it <任务编码>`
     - 调 `code-unit <任务编码>`(若 `code-it` 输出含"测试需要=Y")
  - AC-4.3:任务按"任务总览"区段的行顺序执行
  - AC-4.4:每个任务完成后,**不**做"中间评审"(`code-review` 在所有任务完成后才调,见 FR-5)

### FR-5:评审循环(对 `code-review` 派生任务)

- **描述**:`code-auto` 调 `/code-review REQ-NNNNN`,若产生"必须改"任务,自动完成并复评
- **优先级**:必须
- **AC**:
  - AC-5.1:调 `code-review REQ-NNNNN` → 读 `review/REQ-NNNNN/REVIEW-REPORT.md`
  - AC-5.2:若"必须改"列表为空 → 结束
  - AC-5.3:若"必须改"列表非空 → 对每条"必须改"任务:
     - 调 `code-it <派生任务编码>`(派生任务编码由 `code-review` 写入 `PLAN.md` 任务总览,`code-auto` 从中读取)
     - 调 `code-unit <派生任务编码>`(若派生任务涉及测试)
  - AC-5.4:派生任务完成后,重新调 `code-review REQ-NNNNN`
  - AC-5.5:循环直至"必须改"列表为空(Q-1 锁定 A:无轮数上限)
  - AC-5.6:**必须改判定**:沿用 `code-review` 既有"必须改"档(与"建议改"/"可选"区分);具体阈值由 `code-review` 内部决定,`code-auto` 仅消费

### FR-6:用户确认自动化(Q-4 锁定 A)

- **描述**:`code-auto` 驱动子技能时,所有 `AskUserQuestion` 自动选"推荐项"
- **优先级**:必须
- **"推荐项"定义**:
  - `AskUserQuestion` 工具的 `options` 数组中,**第一项**为推荐项
  - 若选项标注"(推荐)"或"(Recommended)",取该项
  - 若无标注,取第一项
- **AC**:
  - AC-6.1:子技能触发 `AskUserQuestion` 时,`code-auto` 自动选"推荐项",**不**向用户提问
  - AC-6.2:用户全程无感知(除非事后查看日志)
  - AC-6.3:`code-auto` 自身**不**触发 `AskUserQuestion`(本技能无歧义需澄清)

### FR-7:异常立即中断 + 报告(Q-2 锁定 A)

- **描述**:子技能异常时立即中断 + 报告
- **优先级**:必须
- **AC**:
  - AC-7.1:子技能退出码 ≠ 0 → 立即中断
  - AC-7.2:不重试(Q-2 锁定 A 衍生:避免阻塞)
  - AC-7.3:输出报告(中断位置 / 错误信息 / 已完成工作 / 剩余工作)
  - AC-7.4:**不**回滚已产生的文件(`code-auto` 不持有"事务"概念,所有已写文件保留在磁盘)
  - AC-7.5:`Ctrl+C` (SIGINT) 视为"用户中止",同 S-4 流程

### FR-8:不修改其他 9 个 `code-*` 技能(Q-5 锁定 A)

- **描述**:`code-auto` 是"编排者",**不**修改其他 9 个技能的 SKILL.md;子技能保持各自现有行为
- **优先级**:必须
- **AC**:
  - AC-8.1:9 个子技能 SKILL.md **不**被本需求修改
  - AC-8.2:子技能按各自原始设计运行(含 REQ-00005 加的"首步拉取 + 末步提交",不引入批量模式)
  - AC-8.3:`marketplace.json` / `plugin.json` **不**被本需求修改
  - AC-8.4:`assistants/rules/` 下任何规范文件**不**被本需求修改
  - AC-8.5:中英 README 中追加"code-auto"能力描述(按 `doc-conventions §规则 1` 同次提交)

### FR-9:完整报告(Q-3 锁定 A)

- **描述**:`code-auto` 完成或中断时,输出详细报告
- **优先级**:必须
- **报告字段**:
  - **总状态**:✓ 完成 / ⏹ 用户中止 / ✗ 子技能异常
  - **执行摘要**:每个子技能的调用次数
  - **最终状态**:REQ-NNNNN 状态 / 任务清单 / 缺陷 / 派生任务
  - **后续建议**(完成时):`code-dashboard` / `code-publish` 的提示
  - **剩余工作**(中断时):已完成 + 未完成清单
- **AC**:
  - AC-9.1:完成时输出 S-1 格式报告
  - AC-9.2:异常时输出 S-3 格式报告
  - AC-9.3:中止时输出 S-4 格式报告
  - AC-9.4:报告写入 `./assistants/<版本号>/require/REQ-NNNNN/auto-report.md`(留痕,便于事后回溯)

### FR-10:报告留痕(新增,本需求必备)

- **描述**:`code-auto` 完整执行后,把报告写入版本工作空间,作为 `code-require` 阶段的过程文档之一
- **优先级**:必须
- **AC**:
  - AC-10.1:写入 `./assistants/<版本号>/require/REQ-NNNNN/auto-report.md`
  - AC-10.2:与 `RESULT.md` / `materials-index.md` 等同目录
  - AC-10.3:由 `code-auto` 创建(子技能不会写此文件)
  - AC-10.4:含完整 §FR-9 报告字段

---

## 5. 非功能需求 / 约束(NFR)

### NFR-1:零新增依赖
- **描述**:本需求不引入新依赖;复用 Claude Code 的 `Skill` 工具 + 子技能全部已存在
- **强制级别**:必须

### NFR-2:串行而非并发(Q-7 锁定)
- **描述**:`code-auto` 串行调子技能,**不**并发
- **强制级别**:必须
- **理由**:并发调用会导致"上下文冲突"(多个子技能同时写看板的同一区段)

### NFR-3:`code-auto` 自身不自动 commit
- **描述**:`code-auto` 自身**不**触发 `git commit`(Q-12 采纳默认);由各子技能按各自规则提交
- **强制级别**:必须
- **理由**:`code-auto` 是"编排者",不持有"事务"概念

### NFR-4:不引入"批量模式"
- **描述**:`code-auto` **不**为子技能提供"批量模式"开关(Q-5 锁定 A)
- **强制级别**:必须
- **理由**:子技能保持各自现有行为,降低复杂度

### NFR-5:与 `code-require` 数据源严格一致
- **描述**:`code-auto` 产出的"完成"事件必须能被 `code-dashboard` 看到
- **强制级别**:必须

### NFR-6:与 `code-publish` 数据源严格一致
- **描述**:`code-auto` 完成后,本版本应**已通过** `code-publish` 的前置检查
- **强制级别**:必须

### NFR-7:中止约定
- **描述**:`code-auto` 中止(Q-3 锁定 A):
  - 正常完成 → 输出报告 + 写入 `auto-report.md`
  - 异常中断 → 输出报告 + **不**写 `auto-report.md`(避免半成品留痕)
  - 用户 `Ctrl+C` → 输出报告 + **不**写 `auto-report.md`
- **强制级别**:必须

### NFR-8:不增量恢复(Q-11 锁定)
- **描述**:`code-auto` 中止后,不支持"增量恢复";用户需重跑,从头开始
- **强制级别**:必须
- **理由**:增量恢复需要状态机 + 持久化,实现复杂度高;当前 V0.0.2 阶段不实现

### NFR-9:与 REQ-00005 / REQ-00006 / REQ-00004 协同
- **描述**:`code-auto` 不修改这 3 个需求的边界;按其原始设计工作
- **强制级别**:必须

### NFR-10:可观察性
- **描述**:`code-auto` 在每个子技能调用前,打印一行进度(子技能名 / 任务编码 / 第 N 轮)
- **强制级别**:必须
- **目的**:让用户能"跟着看"(`code-auto` 跑长时,用户可观察进度)

---

## 6. 页面与界面(输出形态)

### 6.1 进度输出(每步)

```
[code-auto] 步骤 1/6:code-require "<需求内容>"
[code-auto]   → 产出 REQ-00008
[code-auto] 步骤 2/6:code-design REQ-00008
[code-auto]   → 产出 design/REQ-00008/RESULT.md
[code-auto] 步骤 3/6:code-plan REQ-00008
[code-auto]   → 拆 5 个任务
[code-auto] 步骤 4/6:任务循环(5 个)
[code-auto]   → 1/5:code-it TASK-REQ-00008-001 ✓
[code-auto]   → 1/5:code-unit TASK-REQ-00008-001 ✓ (跳过,无需测试)
[code-auto]   → 2/5:code-it TASK-REQ-00008-002 ✓
[code-auto]   → ...
[code-auto] 步骤 5/6:code-review REQ-00008
[code-auto]   → 第 1 轮:"必须改"任务 2 个
[code-auto] 步骤 6/6:评审循环
[code-auto]   → 1/2:code-it F-1 ✓
[code-auto]   → 2/2:code-it F-2 ✓ + code-unit F-2 ✓
[code-auto]   → code-review 第 2 轮:无"必须改" → 结束
```

### 6.2 完成报告(S-1)

```
✓ code-auto 完成

执行摘要:
  需求分析(code-require):1 次
  概要设计(code-design):1 次
  详细设计(code-plan):1 次
  代码实现(code-it):7 次
  单元测试(code-unit):4 次
  代码审查(code-review):2 次
  总计:17 次子技能调用

最终状态:
  REQ-00008:已完成(需求分析)
  任务:TASK-REQ-00008-001 ~ 005,均已完成
  缺陷:0
  派生任务:2(均已完成)

后续建议:
  > 执行 /code-dashboard 查看完整状态
  > 执行 /code-publish 生成发布手册
```

### 6.3 异常报告(S-3)

```
✗ code-auto 中断(子技能异常)

中断位置:code-it TASK-REQ-00008-003
错误信息:<stderr 内容>
退出码:1

已完成工作(已保留):
  REQ-00008 需求分析:✓
  REQ-00008 概要设计:✓
  REQ-00008 详细设计:✓
  任务 001 ~ 002:已完成
  任务 003:~ 中断

⚠ 本版本不实现增量恢复,请重跑 code-auto 从头开始
```

---

## 7. 交互逻辑

### 7.1 完整状态机

```
[启动]
  ↓
[步骤 0:版本上下文检测] ─────────┐
  ↓ (成功)                        │ (失败 → E-1,提示 code-version)
[步骤 1:code-require <需求>]     │
  ↓ (成功)                        │ (失败 → E-2)
[步骤 2:code-design REQ-...]     │
  ↓ (成功)                        │ (失败 → E-2)
[步骤 3:code-plan REQ-...]       │
  ↓ (成功)                        │ (失败 → E-2)
[步骤 4:任务循环]                │
  ↓ (成功)                        │ (失败 → E-2)
[步骤 5:code-review REQ-...]     │
  ↓                              │
[解析"必须改"列表]              │
  ↓                              │
[列表空?]
  ├─ 是 → [完成 + 报告] → [退出]
  └─ 否 → [步骤 6:派生任务循环]
            ↓
        [回到步骤 5:code-review]
            ↓
        ...(循环直到"必须改"列表空)
```

### 7.2 子技能失败处理

```
[子技能退出码]
  ↓
  ├─ 0 → 继续下一步
  └─ ≠0 → [立即中断 + 报告(不写 auto-report.md)]
```

### 7.3 SIGINT 处理

```
[收到 SIGINT (Ctrl+C)]
  ↓
[输出报告(中止格式)]
  ↓
[退出]
```

---

## 8. 数据与状态

### 8.1 关键数据源

| 数据 | 路径 | 用途 |
| --- | --- | --- |
| 用户输入 | 命令行参数 | 需求内容 |
| `.current-version` | `./assistants/.current-version` | 决定当前版本 |
| `require/REQ-NNNNN/RESULT.md` | 子技能产物 | 步骤 1 输出 |
| `design/REQ-NNNNN/RESULT.md` | 子技能产物 | 步骤 2 输出 |
| `plan/REQ-NNNNN/PLAN.md` | 子技能产物 | 步骤 3 输出 + 步骤 4 任务列表 |
| `plan/REQ-NNNNN/PLAN.md` 任务总览 | 派生任务来源 | 步骤 6 输入 |
| `review/REQ-NNNNN/REVIEW-REPORT.md` | 子技能产物 | 步骤 5/6 输入 |
| `auto-report.md` | 本技能产物 | 步骤 N 输出 |

### 8.2 "推荐项"判定

```ts
{
  pickRecommended(options: AskUserQuestionOption[]): string {
    // 1. 优先取标注 "(推荐)" 或 "(Recommended)" 的项
    const recommended = options.find(o =>
      o.label.includes('(推荐)') || o.label.includes('(Recommended)')
    )
    if (recommended) return recommended.label
    // 2. 否则取第一项
    return options[0].label
  }
}
```

### 8.3 任务编码解析(沿用 `code-dashboard` NFR-3)

```text
新格式正则: ^TASK-(REQ|BUG)-(\d{5})-(\d{5})$
旧格式正则: ^(REQ|BUG)-(\d{5})-(\d{5})$
```

### 8.4 "必须改"判定(消费 `code-review` 输出)

- `code-review` 输出 `REVIEW-REPORT.md`,含"评审发现汇总"区段
- `code-auto` 读取该区段,筛选"级别=必须改" + "状态≠已处理"的发现
- 该列表为空 → 结束;非空 → 派生任务循环

---

## 9. 边界与异常

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | 无 `.current-version` | 提示调 `code-version`,退出 |
| **E-2** | 子技能退出码 ≠ 0 | 立即中断 + 报告(Q-2 锁定 A) |
| **E-3** | 子技能无 `AskUserQuestion` 选项(无 options 数组) | 视为"无歧义",继续(不会发生) |
| **E-4** | `plan/REQ-NNNNN/PLAN.md` 不存在(子技能产物缺失) | 视为"未完成",中断 + 报告 |
| **E-5** | `review/REQ-NNNNN/REVIEW-REPORT.md` 不存在 | 视为"未完成",中断 + 报告 |
| **E-6** | 用户 `Ctrl+C` | 报告(中止格式),**不**写 `auto-report.md` |
| **E-7** | "必须改"循环无收敛(Q-1 锁定 A:无上限) | 持续循环;**接受**"修改引入新问题"风险;用户可 `Ctrl+C` 中止 |
| **E-8** | 子技能耗时过长(如 `code-it` 在某任务上卡住) | 接受(Q-3 锁定 A,中止靠 Ctrl+C) |
| **E-9** | `code-auto` 自身崩溃(代码 bug) | 报告(部分);不写 `auto-report.md` |
| **E-10** | `auto-report.md` 写入失败(权限) | 警告,不中断(报告内容已打印到屏幕) |

---

## 10. 验收标准(AC 总览)

按 FR 编号归类,合计 ~40 条:

- **FR-1**(3 条):AC-1.1 / AC-1.2 / AC-1.3
- **FR-2**(3 条):AC-2.1 / AC-2.2 / AC-2.3
- **FR-3**(5 条):AC-3.1 ~ AC-3.5
- **FR-4**(4 条):AC-4.1 ~ AC-4.4
- **FR-5**(6 条):AC-5.1 ~ AC-5.6
- **FR-6**(3 条):AC-6.1 / AC-6.2 / AC-6.3
- **FR-7**(5 条):AC-7.1 ~ AC-7.5
- **FR-8**(5 条):AC-8.1 ~ AC-8.5
- **FR-9**(4 条):AC-9.1 ~ AC-9.4
- **FR-10**(4 条):AC-10.1 ~ AC-10.4
- **NFR-1**(1 条):零依赖
- **NFR-2**(1 条):串行
- **NFR-3**(1 条):不 commit
- **NFR-4**(1 条):无批量模式
- **NFR-5**(1 条):与 dashboard 一致
- **NFR-6**(1 条):与 publish 一致
- **NFR-7**(1 条):中止约定
- **NFR-8**(1 条):不增量恢复
- **NFR-9**(1 条):与 3 需求协同
- **NFR-10**(1 条):可观察性

**总计**:约 40 条 AC。

---

## 11. 关联需求

| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| **REQ-00005**(V0.0.2) | 子技能被 N 次调用,触发重复拉取/重复提交 | NFR-4:不引入批量模式,子技能按原设计运行 | `./assistants/V0.0.2/require/REQ-00005/RESULT.md` §FR-1 / §FR-3 |
| **REQ-00006**(V0.0.2) | `code-publish` 是下游衔接 | NFR-6:完成后建议调 `code-publish` | `./assistants/V0.0.2/require/REQ-00006/RESULT.md` §FR-1 |
| **REQ-00004**(V0.0.2) | `code-dashboard` 共享看板 3 区段 | NFR-5:数据源严格一致 | `./assistants/V0.0.2/require/REQ-00004/RESULT.md` §FR-4 |
| **REQ-00003**(V0.0.1) | `code-rule` 维护项目级规范 | 本需求**不**直接写 `auto-conventions.md`(留作 follow-up) | `./assistants/V0.0.1/require/REQ-00003/RESULT.md` |
| **REQ-00001**(V0.0.1) | `code-review` 派生任务模式 | FR-5:循环中识别派生任务 | V0.0.1/RESULT.md "派生任务记录"段 |
| **REQ-00002**(V0.0.1) | 3 类编码权威源 | 8.3:任务编码解析严格遵循 | `./assistants/V0.0.1/require/REQ-00002/RESULT.md` + `encoding-conventions.md` |

详细关联分析见 `related-requirements.md`。

---

## 12. 待澄清 / 未决项(本轮未处理 / 留作默认)

### Q-6:与 REQ-00006 的衔接
- **状态**:采纳默认(`code-auto` 完成时提示用户调 `code-publish`)
- **回退路径**:v2 可自动调 `code-publish`

### Q-7:`code-auto` 循环驱动机制
- **状态**:采纳默认(串行,无并发)
- **回退路径**:v2 可考虑并发(需解决上下文冲突)

### Q-8:`plugins/code-skills/CLAUDE.md` "AI 工作约定"小节追加
- **状态**:采纳默认(不追加,留作 follow-up)
- **回退路径**:v2 可由 `code-rule` 沉淀

### Q-9:`commit-conventions.md` 规则沉淀
- **状态**:采纳默认(不沉淀,留作 follow-up)
- **回退路径**:v2 可由 `code-rule` 沉淀

### Q-10:轮次计数器存放位置
- **状态**:采纳默认(不显式存,依靠看板"任务清单"区段)
- **回退路径**:v2 可显式计数

### Q-11:用户中止后"恢复"行为
- **状态**:采纳默认(不支持恢复,重跑从头开始)
- **回退路径**:v2 可实现增量恢复(需状态机 + 持久化)

### Q-12:`code-auto` 自身的"末尾提交"行为
- **状态**:采纳默认(不自动 commit)
- **回退路径**:v2 可加 `--auto-commit` 参数

### Q-13(新增):派生任务预警
- **建议派生**:
  - "用 `code-rule` 沉淀 `auto-conventions.md`(自动化边界/终止条件/中止开关)"(由 `code-review` 决定)
  - "把 `code-auto` 加入 `code-publish` 的'发布前置检查'说明"(由 `code-review` 决定)
  - "`code-dashboard` 升级'全完成'建议为 `code-auto` + `code-publish`"(由 `code-review` 决定)
- **状态**:本需求不阻塞

---

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-04 13:59 | v1 | 初始创建:10 FR / 10 NFR / ~40 AC / 10 个边界场景;Q-1~Q-5 锁定,Q-6~Q-12 留默认/未采用;用户原文 1 处笔误已纠正(`/code-desgin` → `/code-design`);Q-1 锁定"仅按状态终止"(无轮数上限,接受"修改引入新问题"风险);Q-2 锁定"立即中断 + 报告";Q-3 锁定"Ctrl+C 中止 + 报告";Q-4 锁定"总选推荐项";Q-5 锁定"不引入批量模式" | wangmiao |
