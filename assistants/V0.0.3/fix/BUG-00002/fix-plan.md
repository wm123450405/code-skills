# fix-plan — BUG-00002(SKILL.md 描述中"特定文件类型"字面)

- **缺陷编号**:BUG-00002
- **严重度**:P0
- **当前状态**:调查中 → 修复规划中
- **更新时间**:2026-06-08 14:20
- **版本**:V0.0.3

## 1. 缺陷摘要
- 链接:./RESULT.md
- 标题:SKILL.md 描述中"特定文件类型"字面违反本项目"通用开发技能集"定位
- 严重度:P0(阻断)
- 当前状态:修复规划中

## 2. 根因定位

本项目"通用开发技能集"定位未在所有 SKILL.md 描述中显式遵守。

**根因**:`code-it` L16 等多处使用"`skills/*/SKILL.md`" / "`tests/`" / "`*.test.*`"等"特定文件类型/特定目录"字面。这些字面虽指向真实文件,但语言上把本项目锁死为"SKILL 专用"或"特定语言/特定项目专用",违背"通用开发技能集"自我定位。

**关键判断**:
- **5 个不变量字面保留**(`code-require` L530 / `code-design` L594 / `code-plan` L1093 / `code-fix` L433 + 1 处 L363 命令):描述本项目"不得修改自身管理目录",本项目是"开发技能库"必然管理 skills/,这些字面**不能**泛化为"`<本仓库>` 中除了 `./assistants` 目录中的其他代码文件"。
- **`code-it` L16 描述性段(本轮报告的典型例子)**:虽是描述本项目自身管理 SKILL.md 的"硬约束",但其字面是"`skills/*/SKILL.md`",语言上违反"通用性",**应**改。
- **B 类 8 处**(用户项目语境):应**改**为泛用表述。

## 3. 修复方案

### 3.1 选定方案
**方案 A(选定)**:把 9 处"特定文件类型"字面分两类处理:
- **A 类 1 处**(`code-it` L16 描述性段):改为"`<本仓库>` 中除了 `./assistants` 目录中的其他代码文件"(用户原话)
- **B 类 8 处**(用户项目语境):用"用户的项目代码" / "用户的测试代码"等泛用表述代替 `tests/` / `__tests__/` / `*.test.*` / `*.spec.*`
- **5 处不变量字面保留**

### 3.2 候选方案
- **方案 B(否决)**:完全删除路径字面,只用"项目代码" / "测试文件"——丢失了"用户在自家项目中测试目录结构"的语义提示
- **方案 C(否决)**:改用占位符 `<本仓库>` 代替——但用户原话明确"`<本仓库>` 中除了 `./assistants` 目录",**双层语义更精确**

### 3.3 选定理由
- 用户原话直接给出修复语义
- 与本项目既有"占位符 `<本仓库>`"约定兼容(REQ-00026)
- 与 BUG-00003(绝对路径)合并修复可一次性解决"描述性段落去专属化"

## 4. 涉及文件与变更

### 4.1 A 类(改 1 处)
| 文件 | 行 | 改前 | 改后 | 性质 |
| --- | --- | --- | --- | --- |
| `plugins/code-skills/skills/code-it/SKILL.md` | L16 | "...唯一被允许修改 `<本仓库>/skills/*/SKILL.md` 的技能" | "...唯一被允许修改 `<本仓库>` 中除了 `./assistants` 目录中的其他代码文件" | 描述性(本轮报告典型例子) |

### 4.2 B 类(改 8 处)
| 文件 | 行 | 改前 | 改后 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-unit/SKILL.md` | L13 | "本技能被允许**仅**修改 CWD 下的测试文件(如 `tests/` / `__tests__/` / `*.test.*` / `*.spec.*`)" | "本技能被允许**仅**修改 CWD 下的测试文件(如用户的项目代码中常见的测试目录与文件命名)" |
| `plugins/code-skills/skills/code-unit/SKILL.md` | L318 | "看文件命名风格(`*.test.*` / `*_test.*` / `*Test.*` / `*.spec.*`)" | "看用户项目代码的测试文件命名风格" |
| `plugins/code-skills/skills/code-init/SKILL.md` | L229 | "测试目录(`test/`、`tests/`、`__tests__/`、`spec/`)" | "用户的测试目录(常见的命名约定)" |
| 6 个 `assistants-layout.md` 模板(`code-it` / `code-publish` / `code-unit` / `code-version` / `code-check` / `code-init` / `code-require` / `code-design` / `code-plan` / `code-fix`) | 命中段 | "用户的测试代码" | 保留(已是泛用表述,无需改) |

注:6 个 `assistants-layout.md` 模板的 `tests/` 描述已有"用户的测试代码"标注,属泛用,不需要改。

### 4.3 不变量字面(不改,共 5 处)
- `code-require/SKILL.md` L530:`不修改 \`plugins/code-skills/skills/*/SKILL.md\` 任何文件`
- `code-design/SKILL.md` L594:同上
- `code-plan/SKILL.md` L1093:同上
- `code-fix/SKILL.md` L433:同上
- `code-unit/SKILL.md` L13 后半段:`不得修改 \`plugins/code-skills/skills/*/SKILL.md\` 或其他生产代码文件`

