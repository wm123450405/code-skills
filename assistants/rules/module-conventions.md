# 模块规划规范(module-conventions)

> 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
> 最后更新:2026-06-03 18:50
> 适用版本:跨所有版本共享(项目级)

> ⚠️ **DEPRECATED(已弃用)**:本文件内容已迁移到 `directory-conventions.md`(2026-06-04 REQ-00003 H2 决策,详见 `plan/REQ-00003/RESULT.md`)。本文件保留作为历史参考,新规则请追加到 `directory-conventions.md`。

## 适用场景
本规范适用于 `plugins/code-skills/skills/<技能名>/` 目录内子目录的命名与用途,以及"技能引用的资源"在仓库中的摆放位置。涉及"模板/清单/规则放在哪里"时查阅本文件。

## 强制级别约定
本文件中各规则的强制级别逐条标注(参见各"规则 N"小节的"强制级别"字段),本文件头部不统一声明。

---

## 规则 1:技能资源必须放在技能目录的固定子目录中

### 条款
`plugins/code-skills/skills/<技能名>/` 下的所有**资源文件**必须放在下列固定子目录之一,不得散落到仓库其它位置:

| 子目录名(固定) | 用途 | 命名风格 |
| --- | --- | --- |
| `templates/` | 技能产出的文档模板(如 `version-RESULT.md`、`requirements.md`、`bug.md` 等) | kebab-case `<用途>.md` |
| `checklists/` | 技能强制执行的校验清单(如 `review-checklist.md`) | kebab-case `<用途>.md` |
| `guidelines/` | 技能强制遵守的规则文档(如 `coding-style.md`) | kebab-case `<用途>.md` |

例外:`SKILL.md` 本身放在技能根目录(不放在子目录里),它是技能入口。

资源类型不在以上三类中的(例如原始示例、测试夹具、未来新增的"工具脚本"),需先经设计评审再决定放在哪个子目录;**禁止**直接放技能根目录或仓库其它位置。

### 强制级别
- 必须

### 适用范围
- `plugins/code-skills/skills/*/` 目录(本插件所有技能)
- 资源文件**包括但不限于**:`.md` 模板 / `.md` 清单 / `.md` 指南;二进制资源(图表/音频)同样适用本约束(放对应子目录)

### 正面示例
```
plugins/code-skills/skills/code-review/
├── SKILL.md
├── checklists/
│   └── review-checklist.md     # ✅ 在固定子目录
└── templates/
    ├── REVIEW-REPORT.md
    ├── REVIEW-FIX.md
    └── assistants-layout.md
```

### 反面示例
```
plugins/code-skills/skills/code-review/
├── SKILL.md
├── my-checklist.md              # ❌ 散落在技能根目录(应在 checklists/)
├── docs/
│   └── REVIEW-REPORT.md         # ❌ 使用了非约定子目录名(应在 templates/)
└── REVIEW-FIX.md                # ❌ 散落在技能根目录(应在 templates/)
```

### 例外
- 临时草稿(尚未进入正稿的探索性 `.md`)可放在 `drafts/` 子目录,但需在文件头标注"草稿,未生效",且不得被任何 `code-*` 技能引用

### 关联规范
- `./assistants/rules/skill-conventions.md §规则 1`(SKILL.md frontmatter 必含 name + description)
- `./assistants/rules/dashboard-conventions.md §规则 1`(看板/模板扩展时的同步)

### 来源
- 由 `code-rule` 技能添加于 2026-06-03 18:50
- 用户原始描述:"技能引用的资源(模板/清单/规则)放同级 `templates/` / `checklists/` / `guidelines/`,不放别处"
