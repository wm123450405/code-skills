# 风险分析 — REQ-00030

更新时间:2026-06-12 14:31
版本:V0.0.3

## 异常处理

| 异常路径 | 触发条件 | 处理策略 | 监控指标 | 对应任务 |
| --- | --- | --- | --- | --- |
| 模板加载失败 | 模板文件被损坏 / 编码错误 | `code-design` 步骤 8A 询问用户;允许用户重写模板 | (无) | T-002 |
| frontmatter L1-3 误改 | 误删 / 误改 `name` / `description` 字段 | INV-1 字节级保留;`code-check` 校验点 2 派生"概设越界"任务 | `code-check` 派生任务计数 | T-005 |
| 模板章节超出 5/4/4 阈值 | 步骤 9A/10A 生成超阈值表格 | `code-check` 校验点 2 派生"概设越界"任务 | 同上 | T-005 |
| `code-plan` §4-§10 章节缺失 | 步骤 14A 未生成必填章节 | `code-check` 校验点 1 派生"详设缺失"任务 | `code-check` 派生任务计数 | T-005 |
| 架构骨架误触发 / 漏触发 | 5 条件"或"逻辑 bug | `code-check` 人工评审;后续增量修订 | 人工评审 | T-003 |
| 既有 9 个 REQ design / plan 被误改 | 实施时误改 | INV-7 字节级保留;`git status` 校验 | 实施后 `git status` 对比 | T-001 / T-003 |
| 11 个 `code-*` 技能 SKILL.md 被误改 | 实施时误改 | INV-4 字节级保留;`git status` 校验 | 同上 | T-001 / T-003 / T-005 |

## 安全边界

### 鉴权要求

- **不适用**(本仓库无 API / 无鉴权)

### 输入校验

- 模板字段缺失 → `code-design` 步骤 8A 询问用户
- 任务编号格式错误 → `code-check` 校验点 1 标"涉及文件 X 未在 §4-§10 引用"
- 触发/来源枚举错误 → 沿用既有 13 枚举(本需求**不**新增)

### 敏感数据处理

- **不适用**(本仓库无敏感数据)

### 审计日志

- 沿用既有:`commit-conventions.md` 提交前缀 + `git log` 审计
- 本需求落地后:每次实施 commit 形如 `chore(<skill>): REQ-00030 优化 /code-design 与 /code-plan 职责分离`

### 依据规范

- `commit-conventions.md`
- `dashboard-conventions §规则 1`(派生任务同步)

## 性能与资源

### 关键路径耗时目标

- `code-design` 启动 → 概设完成:**不**有严格 P50 / P95 目标(本仓库不涉及性能)
- `code-plan` 启动 → 详设完成:同上

### 并发上限

- 沿用既有:每个 `code-*` 技能串行执行

### 资源限制

- **不适用**(本仓库不涉及内存 / 连接 / 线程)

### 缓存策略

- **不适用**

### 批量/异步

- **不适用**

### 降级策略

- `code-check` 校验点 3(行数比例)即使 ratio > 1.2 也**不**阻断,**仅**标黄警告(FR-7 锁定)
- `code-check` 校验点 1 / 2 派生任务**不**直接阻断,供 `code-it` 处理

## 回退策略

| 触发条件 | 步骤 | 验证 |
| --- | --- | --- |
| 5 个被改文件改动过大,引入 bug | `git revert <commit>` 回退 | `git status` 校验无 dirty |
| `code-plan` 强约束 §4-§10 必填后部分小需求无法填充 | 模板允许"本需求不涉及"显式声明(本设计 §3.4 / §3.5 锁定) | 人工评审 |
| `code-check` 3 校验点误判(派生任务过多) | 校验点仅派生"重构"类型任务,不直接阻断;`code-check` 评审人员可手动忽略 | `code-dashboard` 查看派生任务数 |
| 既有 9 个 REQ 兼容性 | 本设计**不**追溯;新需求应用新规则 | `git diff` 校验既有 9 个 REQ 0 改 |
| 11 个 `code-*` 技能 SKILL.md 受影响 | 严格 INV-3 字节级保留,只**追加**不**重写** | `git diff` 校验 11 个 SKILL.md 0 改 |

## 测试要点(本仓库**不**含测试框架,故测试要点主要是人工评审 + git diff 验证)

### 单元测试

- **不适用**(本仓库无单元测试框架)

### 集成测试

- **不适用**(本仓库无集成测试框架)

### 端到端测试

- **不适用**(本仓库无端到端测试框架)

### 性能/安全测试

- **不适用**(本仓库无性能/安全测试框架)

### 人工评审清单(本仓库"测试"实际是"人工评审")

| 评审项 | 评审方法 | 通过标准 |
| --- | --- | --- |
| INV-1 字节级保留 | `git diff plugins/code-skills/skills/<skill>/SKILL.md` | L1-3 0 变化 |
| INV-2 "## 不要做的事" 字节级保留 | `git diff` | 该小节 0 变化 |
| INV-3 既有章节字节级保留 | `git diff` | 既有步骤 0 变化 |
| INV-4 11 个 `code-*` 技能 SKILL.md 0 改 | `git diff` | 11 个 SKILL.md 0 变化 |
| INV-5 `./assistants/rules/*.md` 0 改 | `git diff` | 7 个规范文件 0 变化 |
| INV-6 `marketplace.json` / `plugin.json` / `CLAUDE.md` / `README*.md` 0 改 | `git diff` | 4 个文件 0 变化 |
| INV-7 既有 9 个 REQ design / plan 0 改 | `git diff` | 9 个 REQ 0 变化 |
| INV-8 0 新增三方依赖 | `git diff` | `package.json` / `requirements.txt` / `go.mod` 0 变化(本仓库无) |
| INV-9 看板字段三方同步 0 触发 | 看板文档 diff | 字段 / 枚举 / 区段 0 变化 |
| FR-1 ~ FR-8 实施完整 | 人工对照 RESULT.md §3.1~§3.8 | 8 个关键设计点全部实施 |
| AC-1 ~ AC-9 全部满足 | 人工对照上游需求 §10 | 9 AC 全部满足 |
| NFR-1 行数收敛(下个新需求) | 落地后 3 个新需求观测 | design ≤ 184 / plan ≥ 340 |
| NFR-2 向下兼容 | 既有 9 个 REQ 0 改 | 通过 |
| NFR-3 frontmatter / 既有章节字节级保留 | `git diff` | 通过 |
| NFR-4 看板字段三方同步 0 触发 | 看板文档 diff | 通过 |
| NFR-5 流程性约束 | 步骤编号 / 锚点保留 | 步骤编号 0 新增 |
| NFR-6 过程文档零副作用 | `module-breakdown.md` ≤ 5 列 | 通过 |
