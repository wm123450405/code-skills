# 依赖与集成 — REQ-00003
版本:V0.0.1

## 第三方依赖(无)

本需求**不引入**任何第三方依赖:
- 无新的 npm/Python/Go 包
- 无新的 CLI 工具
- 无新的 Claude Code 协议

**理由**:本需求是 `code-rule` 技能的纯逻辑扩展(增加 3 种目标类型处理流程),所有改动都是 Markdown 文档 + 流程逻辑,无运行时依赖。

## 内部模块依赖(本仓库内)

### 依赖 1:`templates/rule.md` 扩展
- **方向**:`code-rule` SKILL.md → `code-rule/templates/rule.md`
- **类型**:读取 + 扩展
- **变更**:在 `rule.md` 头部追加"占位模式" + "引导模式"说明
- **风险**:若其他技能误用 `templates/rule.md`,会看到新增的"占位模式"说明
  - 实际:仅 `code-rule` 使用此模板;其他技能用各自的 `templates/*.md`
  - 缓解:无

### 依赖 2:`plugins/code-skills/CLAUDE.md` 读取
- **方向**:`code-rule` → `CLAUDE.md`
- **类型**:只读 + 末尾追加
- **变更**:检测是否含"## AI 工作约定"小节;不存在则追加
- **风险**:CLAUDE.md 被 `code-rule` 之外的进程修改(如 GitHub 同步) → `Edit` 工具的 old_string 失效
  - 缓解:用上下文锚定 + 全文 Read 后定位

### 依赖 3:`plugins/code-skills/skills/*/templates/*.md` 读取
- **方向**:`code-rule` → 27 个模板文件
- **类型**:只读 + 末尾追加 / 内联追加
- **变更**:Type C 流程
- **风险**:
  - 27 个模板跨多个技能,`code-rule` 需 Glob 全表
  - 内联模式需要精确匹配二级小节名,可能因格式漂移失败
- **缓解**:
  - Glob `plugins/code-skills/skills/*/templates/*.md` 一次
  - 内联模式前 `Read` 全文,人工确认小节名

### 依赖 4:9 个其他 `code-*` 技能 SKILL.md
- **方向**:`code-rule` → 其他 9 个 SKILL.md
- **类型**:**不依赖**(只读约束)
- **依据**:本需求 FR-9 边界 — `code-rule` 不得修改其他 SKILL.md

### 依赖 5:`./assistants/rules/` 现有 5 个文件
- **方向**:`code-rule` → 现有 5 个规范文件
- **类型**:读取 + (本需求)4 个保留 + 1 个弃用标记追加
- **变更**:
  - `dashboard-conventions.md` / `doc-conventions.md` / `marketplace-protocol.md` / `skill-conventions.md`:**0 变更**
  - `module-conventions.md`:**仅追加** DEPRECATED 标记
- **风险**:
  - 现有规范文件若被用户外部修改,`Edit` 可能失败
  - 缓解:Read 全文 + 上下文锚定

## 数据流图

```
用户输入:"对 templates/plan.md 增加提示:任务依赖图必须画"
                        │
                        ▼
        [code-rule 类型识别引擎(M-1)]
                        │
                        │ 关键词命中:templates/ + plan.md
                        │ 候选类型:C (高置信度)
                        ▼
        [Type C 子流程(M-4)]
                        │
                        │ 询问:末尾追加 / 内联?
                        │ 用户:末尾追加
                        ▼
        [Read templates/plan.md 全文]
                        │
                        ▼
        [Edit templates/plan.md]
        - 检测"## 提示"小节是否存在
        - 不存在 → 末尾追加"## 提示: 任务依赖图" + 4 字段
                        │
                        ▼
        [汇报:已在 plan.md 末尾追加"## 提示: 任务依赖图"]
```

## 兼容性矩阵

| 现有使用方 | 调用方式 | 本需求变更 | 兼容? |
| --- | --- | --- | --- |
| 项目主导者(R-1) | 调 `code-rule` 一次性建 6 类占位 | 新增 6 类识别 + 占位模式 | ✅ 后向兼容 |
| 规范沉淀人(R-2) | 调 `code-rule` 加命名/提交等规范 | Type A 现有流程 + 新分类识别 | ✅ 后向兼容(关键词扩展) |
| 模板作者(R-3) | 调 `code-rule` 加模板提示 | 新增 Type C | ✅ 新功能,不影响现有调用 |
| AI 协作者(R-4) | 读 `CLAUDE.md` + `templates/*.md` | CLAUDE.md 新增"AI 工作约定"小节;模板新增"提示" | ✅ 增量信息,不影响现有内容 |
| 其他 9 个 `code-*` 技能 | 读 `./assistants/rules/` 作为约束 | 5 → 11 个文件(4 新 + 1 迁移),关键词表扩展 | ✅ 文件数增加,但规则内容相同,无破坏 |

## 风险评估

| 风险 | 概率 | 影响 | 缓解 |
| --- | --- | --- | --- |
| 现有 `code-rule` 调用者流程感知变化 | 低 | 中(用户需重新学习) | SKILL.md 步骤 4 仅在关键词表扩展,不改变主流程;Type A 调用者无感 |
| `module-conventions.md` 弃用后,其他技能误读 | 低 | 中 | DEPRECATED 标记 + 文档说明"内容已迁移到 directory-conventions.md";其他技能读 `Glob` 仍能发现该文件,加判 DEPRECATED 标记忽略 |
| Type B 内联追加到错误小节 | 中 | 中 | 强制用户指定二级标题精确匹配;若不匹配则报错 |
| Type C 末尾追加破坏模板结构 | 低 | 中 | `## 提示: <主题>` 是新增小节,不替换既有内容 |
| `code-rule` 主流程文档膨胀(从 272 → 400+ 行) | 中 | 低 | 用子小节清晰切分;类型识别作为独立子流程 |

## 集成测试要点

| 测试 | 验证内容 | 通过条件 |
| --- | --- | --- |
| IT-1:Type A 现有流程回归 | 旧 `code-rule` 调用("函数命名用 camelCase")仍归类到"命名约定" | ✅ 与 v0 一致 |
| IT-2:Type A 6 分类识别 | 6 个描述各命中 6 类 | ✅ 6 规则分别落到 6 个文件 |
| IT-3:Type A 条件性追问 | 描述触发"现在需要/未来占位/跳过" | ✅ 3 选项呈现 |
| IT-4:Type A 占位模式 | 选"未来占位" → 创建空骨架 | ✅ 文件仅含分类标题 + 占位 |
| IT-5:Type B 末尾追加 | 触发 Type B → CLAUDE.md 末尾新增"AI 工作约定" | ✅ 纯追加,无删除 |
| IT-6:Type C 末尾追加 | 触发 Type C + 末尾 → 模板末尾新增"## 提示" | ✅ 纯追加 |
| IT-7:Type C 内联 | 触发 Type C + 内联 + 指定小节 → 在该小节末尾追加 | ✅ 精确插入 |
| IT-8:类型识别 | 3 类典型 + 1 类模糊 | ✅ 高置信度自动,低置信度追问 |
| IT-9:边界 | 跑完整流程,`git status` 仅显示预期文件 | ✅ 不触及 marketplace.json / plugin.json / 其他 SKILL.md |
