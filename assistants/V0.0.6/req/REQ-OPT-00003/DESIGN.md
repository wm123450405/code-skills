# 软件设计 — REQ-OPT-00003 · 移除板块标题序号,引用处同步改为板块标题

> 所属版本:V0.0.6
> 创建时间:2026-07-24 11:25

## 1. 设计概述

清理 28 个 .md 文件的板块标题序号(## N. / ### N.M / ## §N / ### §N.M / #### Na / #### Na-N 等),并将正文 §-引用同步改为板块标题文字。

## 2. 模块拆分

### 2.1 替换规则

| 形态 | 原样 | 清理后 |
|------|------|--------|
| 数字点序 | `## 1. 缺陷描述` | `## 缺陷描述` |
| 数字点层级 | `### 1.2 强制结构` | `### 强制结构` |
| § 序 | `## §1 参数解析` | `## 参数解析` |
| § 层级 | `### §2.1 搜索范围` | `### 搜索范围` |
| 字母序 | `#### 9a 扩展性确认` | `#### 扩展性确认` |
| 字母-数字 | `#### 5a-1 技术选型过滤` | `#### 技术选型过滤` |
| 正文引用 | `详见 §3.4` | `详见「模板填充」` |
| 正文引用 | `DESIGN.md §1` | `DESIGN.md 的「设计概述」` |

### 2.2 文件清单(28 个)

| # | 文件 | 标题数 | 引用数(估) | 类型 |
|---|------|--------|-----------|------|
| 1 | `_shared/contracts.md` | 22 | 8 | 契约层 |
| 2 | `references/req/coding.md` | 12 | 5 | 步骤详细 |
| 3 | `references/req/design.md` | 11 | 4 | 阶段流程 |
| 4 | `references/req/require.md` | 11 | 6 | 阶段流程 |
| 5 | `references/req/plan.md` | 3 | 5 | 阶段流程 |
| 6 | `references/merge/SKILL.md` | 3 | 2 | 技能入口 |
| 7 | `references/ver/SKILL.md` | 0 | 25 | 技能入口(仅引用) |
| 8 | `references/ver/common.md` | 9 | 8 | 详细流程 |
| 9 | `references/faq/SKILL.md` | 2 | 14 | 技能入口 |
| 10 | `references/faq/common.md` | 4 | 35 | 详细流程 |
| 11 | `references/runtime-environment.md` | 6 | 6 | 详细流程 |
| 12 | `references/req/common.md` | 11 | 5 | 详细流程 |
| 13 | `references/fix/fix-register.md` | 0 | 12 | 详细流程 |
| 14 | `references/req/languages/*.md`(6 个) | 48 | 5 | 语言适配 |
| 15 | `templates/req/REQUIRE.md` | 8 | 0 | 模板 |
| 16 | `templates/req/DESIGN.md` | 9 | 0 | 模板 |
| 17 | `templates/req/TASK.md` | 5 | 0 | 模板 |
| 18 | `templates/req/CHECK.md` | 0 | 1 | 模板(仅引用) |
| 19 | `templates/req/PLAN.md` | 0 | 0 | 模板 |
| 20 | `templates/fix/BUG.md` | 5 | 0 | 模板 |
| 21 | `templates/fix/...` | - | - | 见 §2.3 |
| 22 | `templates/faq/REQUIRE-EXPORT.md` | 6 | 0 | 模板 |
| 23 | `templates/faq/DESIGN-EXPORT.md` | 6 | 0 | 模板 |
| 24 | `templates/faq/SUMMARY-EXPORT.md` | 3 | 0 | 模板 |
| 25 | `templates/ver/RESULT.md` | 0 | 2 | 模板(仅引用) |
| 26 | `SKILL.md`(主) | 0 | 8 | 主入口(仅引用) |
| 27 | `references/rule/SKILL.md` | 0 | 2 | 技能入口(仅引用) |
| 28 | `references/fix/SKILL.md` | 0 | 4 | 技能入口(仅引用) |

### 2.3 templates/fix 完整清单

`templates/fix/BUG.md` 5 个标题。`templates/fix/` 下其他文件如有带序号标题,扫描阶段已全部识别。

## 3. 接口设计

无接口变更。本次为纯文档清理。

## 4. 数据设计

无数据变更。

## 5. 关键流程

### 5.1 替换流程(每个文件)

```
1. Read 文件 → 列出所有匹配 ^#+\s+(\d+(\.\d+)*|§\d+(\.\d+)*|[a-z]-\d+|[a-z])\s 的标题行
2. 对每个标题行构造 old_string 与 new_string
3. 列出所有正文 § 引用(非标题行),按上下文确认替换目标
4. 一次性 Edit 替换所有标题(用 replace_all=true 按行替换)
5. 一次性 Edit 替换所有正文引用(按映射表)
6. Read 文件验证 grep ^#+\s+(\d|§) 命中数 = 0
7. 验证 grep §\d (非标题行) 命中数 = 0
```

### 5.2 引用映射原则

对每个 § 引用,在被引用文件中查找对应标题文字:
- 若唯一 → 直接替换为标题文字
- 若同名多个 → 按上下文选最相关;若仍歧义,在标题文字前加限定(如"ver §8.6 高优先级缺陷统计"→"ver 的「高优先级缺陷统计」(§8.6)" 改为"ver 的「高优先级缺陷统计」")
- 若无对应标题(§ 引用已删除的旧标题)→ 标注"⚠ 引用已无对应板块"待人工处理

### 5.3 验证流程

替换完成后:
1. `grep -rn '^#+\s+\d' plugins/code-skills/skills/code/` → 0 命中
2. `grep -rn '^#+\s+§' plugins/code-skills/skills/code/` → 0 命中
3. `grep -rn '§\d' plugins/code-skills/skills/code/`(排除 § 开头标题)→ 0 命中
4. README.md / README.en.md 顶部 # 1./2./3. 仍存在
5. FR-/NFR-/AC-/E-/INV-/TASK-/BUG-/REQ- 编号未变

## 6. 方案选型

### 6.1 方案 A:逐项预览 + 单文件 Edit(选定)

- **做法**:为每个文件先输出"原标题/引用 → 新标题/引用"对照表,等用户一次性确认后批量执行
- **优点**:可控、可回滚、用户全程参与
- **缺点**:周期长(28 个文件)

### 6.2 方案 B(已否决)

- 自动化脚本(正则)批量替换 → 风险高,跨文件语义易丢

### 6.3 方案 C(已否决)

- 分批:先 5 个文件 → 用户验收 → 再 23 个 → 用户验收

## 7. 规范合规

- ✅ 不修改 `./assistants/rules/`
- ✅ 不修改 `RESULT.md`(仅在 INIT 阶段追加需求清单一行)
- ✅ CWD 源码修改仅在 CODING 阶段执行
- ✅ 不引用 REQ-OPT-00003 编号到源码注释

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-24 11:25 | v1 | 初始创建 | 软件设计完成;危险操作(大范围跨文件)已用户逐项预览策略确认 | wangmiao |