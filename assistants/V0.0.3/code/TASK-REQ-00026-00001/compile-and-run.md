# 编译与启动验证 — TASK-REQ-00026-00001
版本:V0.0.3

## 构建
- 命令:N/A
- 原因:本仓库为纯文档仓库,无构建系统

## 启动
- 命令:N/A
- 原因:无运行时

## 测试
- 命令:N/A
- 原因:无单元测试(本仓库纯文档,沿用 `code-unit` 守卫"项目可测性"判 0)

## 静态校验(本任务的实际验证手段)
- 工具:`git diff --stat plugins/code-skills/skills/`
  - 期望:列出 2 个文件(`code-it/SKILL.md` + `code-publish/SKILL.md`)
- 工具:`git diff` 校验 frontmatter
  - 期望:`name` / `description` 字段字节级不变
- 工具:`git diff marketplace.json plugin.json README*.md CLAUDE.md`
  - 期望:0 diff
- 工具:`grep "plugins/code-skills" plugins/code-skills/skills/{code-it,code-publish}/SKILL.md`
  - 期望:命中**只**属于不变量段(本任务应 0 命中)

## 修复记录
- 无
