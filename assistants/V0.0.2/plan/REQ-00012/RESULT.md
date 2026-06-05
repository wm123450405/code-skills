# 详细设计 — REQ-00012(在仓库根创建极简 README + 移动 CLAUDE.md 到根)

- 需求编码:REQ-00012
- 所属版本:V0.0.2
- 设计版本:v1
- 状态:已完成(首次)
- 责任人:wangmiao
- 创建:2026-06-05
- 最近更新:2026-06-05
- 上游需求:`./assistants/V0.0.2/require/REQ-00012/RESULT.md`(v1)
- 上游概要设计:`./assistants/V0.0.2/design/REQ-00012/RESULT.md`(v1)
- 遵循规范:`./assistants/rules/` 下 13 个文件,核心约束来自 `doc-conventions.md §规则 1 / §规则 2`

---

## 1. 概述

本详细设计把概要设计"仓库根门面改造"落地为**可直接编码的 3 个功能点任务**(零代码模块、零 API 变更、零数据结构、零依赖)。

**核心范围**:
1. **T-001**:创建仓库根 `./README.md`(中文,< 50 行)
2. **T-002**:创建仓库根 `./README.en.md`(英文,< 50 行,与 T-001 同次提交)
3. **T-003**:`git mv plugins/code-skills/CLAUDE.md → ./CLAUDE.md`(原位置不保留)

## 2. 模块详细化

### 模块 1:仓库根 README(中文 + 英文)

| 维度 | 内容 |
| --- | --- |
| 路径 | `./README.md`(中文)+ `./README.en.md`(英文) |
| 文件类型 | Markdown |
| 行数限制 | < 50 行(NFR-2 强制) |
| 章节结构 | `## 简介` / `## 快速开始` / `## 主要能力` / `## 📖 详细文档` / `## 许可证` |
| 链接 | `./plugins/code-skills/README.md`(详细文档) |
| 内部命令 | `claude plugin marketplace add ...` / `claude plugin install code-skills@code-skills` / `/code-version` / `/code-require` |
| 与概要设计对应 | §3 模块拆分(根 README 中/英 2 个文档模块) |
| 符合的规范 | `doc-conventions §规则 1`(章节对仗)+ `§规则 2`(核心小节,主动善意) |

### 模块 2:`CLAUDE.md` 移动

| 维度 | 内容 |
| --- | --- |
| 原路径 | `plugins/code-skills/CLAUDE.md`(9,418 bytes) |
| 新路径 | `./CLAUDE.md`(内容不变) |
| 操作 | `git mv plugins/code-skills/CLAUDE.md CLAUDE.md` |
| 副作用 | 旧位置 `plugins/code-skills/CLAUDE.md` 删除 |
| 与概要设计对应 | §3 模块拆分(移动模块 1 个) |
| 符合的规范 | NFR-3(git mv 保留 blame)+ NFR-8(不提供重定向) |

## 3. 算法与逻辑

### 算法 1:创建根 README(中文)— T-001

```
步骤 1:  Read REQ-00012/RESULT.md §6.1 模板(40 行 Markdown)
步骤 2:  Write ./README.md
         - 第 1 行:# code-skills
         - 第 2 行:> <一句话简介>
         - ## 简介(说明技能集合覆盖范围)
         - ## 快速开始(3 步:marketplace add / install / 首个技能)
         - ## 主要能力(11 个 code-* 技能表格)
         - ## 📖 详细文档(链到 plugins/code-skills/README.md)
         - ## 许可证([MIT](LICENSE))
步骤 3:  Validate:行数 < 50 + 含核心 5 小节
```

### 算法 2:创建根 README(英文)— T-002

```
步骤 1:  Read REQ-00012/RESULT.md §6.2 模板(40 行 Markdown)
步骤 2:  Write ./README.en.md
         - 章节名与中文版**对仗**:Introduction / Quick Start / Main Capabilities / Detailed Documentation / License
         - 11 技能表格行顺序与中文版**完全一致**(便于 §规则 1 对仗校验)
步骤 3:  Validate:行数 < 50 + 章节对仗(中英 1-1 对应)
步骤 4:  git add README.md README.en.md(同次提交准备,§规则 1 强制)
```

### 算法 3:移动 CLAUDE.md — T-003

