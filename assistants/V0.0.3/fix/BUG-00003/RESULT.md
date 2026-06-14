# BUG-00003 缺陷详情 — SKILL.md 描述中"绝对路径"在 plugin 安装后断链

## 文档头
- 缺陷编号:BUG-00003
- 严重度:P0(阻断 — plugin 安装后,SKILL.md 中出现的 `plugins/code-skills/...` 绝对路径无法定位,导致引用断裂)
- 报告人:wangmiao
- 报告时间:2026-06-08 14:10
- 状态:修复编码中
- 当前负责人:wangmiao
- 修复时间:—
- 修复人:—
- 修复提交:—
- **与 BUG-00002 关联**:**修复工作合并**(同属"描述性段落去专属化",同一批 Edit)

## 缺陷描述

### 用户原始报告
各技能中引用 references / templates 目录中的文档时应使用相对路径,本技能将发布为 plugin 安装到用户使用环境中,使用本项目路径会导致用户运行时无法定位文件。

### 典型例证
- `code-require/SKILL.md` L530:`不修改 \`plugins/code-skills/skills/*/SKILL.md\` 任何文件`
- `code-design/SKILL.md` L594:同上
- `code-plan/SKILL.md` L1093:同上
- `code-fix/SKILL.md` L433:同上
- `code-unit/SKILL.md` L13:`不得修改 \`plugins/code-skills/skills/*/SKILL.md\` 或其他生产代码文件`
- `code-publish/SKILL.md` L312 / L325 / L361:`Read: plugins/code-skills/skills/code-publish/templates/...`
- `code-publish/SKILL.md` L556:`不要追加 \`plugins/code-skills/CLAUDE.md\` "AI 工作约定"小节`
- `code-rule/SKILL.md` L363:`Read plugins/code-skills/CLAUDE.md 全文`

### 期望行为
plugin 安装后,用户环境中 `plugins/code-skills/...` 路径不存在,SKILL.md 描述与命令示例中所有此类字面均会断链。期望:用相对路径(从 SKILL.md 所在位置出发)或泛用指代代替。

### 实际行为
当前 SKILL.md 中含 `plugins/code-skills/...` 绝对路径字面,plugin 安装后无法定位。

### 复现步骤
1. 假设本仓库 plugin 安装到用户 `~/.claude/plugins/...` 目录
2. 用户执行 `code-rule` 技能,该技能 L363 命令示例 `Read plugins/code-skills/CLAUDE.md 全文`
3. 用户环境中 `plugins/code-skills/CLAUDE.md` 不存在(因安装后 skills 目录结构不同)
4. 命令失败

### 涉及文件/模块
**绝对路径字面(在 SKILL.md / templates 中作为描述、命令示例、引用):**
- `code-require/SKILL.md` L530
- `code-design/SKILL.md` L594
- `code-plan/SKILL.md` L1093
- `code-fix/SKILL.md` L433
- `code-unit/SKILL.md` L13
- `code-publish/SKILL.md` L312 / L325 / L361 / L556
- `code-rule/SKILL.md` L363

共 8 个 SKILL.md 文件 11 处绝对路径字面。

### 根因假设
本项目作为 plugin 发布时,SKILL.md 中的 `plugins/code-skills/...` 字面是"开发视角"的本仓库路径,**不是**"plugin 视角"的相对路径。修复方向:用"相对路径"或"泛用指代"代替,确保 plugin 安装后仍可定位。

## 修复方案
- 旧方案(已废弃):[fix-plan.md](./fix-plan.md)用 `<本仓库>` 占位符
- **新方案**:
  - **使用技能相关的文件**(templates / references)→ **相对路径**(从 SKILL.md 所在位置出发的 `./` 或 `../`)
  - **对用户目标仓库的操作**→ 明确是"用户仓库"语义
  - **不应该有 plugin / code-skills 等路径特点**
  - **`./assistants` 目录**是用户仓库中的项目管理目录,需要在技能中明确使用
- 新方案由 `code-plan BUG-00003` 增量更新产出

## 修复实施
- commit `75297dc`:2 文件 5 处 Edit(code-publish L312/L325/L361/L556 + code-rule L363)
- 0 改 frontmatter
- `marketplace.json` / `plugin.json` / 4 个 README / `CLAUDE.md` 0 diff

## 验证结果
静态校验全部通过(本仓库纯文档,验证手段 = 0 diff 校验)

## 修复日志
- 2026-06-08 14:10  登记  wangmiao 报告缺陷:SKILL.md 描述中"绝对路径"在 plugin 安装后断链
- 2026-06-08 14:15  关联  本缺陷与 BUG-00002(特定文件类型)同属"描述性段落去专属化",修复工作合并
- 2026-06-08 14:45  询问  本轮确认与 BUG-00002 修复合并,剩 5 处命令示例需补修;用户选"保持调查中,先调 code-plan BUG-00003"——状态暂不推进,等待 code-plan 产出 fix-plan.md 后再推进
- 2026-06-08 14:50  修复规划  code-plan 已产出 fix-plan.md(4 步骤,与 BUG-00002 方案统一)
- 2026-06-08 14:55  修复开始  code-it 开始实施修复(2 文件 5 处 Edit)
- 2026-06-08 14:55  修复完成  code-it 完成修复,提交 75297dc,等待验证
- 2026-06-08 15:00  补修发现  wangmiao 指出"未完全修复"——5 处 `<本仓库>` 占位符虽语义统一,但 plugin 安装后解析机制未保证可用;应改用**相对路径**(`./` / `../`);`./assistants` 目录是用户仓库中的项目管理目录,需明确使用。回退到"修复编码中"重新实施方案。

## 变更记录
- 2026-06-08 14:10  缺陷登记  code-fix 创建缺陷 BUG-00003(严重度 P0)  BUG-00003
- 2026-06-08 14:15  状态推进  BUG-00003 状态"报告"→"调查中"(Grep 扫描波及范围完成:8 个 SKILL.md 共 11 处 `plugins/code-skills/...` 绝对路径字面;与 BUG-00002 合并修复)  BUG-00003
- 2026-06-08 14:45  修复日志追加  code-fix 复跑 BUG-00003;本轮状态保持"调查中",等待 code-plan BUG-00003 产出修复方案  BUG-00003
- 2026-06-08 14:50  状态推进  BUG-00003 状态"调查中"→"修复规划中"(code-plan 完成 fix-plan.md;4 步骤)  BUG-00003
- 2026-06-08 14:55  状态推进  BUG-00003 状态"修复规划中"→"修复编码中"(code-it 开始实施)  BUG-00003
- 2026-06-08 14:55  状态推进  BUG-00003 状态"修复编码中"→"已修复-待验证"(commit 75297dc,2 文件 5 处 Edit)  BUG-00003
- 2026-06-08 15:00  状态推进  BUG-00003 状态"已修复-待验证"→"修复编码中"(补修:5 处 `<本仓库>` → 相对路径)  BUG-00003

## 不做边界
- **不**修改 5 个 SKILL.md 中的"`不修改 plugins/code-skills/skills/*/SKILL.md` 任何文件"——这 5 处是**不变量字面**,描述的是"本项目自身管理 skills/ 目录"的硬约束,与本仓库自我管理边界强相关;**保留字面**;本仓库是"开发技能库"必然管理 skills/ 目录。

> **注意**:本边界与 BUG-00002 的"不做边界"完全一致。修复合并后,本轮的"`去掉路径,仅保留泛用指代`"方案**实际上仅作用于命令示例(可改)+ 描述性段(可改)**,不变量字面**保留**。
