# 通用流程细节 — code-design

> 本文件为 code-design 技能提供语言无关的通用流程细节。
> 在技能启动时始终加载本文件。

## §1 步骤 0a — 拉取最新代码

1. 探测 `git` 可用性 → `Bash: git --version`,失败 → 中断
2. 执行 `Bash: git pull`
3. 拉取失败分类处理:
   - 冲突 → 打印冲突文件,提示手动解决
   - 网络 → 打印 remote-url,提示检查网络/代理
   - 凭据 → 提示检查 SSH key / token
   - 其他 → 透传 stderr,中断
4. 拉取成功后立即 `Read .current-version`

## §2 步骤 0b.0 — 调用上下文检测

- 检测机制:`Bash: test -f ./assistants/.code-auto-running && echo "DETECTED" || echo "NOT_DETECTED"`
- 24 小时超时:若文件存在但距启动 > 24h → 视为脏数据
- 决策:
  - 检测到 code-auto → 跳过 AskUserQuestion,采纳默认值
  - 未检测到 → 正常进入步骤 0b

## §3 步骤 0b — 设计目标确认

### 扩展性触发判定
```
触发扩展性 = 满足任一:
1. 需求"待评估三方依赖"清单非空
2. 模块拆分预评估涉及模块数 ≥ 3
3. 上游需求 FR 含"多实现/抽象层/可替换/多套实现"语义
```

### 自适应问题数
- 小需求(1 任务,无扩展性触发):0 个 AskUserQuestion
- 小需求(1 任务,有扩展性触发):1 个 AskUserQuestion
- 中等需求(2-5 任务):1 个 AskUserQuestion
- 大需求(≥6 任务):2 个 AskUserQuestion

### 屏显模板
```
=== code-design 设计目标确认 ===
整体设计目标:<--minimal/--extensible/--balanced>
维度优先级:
功能性:<高/中/低>
已回写至 design/<REQ>/RESULT.md "## 设计目标" 小节
```

## §4 过程文档自适应判定

### 判定准则
| 过程文档 | 判定准则 |
| --- | --- |
| materials-index.md | 始终生成 |
| design-notes.md | 始终生成 |
| module-breakdown.md | 模块数 ≥ 2 → 生成 |
| dependencies.md | 依赖其他模块/服务 ≥ 1 → 生成 |
| related-designs.md | Glob 发现 ≥ 1 关联设计 → 生成 |
| rule-compliance.md | rules/ 存在且有内容 → 生成 |
| clarifications.md | 本轮有用户问路 → 生成 |

## §5 修改文件定位的语义化约定

- **禁止**使用行号作为唯一定位方式
- **应当**使用结构化语义定位:段落/章节 / 类型/类/接口 / 方法/成员 / 函数 / 分支/循环/块 / 配置项/字段
- 多匹配消歧:附加"上下文锚点"

## §6 步骤 5 — 通用项目探索

### 语言检测
> 详见 references/<语言>.md §1

检测算法:
1. Glob 模块根目录,查找描述文件
2. 按优先级匹配:package.json → pyproject.toml → Cargo.toml → go.mod → pom.xml → build.gradle
3. 多模块时对每个模块独立检测
4. 无匹配 → "unknown",兜底使用 common.md

### 通用子步骤(语言无关)
1. 项目类型识别
2. 目录结构
3. 入口与主流程
4. 已有模块识别
5. 已有接口识别
6. 已有数据模型
7. 已有第三方依赖
8. 编码与构建约定
9. 可复用资产

## §7 步骤 7A-15A — 首次设计流程

1. 步骤 7A:架构方案构思(design-notes.md)
2. 步骤 8A:澄清冲突与不确定项(AskUserQuestion)
3. 步骤 9A:模块拆分(module-breakdown.md,5 列)
4. 步骤 10A:接口与数据结构(接口概要 + 数据结构)
5. 步骤 11A:三方依赖评估(dependencies.md)
6. 步骤 12A:检索关联概要设计
7. 步骤 13A:撰写 RESULT.md(按 templates/design.md)
8. 步骤 14A:同步版本看板
9. 步骤 15A:完善过程文档与汇报

