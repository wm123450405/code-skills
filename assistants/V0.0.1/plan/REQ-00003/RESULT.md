# 详细设计 — REQ-00003(优化 `code-rule` 技能,增加不同类型的核心编码规范的解析或引导)

- 需求编码:REQ-00003
- 所属版本:V0.0.1
- 详细设计版本:v1
- 状态:已完成(首次)
- 责任人:wangmiao
- 创建:2026-06-03
- 最近更新:2026-06-04 09:15
- **上游**:
  - `./assistants/V0.0.1/require/REQ-00003/RESULT.md`(v1,已锁定)
  - `./assistants/V0.0.1/design/REQ-00003/RESULT.md`(v1,已完成)
- **下游**:`code-it REQ-00003-NNN` 实施;`code-unit` 验证
- **遵循规范**:`./assistants/rules/` 下 5 个现有文件 + 6 个新分类文件将由本设计创建 + `module-conventions.md` 弃用

---

## 1. 概述

### 1.1 目标

把概要设计"系统长什么样"落地为**可直接编码的细节**,主要交付物包括:
- `code-rule/SKILL.md` 步骤 4 的 3 段扩展(拆分 + 类型识别 + 归类)
- Type B / Type C 子流程的完整算法、数据结构、插入位置
- 6 个新分类占位文件 + 1 个弃用标记的精确内容模板
- CLAUDE.md 末尾"AI 工作约定"小节的初始化结构
- 11 条不变量 + 7 个测试要点 + 6 commit 实施顺序

### 1.2 范围

**修改对象**(共 3 个):
- `plugins/code-skills/skills/code-rule/SKILL.md`(扩展正文:步骤 4 拆 3 段 + 新增 2 个小节 + 工作目录约定更新)
- `plugins/code-skills/skills/code-rule/templates/rule.md`(头部追加占位/引导模式说明)
- `assistants/rules/module-conventions.md`(头部追加 DEPRECATED 标记)

**新增对象**(共 7 个):
- 6 个新分类占位文件(C-1~C-6)
- `plugins/code-skills/CLAUDE.md` 末尾新增"## AI 工作约定(由 code-rule 维护)"小节

**零变更对象**(4 保留 + 2 协议清单 + 9 SKILL.md + V0.0.0/1 工作文件):见 INV-5 / INV-6

### 1.3 与概要设计的关系

| 概要设计章节 | 本详细设计对应章节 | 关系 |
| --- | --- | --- |
| §3.1 核心架构 | §3.1 核心架构 | 一致(单技能 + 3 子流程) |
| §3.2 Type A 子流程 | §3.3 Type A 子流程(M-2) | 一致(扩展,9 步骤主流程不变) |
| §3.2.2 占位模式 | §3.3.2 占位流程 | 一致 |
| §3.2.3 引导模式 | §3.3.3 引导流程 | 一致 |
| §3.2.4 分类映射表 | §3.3.4 分类映射表 | 一致 |
| §3.3 Type B 子流程 | §3.4 Type B 子流程(M-3) | 一致 |
| §3.4 Type C 子流程 | §3.5 Type C 子流程(M-4) | 一致 |
| §3.5 类型识别引擎 | §3.6 类型识别引擎(plan 微调) | **微调**:从独立子流程变更为步骤 4 子段 4.2 |
| §4 数据结构 | §4 数据结构 | 一致 |
| §5 不变量 | §5 不变量 | 继承 9 条 + 新增 INV-10 / INV-11 |

## 2. 上游引用

- 需求分析:`./assistants/V0.0.1/require/REQ-00003/RESULT.md`(v1,已锁定)
- 概要设计:`./assistants/V0.0.1/design/REQ-00003/RESULT.md`(v1,已完成)
- 设计过程文档:
  - `design/REQ-00003/design-notes.md`(8 个 Q + 8 决策)
  - `design/REQ-00003/module-breakdown.md`(M-1~M-9 模块拆分)
  - `design/REQ-00003/clarifications.md`(5 项用户答复 + 3 项 design 决策)
  - `design/REQ-00003/rule-compliance.md`(14 项自检)
  - `design/REQ-00003/dependencies.md` / `related-designs.md` / `materials-index.md`
