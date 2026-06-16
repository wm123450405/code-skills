# 发布部署 Q&A — <本版本号>

> 本手册聚合自 `assistants/qanda/`,供发布部署中遇到问题时查阅。
>
> ⚠ **本手册当前为占位状态** — `assistants/qanda/` 目录中暂无 Q&A 内容(仅 `README.md`)。请按下方"## 占位:常见问题(待补充)"的提示添加 Q&A 后,再重跑 `code-publish` 生成充实版。

---

## 占位:常见问题(待补充)

本节为**占位章节**;在 `assistants/qanda/` 目录中添加 Q&A 内容后,本节会被 `code-publish` 技能自动替换为 N 个聚合章节(每个对应一个 qanda .md 文件)。

### 如何添加 Q&A 内容

1. **阅读格式规范**:`assistants/qanda/README.md` 说明了目录用途、文件命名建议、引用规范
2. **创建 Q&A 文件**:在 `assistants/qanda/` 目录下新建 `<主题>.md`(例:`deploy-faq.md` / `db-init-faq.md` / `rollback-faq.md`)
3. **写入 Q&A 内容**:每个文件用 Markdown 写 1 个或多个 Q&A,示例结构:
 ```markdown
 # <主题>常见问题
 
 ## Q: <问题 1>
 A: <答案 1>
 
 ## Q: <问题 2>
 A: <答案 2>
 ```
4. **重跑 `code-publish`**:在 Claude Code 中调 `/code-publish`(或 `/code-publish <本版本号>`),`code-publish` 会自动:
 - 读取 `assistants/qanda/*.md`(排除 `README.md`)
 - 在本占位章节**之前**插入 N 个 `## <主题>(来源:qanda/<文件>)` 章节
 - 内容为各文件的全文

### 完整生成结果示例(假设 qanda/ 有 2 个文件)

添加 `assistants/qanda/deploy-faq.md` + `assistants/qanda/db-init-faq.md` 后,重跑 `code-publish` 会得到:

```markdown
# 发布部署 Q&A — V0.0.2

> 本手册聚合自 `assistants/qanda/`,供发布部署中遇到问题时查阅。

## 1. deploy-faq(来源:qanda/deploy-faq.md)
# 部署常见问题
## Q: 服务启动失败怎么办?
A: ...

## 2. db-init-faq(来源:qanda/db-init-faq.md)
# 数据库初始化常见问题
## Q: ...
A: ...

---

## 占位:常见问题(待补充)
(本节保留作为兜底,实际不再有内容)
```

### 排除规则

`code-publish` 聚合时**自动排除** `assistants/qanda/README.md`(避免把"目录说明"当 Q&A 内容)。

### 排序规则

聚合章节按**文件名字典序**排序,确保幂等(重跑结果一致)。
