# 接口详细规格 — REQ-00007

更新时间:2026-06-05 10:05
版本:V0.0.2

## 接口 1:`code-auto` 技能对外接口(Skill 工具触发)

### 形式
Claude Code `Skill` 工具(用户从提示符触发,例如 `/code-auto "<需求内容>"`)

### 路径/签名
```
/code-auto <需求内容>
```
或(多参数拼接):
```
/code-auto arg1 arg2 arg3 ...
```
→ 等价于 `/code-auto "arg1 arg2 arg3 ..."`

### 入参

| 参数 | 类型 | 必填 | 约束 | 缺省行为 |
| --- | --- | --- | --- | --- |
| `<需求内容>` | string | 是 | 自然语言,无长度上限(由 Claude Code 模型层管理) | 无参数 → 提示用法示例 + 退出 ≠ 0 |

### 出参

#### 屏幕(stdout)输出
**3 段式**:
1. **进度日志**(每步一行,沿用 NFR-10):
   ```
   [code-auto] 步骤 0a:git pull(沿用 REQ-00005 模式)
   [code-auto] 步骤 0:读 .current-version → V0.0.2
   [code-auto] 步骤 1/6:code-require "<需求内容>"
   [code-auto]   → 产出 REQ-00008
   ...
   ```
2. **完成/中断/中止报告**(终态):
   - ✓ 完成 / ⏹ 用户中止 / ✗ 子技能异常(详见 §1.3)
3. **后续建议**(完成时):
   ```
   后续建议:
     > 执行 /code-dashboard 查看完整状态
     > 执行 /code-publish 生成发布手册
   ```

#### 磁盘输出(完成时)
- **路径**:`./assistants/<版本号>/require/REQ-NNNNN/auto-report.md`
- **格式**:Markdown
- **覆盖语义**:同名文件**覆盖**(不追加)

### 错误码(退出码)

| 退出码 | 含义 | 触发场景 |
| --- | --- | --- |
| 0 | 正常完成 | 全部步骤通过 + 必须改列表空 |
| 1 | 子技能异常 | 子技能退出码 ≠ 0(具体子技能名 + 任务编码在报告中) |
| 130 | 用户中止 | 收到 SIGINT (Ctrl+C) |
| 2 | 步骤 0a 失败 | `git pull` 冲突 / 网络 / 凭据(沿用 REQ-00005 错误码) |
| 3 | 步骤 0 失败 | 无 `.current-version` |
| 4 | 缺参数 | 无 `<需求内容>` 参数 |

### 示例

#### 正常调用
```
$ /code-auto "添加用户登录功能,支持手机号+密码"
[code-auto] 步骤 0a:git pull
[code-auto] 步骤 0:读 .current-version → V0.0.2
[code-auto] 步骤 1/6:code-require "添加用户登录功能,支持手机号+密码"
[code-auto]   → 产出 REQ-00008
...
[code-auto] 步骤 6/6:code-review REQ-00008
[code-auto]   → 第 2 轮:无"必须改" → 结束
✓ code-auto 完成
...
退出码:0
```

#### 子技能失败
```
[code-auto] 步骤 4/6:code-it TASK-REQ-00008-003
✗ code-it 失败(退出码 1)
  stderr: <子技能 stderr>
✗ code-auto 中断(子技能异常)
...
退出码:1
```

#### 用户中止
```
[code-auto] 步骤 4/6:code-unit TASK-REQ-00008-005
⏹ code-auto 用户中止(Ctrl+C)
...
退出码:130
```

### 版本策略
- `code-auto` v1(本需求首次实现)
- 未来 v2 改进空间:增量恢复(留作 follow-up,Q-11 锁定)
- **不**做向后兼容测试(无 v0 存在)

### 兼容策略
- 与 6 个子技能的 SKILL.md frontmatter 字节级兼容(子技能不修改)
- 与 `.current-version` 机制兼容(沿用 `code-version` 既有约定)
- 与 `marketplace.json` `plugins[].skills` 数组追加 1 项兼容(`marketplace-protocol §规则 1`)