- 项目级规范:`./assistants/rules/` 下 5 个文件(Glob 命中)
- plan 阶段过程文档:
  - `plan/REQ-00003/materials-index.md` / `design-notes.md` / `clarifications.md`
  - `plan/REQ-00003/module-details.md` / `interface-specs.md` / `data-changes.md`
  - `plan/REQ-00003/risk-analysis.md` / `rule-compliance.md`

## 3. 模块详细化

### 3.1 核心架构

```
[用户调用 code-rule + 描述]
        │
        ▼
[步骤 3 — 收集规范描述]
        │
        ▼
[步骤 4 — 拆分 + 类型识别 + 初步归类](plan 微调,详见 §3.6)
   ├─→ 4.1 拆分(<原始描述> → Rule[1..N])
   ├─→ 4.2 类型识别(关键词 + 置信度 + 显式确认)
   └─→ 4.3 初步归类
         ├─→ Type A → 走步骤 5-9 现有流程(M-2)
         ├─→ Type B → 走 §3.4 Type B 子流程(M-3)
         └─→ Type C → 走 §3.5 Type C 子流程(M-4)
        │
        ▼
[汇报]
```

**关键设计决策**(继承 design 阶段 + plan 微调):
- D-1:单技能 + 3 子流程(非 3 技能)— 保持单一入口
- D-PLAN-1:类型识别**合并到步骤 4** 子段 4.2(plan 阶段微调 design M-1)
- D-3:Type A 现有 9 步骤流程**完全保持**(NFR-1 向后兼容)
- D-4:Type B / Type C 各自独立子流程,但文档上**与 Type A 同级**列在 `code-rule/SKILL.md`

### 3.2 模块清单(9 个,继承 design M-1~M-9)

| 模块 | 路径 | 状态 | 关联任务 |
| --- | --- | --- | --- |
| M-1 类型识别引擎 | `code-rule/SKILL.md` §步骤 4 子段 4.2 | 新增(plan 微调) | T-001 |
| M-2 Type A 子流程(扩展) | `code-rule/SKILL.md` §步骤 4-9 | 修改 | T-001 + T-002 + T-003 |
| M-3 Type B 子流程 | `code-rule/SKILL.md` 新增小节"Type B 子流程" | 新增 | T-001 + T-005 |
| M-4 Type C 子流程 | `code-rule/SKILL.md` 新增小节"Type C 子流程" | 新增 | T-001 |
| M-5 占位文件创建 | `assistants/rules/*.md` × 6 | 新增 | T-002 |
| M-6 迁移与弃用标记 | `assistants/rules/module-conventions.md` | 修改 | T-003 |
| M-7 CLAUDE.md 新小节 | `plugins/code-skills/CLAUDE.md` | 新增 | T-005 |
| M-8 模板扩展 | `code-rule/templates/rule.md` | 修改 | T-004 |
| M-9 工作目录约定更新 | `code-rule/SKILL.md` §工作目录约定 | 修改(并入 T-001) | T-001 |

### 3.3 Type A 子流程(M-2)

#### 3.3.1 现有流程继承(FR-8 约束)

Type A 现有 9 步骤工作流保持(`code-rule/SKILL.md` L83-224,字段不变):
- 步骤 0-3(不需要版本上下文 / 探查 / 兜底 / 收集)— **不变**
- 步骤 4(拆分 + 初步归类)— **扩展为 3 段**(详见 §3.6)
- 步骤 5(澄清规则细节)— **不变**
- 步骤 6(探测目标文件现状)— **不变**
- 步骤 7(写文件)— **增加"占位模式"分支**
- 步骤 8(汇报)— **不变**
- 步骤 9(多规则与迭代)— **不变**

