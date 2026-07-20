# 缺陷登记 — BUG-00009

## 缺陷标题

`/code ver` 切换版本后未在最后阶段提交代码

## 缺陷描述(用户原始输入)

> 使用 `/code ver` 命令切换版本后应当在最后阶段提交代码,目前代码没有提交,`2026-07-20-112733-local-command-caveatcaveat-the-messages-below.txt` 文件中记录了最后的执行过程。

## 触发条件

1. 用户在已初始化的项目中调 `/code ver <目标版本号>`
2. 当前版本有活跃内容,用户选择先发布再切换(或直接切换不发布)
3. SKILL.md 走步骤 1B-6B,完成步骤 4B 创建新版本工作空间、写 `.current-version`
4. **步骤 6B 验证与汇报后,流程退出,未触发任何 git 提交**

## 复现路径(2026-07-20 实测)

```
当前:V0.0.5(5 需求 + 8 缺陷,全部 DONE)
↓
/code ver V0.0.6
↓
用户选"先发布 V0.0.5 再切换"
↓
步骤 3B:发布检查 → 生成 DEPLOY.md / UPDATE.md / FAQ.md / faq/README.md
↓
步骤 4B:创建 V0.0.6/ + RESULT.md + 切换 .current-version
↓
步骤 6B:汇报(屏幕输出)
↓
退出 → 工作区 dirty
```

复现文件:
- 新增 5 个:`DEPLOY.md` / `UPDATE.md` / `FAQ.md` / `faq/README.md` / `faq/FAQ.md` / `V0.0.6/RESULT.md`
- 修改 1 个:`.current-version`
- 总计 7 个文件,**全部未提交**

## 可能成因

### 根因 1:`/code ver` 缺乏"DONE 阶段"等价物

`/code req` 与 `/code fix` 在 SKILL.md 的 DONE 阶段(步骤 6)明确定义了"执行兜底提交":
```
执行 git rev-parse --git-dir  → 非 git 仓库则跳过
执行 git status --porcelain   → 输出为空则跳过
执行 git add -A
生成 commit message
AskUserQuestion 确认后 commit(非 --auto)/ 直接 commit(--auto)
```

`/code ver` 的步骤 6B"验证与汇报"**未包含任何 git 操作**,等价于跳过了兜底提交。

### 根因 2:SKILL.md 步骤 6B 描述与 req/fix DONE 不一致

`/code ver` 步骤 6B 仅产出"屏幕输出验证与汇报",无 git commit 环节。
对比 `/code req` 步骤 6"执行兜底提交(强制,不可跳过)"——这是已落地的强约束。

### 根因 3:`references/ver/common.md` §3.4 步骤 6B 缺少 git 提交逻辑

`references/ver/common.md` 是 `ver` 的执行细节参考,§3.4 当前描述为"验证与汇报"——不含 git 操作。

## 影响范围

| 受影响对象 | 影响 |
| --- | --- |
| `/code ver` 所有版本切换路径 | 工作区 dirty,所有产物未入库 |
| V0.0.5 → V0.0.6 实测 | 7 个产物文件全部 untracked |
| 发布产物(publish/DEPLOY.md 等) | 未随代码库版本化 |
| 跨版本规则 | `rules/` 未受影响,但 .current-version 是版本切换的运行时状态 |
| 历史影响 | 之前所有 `/code ver` 切换若产生过文件,可能也未提交 |

## 严重程度

**P1** — 不阻塞开发流程,但每次版本切换都留下未提交 dirty 状态,违反"代码修改必提交"的基本纪律;长期积累将导致 `git status` 噪声、误操作丢文件风险。

## 与既有规范/缺陷的关系

- 与 `req` / `fix` 的 DONE 阶段兜底提交机制形成不一致(它们有,`ver` 没有)
- 类似缺陷 `BUG-00004`(DONE 阶段兜底提交未触发,指令不够显式)——但 BUG-00004 是 req/fix 侧,本缺陷是 ver 侧
- `ver` SKILL.md 没有"阶段"概念(只有步骤 1A/1B/1C/1D/2-6B),但具备类似的"最后阶段"语义,即"步骤 6B 验证与汇报"

## 修复方向(待 DESIGN 阶段确认)

候选方案:
- **方案 A**(推荐):在 `/code ver` SKILL.md 的"步骤 6B 验证与汇报"中加入 git 兜底提交逻辑,与 req/fix DONE 阶段对齐
- **方案 B**:在 `references/ver/common.md` §3.4 步骤 6B 详细描述中加入 git 操作
- **方案 C**:方案 A + B 同时实施

## 复现材料

- 用户执行记录:`./2026-07-20-112733-local-command-caveatcaveat-the-messages-below.txt`
- 当前工作区状态:`git status --porcelain` 应包含 7 个 untracked + 1 modified