### 依据规范
- `skill-conventions.md §规则 1`(frontmatter 必含 name+description)
- `marketplace-protocol.md §规则 1`(skills 数组元素以 `./` 开头)

---

## 接口 2:子技能调用契约(`code-auto` → 6 个子技能)

### 形式
Claude Code `Skill` 工具

### 调用表(7 步)

| 步骤 | 子技能 | 输入 | 期望产物 | 失败处理 |
| --- | --- | --- | --- | --- |
| 1 | `code-require` | `"<需求内容>"` | `require/REQ-NNNNN/RESULT.md` | 中断 + 报告 |
| 2 | `code-design` | `REQ-NNNNN` | `design/REQ-NNNNN/RESULT.md` | 中断 + 报告 |
| 3 | `code-plan` | `REQ-NNNNN` | `plan/REQ-NNNNN/{RESULT,PLAN}.md` | 中断 + 报告 |
| 4 | `code-it` | `TASK-REQ-NNNNN-NNNNN` 或 `REQ-NNNNN-NNNNN` | `code/TASK-.../RESULT.md` | 中断 + 报告 |
| 4 | `code-unit` | 同上(条件触发) | `test/TASK-.../RESULT.md` | 中断 + 报告 |
| 5 | `code-review` | `REQ-NNNNN` | `review/REQ-NNNNN/REVIEW-REPORT.md` | 中断 + 报告 |
| 6 | `code-it` | 派生任务编码 | `code/.../RESULT.md` | 中断 + 报告 |
| 6 | `code-unit` | 派生任务编码(条件触发) | `test/.../RESULT.md` | 中断 + 报告 |

### 附加约束(通过 prompt 注入到子技能)
```
在执行本任务时,若 Claude Code 触发 `AskUserQuestion` 询问用户,
**总选第一项 / 标注 (推荐) 的项**;不向用户提问
```
(此约束**不**作为 `Skill` 工具的"参数"传递,而是作为 `code-auto` 自身 prompt 的一部分;详见概要设计 D-2)

### 错误码
- 子技能退出码 ≠ 0 → `code-auto` 中断 + 报告(详见接口 1)
- **不**透传子技能具体退出码;统一映射为 `code-auto` 退出码 1

### 版本策略
- 6 个子技能 SKILL.md **零修改**(FR-8.AC-8.1)
- 子技能未来的 v2 升级,由各自的 `code-design` / `code-plan` 独立管理

### 兼容策略
- **不**向子技能传任何特殊参数(无显式契约,D-5 选定 A)
- 子技能**不感知**被 `code-auto` 调 vs 被用户直接调(行为一致)

### 依据规范
- `module-conventions.md §规则 1`(子技能零修改)

---

## 接口 3:数据源契约(`code-auto` 读 3 类文件)

### 形式
Claude Code `Read` 工具

### 3.1 读 `.current-version`

| 属性 | 值 |
| --- | --- |
| 路径 | `./assistants/.current-version` |
| 格式 | 1 行字符串(如 `V0.0.2`) |
| 读取时机 | 步骤 0 |
| 异常处理 | 文件不存在 → 提示调 `code-version` + 退出 3 |

### 3.2 读 `plan/REQ-NNNNN/PLAN.md`

| 属性 | 值 |
| --- | --- |
| 路径 | `./assistants/<版本号>/plan/REQ-NNNNN/PLAN.md` |
| 格式 | Markdown,含 `## 任务总览` 区段 |
| 解析锚点 | `^## 任务总览$`(定位区段)+ `^\| .* \|$`(定位表格行) |
| 提取字段 | 每行第 1 列(任务编码) |
| 任务编码正则 | 新格式:`^TASK-(REQ\|BUG)-\d{5}-\d{5}$`;旧格式:`^(REQ\|BUG)-\d{5}-\d{5}$` |
| 读取时机 | 步骤 4 前置 |
| 异常处理 | 文件不存在或缺区段 → 中断 + 报告(退出码 1) |