**本需求变更**:
- 步骤 4 子段 4.3 关键词表**扩展**(从 11 个旧 → 6 核心 + 5 保留专项,见 §3.3.4)
- 步骤 4 子段 4.3 后增加"条件性分类追问"分支
- 步骤 7 写文件增加"占位模式"分支(M-2 占位模式)
- **其余步骤字段不变**(NFR-1 向后兼容)

#### 3.3.2 占位模式(FR-3,条件性分类)

**触发条件**:
- 用户描述命中 C-1 / C-2 / C-6(条件性分类)
- 用户选择"未来占位"

**算法**(伪代码):
```python
def place_holder_mode(classification, file_path):
    """占位模式:创建空骨架文件"""
    if not exists(file_path):
        # 不存在 → 创建骨架
        content = build_skeleton(classification)  # 详见 §3.3.5
        write(file_path, content)
        report(f"已创建占位文件: {file_path}")
    else:
        # 存在 → 走现有追加流程
        proceed_existing(classification, file_path)
```

**用户选择分支**:
- "现在需要" → 走 §3.3.3 引导模式
- "未来占位" → 走 §3.3.2 占位模式
- "跳过" → 不创建任何文件

#### 3.3.3 引导模式(FR-4,默认分类)

**触发条件**:
- 用户描述命中 C-3 / C-4 / C-5(默认分类)
- 用户**首次添加**该类规则(目标文件不存在)

**算法**(伪代码):
```python
def bootstrap_mode(classification, file_path):
    """引导模式:首次添加默认分类时,提示用户填示例"""
    if not exists(file_path):
        # 不存在 → 引导用户填示例
        user_choice = ask_user("是否同时补 1-2 条示例规则?")
        if user_choice == "是":
            # 走标准流程 + 用户提供示例
            proceed_new_with_examples(classification, file_path)
        else:
            # 走占位模式
            place_holder_mode(classification, file_path)
    else:
        # 存在 → 走现有追加流程
        proceed_existing(classification, file_path)
```

**不变量**:
- INV-2:即使引导模式,用户**未提供示例**时仍走占位模式(占位模式是兜底)

#### 3.3.4 分类映射表

| 分类 | 文件名 | 关键词 | 条件性 | 与现有关系 |
| --- | --- | --- | --- | --- |
| C-1 框架规范 | `framework-conventions.md` | 框架 / 架构 / framework | 条件性 | **新建**(空占位) |
| C-2 三方依赖规范 | `dependency-conventions.md` | 依赖 / 第三方 / 库 / 包 | 条件性 | **新建**(空占位) |
| C-3 语言与命名规范 | `naming-conventions.md` | 命名 / camelCase / snake_case | 默认 | **新建**(空占位) |
| C-4 目录与模块规范 | `directory-conventions.md` | 目录 / 模块 / 包结构 | 默认 | **新建**(空占位 + 承载 module-conventions 内容) |
| C-5 代码书写规范 | `coding-style.md` | 代码风格 / 注释 / 错误处理 | 默认 | **新建**(空占位) |
| C-6 提交与合并规范 | `commit-conventions.md` | 提交 / commit / 合并 / merge | 条件性 | **新建**(空占位) |
| 保留:看板 | `dashboard-conventions.md` | 看板 / 仪表盘 | — | **保留** |
| 保留:文档 | `doc-conventions.md` | README / 中英 | — | **保留** |
| 保留:marketplace | `marketplace-protocol.md` | marketplace / plugin | — | **保留** |
| 保留:技能 | `skill-conventions.md` | SKILL.md / frontmatter | — | **保留** |
| 弃用:模块 | `module-conventions.md` | — | — | **弃用**(追加 DEPRECATED 标记) |

#### 3.3.5 占位文件骨架(6 个新文件统一结构)

```markdown
# <分类中文名>规范(<分类英文名>)

> 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
> 最后更新:YYYY-MM-DD HH:mm
> 适用版本:跨所有版本共享(项目级)

## 适用场景
<本规范文件覆盖什么范围>

## 强制级别约定
本文件中各规则的强制级别逐条标注。

---

## 规则 1: (待添加)

<本条规则等待用户在后续调 `code-rule` 时填充。>
```

