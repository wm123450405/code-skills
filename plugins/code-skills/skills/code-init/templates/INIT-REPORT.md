# 工程初始化报告 — <初始版本号>

> 本报告由 `code-init` 技能生成,作为新成员(包括 AI Agent)快速理解本仓库的入口。
> 最后更新:YYYY-MM-DD HH:mm
> 适用版本:基线版本 `<初始版本号>`(项目当前状态)

## 项目概述
<一两句话说明本仓库做什么,服务什么用户,解决什么问题>

## 技术栈

| 维度 | 选型 |
| --- | --- |
| 语言 | <如 Python 3.11 / TypeScript 5.x / Go 1.22> |
| 框架 | <如 FastAPI / Express / Gin> |
| 数据库 | <如 PostgreSQL 16 / MongoDB 7 / 无> |
| 缓存 | <如 Redis 7 / 无> |
| 消息队列 | <如 RabbitMQ / 无> |
| 构建/包管理 | <如 npm / pnpm / poetry / go mod> |
| 测试框架 | <如 pytest / jest / go test> |
| CI/CD | <如 GitHub Actions / GitLab CI / 无> |
| 部署形态 | <如 Docker / k8s / bare metal / serverless> |

> 无相应项请写"无",不要留空。

## 目录结构

```
<项目根>/
├── <顶层目录 1>/             <一句话职责>
│   ├── <子目录>/             <一句话职责>
│   └── ...
├── <顶层目录 2>/             <一句话职责>
├── <关键顶层文件>            <一句话作用>
└── ...
```

> 只画到 2-3 层;目录过多时折叠次要目录。

## 核心模块与职责

| 模块 | 路径 | 职责 | 对外暴露的接口 |
| --- | --- | --- | --- |
| <模块名> | <如 src/auth/> | <一句话> | <如 login()/verify_token() / POST /api/v1/auth/login> |
| ... | ... | ... | ... |

## 入口与主流程

### 主入口
- 文件:`<如 src/main.py / cmd/server/main.go / src/index.ts>`
- 启动方式:`<如 python src/main.py / go run cmd/server/main.go / npm start>`

### 主流程链路
1. <步骤 1:启动时初始化什么,如加载配置、建立 DB 连接>
2. <步骤 2:注册路由/中间件>
3. <步骤 3:监听端口/等待请求>
4. <步骤 4:处理单个请求的路径:路由 → 控制器 → 服务 → 数据访问>

## 外部接口

### HTTP API(若有)

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | /api/v1/... | ... |
| POST | /api/v1/... | ... |
| ... | ... | ... |

### CLI 命令(若有)

| 命令 | 说明 |
| --- | --- |
| `<如 ./bin/migrate>` | ... |
| ... | ... |

### SDK / 库导出(若是库项目)

| 导出名 | 类型 | 说明 |
| --- | --- | --- |
| ... | ... | ... |

## 数据模型

> 仅在项目使用结构化存储时填写。

| 实体 | 主要字段 | 关系 | 存储位置 |
| --- | --- | --- | --- |
| <如 User> | id, name, email, created_at | 1:N → Order | PostgreSQL `users` 表 |
| ... | ... | ... | ... |

### Schema 文件
- `<如 prisma/schema.prisma / models.py / migrations/...>`

## 构建与运行

### 构建
\```
<构建命令,例如 npm run build / go build -o bin/server / poetry build>
\```

### 启动
\```
<启动命令,例如 npm start / go run cmd/server/main.go>
\```

### 配置
- 配置文件位置:`<如 config/local.yaml / .env>`
- 关键环境变量:`<如 DATABASE_URL / JWT_SECRET / PORT>`

## 测试情况

| 维度 | 现状 |
| --- | --- |
| 是否有测试 | 是 / 否 / 部分模块有 |
| 测试框架 | <如 pytest / jest> |
| 覆盖率 | <如约 60% / 未配置> |
| 测试组织 | <如 tests/ 目录,与 src/ 平级> |
| CI 集成 | <如 GitHub Actions 自动跑 / 未集成> |

## 可复用资产

> 列出值得未来新功能复用的工具/类/函数。

| 资产 | 位置 | 用途 |
| --- | --- | --- |
| <如 Logger> | <src/utils/logger.ts> | <统一日志格式> |
| <如 数据库连接池> | <src/db/pool.py> | <复用连接池> |
| ... | ... | ... |

## 已知问题/技术债

> 有则记,无则省略。

- <如:src/legacy/ 下仍是 jQuery + 回调风格,未迁移到当前框架>
- <如:测试覆盖率仅 30%,核心交易模块无单测>
- <如:多处硬编码魔法数字,未提取为常量>
- ...

## 现有功能需求清单

> 详细的"现有功能"需求见 `./assistants/<初始版本号>/require/EXISTING-NNN/RESULT.md`。
> 本节只列索引。

| 需求编码 | 标题 | 关键路径 | 需求文档 |
| --- | --- | --- | --- |
| EXISTING-001 | <一句话> | <如 src/auth/> | [RESULT.md](require/EXISTING-001/RESULT.md) |
| EXISTING-002 | <一句话> | <如 src/orders/> | [RESULT.md](require/EXISTING-002/RESULT.md) |
| ... | ... | ... | ... |

## 报告元信息

| 字段 | 值 |
| --- | --- |
| 生成工具 | `code-init` |
| 生成时间 | YYYY-MM-DD HH:mm |
| 适用版本 | `<初始版本号>` |
| 覆盖的源文件数 | <数字> |
| 现有功能数 | <数字> |
| 项目类型 | <如 Node.js 后端 / Python CLI / 静态站点> |
| 总体规模 | <如 约 5000 行代码 / 12 个模块> |
