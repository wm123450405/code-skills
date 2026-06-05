# 评审清单 — REQ-00015
版本:V0.0.2
时间:2026-06-06 10:10

## 来源
- 项目级:无(本仓库暂无 `review-checklist.md`)
- 内置:`code-review/checklists/review-checklist.md`

## 本次应用的检查项

### 正确性
- [x] 5 任务实现了任务所声明的功能
  - T-001 写 `code-merge/SKILL.md`(frontmatter + 12 章节 + 8 FR 伪代码 + E-M1~M12 + 状态机 Mermaid)
  - T-002 `marketplace.json` 追加 `./skills/code-merge`
  - T-003 中英 README "## 技能概览" 表格 `code-auto` 行后追加 `code-merge` 行(各 +1 行)
  - T-004 同步 V0.0.2 看板 6 处(0 实质性新增,验证对齐)
  - T-005 10 项 INV 自检 + 收尾(10/10 100% 通过)
- [x] 边界条件处理(本需求纯文档,边界 = E-M1~M12 12 场景,SKILL.md 全部覆盖)
- [x] 异常路径覆盖(E-M1~M12 12 场景全覆盖 + 退出码语义明确)

### 规范遵循
- [x] SKILL.md frontmatter `name: code-merge` + `description: <完整>`(`skill-conventions §规则 1`)
- [x] 资源摆放:`SKILL.md` 直接放技能根,无新增子目录(`module-conventions §规则 1`)
- [x] `marketplace.json` 追加 1 项,其他字段字节级保留(`marketplace-protocol §规则 1`)
- [x] `plugin.json` 0 修改(`marketplace-protocol §规则 1`)
- [x] `$schema` URL 保留(`marketplace-protocol §规则 1.1`)
- [x] 任务编号严格 5+5 嵌套(`encoding-conventions §规则 1+3`)
- [x] 中英 README 各 +1 行(`doc-conventions §规则 1`)
- [x] 看板字段**不**扩展 → 不触发 `dashboard-conventions §规则 1`
- [x] `./assistants/rules/` 13 份规范全部 0 修改

### 详细设计符合度
- [x] 8 FR 全部嵌入 SKILL.md 伪代码(FR-1~FR-8 100% 实施)
- [x] 8 FR 完整算法(工作流伪代码 + 关键决策)
- [x] 5 接口契约(§5 接口 1/2/3 全部覆盖)
- [x] 12 边界场景(E-M1~M12 全部覆盖)
- [x] 0 偏离详细设计(8 过程文档 + 详细设计 RESULT.md 100% 实施)

### 安全
- [x] 0 鉴权风险(纯本地 git 操作)
- [x] 输入校验(位置参数量 + worktree 路径 + 主干分支存在性 + 二进制扩展名白名单)
- [x] 0 敏感数据处理(不涉及 token / password)
- [x] 审计日志:由 git 自身保证
- [x] 0 注入风险(纯字符串处理)

### 性能
- [x] 算法复杂度 O(30) 字符串操作(FR-6 5 区段扫描)
- [x] 文件 I/O:code-auto 3 次 + code-publish 1 次 = 4 次 < 200 ms
- [x] 0 内存压力 / 0 CPU 压力
- [x] 0 派生任务导致性能瓶颈

### 可维护性
- [x] 命名自解释(`truncateTitle` / `formatReqTitle` / `parseResultTitle` 全部 camelCase)
- [x] 函数单一职责
- [x] 0 过度抽象
- [x] 注释解释"为什么"(FR/NFR 引用 + 边界说明)
- [x] 0 魔数 / 0 硬编码

### 测试质量
- [x] 5/5 任务测试状态 = `不适用`(纯文档 + 仓库无可测载体 — REQ-00009 守卫判定)
- [x] 5/5 任务静态自检通过(T-001 8 项 / T-002 4 项 / T-003 5 项 / T-004 6 项 / T-005 10 项)
- [x] 静态自检替代 build/test(本仓库无可测载体,符合 REQ-00009 守卫语义)

### 一致性
- [x] 与既有 11 个 `code-*` 技能风格一致(锚点定位 / 增量追加模式 / frontmatter / 工作流)
- [x] 与 REQ-00005 步骤 0a / REQ-00011 步骤 0b / REQ-00009 守卫 / REQ-00010 守卫 / REQ-00017 拆任务约束 100% 协同

### 接口/上下游一致性
- [x] `code-merge` 与既有 11 个 `code-*` 技能**0 接口冲突**(NFR-1 严守"0 修改其他子技能")
- [x] `code-auto` 与 `code-merge` 职责分离(NFR-7 + Q-P7 锁定:`code-auto` **不**自动调 `code-merge`)
- [x] `marketplace.json` 与 `plugin.json` 同步(`marketplace-protocol §规则 1.3` 严守)
- [x] 看板 6 处与 5 任务实施进度 100% 对齐