## §8 步骤 7B-10B — 增量更新流程

1. 识别变更源:需求侧/代码侧/规范侧/设计侧
2. 局部更新 RESULT.md(不重写稳定章节)
3. 重做规范自检
4. 同步版本看板

## §9 步骤 N — 末尾兜底提交

1. `Bash: git status --porcelain`
2. 无变更 → 跳过
3. `Bash: git add <所有 dirty 文件>`
4. 生成 commit message 预览
5. AskUserQuestion 3 选 1(确认/修改/取消)
6. `Bash: git commit -m "<message>"`

## §10 过程文档格式

### materials-index.md
```
# 材料登记 — <需求编码>
更新时间:YYYY-MM-DD HH:mm
版本:<版本号>

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |

## 上游需求
- 来源:./assistants/<版本号>/require/<需求编码>/RESULT.md

## 项目现状(本次扫描)
### 项目类型 / 目录结构 / 已有模块 / 已有接口 / 已有数据模型 / 已有第三方依赖
```

### rule-compliance.md
```
# 规范遵循记录 — <需求编码>
## 1. 本次参考的规范文件
## 2. 规范 vs 现状偏离
## 3. 规范 vs 需求冲突
## 4. 用户授权的偏离
## 5. 规范变更响应
```

## §11 模板填充步骤

### 触发条件
- 用户调 `code-design <REQ> --result <模板文件>` 时触发
- 无参数 / code-auto 上下文 / 模板不存在 / 二进制格式 → 跳过

### 执行流程
1. Read 模板
2. 扫描 `{{...}}` 占位符
3. 从 RESULT.md 提取结构化数据
4. 替换占位符
5. 写出 `<原目录>/DESGIN.<ext>`

### 占位符映射
| 占位符 | 来源 |
| --- | --- |
| `{{设计概述}}` | design/.../RESULT.md §1 |
| `{{模块列表}}` | design/.../RESULT.md §模块拆分 |
| `{{接口列表}}` | design/.../RESULT.md §接口 |
| `{{数据结构}}` | design/.../RESULT.md §数据结构 |

## §12 标题解析工具函数

```ts
function truncateTitle(title: string, maxLen: number = 30): string {
  if ([...title].length <= maxLen) return title
  return [...title].slice(0, maxLen).join('') + '...'
}

function formatReqTitle(reqNum: string, title: string): string {
  return `${reqNum} · ${truncateTitle(title)}`
}
```

## §13 命令行参数解析

### 支持的参数
| 参数 | 性质 | 模板产出物 |
| --- | --- | --- |
| `--result <模板文件>` | 可选 | `DESGIN.<ext>` |

### 边界与异常
- E-1:缺值 → 屏显警告,跳过
- E-2:含通配符 → 屏显警告,跳过
- E-3:路径跳出工作空间 → 屏显警告,跳过
- E-4:code-auto 上下文 → 不传 --result

## §14 通用屏显模板

| 场景 | 格式 |
| --- | --- |
| 启动 | `正在处理: REQ-NNNNN · <需求标题>` |
| 完成 | `完成: REQ-NNNNN · <需求标题>` |
| 中止 | `⛔ code-design 中止: REQ-NNNNN · <需求标题>(<原因>)` |
| 错误 | `✗ 错误: REQ-NNNNN · <需求标题>(<错误信息>)` |

## §15 通用边界与异常处理

| 场景 | 处理 |
| --- | --- |
| 语言检测失败(unknown) | 仅加载 common.md,屏显警告 |
| references 文件缺失 | 屏显警告,使用通用流程 |
| rules/ 目录不存在或为空 | AskUserQuestion 询问是否继续 |
| RESULT.md 已存在 | 进入增量更新分支 |