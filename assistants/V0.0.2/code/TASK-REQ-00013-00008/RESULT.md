# 改修总结 — TASK-REQ-00013-00008
- **任务编码**:TASK-REQ-00013-00008
- **标题**:`[修改] code-publish/SKILL.md 增量追加(报告未完成项格式升级)`
- **类型**:修改(协同) / 完成时间:2026-06-05 21:30 / 完成人:wangmiao
- **文件**:`plugins/code-skills/skills/code-publish/SKILL.md` (+约 80 行,锚点 = "### 步骤 1:PreflightChecker > #### 1.4 决策 > 异常路径 > #### 1.5 报告格式升级")
- **关键变更**:
  1. 在 PreflightChecker 章节末尾(### 步骤 2.0 前)追加"#### 1.5 报告格式升级 — 未完成项"编号+标题" (REQ-00013 新增)"
  2. 工具函数:`truncateTitle` / 3 个 `formatXxxTitle`
  3. 解析函数:`parseResultTitle` / `parsePlanTaskTitle` / `parseFixTitle`
  4. 报告"未完成项"行格式升级(原 `REQ-NNNNN 状态=...` → 新 `REQ-NNNNN · <需求标题> 状态=...`)
- **不**修改看板"任务清单" / "需求清单" / "缺陷清单" 3 区段解析逻辑
- **不**修改 `ReportFormatter` 既有"未通过"模板的字段
- **不**修改 `code-publish` 自身 0 commit 行为(NFR-3)
- **字节级保留**:✅ L1-3 frontmatter / 原"#### 1.4 决策" / "**异常路径**" / "### 步骤 2.0" 章节标题
- **偏离**:**0 项** / **8 项 INV 自检**:**100% 通过**
- **提交哈希**:留 dirty tree
