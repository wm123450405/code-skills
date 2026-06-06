# 模块详细化 — REQ-00020
版本:V0.0.3

## 模块:M-1 调用上下文检测引用
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 0b.0
- **关键类/函数**:无
- **调用顺序**:技能启动 → 步骤 0a git pull → 步骤 0a.0(本需求改后 12 行引用)
- **状态归属**:无
- **与概要设计的对应**:D-4
- **符合的规范**:`module-conventions §规则 1`(过程文档同源段引用)
- **关键变更**:
  - 删除 18 行重复(检测机制 / 24h 超时 / 决策 / 约束 / D-5 修订说明)
  - 新增 12 行 `> 引用:` 段,显式说明"本需求 M-1 归并,引用 `code-design` 步骤 0b.0 段"

## 模块:M-2/M-3 公共子步骤引用
- **路径**:
  - `plugins/code-skills/skills/code-plan/SKILL.md` §步骤 3 / 5 / 21 / 22
  - `plugins/code-skills/skills/code-it/SKILL.md` §步骤 23
- **关键类/函数**:无
- **调用顺序**:M-2 抽"## 公共子步骤:读规范/读上游/探索代码"概念,4 处用 `> 引用:` 块引用;M-3 `code-it` 步骤 23 引用任务分支 9-12
- **状态归属**:无
- **与概要设计的对应**:D-4
- **符合的规范**:`module-conventions §规则 1`
- **关键变更**:
  - M-2:`code-plan` 步骤 3 / 5 → 抽"## 公共子步骤"段,4 处用 `> 引用:`
  - M-3:`code-it` 步骤 23 → 23.1-23.4 共 40 行 → 14 行引用

## 模块:M-4 删除多余逻辑分支
- **路径**:
  - `plugins/code-skills/skills/code-plan/SKILL.md` §步骤 6
  - `plugins/code-skills/skills/code-it/SKILL.md` §步骤 0a.7
- **关键类/函数**:无
- **调用顺序**:`code-plan` 步骤 6 4 种情形 → 3 种情形;`code-it` 步骤 0a.7 E 边界 10 → 6 + 1 表
- **状态归属**:无
- **与概要设计的对应**:D-4
- **符合的规范**:`module-conventions §规则 1`
- **关键变更**:
  - `code-plan` 步骤 6:4 种情形 → 3 种情形
  - `code-it` 步骤 0a.7:10 个 E 边界 → 6 个独立小节 + 1 张职责归属表

## 模块:`code-design` 步骤 0b 简化
- **路径**:`plugins/code-skills/skills/code-design/SKILL.md` §步骤 0b
- **关键类/函数**:无
- **调用顺序**:评估需求规模 → 触发 1-2 个 `AskUserQuestion` → 写"## 设计目标"小节
- **状态归属**:无
- **与概要设计的对应**:D-1
- **符合的规范**:`skill-conventions §规则 1`

## 模块:`code-plan` 步骤 0b 扩展
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 0b
- **关键类/函数**:无
- **调用顺序**:读 `design/.../RESULT.md` 顶部"## 设计目标"小节(沿用)→ 补充 6 维度(扩展性 / 健壮性 / 可维护性 / 封装性 / 可复用性 / 可读性)→ 写"## 设计目标"小节
- **状态归属**:无
- **与概要设计的对应**:D-2
- **符合的规范**:`skill-conventions §规则 1`

## 模块:`code-plan` 任务粒度调整规则 +3 行
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 10A 末尾
- **关键类/函数**:无
- **调用顺序**:任务拆分时读"## 设计目标"小节 → 提取 7 维度优先级 → 调整任务粒度
- **状态归属**:无
- **与概要设计的对应**:D-3
- **符合的规范**:`commit-conventions`(0 派生"更新看板"任务)

## 模块:`--result` / `--plan` 参数预留
- **路径**:`code-require` / `code-design` / `code-plan` SKILL.md 顶部"## 命令行参数解析"小节
- **关键类/函数**:无
- **调用顺序**:本需求**不**实现,留 REQ-00021
- **状态归属**:无
- **与概要设计的对应**:D-6
- **符合的规范**:N/A(本需求 0 改)

## 自检(对照 13 份规范)

- 命名是否符合规范:是(命名沿用既有 `### 步骤 0b` / `### 步骤 0b.0` 格式)
- 目录位置是否符合规范:是(SKILL.md 在 `plugins/code-skills/skills/<name>/` 根目录)
- 依赖方向是否违反规范:否(本需求 0 新增跨技能依赖)
- 是否有被禁止的模式:否(仅在既有 SKILL.md 段内追加锚点 + 归并)
