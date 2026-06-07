# 材料登记 — REQ-00024
更新时间:2026-06-07

## 用户原始输入
- **类型**:自然语言描述(无材料附件)
- **完整文本**(本轮用户输入):
  > 移除 `/code-auto` 中的 from 关键字逻辑,通过文件/文件夹是否存在判断后续步骤走向,默认任务输入内容为需求编号,若 `./assistants/版本号/require/需求编号` 文件夹存在表示确实为需求编号,再判断 `./assistants/版本号/require/需求编号/RESULT.md` 文件是否存在,若 `./assistants/版本号/require/需求编号/RESULT.md` 文件存在表示已完成需求分析,直接进入后续的需求概要设计阶段;若 `./assistants/版本号/require/需求编号/RESULT.md` 文件不存在表示尚未完成需求设计,则进入需求设计阶段;若 `./assistants/版本号/require/需求编号` 文件夹不存在,则认定输入内容为缺陷编号,判断 `./assistants/版本号/fix/缺陷编号` 文件夹是否存在,若 `./assistants/版本号/fix/缺陷编号` 文件夹存在,按照缺陷修复逻辑进入缺陷修复详设阶段;若 `./assistants/版本号/fix/缺陷编号` 文件夹也不存在,则认定输入内容为需求内容,直接将内容添加为需求,并进入需求设计阶段。

## 关键摘录
- **本需求核心**:用"路径感知"(文件/文件夹存在性)替代 `from` 关键字
- **默认输入** = 需求编号
- **4 条判定链**:
  1. `require/<input>/` 存在 + `RESULT.md` 存在 → 跳到概要设计
  2. `require/<input>/` 存在 + `RESULT.md` 不存在 → 进入需求设计
  3. `fix/<input>/` 存在 → 进入缺陷修复详设
  4. 都不存在 → 视为需求内容,分配新编号

## 已读参考材料
| 路径 | 类型 | 用途 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-auto/SKILL.md` | 文档 | 理解现有 from 关键字实现 |
| `plugins/code-skills/skills/code-require/SKILL.md` | 文档 | 了解 code-require 接口契约 |
| `assistants/V0.0.3/RESULT.md` | 看板 | 确认当前版本状态(本需求归属 V0.0.3) |
| `./assistants/rules/*.md` | 规范 | 13 份规范(本需求 0 触发新增/修改) |
