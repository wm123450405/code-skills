# 材料登记 — REQ-00030

更新时间:2026-06-12 14:11
版本:V0.0.3

## 用户原始输入

> 目前技能 `/code-design`,输出的内容过于细节全面,而 `/code-plan` 却只直接使用了,并没有进一步分析,请优化这两个技能,确保 `/code-design` 只做概要设计,`/code-plan` 才开始做详细设计。同时对 `/code-design` 中关于扩展性选项的优化:较小的需求没必要考虑扩展性,可以不选择;稍大的需求或需要使用第三方依赖的需求才考虑扩展性,并且高扩展性的设计编码阶段才考虑新增前置框架任务、详设阶段考虑框架设计,概设阶段无需展开扩展新设计细节。

## 关键提取

- **核心痛点**:`code-design` 输出内容"过深",挤压了 `code-plan` 的产出空间;`code-plan` 沦为"直接使用 design 的结果"
- **优化目标 A**:`code-design` 只做**概要设计**;`code-plan` 才开始**详细设计**
- **优化目标 B**(扩展性选项):
  - 较小的需求 → **不**考虑扩展性
  - 稍大的需求 / 需要使用第三方依赖的需求 → 才考虑扩展性
  - 扩展性相关设计:
    - 概设阶段:**不**展开扩展新设计细节
    - 详设阶段:考虑框架设计
    - 编码阶段:才考虑新增前置框架任务

## 关联需求与设计(已落地的实证)

| 编号 | 标题 | 关键证据 | 路径 |
| --- | --- | --- | --- |
| REQ-00029 | 优化 /code-dashboard 屏显报告 | design=177 行(含 §1-§11 + INV-1~7),plan=298 行(详设反比概设更厚) | `./assistants/V0.0.3/design/REQ-00029/RESULT.md`、`./assistants/V0.0.3/plan/REQ-00029/RESULT.md` |
| REQ-00028 | 新增 code-answer 技能 | design=142 行(包含"禁用工具列表"等细粒度,详设反无新增内容) | `./assistants/V0.0.3/design/REQ-00028/RESULT.md`、`./assistants/V0.0.3/plan/REQ-00028/RESULT.md` |
| REQ-00025 | (跨多技能) | design=246 行 / plan=504 行 + 456 行 — plan 反向是 design 的 2 倍 | `./assistants/V0.0.3/design/REQ-00025/`、`./assistants/V0.0.3/plan/REQ-00025/` |
| REQ-00023 | (跨多技能) | design=425 行(单文件 425 行概设,落地为 plan 334 行) | `./assistants/V0.0.3/design/REQ-00023/` |

**实证规律**:`design/.../RESULT.md` 行数普遍 ≥ `plan/.../RESULT.md`,且当 plan 反而更厚时(如 REQ-00025 / REQ-00027),多为 plan 在补做"design 漏掉的"细节——直接证明 design 越界、plan 沦为"填空"。

## 上游规范(./assistants/rules/)

| 规范文件 | 关键约束摘要 |
| --- | --- |
| `skill-conventions.md §规则 1` | SKILL.md 必须含 name + description;name 与目录名一致;frontmatter L1-3 字节级保留 |
| `module-conventions.md §规则 1` | 资源文件必须放 `templates/` / `guidelines/` / `checklists/` 子目录 |
| `doc-conventions.md` | 文档章节布局、引用方式(本需求主要约束项) |
| `encoding-conventions.md` | 任务编号正则(本需求不直接受影响) |
| `dashboard-conventions.md §规则 1` | 看板字段三方同步(本需求不触发字段扩展) |

## 上下游技能(本需求的影响面)

- **直接修改**:
  - `plugins/code-skills/skills/code-design/SKILL.md`(步骤 9A-11A 弱化 + 步骤 0b 收敛)
  - `plugins/code-skills/skills/code-design/templates/design.md`(§7-§11 深度上限)
  - `plugins/code-skills/skills/code-plan/SKILL.md`(步骤 7A 强化"补做"职责)
  - `plugins/code-skills/skills/code-plan/templates/plan.md`(§4-§10 展开)
- **横向参考**(不改):
  - `plugins/code-skills/skills/code-auto/SKILL.md`(沿用 `--balanced` 默认)
  - `plugins/code-skills/skills/code-it/SKILL.md`(沿用"首个任务 = 架构骨架"既有契约)
- **看板同步**:
  - `./assistants/V0.0.3/RESULT.md`(本需求在 V0.0.3 处理 → 同步"需求清单" + "变更记录"区段)
