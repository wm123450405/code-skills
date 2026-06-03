# 目录结构 — code-rule

本技能操作的目录结构如下:

```
<当前工作目录(CWD)>/
└── assistants/
    └── rules/                       # 项目级规范(本技能产出/扩展)
        ├── architecture.md          # 功能架构
        ├── module-conventions.md    # 模块规划
        ├── naming.md                # 命名约定
        ├── error-handling.md        # 错误处理
        ├── api-standards.md         # 接口定义
        ├── data-modeling.md         # 数据结构
        ├── security.md              # 安全
        ├── performance.md           # 性能
        ├── testing.md               # 测试
        ├── observability.md         # 可观测性
        ├── git-conventions.md       # 提交规范
        └── <其他分类>.md            # 用户自定义分类
```

## 关键约束

- `./assistants/` 与 `./assistants/rules/` 由本技能按需创建(若不存在)
- `./assistants/.current-version` **不**由本技能读写(属于 `code-version` 技能)
- `./assistants/<版本号>/` **不**由本技能读写(属于 `code-version` 技能)
- 本技能只**追加**到已有规范文件,**不**重写或删除既有内容

## 文件名约定

- 英文小写
- 单词之间用 `-` 连接(`error-handling.md`,不是 `error_handling.md`)
- 反映规范**分类**而不是单条规则
- 一类规范一个文件,文件内可有多个"规则 N"小节
