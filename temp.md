/code-skills:code-require 优化 `/code-require`、`/code-design`、`/code-plan`、`/code-it`、`/code-unit`、`/code-check`、`/code-fix` 这些技能，在最后兜底代码提交环节默认自动提交，无需用户确认，提交时确保所有修改的文件、过程文件、结果文件都被包含在提交记录中，不要有遗漏。

/code-skills:code-require 优化 `/code-fix` 技能，该技能只登记并分析缺陷（类似`/code-require`技能），不进行直接修复。被登记的缺陷需要经过 `/code-plan` 技能进行比编码详细设计，在经过 `/code-it` 技能进行实际的编码修复和 `/code-unit` 技能补充单元测试，最后通过 `/code-check` 技能进行修复检查更新修复状态。再优化 `/code-auto` 技能，若检测到是缺陷修复任务，应该通过 `/code-plan`->`/code-it`->`/code-unit`->`/code-check`（可以直接复用原来针对 `/code-require` 创建需求的后续逻辑） 技能进行修复，并提交。

/code-skills:code-require 优化 `/code-require` 技能，在技能登记结束后的报告中，输出下一步建议是，针对微小需求建议直接使用 `/code-auto` 技能直接完成开发任务，其他的需求才建议先进行 `/code-design` 进行概设并继续后续任务。

/code-skills:code-require 优化 `/code-plan` 规划任务时，每个任务应该确保编译或运行成功，而不是单独规划一个编译运行检测的任务，也不需要在任务阶段编写单元测试功能。


需求澄清技能 `/code-require` 时不涉及技术选型确定，只涉及功能点确定；技术选型确定放在 `/code-design` 技能阶段，没有必要进行技术选型的需求无需分析技术选型选项。

移除技能 `/code-unit`，将技能能力整合进 `/code-it` 技能中，功能代码编写完成根据需要直接编写单元测试或针对不适用的工程跳过单元测试编写。