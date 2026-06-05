# 数据结构完整变更 — REQ-00016
更新时间:2026-06-05 16:15
版本:V0.0.2

> 本需求**不**修改任何数据库表 / ORM 模型 / 数据迁移脚本;主数据结构 = 2 个 SKILL.md 增量追加(纯文本)。
>
> 全部数据结构都是**纯文本 / Markdown**,无 schema 变更、无类型校验、无索引、无外键。

---

## 修改数据结构 1:既有 `code-design/SKILL.md` — **增量追加 2 段,不修改既有**

### 路径
- `plugins/code-skills/skills/code-design/SKILL.md`

### 字段(沿用既有)
- 既有 1-15 步骤 / 既有 5 章节字面 — **字节级不变**(INV-1 / INV-5 / INV-12 / INV-13)

### 字段级变更
**2 段新增**(锚点 A + 锚点 B):
- 锚点 A("步骤 0"末尾 + 空行):`### 步骤 0.5 — 模式选择(本需求新增,快模式入口)`(接口 6 字面)
- 锚点 B("步骤 N 步骤 3"末尾 + 空行):`### 步骤 N 步骤 3.5 — 模式分支判断(本需求新增,快模式末尾兜底跳过 3 选 1)`(接口 7 字面)

### 写入策略
- Edit 工具(增量追加,非 Write)
- 严格按锚点字面(INV-12)
- Grep 自检既有字面不变

### 依据规范
- FR-5(完整模式字节级不变)
- INV-1 / INV-4 / INV-5 / INV-12 / INV-13

---

## 修改数据结构 2:既有 `code-plan/SKILL.md` — **增量追加 2 段,不修改既有**

### 路径
- `plugins/code-skills/skills/code-plan/SKILL.md`

### 字段(沿用既有)
- 既有 1-18 步骤 / 既有 5 章节字面 — **字节级不变**

### 字段级变更
- 锚点 A("步骤 0"末尾 + 空行):`### 步骤 0.5 — 模式选择(本需求新增,快模式入口)`(接口 6 字面,2 个文件共享)
- 锚点 B("步骤 N 步骤 3"末尾 + 空行):`### 步骤 N 步骤 3.5 — 模式分支判断(本需求新增,快模式末尾兜底跳过 3 选 1)`(接口 7 字面,2 个文件共享)

### 写入策略
- Edit 工具(增量追加,非 Write)
- 严格按锚点字面

### 依据规范
- FR-5(完整模式字节级不变)
- INV-1 / INV-4 / INV-5 / INV-12 / INV-13

---

## 不修改的数据结构

- `code-design/SKILL.md` frontmatter(L1-3)— 字节级不变(INV-4)
- `code-design/SKILL.md` 既有 1-15 步骤字面 — 字节级不变(INV-1 / INV-5)
- `code-design/SKILL.md` 既有 5 章节字面 — 字节级不变(INV-13)
- `code-design/templates/{design,assistants-layout}.md` — 字节级不变(INV-13 隐含)
- `code-plan/SKILL.md` frontmatter(L1-3)— 字节级不变(INV-4)
- `code-plan/SKILL.md` 既有 1-18 步骤字面 — 字节级不变(INV-1 / INV-5)
- `code-plan/SKILL.md` 既有 5 章节字面 — 字节级不变(INV-13)
- `code-plan/templates/{plan,task-plan,fix-plan,assistants-layout}.md` — 字节级不变(INV-13 隐含)
- 其他 11 个 `code-*/SKILL.md` — 字节级不变(INV-6)
- `marketplace.json` / `plugin.json` — 字节级不变(INV-7)
- `assistants/rules/` 下 13 个规范文件 — 字节级不变(INV-7)
- `plugins/code-skills/README.md` / `README.en.md` — 字节级不变(INV-7)
- `plugins/code-skills/CLAUDE.md` — 字节级不变(INV-7)

---

## 数据结构自检结论

- ✅ 0 新增数据库表 / ORM / schema
- ✅ 0 新增索引 / 外键
- ✅ 0 数据迁移脚本
- ✅ 2 个数据结构变更(均为 2 个 SKILL.md 增量追加,均为文本文件)
- ✅ 13 项 INV 全部满足
- ✅ 100% 沿用既有 5 模板