**6 个文件的实际填法**:
- `framework-conventions.md` → `# 框架规范(Framework Conventions)`
- `dependency-conventions.md` → `# 三方依赖规范(Dependency Conventions)`
- `naming-conventions.md` → `# 语言与命名规范(Naming Conventions)`
- `directory-conventions.md` → `# 目录与模块规范(Directory Conventions)`
- `coding-style.md` → `# 代码书写规范(Coding Style)`
- `commit-conventions.md` → `# 提交与合并规范(Commit Conventions)`

### 3.4 Type B 子流程(M-3)

#### 3.4.1 触发与识别

- 用户描述含以下关键词之一:
  - `CLAUDE.md` / `AI 工作` / `AI 约定` / `AI 写` / `AI 读` / `AI 应` / `AI 协作者`
- 关键词命中 + 高置信度 → 直接进入 Type B 子流程
- 用户可显式覆盖:`"对 CLAUDE.md 增加 X"`

#### 3.4.2 Type B 数据结构(5 字段)

```markdown
### 指引 N:<指引简称>

#### 描述
<一句话或一段说明该指引做什么>

#### 适用场景
<什么情况下 AI 应遵守>

#### 期望行为
<AI 应如何行动,可含"读哪个文件/调哪个技能/避免什么">

#### 来源
- 用户原始描述:"<用户最初说的话>"
- 添加时间:YYYY-MM-DD HH:mm
```

#### 3.4.3 插入位置与算法(伪代码)

```python
def type_b_append(user_description):
    """Type B:追加 AI 工作指引到 CLAUDE.md"""
    claude_md_path = "./plugins/code-skills/CLAUDE.md"
    content = read(claude_md_path)
    
    if not exists_section(content, "## AI 工作约定(由 code-rule 维护)"):
        # 不存在 → 末尾追加小节 + 1 个空指引占位
        new_section = """
## AI 工作约定(由 code-rule 维护)

> 本小节由 `code-rule` 技能维护;手动修改可能被 `code-rule` 覆盖。
> 适用对象:Claude Code 在本仓库工作时

### 指引 1: (待添加)
"""
        content = content.rstrip() + "\n" + new_section
        write(claude_md_path, content)
        report(f"已在 CLAUDE.md 末尾追加 'AI 工作约定' 小节(首次创建)")
    else:
        # 存在 → 在该小节末尾追加新指引
        n = count_existing_directives(content) + 1
        new_directive = build_directive(n, user_description)  # 见 §3.4.2
        content = append_to_section(content, "## AI 工作约定(由 code-rule 维护)", new_directive)
        write(claude_md_path, content)
        report(f"已在 CLAUDE.md 'AI 工作约定' 小节追加指引 {n}")
```

**不变量**:
- INV-3:仅追加,不改 / 不删(`git diff CLAUDE.md` 仅显示"+"行,无"-"行)

### 3.5 Type C 子流程(M-4)

#### 3.5.1 触发与识别

- 用户描述含以下关键词之一:
  - `模板` / `template` / `templates/` / 具体模板文件名(如 `plan.md` / `requirements.md`)
- 关键词命中 + 高置信度 → 直接进入 Type C 子流程
- 用户可显式覆盖:`"对 templates/plan.md 增加 X"`

#### 3.5.2 Type C 数据结构(4 字段)

**末尾追加模式**(`## 提示: <主题>`):
```markdown
## 提示: <主题>

- **字段**:<主题>
- **必填**:是 / 否
- **简明说明**:<1-2 句话>
- **错误示例**(可选):<错误填法>
```

**内联模式**(`### 提示: <字段>`):
```markdown
### 提示: <字段>

- **字段**:<字段>
- **必填**:是 / 否
- **简明说明**:<1-2 句话>
```

#### 3.5.3 插入位置与算法(伪代码)

