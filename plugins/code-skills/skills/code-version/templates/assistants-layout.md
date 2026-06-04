# 工作目录布局参考 — code-version

> `code-version` 技能强制约定。**本技能定义版本工作空间层**,
> 所有其他 `code-*` 技能在此基础上展开工作。

## 整体布局

```
<项目根目录>/
├── assistants/
│   ├── rules/                          ← 项目级规范(跨版本共享,只读)
│   │   ├── architecture.md
│   │   ├── module-conventions.md
│   │   ├── api-standards.md
│   │   └── ...
│   ├── .current-version                ★ 当前激活版本标记文件
│   │                                    内容示例:
│   │                                    v1.0.0
│   │
│   ├── v1.0.0/                         ← 版本工作空间 1(由 code-version 创建)
│   │   ├── RESULT.md                   ★ 版本开发进度看板
│   │   ├── require/                    ← code-require 产出
│   │   │   └── REQ-00001/
│   │   │       ├── RESULT.md
│   │   │       └── ...
│   │   ├── design/                     ← code-design 产出
│   │   │   └── REQ-00001/
│   │   │       ├── RESULT.md
│   │   │       └── ...
│   │   ├── plan/                       ← code-plan 产出
│   │   │   └── REQ-00001/
│   │   │       ├── RESULT.md
│   │   │       ├── PLAN.md
│   │   │       └── ...
│   │   ├── code/                       ← code-it 产出
│   │   │   └── TASK-REQ-00001-00001/
│   │   │       ├── RESULT.md
│   │   │       └── ...
│   │   ├── test/                       ← code-unit 产出
│   │   │   └── TASK-REQ-00001-00001/
│   │   │       ├── RESULT.md
│   │   │       └── ...
│   │   └── review/                     ← code-review 产出
│   │       ├── REQ-00001/
│   │       │   ├── REVIEW-REPORT.md
│   │       │   └── ...
│   │       └── TASK-REQ-00001-00005/
│   │           ├── RESULT.md           (派生"审查改修"任务)
│   │           └── ...
│   │
│   ├── v1.1.0/                         ← 版本工作空间 2(并行或后续)
│   │   ├── RESULT.md
│   │   └── ...
│   │
│   └── <其他历史/并行版本>/
│       └── ...
│
├── src/                                # 用户的项目源码(由 code-it 修改)
├── tests/                              # 用户的测试代码(由 code-unit 修改)
└── ...
```

## 关键点

### 1. 版本层在 `assistants/` 之下

路径模式从原来的:
```
./assistants/plan/需求编号/PLAN.md
```
变为:
```
./assistants/<版本号>/plan/<需求编号>/PLAN.md
```

`code-version` 创建/切换的就是 `<版本号>/` 这一层。

### 2. `rules/` **不**在版本下

项目级编码规范跨所有版本共享,位于 `./assistants/rules/`,**不**放入任何版本目录。
理由:规范是"项目元约定",不随版本变化。

### 3. `.current-version` 是"上下文切换点"

- 内容为单行版本号字符串(如 `v1.0.0\n`)
- 其他 `code-*` 技能在执行前**第一步**就是读它
- 若不存在 → 提示用户先调 `code-version`
- `code-version` 在切换/创建后总是覆写它

### 4. 每个版本工作空间内部结构

每个 `<版本号>/` 下的目录结构由其他 `code-*` 技能按需填充:
- `require/`, `design/`, `plan/`, `code/`, `test/`, `review/` — 6 类产出
- `RESULT.md` — 看板(由 `code-version` 初始化,各 `code-*` 持续更新)

### 5. 与各 code-* 技能的目录粒度对比

| 技能 | 主输出目录 | 路径模式(加入版本层后) |
| --- | --- | --- |
| code-version | 版本级 | `assistants/<version>/` + `assistants/.current-version` |
| code-require | 需求级 | `assistants/<version>/require/<需求编号>/` |
| code-design | 需求级 | `assistants/<version>/design/<需求编号>/` |
| code-plan | 需求级 | `assistants/<version>/plan/<需求编号>/` |
| code-it | 任务级 | `assistants/<version>/code/<任务编码>/` |
| code-unit | 任务级 | `assistants/<version>/test/<任务编码>/` |
| code-review | 需求级 + 任务级 | `assistants/<version>/review/<需求编号>/` + `assistants/<version>/review/<任务编码>/` |

## 多版本隔离

- 不同版本的 `assistants/<version>/` 完全独立,互不污染
- 切换版本 = 改 `.current-version`,不影响历史版本目录
- 删除/归档版本 = 删除/移动 `<version>/` 目录(本技能不提供,属人工操作)

## 跨技能协作:看板同步

每个 `code-*` 技能都负责维护 `./assistants/<version>/RESULT.md` 中自己对应的区段:
- `code-require` → 需求清单
- `code-design` → 概要设计清单
- `code-plan` → 详细设计与任务计划汇总 + 任务清单(首次登记)
- `code-it` → 任务清单(开发状态) + 缺陷清单(若发现)
- `code-unit` → 任务清单(测试状态) + 缺陷清单(若发现)
- `code-review` → 评审发现汇总 + 派生任务记录 + 缺陷清单(若发现)
- 全部 → 变更记录(在自己的关键节点追加)

**写入约束**:
- 各技能只能**追加/更新自己负责的区段**,**不重写**整个看板
- 看板"文档头"和"版本信息"只在 `code-version` 创建/重新初始化时覆写
- 任何"看板字段扩展"需在变更记录中标注

## 多项目隔离

不同项目的 `assistants/` 完全独立。
