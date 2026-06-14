# 模块详细化 — REQ-00025
版本:V0.0.3

## 模块:encoding-conventions.md(对应概要设计 §3.1 / D-1 / D-2 / D-6)

- **路径**:`./assistants/rules/encoding-conventions.md`
- **状态**:**修改**(+ 1 个新增小节 §规则 1.5)
- **关键修改锚点**(语义化,非行号):
  - `§规则 1 §条款 表` 3 行(需求 / 缺陷 / 任务):正则列 + 容量列 + 备注列
  - `§规则 2 §条款`(5 位纯数字约束):从"5 位固定宽度"改为"生成端 5 位纯数字 + 接收端任意 1+ 位后缀"
  - `§规则 4 §条款` 步骤 4(解析入口):正则字面量替换
  - `§规则 1.5`(全新小节,**插在 §规则 1 与 §规则 2 之间**):"第三方平台接入指南" + 初始空表
- **关键类/函数**:N/A(纯文档)
- **内部状态**:N/A
- **关键调用顺序**:N/A
- **状态归属**:跨版本共享,所有 `code-*` 技能只读
- **资源管理**:N/A
- **错误处理范式**:N/A
- **日志埋点**:N/A
- **与概要设计的对应**:§3.1 + D-1 + D-2 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1/2/4`(本需求**直接修订**)

## 模块:code-require/SKILL.md

- **路径**:`./plugins/code-skills/skills/code-require/SKILL.md`
- **状态**:**修改**(字面更新)
- **关键修改锚点**:
  - `§输入 > 需求编码格式`(语义化锚点):"必须 5 位纯数字" → "默认 5 位纯数字 / 接收可放宽"
  - `§工具使用约定 > 标题解析(REQ-00013 新增) > parseResultTitle` 注释段:加注"完整编号不截断"
- **与概要设计的对应**:§3.2 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1`(本需求修订后)+ `skill-conventions.md §规则 1`

## 模块:code-design/SKILL.md

- **路径**:`./plugins/code-skills/skills/code-design/SKILL.md`
- **状态**:**修改**
- **关键修改锚点**:
  - `§输入 > 需求编码格式`:同 code-require
  - `§工作目录约定(强制) > 本技能的目录粒度是需求`:加注"沿用新规则(后缀自由)"
- **与概要设计的对应**:§3.3 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1`(本需求修订后)+ `skill-conventions.md §规则 1`

## 模块:code-plan/SKILL.md

- **路径**:`./plugins/code-skills/skills/code-plan/SKILL.md`
- **状态**:**修改**
- **关键修改锚点**:
  - `§输入 > 需求编码 / 缺陷编号`:同 code-require
  - `§工作流程 > 步骤 10A 任务拆分 > 任务编号`:格式定义从"五位补零" → "**生成端** 5 位纯数字(默认) + **接收端** `[A-Za-z0-9.\-_]+`"
  - `§工作流程 > 步骤 9B 增量更新 PLAN.md > 任务编号分配`:同上加注
- **与概要设计的对应**:§3.4 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1/3`(本需求修订后)+ `skill-conventions.md §规则 1`

## 模块:code-it/SKILL.md

- **路径**:`./plugins/code-skills/skills/code-it/SKILL.md`
- **状态**:**修改**
- **关键修改锚点**:
  - `§输入 > 任务编码格式`:同 code-require
  - `§工作流程 > 步骤 1 解析任务编码`:正则从 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` → `^TASK-(REQ|BUG)-[A-Za-z0-9.\-_]+-[A-Za-z0-9.\-_]+$`
  - `§工作流程 > 步骤 7 写入 RESULT.md`:子目录生成时,父级 + 子级后缀沿用新规则
- **与概要设计的对应**:§3.5 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1/3`(本需求修订后)+ `skill-conventions.md §规则 1`

## 模块:code-unit/SKILL.md

- **路径**:`./plugins/code-skills/skills/code-unit/SKILL.md`
- **状态**:**修改**
- **关键修改锚点**:
  - `§输入 > 任务编码格式`:同 code-require
- **与概要设计的对应**:§3.6 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1`(本需求修订后)+ `skill-conventions.md §规则 1`

## 模块:code-check/SKILL.md

- **路径**:`./plugins/code-skills/skills/code-check/SKILL.md`
- **状态**:**修改**
- **关键修改锚点**:
  - `§输入 > 需求编号 / 任务编码`:同 code-require
- **与概要设计的对应**:§3.7 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1`(本需求修订后)+ `skill-conventions.md §规则 1`

## 模块:code-fix/SKILL.md

- **路径**:`./plugins/code-skills/skills/code-fix/SKILL.md`
- **状态**:**修改**
- **关键修改锚点**:
  - `§输入 > 缺陷编号格式`:同 code-require
  - `§工作流程 > 步骤 1 收集输入 ID 并判定路径`:正则从 `^BUG-\d{5}$` → `^BUG-[A-Za-z0-9.\-_]+$`
- **与概要设计的对应**:§3.8 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1`(本需求修订后)+ `skill-conventions.md §规则 1`

## 模块:code-dashboard/SKILL.md

- **路径**:`./plugins/code-skills/skills/code-dashboard/SKILL.md`
- **状态**:**修改**
- **关键修改锚点**:
  - `§工作流程 > 算法 4 解析任务编号`:正则从 `TASK-(REQ|BUG)-\d{5}-\d{5}` → `TASK-(REQ|BUG)-[A-Za-z0-9.\-_]+-[A-Za-z0-9.\-_]+`(双正则兼容,沿用 AC-7)
- **与概要设计的对应**:§3.9 + D-6
- **符合的规范**:`encoding-conventions.md §规则 1/3`(本需求修订后)+ `skill-conventions.md §规则 1`
