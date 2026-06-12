# 材料登记 — REQ-00032

更新时间:2026-06-12 16:05
版本:V0.0.3

## 1. 项目级规范

(本节沿用 code-require 既有约束,无新增)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| encoding-conventions.md | 编码 | 5 位纯数字生成端;接收端可放宽;需求编号 5 位 |
| naming-conventions.md | 命名 | kebab-case 目录;中英混排标题 |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留 |
| module-conventions.md | 模块 | 资源文件放 templates/ 子目录 |
| dashboard-conventions.md | 看板 | 看板字段三方同步 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀 |
| review-checklist.md | 评审 | 12 维度评审清单(8.1-8.12) |

## 2. 上游需求

- 来源:用户口头输入(2026-06-12 16:00)
- 形式:1 句需求描述
- 提取:无新材料,需求直接来自用户口头/文本输入

## 3. 项目现状(本次扫描)

### 3.1 当前 code-require 完成后的报告模式

通读 `code-require/SKILL.md` "## 工作流程 → 步骤 10A / 步骤 10B" 节,识别出现状:

- **步骤 10A — 完善过程文档**(对应首次分析)
  - 末尾"向用户汇报:本次新增了哪些 FR/AC、哪些被列为待澄清、关联了哪些需求、版本看板的更新点"
  - **未**包含"下一步建议"段
- **步骤 10B — 汇报**(对应增量更新)
  - 末尾"新增的待澄清项 / 版本看板的同步情况"
  - **未**包含"下一步建议"段

### 3.2 当前 code-dashboard 的"建议策略"已有先例

通读 `./assistants/rules/dashboard-conventions.md` 引导 N 条,识别出:
- 建议策略:5 类优先级(高/中/低/—)+ 最多 5 条
- 命令严格按既有 10 个 `code-*` SKILL.md 真实语法
- 屏幕日志可作为"建议"展示的载体

### 3.3 待改造的技能:code-require

| 技能 | 路径 | 当前状态 | 改造范围 |
| --- | --- | --- | --- |
| code-require | `plugins/code-skills/skills/code-require/SKILL.md` | **不含**"下一步建议"段 | 步骤 10A / 步骤 10B 末尾追加 |

### 3.4 相关既有需求(同类型:UI 引导 / 流程推荐)

| 需求 | 版本 | 关联点 | 对本需求的影响 |
| --- | --- | --- | --- |
| REQ-00026 | V0.0.3 | code-dashboard 引导 N 中已含"建议策略"(5 类优先级) | 沿用同套优先级语义 |
| REQ-00030 | V0.0.3 | 元技能改 + 12 维度评审 + 看板 | INV 字节级保留约束沿用 |
| REQ-00031 | V0.0.3 | 元技能改 /code-plan /code-it /code-unit /code-auto | 元技能改路径的同类参考 |
| REQ-00025 | V0.0.3 | 编码 / 字符数 / 屏显格式契约 | 屏显格式契约(中点 `·`、≤ 30 字)沿用 |

### 3.5 既有项目级规范要点(本需求相关)

- **`skill-conventions.md`**:SKILL.md frontmatter L1-3 字节级保留(INV-1)
- **`naming-conventions.md`**:中英混排标题,中点 `·` 间隔编号与标题
- **`commit-conventions.md`**:`chore(<skill>):` 前缀(INV-3)
- **既有 12 个 `code-*` 技能 SKILL.md 0 改**(INV-4)
- **既有 11 个 REQ 的 RESULT.md 0 改**(INV-7,11 个升级为 12)

## 4. 用户原始输入(verbatim)

> 优化 `/code-require` 技能,在技能登记结束后的报告中,输出下一步建议是,针对微小需求建议直接使用 `/code-auto` 技能直接完成开发任务,其他的需求才建议先进行 `/code-design` 进行概设并继续后续任务。
