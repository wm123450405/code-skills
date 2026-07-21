---
name: code-rule
description: `/code rule` 编码规范追加/扩展。模型在用户陈述规范(如"统一用 snake_case")、团队 review 后形成新条款、或启动项目建立首批规范时调用。3 类:Type A 规范条款 → `./assistants/rules/<分类>.md`;Type B AI 工作约定 → `<本仓库>/CLAUDE.md`;Type C 模板提示 → `templates/*.md`。**只追加不重写**;不需要版本上下文。
---

# `/code rule` — 编码规范管理

> 模板见 [`templates/rule/`](../../../templates/rule/) 与 [`templates/fix/assistants-layout.md`](../../../templates/fix/assistants-layout.md)。

## 目标

把自然语言描述的规范自动归类、结构化、落地到 `./assistants/rules/<分类>.md`,供其他 `/code` 子命令只读消费。

**定位**: `rule` 是"规范基建"工具,`req`/`fix`/`ver`/`faq`/`merge` 都把 `./assistants/rules/` 视为只读强约束输入。

## 类型分流

| Type | 落地位置 | 何时用 |
| --- | --- | --- |
| A 规范条款 | `./assistants/rules/<分类>.md` | 命名/错误处理/安全/性能等具体条款 |
| B AI 工作约定 | `<本仓库>/CLAUDE.md` "AI 工作约定"小节 | 指引 N 类元规则(不归类 rules/) |
| C 模板提示 | `templates/*.md` | 末尾 `## 提示:` 或内联 `### 提示:` |

Type A 子分类(C-1 框架 / C-2 依赖 / C-3 命名 / C-4 目录 / C-5 代码风格 / C-6 提交与合并 等)由首次写入时确定。

## 工作流

1. 探 `./assistants/` 现状(`Bash: ls` + `Glob "./assistants/rules/*"`)
2. 兜底建目录(`mkdir -p ./assistants/rules/`),**不**创建 `.current-version` 或版本目录(那是 `ver` 的事)
3. 收集规范描述(用户给就用,否则主动问)
4. 拆分 + 类型识别 + 初步归类
5. 追问 1-3 个最阻塞字段(强制级别 / 适用范围 / 正反示例 / 例外 / 关联)
6. 探测目标文件现状,识别冲突与重复
7. 写文件: 不存在 → `Write` 新建;存在 → `Edit` 末尾追加 "规则 N"
8. 汇报分类、规则简称、强制级别、文件位置、下游影响
9. 询问"继续追加 / 查看现有清单 / 结束"

## 强制约束

- **不重写已有规范** — 用 `Edit` 末尾追加
- 不读取/写入 `.current-version` 与版本目录
- 分类未确认前不写文件
- 不把"必须"和"推荐"的规则混用同一文件头部声明
- 不在没有澄清强制级别的情况下写入
- 不在没有 `Read` 现有文件的情况下 `Write` 覆盖
- 不替用户决定分类(用 `AskUserQuestion` 确认)

## 衔接

- 下游(被消费方): `/code req` / `/code fix` / `/code ver` / `/code faq` / `/code merge` 全部只读消费本技能产出
- 上游: 用户直接发起的自然语言描述
- 横向: 与 `/code ver` 无依赖,可任意顺序调用