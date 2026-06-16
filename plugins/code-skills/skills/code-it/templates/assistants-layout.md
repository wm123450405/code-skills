# 工作目录布局参考 — code-it(版本感知)

> `code-it` 技能强制约定。**本技能的目录粒度是任务(而非需求)**——每个任务有自己的目录。
> 本技能受 `code-version` 管理,实际工作空间 = `./assistants/<版本号>/`(由 `./assistants/.current-version` 决定)。

## 整体布局
```
<项目根目录>/
├── assistants/
│ ├── rules/ ← 项目级规范(只读,跨版本共享)
│ │ ├── architecture.md
│ │ ├── module-conventions.md
│ │ ├── api-standards.md
│ │ ├── data-modeling.md
│ │ └── ...
│ ├── .current-version ← 当前激活版本标记
│ │ (内容示例:v1.0.0)
│ └── <版本号>/ ★ 版本工作空间
│ ├── RESULT.md ← 版本开发进度看板
│ ├── require/<需求编号>/
│ │ └── RESULT.md ← 上游需求(只读)
│ ├── design/<需求编号>/
│ │ └── RESULT.md ← 上游概要设计(只读)
│ ├── plan/
│ │ └── <需求编号>/
│ │ ├── RESULT.md ← 上游详细设计(只读,审查改修任务不读此文件)
│ │ └── PLAN.md ← 上游任务计划(只读,但本技能会更新本任务开发状态字段)
│ ├── review/<任务编码>/ ← 触发/来源=审查改修 时的输入源(只读)
│ │ └── RESULT.md
│ └── code/
│ └── <任务编码>/ ← 本技能产出,可写
│ ├── RESULT.md # 改修总结(主产出)
│ ├── work-log.md # 过程文档:开发过程日志
│ ├── compile-and-run.md # 过程文档:编译/启动验证
│ ├── deviations.md # 过程文档:偏离设计/规范
│ └── test-results.md # 过程文档:测试结果(若适用)
├── src/ # 用户的项目源码(本技能会修改)
├── package.json / pyproject.toml / ... # 用户的项目配置
├── tests/ # 用户的测试代码(本技能可能修改)
└── ...
```

## 与其他技能目录粒度的对比

| 技能 | 目录粒度 | 路径 |
| --- | --- | --- |
| code-version | 版本级 | `assistants/<version>/` + `assistants/.current-version` |
| code-require | 需求级 | `assistants/<version>/require/<需求编号>/` |
| code-design | 需求级 | `assistants/<version>/design/<需求编号>/` |
| code-plan | 需求级 | `assistants/<version>/plan/<需求编号>/` |
| **code-it** | **任务级** | `assistants/<version>/code/<任务编码>/` |
| code-unit | 任务级 | `assistants/<version>/test/<任务编码>/` |
| code-check | 需求级 + 任务级 | `assistants/<version>/review/<需求编号>/` + `assistants/<version>/review/<任务编码>/` |

为什么 code-it 用任务级?
- code-it 是流水线中**唯一实际改动生产代码的技能**
- 任务级粒度让每次开发工作的过程文档(`work-log.md` / `compile-and-run.md` / `deviations.md`)有独立归宿
- 多个任务可被不同人或同一人在不同时间执行,互不污染
- 任务的整个生命周期(开始 → 进行中 → 完成 → 复盘)有完整档案

## 任务编码格式
- 格式:`TASK-(REQ|BUG)-NNNNN-NNNNN`,如 `TASK-REQ-00001-00001`
- 来源:`./assistants/<版本号>/plan/<需求编号>/PLAN.md` 的"任务总览"表
- 一经分配不再改变,与任务状态无关

## 触发/来源决定输入源
| 触发/来源 | 输入源 |
| --- | --- |
| 大多数(`需求新增` / `设计变更` / ...) | `./assistants/<版本号>/plan/<需求编号>/RESULT.md` |
| **`审查改修`** | `./assistants/<版本号>/review/<任务编码>/RESULT.md`(**不读** plan/RESULT.md) |
| `需求撤回` | 任务标"已取消",无输入 |

## 本技能的双主输出
| 输出 | 位置 | 何时写 |
| --- | --- | --- |
| `RESULT.md`(改修总结) | `./assistants/<版本号>/code/<任务编码>/RESULT.md` | 任务完成后 |
| **代码变更** | CWD 下的项目源码 | 步骤 8–12 持续产出 |
| **开发状态推进** | `./assistants/<版本号>/plan/<需求编号>/PLAN.md` | 步骤 7(开始)+ 步骤 14(完成) |
| **版本看板同步** | `./assistants/<版本号>/RESULT.md` | 步骤 14,15(任务清单 / 缺陷清单 / 执行的开发命令记录 / 变更记录) |

> 重要:本技能对 `PLAN.md` 的修改**仅限**本任务的状态/完成字段/变更记录,绝不能修改其他任务。
> 重要:本技能对 `<版本号>/RESULT.md` 的修改**仅限**本技能负责的区段,不能改其他区段。

## 本技能会修改的文件清单

| 文件 | 修改内容 | 修改位置 |
| --- | --- | --- |
| CWD 下的项目源码 | 实际编码 | 步骤 8 |
| `./assistants/<版本号>/code/<任务编码>/work-log.md` | 持续追加开发日志 | 步骤 4–15 |
| `./assistants/<版本号>/code/<任务编码>/compile-and-run.md` | 编译/启动验证记录 | 步骤 9–12 |
| `./assistants/<版本号>/code/<任务编码>/deviations.md` | 偏离记录 | 步骤 8, 12 |
| `./assistants/<版本号>/code/<任务编码>/test-results.md` | 测试结果 | 步骤 11–12 |
| `./assistants/<版本号>/code/<任务编码>/RESULT.md` | 改修总结 | 步骤 13 |
| `./assistants/<版本号>/plan/<需求编号>/PLAN.md` | **仅**本任务的开发状态/完成字段 + 变更记录 | 步骤 7, 14 |
| `./assistants/<版本号>/RESULT.md` | **仅**本技能负责的区段(任务清单 / 缺陷清单 / 执行的开发命令记录 / 变更记录) | 步骤 15 |

## 本技能不会修改的文件清单

| 文件 | 原因 |
| --- | --- |
| `./assistants/rules/` 任何文件 | 规范只读,变更需用户处理 |
| `./assistants/<版本号>/require/<需求编号>/` 任何文件 | 上游只读,变更需重跑 code-require |
| `./assistants/<版本号>/design/<需求编号>/` 任何文件 | 上游只读,变更需重跑 code-design |
| `./assistants/<版本号>/plan/<需求编号>/RESULT.md` | 详细设计只读,**审查改修任务明确不读此文件** |
| `./assistants/<版本号>/plan/<需求编号>/PLAN.md` 中其他任务的内容 | 任务独立,不可越界 |
| `./assistants/<版本号>/RESULT.md` 中非本技能负责的区段 | 各技能分区维护 |

## 多项目隔离
不同项目的 `assistants/` 完全独立。

## 跨任务检索
- 同需求的多个任务在 `assistants/<版本号>/code/<需求编号>-*` 下形成序列
- `RESULT.md` 中"关联任务"字段记录任务间依赖
- 复盘时按 `work-log.md` 的时间顺序回放
- 跨版本(可选):同编码的任务可同时存在于不同版本目录
