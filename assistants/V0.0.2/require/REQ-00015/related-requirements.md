# 关联需求 — REQ-00015

## REQ-00010(优化 `/code-it`,增加"前置任务"守卫)— V0.0.2
- **关联点**:`code-it` 步骤 0a 的"前置任务检查"守卫会读 `plan/<REQ>/PLAN.md` 判定任务开发顺序;`code-merge` 在合并 worktree 时,若涉及 `plan/<REQ>/PLAN.md` 的看板数据冲突,需在合并后**自检** PLAN.md 的"任务总览"顺序是否与实际 `code/<TASK>/` 目录一致
- **影响**:`code-merge` 看板自检的"任务清单"区段需检查"关联任务"列与"完成时间"列的逻辑顺序
- **版本**:V0.0.2

## REQ-00004(添加 `/code-dashboard` 开发看板技能)— V0.0.2
- **关联点**:`code-dashboard` 是消费方,只读看板;`code-merge` 自检 5 区段的能力应与 `code-dashboard` 的解析口径一致(任务编号双格式 / 状态字面不归一化 / 真正可发布算法)
- **影响**:`code-merge` 内部自检需复用 `code-dashboard` 的算法 1(区段解析)+ 算法 4(`parseTaskId`)+ 算法 5(`renderBar`),避免双方口径不一致
- **版本**:V0.0.2

## REQ-00007(增加 `/code-auto` 自动开发技能)— V0.0.2
- **关联点**:`code-auto` 是 `code-merge` 的潜在上游 — 在自动开发循环中,`code-auto` 可能驱动 `code-it` 多次提交,最终需 `code-merge` 收尾
- **影响**:`code-merge` 不**被** `code-auto` 调用(Q-1 锁定 code-auto 不调 code-merge),但 `code-merge` 应支持"被外部技能触发后,在 dirty tree 上继续运行"的场景
- **版本**:V0.0.2

## REQ-00005(优化 code-require/code-design/code-plan,首步拉取+末步提交)— V0.0.2
- **关联点**:`code-require` / `code-design` / `code-plan` 都有"步骤 0a 拉取最新代码"与"步骤 N 末尾兜底提交"逻辑;`code-merge` 在 worktree 内部执行的"提交所有文件"应**复用**步骤 N 的 commit message 模板(`chore(<scope>):` 格式)
- **影响**:`code-merge` 步骤 4.6 的 commit message 生成逻辑应与 `code-require` / `code-design` / `code-plan` 的步骤 N 同源
- **版本**:V0.0.2

## REQ-00006(增加 `/code-publish` 发布部署技能)— V0.0.2
- **关联点**:`code-publish` 在"前置检查"时要求"所有需求=已完成 ∧ 所有任务=已完成 ∧ 测试∈{已运行-通过, 不适用} ∧ 缺陷=已修复";`code-merge` 合并完成后,若自检发现看板数据未达 `code-publish` 前置条件,应**不阻止** `code-merge` 退出(只打印提示)
- **影响**:`code-merge` 不阻塞 `code-publish` 流程,自检失败仅打印提示,用户后续自行决定
- **版本**:V0.0.2

## V0.0.1 任务 `T-001`(已迁移至 V0.0.2,内容:`/code-fix` 创建 + 0 模板 + 17 任务)— V0.0.1(已合并)
- **关联点**:`code-fix` 是缺陷管理技能,缺陷 ID 走 `^BUG-\d{5}$` 格式(`encoding-conventions §规则 1`);`code-merge` 自检的"缺陷清单"区段需严格按 `BUG-NNNNN` 解析
- **影响**:`code-merge` 内部自检的"缺陷清单"解析应与 `code-fix` 一致
- **版本**:V0.0.1(基线,已合并至 V0.0.2)
