# 模块详细化 — REQ-00002
版本:V0.0.1

## 模块:T-1 同步 10 个 SKILL.md(只改正文,不改 frontmatter)

- **路径**:`plugins/code-skills/skills/<技能名>/SKILL.md` × 10
- **关键变更**:
  - 把正文中所有 `REQ-2026-0001` / `REQ-2025-0099` 替换为新格式 `REQ-00001` / `REQ-00510`(编号视上下文)
  - 把正文中所有 `REQ-2026-0001-001` 替换为新格式 `REQ-00001-00001` 或新 TASK 编码 `TASK-REQ-00001-00001`(视上下文)
  - **不修改** YAML frontmatter(`name` + `description` 保持原状)
- **关键文件**:
  - `skills/code-it/SKILL.md`(L4 + L107 命中)
  - `skills/code-plan/SKILL.md`(L4 + L197 命中)
  - `skills/code-require/SKILL.md`(L44 + L267 + L270 命中)
  - `skills/code-unit/SKILL.md`(L103 命中)
  - 其余 6 个 SKILL.md 需 `Read` 后逐文件确认替换点
- **状态归属**:`code-it` 执行,本模块只产出文件改动 + 1 commit
- **与概要设计的对应**:design §3.1
- **符合的规范**:skill-conventions §规则 1(frontmatter 保持);doc-conventions §规则 1(后续 T-3 同次 commit)

## 模块:T-2 同步 27 模板(改正文占位符 + 示例值)

- **路径**:`plugins/code-skills/skills/<技能名>/templates/*.md` × 27
- **关键变更**:
  - 占位符:`<需求编号>` → `<需求编码>`(语义不变,但示例值需对齐)
  - 示例值:`REQ-2026-0001` → `REQ-00001` / `REQ-00002`
  - 任务编码示例:`REQ-2026-0001-001` → `REQ-00001-00001` 或新 `TASK-REQ-00001-00001`
  - 关联文件示例:`./v0.1.0/require/REQ-2026-0001/RESULT.md` → `./v0.1.0/require/REQ-00001/RESULT.md`
- **关键文件**(基于 Grep 命中):
  - 强命中(必改):`code-design/templates/assistants-layout.md` / `code-require/templates/assistants-layout.md` / `code-plan/templates/assistants-layout.md` / `code-version/templates/assistants-layout.md` / `code-version/templates/version-RESULT.md` / `code-it/templates/assistants-layout.md` / `code-unit/templates/assistants-layout.md` / `code-require/templates/requirements.md` / `code-fix/templates/bug.md`
  - 弱命中(`Read` 后确认):其余 18 个模板
- **状态归属**:`code-it` 执行,本模块产出 27 文件改动 + 1 commit
- **与概要设计的对应**:design §3.2
- **符合的规范**:doc-conventions §规则 2(占位文本需有 TODO 注释);module-conventions(占位符命名)

## 模块:T-3 同步中英 README(同次 commit)

- **路径**:
  - `plugins/code-skills/README.md`
  - `plugins/code-skills/README.en.md`
- **关键变更**:
  - 替换所有 `code-require REQ-2026-0001` / `code-design REQ-2026-0001` / `code-plan REQ-2026-0001` / `code-it REQ-2026-0001-001` / `code-unit REQ-2026-0001-001` / `code-review REQ-2026-0001` / `code-fix "在 code-it REQ-2026-0001-003 过程中发现:..."` 为新格式示例
  - 替换所有 `./v0.1.0/require/REQ-2026-0001/RESULT.md` 路径引用
  - 中英同次 commit(doc-conventions §规则 1)
- **关键行**:
  - README.md:14 处命中(L439 / 480 / 524 / 575 / 577 / 615 / 646 / 731 / 732 / 734 / 735 / 737 / 739 / 756 / 760 / 797 / 809 / 811 / 815 / 821)
  - README.en.md:14 处命中(同结构)
- **状态归属**:`code-it` 执行,本模块产出 2 文件改动 + 1 commit(中英同次)
- **与概要设计的对应**:design §3.3
- **符合的规范**:doc-conventions §规则 1(同次提交)+ 规则 2(与代码现状同步)

## 模块:T-4 同步 CLAUDE.md(预期 0 变更)

