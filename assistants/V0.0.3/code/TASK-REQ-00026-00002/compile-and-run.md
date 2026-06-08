# 编译与启动验证 — TASK-REQ-00026-00002
版本:V0.0.3

## 构建 / 启动 / 测试
- 命令:N/A(本仓库纯文档,沿用 code-unit 守卫"项目可测性"判 0)

## 静态校验
- 工具:`git diff --stat plugins/code-skills/skills/code-rule/SKILL.md` 期望 1 文件
- 工具:`git diff plugins/code-skills/skills/code-rule/SKILL.md` 期望 L336 替换,L363 保留
- 工具:`git diff marketplace.json plugin.json README*.md CLAUDE.md` 期望 0 diff
- 工具:`Read plugins/code-skills/skills/code-rule/SKILL.md` frontmatter L1-5 字节级一致

## 修复记录
- 无
