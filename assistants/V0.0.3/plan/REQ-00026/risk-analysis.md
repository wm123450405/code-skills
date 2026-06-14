# 风险分析 — REQ-00026
更新时间:2026-06-08 12:45
版本:V0.0.3

## 异常处理
**N/A**(本需求无运行时异常)

## 安全边界
**N/A**(本需求无运行时安全面)

## 性能与资源
**N/A**(本需求无运行时性能)

## 回退策略
- **触发条件**:改动后发现某 SKILL.md 描述被破坏可读性 / 与既有功能脱节
- **步骤**:
  1. `git revert` 本次 commit
  2. 重新审视该 SKILL.md 的"描述性 vs 硬约束"边界
  3. 增量回填
- **验证**:
  - `git diff HEAD~1 -- plugins/code-skills/skills/<skill>/SKILL.md` 应恢复原状
  - 重新跑 `code-check REQ-00026`(若有)校验 0 残留问题

## 测试要点
- **N/A**(本仓库无源代码,无单元测试)
- **静态校验**:
  - 10 SKILL.md 的 frontmatter 字节级一致(`name` / `description` 字段值不变)
  - `git diff --stat` 改动文件清单 = 14 个目标文件
  - `git diff marketplace.json plugin.json README*.md CLAUDE.md` 全 0
  - 旧需求档案 `git diff` 0
- **人工 review**:
  - 每个被改 SKILL.md 的"概述段"首句可读性
  - 占位符 `<本仓库>` 含义对读者清晰

## 风险
| 风险 | 可能性 | 影响 | 缓解 |
| --- | --- | --- | --- |
| 半改半留(同文件内"plugins/code-skills" 既出现在描述段也出现在 INV 段,描述段改了 INV 段没改 → 不一致) | 中 | 中 | `code-it` 阶段按"段级 grep + 段落标题"二分类,确保描述段全改、INV 段全保留 |
| 改 frontmatter 误删 description | 低 | 高 | `code-it` 阶段用 `Read` 校验 frontmatter 字节级,任何差异立即中止 |
| 旧需求档案被误改 | 极低 | 中 | `code-it` 阶段 `git diff` 校验,本需求不涉及 |
