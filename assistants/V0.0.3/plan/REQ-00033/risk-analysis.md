# 风险分析 — REQ-00033

更新时间:2026-06-15 12:30
版本:V0.0.3

## 异常处理

| 异常场景 | 处理 | 监控 |
| --- | --- | --- |
| 材料含技术选型字面(E-1) | `code-require` **不**主动提取;若用户**强提示**,放进"## 12 待澄清" | 屏显 |
| 增量更新(E-2) | 同样触发本硬约束 | 屏显 |
| `code-require` 误产出技术选型(E-3) | `code-check` 评审时由"§不要做的事"小节兜底校验(本需求**不**实现 `code-check` 改造,留作 follow-up) | `code-check` 评审报告 |
| 用户在建议前中断(E-4) | `code-require` 既有"中止"逻辑(本需求不介入) | exit 130 |
| 既有 12 个 REQ 的 RESULT.md 是否受影响 | **无**(INV-7 字节级校验) | git diff |
| `code-it` 步骤 7 写入时位置漂移(E-5) | 锁定措辞;`code-it` 步骤 7 沿用"## 不要做的事" 小节末尾语义锚点 | `code-check` 评审 |

## 安全边界

**不适用**(本设计是 SKILL.md 文字改造,无安全变更)

## 性能与资源

**不适用**(本设计是 SKILL.md 文字改造,无性能变更)

## 回退策略

- **触发条件**:`code-it` 步骤 7 写入后 `git diff` 发现措辞漂移 / 净增行数超 +4 / frontmatter 改变
- **步骤**:`git revert <commit-hash>`(单 commit 回退,无副作用)
- **验证**:`git diff` 校验全部 INV 字节级保留

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

### 校验要点(`code-it` 步骤 13 + `code-check` 评审)

| 校验点 | 验证方式 | 预期 |
| --- | --- | --- |
| `code-require/SKILL.md` §"不要做的事" 新增 1 条 | `Read` + 校验 3 个语义子句 | AC-2.1 全包含 |
| `code-require/SKILL.md` frontmatter L1-3 字节级保留 | `git diff` 校验 | AC-2.2 |
| `code-require/SKILL.md` §"工作流程" 既有段 0 改 | `git diff` 校验 | AC-2.3 |
| 净增行数 +2 ~ +4 行 | `git diff --stat` | AC-2.4 |
| 11 个其他 `code-*` 技能 SKILL.md 0 改 | `git diff` 校验 | AC-3.1 |
| 既有 12 个 REQ 的 RESULT.md 0 改 | `git diff` 校验 | AC-3.2 |
| 12 个项目级规范 0 改 | `git diff` 校验 | AC-3.3 |
| 4 README / CLAUDE.md 0 改 | `git diff` 校验 | AC-3.4 |
| templates/requirements.md 0 改 | `git diff` 校验 | AC-3.5 |
