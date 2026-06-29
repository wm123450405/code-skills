# 模块详细化 — REQ-00041

## 模块 1: code-design/SKILL.md

- **路径**:`plugins/code-skills/skills/code-design/SKILL.md`
- **动作**:Edit 精简(~669 → ~250 行)
- **保留**:frontmatter / 目标-不适用 / 工作目录约定(简化) / 输入输出(简化) / 工具使用约定 / 工作流程(骨架) / 衔接 / 不要做的事
- **移除**:过程文档自适应判定 / 修改文件定位 / 命令行参数解析 / 模板填充 / 过程文档格式 / 标题解析 / 步骤细节
- **与概要设计的对应**:§4 模块 1
- **符合的规范**:skill-conventions.md §规则 1-2

## 模块 2: code-design/references/

- **路径**:`plugins/code-skills/skills/code-design/references/`
- **动作**:新建 7 个文件
- **common.md**:15 章节(步骤 0a/0b/0b.0 细节 + 过程文档判定 + 文件定位 + 步骤 5 通用探索 + 首次/增量设计 + 末尾提交 + 格式 + 模板 + 标题解析 + 命令行 + 屏显 + 边界)
- **6 语言文档**:各 7 章节(项目结构/构建/测试/运行/monorepo/编码约定/工具链)
- **与概要设计的对应**:§4 模块 2
- **符合的规范**:skill-conventions.md §规则 1

## 模块 3-8: code-plan / code-it / code-check(同构)

参照模块 1-2 模式,各技能 SKILL.md 精简 + references/ 创建。差异在于各技能 references/ 内容侧重不同(详见 PLAN.md 任务详情)。