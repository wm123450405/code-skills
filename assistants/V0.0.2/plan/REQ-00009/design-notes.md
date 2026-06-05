# 详细设计笔记 — REQ-00009
更新时间:2026-06-05 17:20
版本:V0.0.2

## 关键实现细节决策

### P-D1:`package.json` 验证 `scripts.test` 的具体判定
- **问题**:`package.json` 存在但 `scripts.test` 是空字符串 / `null` / 不存在,如何判定?
- **选定**:`"test" in scripts and scripts["test"]` 非空字符串 → 才算命中
- **理由**:`code-unit` 守卫通过后会跑 `npm test`,空字符串 / null 会失败
- **伪代码**:
  ```python
  scripts = json["scripts"]  # 缺省为 {}
  if "test" in scripts and isinstance(scripts["test"], str) and scripts["test"].strip():
      hit = True
  else:
      hit = False
  ```

### P-D2:`pyproject.toml` 验证测试配置的具体判定
- **问题**:`pyproject.toml` 存在但无 `[tool.pytest]` / `[tool.pytest.ini_options]` 等,如何判定?
- **选定**:存在以下任一 → 命中:`[tool.pytest]` / `[tool.pytest.ini_options]` / `[tool.tox]` / `[tool.nox]`
- **理由**:这是 Python 生态中最常见的 4 种测试配置入口
- **伪代码**:
  ```python
  toml_keys = set(toml.keys())  # top-level keys
  test_tool_keys = {"tool.pytest", "tool.pytest.ini_options", "tool.tox", "tool.nox"}
  hit = any(key in toml_keys for key in test_tool_keys)
  ```

### P-D3:守卫检查项的执行顺序
- **问题**:7 项检查应按什么顺序执行?
- **选定**:按"复杂度递减"顺序 — 复杂验证优先(`package.json` / `pyproject.toml` 需 Read 验证) → 简单存在性检查(`Cargo.toml` / `go.mod` / `pom.xml` / `build.gradle` / `test/` 目录)
- **理由**:命中优先返回,避免不必要的 Glob 调用(性能优化)
- **伪代码**:
  ```python
  # 顺序:package.json > pyproject.toml > Cargo.toml > go.mod > pom.xml > build.gradle > test/
  # 命中任一即短路返回
  ```

### P-D4:守卫不通过时屏幕输出的"任务"信息从哪来?
- **问题**:屏幕输出含 "任务: TASK-REQ-00009-00001",这个信息从哪来?
- **选定**:从 `code-unit` 启动参数 `<任务编码>` 来,沿用既有 `步骤 1` 的解析结果
- **理由**:`code-unit` 已经在步骤 1 解析任务编码,守卫可直接复用,不重复解析

### P-D5:看板"测试状态"列写入路径(FR-2.AC-2.1)
- **问题**:守卫不通过时,看板"测试状态"列如何写入?
- **选定**:沿用 `code-unit` 步骤 14 既有写入路径
- **理由**:NFR-3 强约束"沿用 V0.0.1 既有枚举 + 既有写入路径",**0** 新增路径
- **具体路径**:`edit_file(VERSION/RESULT.md, "§任务清单", old_line, new_line_with_test_status="不适用")`

### P-D6:E-2 编号冲突的处理
- **问题**:`code-unit/SKILL.md` 既有"边界 E-2"可能已存在,本需求"守卫不通过"边界使用哪个编号?
- **选定**:
  - 既有 E-2 已有内容 → 本需求使用 `#### E-8 守卫不通过`(追加)
  - 既有 E-2 是"预留"空位 → 本需求使用 `#### E-2 守卫不通过`(复用)
  - 既有 E-2 不存在 → 同上(复用)
- **T-001 实施时判定**:读 `code-unit/SKILL.md`,若 `^#### E-2` 存在且有内容 → 用 E-8;否则用 E-2
- **影响**:T-001 实施时**必须**先 Read SKILL.md 确认,**不**在计划阶段锁死

### P-D7:守卫"屏幕报告"在 `code-unit` 哪个阶段输出?
- **问题**:守卫检查结果何时输出到屏幕?
- **选定**:**步骤 0a 入口**输出(守卫完成后立即)
- **理由**:让用户立即看到守卫判定结果,无需等待"步骤 0"+ 既有流程
- **细节**:
  - 守卫通过 → 输出"✓ 守卫通过"+ 检查详情 → 进入"步骤 0"
  - 守卫不通过 → 输出"⏭ 守卫不通过 + 跳过原因" → 进入 FR-2 跳过流程 → 退出

## 与概要设计的差异
- **0 偏离**(100% 沿用概要设计 8 决策 D-1~D-8)
- **新增 P-D6**(E-2 编号冲突处理):概要设计未涉及,本详细设计阶段发现并锁定

## 风险与缓解

| 风险 | 影响 | 缓解 |
| --- | --- | --- |
| `code-unit/SKILL.md` 行数偏差超 ±20% | 静态自检 INV-7 失败 | T-001 实施时,新增内容严守"~30 行"估算(7 项检查 ~15 行 + 判定逻辑 ~5 行 + 跳过流程 ~5 行 + 屏幕报告 ~5 行 = ~30 行) |
| 既有 E-2 编号冲突未识别 | 静态自检 INV-4 / INV-5 失败 | T-001 实施时**先 Read SKILL.md** 确认既有 E-2 状态,据 P-D6 决策 |
| `package.json` 验证伪代码误判 | 守卫通过后跑 `npm test` 失败 | 严守 P-D1 判定:`"test" in scripts and scripts["test"]` 非空 |
| 8 个关键 token 漏写 | 静态自检 INV-8 失败 | T-001 实施时,8 token 全部写入 SKILL.md 守卫说明段落 |

## 与既有 `code-it` / `code-unit` 流程的衔接
- **0 触发** `code-it` 任何变更(本需求不改 `code-it`)
- **0 触发** `code-unit` 既有"步骤 0"及之后任何变更(只新增"步骤 0a")
- **本需求不实施具体代码 / 配置 / 数据库**:`code-it` 在 T-001 实施时,只改 SKILL.md 1 个文件
