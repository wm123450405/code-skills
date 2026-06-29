# 改修总结 — TASK-REQ-00041-00003

## 1. 任务信息
- **任务编码**:TASK-REQ-00041-00003
- **标题**:[修改] code-plan 精简 SKILL.md + 创建 references/ 7 文件
- **类型**:修改
- **来源 PLAN.md**:`./assistants/V0.0.4/plan/REQ-00041/PLAN.md`

## 2. 改修内容总览
- **修改文件**:`code-plan/SKILL.md`: 1187 → 199 行(减少 83%)
- **references/ 文件**:7 个(已在 TASK-00001 中创建,本任务验证完整性)

## 3. 详细改动
- 保留:frontmatter,目标/适用场景/不适用,工作目录约定(简化),输入/输出,工具使用约定,衔接,不要做的事
- 替换为 references 引用:过程文档判定/标题解析/文件定位/命令行参数/工作流程细节/缺陷分支细节
- 步骤骨架:步骤 0a 到步骤 N,仅保留编号+标题+references 引用

## 4. 验证结果
- SKILL.md 行数:199(目标 ≤350) ✓
- frontmatter 不变 ✓
- 步骤编号完整 ✓
- references/ 7 文件完整 ✓