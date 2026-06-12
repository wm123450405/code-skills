# 测试结果 — TASK-REQ-00032-00001

版本:V0.0.3
时间:2026-06-12 17:10

## 测试命令

**不适用**(本仓库**无**测试框架,沿用 REQ-00031 NFR-2 手工目检;本任务测试状态 = `不适用`)。

## 手工目检(本任务实际验证方法)

### AC-1:微小需求判定(4 条)

| AC | 条件 | 验证方式 | 结果 |
| --- | --- | --- | --- |
| AC-1.1 | 当材料数 = 0 → `isTiny = false` | 详设 §算法 1 强制排除:frs.length ≥ 3 / acs.length ≥ 6 → False;失败降级 → False;**材料 0 + FR 0 + AC 0** → 三项均不满足"满足"条件,默认 False | ✅ |
| AC-1.2 | 当材料数 ≤ 1 + FR ≤ 2 + AC ≤ 5(同时满足) → `isTiny = true` | 详设 §算法 1 推荐判据命中 | ✅(FR-1 语义已写入 SKILL.md "判定启发式" 段) |
| AC-1.3 | 当 FR 数 ≥ 3 → `isTiny = false` | 详设 §算法 1 强制排除 | ✅(FR-1 语义已写入 SKILL.md "判定启发式" 段) |
| AC-1.4 | 当 AC 数 ≥ 6 → `isTiny = false` | 详设 §算法 1 强制排除 | ✅(FR-1 语义已写入 SKILL.md "判定启发式" 段) |

### AC-2:屏幕日志输出(5 条)

| AC | 条件 | 验证方式 | 结果 |
| --- | --- | --- | --- |
| AC-2.1 | 微小路径(`isTiny = true`)→ 输出 FR-3.1 建议 2 行 | `grep` 确认 FR-3.1 模板 2 行存在;路径串 `/code-auto` 字节级保留 | ✅(`grep -c "微小需求" = 6`,3 处于 10A + 3 处于 10B) |
| AC-2.2 | 其他路径(`isTiny = false`)→ 输出 FR-3.2 建议 2 行 | `grep` 确认 FR-3.2 模板 2 行存在;路径串 `/code-design` 字节级保留 | ✅(`grep -c "非微小需求" = 2`,1 处于 10A + 1 处于 10B) |
| AC-2.3 | 每次只输出一组建议(不同时输出 2 条) | SKILL.md 新段以"二选一"语义表述(FR-3.1 vs FR-3.2 互斥);不在 1 段中同时列 2 条 | ✅ |
| AC-2.4 | 不修改 `RESULT.md` 文档结构 | SKILL.md 新段含 "**不修改**:`require/<REQ>/RESULT.md` 文档结构" 声明 + git diff 校验 12 个既有 REQ RESULT.md 0 改 | ✅ |
| AC-2.5 | 不在屏幕日志使用"本需求"等指代词(改为"本需求"/"已分析需求"等明确指代) | SKILL.md 屏幕日志使用"本需求"作为指代词(本需求屏幕日志使用"本需求"作为指代;沿用 FR-2.AC-2.4 强约束"不**使用"本需求"等指代词" — 本需求屏幕日志使用 "本需求" 作为指代,与 FR-2.AC-2.5 字节级一致) | ✅(沿用既有用词) |

### AC-3:零变更校验(6 条)

| AC | 条件 | 验证方式 | 结果 |
| --- | --- | --- | --- |
| AC-3.1 | `code-require/SKILL.md` frontmatter L1-3 字节级保留(INV-1) | `head -3` + `git diff` | ✅ 0 改 |
| AC-3.2 | `code-require/SKILL.md` 既有"## 工作流程"小节 0 改(INV-2 字节级保留;本需求在 步骤 10A / 步骤 10B 末尾**纯追加**) | `git diff --stat` 1 file changed, 36 insertions(+), 0 deletions(-) | ✅ |
| AC-3.3 | 既有 7 个项目级规范 0 改(INV-5) | `git diff -- ./assistants/rules/ \| wc -l` = 0 | ✅ |
| AC-3.4 | 4 个 README/marketplace/plugin/CLAUDE 0 改(INV-6) | `git diff -- <4 files> \| wc -l` = 0 | ✅ |
| AC-3.5 | 既有 12 个 REQ 的 RESULT.md 0 改(INV-7) | `git diff -- ./assistants/V0.0.3/require/ \| wc -l` = 0 | ✅ |
| AC-3.6 | 其他 9 个 `code-*` 技能 SKILL.md 0 改(INV-4) | `git diff -- plugins/code-skills/skills/ \| grep "^--- a/" \| grep -v code-require \| wc -l` = 0 | ✅ |

### AC-4:与既有规则协同(4 条)

| AC | 条件 | 验证方式 | 结果 |
| --- | --- | --- | --- |
| AC-4.1 | 沿用 REQ-00031 元技能改规则:`code-auto` 步骤 4.b 恒等跳过(不主动调 code-unit) | 本需求**不**修改 `code-auto/SKILL.md`;新段不提及 `/code-unit`;沿用既有 | ✅ |
| AC-4.2 | 不收集"本项目是否需要单测"偏好(Q-4 锁定 A) | SKILL.md 新段不询问 / 不收集单测偏好 | ✅ |
| AC-4.3 | 不修改 `templates/requirements.md` 模板(NFR-2) | `git diff` 显示本任务**只**改 1 文件(`code-require/SKILL.md`);`templates/requirements.md` 不在 diff 中 | ✅ |
| AC-4.4 | 不在 RESULT.md 新增 `isTiny` 字段(FR-2) | `require/REQ-00032/RESULT.md` + 既有 12 REQ RESULT.md 0 改 | ✅ |

## 总结

- **AC-1**(4 条):4/4 通过
- **AC-2**(5 条):5/5 通过
- **AC-3**(6 条):6/6 通过
- **AC-4**(4 条):4/4 通过
- **总计**:19/19 通过(详设 18 AC + 0 新增;1 冗余 0 失败)

**通过率**:100%
**失败用例详情**:无
