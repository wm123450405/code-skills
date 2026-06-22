# 设计权衡笔记 — REQ-00039

更新时间:2026-06-22 15:00
版本:V0.0.3

## 1. 关键设计问题

| # | 问题 | 选定 | 理由 |
| --- | --- | --- | --- |
| Q-1 | 逻辑行计算函数伪代码放哪? | **`logic-loc.md` 共享库** | DRY 原则;`code-it` / `code-check` 共用 |
| Q-2 | tokei / cloc 检测 vs 启发式回退 vs 阈值默认值 | **3 个独立文档(`logic-loc.md` + `logic-loc-defaults.md`)** | 单一职责;阈值配置可能用户覆盖 |
| Q-3 | `calcLogicLoc` 失败时如何处理? | **屏显 `⚠` + 跳过,不阻断 `code-it`** | NFR-7 不阻断 |
| Q-4 | `code-check` 步骤 8.13 派生发现格式 | **字节级沿用 8.12 屏显契约** | 学习成本低 |
| Q-5 | 缺陷分支是否完全跳过 `calcLogicLoc`? | **完全跳过** | NFR-8;与 REQ-00038 一致 |
| Q-6 | 单文件过大(> 10MB)如何处理? | **跳过该文件,屏显警告** | 性能保护 |
| Q-7 | git diff 失败(非 git 仓库)如何处理? | **屏显 `⚠` + 跳过** | 退化路径 |

## 2. 候选方案对比

### 2.1 Q-1 逻辑行计算函数伪代码位置

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| A. `code-it/SKILL.md` 内嵌 | 1 文件搞定 | `code-check` 需重复定义 |
| B. `logic-loc.md` 共享库 | DRY;沿用既有 `module-conventions` | 1 个新文件 |
| C. `code-check/SKILL.md` 内嵌 | `code-check` 自身可单读 | `code-it` 需重复定义 |

**选定 B**(DRY + 共享)。

### 2.2 Q-2 工具集成文档结构

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| A. 1 个文档含 3 函数 | 1 文件搞定 | 单一职责违反 |
| B. 3 个独立文档 | 单一职责;可独立扩展 | 文件多 |
| C. 2 个文档(函数 + 默认值) | 平衡 | — |

**选定 C**(2 个文档:`logic-loc.md` 含 4 函数 + `logic-loc-defaults.md` 含 2 字段)。

## 3. 选定方案

### 3.1 `logic-loc.md` 共享库(新建)

包含 4 个函数伪代码(`detectLocTool` / `calcLogicLines` / `heuristicLoc` / `code-check-exceed`)+ 检测机制 + 启发式算法 + 派生发现格式。

### 3.2 `logic-loc-defaults.md` 默认值(新建)

```
单文件逻辑行总规模阈值:500
单文件逻辑行新增阈值:200
```

### 3.3 `code-it/SKILL.md` 步骤 8 末尾追加 2 子步骤(修改)

`detectLocTool`(沿用库 §1)+ `calcLogicLoc`(沿用库 §2)+ 屏显契约。

### 3.4 `code-check/SKILL.md` 步骤 8 末尾追加 1 子步骤(修改)

`code-check-exceed`(沿用库 §4)+ 评审维度速查表新增第 13 维度"代码行数超标"(P3)。

### 3.5 `code-it/templates/RESULT.md` 新增"## 逻辑行统计(由 code-it 内化)"小节示例(修改)

沿用既有"## 单元测试(由 code-it 内化)"小节位置 + 格式。

## 4. 不变量(NFR)

- **不**修改 `code-it` / `code-check` frontmatter(L1-3 字节级保留)
- **不**修改既有"## 工作流程"小节 / "## 不要做的事"小节
- **不**修改其他 9 个 `code-*` 技能 SKILL.md
- **不**修改 `code-check` 步骤 8.1 ~ 8.12 子步骤(字节级沿用)
- **不**修改 `code-it` 步骤 8a / 8.5(REQ-00034 + REQ-00038 改造范围)
- **不**触发 `AskUserQuestion`(code-auto 上下文)
- **不**新增 CLI 参数
- **不**新增三方依赖

## 5. 风险与回退

- **R-1**:tokei / cloc 在用户环境**未**安装 → 启发式回退立即生效(用户已接受,精度 ~95%)
- **R-2**:启发式不支持的语言 → 退化到"统计非空非注释行"(纯字符串匹配)
- **R-3**:跨平台路径 → 沿用 `path.posix` 规范化
- **R-4**:`calcLogicLoc` 失败 → 屏显 `⚠` + 跳过(NFR-7)
- **R-5**:`code-check` 8.13 误触发 → 屏显 `⚠` + 跳过,不阻断

**回退方式**:单 commit 模式 `Bash: git revert HEAD`(T-7 末尾兜底统一处理)

## 6. 与上游 REQ-00038 / REQ-00037 / REQ-00034 的协同

- **REQ-00038**:`code-it` 步骤 8a / 8.5(模块级单测)— 本需求**不**修改
- **REQ-00037**:`code-it` §缺陷分支 17-25 — 本需求缺陷分支不触达(NFR-8)
- **REQ-00034**:`code-it` 步骤 8a / 8.5(原 `code-unit` 整合)— 本需求**不**修改