# 关联需求 — REQ-00021

## REQ-00020(V0.0.3):架构设计目标重新归位 + 3 新维度
- **关联点**:本需求沿用 V0.0.3 工作空间(同版本),不与 REQ-00020 的架构设计目标冲突
- **影响**:本需求**不**涉及架构设计目标,仅新增 CLI 参数 + 模板填充
- **来源**:扫描 `./assistants/V0.0.3/require/REQ-00020/RESULT.md`

## REQ-00005(V0.0.2):首步拉取最新代码 + 末步兜底提交
- **关联点**:本需求 `--result` / `--plan` 解析在步骤 0 之前;末步兜底提交沿用
- **影响**:FR-1 解析位置在"步骤 0a 拉取"前;模板产出物也参与 git 跟踪(末步 commit)
- **来源**:扫描 `./assistants/V0.0.2/require/REQ-00005/RESULT.md`

## REQ-00007(V0.0.2):`code-auto` 自动开发技能
- **关联点**:本需求 `code-auto` 不传 `--result` / `--plan`(沿用 Q-4 "总选推荐项",推荐项**不**含模板参数)
- **影响**:INV-9 + E-4 锁定 `code-auto` 不传 2 参数
- **来源**:扫描 `./assistants/V0.0.2/require/REQ-00007/RESULT.md`

## REQ-00011(V0.0.2):`code-design` / `code-plan` 步骤 0b 设计目标确认
- **关联点**:本需求**不**改步骤 0b;`--result` / `--plan` 在步骤 0 之前解析
- **影响**:本需求与步骤 0b 协同 0 冲突
- **来源**:扫描 `./assistants/V0.0.2/require/REQ-00011/RESULT.md`

## REQ-00013(V0.0.2):6 技能启用"编号+标题" 显示
- **关联点**:本需求模板填充屏显沿用 `formatReqTitle` 风格
- **影响**:NFR-4.1 屏显格式契约
- **来源**:扫描 `./assistants/V0.0.2/require/REQ-00013/RESULT.md`

## REQ-00017(V0.0.2):`code-plan` 不再为"更新看板"拆派生任务
- **关联点**:本需求 INV-7 沿用;模板产出物**不**是任务,**不**触发 `dashboard-conventions §规则 1` 三同步
- **影响**:FR-4 看板同步**不**追加新行
- **来源**:扫描 `./assistants/V0.0.2/require/REQ-00017/RESULT.md`

## REQ-00019(V0.0.2):`code-plan` BUG 模式同构
- **关联点**:本需求模板填充对 BUG 路径同样生效,输出目录为 `fix/<BUG-NNN>/` 而非 `plan/<REQ>/`
- **影响**:`code-plan` 步骤 22 之后触发模板填充
- **来源**:扫描 `./assistants/V0.0.2/require/REQ-00019/RESULT.md`
