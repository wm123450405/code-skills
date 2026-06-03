# 工作目录布局参考 — code-design(版本感知)

> `code-design` 技能强制约定。所有路径以**当前工作目录(CWD)**为基准。
> 本技能受 `code-version` 管理,实际工作空间 = `./assistants/<版本号>/`(由 `./assistants/.current-version` 决定)。

## 整体布局
```
<项目根目录>/
├── assistants/
│   ├── rules/                          ← 项目级规范(只读,跨版本共享)
│   │   ├── architecture.md             例:功能架构规范
│   │   ├── module-conventions.md       例:模块规划规范
│   │   ├── api-standards.md            例:接口定义规范
│   │   ├── data-modeling.md            例:数据结构规范
│   │   ├── security.md                 例:安全规范(可选)
│   │   ├── performance.md              例:性能规范(可选)
│   │   └── ...
│   ├── .current-version                ← 当前激活版本标记
│   │   (内容示例:v1.0.0)
│   └── <版本号>/                       ★ 版本工作空间
│       ├── RESULT.md                   ← 版本开发进度看板
│       ├── require/
│       │   └── REQ-2026-0001/
│       │       ├── RESULT.md            ← 上游,本技能只读
│       │       └── ...
│       └── design/
│           ├── REQ-2026-0001/
│           │   ├── RESULT.md            # 本技能产出
│           │   ├── materials-index.md
│           │   ├── design-notes.md
│           │   ├── module-breakdown.md
│           │   ├── dependencies.md
│           │   ├── related-designs.md
│           │   ├── rule-compliance.md
│           │   └── clarifications.md
│           ├── REQ-2026-0002/
│           │   └── ...
│           └── REQ-2025-0099/
│               └── ...
├── src/                                # 用户的项目源码
├── package.json / pyproject.toml / ... # 用户的项目配置
└── ...
```

## 三类目录的只读/可写关系

| 目录 | 写入方 | 本技能态度 |
| --- | --- | --- |
| `./assistants/rules/` | 用户(项目负责人) | **只读**。规范变更后,需要重跑 `code-design` 让本次设计同步 |
| `./assistants/<版本号>/require/<需求编码>/` | 用户 / `code-require` | **只读**。需求变更后,需要重跑 `code-design` |
| `./assistants/<版本号>/design/<需求编码>/` | 本技能 | **可写**。增量更新时只编辑变化处,稳定章节不重写 |
| `./assistants/<版本号>/RESULT.md` | code-version 初始化;本技能追加"概要设计清单"区段 | 只能追加,不能重写其他区段 |
| CWD 下的项目源码 | 用户 / 后续 `code-it` | 本技能只读,只用于"结合现状" |

## `rules/` 目录使用建议

- **建议存在**:规范是 design 输出的硬约束,缺失规范时本技能会询问是否继续
- **文件命名**:建议按"功能类别"命名,例如:
  - `architecture.md` / `模块架构规范.md`
  - `api-standards.md` / `接口规范.md`
  - `data-modeling.md` / `数据建模规范.md`
  - `security.md` / `performance.md` / `testing.md` / `observability.md` ...
- **格式建议**:用 Markdown,一级标题对应类别,二级标题对应具体条款
- **作用范围**:项目级(整个仓库),**跨版本共享**——不是单需求
- **修改流程**:规范修改后,本技能在增量更新时会自动识别"规范侧变更",并触发相应章节的复核
- **若某需求有特殊规范**:在 `rule-compliance.md` 的"用户授权的偏离"区记录,而不是新建规范文件

## 与 code-require 的关系
- 本技能不修改 `./assistants/<版本号>/require/<需求编码>/` 下的任何内容,只读
- 读取上游 `RESULT.md` 后,把关键 FR/NFR 摘要写到本目录的 `materials-index.md` 中(冗余存储,避免上游改动影响本次设计)

## 用户 vs 技能产出
| 类别 | 写入方 | 修改方 |
| --- | --- | --- |
| `<版本号>/design/<需求编码>/RESULT.md` | 技能 | 技能(增量更新) |
| 过程文档 | 技能 | 技能 |
| `<版本号>/RESULT.md` | code-version + 各技能 | 只能追加区段 |
| `./assistants/rules/` | 用户 | 用户(本技能不写) |
| `./assistants/<版本号>/require/<需求编码>/` | 用户 / code-require | 用户 / code-require(本技能只读) |
| CWD 下的项目源码 | 用户 | 用户 / 后续 code-it |

> 用户不应手动改 `RESULT.md`。如有调整请:
> - 改规范 → 改 `./assistants/rules/`,再重跑 `code-design`
> - 改需求 → 改上游材料,重跑 `code-require`,再重跑 `code-design`
> - 改设计 → 直接重跑 `code-design`,在步骤 5 选择增量更新分支

## 多项目隔离
不同项目的 `assistants/` 完全独立。跨项目不会误检索到对方的规范/需求/设计。

## 跨设计检索
本技能会扫描 `./assistants/<版本号>/design/*/RESULT.md` 寻找关联设计(同版本);
可选:跨版本扫描 `./assistants/*/design/*/RESULT.md`(需用户授权)。
为保证检索质量:
- 关键模块名/接口名/数据结构名在 `RESULT.md` 中保持一致命名
- 详细字段放在 `module-breakdown.md` / `dependencies.md` / `rule-compliance.md`,`RESULT.md` 只放概要
- 跨版本关联时,在 `related-designs.md` 中注明"所在版本"
