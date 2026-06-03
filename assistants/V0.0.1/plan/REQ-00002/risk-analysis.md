# 风险分析 — REQ-00002
版本:V0.0.1

## 异常处理

### 异常路径 1:某个 SKILL.md 替换点遗漏
- **描述**:`Grep` 验证显示 `code-skill/SKILL.md` 中仍有 `REQ-\d{4}-\d{4}` 命中
- **处理**:
  1. 重新 `Read` 该文件
  2. 定位遗漏点(可能因多行字符串或转义符)
  3. 逐处 `Edit` 替换
  4. 再次 `Grep` 验证
- **监控**:T-1 完成后 `Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/.*SKILL.md` 应为 0 命中
- **预防**:在 `code-it` 执行时**先 `Read` 全文**,再 `Edit`;不依赖 `Grep` 自动定位所有点

### 异常路径 2:中英 README 替换不对仗
- **描述**:中英 README 替换后,两边行数或语义不对应
- **处理**:
  1. `git diff` 两侧对比
  2. 不对仗处补 `Edit`
  3. 重新 `git diff --stat` 确认两侧变更行数一致
- **监控**:T-3 完成后 `git diff --stat` 应显示两 README 变更行数相近(±1-2 行)
- **预防**:doc-conventions §规则 1 已强制同次 commit,本任务不容忍不对仗

### 异常路径 3:多 commit 顺序错乱
- **描述**:7 个 commit 顺序错乱(如模板 commit 在 SKILL.md commit 之前)
- **处理**:
  1. `git log --oneline` 检查 commit 顺序
  2. 若错乱,**回退**:`git reset --soft HEAD~N` + 重新按正确顺序 commit
- **监控**:T-1 ~ T-7 完成后 `git log --oneline` 应显示 7 个 commit 按预期顺序
- **预防**:在 `code-it` 实施时,严格按 PLAN.md §2.1 ~ §2.7 顺序执行;**不并行** commit

### 异常路径 4:新规范文件创建后,内容被既有规则冲突
- **描述**:`encoding-conventions.md` 与 `doc-conventions.md` 或 `dashboard-conventions.md` 冲突
- **处理**:
  1. 重新审视 `encoding-conventions.md` 内容
  2. 若有冲突,**调整**新文件,使其不与既有规范重叠
  3. 若无法调整,记入 `deviations.md` 并停下询问用户
- **监控**:T-5 完成后 `Read encoding-conventions.md` 全文,逐条对照既有规范
- **预防**:`encoding-conventions.md` 只定义"编码格式"这一个领域,不涉及"文档结构"或"看板结构"

### 异常路径 5:全仓库 Grep 命中超出预期
- **描述**:T-7 全仓库 Grep 发现新文件中仍有旧串(如 5 个现有 rules/ 文件中)
- **处理**:
  1. 记入 `code/REQ-00002-00007/deviations.md`
  2. 标注"范围外,留给 `code-rule` 跟进"
  3. 不修复,继续 T-7 完成
- **监控**:T-7 完成后 `deviations.md` 至少含 2 条已知偏离(doc-conventions.md + V0.0.0)
- **预防**:本需求 FR 边界已明确"不修改 rules/";Grep 命中是预期内

## 安全边界

### 鉴权要求
- **不适用**(本需求为纯文档/字符串字面量替换,无鉴权)

### 输入校验
- **不适用**(本需求不引入新用户输入)

### 敏感数据处理
- **不适用**(无敏感数据)

### 审计日志
- 通过 7 个 commit 的 commit message 留痕
- commit message 格式:`chore(encoding): <子任务标题>`
- 包含 `关联需求: REQ-00002`

## 性能与资源

### 关键路径预估
- **无运行时路径**(本需求不影响 `code-*` 技能的运行性能)
- **build/install 路径**:不适用(本仓库为 Markdown 文档,无 build 步骤)

### 资源限制
- **不适用**

### 缓存策略
- **不适用**

## 回退策略

### 触发条件
- 任一 commit 引入非预期问题(如替换点错误导致 SKILL.md 语义改变)
- 7 个 commit 全部完成但有"致命"内容错误

### 步骤
1. **单 commit 回退**:
   ```bash
   git revert <commit-hash>  # 推荐:revert 留下证据
   # 或
   git reset --hard HEAD~1   # 危险:无证据,需用户明确授权
   ```
2. **全部回退**:
   ```bash
   git revert HEAD~7..HEAD   # 7 个 commit 一次性 revert
   # 或
   git reset --hard <REQ-00002 之前 commit>
   ```
3. **重新实施**:
   - 调整 `code-it` 策略
   - 重新执行 7 任务

### 验证
- 回退后,`git log --oneline` 不含本需求 7 个 commit
- `Grep "REQ-\d{4}-\d{4}"` 应回到本需求实施前的状态(即恢复旧格式)
- 看板状态回退到本需求未开始

## 测试要点

### 单元测试
- **不适用**(本需求无编程逻辑变更)

### 集成测试
- **不适用**(同上)

### 端到端测试
- **不适用**(同上)

### 验证测试(本需求专属)
- **V-1**:全仓库 Grep 验证 0 命中(在 SKILL.md / 模板 / README / CLAUDE.md 范围)
  - 命令:`Grep "REQ-\d{4}-\d{4}" plugins/code-skills/skills/` → 0 命中
  - 命令:`Grep "REQ-\d{4}-\d{4}" plugins/code-skills/README*.md` → 0 命中
  - 命令:`Grep "REQ-\d{4}-\d{4}" plugins/code-skills/CLAUDE.md` → 0 命中
- **V-2**:13 不变量自检(INV-1 ~ INV-13)逐条成立
- **V-3**:中英 README 行数差异 ≤ 1 行(`git diff --stat` 对比)
- **V-4**:7 个 commit 顺序正确(`git log --oneline`)
- **V-5**:新规范文件内容合法(`Read encoding-conventions.md` + `Read migration-mapping.md`)
- **V-6**:看板同步完成(本计划 + 实施 7 任务行,全部"已完成 / 不适用")
