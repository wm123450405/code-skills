# 改修总结 — TASK-REQ-00041-00002

## 1. 任务信息
- **任务编码**:TASK-REQ-00041-00002
- **标题**:[修改] code-design 精简 SKILL.md + 创建 references/ 7 文件
- **类型**:修改
- **触发/来源**:需求新增
- **来源 PLAN.md**:`./assistants/V0.0.4/plan/REQ-00041/PLAN.md`

## 2. 改修内容总览
- **修改文件**:1 个(`code-design/SKILL.md`: 669 → 192 行)
- **references/ 文件**:7 个(已在 TASK-00001 中创建,本任务验证完整性)

## 3. 详细改动

### 3.1 code-design/SKILL.md 精简
- **保留**:frontmatter(字节级),目标/适用场景/不适用,工作目录约定(简化),输入/输出,工具使用约定,衔接,不要做的事
- **替换为 references 引用**:
  - `## 过程文档自适应判定` → `> 详见 references/common.md §4`
  - `## 修改文件定位的语义化约定` → `> 详见 references/common.md §5`
  - `## 命令行参数解析` → `> 详见 references/common.md §13`
  - `## 工作流程` 各步骤细节 → 编号+标题+references 引用
  - `## 过程文档格式` → 已移除(引用 common.md §10)
  - `## 模板填充步骤` → 已移除(引用 common.md §11)
- **行数变化**:669 → 192 行(减少 71%)

### 3.2 code-design/references/ 验证
- `common.md`:15 章节,完整(已在 TASK-00001 中创建)
- 6 语言文档:各 7 章节,完整

## 4. 关键决策与权衡
- 步骤 0a/0b.0/0b 细节全部移到 references/common.md,SKILL.md 仅保留一行引用
- 步骤 5 语言检测通过 `references/<语言>.md §1` 引用
- 步骤 7A-15A 和 7B-10B 的细节合并到 common.md §8-§9

## 5. 偏离设计/规范
- 无偏离

## 6. 验证结果
- SKILL.md 行数:192(目标 ≤300) ✓
- SKILL.md frontmatter 不变 ✓
- SKILL.md 所有步骤编号完整 ✓
- references/ 7 个文件均非空 ✓

## 7. 已知问题/未完成项
- 无

## 8. 关联任务与提交
- 前置任务:TASK-REQ-00041-00001(已完成)
- 后置任务:TASK-REQ-00041-00003~00005
- 提交:待末尾兜底提交