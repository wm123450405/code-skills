# 材料登记 — REQ-00003
更新时间:2026-06-03 20:45
版本:V0.0.1

## 项目级规范
继承 `code-design` 阶段(本需求尚在 `code-require` 阶段)对 `./assistants/rules/` 的认知;本需求不新增任何规范文件,仅扩展 `code-rule` 技能本身。

| 规范文件 | 与本需求的关系 |
| --- | --- |
| `dashboard-conventions.md` | 间接相关 — 本需求不在看板字段约定上做扩展(仅新增 1 条 `code-rule` 技能触发的"任务清单"行,无新字段) |
| `doc-conventions.md` | 弱相关 — 本需求新增的 SKILL.md 章节与模板提示需遵循"中英对仗"(若本仓库加英文版) |
| `marketplace-protocol.md` | 不触发 — 本需求不修改 `marketplace.json` / `plugin.json` |
| `module-conventions.md` | 弱相关 — 与本需求 FR-2 的 C-4"目录与模块规范"可能重叠(详见 Q-4) |
| `skill-conventions.md` | 强相关 — 本需求修改 `code-rule` 自身 SKILL.md,需遵循其 §规则 1(frontmatter 必含 `name` + `description`) |

## 上游需求
- **本需求的源材料**(用户原始输入):
  > 优化 `/code-rule` 技能,增加不同类型的核心编码规范的解析或引导。
  > 示例:对 CLAUDE.md 增加说明、对模板(requirements/design/plan/templates)提供内容提示等。
- 提取的 FR / NFR / AC 数量:10 FR / 6 NFR / 10 AC
- 待澄清:5 项(Q-4 ~ Q-8),均非阻塞;3 项已锁定(Q-1 ~ Q-3,2026-06-03 20:35)

## 项目现状(本次扫描)

### 项目类型
- Claude Code marketplace + 单 plugin:`code-skills`
- 仓库结构:marketplace 根 + `plugins/code-skills/`(10 个 code-* 技能)
- 本需求聚焦:**`code-rule` 技能**(位于 `plugins/code-skills/skills/code-rule/`)

### 关键文件清单
| 文件路径 | 状态 | 与本需求的关系 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-rule/SKILL.md` | 已有 | 本需求主修改目标(扩展技能定义) |
| `plugins/code-skills/skills/code-rule/templates/rule.md` | 已有 | 本需求主修改目标(可能扩展/新增变体模板,适配 Type B/C) |
| `plugins/code-skills/skills/code-rule/templates/assistants-layout.md` | 已有 | 不修改 |
| `./assistants/rules/*.md`(5 个现有) | 已有 | 本需求**不修改**(FR-9);但 Type A 流程需识别这些分类 |
| `./assistants/rules/<新分类>.md`(6 个新分类) | 不存在 | 本需求 Type A 处理时可能创建(FR-2 / FR-3 / FR-4) |
| `plugins/code-skills/CLAUDE.md` | 已有 | 本需求 Type B 处理目标(FR-5) |
| `plugins/code-skills/skills/<技能>/templates/*.md`(15+ 个) | 已有 | 本需求 Type C 处理目标(FR-6) |
| `plugins/code-skills/skills/<其它 9 个 code-*>/SKILL.md` | 已有 | 本需求**不修改**(FR-9) |
| `.claude-plugin/marketplace.json` | 已有 | 本需求**不修改**(FR-9) |
| `plugins/code-skills/.claude-plugin/plugin.json` | 已有 | 本需求**不修改**(FR-9) |

### 编码与构建约定
- 无源代码;本需求修改的是 Markdown 技能定义与模板
- 技能 frontmatter 必含 `name` + `description`(`skill-conventions.md §规则 1`)

### 可复用资产
- `code-rule` 现有 SKILL.md 的"分类识别"步骤可直接扩展,支持 6 个新分类(FR-2)
- `code-rule` 现有 `templates/rule.md` 模板可作为 Type A 的模板基础
- CLAUDE.md 现有结构(7 个二级小节)可作为 Type B 追加位置的参考(在文件末尾新增"## AI 工作约定"小节)

### 关键观察
1. `code-rule` 当前**完全没有 Type B/C 的概念**;扩展时需从零设计这两种类型的内容结构
2. 现有 5 个规范文件命名风格 kebab-case + `<主题>-conventions.md`;新增 6 个分类应保持一致
3. CLAUDE.md 现有 7 个二级小节是"仓库结构 / 约定 / 技能编写指南"等基础设施,**不应**被 Type B 改动;Type B 必须在文件末尾新增独立小节
4. 现有 templates/*.md 文件都是长文档(400+ 行);Type C 末尾追加"## 提示"小节,应放在文件最后;Type C 内联需精确匹配二级标题

## 本次变更源(增量更新时)
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | (无变化,v1 已锁定 FR/NFR/AC) | — |
| 设计侧 | (待 code-design 阶段) | — |
| 规范侧 | (无变化) | — |
| 代码侧 | (本需求修改 code-rule SKILL.md 与 templates/rule.md,无应用代码) | — |
