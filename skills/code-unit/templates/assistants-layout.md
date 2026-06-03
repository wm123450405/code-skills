# 工作目录布局参考 — code-unit(版本感知)

> `code-unit` 技能强制约定。**本技能的目录粒度是任务(与 `code-it` 同级但路径不同)**——测试工作与开发工作分离存放。
> 本技能受 `code-version` 管理,实际工作空间 = `./assistants/<版本号>/`(由 `./assistants/.current-version` 决定)。

## 整体布局
```
<项目根目录>/
├── assistants/
│   ├── rules/                          ← 项目级规范(只读,跨版本共享)
│   ├── .current-version                ← 当前激活版本标记
│   └── <版本号>/                       ★ 版本工作空间
│       ├── RESULT.md                   ← 版本开发进度看板(可写,本技能会更新测试相关区段)
│       ├── require/<需求编号>/
│       │   └── RESULT.md              ← 上游需求(只读)
│       ├── design/<需求编号>/
│       │   └── RESULT.md              ← 上游概要设计(只读)
│       ├── plan/
│       │   └── <需求编号>/
│       │       ├── RESULT.md          ← 上游详细设计(只读)
│       │       └── PLAN.md            ← 上游任务计划(只读,但本技能会更新本任务测试相关字段)
│       ├── code/
│       │   └── <任务编码>/              ← code-it 产出(只读,作为上下文)
│       │       ├── RESULT.md
│       │       ├── work-log.md
│       │       └── ...
│       └── test/
│           └── <任务编码>/              ← 本技能产出,可写
│               ├── RESULT.md          # 测试改修总结(主产出)
│               ├── work-log.md        # 过程文档:测试编写日志
│               ├── test-results.md    # 过程文档:测试运行结果
│               ├── coverage-analysis.md # 过程文档:覆盖率分析
│               └── deviations.md      # 过程文档:偏离设计/规范
├── src/                                # 用户的项目源码(本技能只读,被测对象)
├── tests/ 或 __tests__/ 或 *_test.go/   # 用户的测试代码(本技能会修改)
├── package.json / pyproject.toml / ...  # 用户的项目配置
└── ...
```

## `code/` 与 `test/` 双目录的设计意图

| 维度 | `assistants/<版本号>/code/<任务编号>/` | `assistants/<版本号>/test/<任务编号>/` |
| --- | --- | --- |
| 写入方 | `code-it` | `code-unit` |
| 内容性质 | 代码改修正文 | 测试改修总结 |
| 状态维度 | 开发状态 | **测试状态** |
| 产出 | `RESULT.md` (改修总结) | `RESULT.md` (测试总结) |
| 修改的 CWD 内容 | 源码 | **测试代码** |

> 同一任务有两份档案:开发档案(code/)和测试档案(test/),互不污染。
> 两个目录都在版本工作空间内,版本切换时一起归档/加载。

## 任务编码格式
- 格式:`<需求编号>-<任务序号>`,如 `REQ-2026-0001-001`
- 来源:`./assistants/<版本号>/plan/<需求编号>/PLAN.md` 的"任务总览"表
- 一经分配不再改变

## 本技能的双主输出
| 输出 | 位置 | 何时写 |
| --- | --- | --- |
| `RESULT.md`(测试总结) | `./assistants/<版本号>/test/<任务编码>/RESULT.md` | 任务完成后 |
| **测试代码变更** | CWD 下的项目测试目录 | 步骤 9-11 持续产出 |
| **测试状态推进** | `./assistants/<版本号>/plan/<需求编号>/PLAN.md` | 步骤 14 |
| **版本看板同步** | `./assistants/<版本号>/RESULT.md` | 步骤 15(任务清单-测试状态 / 缺陷清单 / 变更记录) |

## 本技能会修改的文件清单

| 文件 | 修改内容 | 修改位置 |
| --- | --- | --- |
| CWD 下的项目测试代码 | 实际写/改测试 | 步骤 9-11 |
| `./assistants/<版本号>/test/<任务编码>/work-log.md` | 持续追加测试编写日志 | 步骤 6-15 |
| `./assistants/<版本号>/test/<任务编码>/test-results.md` | 测试运行结果 | 步骤 10-11 |
| `./assistants/<版本号>/test/<任务编码>/coverage-analysis.md` | 覆盖率分析 | 步骤 12 |
| `./assistants/<版本号>/test/<任务编码>/deviations.md` | 偏离记录 + 发现的代码 bug | 步骤 9, 11 |
| `./assistants/<版本号>/test/<任务编码>/RESULT.md` | 测试总结 | 步骤 13 |
| `./assistants/<版本号>/plan/<需求编号>/PLAN.md` | **仅**本任务的**测试相关字段** + 变更记录 | 步骤 14 |
| `./assistants/<版本号>/RESULT.md` | **仅**任务清单-测试状态 / 缺陷清单 / 变更记录 | 步骤 15 |

## 本技能不会修改的文件清单

| 文件 | 原因 |
| --- | --- |
| `./assistants/rules/` 任何文件 | 规范只读(跨版本共享) |
| `./assistants/<版本号>/require/<需求编号>/` 任何文件 | 上游只读 |
| `./assistants/<版本号>/design/<需求编号>/` 任何文件 | 上游只读 |
| `./assistants/<版本号>/plan/<需求编号>/RESULT.md` | 详细设计只读 |
| `./assistants/<版本号>/code/<任务编号>/` 任何文件 | **code-it 的产出,本技能只读** |
| `./assistants/<版本号>/plan/<需求编号>/PLAN.md` 中**开发相关字段** | 开发状态/关键变更等是 `code-it` 的事 |
| `./assistants/<版本号>/RESULT.md` 中非本技能负责的区段 | 各技能分区维护 |
| **CWD 下的项目源码** | **本技能只测不改**;被测代码的修正是 `code-it` 的工作 |

## 与 code-it 的协作协议

**code-it 写代码,code-unit 写测试,二者职责严格分离**:

| 情形 | 谁处理 | code-unit 的动作 |
| --- | --- | --- |
| 测试代码 bug(本测试写错了) | code-unit 自己 | 修测试,重跑 |
| 被测代码 bug(实际代码逻辑错) | **code-it** | 写进 `deviations.md`,**不修代码**,通知用户 |
| 测试设计有争议 | 用户 | 写进 `deviations.md`,停下询问 |

发现被测代码 bug 时,code-unit 的处理:
1. 把 bug 信息(位置、现象、期望、实际、推断根因)写进 `deviations.md`
2. 把测试状态标为 `已运行-失败`(不写"已运行-通过")
3. 通知用户:测试失败,根因是代码 bug,需要回到 `code-it` 修复
4. 修复后,重跑 `code-unit` 验证

## 多项目隔离
不同项目的 `assistants/` 完全独立。

## 跨任务检索
- 同需求的多个任务在 `assistants/<版本号>/test/<需求编号>-*` 下形成序列
- 跨需求时通过需求编码前缀关联
- 复盘时按 `work-log.md` 的时间顺序回放测试过程
- 跨版本(可选):同编码的任务可同时存在于不同版本目录
