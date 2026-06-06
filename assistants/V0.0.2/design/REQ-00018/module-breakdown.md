# 模块拆分 — REQ-00018
更新时间:2026-06-06 13:00
版本:V0.0.2
需求编码:REQ-00018

## 模块变更清单(本需求只改 1 个)

| 模块 / 路径 | 状态 | 职责(一句话) | 涉及接口 | 依赖(对内) | 关键决策 | 规范依据 |
| --- | --- | --- | --- | --- | --- | --- |
| `plugins/code-skills/skills/code-version/SKILL.md` | **修改既有** | 优化 `code-version` 技能,在步骤 6 后追加"步骤 7 CWD 描述文件同步" | 既有 0 个对外接口,**不**新增 | 既有 0 个对内依赖,**不**新增 | D-1 增量追加锚点 = "## 工作流程" 段后 / "## 看板字段约定" 段前 | skill-conventions §规则 1 / module-conventions §规则 1 |

## 明确**不**修改的模块(12 个其他技能)

| 模块 / 路径 | 状态 | 理由 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-init/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-rule/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-require/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-design/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-it/SKILL.md` | 不修改 | NNR-3 强约束 |
| `plugins/code-skills/skills/code-unit/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-fix/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-review/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-publish/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-merge/SKILL.md` | 不修改 | NFR-3 强约束 |
| `plugins/code-skills/skills/code-auto/SKILL.md` | 不修改 | NFR-3 强约束 |

## 明确**不**修改的 `code-skills` 自身产物

| 文件 | 理由 |
| --- | --- |
| `.claude-plugin/marketplace.json` | NFR-4 强约束(Q-1 锁定) |
| `plugins/code-skills/.claude-plugin/plugin.json` | NFR-4 强约束 |
| `plugins/code-skills/README.md` / `README.en.md` | NFR-4 强约束 |
| `plugins/code-skills/CLAUDE.md` | NFR-4 强约束 |
| `./assistants/rules/` 13 份规范 | NFR-5 强约束 |
| `plugins/code-skills/skills/code-version/templates/version-RESULT.md` | NFR-6 强约束 |

## 步骤 7 子小节结构(注入到 SKILL.md)

```
## 步骤 7 — CWD 描述文件版本号同步(REQ-00018 新增)

### 7.1 目标
- 在 code-version 步骤 6 之后,扫描 CWD 下的已知工程类型描述文件,同步版本号到新激活的 <版本号>

### 7.2 触发条件
- code-version 步骤 3 决定激活此版本后(情形 A/B/C/D 任意一种,选 A/B/C 时触发;选 C 取消时不触发)

### 7.3 算法
- [7 步伪代码:解析 argv → Glob 6 类 → 对每命中文件 Edit → 屏幕输出]

### 7.4 通过条件
- 成功:屏幕输出 1+ 行 ✓ 日志
- 0 命中:屏幕输出 ⚠
- 失败不阻断(NFR-8):退出码仍 0

### 7.5 屏幕输出契约
- [5 类:✓ 成功 / ⚠0 命中 / ⚠解析失败 / ⚠缺版本号字段 / ⚠go.mod]

### 7.6 边界与异常
- [E-1 ~ E-8 共 8 个边界场景]

### 7.7 性能
- 单文件 ~1 秒;monorepo 10 个文件 ~5 秒

### 7.8 与步骤 1~6 协同
- 不修改既有步骤 1~6 的语义
```

## 关键决策:为什么改 SKILL.md 而不改其他位置

- **改 SKILL.md**:1 个文件 / 1 个小节追加 / 0 新文件 / 0 新依赖 — 最小变更
- **改 templates/**:违背"技能资源放固定子目录"(module-conventions §规则 1)— SKILL.md 是技能入口,append 锚点对齐
- **新设子技能**:过度抽象 — 1 个步骤不值得拆
- **改 markdown-it 解析**:引入新依赖(违反 NFR-1 零依赖)
