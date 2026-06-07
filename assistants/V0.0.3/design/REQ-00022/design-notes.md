# 设计笔记 — REQ-00022
更新时间:2026-06-07
版本:V0.0.3

## 关键设计问题清单

| # | 设计问题 | 选定方案 |
| --- | --- | --- |
| **Q-1** | 技能入口重命名策略 | 硬重命名(`git mv` + 改 frontmatter + 改 H1) |
| **Q-2** | JSON 同步策略 | 全部同步改(`skills[]` + `keywords[]` + `description`) |
| **Q-3** | docs 同步策略 | 全部同步改(25 文件) |
| **Q-4** | 历史产物处理 | 不追溯(V0.0.0/V0.0.1/V0.0.2/V0.0.3 review) |
| **Q-5** | 产出物类型目录 | `review/` 目录名保留(产出物类型,不是技能名) |
| **Q-6** | 中文表述 | 不强求统一(代码评审/代码检查可共存) |

## 关键设计决策(本需求 N=6 项)

| # | 决策 | 选定方案 | 备选 + 否决理由 | 依据规范 |
| --- | --- | --- | --- | --- |
| **D-1** | 技能入口重命名策略 | **硬重命名** | A. 软重命名(保留 `/code-review` 别名)— 否决,违反 `skill-conventions §规则 1`;B. 硬重命名(选定) | `skill-conventions §规则 1` |
| **D-2** | JSON 同步策略 | **全部同步改** | A. 只改 `skills[]` 路径 — 否决,产品语义混乱;B. 全部同步改(选定) | `marketplace-protocol §规则 1` |
| **D-3** | docs 同步策略 | **全部同步改** | A. 只改 SKILL.md + JSON,docs 留 follow-up — 否决,后续 PR 混乱;B. 全部同步改(选定) | `doc-conventions §规则 1` |
| **D-4** | 历史产物处理 | **不追溯** | A. 历史产物也同步改 — 否决,破坏 git 历史;B. 不追溯(选定) | `migration-mapping §规则 5` |
| **D-5** | 产出物类型目录 | **`review/` 目录名保留** | A. 同步改 `review/` → `check/` — 否决,破坏 V0.0.2 历史;B. 保留(选定) | 沿用既有约定 |
| **D-6** | 中文表述 | **不强求统一** | A. 全部改"代码检查" — 否决,过度约束;B. 不强求(选定) | 尊重用户原文 |

## 候选方案权衡(已锁定)

### 方案 A:仅改 SKILL.md frontmatter(不推荐)
- 优点:变更面最小(1 个文件)
- 缺点:违反 `skill-conventions §规则 1`(`name: code-check` 但目录名 `code-review/`)
- 决策:**不采纳**

### 方案 B:硬重命名(目录 + SKILL.md + JSON + docs)
- 优点:严格遵循 `skill-conventions §规则 1` + `marketplace-protocol §规则 1` + `doc-conventions §规则 1`;零歧义
- 缺点:用户需主动改输入习惯(/code-review 报错);约 38-39 文件改动
- 决策:**采纳**

### 方案 C:软重命名(目录 + SKILL.md + 别名)
- 优点:向后兼容
- 缺点:需要双 frontmatter 或 symlink 机制;`skill-conventions §规则 1` 不接受双 `name`
- 决策:**不采纳**

## 不变量(本需求 INV=9 条)

详 `RESULT.md` §3.3

## 下一轮要深挖的方向
- (本需求为"字面量重命名",无 follow-up 必要)
