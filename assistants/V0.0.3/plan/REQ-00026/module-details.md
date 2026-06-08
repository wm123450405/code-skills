# 模块详细化 — REQ-00026
更新时间:2026-06-08 12:45
版本:V0.0.3

> **本仓库是纯文档仓库,无源代码模块。** 本文件中"模块"指代 SKILL.md / templates 等 Markdown 文档,职责是"承载技能的契约文本"。

## 模块 1:code-require/SKILL.md
- **路径**:`plugins/code-skills/skills/code-require/SKILL.md`
- **关键修改区段**(描述性段):
  - 顶部"YAML frontmatter description"段(若含 `plugins/code-skills/...` 字面)
  - §适用场景 / §工作目录约定 / §工具使用约定 / §工作流程 各段中引用 `plugins/code-skills/...` 路径
  - 末尾兜底提交步骤中 `git diff` 命令的"目标路径"行(若含 `plugins/code-skills`)
- **不修改区段**:frontmatter `name` / `description` 字段值;§适用场景 中的不变量行;AC/INV 列表
- **关键决策**:每个被改 SKILL.md 顶部"概述段"加一句"`<本仓库>` 指代本 marketplace 仓库的根目录"
- **对应 FR**:FR-1
- **符合规范**:`skill-conventions.md §规则 1`(frontmatter 不变)

## 模块 2:code-design/SKILL.md
- 同 §1 结构,典型命中点:§"工作目录约定" 中的"项目根" 描述 / §"修改文件定位的语义化约定" 概述
- **对应 FR**:FR-1

## 模块 3:code-plan/SKILL.md
- 同 §1 结构,典型命中点:§"工作目录约定" / §"工具使用约定"
- **对应 FR**:FR-1

## 模块 4:code-it/SKILL.md
- 同 §1 结构,典型命中点:§"工作目录约定" / §"上下游衔接"
- **对应 FR**:FR-1

## 模块 5:code-unit/SKILL.md
- 同 §1 结构,典型命中点:§"工作目录约定"
- **对应 FR**:FR-1

## 模块 6:code-check/SKILL.md
- 同 §1 结构,典型命中点:§"工作目录约定"
- **对应 FR**:FR-1

## 模块 7:code-fix/SKILL.md
- 同 §1 结构,典型命中点:§"工作目录约定"
- **对应 FR**:FR-1

## 模块 8:code-publish/SKILL.md
- 同 §1 结构,典型命中点:§"工作目录约定" / §"上下游衔接" / §"工具使用约定"
- **对应 FR**:FR-1

## 模块 9:code-rule/SKILL.md
- 同 §1 结构 + 3 处硬替换点(L336 / L363 / L370 的"追加到 `plugins/code-skills/CLAUDE.md`" → "追加到 `<本仓库>/CLAUDE.md`")
- **对应 FR**:FR-1 + FR-5

## 模块 10:code-init/SKILL.md
- 同 §1 结构,典型命中点:§"工作目录约定"
- **对应 FR**:FR-1

## 模块 11:code-publish/templates/DEPLOY.md
- **路径**:`plugins/code-skills/skills/code-publish/templates/DEPLOY.md`
- **关键修改区段**:L3 头部 `> ⚠ **本手册为通用发布部署骨架**,由 \`code-publish\` 技能从 \`plugins/code-skills/skills/code-publish/templates/DEPLOY.md\` 复制生成` → 把 `plugins/code-skills/skills/...` 替换为 `<本仓库>/skills/...`
- **对应 FR**:FR-4

## 模块 12:code-publish/templates/UPDATE.md
- 同 §11
- **对应 FR**:FR-4

## 模块 13:code-publish/templates/qanda-README.md
- **关键修改区段**:L133 "草稿应该放项目内的 `drafts/` 子目录" 段(语义保持,字面替换)
- **对应 FR**:FR-4

## 模块 14:code-init/templates/INIT-REPORT.md
- **关键修改区段**:
  - L3 "本报告由 `code-init` 技能生成,作为新成员(包括 AI Agent)快速理解本项目的入口" → "本仓库"
  - L8 "<一两句话说明本项目做什么,服务什么用户,解决什么问题>" → "本仓库"(占位符语义不变,字面改)
- **对应 FR**:FR-4

## 关键决策总结
- **改 14 个模块**:10 SKILL.md + 3 templates + 1 INIT-REPORT
- **0 改 frontmatter**
- **0 改 AC / INV / 命令示例**
- **0 改 marketplace.json / plugin.json / README / CLAUDE.md**
