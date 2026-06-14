# 材料登记 — REQ-00027
更新时间:2026-06-08 15:10

| 文件路径 | 类型 | 用途 | 读取状态 | 关键摘要 |
| --- | --- | --- | --- | --- |
| (会话 args) | 文本 | 用户发起本轮 `code-require` 时在 args 中直接给出的需求描述 | 已读 | ① 优化 `/code-fix` 为纯登记型(类似 `code-require`);② 缺陷修复走 `code-plan` → `code-it` → `code-unit` → `code-check`;③ 优化 `/code-auto` 在 BUG-NNN 任务时走此流水线 |