```python
def type_c_append(user_description):
    """Type C:追加模板内容提示到目标模板"""
    template_path = parse_template_path(user_description)  # 从描述中提取
    if not template_path:
        # 追问用户
        template_path = ask_user("请指定目标模板文件(相对路径):")
    
    position = ask_user("插入位置?(末尾追加 / 内联)")
    
    if position == "末尾追加":
        append_to_template_end(template_path, user_description)
    else:  # 内联
        target_section = ask_user("请指定目标二级小节(精确匹配 '## N. <小节名>'):")
        # 必须精确匹配,否则追问(不自动推断)
        if not section_exists(template_path, target_section):
            raise NeedClarification("目标二级小节不存在,请重新指定")
        inline_to_section(template_path, target_section, user_description)


def append_to_template_end(template_path, user_description):
    content = read(template_path)
    if not exists_section(content, "## 提示"):
        # 不存在 → 末尾追加小节 + 1 个空提示占位
        new_section = """
## 提示: (待添加)

> 本小节由 `code-rule` 技能维护;手动修改可能被 `code-rule` 覆盖。
"""
        content = content.rstrip() + "\n" + new_section
        write(template_path, content)
    
    # 追加新提示
    n = count_existing_tips(content) + 1
    new_tip = build_tip(n, user_description)  # 见 §3.5.2
    content = append_to_section(content, "## 提示", new_tip)
    write(template_path, content)


def inline_to_section(template_path, target_section, user_description):
    content = read(template_path)
    new_tip = build_inline_tip(user_description)  # 见 §3.5.2
    content = append_to_section(content, target_section, new_tip)
    write(template_path, content)
```

**不变量**:
- INV-4:仅追加,不改 / 不删(`git diff templates/*.md` 仅显示"+"行)

### 3.6 类型识别引擎(M-1,plan 微调)

#### 3.6.1 步骤 4 子段 4.2 位置

> **plan 阶段微调**(Q-PLAN-2):原 design M-1 作为"独立子流程"插入步骤 4 之前;plan 阶段合并到步骤 4 子段 4.2。模块命名保留 M-1 便于追踪。

#### 3.6.2 关键词扫描

| 类型 | 关键词 |
| --- | --- |
| Type A | `规则` / `规范` / `约定` / `命名` / `提交` / `代码风格` / `依赖` / `框架` / `目录` / `模块` / `package` / `architecture` / `naming` / `commit` / `dependency` |
| Type B | `CLAUDE.md` / `AI 工作` / `AI 约定` / `AI 写` / `AI 读` / `AI 应` / `AI 协作者` |
| Type C | `模板` / `template` / `templates/` / 具体模板文件名(如 `plan.md` / `requirements.md`) |

#### 3.6.3 置信度评估

| 命中情况 | 置信度 | 处理 |
| --- | --- | --- |
| 1 个类型 + 1+ 关键词 + 目标文件明确 | **高** | 跳过追问,直接进入子流程 |
| 1 个类型 + 0 关键词 + 语义提示模糊 | **中** | `AskUserQuestion` 确认 |
| 多类型 / 0 类型 / 0 关键词 | **低** | `AskUserQuestion` 列出候选 |

#### 3.6.4 显式覆盖

用户可用 `"对 X 文件加 Y"` 形式显式指定:
- `X = CLAUDE.md` → Type B
- `X = templates/<file>` → Type C
- `X = <其他>` → Type A + 按 X 推断分类

#### 3.6.5 类型识别算法(伪代码)

```python
def step_4_type_recognition(rules):
    """步骤 4 子段 4.2:对每条 Rule 做类型识别"""
    for rule in rules:
        candidates = keyword_scan(rule.description)
        confidence = evaluate_confidence(candidates, rule.description)
        
        if confidence == "高":
            rule.type = candidates[0]
        elif confidence == "中":
            user_choice = ask_user(f"这条规则的类型是?(候选: {candidates})")
            rule.type = user_choice
        else:  # 低
            user_choice = ask_user(f"无法自动识别类型,请选择:(A 规则文件 / B CLAUDE.md / C 模板)")
            rule.type = user_choice
```

## 4. 数据结构(本设计范围内)

### 4.1 规则条目(Type A,已有,不变)

