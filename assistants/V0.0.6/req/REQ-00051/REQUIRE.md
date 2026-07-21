# 需求分析 — REQ-00051 · 主 SKILL.md 拆分与 help 子命令化

> 所属版本:V0.0.6
> 创建时间:2026-07-21 15:43

## 0. 用户原始输入

> fix 技能`/code`的`SKILL.md`文件内容过多,合并后所有的技能内容统一放在了这个文件中,应当为每个子命令使用单独的文件进行管控。在主技能文件中引入每个子命令技能文件。主技能文件保留子命令路由能力。同时命令错误的帮助引导功能也应该作为子命令的一种被单独管控,主技能文件只负责路由和引用。

## 1. 需求概述

把 `/code` 主 SKILL.md 中按子命令组织的 6 段(ver / req / fix / faq / rule / merge)正文拆分为各子命令独立的 SKILL.md;主 SKILL.md 仅保留路由能力(首 token 识别 + 分派)。HELP 帮助系统(原 SKILL.md 中 §A / §B / §C / §D 四段)作为独立的 `help` 子命令单独管控,主 SKILL.md 不再承担帮助职责。

## 2. 背景与目标

### 背景

- `/code` 是合并 6 个原独立技能(`/code-ver` / `/code-req` / `/code-fix` / `/code-faq` / `/code-rule` / `/code-merge`)而成的单一入口
- 合并后所有内容写在 `plugins/code-skills/skills/code/SKILL.md` 一个文件里,文件约 90KB
- 文件过大导致:(a) 加载成本高;(b) 各子命令职责边界不清;(c) 维护/审查/迭代效率低
- HELP 帮助系统也作为主 SKILL.md 的一部分,职责杂糅

### 目标

- G-1:每个子命令(ver / req / fix / faq / rule / merge)拥有独立的 `SKILL.md`,承载该子命令的全部流程
- G-2:help 引导能力从主 SKILL.md 抽出,作为独立子命令文件 `help/SKILL.md`
- G-3:主 SKILL.md 仅承担路由职责(§0 不变式 + 首 token 分派 + 子命令文件引用),体积大幅缩减
- G-4:不丢失任何功能 — 现有 6 个子命令的所有 FR/NFR/边界条款在拆分后仍 100% 覆盖
- G-5:不引入历史变更痕迹(沿用上次清理结果,不出现 "原 code-*" 等历史表述)

## 3. 功能需求(FR)

### FR-1: 子命令独立 SKILL.md
- **描述**:为 ver / req / fix / faq / rule / merge 6 个子命令各创建一个独立 SKILL.md,内容从主文件原样迁出
- **输入**:主 SKILL.md 中各子命令对应的章节正文
- **输出**:`plugins/code-skills/skills/code/<子命令>/SKILL.md` × 6
- **来源**:主 SKILL.md

### FR-2: 主 SKILL.md 瘦身(仅路由)
- **描述**:主 SKILL.md 只保留:frontmatter + §0 不变式 + 首 token 路由表 + 引用各子命令文件
- **输入**:主 SKILL.md 当前内容
- **输出**:精简后的主 SKILL.md
- **约束**:必须仍能被 Claude Code 作为 `/code` 入口识别(description 字段保留)

### FR-3: help 引导独立化
- **描述**:原主 SKILL.md 中 HELP 章节(§A 完整 / §B 参数错误 / §C 子命令内部异常下沉 / §D 输出规范)抽到独立的 `help/SKILL.md`,作为 7 号子命令
- **输入**:主 SKILL.md 中 §A / §B / §C / §D
- **输出**:`plugins/code-skills/skills/code/help/SKILL.md`
- **约束**:help 子命令的触发方式需可被 Claude Code description 匹配

### FR-4: 路由机制 — description 字段触发
- **描述**:每个子命令的 SKILL.md 必须在 frontmatter `description` 字段中清晰描述"何时应触发本子命令",Claude Code 通过 description 命中触发
- **输入**:无
- **输出**:7 个 SKILL.md 的 description 字段独立且互斥
- **约束**:description 之间语义边界清晰,无重叠导致误触发

