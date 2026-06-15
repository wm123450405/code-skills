# 风险分析 — REQ-00034

更新时间:2026-06-15 14:00
版本:V0.0.3

## 异常处理

| 异常场景 | 处理 | 监控 |
| --- | --- | --- |
| E-1(本仓库无项目级规范) | 沿用 `code-require` 既有 `AskUserQuestion` | 屏显 |
| E-2(项目不可测) | `code-it` 步骤 8a 守卫不通过 → 跳过步骤 8.5 → 看板"测试状态"= `不适用` → exit 0 | 屏显 |
| E-3(任务类型 = `文档`) | `code-it` 步骤 8.5 跳过写单测 → 写 `unit-test-results.md` = "本任务不涉及单元测试" | 屏显 |
| E-4(`code-unit` 老用户手动调) | 不可用,屏幕输出"⛔ code-unit 已退场" | 屏显 |
| E-5(历史 `test/<TASK-...>/RESULT.md` 存在) | 字节级保留;`code-check` 评审时**仍**读历史路径 | git diff |
| E-6(历史 `auto-report.md` 含 `code-unit` 跳过日志) | 字节级保留(NFR-2 沿用) | git diff |
| E-7(`code-it` 步骤 8.5 自动判定失败) | 沿用既有"失败 → 屏显 → 中断"逻辑 | 屏显 |
| E-8(`code-it` 步骤 8.5 写单测跑通失败) | 沿用原 `code-unit` 步骤 11 错误修复循环;最连续失败 5 次后必须停下询问用户 | `work-log.md` |

## 安全边界

**不适用**(本设计是元技能改造,无安全变更)

## 性能与资源

**不适用**(本设计是元技能改造,无运行时性能变更)

- **估计净变化**:约 -600 ~ -800 行(技能合并;删除多于新增)
- **`code-it/SKILL.md` 净增**:约 +150 ~ +250 行(守卫 7 项 + 写单测 + 跑通步骤)
- **`code-it` 当前 938 行,加 200 后 ~1138**,仍在 LLM 单次加载阈值内

## 回退策略

- **触发条件**:
  - `code-it` 步骤 8a 守卫 7 项检查与原 `code-unit` 步骤 0a 行为不一致
  - `code-auto` 步骤 4.b 整段删除后,屏幕日志异常
  - 2 JSON 字面删除后,plugin 加载失败
  - 11 技能描述段字面改写后,frontmatter 解析失败
- **步骤**:`git revert <commit-hash>`(单 commit 回退;多 commit 按 `code-plan` 阶段 16A 看板同步顺序回退)
- **验证**:
  - `git diff` 校验 29 个文件全部 0 改
  - `code-unit` 整体不存在
  - 2 JSON 合法性
  - 11 描述段 frontmatter L1-3 字节级保留

## 测试要点

### 单元测试范围
- **不适用**(`code-plan` 不规划单元测试任务,沿用 REQ-00031 FR-2;`code-unit` 退场后 `code-it` 接管)
- 本设计无 `code-unit` 任务(测试状态 = `不适用`)

### 集成测试范围
- **不适用**

### 端到端测试范围
- **不适用**

### 性能/安全测试
- **不适用**

### 校验要点(由 `code-it` 末尾兜底负责 + `code-check` 评审时校验)

| 校验点 | 验证方式 | 预期 | 对应 AC |
| --- | --- | --- | --- |
| `code-unit/SKILL.md` 不存在 | `Bash: test -f ... && echo EXISTS \|\| echo NOT_EXISTS` | NOT_EXISTS | AC-1.1 |
| `code-unit/templates/` 不存在 | `Bash: test -d ... && echo EXISTS \|\| echo NOT_EXISTS` | NOT_EXISTS | AC-1.2 |
| `code-unit/templates/RESULT.md` 不存在 | `Bash: test -f ...` | NOT_EXISTS | AC-1.3 |
| `code-it/SKILL.md` 步骤 8a / 8.5 是**纯新增**段 | `git diff` | 既有 9 步 0 改 | AC-2.1 |
| `code-it` 文档头字面改写 | `git diff` | "不含单元测试" 反向声明 → "含按需写单测" | AC-2.x |
| 11 SKILL.md frontmatter L1-3 字节级保留 | `git diff` | 0 改 | AC-11.2 |
| 既有 12 个 REQ 的 `plan/<REQ>/PLAN.md` 0 改 | `git diff` | 0 改 | AC-12.5 |
| V0.0.2 / V0.0.3 既有 `test/<TASK-...>/RESULT.md` 0 改 | `git diff` | 0 改 | AC-12.1 |
| V0.0.2 / V0.0.3 既有 `auto-report.md` 0 改 | `git diff` | 0 改 | AC-12.3 |
| 2 JSON 合法性 | `python -m json.tool < ...` | 合法 | AC-8.4 |
| `code-fix` 5 候选状态机 0 改 | `git diff` | 0 改 | AC-12.6 |
| `code-dashboard` 12 维度屏显契约 0 改 | `git diff` | 0 改 | AC-12.7 |
