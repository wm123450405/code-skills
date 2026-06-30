# 文档编写规范(doc-conventions)

> 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
> 最后更新:2026-06-03 19:15
> 适用版本:跨所有版本共享(项目级)

## 适用场景
本规范适用于仓库内**所有** `README*.md` 文件的编写与维护,以及它们的同步约束。涉及"如何写 README、是否需要中英版本、版本之间是否一致"时查阅本文件。

## 强制级别约定
本文件中各规则的强制级别逐条标注(参见各"规则 N"小节的"强制级别"字段),本文件头部不统一声明。

---

## 规则 1:README 多语言版本必须保持结构对仗

### 条款
当仓库内出现**两个或更多**语言版本的 README(如 `README.md` 中文 + `README.en.md` 英文)时:

1. **结构对仗**:每个语言版本必须包含**相同数量、相同顺序的章节**(标题层级、表格列数、列表条数可以因语言表达差异微调,但"段落的语义对应"必须一目了然)
2. **同步修改**:任一语言版本发生修改后,必须在**同一次提交**中同步其它语言版本,不得出现"中文版有 X 章节,英文版无 X 章节"的漂移
3. **缺失即违规**:仅维护单一语言版本的项目不受本规则约束;但一旦新增/发现第二个语言版本,**所有现存语言版本**必须按本规则保持对仗

判别标准:把两个 README 的目录树并列对比,若任何"二级标题"或"一级编号章节"只在一边出现,即视为结构漂移。

### 强制级别
- 必须

### 适用范围
- 整个仓库内**所有** `README*.md` 文件(包含但不限于 `plugins/code-skills/README.md` + `plugins/code-skills/README.en.md`,未来若加 `docs/*.md` 或 marketplace 根 `README*.md` 同样适用)
- 新增语言版本、修改任一语言版本时均适用

### 正面示例
`plugins/code-skills/README.md` 与 `plugins/code-skills/README.en.md`:

```markdown
# 中文版:
## 技能概览
| 技能 | 用途 | ... |
| --- | --- | --- |
## 工作流管道
...

# 英文版:
## Skills Overview
| Skill | Purpose | ... |
| --- | --- | --- |
## Pipeline
...
```

要点:两个文件的"二级标题集合"完全对应(都是 `技能概览/Skills Overview` + `工作流管道/Pipeline` + `使用说明/How to Use` + ...)

### 反面示例
```markdown
# 中文版多了一个章节:
## 技能概览
## 工作流管道
## 致谢           # ← 英文版没有"致谢"
## 许可证

# 英文版:
## Skills Overview
## Pipeline
## How to Use     # ← 中文版"使用说明"未对齐到此
## License
```

这是典型的"漂移":中文"致谢"无对应英文节,英文"How to Use"无对应中文节。

### 例外
- **特定章节的"语言特定补充"**:可在文件末尾加 "Translation Notes" 小节(只在该语言版本中存在),用于说明"此版本独有的本地化补充",但**不得**承载核心信息
- 翻译进度说明(例如"本文档部分章节为机器翻译,待校对")可放在文末,但不影响对仗判定

### 关联规范
- `./assistants/rules/skill-conventions.md §规则 1`(技能元信息一致性)

### 来源
- 由 `code-rule` 技能添加于 2026-06-03 18:50
- 用户原始描述:"README 的中英版本必须保持结构对仗,改一边需同步另一边"

---

## 规则 2:仓库级使用说明文档必须存在并持续维护

### 条款
`plugins/code-skills/README.md`(本仓库的"使用说明文档")必须满足:

1. **存在性**:该文件**必须存在**且非空(空文件、占位符、`<TODO>` 视为本规则违反)
2. **核心内容覆盖**:至少含以下核心小节(顺序可调,但每节都需有实质内容):
   - 简介(项目是什么、面向谁)
   - 安装/获取方式(怎么把本仓库用起来)
   - 核心使用流程(主要场景的"端到端"步骤)
   - 主要能力/特性清单(可选,但推荐)
3. **与代码现状同步**:README 中提到的命令、目录名、配置项必须与仓库实际状态一致;引用任何路径/版本号/CLI 命令时,不得有"指向不存在文件"或"版本号已过时"的引用
4. **持续维护**:README 出现"待补充"、"TODO"、"略"、"此处省略"等占位文本时,必须**有对应的 issue / TODO 注释** 指向该占位的修复责任(允许"分阶段完善",但不允许"无主占位")

### 强制级别
- 必须

