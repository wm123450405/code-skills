# 未派生任务的发现 — REQ-00001

版本:V0.0.1
时间:2026-06-04 10:35

## 类别:可选

### T-002:F2(CLAUDE.md 目录树图例)
- **位置**:`plugins/code-skills/CLAUDE.md:31-35`
- **类别**:可维护性
- **描述**:CLAUDE.md 目录树图例显示 `code-skills/ ← marketplace 仓库根`,未明确说明"marketplace 标识(`name` 字段)已改为 `code-skills-marketplace`,仅本地目录名保持 `code-skills`"。读者可能误以为"marketplace 名称 = 目录名"。
- **建议**:
  - 在 CLAUDE.md 顶部或目录树图例前加一句说明:
    > 注:`marketplace.json` 根 `name` 字段为 `code-skills-marketplace`(2026-06-03 REQ-00001 落地),与本地目录名 `code-skills` 区分。
  - 或在目录树注释中加 `(marketplace 标识见根 marketplace.json)`
- **不派生任务理由**:
  - 不影响功能,CLAUDE.md 是 AI 协作者参考文档,内容已正确(目录结构本身未变)
  - 属于"完美主义"改进,优先级低
  - 留给未来 PR review 阶段或专门的 `code-rule` 调用
- **授权**:不派生(用户答复"派生 1 任务",F-2 不在派生范围)

## 类别:已知偏离(已记录在 T-004 deviations.md)

- T-004 偏差 1:`doc-conventions.md:113` 正面示例含旧串(规则文件不可改)
- T-004 偏差 2:`V0.0.0/INIT-REPORT.md` 3 处旧串(基线历史)
- T-004 偏差 3:`git push` 未自动执行(网络风险)

这些偏差已由 T-004 详细记录并经评审确认,不需要派生新任务。
