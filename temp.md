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



需要对现有工程的所有技能组进行功能大改版，需要将现有技能缩减为 `code-ver`、`code-req`、`code-fix`、`code-faq`、`code-rule`, `code-merge`、`code-dashboard` 7个技能。
1. `code-ver` 技能合并现有 `code-version`、`code-publish` 和 `code-init` 技能的主要能力，若是初始项目执行 `code-ver` 是应该按照现在 `code-init` 技能能力进行工程的初始化，后按照现在 `code-version` 技能能力创建版本；若是已初始化过的工程，应该按照现有 `code-versin` 技能的功能切换版本号，若当前所处的版本是未发布的版本应该在切换版本号时询问是否执行现有 `code-publish` 技能的功能进行发布后再切换到指定的版本号上。
2. `code-req` 技能合并现有 `code-require`、`code-design`、`code-plan`、`code-it`、`code-check` 技能中关于需求开发的内容，按照现有 `code-auto` 中针对需求的全自动化逻辑执行上述技能功能（`code-req`技能无需完成 `code-auto` 技能中的缺陷修复路径，仅需要完成需求开发的路径）。同时使用 `code-req` 进行需求自动开发过程中时区别现有的 `code-auto` 技能，应该事事与用户确认后再进行下一步。但增加 `--auto` 指令来达到现在 `code-auto` 技能中所有事项使用推荐选项的静默开发效果。
3. `code-fix` 技能合并现有 `code-fix`、`code-plan`、`code-it`、`code-check` 技能中关于缺陷修复的内容，按照现有 `code-fix` + `code-auto` 中针对缺陷修复的全自动化逻辑执行上述技能功能（新`code-fix` 技能无需完成原 `code-auto` 技能中的需求开发路径，仅需要完成缺陷修复的路径）。同时使用新 `code-fix` 进行缺陷自动化修复过程中时区别现有的 `code-auto` 技能，应该事事与用户确认后再进行下一步。但增加 `--auto` 指令来达到现在 `code-auto` 技能中所有事项使用推荐选项的静默开发效果。
4. 新 `code-req` 技能与新 `code-fix` 技能输出内容上做精简，输出格式上做优化：`assistants/` 目录功能保持不变，依然统一存放所有本工程下技能的所有输出；`assistants/<版本号>/` 目录与 `assistants/.current-version` 文件的功能保持不变，用于管理各版本下的需求、缺陷、任务以及当前版本信息；`assistants/<版本号>/` 目录下的 `code/`、`design/`、`plan/`、`require/`、`review/`、`check/`、`test/`、`fix/` 等目录重组，按照 `req/`、`fix/` 两大目录分别管理需求和缺陷；`req/` 目录下按照需求编号目录管理各需求，其中使用 `REQUIRE.md` 作为需求分析的结果产物，使用 `DESGIN.md` 作为软件设计产物（不区分概要设计、详细设计），使用 `PLAN.md` 作为开发任务排期计划结果产物，使用 `TASK-<任务需要>.md` 文档作为任务完成的结果产物，使用 `CHECK.md` 文档作为代码审查的结果产物，无需额外记录多份过程文档，如有额外信息需要记录可记录为一份 `LOG.md` 的过程文档（非必要不记录）；`fix/` 目录下按照缺陷编号目录管理各缺陷，其中使用 `BUG.md` 作为缺陷分析的结果产物（主要分析缺陷出发的条件、缺陷的可能成因），`DESGIN.md`、`PLAN.md`、`TASK-<任务序号>.md`、`CHECK.md`、`LOG.md` 等文档与 `req/` 目录下内容和生成逻辑保持一致（新 `code-req` 与 `code-fix` 大部分开发进程能力一致，仅登记的需求与登记的缺陷文档不一致，两项技能中应保持一致的总体逻辑）；每个需求目录或缺陷目录中应当包含 `PROCESS.md` 文件用于记录当前的执行进程，在操作中断后能够通过新的 `code-req`、`code-fix` 技能从中断的地方继续执行（`PROCESS.md`文件以追加的方式记录过程，记录前无需单独读取文件内容）。
5. `code-faq` 技能主要保留现有 `code-answer` 技能内容，但是增加 `--require` 参数 + 文件路径导出需求文档功能、增加 `--desgin` 参数 + 文件路径导出详细设计文档功能（额外增加 `--summary` 参数导出概要设计文档，概要设计文档应该从软件设计文档中提取概要设计信息编写为新文档内容）。以上三个参数模式下可以通过 `--template` + 文件路径的方式执行导出的文件模板。需要导出的内容参考最新的文件结构和输出内容。
6. 各项技能需要简化 `assistants/<版本号>/RESULT.md` 中版本看板数据的记录逻辑，避免频繁读写该文档，仅在需求、缺陷创建时追加记录需求、缺陷对应的进度文档（`PROCESS.md`）引用。
7. 保留现有 `code-rule`, `code-merge`、`code-dashboard` 三个技能的基本功能，但是参考的文件和内容按照最新的各项技能的输出要求。