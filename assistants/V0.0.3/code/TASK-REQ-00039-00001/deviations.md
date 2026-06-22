# 偏离记录 — TASK-REQ-00039-00001

版本:V0.0.3

## 偏离 1:无生产代码改动

- **类别**:任务范围外(本任务为纯 Markdown 文档改造)
- **依据**:
 - 详细设计 §4 模块 1 + §4 模块 2:`logic-loc.md` + `logic-loc-defaults.md` 均为新建 Markdown 文件
 - PLAN.md §3 TASK-REQ-00039-00001 任务详情:涉及文件仅 `plugins/code-skills/skills/code-it/lib/logic-loc.md` + `logic-loc-defaults.md`
- **实际做法**:仅新建 2 个 Markdown 文档(共享库),未触发任何 `Bash` 编译/运行/测试命令;`Bash: mkdir -p` 仅创建目录,**不**算生产代码改动
- **偏离理由**:本仓库是 Claude Code 技能插件集合,无构建/运行/测试命令
- **影响**:无
- **授权**:用户预先在 PLAN.md §12.3 实施关键约束中确认
- **时间**:2026-06-22 15:04

## 偏离 2:无 frontmatter(纯 Markdown 文档)

- **类别**:刻意省略(沿用既有约定)
- **依据**:`skill-conventions §规则 1` 字节级保留:**本需求**新建的 2 个共享库文档**无** frontmatter(纯 Markdown 文本),**不**触发 `skill-conventions §规则 1`
- **实际做法**:`logic-loc.md` + `logic-loc-defaults.md` 仅有 Markdown 标题 / 章节 / 代码块,**不**含 `---` frontmatter 块
- **偏离理由**:`lib/` 子目录的共享库文档约定是纯 Markdown 文本(沿用 `module-conventions §规则 1`);`SKILL.md` 才有 frontmatter 约束
- **影响**:无
- **授权**:`module-conventions §规则 1` 隐含约定
- **时间**:2026-06-22 15:04

## 偏离 3:本任务不重复追加 ## 不要做的事 段

- **类别**:刻意省略(沿用 T-3 / T-4 模式)
- **依据**:`code-it/SKILL.md` 既有 ## 不要做的事 段是 SKILL.md 文档的约定;**本任务**新建的是 `lib/` 子目录的共享库文档,**不**含 ## 不要做的事 段
- **实际做法**:`logic-loc.md` + `logic-loc-defaults.md` **不**含 ## 不要做的事 段
- **偏离理由**:`lib/` 子目录的共享库文档**不**沿用 SKILL.md 的 ## 不要做的事 段约定
- **影响**:无
- **授权**:`module-conventions §规则 1` 隐含约定
- **时间**:2026-06-22 15:04