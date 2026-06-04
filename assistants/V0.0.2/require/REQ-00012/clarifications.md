# 澄清记录 — REQ-00012

更新时间:2026-06-04 15:11

## 2026-06-04 15:11(本轮)

### Q-1:根 README 内容范围
- **问题**:"根目录下项目使用说明文档"的范围是?
- **选项**:
  - A. 只极简概览 + 链到详情(推荐)— 仓库根 README 仅简介+安装+使用,详细指向 `plugins/code-skills/README.md`
  - B. 复制详细内容到根 — `plugins/code-skills/README.md` 转为"技能开发指南"补充
  - C. 不创建根 README — 仅在 `plugins/code-skills/README.md` 顶加"请从根阅读"提示
- **用户回答**:A,**只极简概览 + 链到详情**
- **影响**:RESULT.md §FR-1(根 README 内容);§6 页面(极简模板)
- **关键解读**:
  - 仓库根 `./README.md` + `./README.en.md` 是"门面"级极简
  - 详细说明全部在 `plugins/code-skills/README.md`(子文档)
  - 这是 GitHub 项目的标准两层 README 模式

### Q-2:CLAUDE.md 在根目录的处理
- **问题**:`CLAUDE.md` 在根目录是?
- **选项**:
  - A. 移动到根目录(推荐)— `plugins/code-skills/CLAUDE.md` → 仓库根
  - B. 新建 + 保留原文件
  - C. 新建指针文件
- **用户回答**:A,**移动到根目录**
- **影响**:RESULT.md §FR-2(CLAUDE.md 移动);§9 边界
- **关键解读**:
  - 仓库根 `./CLAUDE.md` 是 `code-skills` 项目的**唯一** `CLAUDE.md`
  - 移动后 `plugins/code-skills/CLAUDE.md` 不再保留
  - git 中体现为 `git mv` 操作

### Q-3:plugins/code-skills/CLAUDE.md 移动后的命运
- **问题**:移动后原位置 `plugins/code-skills/CLAUDE.md` 怎么办?
- **选项**:
  - A. 不保留(推荐)— git `mv` 操作,原位置消失
  - B. 保留为子文档(内容不同)
  - C. 转为指针
- **用户回答**:A,**不保留**
- **影响**:RESULT.md §FR-2.AC-2.5(显式 `git mv`)
- **关键解读**:
  - 仓库根 `./CLAUDE.md` 是**唯一** `CLAUDE.md`
  - git 历史可看到 move 操作

### Q-4(本轮未结构化提问,默认采纳):与 `doc-conventions.md` 协同
- **建议默认**:
  - 仓库根 `./README.md`(中文)+ `./README.en.md`(英文)同次提交(§规则 1)
  - 仓库根 README 必含核心小节(简介 / 安装 / 使用 / 能力)(§规则 2)
- **状态**:采纳默认,不阻塞

### Q-5(本轮未结构化提问,默认采纳):"极简"的具体含义
- **建议默认**:
  - **长度**:README < 50 行
  - **内容**:1 段简介 + 1 段"快速开始"(`claude plugin marketplace add ...` + `claude plugin install ...`) + 1 段"详细文档"链
  - **不**复制 `plugins/code-skills/README.md` 内容
- **状态**:采纳默认,不阻塞

### Q-6(本轮未结构化提问,默认采纳):与 REQ-00003 / REQ-00005~00011 协同
- **建议默认**:
  - 本需求**不**触发 `code-rule` 升级
  - 本需求**不**修改 `plugins/code-skills/skills/*/SKILL.md`
  - 本需求**不**修改 `assistants/rules/`
  - 仓库根 README **链到** `plugins/code-skills/README.md` 而**不**复制内容
- **状态**:采纳默认,不阻塞

### Q-7(新增,默认采纳):与 9 个 `code-*` 技能的关系
- **建议默认**:仓库根 README 在"能力"或"使用"小节**简述** 9 个技能;**详细**指向 `plugins/code-skills/README.md`
- **状态**:采纳默认,不阻塞
- **回退路径**:v2 可改为"仓库根 README 含每个技能的 1 段简介"

### Q-8(新增,默认采纳):`.gitignore` 是否需要更新
- **建议默认**:**不**需更新(本需求不引入新文件类型,均为 `.md`)
- **状态**:采纳默认,不阻塞
