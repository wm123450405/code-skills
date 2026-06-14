/code-skills:code-require 优化 `/code-require`、`/code-design`、`/code-plan`、`/code-it`、`/code-unit`、`/code-check`、`/code-fix` 这些技能，在最后兜底代码提交环节默认自动提交，无需用户确认，提交时确保所有修改的文件、过程文件、结果文件都被包含在提交记录中，不要有遗漏。

需求澄清技能 `/code-require` 时不涉及技术选型确定，只涉及功能点确定；技术选型确定放在 `/code-design` 技能阶段，没有必要进行技术选型的需求无需分析技术选型选项。

移除技能 `/code-unit`，将技能能力整合进 `/code-it` 技能中，功能代码编写完成根据需要直接编写单元测试或针对不适用的工程跳过单元测试编写。