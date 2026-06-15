# 模块详细化 — REQ-00033

更新时间:2026-06-15 12:30
版本:V0.0.3

## 模块清单(本设计 0 新增)

| 模块名 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| — | — | — | (本设计是 SKILL.md 文字改造,无模块变化) | — |

## 唯一改造:`code-require/SKILL.md` §"不要做的事" 小节末尾

### 关键"代码"

**新增条目**(锁定,1 条 Markdown 列表项):
```
- 不涉及技术选型 / 技术栈 / 技术方案的确定:本技能只确定功能点(FR / NFR / 页面 / 交互 / 数据 / 边界);技术选型 / 架构风格 / 接口风格 / 数据模型(库表层) / 部署形态归 `code-design`(由其结合项目实际状况给出方案);没有**必要**进行技术选型的需求,**无需**在 `code-require` 阶段分析技术选型选项。
```

### 调用顺序

不适用(本设计是 SKILL.md 文字改造,无函数调用)

### 状态归属

不适用(本设计是 SKILL.md 文字改造,无运行时状态)

### 错误处理范式

不适用(本设计是 SKILL.md 文字改造,无错误处理)

### 日志埋点

不适用(本设计是 SKILL.md 文字改造,无日志)

### 与概要设计的对应

- `design/.../RESULT.md` §3 决策 D-1(锚点 = §"不要做的事" 小节末尾)
- `design/.../RESULT.md` §3 决策 D-2(对偶引用 `code-design`)
- `design/.../RESULT.md` §9 不变量 INV-1 ~ INV-9

### 符合的规范

- `skill-conventions.md §规则 1`(SKILL.md frontmatter 字节级保留)
- `module-conventions.md`(资源放 `templates/`;本设计**不**改模板)
- `commit-conventions.md`(`chore(<skill>):` 前缀)
- `dashboard-conventions.md`(看板字段三方同步;本设计**不**触发)
