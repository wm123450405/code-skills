# 模块拆分 — REQ-00039

更新时间:2026-06-22 14:30
版本:V0.0.3

| 模块名 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| `logic-loc.md` | `plugins/code-skills/skills/code-it/lib/logic-loc.md` | **新增** | 共享库:逻辑行计算函数(`detectLocTool` / `calcLogicLines` / `heuristicLoc` / `code-check-exceed`) | 无 |
| `logic-loc-defaults.md` | `plugins/code-skills/skills/code-it/lib/logic-loc-defaults.md` | **新增** | 阈值默认值(单文件 ≤ 500 行总规模 / ≤ 200 行新增) | `logic-loc.md` |
| `code-it/SKILL.md` | `plugins/code-skills/skills/code-it/SKILL.md` | **修改既有**(步骤 8 末尾追加 2 子步骤) | 实施开发末尾新增 `detectLocTool` + `calcLogicLoc` 子步骤;屏显契约"=== code-it 逻辑行统计 ===" | `logic-loc.md` |
| `code-check/SKILL.md` | `plugins/code-skills/skills/code-check/SKILL.md` | **修改既有**(步骤 8.13 新增 + 评审维度速查表新增第 13 维度) | 评审派生"代码行数超标"发现 | `logic-loc.md` |
| `code-it/templates/RESULT.md` | `plugins/code-skills/skills/code-it/templates/RESULT.md` | **修改既有**(新增"## 逻辑行统计"小节示例) | 模板示例展示逻辑行 metadata 格式 | 无 |

**自检**(对照 `module-conventions.md`):

- **命名**:模块名 `logic-loc` + `logic-loc-defaults` 符合 kebab-case 约定 ✓
- **目录位置**:`code-it/lib/` 而非 `code-it/templates/`(沿用既有 `module-conventions.md` §规则 1 `templates/` 留作历史不删 — 新模块在 `lib/`) ✓
- **依赖方向**:`code-it` / `code-check` → `code-it/lib/logic-loc.md`(单向依赖,无循环) ✓
- **禁止模式**:无被禁止的循环依赖 / 跨层调用 ✓

**模块数 = 5**(≥ 2 → 满足 `module-breakdown.md` 生成准则)