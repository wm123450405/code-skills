# 关联概要设计 — REQ-00015
更新时间:2026-06-06 09:00
版本:V0.0.2

## 同版本(V0.0.2)关联设计
| REQ | 标题 | 关联点 |
| --- | --- | --- |
| REQ-00004 | `/code-dashboard` | FR-6 看板自检**复用**其"算法 1 + 算法 5"(5 区段表格行计数) |
| REQ-00005 | 首步拉取+末步提交 | FR-2 commit 格式 `chore(<scope>): ...` 同源 |
| REQ-00006 | `/code-publish` | FR-6 自检**不**阻塞 publish 流程(同源"非阻塞警告"语义) |
| REQ-00007 | `/code-auto` | **不**调用 code-merge(NFR-7 + Q-P7 锁定,职责分离) |
| REQ-00010 | 优化 `/code-it` 前置任务守卫 | FR-6 看板自检的"任务清单"区段检查与 code-it 同源 |
| REQ-00013 | 优化 6 技能,启用"编号+标题"显示 | INV-1 严守(code-merge **不**触发 dashboard 3 文件同步) |

## 跨版本关联(可选)
- 无(本需求是 V0.0.2 内的纯新增,无跨版本依赖)

## 关键横向引用
- **`code-dashboard` 算法 1**:5 区段定位 + 表格行计数
- **`code-dashboard` 算法 5**:统计行匹配(形如 `**统计**:N` / `总数:N`)
- **`code-it` 步骤 N 末尾兜底提交**:`chore(<scope>): <description>` 格式
- **`code-require` 状态机 Mermaid 风格**:本设计 §4 状态机沿用
- **`code-publish` PreflightChecker 风格**:本设计 FR-1~FR-8 各步打印沿用

## 冲突点
**0** —— 本需求与既有 12 个 `code-*` 的契约**无冲突**:
- 不修改既有 SKILL.md(INV-1)
- 不修改 marketplace.json 其他字段(INV-2)
- 不修改 plugin.json(INV-3)
- 不实现 v1 follow-up(INV-7)
