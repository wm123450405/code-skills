# 编译与启动验证 — TASK-REQ-00013-00003
版本:V0.0.2

## 静态自检
- ✅ 8 项 INV 自检 100% 通过
- ✅ INV-1:frontmatter L1-8 字节级保留(本 SKILL.md frontmatter 8 行,含多行 description)
- ✅ INV-1:"## 工具使用约定" 段 L81-86 字节级保留
- ✅ INV-1:"---" 分隔符 L88 字节级保留
- ✅ INV-1:"## 工作流程" 章节标题 L90 字节级保留
- ✅ INV-2:锚点统一
- ✅ INV-3:屏幕输出格式契约(启动 / 登记 / 完成 / 中止 / 错误 5 类)
- ✅ INV-4:`truncateTitle` 伪代码 3 行完整性
- ✅ INV-5:0 触发 `dashboard-conventions §规则 1` 3 处同步
- ✅ INV-7:`code-fix` "## 缺陷标题" 小节不写入看板(严守)

## 修复记录
- **0 次失败**
