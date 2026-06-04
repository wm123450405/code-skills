# 编译与启动验证 — TASK-REQ-00006-00006

版本:V0.0.2
任务:T-006 `[新增] 写 templates/assistants-layout.md 模板`
文档型任务,无 build/run/test 命令可执行

## 构建

- 命令:**N/A**
- 结论:**不适用**(纯文档型,无 build)

## 启动

- 命令:**N/A**
- 结论:**不适用**(模板不"运行")

## 测试

- 命令:**N/A**
- 结论:**不适用**

## 静态验证

| 检查项 | 期望 | 实际 | 结论 |
| --- | --- | --- | --- |
| 模板路径 | `plugins/.../templates/assistants-layout.md` | 同 | ✓ |
| 沿用 code-version 范式(6 段结构) | ✓ | 6 段(整体布局 / code-publish 特定扩展 / 关键点 / 多版本隔离 / 跨技能协作 / 多项目隔离) | ✓ |
| 目录树含 `publish/` 与 `qanda/` | ✓ | 全部含 | ✓ |
| H1 标题格式 | `# 工作目录布局参考 — code-publish` | 同 | ✓ |
| `## 整体布局` 代码块 | 完整目录树 | 含 rules / qanda / .current-version / <版本号> / publish / 子目录 | ✓ |
| `## code-publish 的特定扩展` 4 段 | 4 段(qanda / publish / RESULT.md / .current-version) | 4 段齐全 | ✓ |
| `## 关键点` 3 段 | 5 类资源 / 模板双向引用 / 可写目录边界 | 3 段齐全 | ✓ |
| 标注本技能对各目录读/写角色 | ✓ | 5 类资源表 + 4 段关键点 | ✓ |
| 明确"不修改"的范围 | ✓ | 列举:RESULT.md / rules / 其他 10 技能 / marketplace / plugin / CLAUDE.md / commit-conventions | ✓ |
| 不引用 SKILL.md(模块边界) | ✓ | 无反向引用 | ✓ |
| 不修改其他 10 个 `code-*` 技能 | ✓(仅新文件) | `git status` 验证 | ✓ |
| 不修改 `rules/` | ✓ | `git status` 验证 | ✓ |
| 不修改 CLAUDE.md / README | ✓ | `git status` 验证 | ✓ |

**结论**:**所有静态验证通过**,assistants-layout.md 模板可作为"标准技能资产"被其他用户查阅。

## 修复记录

无(无 build/run/test 失败)
