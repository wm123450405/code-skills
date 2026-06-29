# 关联需求 — REQ-00042

## REQ-00036 (技能文档开发痕迹清理, 版本 V0.0.3)
- **关联点**:REQ-00036 规定 SKILL.md 与 templates/ 中不得包含开发痕迹(需求编号/缺陷编号/决策记录等),本需求将其理念扩展到代码产出层面
- **影响**:本需求与 REQ-00036 互补——REQ-00036 清理技能文件本身,本需求清理技能产出到目标项目的代码
- **来源**:扫描 ./assistants/V0.0.3/require/REQ-00036/RESULT.md + ./assistants/rules/skill-conventions.md 规则 2

## REQ-00041 (技能多语言模块化重构, 版本 V0.0.4)
- **关联点**:REQ-00041 重构了 code-it 的文件结构(SKILL.md + references/),本需求的修改需要在 references/common.md 的编码原则中落地
- **影响**:本需求需在 REQ-00041 重构后的文件结构上实施,修改 references/common.md §5(通用编码原则)
- **来源**:扫描 ./assistants/V0.0.4/require/REQ-00041/RESULT.md