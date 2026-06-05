# 数据结构完整变更 — REQ-00013
更新时间:2026-06-05 21:30
版本:V0.0.2

## 总体变更范围

**0 新增 / 0 修改 / 0 删除**既有数据模型(NFR-2 强约束零规范变更)。

## 既有数据结构(本轮**不**修改,仅消费)

### 1. `assistants/V<版本>/require/<REQ-NNNNN>/RESULT.md`

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| 第 1 行标题 | markdown H1 | `^# 需求提示词文档 — (.+)$` | — | **本轮消费**:`code-require` / `code-plan` / `code-review` / `code-auto` 解析此行提取"需求标题"|

**本轮变更**:**0**(仅消费,不修改)

### 2. `assistants/V<版本>/plan/<REQ-NNNNN>/PLAN.md`

| 区段 | 字段 | 消费方 |
| --- | --- | --- |
| 任务总览 | "标题"列(第 5 列)| `code-plan` / `code-it` / `code-unit` / `code-review` / `code-auto` 解析此列提取"任务标题"|

**本轮变更**:**0**(仅消费)

### 3. `assistants/V<版本>/fix/<BUG-NNNNN>/RESULT.md`

| 字段 | 类型 | 约束 | 索引 | 说明 |
| --- | --- | --- | --- | --- |
| **新增**"## 缺陷标题" | markdown H2 | `^## 缺陷标题$` | — | **本轮新增**,`code-fix` 步骤 1 末尾追加 |

**本轮变更**:**新增 1 个小节**(在 `fix/.../RESULT.md` 内部,**不**写入看板"缺陷清单"区段,NFR-2 / INV-7 严守)

### 4. `assistants/V<版本>/RESULT.md`(版本看板)

| 区段 | 字段 | 消费方 |
| --- | --- | --- |
| 任务清单 | "标题"列(已存在,V0.0.1 起固定) | `code-publish` PreflightChecker 解析此列 |
| 需求清单 | "标题"列(已存在) | `code-publish` PreflightChecker 解析此列 |
| 缺陷清单 | "标题"列(已存在) | `code-publish` PreflightChecker 解析此列 |

**本轮变更**:**0**(仅消费已存在的"标题"列)

## 模板文件变更

**0 修改**(NFR-2 严守):
- `plugins/code-skills/skills/code-version/templates/version-RESULT.md` — 不修改
- `plugins/code-skills/skills/code-design/templates/design.md` — 不修改
- `plugins/code-skills/skills/code-plan/templates/plan.md` — 不修改
- `plugins/code-skills/skills/code-fix/templates/fix.md` — 不修改(若存在)

## 迁移脚本

**0 迁移脚本**(N/A — 本轮 0 数据库 / 0 配置 / 0 部署脚本变更)

## 与 `data-modeling.md` 自检

- N/A(本仓库无 `data-modeling.md` 规范文件,占位)
- ✅ 0 触发 `dashboard-conventions §规则 1` 3 处同步(看板字段不扩展,INV-5 严守)
