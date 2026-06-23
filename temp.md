/code-skills:code-require 优化 `/code-require`、`/code-design`、`/code-plan`、`/code-it`、`/code-unit`、`/code-check`、`/code-fix` 这些技能，在最后兜底代码提交环节默认自动提交，无需用户确认，提交时确保所有修改的文件、过程文件、结果文件都被包含在提交记录中，不要有遗漏。

/code-skills:code-require 优化 `/code-fix` 技能，该技能只登记并分析缺陷（类似`/code-require`技能），不进行直接修复。被登记的缺陷需要经过 `/code-plan` 技能进行比编码详细设计，在经过 `/code-it` 技能进行实际的编码修复和 `/code-unit` 技能补充单元测试，最后通过 `/code-check` 技能进行修复检查更新修复状态。再优化 `/code-auto` 技能，若检测到是缺陷修复任务，应该通过 `/code-plan`->`/code-it`->`/code-unit`->`/code-check`（可以直接复用原来针对 `/code-require` 创建需求的后续逻辑） 技能进行修复，并提交。

/code-skills:code-require 优化 `/code-require` 技能，在技能登记结束后的报告中，输出下一步建议是，针对微小需求建议直接使用 `/code-auto` 技能直接完成开发任务，其他的需求才建议先进行 `/code-design` 进行概设并继续后续任务。

/code-skills:code-require 优化 `/code-plan` 规划任务时，每个任务应该确保编译或运行成功，而不是单独规划一个编译运行检测的任务，也不需要在任务阶段编写单元测试功能。


需求澄清技能 `/code-require` 时不涉及技术选型确定，只涉及功能点确定；技术选型确定放在 `/code-design` 技能阶段，没有必要进行技术选型的需求无需分析技术选型选项。

移除技能 `/code-unit`，将技能能力整合进 `/code-it` 技能中，功能代码编写完成根据需要直接编写单元测试或针对不适用的工程跳过单元测试编写。

修改所有技能的 `description` 中的描述，用通俗的语言描述技能的主要能力，而不是介绍技能具体的代码逻辑，比如不需要说明操作的目录和文件。

修改所有技能的过程文档记录逻辑，移除没必要的过程文档记录，减少token消耗；所谓没必要的过程文档是指在部分需求、部分类型的工程下不涉及、不适用的过程文档，需要判断是否生成对应的过程文档，而不是生成一个包含不涉及、不适用说明内容的文档。


优化 `/code-fix` 技能以及整个缺陷修复流程中的技能，`/code-fix` 负责登记缺陷（缺陷初始状态待处理），`/code-plan` 负责分析缺陷并计划修复的开发任务（完成后直接标记缺陷状态未待开发）, `/code-it` 执行具体的开发工作（若只有一项开发任务，完成后直接标记缺陷为待审查，若有多项开发任务，完成第一项时标记缺陷状态为开发中，完成所有开发任务后标记缺陷状态为待审查）， `/code-check` 审查缺陷修复的代码（审查完成后标记缺陷状态为已完成），整个过程 `/code-fix` -> `/code-plan` -> `/code-it` -> `/code-check` 后结束，过程中无需反复调用 `/code-fix` 技能来修改缺陷状态。

编码、审查过程对于要求代码行数限制的部分，应该只计算实际代码逻辑的行数，不要计算注释、说明、空行等内容的行数

现有的 `/code-it` 技能在判断是否需要编写单元测试的逻辑上存在遗漏，有些工程下的子模块需要单独编写单元测试；优化 `/code-it` 技能，判断逻辑不能以整个工程为为主，而是要判断改修的代码属于哪个模块的，单独判断模块是否应该编写单元测试。




BUG:

1. 技能 `/code-require` 还是会出现技术选型的选择的问题，应该只能在 `/code-design` 阶段出现选择技术选型相关提问。`/code-require` 不应该分析或记录任何与技术选型相关的内容，只分析需求本身的功能，技术选型完全放到 `/code-design` 技能中去完成。

2. 技能 `/code-it` 还是会出现输出不必要的过程文档的情况，以下是一个markdown类的工程下执行后的日志，请分析原因并修正这个问题，并检查其他所有技能过程文档，若存在类似问题需要一并修改。
● Write(assistants\V0.0.3\code\TASK-REQ-00039-00003\compile-and-run.md)
  ⎿  Wrote 17 lines to assistants\V0.0.3\code\TASK-REQ-00039-00003\compile-and-run.md
       2 # 编译与启动验证 — TASK-REQ-00039-00003
       3 版本:V0.0.3
       4 
       5 ## 构建
       6 
       7 - 命令:(无 — 本任务为纯 Markdown 技能定义改造,无生产代码改动,无可执行构建命令
         )
       8 - 结论:不适用(沿用 PLAN.md §3 T-1 验证手段;本仓库是 Claude Code 技能插件集合)
       9 
      10 ## 启动
     … +7 lines (ctrl+o to expand)

● Write(assistants\V0.0.3\code\TASK-REQ-00039-00003\test-results.md)
  ⎿  Wrote 32 lines to assistants\V0.0.3\code\TASK-REQ-00039-00003\test-results.md
       2 # 测试结果 — TASK-REQ-00039-00003
       3 版本:V0.0.3
       4 时间:2026-06-22 15:12
       6 ## 测试命令
       7 
       8 (无 — 本任务为纯 Markdown 技能定义改造,无生产代码改动,无可执行测试命令;沿用 `
         ect.toml` 含 `[tool.pytest*]` / `Cargo.toml` / `go.mod` / `pom.xml` / `build.
         gradle` / `test/` → 守卫不通过 → 任务"测试状态"列 = `不适用`)
       9 
      10 ## 输出摘要
     … +32 lines (ctrl+o to expand)

● Write(assistants\V0.0.3\code\TASK-REQ-00039-00003\work-log.md)
  ⎿  Wrote 95 lines to assistants\V0.0.3\code\TASK-REQ-00039-00003\work-log.md
       2 开始时间:2026-06-22 15:1039-00003
       3 版本:V0.0.3
       4 
       5 ## 项目现状(步骤 6 记录)
       6 
       7 - 项目类型:Claude Code 技能插件集合(`plugins/code-skills/skills/<name>/SKILL.
         md`)
       8 - 构建命令:无(纯 Markdown 技能定义)
       9 - 运行命令:无
      10 - 测试命令:无(项目不可测;沿用 T-1 步骤 8a 守卫判定)
     … +115 lines (ctrl+o to expand)