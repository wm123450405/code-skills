# 编码规范占位 — code-it

> 由 `code-it` 技能引用。**真正的项目级编码规范应在 `./assistants/rules/` 下**,
> 本文件只放一些"通用编码原则"作为兜底,具体项目应通过 `rules/` 提供专属规范。

## 通用原则(兜底)

### 命名
- 变量/函数:`lowerCamelCase`(JS/TS) / `snake_case`(Python/Rust) / `PascalCase`(类/类型)
- 常量:`UPPER_SNAKE_CASE`
- 文件:`kebab-case`(前端/通用) / `snake_case`(Python) / `PascalCase`(React 组件)

### 函数/方法
- 单一职责
- 入参 ≤ 3 个,超过用对象包装
- 早返回,避免深层嵌套
- 默认参数放末尾

### 错误处理
- **不吞异常**:接住就要处理或重新抛出
- 边界条件显式处理(空、null、超长、并发)
- 错误信息要带上下文(哪个对象/哪个步骤)
- 区分业务异常和系统异常

### 日志
- 关键路径埋点(进入/退出/分支)
- 日志带请求 ID / 追踪 ID
- 不在循环里打 INFO
- 敏感数据脱敏(密码/token/手机号)

### 注释
- 解释"为什么",不解释"是什么"
- 公共 API 必须有 JSDoc/docstring
- TODO 注释带负责人 + 期望完成时间

### 依赖
- 引入新依赖前确认:必要性、许可、维护活跃度、是否有项目内可复用替代
- 锁版本(`package-lock.json` / `poetry.lock` / `go.sum` / `Cargo.lock`)
- 依赖在 `dependencies.md` 中已记录(code-design 阶段)

## 建议
各项目在 `./assistants/rules/` 下提供:
- `architecture.md` / `模块架构规范.md`
- `module-conventions.md` / `模块组织规范.md`
- `api-standards.md` / `接口规范.md`
- `data-modeling.md` / `数据建模规范.md`
- `security.md` / `安全规范.md`
- `performance.md` / `性能规范.md`
- `testing.md` / `测试规范.md`
- `observability.md` / `可观测性规范.md`
- `git-conventions.md` / `Git 规范.md`(提交信息格式、分支策略)