### 3.3 读 `review/REQ-NNNNN/REVIEW-REPORT.md`

| 属性 | 值 |
| --- | --- |
| 路径 | `./assistants/<版本号>/review/REQ-NNNNN/REVIEW-REPORT.md` |
| 格式 | Markdown,含 `## 评审发现汇总` 区段 |
| 解析锚点 | `^## 评审发现汇总$`(定位区段)+ `^\| .* \|$`(定位表格行) |
| 提取字段 | 每行的"级别"列 + "任务编码"列 |
| 筛选规则 | `级别` = `必须改` **且** `状态` ≠ `已处理` |
| 读取时机 | 步骤 5/6 循环 |
| 异常处理 | 文件不存在或缺区段 → 中断 + 报告(退出码 1) |

### 依据规范
- `encoding-conventions.md §规则 1-4`(任务编码正则)
- `dashboard-conventions.md §规则 1`(沿用看板解析锚点)

---

## 接口 4:磁盘写入契约(`code-auto` 写 `auto-report.md`)

### 形式
Claude Code `Write` 工具

### 路径
`./assistants/<版本号>/require/REQ-NNNNN/auto-report.md`

### 写入时机
- **写入**:步骤 7 完成分支(成功条件)
- **不写入**:步骤 7 中断/中止分支(避免半成品)

### Schema(标准结构)

```markdown
# auto-report — REQ-NNNNN(<需求标题>)

- 需求编码:REQ-NNNNN
- 所属版本:<版本号>
- code-auto 起始时间:YYYY-MM-DD HH:mm
- code-auto 结束时间:YYYY-MM-DD HH:mm
- 总状态:✓ 完成
- 总子技能调用次数:N

## 执行摘要
| 子技能 | 调用次数 |
| --- | --- |
| code-require | 1 |
| code-design | 1 |
| code-plan | 1 |
| code-it | N1 |
| code-unit | N2 |
| code-review | N3 |

## 最终状态
- REQ-NNNNN 状态:已完成
- 任务清单:TASK-... × N,均已完成
- 缺陷:0
- 派生任务:N,均已完成

## 后续建议
- 执行 /code-dashboard 查看完整状态
- 执行 /code-publish 生成发布手册
```

### 错误处理
- `Write` 工具失败(权限/磁盘满)→ **警告不中断**(D-6 选定 A)
- stderr 警告:`⚠ auto-report.md 写入失败(<原因>),报告仅输出在屏幕`
- 继续退出 0(用户核心需求"看到报告"已满足)

### 版本策略
- v1 schema(本需求首次定义)
- 未来 v2 改进:可加 JSON 副产物(留作 follow-up)

### 兼容策略
- **覆盖语义**:同名文件覆盖(不追加)
- 与 `code-publish` `publish/` 目录的"幂等覆盖"约定一致(NFR-6)

### 依据规范
- NFR-7(完成时写 / 中止时不写)
- NFR-6(覆盖语义与 `code-publish` 一致)

---

## 总结

| 接口 | 形式 | 状态 | 对应任务 | 依据规范 |
| --- | --- | --- | --- | --- |
| 1. `code-auto` 触发 | `Skill` 工具 | 新增 | T-001 | `skill-conventions §规则 1` |
| 2. 子技能调用 | `Skill` 工具 × 6 | 复用(零修改) | T-001 | `module-conventions §规则 1` |
| 3. 数据源读取 | `Read` 工具 × 3 | 复用 | T-001 | `encoding-conventions §规则 1-4` |
| 4. 磁盘写入 | `Write` 工具 | 新增 | T-001(运行时) | NFR-6/7 |
| 5. marketplace.json 修改 | `Edit` 工具 | 修改(1 处) | T-002 | `marketplace-protocol §规则 1` |
| 6. 中英 README 修改 | `Edit` 工具 × 2 | 修改(各 1 处) | T-003 | `doc-conventions §规则 1` |
| 7. 看板同步 | `Edit` 工具 × 5 | 修改 | T-004 | `dashboard-conventions §规则 1` |
