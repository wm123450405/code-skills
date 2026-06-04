# 编译与启动验证 — TASK-REQ-00006-00005

版本:V0.0.2
任务:T-005 `[新增] 写 templates/qanda-README.md 模板`
文档型任务,无 build/run/test 命令可执行

## 构建

- 命令:**N/A**
- 结论:**不适用**(纯文档型,无 build)

## 启动

- 命令:**N/A**
- 结论:**不适用**(模板不"运行",由 `code-publish` 复制到 `assistants/qanda/README.md`)

## 测试

- 命令:**N/A**
- 结论:**不适用**(无传统单测)

## 静态验证

| 检查项 | 期望 | 实际 | 结论 |
| --- | --- | --- | --- |
| 模板路径 | `plugins/.../templates/qanda-README.md` | 同 | ✓ |
| H1 标题 | `# assistants/qanda/ — 项目级 Q&A 长期沉淀目录` | 同 | ✓ |
| `## 用途` 章节 | 含典型内容示例 | 5 个示例(部署/升级/初始化/首次/安全性能) | ✓ |
| `## 文件命名建议` 章节 | kebab-case + 命名约定 + 至少 2 个具体示例 | 7 个具体示例(`deploy-faq.md` / `db-init-faq.md` / 等) | ✓ |
| `## 引用规范` 章节 | 排除 README.md + 排序规则 + 内容格式建议 + 与 publish/Q&A.md 对比 | 4 段齐全 | ✓ |
| `## 维护方式` 章节 | 4 步 + 当前(v1)与未来(v2)说明 + "不做的事" | 全部齐全 | ✓ |
| 文首警示"当前人工" | ✓ | `⚠ 本目录当前由人工手动维护(REO-00006 §Q-2 锁定 A)` | ✓ |
| 不修改 `module-conventions §规则 1` | 模板在 templates/ | ✓ | ✓ |
| 不修改其他 10 个 `code-*` 技能 | 仅新文件 | `git status` 验证 | ✓ |
| 不修改 `rules/` / CLAUDE.md / README | 仅新文件 | `git status` 验证 | ✓ |
| 与 T-004 Q&A.md 模板引用一致 | "## 引用规范"应说明 README.md 不被聚合 | 显式说明 | ✓ |

**结论**:**所有静态验证通过**,qanda-README.md 模板可被 `code-publish` 技能直接消费(由 QandaScaffolder 在 `code-publish` 步骤 2.5 复制)。

## 修复记录

无(无 build/run/test 失败)
