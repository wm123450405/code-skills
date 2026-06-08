# 编译与启动验证 — TASK-REQ-00026-00003
版本:V0.0.3

## 构建 / 启动 / 测试
- 命令:N/A(本仓库纯文档)

## 静态校验
- `git diff --stat plugins/code-skills/skills/code-publish/templates/` 期望 3 个文件
- 3 个文件 L3 / L133 字面替换生效
- 模板文件其他部分(章节结构、占位符示例)字面保留
- `git diff marketplace.json plugin.json README*.md CLAUDE.md` 0 diff
