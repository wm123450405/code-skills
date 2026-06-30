# 需求提示词文档 — REQ-00043 · 移除 fix-plan.md 废弃引用

> 上游:`./assistants/V0.0.4/require/REQ-00043/`(材料源自用户对话)
> 遵循规范:`./assistants/rules/`(若存在)

## 1. 需求概述

`fix-plan.md` 是已废弃的文件名。`code-fix` 用于登记缺陷,`code-plan` 用于缺陷路径规划,实际产出 `RESULT.md` 和 `PLAN.md`,不会产出 `fix-plan.md`。但多个技能文件和 README 中仍存在对 `fix-plan.md` 的引用,需要清理。

(源自:用户对话输入)

## 2. 背景与目标

### 背景
- REQ-00019(V0.0.2)已将 `code-plan` BUG 路径从"产单文件 `fix-plan.md`"升级为"产 `RESULT.md` + `PLAN.md` + 过程文档"的 REQ 同构模式
- `code-fix` 技能明确声明不产出 `fix-plan.md`
- 但 `CLAUDE.md`、`code-auto/SKILL.md`、`code-fix/SKILL.md`、`code-fix/templates/`、`README.md`、`README.en.md` 中仍有残留引用

### 目标
1. 移除所有 `plugins/code-skills/` 下对 `fix-plan.md` 的引用
2. 替换为对 `PLAN.md`(修复方案)和 `RESULT.md`(缺陷详情)的正确引用

## 3. 用户角色与场景

- **技能调用者(AI)**:不会因读到 `fix-plan.md` 而误判文件存在性
- **技能维护者**:文档中不再引用废弃文件名

## 4. 功能需求(FR)

### FR-1: 清理 CLAUDE.md 中的 fix-plan.md 引用
- **文件**:`CLAUDE.md`
- **修改**:`fix-plan.md` → `PLAN.md`

### FR-2: 清理 code-auto/SKILL.md 中的 fix-plan.md 引用
- **文件**:`plugins/code-skills/skills/code-auto/SKILL.md`
- **修改**:`fix-plan` → `PLAN`

### FR-3: 清理 code-fix/SKILL.md 中的 fix-plan.md 引用
- **文件**:`plugins/code-skills/skills/code-fix/SKILL.md`
- **修改**:所有 `fix-plan.md` 引用替换为 `PLAN.md`(修复方案)或 `RESULT.md`(缺陷详情)

### FR-4: 清理 code-fix/templates/ 中的 fix-plan.md 引用
- **文件**:`assistants-layout.md`、`fix-registry.md`、`bug.md`
- **修改**:`fix-plan.md` → `PLAN.md`

### FR-5: 清理 README.md / README.en.md 中的 fix-plan.md 引用
- **文件**:`README.md`、`README.en.md`
- **修改**:`fix-plan.md` → `PLAN.md`

(源自:用户需求描述)

## 5. 非功能需求 / 约束(NFR)

### NFR-1: 不修改 assistants/ 历史工作产物
- `assistants/` 下的历史文件保留不变

### NFR-2: 不修改 rules/ 目录
- `skill-conventions.md` 中 `fix-plan.md` 作为"退场文件名"示例保留

### NFR-3: 不修改 skill-conventions.md
- 该文件将 `fix-plan.md` 列为退场文件名的示例,属于规范定义,不应修改

## 6. 页面与界面

不涉及。

## 7. 交互逻辑

不涉及。

## 8. 数据与状态

| 文件 | 修改类型 | 预计改动行数 |
| --- | --- | --- |
| CLAUDE.md | 替换 | 1 处 |
| code-auto/SKILL.md | 替换 | 1 处 |
| code-fix/SKILL.md | 替换 | ~15 处 |
| code-fix/templates/assistants-layout.md | 替换 | 2 处 |
| code-fix/templates/fix-registry.md | 替换 | 1 处 |
| code-fix/templates/bug.md | 替换 | 3 处 |
| README.md | 替换 | ~8 处 |
| README.en.md | 替换 | ~8 处 |

## 9. 边界与异常

- **E-1: assistans/ 历史文件**:不修改。历史 `fix-plan.md` 文件本身(如 BUG-00002/fix-plan.md)保留
- **E-2: skill-conventions.md**:不修改。该文件将 `fix-plan.md` 列为退场文件名示例
- **E-3: code-plan/templates/fix-plan.md**:模板文件本身保留(留作历史)

## 10. 验收标准(AC)

### AC-1: CLAUDE.md 无 fix-plan.md 引用
- `grep fix-plan CLAUDE.md` 返回空

### AC-2: code-auto/SKILL.md 无 fix-plan.md 引用
- `grep fix-plan plugins/code-skills/skills/code-auto/SKILL.md` 返回空

### AC-3: code-fix/SKILL.md 无 fix-plan.md 引用
- `grep fix-plan plugins/code-skills/skills/code-fix/SKILL.md` 返回空(自身声明"不产出 fix-plan.md"的条款除外)

### AC-4: code-fix/templates/ 无 fix-plan.md 引用
- `grep fix-plan plugins/code-skills/skills/code-fix/templates/` 返回空

### AC-5: README.md / README.en.md 无 fix-plan.md 引用
- `grep fix-plan plugins/code-skills/README.md plugins/code-skills/README.en.md` 返回空

## 11. 关联需求

| 关联需求 | 版本 | 关联点 |
| --- | --- | --- |
| REQ-00019 | V0.0.2 | BUG 路径从 fix-plan.md 升级为 RESULT.md + PLAN.md 同构 |
| REQ-00036 | V0.0.3 | 技能文档开发痕迹清理,已将 fix-plan.md 列为退场文件名 |

## 12. 待澄清 / 未决项

无。

## 13. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-29 00:00 | v1 | 初始创建 | 需求分析完成,共 5 条 FR / 3 条 NFR / 5 条 AC | wangmiao |