### 适用范围
- `plugins/code-skills/README.md`(本仓库当前的使用说明文档)
- 适用范围**不**包括 README.en.md(那个是规则 1 的"对仗对象");本规则约束**主语言版本**的完整性
- 未来若加 `CONTRIBUTING.md` / `ARCHITECTURE.md` 等额外说明文档,需先经设计评审,再决定是否纳入本规则

### 正面示例
README 包含完整小节、且指向真实存在的文件:
```markdown
# code-skills

## 安装
1. claude plugin marketplace add https://github.com/...
2. claude plugin install code-skills@code-skills
3. /reload-plugins

## 使用说明
0a. 首次接入项目:在 CWD 调 code-init
0b. 建立规范:调 code-rule
1. 首次使用 / 开新开发版本:调 code-version
...
```

每一条命令都对应仓库内实际存在的技能(可在 `plugins/code-skills/skills/` 下找到对应 SKILL.md)。

### 反面示例
```markdown
# code-skills

## 简介
本仓库提供 code-* 技能集合,使用方式详见后续章节。

## 安装
(此处省略,后续版本补充)         # ❌ 无主占位 - 应有 issue / TODO 注释

## 使用说明
略                              # ❌ 占位文本 - 必须有修复责任人

## 主要能力
待补充                          # ❌ 占位文本
```

### 例外
- **项目刚刚初始化**:允许在 `plugins/code-skills/README.md` 文件头注明 `<!-- WARNING: 文档正在重构中,见 issue #N -->`,此状态下"占位文本"暂不视为违规,但 issue 引用必须真实存在
- **本规则不约束 README.en.md**:英文版由 `规则 1 README 多语言版本必须保持结构对仗` 约束

### 关联规范
- `./assistants/rules/doc-conventions.md §规则 1`(README 多语言对仗 — 本规则约束主语言版本的完整性,规则 1 约束多语言版本之间的对仗)
- `./assistants/rules/marketplace-protocol.md §规则 1`(marketplace.json 与 plugin.json 引用一致性)

### 来源
- 由 `code-rule` 技能添加于 2026-06-03 19:15
- 用户原始描述:"增加仓库级别使用说明文档,我会在后续版本中完善说明文档"(本规则在制度层面保证使用说明文档的"持续维护"属性)

---

## 规则 3:技能变更时须同步更新使用说明文档

### 条款
当 `plugins/code-skills/skills/` 下发生以下任一变更时,必须在**同一次需求/缺陷**中将 `plugins/code-skills/README.md` 和 `README.en.md` 的更新纳入任务范围:

1. **技能新增/删除**:新增或删除技能目录
2. **技能重命名**:SKILL.md 的 `name` 字段变更或目录重命名
3. **工作流变更**:技能间的调用顺序、输入输出关系、阶段顺序发生变化
4. **核心概念变更**:版本工作空间、目录结构、状态模型等核心概念发生变化
5. **命令调用方式变更**:用户调用技能的命令格式、参数、交互方式发生变化

### 强制级别
- 必须

### 适用范围
- `plugins/code-skills/README.md` 和 `README.en.md`(两个语言版本同受约束)
- 所有对 `skills/` 下技能的修改,在 DESIGN 阶段就必须评估"是否需要更新 README"
- 若评估需要更新但未纳入 PLAN 任务 → 视为遗漏,CHECK 阶段必须发现

### 正面示例
REQ-00044 将 14 个技能合并为 7 个技能,DESIGN 阶段评估后,PLAN 中纳入"更新 README.md + README.en.md"任务,CODING 阶段执行。

### 反面示例
REQ-00044 重构后,README 仍描述 14 个旧技能、旧命令名、旧目录结构,用户在 README 中找不到任何当前可用的命令。

### 例外
- 仅修改技能内部实现细节(如 references 文件、templates 文件),不影响用户可见的调用方式和工作流 → 不需要更新 README
- 修改 `CLAUDE.md`(面向 AI 的开发指南,非面向用户的使用说明)→ 不需要更新 README

### 关联规范
- `./assistants/rules/doc-conventions.md §规则 1`(README 多语言对仗)
- `./assistants/rules/doc-conventions.md §规则 2`(README 必须存在并持续维护)
- `./assistants/rules/skill-conventions.md §规则 1`(技能元信息一致性)

### 来源
- 由 `code-fix` 技能添加于 2026-06-30
- 缺陷来源:BUG-00002 — REQ-00044 重构后项目使用说明文档未更新
