# 接口详细规格 — REQ-00016
更新时间:2026-06-05 16:15
版本:V0.0.2

> 本需求**不**对外暴露新 API;主接口 = `code-design` / `code-plan` SKILL.md 入口(无参数变化);新增的是 SKILL.md 内部处理逻辑。

---

## 接口 1:`code-design REQ-NNNNN`(完整模式,既有,字节级不变)

### 形式
SKILL.md 入口(1 参 `REQ-NNNNN`)

### 行为(沿用既有,字节级不变)
- 评审单需求 → 写 7 份过程文档 + 写 RESULT.md(14 章节)+ 同步看板多区段 + 末尾兜底 3 选 1 确认
- frontmatter 字节级不变
- 步骤 0-15 字面字节级不变

### 依据规范
- FR-5 全节(完整模式字节级不变)
- INV-1 / INV-2 / INV-3 约束

---

## 接口 2:`code-design REQ-NNNNN --fast`(本设计新增,快模式)

### 形式
SKILL.md 入口(2 参:`--fast` + `REQ-NNNNN`)

### 触发条件
- 用户传 `--fast` CLI 标志

### 入参
- 1 个 `REQ-NNNNN` 编码(同完整模式)
- 1 个 `--fast` 标志(优先级最高)

### 出参
- 屏幕输出:同 §10.1 stdout 输出模板(快模式)
- 磁盘输出:
  - `design/REQ-NNNNN/RESULT.md`(仅核心 4 章节)
  - `design/REQ-NNNNN/materials-index.md`
  - `design/REQ-NNNNN/related-requirements.md`(过程文档,3 份)
  - `assistants/V0.0.2/RESULT.md`(看板同步 1 行 + 0 变更记录 + 0 时间戳)

### 错误码
- 退出码 0:完成
- 退出码非 0:致命错误(沿用既有 11 个 `code-*` 错误码语义)

### 兼容性
- 模式 1 / 模式 2 共存 — `--fast` 与 `--full` 互斥(E-M1 报错退出)
- 多次执行快模式幂等(NFR-3 + INV-8)

### 依据规范
- FR-1.AC-1.1 ~ AC-1.6
- FR-2 全节
- FR-4 全节
- AC-1 / AC-2 / AC-4

---

## 接口 3:`code-design REQ-NNNNN --full`(本设计新增,显式完整模式)

### 形式
SKILL.md 入口(2 参:`--full` + `REQ-NNNNN`)

### 行为
- 显式走完整模式(覆盖 `CODE_FAST_MODE=1` 环境变量)
- 与接口 1 行为完全一致

### 依据规范
- FR-1.AC-1.4(CLI 覆盖)

---

## 接口 4:`code-design`(无参 + `CODE_FAST_MODE=1`)(本设计新增,环境变量快模式)

### 形式
SKILL.md 入口(无参)

### 触发条件
- 用户未传 `--fast` / `--full`
- 环境变量 `CODE_FAST_MODE ∈ {1, true, yes, on}`

### 行为
- 走快模式(同接口 2)

### 依据规范
- FR-1.AC-1.1

---

## 接口 5:`code-design REQ-NNNNN`(默认,完整模式,既有,字节级不变)

### 形式
SKILL.md 入口(1 参 `REQ-NNNNN`)

### 行为
- 默认走完整模式(当 `CODE_FAST_MODE` 未设置 / 设置为 0 / 非法)
- 与接口 1 行为完全一致

### 依据规范
- FR-1.AC-1.6(默认完整模式)

---

## 接口 6:SKILL.md 内部"步骤 0.5 模式选择"段(本设计新增,字面契约)

### 字面(2 个文件共享)

```markdown
### 步骤 0.5 — 模式选择(本需求新增,快模式入口)

**触发条件**:步骤 0 完成(版本号已读)

**逻辑(三态机 + 优先级)**:
1. **CLI 标志解析**:
   - `--fast` 与 `--full` 同时传 → 报错"互斥" + 提示用法 + 退出(E-M1)
   - `--fast` → **快模式** → mode=FAST
   - `--full` → **完整模式** → mode=FULL
2. **环境变量**(CLI 标志未传):
   - `CODE_FAST_MODE ∈ {1, true, yes, on}`(大小写不敏感)→ **快模式** → mode=FAST
   - `CODE_FAST_MODE ∈ {0, false, no, off}` 或未设置 → **完整模式** → mode=FULL
   - 非法值(如 `abc`)→ 警告"⚠ 忽略 CODE_FAST_MODE=<value>" + 走完整模式(E-M2)
3. **优先级**:CLI 标志 > 环境变量 > 默认值
4. **默认值**:mode=FULL(保留现有行为)

**依据**:FR-1.AC-1.1 ~ AC-1.6
```

### 入参
- 用户传参(由步骤 1 收集)
- 环境变量 `CODE_FAST_MODE`(Bash `echo` 读取)

### 出参
- 模式判定结果(FAST / FULL)
- 进入后续步骤时,`mode` 变量在所有步骤的条件判断中可用

### 兼容性
- 完整模式**完全保留**(既有步骤 0-15 字面字节级不变,INV-1)
- 快模式**不**影响既有步骤字面(仅在快模式条件分支中跳过)

---

## 接口 7:SKILL.md 内部"步骤 N 步骤 3.5 模式分支判断"段(本设计新增,字面契约)

### 字面(2 个文件共享)

```markdown
### 步骤 N 步骤 3.5 — 模式分支判断(本需求新增,快模式末尾兜底跳过 3 选 1)

**触发条件**:步骤 N 步骤 3(`git add` 所有 dirty 文件)完成

**逻辑**:
1. **mode == FAST** → **跳过**"步骤 N 步骤 4 弹 3 选 1 确认"→ 直接进入"步骤 N 步骤 5 执行 commit"
2. **mode == FULL** → 执行"步骤 N 步骤 4 弹 3 选 1 确认" → 用户选择 A/B/C → 进入"步骤 N 步骤 5 执行 commit"

**依据**:FR-4 + NFR-7 + 用户 clarifications.md Q-2
```

### 兼容性
- 完整模式**完全保留**(既有"步骤 N 步骤 4 弹 3 选 1 确认"字面字节级不变,INV-3)
- 快模式**跳过**"步骤 N 步骤 4",直接进入"步骤 N 步骤 5 执行 commit"
