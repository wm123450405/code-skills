# 模块详细化 — REQ-00014

更新时间:2026-06-05 13:20
版本:V0.0.2
需求:REQ-00014(优化技能 `/code-plan` 的任务拆分维度)

## 模块:M-1 `code-plan/SKILL.md` §10A 修改(对应概要设计 §4.1)

### 路径
- 文件:`plugins/code-skills/skills/code-plan/SKILL.md`
- 修改区段:**§10A 任务拆分**(当前 L195-199,共 4 行)
- 修改量:L195-199 **完全替换**(Q-D1 锁定 A)为 ~25 行新内容

### 关键"组件"(SKILL.md 工作流视角)

| 组件 | 形式 | 职责 | 章节位置 |
| --- | --- | --- | --- |
| 原 4 行"任务拆分原则" | 文字 | 分层拆分(底层/核心/集成/测试/文档) | L195-199(**完全替换**) |
| 新"按功能点拆分" 子节 | 文字 | 按用户可见能力拆,1 任务 = 完整一套 | (新增) |
| 新"架构任务作为首个" 子节 | 文字 | 3 触发条件 + 任务边界 | (新增) |
| 新"生效范围" 子节 | 文字 | 仅未来需求生效,既有 PLANS 不追溯 | (新增) |
| 任务类型 | 文字 | 6 种(沿用既有) | 沿用 |
| 任务编号 | 文字 | `TASK-(REQ|BUG)-NNNNN-NNNNN`(沿用既有) | 沿用 |
| 任务双状态 | 文字 | 开发 + 测试(沿用既有) | 沿用 |
| 任务触发/来源 | 文字 | 13 个枚举值(沿用既有) | 沿用 |

### 关键"函数"(语义视角)

| "函数" | 触发时机 | 职责 |
| --- | --- | --- |
| `version_detect()` | 步骤 0 | (沿用既有)读 `.current-version` |
| `load_requirement(requirement_id)` | 步骤 1-2 | (沿用既有)读需求 + 设计 + 规范 |
| `evaluate_architecture_need(requirement)` | 步骤 10A.0(**新增**) | 评估需求是否满足架构任务 3 触发条件 |
| `identify_feature_points(requirement)` | 步骤 10A.1(**新增**) | 识别功能点(用户可见能力) |
| `split_task_per_feature_point(fp)` | 步骤 10A.2(**新增**) | 1 个功能点 = 1 个完整一套 = 展示 + 逻辑 + 说明 |
| `assign_task_metadata(task)` | 步骤 10A.3(沿用) | 任务编号 + 双状态 + 触发/来源 |
| `skill_invoke("code-design"/"code-it"/...)` | 步骤 11A+(沿用) | 沿用既有 |

### 关键"调用顺序"(对应 `code-plan` 步骤 10A)

```
[code-plan 步骤 10A 任务拆分](优化后)
  ↓
[10A.0 evaluate_architecture_need(requirement)]
  ├─ 满足触发 1(扩展性 + 复杂度)→ 架构任务=00001
  ├─ 满足触发 2(未来不同实现方式)→ 架构任务=00001
  ├─ 满足触发 3(对接不同三方组件)→ 架构任务=00001
  └─ 都不满足 → 跳过架构任务
  ↓
[10A.1 identify_feature_points(requirement)]
  └─ 输出 feature_points: list[FeaturePoint]
  ↓
[10A.2 for each fp in feature_points]
  ├─ split_task_per_feature_point(fp) → task
  │   ├─ 展示效果(ui/display/screenshot)
  │   ├─ 功能逻辑(algorithm/interface/data)
  │   └─ 使用说明(readme/docs)
  └─ append task to tasks
  ↓
[10A.3 for each task in tasks]
  └─ assign_task_metadata(task)
       ├─ id: TASK-{requirement}-{counter:05d}
       ├─ dev_status: 待开始
       ├─ test_status: 未编写 or 不适用
       └─ source: 需求新增
  ↓
[返回 tasks 列表] → [code-plan 步骤 11A+ 继续]
```

### 内部状态
- **不维护内存状态**:`code-plan` 是无状态工作流定义(沿用既有)
- **不写代码 / 配置 / 数据库**
- **不持有任何凭据**

### 并发模型
- **N/A**(无运行时)

### 资源管理
- **N/A**(无连接 / 锁 / 缓存)

### 错误处理范式
- **不修改既有错误处理**:沿用 `code-plan` 既有的"检测 → 记录 → 跳过"模式
- **新增错误**:触发条件 1-3 评估失败时,自动降级到"不插入架构任务"(简单需求路径)

### 日志埋点
- **N/A**:本需求**不**改日志

### 依据规范
- `skill-conventions §规则 1`:**不**触达(沿用既有 frontmatter)
- `module-conventions §规则 1`:**不**触达(无资源新增)
- `dashboard-conventions §规则 1`:**不**触发(本优化**不**改字段)
- `encoding-conventions §规则 1-4`:**不**触达(任务编号格式沿用既有)

## 自检 — 与概要设计 §7 模块划分的对应

| 概要设计章节 | 本设计章节 | 状态 |
| --- | --- | --- |
| §7.1 模块总览 | (沿用) | ✅ |
| §7.2 M-1 详细 | 本文档 | ✅ |
| §7.3 M-2 详细 | **无**(本需求不产生新模块) | ✅ |

## 横向协同(其他 12 个 `code-*` 技能)

| 技能 | 是否受影响 | 理由 |
| --- | --- | --- |
| `code-init` | ❌ | 不依赖任务拆分维度 |
| `code-version` | ❌ | 不依赖 |
| `code-rule` | ❌ | 不依赖 |
| `code-require` | ❌ | 产出"需求分析",**不**读任务拆分 |
| `code-design` | ❌ | 产出"概要设计",**不**读任务拆分 |
| `code-plan`(自身) | ✅ **本需求唯一修改目标** | 修改 §10A 任务拆分原则 |
| `code-it` | ❌ | 读任务编号/双状态/触发来源(沿用),**不**读拆分原则 |
| `code-unit` | ❌ | 同上 |
| `code-fix` | ❌ | 不依赖 |
| `code-review` | ❌ | 读任务字段(沿用),**不**读拆分原则 |
| `code-dashboard` | ❌ | 读任务清单(沿用),**不**读拆分原则 |
| `code-publish` | ❌ | 读任务清单(沿用),**不**读拆分原则 |
| `code-auto` | ❌ | 读任务清单(沿用),**不**读拆分原则 |

**结论**:**1 个**模块被修改(M-1),**0 个**新增,**0 个**删除。