```
步骤 1:  Validate:./CLAUDE.md 不存在(防止覆盖)
步骤 2:  Validate:plugins/code-skills/CLAUDE.md 存在(9,418 bytes)
步骤 3:  Bash: git mv plugins/code-skills/CLAUDE.md CLAUDE.md
         - 保留 git blame 历史(NFR-3)
步骤 4:  Validate:
         - 仓库根 ./CLAUDE.md 存在
         - 仓库根 ./CLAUDE.md 大小 = 9,418 bytes
         - plugins/code-skills/CLAUDE.md 不存在
步骤 5:  git commit -m "chore(repo): move CLAUDE.md to repo root (REQ-00012)"
```

### 算法 4:同次提交收尾 — T-001/T-002 完成后

```
按 doc-conventions §规则 1:T-001 + T-002 必须**同次提交**。
提交序列:
  git add README.md README.en.md
  git commit -m "chore(repo): add root README/README.en.md (REQ-00012)"

T-003 移动可与 T-001/T-002:
  - 选项 A:同次提交(更紧凑,1 个 commit)
  - 选项 B:分次提交(更可读,2 个 commit)
需求 FR-5 AC-5.5:**不强求同次**,默认采用分次提交
(中文 README + CLAUDE.md 移动是不同语义层)。
```

## 4. 数据结构完整变更

**无数据模型变更**(NFR-1 零依赖,NFR-4 不破坏现有结构)。

## 5. 接口细节

**无 API 变更**。文档模块的"接口"是 Markdown 内部链接,详见概要设计 §4 + 模块详细化 §模块 1。

## 6. 异常处理

| 异常路径 | 处理策略 | 监控/退出码 |
| --- | --- | --- |
| `./CLAUDE.md` 已存在(E-3) | 中止 + 报错"目标已存在,无法移动" | 退出码 ≠ 0 |
| `plugins/code-skills/CLAUDE.md` 不存在(E-2) | 中止 + 报错"无 CLAUDE.md 可移动" | 退出码 ≠ 0 |
| `./README.md` 已存在(E-4) | 中止 + 报错"目标已存在,无法新建" | 退出码 ≠ 0 |
| `./README.en.md` 已存在(E-5) | 中止 + 报错"目标已存在,无法新建" | 退出码 ≠ 0 |
| `git mv` 失败(权限等,E-6) | 中止 + 报错退出,用户手动处理 | 退出码 ≠ 0 |
| 行数超 50(NFR-2) | 中止 + 报错"超出极简约束" | 退出码 ≠ 0 |
| 中英章节不对仗(§规则 1) | 中止 + 报错"结构漂移" | 退出码 ≠ 0 |

## 7. 安全要求

**本需求无安全约束**(纯文档变更,无代码执行入口)。

## 8. 状态机/流程

```
[开始]
  ↓
[T-001:写中文 README]
  ↓
[T-002:写英文 README]
  ↓
[同次提交 T-001 + T-002]
  ↓
[T-003:git mv CLAUDE.md]
  ↓
[commit T-003]
  ↓
[完成]
```

## 9. 性能与资源

**无性能约束**(纯文档创建,微秒级)。

## 10. 测试要点

**本需求无可测代码载体**(仓库无构建/测试文件),`code-unit` 守卫会判定"不可测"(NFR-2 in `doc-conventions`)。

| 验证类型 | 方式 |
| --- | --- |
| 文件存在性 | `ls` 3 个新文件 + 1 个删除 |
| 字节级保留 | `wc -c plugins/code-skills/CLAUDE.md` 移动前后 = 9,418 |
| 行数限制 | `wc -l` 根 README + README.en.md < 50 |
| 章节对仗 | grep 章节名集合 `{简介,Introduction} / {快速开始,Quick Start} / ...` |
| git blame 保留 | `git log --follow CLAUDE.md` 可见历史 |
| 原位置删除 | `ls plugins/code-skills/CLAUDE.md` → 不存在 |

## 11. 规范遵循

- `doc-conventions §规则 1`:中英 README 同次提交(T-001+T-002)✓
- `doc-conventions §规则 1`:章节结构对仗(5 个 1-1 对应)✓
- `doc-conventions §规则 2`:核心小节覆盖(简介/快速开始/主要能力/详细文档/许可证)✓(主动善意)
- `commit-conventions`:NFR-7 1 行 message ✓
- 100% 沿用上游 FR / NFR / AC,**0 规范冲突 / 0 授权偏离**

## 12. 待澄清/未决项

- Q-1~Q-9 全部沿用 `code-require` 阶段结论(详见 `clarifications.md`)
- 0 本阶段新增澄清

## 13. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-05 | v1 | 初始创建:3 个功能点任务 + 0 架构任务(触发条件 1/2/3 均不满足) + 4 个算法(写中/写英/移动/收尾) + 7 个异常路径 + 6 项验证手段 + 100% 规范遵循 | wangmiao |