- 路径:`./assistants/rules/<分类>.md`
- 字段(8 个):分类 / 规则简称 / 强制级别 / 适用范围 / 条款 / 正面示例 / 反面示例 / 例外 / 关联规范 / 来源
- 来源:`code-rule/templates/rule.md` 模板
- **本需求变更**:模板头部追加"占位模式" + "引导模式"说明(不修改 8 字段结构)

### 4.2 指引条目(Type B,新增)

- 路径:`plugins/code-skills/CLAUDE.md` §"AI 工作约定"
- 字段(5 个):指引简称 / 描述 / 适用场景 / 期望行为 / 来源
- 模板:见 §3.4.2

### 4.3 提示条目(Type C,新增)

- 路径:`plugins/code-skills/skills/<技能>/templates/<name>.md`
- 字段(4 个,末尾模式;3 个,内联模式):字段/小节名 / 必填 / 简明说明 / 错误示例(末尾可选)
- 模板:见 §3.5.2

## 5. 不变量(本设计 11 条)

| # | 不变量 | 验证手段 | 来源 |
| --- | --- | --- | --- |
| INV-1 | 现有 Type A 9 步骤流程字段(关键词表除外)完全不变 | `git diff code-rule/SKILL.md` 仅关键词表扩展,无流程字段变更 | REQU FR-8 + NFR-1 |
| INV-2 | 6 个新分类文件仅含最小骨架 | `Grep "规则 1" 新建文件` 命中"## 规则 1: (待添加)"占位 | REQU FR-3 + design Q-5=H1 |
| INV-3 | Type B 仅追加到 CLAUDE.md 末尾的"AI 工作约定"小节 | `git diff CLAUDE.md` 仅显示"+"行,无"-"行 | REQU FR-5 + FR-10 |
| INV-4 | Type C 仅追加到模板末尾或内联 | `git diff templates/*.md` 仅显示"+"行 | REQU FR-6 + FR-10 |
| INV-5 | 不得修改 `marketplace.json` / `plugin.json` / 其他 9 个 SKILL.md frontmatter / `CLAUDE.md` 其他小节 | `git status` 仅显示预期文件 | REQU FR-9 |
| INV-6 | 4 个保留文件 0 变更 | `git diff dashboard-conventions.md doc-conventions.md marketplace-protocol.md skill-conventions.md` clean | design Q-8=H2 |
| INV-7 | `module-conventions.md` 仅追加 DEPRECATED 标记 | `git diff module-conventions.md` 仅显示 DEPRECATED 段 | design Q-8=H2 + 兜底 |
| INV-8 | `code-rule/SKILL.md` 步骤 0 工作目录约定更新为 11 个新分类列表;步骤 4 关键词表更新为 6 核心 + 5 专项 | `Read SKILL.md §工作目录约定` 验证 | design D-1 + Q-8 |
| INV-9 | 6 commit 顺序:SKILL.md(含 T-001 + T-006) → 6 占位 → 1 弃用 → 模板扩展 → CLAUDE.md → 全仓库 Grep | `git log --oneline -6` | design D-7 + plan D-PLAN-2 |
| INV-10(plan 新增) | 任务 REQ-00003-001~007 全部为"文档/规范/Markdown 文件处理"类,测试状态=不适用(纯文档任务) | PLAN.md 任务总览 | plan 阶段决策 D-PLAN-5 |
| INV-11(plan 新增) | Type B/C 严禁重写既有内容的 git 验证手段:commit 后跑 `git diff <file>` 应仅显示"+"行,无"-"行 | commit 后 `git diff` | REQU FR-10 + AC-9 |

## 6. 接口规格

详见 `interface-specs.md`。本需求**无外部编程接口**,仅记录"内部接口"契约:
- Type A 规范文件(`./assistants/rules/<分类>.md`)
- Type B 指引条目(`plugins/code-skills/CLAUDE.md` §"AI 工作约定")
- Type C 提示条目(`plugins/code-skills/skills/<技能>/templates/<name>.md`)

## 7. 异常处理

详见 `risk-analysis.md` §异常处理(E-1 ~ E-8)。

