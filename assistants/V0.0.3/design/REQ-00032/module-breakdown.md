# 模块拆分 — REQ-00032

更新时间:2026-06-12 16:20
版本:V0.0.3

## 1. 总体说明

本需求**只改造 1 个文件**:`plugins/code-skills/skills/code-require/SKILL.md`。

不新增模块,不修改模块边界,不修改 `plugins/code-skills/skills/code-require/` 目录结构。

## 2. 模块清单(本需求涉及)

| # | 模块名 | 路径 | 状态 | 职责 | 对外契约 | 依赖 | 关键决策 | 规范依据 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | code-require 屏幕日志建议段(虚拟模块) | `plugins/code-skills/skills/code-require/SKILL.md` > 步骤 10A 段内文末 | **修改既有** | 在 code-require 完成需求分析后,屏幕输出"下一步建议" | 屏幕日志(2 行字符串) | code-require 步骤 10A 既有流程 | D-2 段内文末追加,不引入新步骤编号 | `skill-conventions.md §规则 1` 字节级保留 frontmatter |
| 2 | code-require 屏幕日志建议段(虚拟模块) | `plugins/code-skills/skills/code-require/SKILL.md` > 步骤 10B 段内文末 | **修改既有** | 在 code-require 增量更新完成后,屏幕输出"下一步建议" | 屏幕日志(2 行字符串) | code-require 步骤 10B 既有流程 | 同上 | 同上 |

## 3. 自检结果

对照 `module-conventions.md` 逐条检查:

| 自检项 | 结果 |
| --- | --- |
| 命名是否符合规范 | ✅ 本需求**不新增**模块名,沿用 `code-require` 目录名 |
| 目录位置是否符合规范 | ✅ 改造位置在 `plugins/code-skills/skills/code-require/SKILL.md` |
| 依赖方向是否违反规范 | ✅ 无新增依赖(仅修改既有 SKILL.md 文档) |
| 是否有被禁止的模式 | ✅ 无 |

## 4. 模块边界

### 4.1 本次需求**不**修改的模块

- 既有 9 个 `code-*` 技能 SKILL.md(`code-design` / `code-plan` / `code-it` / `code-unit` / `code-check` / `code-fix` / `code-init` / `code-version` / `code-rule` / `code-auto`)(INV-4)
- `code-require/templates/requirements.md`(NFR-2 零规范变更)
- `code-require/SKILL.md` frontmatter L1-3(INV-1 字节级保留)
- 7 个项目级规范(INV-5)
- 既有 12 个 REQ 的 RESULT.md(INV-7)
- 4 个 README/marketplace/plugin/CLAUDE(INV-6)

### 4.2 本次需求**修改**的模块

- `code-require/SKILL.md`:
  - **步骤 10A 段内文末**追加 1 段"### 下一步建议(本需求 REQ-00032 新增,2026-06-12 起生效)"
  - **步骤 10B 段内文末**追加 1 段"### 下一步建议(本需求 REQ-00032 新增,2026-06-12 起生效)"
  - 既有"向用户汇报"段、frontmatter、章节标题 0 改

## 5. 模块图(架构示意)

```
┌────────────────────────────────────────────┐
│ code-require/SKILL.md                      │
│                                            │
│  步骤 10A — 完善过程文档  ← 末尾追加       │
│    ├ 既有"向用户汇报"段 (0 改)            │
│    └ [本需求新增]"### 下一步建议"段        │
│                                            │
│  步骤 10B — 汇报           ← 末尾追加       │
│    ├ 既有"向用户汇报"段 (0 改)            │
│    └ [本需求新增]"### 下一步建议"段        │
│                                            │
│  步骤 N — 末尾兜底提交 (0 改)              │
│  其他步骤 (0 改)                           │
└────────────────────────────────────────────┘

↑ ↓

┌────────────────────────────────────────────┐
│ 屏幕日志输出(运行期)                       │
│   → 下一步建议:本需求判定为"微小需求"...   │
│     提示:code-auto 会自动跳过...           │
│   或                                        │
│   → 下一步建议:本需求判定为"非微小需求"... │
│     提示:概设完成后,code-plan ...          │
└────────────────────────────────────────────┘
```

## 6. 关键变更

| 文件 | 锚点 | 变更类型 | 变更描述 |
| --- | --- | --- | --- |
| `code-require/SKILL.md` | 步骤 10A 段内文末 | **纯追加** | 新增 1 段"### 下一步建议" |
| `code-require/SKILL.md` | 步骤 10B 段内文末 | **纯追加** | 新增 1 段"### 下一步建议" |

**不涉及**:
- 删除既有段
- 修改既有字段
- 重命名章节
- 新增/删除/重命名目录