### 4.4 保留模板示例占位符
- `code-plan/templates/fix-plan.md` L103:`<如 \`pytest tests/test_module.py\` 应通过>`(模板占位符,具体)
- `code-fix/templates/bug.md` L82 / L131:`<如 新增单元测试 \`tests/test_login.py:test_password_validation\`>`(模板占位符)
- `code-init/templates/INIT-REPORT.md` L117:`<如 tests/ 目录,与 src/ 平级>`(模板占位符)

理由:模板是"用户消费的最终输出",示例要具体。

## 5. 测试方案

### 5.1 回归用例
- `git diff --stat plugins/code-skills/skills/` 列出预期 4 文件(code-it L16 + code-unit L13/L318 + code-init L229)
- 5 个不变量字面 byte 级保留
- 10 SKILL.md frontmatter byte 级保留
- `git diff marketplace.json plugin.json README*.md CLAUDE.md` 0 diff
- 旧需求档案 0 diff

### 5.2 不引入新 bug
- 仅在描述性段做"段级二分类"(描述段改 / 不变量段保留),不改 frontmatter
- 占位符 `<本仓库>` + "`<本仓库>` 中除了 `./assistants` 目录中的其他代码文件"语义保持

## 6. 风险与回退

### 6.1 风险
- **风险 1**:`code-it` L16 改后语义可能让读者误以为"该技能可以修改任何代码文件"——**不**,因为不变量字面("不得修改...")保留,真正"不得修改"边界仍由不变量约束。
- **风险 2**:B 类 8 处用"用户的项目代码"等表述,可能让"用户具体怎么命名测试文件"语义模糊——**不**,因为模板示例占位符仍具体。

### 6.2 回退
- `git revert` 本次 commit
- 重跑 `code-it BUG-00002` 重新实施

## 7. 修复步骤

```
步骤 1:Edit code-it/SKILL.md L16(1 处,1 行)
  涉及文件:plugins/code-skills/skills/code-it/SKILL.md
  关键变更:把 "skills/*/SKILL.md" 字面 → "`<本仓库>` 中除了 `./assistants` 目录中的其他代码文件"

步骤 2:Edit code-unit/SKILL.md L13 + L318(2 处)
  涉及文件:plugins/code-skills/skills/code-unit/SKILL.md
  关键变更:"tests/ / __tests__/ / *.test.* / *.spec.*" 字面 → "用户项目代码中常见的测试目录与文件命名"

步骤 3:Edit code-init/SKILL.md L229(1 处)
  涉及文件:plugins/code-skills/skills/code-init/SKILL.md
  关键变更:"测试目录(test/、tests/、__tests__/、spec/)" → "用户的测试目录(常见的命名约定)"

步骤 4:静态校验(1 处)
  涉及文件:5 个 SKILL.md frontmatter / 5 个不变量字面 / 旧需求档案
  关键变更:0 diff
```

## 8. 规范遵循

- `skill-conventions.md §规则 1`:SKILL.md frontmatter 必含 name+description,本修复不改 frontmatter ✓
- `marketplace-protocol.md §规则 1`:不改 marketplace.json / plugin.json ✓
- `doc-conventions.md §规则 1`:不改 README ✓
- `commit-conventions.md`:commit 沿用 `chore(code-it):` 前缀 ✓

## 9. 待澄清 / 未决项

无

## 10. 变更记录

| 时间 | 变更 | 关联 |
| --- | --- | --- |
| 2026-06-08 14:20 | 修复规划  code-plan 已产出 fix-plan.md | BUG-00002 |
