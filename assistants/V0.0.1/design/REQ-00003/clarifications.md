# 澄清记录 — REQ-00003
更新时间:2026-06-03 21:00
版本:V0.0.1

> 本需求 **5 项待澄清 + 3 项已锁定**(在 REQU 阶段记录)。
> design 阶段确认全部 5 项待澄清。

## REQU 阶段已锁定的 3 项(继承)

### Q-1:Type A 支持 6 类核心规范(部分条件性,部分默认)
- **REQU 默认(已锁定)**:6 类核心规范
- **本设计采纳**:是
- **影响章节**:`design-notes.md` §Q-2 分类映射表
- **处理时间**:2026-06-03 20:35(REQU 阶段)

### Q-2:类型识别方式
- **REQU 默认(已锁定)**:自动 + 显式两者结合
- **本设计采纳**:是
- **影响章节**:`design-notes.md` §Q-5 类型识别引擎
- **处理时间**:2026-06-03 20:35(REQU 阶段)

### Q-3:Type C 插入位置
- **REQU 默认(已锁定)**:末尾追加 + 内联两者都支持
- **本设计采纳**:是
- **影响章节**:`module-breakdown.md` §M-4
- **处理时间**:2026-06-03 20:35(REQU 阶段)

## design 阶段确认 5 项(用户回答)

### Q-4:C-4 分类(目录与模块规范)的文件名
- **REQU 阶段选项**:H1=合并到 `module-conventions.md` / H2=独立新建 `directory-conventions.md`
- **用户回答**:**沿用需求文档建议的 `directory-conventions`**(独立新建)
- **影响章节**:`design-notes.md` §Q-2 分类映射表(决定 C-4 = `directory-conventions.md`)
- **处理时间**:2026-06-03 21:00(design 阶段)

### Q-5:6 个新分类文件的初始内容策略
- **REQU 阶段选项**:H1=全部建空占位(纯脚手架) / H2=3 个默认预填示例
- **用户回答**:**H1 全部建空占位(纯脚手架)**
- **影响章节**:`module-breakdown.md` §M-5 占位文件创建
- **处理时间**:2026-06-03 21:00(design 阶段)

### Q-6:Type B 标准字段是否加"示例"字段
- **REQU 阶段选项**:是否加"正面示例"/"反面示例"
- **用户回答**:**不增加示例字段**(由本设计默认决策,未明确询问)
- **影响章节**:`module-breakdown.md` §M-3 Type B 数据结构
- **处理时间**:2026-06-03 21:00(design 阶段)
- **默认决策理由**:
  - Type A 的"示例"是"代码可验证的规则",需要正反例
  - Type B 的"指引"是"AI 行为指令",示例作用有限(AI 不能直接验证)
  - 保持字段精简,符合 NFR-4 最小化

### Q-7:Type C 内容提示格式
- **REQU 阶段选项**:H1=`## 提示: <主题>` 末尾追加 / `### 提示: <字段>` 内联 / H2=其他
- **用户回答**:**沿用需求文档默认**(`## 提示:` 末尾 + `### 提示:` 内联,两者并存)
- **影响章节**:`module-breakdown.md` §M-4 Type C 数据结构
- **处理时间**:2026-06-03 21:00(design 阶段)

### Q-8:现有 5 个规范文件(dashboard-conventions / doc-conventions / marketplace-protocol / module-conventions / skill-conventions)的处理
- **REQU 阶段选项**:H1=全部保留(11 个文件并存) / H2=迁移部分重叠(module → directory) / H3=整体重分类(5 个全部映射到 6 类)
- **用户回答**:**H2 迁移部分重叠(module → directory)**
- **影响章节**:
  - `module-breakdown.md` §M-6 迁移与弃用标记
  - `rule-compliance.md` §6 边界 B-6
  - `design-notes.md` §关键决策 D-3
- **处理时间**:2026-06-03 21:00(design 阶段)
- **具体决策**:
  - 4 个文件**保留原状**:`dashboard-conventions.md` / `doc-conventions.md` / `marketplace-protocol.md` / `skill-conventions.md`
  - 1 个文件**追加 DEPRECATED 标记**:`module-conventions.md`
  - 1 个文件**新建**:`directory-conventions.md`(承载原 module-conventions 内容 + 目录结构新规则)
  - 实施后 `assistants/rules/` 共 11 个文件:4 保留 + 1 弃用 + 6 新建

## design 阶段新增澄清(本设计内决策)

### 决策 D-DESIGN-1:Type A 关键词表保留旧 + 新增
- **问题**:旧 SKILL.md 步骤 4 有 11 个分类关键词(架构/模块规划/命名约定/错误处理/接口定义/数据结构/安全/性能/测试/可观测性/提交规范),本需求 6 核心 + 5 保留专项
- **决策**:**保留旧关键词,新增新关键词**(向后兼容)
- **影响章节**:`design-notes.md` §候选分类关键词表
- **理由**:
  - 旧关键词映射到新分类:命名约定 → naming-conventions / 提交规范 → commit-conventions
  - 保留旧关键词让"老用户"无感升级
  - 未来可逐步淘汰旧关键词

### 决策 D-DESIGN-2:`code-rule/SKILL.md` description 不变
- **问题**:本需求扩展 `code-rule` 能力,是否更新 frontmatter `description` 字段?
- **决策**:**description 不变**(只改正文)
- **影响章节**:`rule-compliance.md` §6 边界
- **理由**:
  - `code-rule` description 已被其他 9 个 `code-*` 技能识别为"读取规范"
  - 修改 description 触发其他技能的"读取规范来源"决策可能变化
  - 本需求扩展能力,但 description 已包含"维护项目级共享规范"语义

### 决策 D-DESIGN-3:5 commit 粒度
- **问题**:本需求 5 个 commit,粒度如何?
- **决策**:**5 commit 按模块拆分**(详见 `module-breakdown.md` §实施顺序)
- **影响章节**:`module-breakdown.md` §实施顺序表
- **理由**:
  - 每类变更可独立 review
  - 便于回退某一类(若 Type A 占位被否决,可单独回退 commit 2)
  - 与 code-it 阶段的 PLAN.md 任务一一对应

## 待用户后续确认(无)

本设计阶段**无遗留待用户确认项**。所有 REQU 待澄清(Q-1 ~ Q-8)已确认或采纳默认;design 阶段新增 3 项决策(D-DESIGN-1/2/3)已在本设计内显式说明。