### FR-5: 引用完整性
- **描述**:主 SKILL.md 中如需提及子命令,使用 `<subcommand>` 占位 + 引用子命令 SKILL.md 路径
- **输入**:无
- **输出**:主 SKILL.md 中所有 `references/<X>.md` 引用仍可解析
- **约束**:子命令 SKILL.md 内部引用的 `references/req/*.md` / `references/fix/*.md` / `references/ver/*.md` / `references/faq/*.md` 路径保持不变

### FR-6: 子命令文件组织
- **描述**:子命令 SKILL.md 可放在 `plugins/code-skills/skills/code/<子命令名>/SKILL.md`,也允许平铺 `plugins/code-skills/skills/code-<子命令名>/SKILL.md`(二选一,需在 DESIGN 阶段决策)
- **输入**:无
- **输出**:选定的目录结构
- **约束**:与 Claude Code 的 skill 协议兼容(plugin.json 的 `skills` 数组需正确列出)

### FR-7: plugin.json 与 marketplace.json 更新
- **描述**:`./plugins/code-skills/.claude-plugin/plugin.json` 的 `skills` 字段以及 `./.claude-plugin/marketplace.json` 的 `skills` 字段需要列出新增的子命令入口
- **输入**:拆分方案
- **输出**:更新后的 plugin.json + marketplace.json
- **约束**:Claude Code 仍能将 `/code` / `/code ver` / `/code req` 等命令正确识别

## 4. 非功能需求(NFR)

| 编号 | 类型 | 描述 | 约束 |
| --- | --- | --- | --- |
| NFR-1 | 可维护性 | 主 SKILL.md 体积 | 拆分后主 SKILL.md ≤ 10KB(原 ~90KB) |
| NFR-2 | 可维护性 | 单文件职责 | 每个 SKILL.md 单一职责(路由 / ver / req / fix / faq / rule / merge / help) |
| NFR-3 | 完整性 | 行为对齐 | 拆分前后 6 个子命令的行为 100% 一致,无任何条款丢失 |
| NFR-4 | 兼容性 | 调用语法 | `/code ver` / `/code req "<描述>"` 等现有调用语法保持不变 |
| NFR-5 | 一致性 | 命名 | 子命令目录命名严格小写,与首 token 完全一致(ver / req / fix / faq / rule / merge / help) |
| NFR-6 | 可读性 | 历史痕迹 | 拆分后不出现 "原 code-* 技能" "合并前" 等历史表述 |
| NFR-7 | 可发现性 | description 命中 | 各子命令的 description 字段独立完整,描述"用户何时该调它" |
| NFR-8 | 鲁棒性 | 错误处理 | 当用户输入不可识别子命令时,主 SKILL.md 仍能正确指向 help 子命令文件 |

## 5. 验收标准(AC)

| 编号 | 描述 | 验证方式 |
| --- | --- | --- |
| AC-1 | 7 个子命令 SKILL.md(ver / req / fix / faq / rule / merge / help)各自独立存在 | 目录遍历 + 文件存在性检查 |
| AC-2 | 主 SKILL.md 不再包含任何子命令的详细流程(仅路由) | grep 验证关键字(`步骤 1 REQUIRE` / `看板模式` / `worktree 模式识别` 等子命令专属段落不在主文件中) |
| AC-3 | 主 SKILL.md 体积 ≤ 10KB | `wc -c` 或文件大小 |
| AC-4 | 6 个子命令的现有所有 FR/NFR/边界/不要做的事条款在各自 SKILL.md 中完整保留 | 逐子命令对照清单 |
| AC-5 | plugin.json 与 marketplace.json 的 `skills` 字段列出全部入口 | JSON 解析 + 字段比对 |
| AC-6 | description 字段无重叠语义(命中测试) | 模拟 5 类用户输入,确认每次只有一个子命令被触发 |
| AC-7 | 无历史表述残留 | grep 验证关键字(`code-ver` / `code-req` / `原技能` / `合并前`)在拆分后文件中的出现 |

## 6. 关联需求

| 需求编码 | 版本 | 关联点 | 影响 |
| --- | --- | --- | --- |
| REQ-00050 | V0.0.6 | 上次清理历史 `/code-*` 引用 | 本次拆分不能再次引入历史表述,需复用清理结果 |

## 7. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-21 15:43 | v1 | 初始创建 | 需求分析完成 | wm |
