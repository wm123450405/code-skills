# 风险分析 — REQ-00041

## 异常处理

- **异常 1**:SKILL.md 简化后丢失关键步骤 → 处理:交叉验证(步骤 17A)逐步骤比对
- **异常 2**:references 文件与 SKILL.md 引用不一致 → 处理:引用标记格式统一,正则校验
- **异常 3**:语言检测算法对边界情况(如 package.json 无 scripts.test)误判 → 处理:降级为 "unknown",加载 common.md 兜底

## 安全边界

- 不修改原始 SKILL.md 以外的文件(仅 assistants/ + plugins/code-skills/skills/*/SKILL.md + references/)
- 所有修改通过 git 版本控制可追溯

## 性能与资源

- 每个任务:5-10 次 Write 操作 + 10-20 次 Edit 操作,纯 Markdown 文本
- 无编译/构建/测试,无外部依赖

## 回退策略

- 触发条件:简化后 SKILL.md 无法正常工作
- 步骤:git checkout 恢复 SKILL.md 原始版本,删除 references/ 目录
- 验证:重新运行 code-design / code-plan / code-it / code-check 验证功能正常

## 测试要点

- 验证:每个 SKILL.md 简化后 frontmatter 不变
- 验证:每个 SKILL.md 简化后步骤编号完整
- 验证:每个 references/ 目录包含 7 个文件
- 验证:语言检测算法对 6 类描述文件正确识别
- 验证:references 引用标记格式正确(正则 `> 详见 references/[a-z-]+\.md §\d+`)