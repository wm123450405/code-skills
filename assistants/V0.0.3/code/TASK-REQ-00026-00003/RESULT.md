# TASK-REQ-00026-00003 改修总结 — code-publish/templates 3 个模板字面替换

- **任务编码**:TASK-REQ-00026-00003
- **父级需求**:REQ-00026
- **类型**:修改
- **触发/来源**:详细设计
- **开发状态**:已完成
- **测试状态**:不适用
- **完成时间**:2026-06-08 13:27
- **版本**:V0.0.3

## 1. 任务信息
来源:PLAN.md §2 T-003

## 2. 改修内容总览
3 个 templates 文件,3 处 Edit(每文件 1 处)。

## 3. 详细改动
### DEPLOY.md L3
- 改前:`plugins/code-skills/skills/code-publish/templates/DEPLOY.md`
- 改后:`<本仓库>/skills/code-publish/templates/DEPLOY.md`

### UPDATE.md L3
- 改前:`plugins/code-skills/skills/code-publish/templates/UPDATE.md`
- 改后:`<本仓库>/skills/code-publish/templates/UPDATE.md`

### qanda-README.md L133
- 改前:"草稿应该放项目内的 `drafts/` 子目录"
- 改后:"草稿应该放本仓库内的 `drafts/` 子目录"

## 4. 关键决策
- 模板**不**加"`<本仓库>` 指代..."概述段声明 — 模板是用户消费的最终输出,加占位符会污染用户文档
- 模板文件其余结构(占位符示例、章节顺序)**不**变

## 5. 偏离设计/规范的地方
无

## 6. 验证结果
静态校验通过

## 7. 已知问题/未完成项
无

## 8. 关联任务与提交
- T-001 / T-002 已完成,T-004 / T-005 待开始
- T-005 依赖 T-001 ~ T-004
