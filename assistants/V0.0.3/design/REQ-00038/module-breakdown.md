# 模块拆分 — REQ-00038

更新时间:2026-06-22 13:30
版本:V0.0.3

## 模块清单(5 项:1 主改造 + 1 模板追加 + 1 文档字面改写 + 2 关联适配)

| 模块名 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| `code-it` 步骤 8a.0 模块识别 | `plugins/code-skills/skills/code-it/SKILL.md` 新增 `### 步骤 8a.0 — 模块识别` 子节 | 新增 | 综合多源识别模块路径列表,返回 `modules: string[]` | 无(只读声明文件) |
| `code-it` 步骤 8a 守卫位置改造 | `plugins/code-skills/skills/code-it/SKILL.md` 步骤 8a.1 / 8a.2 / 8a.4 子节扩展 | 修改(扩展) | 守卫检查位置从 CWD 根 → 模块目录,对每个模块独立执行 7 项检查 | `code-it` 步骤 8a.0 |
| `code-it` 步骤 8.5 单测输出位置扩展 | `plugins/code-skills/skills/code-it/SKILL.md` 步骤 8.5.2 / 8.5.5 子节扩展 | 修改(扩展) | 多模块单测写到各自测试目录 | `code-it` 步骤 8a.0 / 8a |
| `code-it/templates/RESULT.md` 多模块支持 | `plugins/code-skills/skills/code-it/templates/RESULT.md` "## 单元测试(由 code-it 内化)" 小节后追加"## 各模块单测结果" | 修改(追加 1 小节) | 多模块单测结果记录 | 无 |
| `code-plan` 任务粒度描述字面改写 | `plugins/code-skills/skills/code-plan/SKILL.md` "## 步骤 10A 任务拆分 > ## 测试状态字段语义" 1 句字面改写 | 修改(字面) | 任务粒度描述对齐模块识别 | 无 |

## 自检(module-conventions.md §规则 1)

- ✅ 所有资源文件均在 `plugins/code-skills/skills/<name>/` 子目录内(SKILL.md / templates/ 既有结构 0 改)
- ✅ 命名符合 kebab-case 约定(无新增子目录名)
- ✅ SKILL.md 放在技能根目录;templates/ 放在 `templates/` 子目录
- ✅ 无散落到仓库其它位置的资源

## 自检(naming-conventions.md)

- ✅ 模块名 / 文件名 / 子节名均为 kebab-case 或小写英文
- ✅ 无驼峰 / 下划线命名

## 自检(directory-conventions.md)

- ✅ `directory-conventions.md` 当前内容"待添加"(实际无强制约束),本需求 0 触发
- ✅ 本需求未引入新子目录,无需追加规范条目