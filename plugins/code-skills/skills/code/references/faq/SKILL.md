---
name: code-faq
description: `/code faq` 跨版本知识查询与文档导出。模型在用户查询"用户登录在哪"/"为什么改成这样"或要求导出 REQUIRE.md / DESIGN.md 时调用。查询模式:跨版本搜文档;导出模式:4 种 flag(`--require` / `--design` / `--summary` / `--template`)组合,写文件到用户指定路径。
---

# `/code faq` — 知识查询与导出

> 工作流细节见 [`common.md`](common.md)。

## 目标

- **查询**: 跨版本搜 REQUIRE.md / BUG.md / DESIGN.md,按相关性排序回答
- **导出**: 4 种 flag 组合写到用户指定路径

## 模式矩阵

| 调用 | 行为 |
| --- | --- |
| `[查询词]` | 查询模式: 当前版本优先,无结果跨版本 |
| `--require <REQ> <out>` | 导出 `REQUIRE.md` 到 `<out>` |
| `--design <REQ> <out>` | 导出 `DESIGN.md` 到 `<out>` |
| `--design <REQ> <out> --summary` | 导出概要(§1 概述 + §2 模块名+职责 + §5 决策;不含接口/数据/伪代码) |
| `--require\|--design ... --template <tpl>` | 按 `{{占位符}}` 模板填充;映射见 common.md §4 |

flag 冲突: `--require` + `--design` 同传 → 报错;`--summary` + `--require` → 忽略 summary 继续;`--template` 无导出 flag → 忽略。

## 工作目录

`./assistants/<版本号>/req/` 与 `./assistants/<版本号>/fix/` 下文档 — **只读**。导出文件写到用户指定路径(CWD 下或任意位置)。仅查询模式可不激活版本。

## 不要做的事

- 不修改 `./assistants/` 下任何文件
- 不臆造源文档中不存在的内容
- 不在 `--template` 模板缺失时中断(跳过填充,原样输出)
- 不修改 `<本仓库>` 中除了用户指定输出路径以外的代码文件