## 8. 安全要求

详见 `risk-analysis.md` §安全边界(S-1 ~ S-8)。

## 9. 状态机/流程

### 9.1 主流程状态机

```
[用户调用 code-rule + 描述]
        │
        ▼
[类型识别(FR-7,自动 + 显式)]
   ├─→ 候选唯一+高置信度 ─→ 直接进入对应类型子流程
   └─→ 候选多/低置信度 ─→ AskUserQuestion 询问
        │
        ▼
[Type A 子流程]  [Type B 子流程]  [Type C 子流程]
   │               │                │
   ▼               ▼                ▼
[分类确认]      [指引结构]      [插入位置确认]
   │               │                │
   ▼               ▼                ▼
[条件性分类追问] [追加到 CLAUDE.md] [追加到 templates/]
(现在需要/未来占位/跳过)
   │
   ▼
[填规则 / 创建占位 / 跳过]
   │
   ▼
[汇报]
```

### 9.2 关键规则
- 类型识别:自动 + 显式(FR-7)
- 并发:N/A(单文件串行追加)
- 超时:N/A(无外部依赖)
- 幂等:同一描述重复调用,`code-rule` 应识别"已添加"并提示

## 10. 性能与资源

| # | 关注点 | 描述 |
| --- | --- | --- |
| P-1 | 关键路径预估 | `code-rule` 处理 1 条规则的关键路径 = 类型识别(< 1 秒) + 写文件(< 1 秒);无外部 IO |
| P-2 | 资源限制 | 无(纯 Markdown 文件处理) |
| P-3 | 缓存策略 | 无(每次都是用户触发) |
| P-4 | 并发 | N/A(单文件串行追加) |

## 11. 测试要点

详见 `risk-analysis.md` §测试要点(T-1 ~ T-10)。

**自动化测试**:**无**(本需求是技能扩展,无运行时)
**单元测试**:**不适用**(所有任务测试状态=不适用,见 INV-10)

## 12. 规范遵循

详见 `rule-compliance.md`。本设计:
- 严格遵循 FR-9 不得修改边界(marketplace.json / plugin.json / 9 SKILL.md / CLAUDE.md 其他小节 / 工作文件)
- 严格遵循 FR-10 Type B/C 不重写既有内容
- 严格遵循 NFR-1 Type A 向后兼容(关键词表扩展但流程不变)
- 本设计**不引入**任何第三方依赖(NFR-4 最小化)
- 本设计**不创建**任何"自动化测试代码"(本需求是技能扩展,无运行时)

## 13. 待澄清/未决项

**无遗留**。所有 REQU 待澄清(Q-1 ~ Q-8)已确认或采纳默认;design 阶段 5 项澄清已与用户确认(Q-4/Q-5/Q-8)或采纳默认(Q-6/Q-7);plan 阶段 2 项澄清已与用户确认(Q-PLAN-1/Q-PLAN-2)。

## 14. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-04 09:15 | v1 | 设计新增 | 完成首次详细设计:11 章节 + 9 模块 + 11 不变量(INV-1~11)+ 7 测试要点 + 6 commit 实施计划 + 7 任务拆分(REQ-00003-001~007)。范围:扩展 `code-rule/SKILL.md` 正文(不改 frontmatter)+ 扩展 `templates/rule.md`(占位/引导模式)+ 6 个新分类占位文件 + `module-conventions.md` 追加 DEPRECATED 标记 + `plugins/code-skills/CLAUDE.md` 末尾追加"AI 工作约定"小节;**plan 阶段对 design 的微调**:类型识别引擎从"独立子流程"变更为"合并到步骤 4 子段 4.2"(Q-PLAN-2 用户答复);**任务粒度**:7 任务 / 6 commit(Q-PLAN-1 用户答复,commit 1 含 T-001 + T-006);所有任务测试状态=不适用(INV-10);新增 INV-10/11;无新增依赖,无偏离规范;**M3 待开始,REQ-00003 阻塞 `code-it` 等待用户触发** | wangmiao |
