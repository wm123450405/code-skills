# 分析笔记 — REQ-00042

## 当前理解

### 核心诉求
用户要求优化 `/code-it` 技能,使其在编写代码时:
- **禁止**:在代码、代码注释、代码说明文档中包含需求编号(REQ-NNNNN)、缺陷编号(BUG-NNNNN)、任务编号(TASK-REQ-NNNNN-NNNNN / TASK-BUG-NNNNN-NNNNN)、任务信息(任务标题、任务状态、任务依赖等)
- **允许**:在代码注释中保留需求的梗概(如"实现用户登录功能"而非"实现 REQ-00042")、缺陷的梗概(如"修复空指针异常"而非"修复 BUG-00001")

### 背景分析
1. `/code-it` 是唯一被允许修改项目源码的技能
2. 当前 `/code-it` 在编写代码时,可能会在注释中引用需求/缺陷/任务编号作为追溯标记
3. 这导致代码与内部追踪系统耦合——脱离 `assistants/` 目录后,代码中的编号变得无意义
4. 代码应该自文档化:注释应描述"做什么/为什么",而非"来自哪个需求单"

### 影响范围
- `/code-it` 的 SKILL.md(步骤 8 实施开发、步骤 13 撰写 RESULT.md)
- `/code-it` 的 references/common.md(§5 通用编码原则)
- `/code-it` 的 templates/RESULT.md(改修总结模板)
- 可能影响 `/code-it` 的 guidelines/coding-style.md

### 与既有规范的关系
- `skill-conventions.md` 规则 2 已规定 SKILL.md 和 templates/ 中不得包含开发痕迹(REQ-00036),但本需求针对的是 `/code-it` **产出到目标项目**的代码
- 本需求与 REQ-00036 是互补关系:REQ-00036 清理技能文件本身,本需求清理技能产出的代码

### 候选方案
1. 在步骤 8(实施开发)的编码原则中增加"禁止在代码/注释中引用编号"的规则
2. 在步骤 13(撰写 RESULT.md)中增加对改修总结的约束
3. 在 guidelines/coding-style.md 中增加独立的注释规范条款

### 疑点
- "任务信息"的范围:是否包括任务标题?根据用户描述,梗概可以保留,但编号不行
- 代码中的 commit message 是否受此约束?(commit message 格式由 commit-conventions.md 规范,通常需要包含编号)