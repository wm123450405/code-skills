# 接口详细规格 — REQ-00031

更新时间:2026-06-12 15:32
版本:V0.0.3

## 接口 1:`code-plan` 任务粒度接口(T-001 修订)

- **形式**:文档子节(非 API,非 CLI)
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md §步骤 10A`
- **入参**:**不适用**(文档修订)
- **出参**:**不适用**(文档修订)
- **错误码**:**不适用**
- **示例**:**不适用**
- **版本策略**:`code-plan` 自身**不**支持版本化(SKILL.md);本需求作为 V0.0.3 内一次修订,**不**影响既有 11 个 REQ
- **兼容策略**:`code-plan` 步骤 10A 既有锚点字节级保留;`code-it` / `code-auto` 既有任务解析逻辑**不**变
- **依据规范**:`skill-conventions.md` INV-1/2/3

### 修改内容
1. "可独立验证"小节追加 1 段(FR-1)
2. "任务类型"列表移除 `测试`(FR-2)
3. "测试状态"枚举收窄(FR-3)
4. "双状态语义"简化(FR-3 副作用)

## 接口 2:`code-auto` 任务循环步骤 4.b(T-004 修订)

- **形式**:文档子节
- **路径**:`plugins/code-skills/skills/code-auto/SKILL.md §步骤 4 任务循环 步骤 4.b`
- **入参 / 出参 / 错误码 / 示例 / 版本**:**不适用**
- **兼容策略**:`code-auto` 自身 SKILL.md 字节级保留(沿用 NFR-4 零修改契约)
- **依据规范**:`skill-conventions.md` INV-1/2/3/10

### 修改内容
1. 步骤 4.b 由"按需调用 code-unit"改为"恒等跳过"
2. 屏幕日志格式 `(跳过,无需测试)` 字节级保留(INV-10)
3. 步骤 4.b 末尾追加"还原指引"注释(以备未来 `code-plan` 重新启用测试规划)

## 接口 3:`code-it` 文档头声明(T-002 修订)

- **形式**:文档头声明
- **路径**:`plugins/code-skills/skills/code-it/SKILL.md ## 目标`
- **入参 / 出参 / 错误码 / 示例 / 版本 / 兼容**:**不适用**(声明性修订)
- **依据规范**:`skill-conventions.md` INV-1/2/3

### 修改内容
1. 末尾追加 1 段"本技能职责范围"

## 接口 4:`code-unit` 文档头声明(T-003 修订)

- **形式**:文档头声明
- **路径**:`plugins/code-skills/skills/code-unit/SKILL.md ## 目标`
- **入参 / 出参 / 错误码 / 示例 / 版本 / 兼容**:**不适用**
- **依据规范**:`skill-conventions.md` INV-1/2/3

### 修改内容
1. 末尾追加 1 段"本技能职责范围"

## 接口 5:`templates/plan.md` 任务类型字段(T-005 修订)

- **形式**:模板字段
- **路径**:`plugins/code-skills/skills/code-plan/templates/plan.md ## 任务总览`
- **入参 / 出参 / 错误码 / 示例 / 版本 / 兼容**:**不适用**
- **依据规范**:`module-conventions.md`(资源文件放 templates/ 子目录)

### 修改内容
1. 任务类型列 6 类 → 5 类(移除 `测试`)
2. 模板顶部追加"任务粒度约束"段
