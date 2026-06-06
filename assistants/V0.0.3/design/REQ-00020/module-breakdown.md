# 模块拆分 — REQ-00020
更新时间:2026-06-06 17:30

## 模块:`code-design/SKILL.md` 步骤 0b
- **路径**:`plugins/code-skills/skills/code-design/SKILL.md` §步骤 0b
- **状态**:**修改既有**(本需求改后)
- **职责**:`code-design` 启动时确认"整体设计目标 + 功能性"2 个问题(大需求);小需求 1 问
- **对外暴露的接口**:无(纯 SKILL.md 文档)
- **依赖**:无
- **关键决策**:**简化**为 1-2 问(原 5 问 → 1-2 问)
- **符合的规范**:`skill-conventions §规则 1`(frontmatter 不改)+ `module-conventions §规则 1`(过程文档摆放)

## 模块:`code-plan/SKILL.md` 步骤 0b
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 0b
- **状态**:**修改既有**(本需求改后)
- **职责**:`code-plan` 启动时确认 7 维度(原 4 + 新增 3)
- **对外暴露的接口**:无
- **依赖**:沿用 REQ-00011 的"## 设计目标"小节
- **关键决策**:**扩展**为 7 维度(原 4 + 封装性/可复用性/可读性)
- **符合的规范**:同 D-1

## 模块:`code-plan/SKILL.md` §步骤 10A 任务粒度表
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 10A 末尾"按'## 设计目标'小节调整任务粒度"小节
- **状态**:**修改既有**(本需求改后)
- **职责**:扩展性 / 封装性 / 可复用性 / 可读性 = 高时,加对应任务类型
- **对外暴露的接口**:无
- **依赖**:`code-plan` 步骤 0b 写入的"## 设计目标"小节
- **关键决策**:**+3 行**任务粒度调整
- **符合的规范**:`commit-conventions` 0 派生"更新看板"任务(REQ-00017 强约束)

## 模块:`code-plan/SKILL.md` §步骤 0b.0
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 0b.0
- **状态**:**修改既有**(M-1 归并,本需求改后)
- **职责**:与 `code-design` 步骤 0b.0 **完全同构**,引用 `code-design` 步骤 0b.0 段
- **对外暴露的接口**:无
- **依赖**:`code-design` 步骤 0b.0 段
- **关键决策**:**M-1 归并**为引用(原 18 行 → 12 行)
- **符合的规范**:`module-conventions §规则 1`(过程文档摆放,同源段引用)

## 模块:`code-plan/SKILL.md` §步骤 3 / 5 / 21 / 22
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 3 / 5 / 21 / 22
- **状态**:**修改既有**(M-2 归并,本需求改后)
- **职责**:读规范 / 探索代码的"## 公共子步骤"概念
- **对外暴露的接口**:无
- **依赖**:无
- **关键决策**:**M-2 归并**,4 处用 `> 引用:` 块引用
- **符合的规范**:`module-conventions §规则 1`

## 模块:`code-plan/SKILL.md` §步骤 6
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 6
- **状态**:**修改既有**(M-4 归并,本需求改后)
- **职责**:检查 RESULT.md / PLAN.md 是否存在,3 种情形
- **对外暴露的接口**:无
- **依赖**:无
- **关键决策**:**M-4 归并**,4 种情形 → 3 种情形
- **符合的规范**:`module-conventions §规则 1`

## 模块:`code-it/SKILL.md` §步骤 23
- **路径**:`plugins/code-skills/skills/code-it/SKILL.md` §步骤 23
- **状态**:**修改既有**(M-3 归并,本需求改后)
- **职责**:缺陷分支编译/启动/测试验证,引用任务分支 9-12
- **对外暴露的接口**:无
- **依赖**:`code-it` 任务分支步骤 9-12
- **关键决策**:**M-3 归并**,23.1-23.4 共 40 行 → 14 行引用
- **符合的规范**:`module-conventions §规则 1`

## 模块:`code-it/SKILL.md` §步骤 0a.7
- **路径**:`plugins/code-skills/skills/code-it/SKILL.md` §步骤 0a.7
- **状态**:**修改既有**(M-4 归并,本需求改后)
- **职责**:职责归属表 + 6 个独立 E 边界小节
- **对外暴露的接口**:无
- **依赖**:无
- **关键决策**:**M-4 归并**,E-1 / E-4 / E-8 / E-9 合并为 1 张表
- **符合的规范**:`module-conventions §规则 1`

## 自检(对照 13 份规范)

- 命名是否符合规范:是(`code-design` / `code-plan` / `code-it` 既有命名,本需求 0 新增模块名)
- 目录位置是否符合规范:是(SKILL.md 在 `skills/<name>/` 根目录,本需求 0 新增子目录)
- 依赖方向是否违反规范:否(本需求 0 新增跨技能依赖)
- 是否有被禁止的模式:否(本需求 0 引入新模式,仅在既有 SKILL.md 段内追加锚点)