- **路径**:`plugins/code-skills/CLAUDE.md`
- **关键变更**:Grep 验证 → 0 命中 → 记录"已核查,无需修改"
- **验证手段**:`Grep "REQ-\d{4}-\d{4}" plugins/code-skills/CLAUDE.md` → 0 命中
- **状态归属**:`code-it` 执行,本模块产出 0 文件改动 + 0 commit
- **与概要设计的对应**:design §3.4
- **符合的规范**:doc-conventions §规则 2(占位文本需有 TODO 注释;不适用)

## 模块:T-5 创建 `encoding-conventions.md` 规范文件

- **路径**:`assistants/rules/encoding-conventions.md`(新建文件)
- **关键内容**:
  - 规范 1:编码格式定义(REQ / BUG / TASK 三类)
  - 规范 2:5 位纯数字格式约束
  - 规范 3:嵌套式 TASK 编码规则
  - 规范 4:实施流程(编码 → 提交 → 引用)
- **创建者**:`code-it` 本任务(由 code-rule 后续接管维护)
- **授权**:本设计 §Q-3 已分析"code-it 创建新文件不违反既有规则"
- **状态归属**:`code-it` 执行,本模块产出 1 新文件 + 1 commit
- **与概要设计的对应**:design §3.6(条件子任务 9,Q-8=a)
- **符合的规范**:本规范文件本身就是规则;`doc-conventions` 中"规则 1/2"的格式风格

## 模块:T-6 创建 `migration-mapping.md` 迁移映射

- **路径**:`assistants/rules/migration-mapping.md`(新建文件)
- **关键内容**:
  - 旧格式 → 新格式映射表(覆盖所有已发现的旧串)
  - 已知不完全映射(若有)
  - 维护说明
- **创建者**:`code-it` 本任务
- **授权**:同 T-5
- **状态归属**:`code-it` 执行,本模块产出 1 新文件 + 1 commit
- **与概要设计的对应**:design §3.7(条件子任务 10,Q-9=a)
- **符合的规范**:同 T-5

## 模块:T-7 全仓库穷举式 Grep + 偏差日志 + 不变量自检 + 提交(收尾)

- **路径**:无文件修改,产出 1 个 `code/REQ-00002-00007/RESULT.md` + `work-log.md` + `deviations.md`
- **关键动作**:
  - 全仓库 `Grep "REQ-\d{4}-\d{4}"` → 应仅命中本工作目录 + V0.0.0 EXISTING-* 基线
  - 13 条不变量自检(INV-1 ~ INV-13)
  - `deviations.md` 记录 3 类已知偏离(参考 REQ-00001 deviations.md):
    1. `doc-conventions.md:113` install 命令旧串(规则文件不可改)
    2. V0.0.0 EXISTING-* 基线历史(范围外)
    3. 5 个现有 rules/ 文件的旧串示例(范围外)
  - **不再 commit** —— 7 个 commit 已由 T-1 ~ T-6 各自完成
- **状态归属**:`code-it` 执行
- **与概要设计的对应**:design §3.8(全仓库验证)
- **符合的规范**:REQU FR-9(看板同步)+ FR-10(范围)

## 模块:T-8 看板同步(本设计 + 实施完成后)

- **路径**:
  - `assistants/V0.0.1/RESULT.md`(版本看板)
  - `assistants/V0.0.1/plan/REQ-00002/PLAN.md`(本计划)
  - `assistants/V0.0.1/design/REQ-00002/clarifications.md`(本设计产生的问题记录)
- **关键动作**:
  - 看板"需求清单"区段:REQ-00002 状态保持"已完成"(需求分析阶段)
  - 看板"概要设计清单"区段:REQ-00002 状态保持"已完成"(概要设计阶段)
  - 看板"详细设计与任务计划汇总"区段:**新增** REQ-00002 计划条目
  - 看板"任务清单"区段:**新增** 7 个任务行
  - 看板"里程碑"区段:更新 M2 = "编码格式统一落地"
  - 看板"变更记录"区段:追加本次详细设计完成 + 后续 7 任务完成记录
  - 看板"执行的开发命令记录"区段:7 个 commit 各自对应 1 条
- **状态归属**:`code-it` 在 T-7 完成后执行
- **与概要设计的对应**:design §6(与版本看板同步)
- **符合的规范**:REQU FR-9(看板同步)
