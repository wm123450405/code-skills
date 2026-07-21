---
name: code-help
description: `/code help` 路由失败兜底。当首 token 不在 {ver, req, fix, faq, rule, merge} 中、或用户输入 `/code`(无参)/ `/code help` / `/code --help` / `/code -h` 时触发。输出完整 HELP 文本 + 7 选项 AskUserQuestion 引导。仅屏幕输出,不落盘。
---

# `/code help` — 帮助引导

## 触发条件

| 用户输入 | 行为 |
| --- | --- |
| `/code`(无任何参数) | §A 完整 HELP + 7 选项 AskUserQuestion |
| `/code <未知子命令>` | §B 参数错误 HELP + 7 选项 |
| `/code help` / `--help` / `-h` | §A 完整 HELP |
| `/code <合法参数>` | **跳过帮助**,直接进子命令 |
| 子命令参数异常(如 `/code req` 无描述) | 子命令自身处理(§C) |

## §A — 完整 HELP

```
╔═══════════════════════════════════════════════════════╗
║             /code  · 集成开发入口                    ║
╚═══════════════════════════════════════════════════════╝

  /code 是单一入口。首 token = 子命令。

  ver    版本管理与开发看板
    /code ver                       开发进度看板(无参,推荐先用)
    /code ver <版本号>               切换或创建版本(如 V0.0.5)
    /code ver --publish             发布检查(不切换版本)

  req    需求开发 7 阶段
    /code req <需求描述>             新建需求(自然语言)
    /code req REQ-NNNNN             续跑某条已有需求
    /code req <...> --confirm       每阶段强制确认
    /code req <...> --auto          静默全跑通(!--confirm 互斥)

  fix    缺陷修复 6 阶段
    /code fix <缺陷描述>             新建缺陷
    /code fix BUG-NNNNN             续跑
    /code fix <...> --confirm       每阶段强制确认
    /code fix <...> --auto          静默全跑通

  faq    跨版本知识查询与文档导出
    /code faq <查询词>               知识查询(可留空)
    /code faq --require <REQ> <out>  导出 REQUIRE.md
    /code faq --design  <REQ> <out>  导出 DESIGN.md
    /code faq --design ... --summary  仅导出概要
    /code faq ... --template <tpl>   占位符模板填充

  rule   编码规范追加
    /code rule "<规范描述>"           自动归类入库(只追加不重写)

  merge  worktree 合回主干
    /code merge                      合 origin/main(默认)
    /code merge <branch>             合 origin/<branch>
    仅限 git worktree 内执行
```

### AskUserQuestion 引导

```
你想做什么?
A. /code ver        ← 看开发进度(推荐先调)
B. /code req        ← 开发新需求
C. /code fix        ← 修复缺陷
D. /code faq        ← 查需求/缺陷
E. /code rule       ← 加编码规范
F. /code merge      ← 合并 worktree
G. /code help       ← 再看一次完整帮助
```

## §B — 参数错误 HELP

```
⚠ /code <第一个参数> 不是已识别的子命令。

已识别的 7 个子命令(含帮助):
  ver / req / fix / faq / rule / merge / help

常见误用:
  /code --ver  →  /code ver   (不要给子命令加 --)
  /code help   →  /code       (help 直接调 /code 看完整帮助)
```

## §C — 子命令内部参数异常(责任下沉)

子命令已识别但参数异常时,由各子命令自身承担:

| 子命令 | 异常场景 |
| --- | --- |
| `ver` | 版本号含非法字符 / 未知 flag |
| `req` | 无需求描述 / `--auto` 与 `--confirm` 同时指定 |
| `fix` | 同 req |
| `faq` | 未知 flag / `--require` 的 REQ 不存在 / `--summary` 单用 |
| `rule` | 无规范描述 → 主动询问 |
| `merge` | ≥2 个非空参 → E-M8 |

## 输出规范

- 只屏幕输出,**不**落盘任何文件
- 不调用 `Write` / `Edit` / `Bash`,只用 `Read` / `Glob`
- 显示 HELP 后立即 `AskUserQuestion`,不等待用户重新输入

## 衔接

- 上游: 主 SKILL.md 的路由表(路由失败时)
- 下游: 7 个子命令 SKILL.md(用户最终被引导到对应子命令)