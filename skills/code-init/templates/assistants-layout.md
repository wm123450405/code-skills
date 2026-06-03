# 目录结构 — code-init

本技能**只**在 CWD 下创建 `./assistants/` 及其子结构,**不**修改项目源代码。

## 执行前(典型情况)

```
<当前工作目录(CWD)>/
├── <项目源代码...>
├── README.md
├── package.json / go.mod / pyproject.toml / ...
└── ...
```

## 执行后

```
<当前工作目录(CWD)>/
├── assistants/                          # 本技能创建
│   ├── rules/                           # 跨版本共享的编码规范(本技能只创建空目录)
│   ├── .current-version                 # 本技能写入,内容 = <初始版本号>
│   └── <初始版本号>/                     # 基线版本工作空间
│       ├── RESULT.md                    # 版本看板(本技能写入)
│       ├── INIT-REPORT.md               # 功能分析报告(本技能写入,**仅首次初始化**)
│       ├── require/
│       │   ├── EXISTING-001/
│       │   │   └── RESULT.md            # 第一项现有功能需求
│       │   ├── EXISTING-002/
│       │   │   └── RESULT.md            # 第二项现有功能需求
│       │   └── ...                      # 按发现的功能数 N 生成 N 个
│       ├── review/                      # 本技能创建空目录(占位)
│       ├── design/                      # 本技能创建空目录(占位,仅全新项目)
│       ├── plan/                        # 本技能创建空目录(占位,仅全新项目)
│       ├── code/                        # 本技能创建空目录(占位,仅全新项目)
│       └── test/                        # 本技能创建空目录(占位,仅全新项目)
└── <原有项目代码,未做任何修改>
```

## 关键约束

- 本技能**只**创建目录,从不删除任何已存在目录
- 本技能**只**写入 `RESULT.md` / `INIT-REPORT.md` / `EXISTING-NNN/RESULT.md` / `.current-version` 四类文件
- 本技能**不**触碰 `./assistants/rules/` 下任何已存在文件(那是 `code-rule` 的职责)
- 本技能**不**触碰项目源代码(只读分析)

## 文件名约定

- `EXISTING-NNN`:`EXISTING-` 前缀 + 三位数字,从 `001` 起递增
- `INIT-REPORT.md`:固定文件名,大写连字符
- `RESULT.md`:固定文件名,与其他 `code-*` 技能保持一致
