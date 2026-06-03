# 看板与版本工作空间规范(dashboard-conventions)

> 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
> 最后更新:2026-06-03 18:50
> 适用版本:跨所有版本共享(项目级)

## 适用场景
本规范适用于 `assistants/` 目录下的"看板/模板/CLAUDE.md"这三类**项目级共享资产**的扩展与同步。涉及"加新区段、改字段约定、调工作流"时查阅本文件。

## 强制级别约定
本文件中各规则的强制级别逐条标注(参见各"规则 N"小节的"强制级别"字段),本文件头部不统一声明。

---

## 规则 1:看板字段约定扩展需多文件同步

### 条款
`./assistants/V<版本号>/RESULT.md`(版本看板)的字段约定(区段、表格列、枚举值)定义在以下三处,必须保持**三方同步**:

| 同步位置 | 路径 | 角色 |
| --- | --- | --- |
| 看板模板 | `plugins/code-skills/skills/code-version/templates/version-RESULT.md` | 各版本 `RESULT.md` 的**实际样板** |
| 字段约定说明 | `plugins/code-skills/CLAUDE.md` 中"看板字段约定"段落 | **给人/AI 看的字段语义与填写规则** |
| 本规范自身 | `./assistants/rules/dashboard-conventions.md` | 跨版本共享的**强约束** |

凡对看板做以下任一扩展,必须**同一次提交**同步更新上述三处(且保持语义一致):

1. 新增/删除/重命名"区段"(如新增"风险登记"区段)
2. 新增/删除/重命名"表格列"(如需求清单新增"评审人"列)
3. 新增/删除/修改"枚举值"(如任务"开发状态"新增"待重新评估")
4. 调整"字段语义说明"(如改变"完成定义"的判定规则)

任一文件未同步更新,视为本规则违反。

### 强制级别
- 必须

### 适用范围
- 跨所有版本(项目级共享) — 适用于 `./assistants/<任意版本号>/RESULT.md` 的任何扩展动作
- 各 `code-*` 技能在改写 `RESULT.md` 字段时也受本规则约束(不得"自定义字段而不通知")

### 正面示例
**场景**:新增"风险登记"区段到看板

**同一次提交内**:
1. `plugins/code-skills/skills/code-version/templates/version-RESULT.md` 中插入"风险登记"段(放在"缺陷清单"与"评审发现汇总"之间)
2. `plugins/code-skills/CLAUDE.md` 中"看板字段约定"段加一句:"风险登记 — 记录本版本中识别到的风险及其缓解措施,字段:风险 ID/描述/级别/状态/缓解人/关联任务"
3. 在本文件 §规则 1 同步追加新规则(若属于"看板字段约定扩展"的新类型)

### 反面示例
```markdown
# 反例 A:改了模板,CLAUDE.md 没改
#   提交内容:
plugins/code-skills/skills/code-version/templates/version-RESULT.md  | 12 +++++++---
#   缺漏:
plugins/code-skills/CLAUDE.md  ← 未同步更新"看板字段约定"段

# 反例 B:改了 CLAUDE.md,模板没改
#   提交内容:
plugins/code-skills/CLAUDE.md  | 8 ++++++++
#   缺漏:
plugins/code-skills/skills/code-version/templates/version-RESULT.md  ← 未同步插入新段
```

### 例外
- **纯排版/格式调整**(如改表格对齐、改链接文本)不触发本规则,只调整样式不影响字段语义
- **历史快照**:`code-version` 在切换到旧版本时,旧版本的 `RESULT.md` 是历史快照,不再受本规则约束(本规则只约束**当前及未来**版本)

### 关联规范
- `./assistants/rules/skill-conventions.md §规则 1`(SKILL.md frontmatter 同步扩展)
- `./assistants/rules/module-conventions.md §规则 1`(技能资源摆放)
- `plugins/code-skills/CLAUDE.md`(同步位置之一)
- `plugins/code-skills/skills/code-version/templates/version-RESULT.md`(同步位置之一)

### 来源
- 由 `code-rule` 技能添加于 2026-06-03 18:50
- 用户原始描述:"看板字段约定扩展需同步更新 `templates/version-RESULT.md` + `CLAUDE.md`"
