# 升级部署手册 — 从 <源版本> 升级到 <本版本号>

> ⚠ **本手册为通用升级部署骨架**,由 `code-publish` 技能从 `<本仓库>/skills/code-publish/templates/UPDATE.md` 复制生成(**仅当本版本非基线**)。
>
> **请先手动补全所有 `<placeholder>`(除 `<本版本号>` / `<源版本>` 外),再按本手册的步骤执行升级。**
>
> 本手册**默认提供"最常见升级方式"的占位示例**(原地升级 + tar.gz 包替换 + MySQL 数据库);若你使用蓝绿 / 灰度 / 容器化等其他升级方式,请按需调整各章节示例。
>
> **重要:升级前请务必完成第 8 节"回滚方案"的全部准备**(备份 / 回滚脚本 / 决策点);**任何升级都不是"不可逆"的**。

---

## 1. 概述

- **源版本**:<源版本>(由 `code-publish` 自动填充 — 即上一版本号)
- **目标版本**:<本版本号>(由 `code-publish` 自动填充)
- **升级方式**:<原地 / 蓝绿 / 灰度>
- **升级窗口**:<YYYY-MM-DD HH:mm 至 YYYY-MM-DD HH:mm,预计持续 N 分钟>
- **发布者**:<执行升级的人员>

> **升级方式选择指引**(若你还不确定选哪种):
> - **原地升级**:停服 → 替换 → 重启(简单,适合停服窗口可接受的小型服务)
> - **蓝绿部署**:部署新版本到"绿"环境 → 切换流量 → 旧版本保留为"蓝"以备回滚(零停机,需 2 倍资源)
> - **灰度发布**:先发布到 5-10% 流量 → 观察 → 逐步扩大(降低风险,需负载均衡支持流量切分)

---

## 2. 打包

> 升级的打包方式通常**沿用首次部署时的选择**(与 DEPLOY.md §2 一致);但若新版本引入新的构建产物格式,可能需要调整。

### 2.1 软件包方式(默认)

```bash
# 默认示例:tar.gz 打包(与 DEPLOY.md §2.1 一致)
# <source_dir> = 编译后或构建后的目录(例如:dist/ / build/ / target/)
# <output> = 输出的压缩包路径(例如:myapp-v0.0.2.tar.gz,**注意版本号与源版本不同**)

tar -czf <output>.tar.gz <source_dir>

# 校验(强烈建议)
sha256sum <output>.tar.gz > <output>.tar.gz.sha256
```

### 2.2 目录方式

```bash
# 默认示例:rsync 同步(与 DEPLOY.md §2.2 一致)
rsync -avz --delete <source_dir>/ <user>@<server>:/path/to/dest/
```

### 2.3 镜像方式

```bash
# 默认示例:Docker 镜像
# **注意镜像 tag 必须与源版本不同**(避免覆盖源版本镜像)
docker build -t <image_name>:<version> .
docker save -o <output>.tar <image_name>:<version>
```

---

## 3. 获取成果物

<列出本版本的发布物,与源版本对比;示例:>

```
dist/
├── myapp-v0.0.1.tar.gz (源版本,保留)
├── myapp-v0.0.1.tar.gz.sha256
├── myapp-v0.0.2.tar.gz (本版本,新)
├── myapp-v0.0.2.tar.gz.sha256
├── upgrade-db.sql (数据库升级脚本,**新**)
├── rollback-db.sql (数据库回滚脚本,**新 — 必须有**)
└── release-notes.md (本次变更说明)
```

- **主成果物**:<新版本文件名,如 myapp-v0.0.2.tar.gz>
- **数据库升级脚本**:`<upgrade-db.sql>(必备;若新版本无 DB 变更,标注"无")
- **数据库回滚脚本**:`<rollback-db.sql>(必备;详 §8)
- **校验文件**:<新版本 sha256>
- **保留源版本成果物**:升级成功后**不要立即删除**源版本的发布物,至少保留到下次发版后

---

## 4. 上传服务器(可选)

> 若打包方式已是 2.3 镜像方式且直接在目标服务器上 `docker load`,可跳过本节。

```bash
# 默认示例:scp 上传
# **注意:不要覆盖源版本的文件**;建议上传到独立的升级目录

scp <output>.tar.gz <user>@<server>:/path/to/upgrade/
scp <output>.tar.gz.sha256 <user>@<server>:/path/to/upgrade/
scp <upgrade-db.sql> <user>@<server>:/path/to/upgrade/
scp <rollback-db.sql> <user>@<server>:/path/to/upgrade/

# 验证上传完整性
ssh <user>@<server> "cd /path/to/upgrade/ && sha256sum -c <output>.tar.gz.sha256"
```

**建议的目录结构**(避免与生产目录冲突):

```
/opt/
├── myapp/ # 当前生产目录(运行源版本)
│ ├── bin/myapp
│ ├── config/config.yaml
│ └── ...
├── releases/ # 历史发布物归档
│ ├── myapp-v0.0.1/
│ └── ...
└── upgrade/ # 升级专用目录(本次升级的临时文件)
 ├── myapp-v0.0.2.tar.gz
 ├── myapp-v0.0.2.tar.gz.sha256
 ├── upgrade-db.sql
 └── rollback-db.sql
```

---

## 5. 初始化系统(升级)

> **核心原则:升级 = 数据迁移 + 进程替换**;配置变更与 DB 升级是**最容易出错**的两步。

### 5.1 环境变更(若新版本引入新运行时依赖)

> 若新版本**不引入**新依赖,可跳过本节。

<若新版本需要新的运行时,例如:>

- **新增运行时**:<如 Java 17 → Java 21 / Python 3.10 → 3.11 / Node 18 → 20>
- **新增系统包**:<如新增 imagemagick / ffmpeg / ...>

**安装命令**(参考 DEPLOY.md §5.1):

```bash
# 升级运行时示例(若新版本需要)
sudo apt update && sudo apt install -y <new-runtime-package>
```

### 5.2 数据库**升级**脚本

> 升级数据库**前必做**:在源版本仍在运行时**导出全库备份**(详 §8 回滚方案)。
>
> 升级数据库**前必读**:仔细 review `<upgrade-db.sql>` 内容,确保每条 DDL/DML 与新版本代码兼容。

```bash
# 默认示例:MySQL 数据库升级

# 1. (升级前)导出全库备份
mysqldump -u<user> -p<passwd> --single-transaction --routines <dbname> > /opt/upgrade/pre-upgrade-backup-$(date +%Y%m%d%H%M%S).sql

# 2. 应用升级脚本
mysql -u<user> -p<passwd> <dbname> < <upgrade-db.sql>

# 3. 验证表结构
mysql -u<user> -p<passwd> -e "USE <dbname>; SHOW TABLES;" | head
mysql -u<user> -p<passwd> -e "USE <dbname>; SELECT * FROM schema_migrations ORDER BY version DESC LIMIT 5;" # 若用 Flyway / Liquibase
```

**说明**:
- `<upgrade-db.sql>` 应**只包含增量变更**(新增表 / 新增列 / 数据迁移);**不要**包含 DROP 之类不可逆操作
- 若使用 Flyway / Liquibase 等迁移工具,直接用工具升级即可
- 升级脚本的编写规范:每个 DDL 操作前加注释说明"为什么改 / 从哪个版本改"

### 5.3 数据库迁移数据(若有)

> 若新版本需要**将源版本的数据迁移到新结构**(如:`users.full_name` 拆为 `users.first_name` + `users.last_name`),详 upgrade-db.sql 中的 `INSERT ... SELECT ...` 语句。

```sql
-- 默认示例:数据迁移 SQL 片段
-- (以下内容应已在 upgrade-db.sql 中)

UPDATE users
SET first_name = SUBSTRING_INDEX(full_name, ' ', 1),
 last_name = SUBSTRING_INDEX(full_name, ' ', -1)
WHERE full_name IS NOT NULL;
```

**验证**:

```sql
-- 验证迁移结果
SELECT COUNT(*) FROM users WHERE first_name IS NULL AND full_name IS NOT NULL;
-- 应返回 0(所有数据已迁移)
```

### 5.4 配置变更(diff 形式)

> **核心**:升级时**不**重写整个配置文件;只 apply **diff**。
>
> 配置变更的"diff 模板"应随发布物一并提供,或在 `release-notes.md` 中详细说明。

**变更类型**(可能同时存在):

- **新增配置项**:新功能所需的新参数(默认值;若可平滑启用,无需修改)
- **废弃配置项**:旧参数(代码仍兼容,只是日志告警;后续版本删除)
- **删除配置项**:**极少见**;若发生,需手动迁移
- **默认值变更**:某参数默认值改了(影响行为)

**配置 diff 示例**(从源版本到本版本):

```diff
# /etc/myapp/config.yaml
 server:
 port: 8080
+ max_connections: 1000 # 新增(默认值 1000)
 logging:
 level: INFO
- enable_legacy_logging: false # 废弃(代码兼容,日志告警)
 db:
 url: jdbc:mysql://localhost:3306/myapp_prod
+ connection_timeout: 30s # 新增(默认 30s)
```

**应用方式**:

```bash
# 默认示例:用 sed / 手工编辑
ssh <user>@<server> "sudo vim /etc/myapp/config.yaml"

# 或(若配置由配置中心管理):
# curl -X POST <config-center-api>/apps/myapp-v0.0.2/configs -d @config-diff.yaml
```

**注意**:
- 升级前**先备份源版本配置**:`sudo cp /etc/myapp/config.yaml /opt/upgrade/config.yaml.bak`
- 配置变更后**不要重启服务**(等 §6 一起重启)

---

## 6. 重新启动软件

> 升级时**通常需要重启服务**;具体步骤与 DEPLOY.md §6 类似,但**先停服,再替换文件,再启动**。

```bash
# 默认示例:systemd 重启(原地升级)

# 1. 停止当前服务(源版本)
sudo systemctl stop myapp

# 2. 备份源版本二进制(以备回滚)
sudo cp /opt/myapp/bin/myapp /opt/upgrade/myapp.v0.0.1.bak

# 3. 替换为新版本二进制
sudo cp /path/to/upgrade/<output>.tar.gz /tmp/
cd /tmp && tar -xzf <output>.tar.gz
sudo rsync -av --delete <extracted-dir>/ /opt/myapp/ # 注意: --delete 会删除旧文件;先确认无遗留

# 4. 启动新版本
sudo systemctl start myapp

# 5. 查看状态
sudo systemctl status myapp
```

**其他升级方式**(若使用):

- **蓝绿部署**:不停止蓝环境,启动绿环境 → 切流量(负载均衡)→ 验证 → 停止蓝环境
- **灰度发布**:通过负载均衡 / 服务网格(istio)将 5% 流量切到新版本 → 观察 → 逐步扩大
- **Docker**:滚动更新(`docker service update` 或 Kubernetes 的 `kubectl rollout`)

---

## 7. 验证清单

升级完成后,**逐项勾选**以下清单;所有项必须为 `[x]` 才能视为升级成功。

- [ ] **服务进程已切换**:用 `ps` / `systemctl status` 确认运行的是新版本二进制(版本号 / git commit)
- [ ] **数据库升级完成**:`<upgrade-db.sql>` 已成功应用;`schema_migrations` 表(若用)显示新版本
- [ ] **数据库数据迁移完成**(若 §5.3):所有旧数据已迁移到新结构;`SELECT COUNT(*)` 验证无遗漏
- [ ] **配置变更已应用**:`config.yaml` 含本版本的 diff(新增/废弃/默认值变更);旧配置备份已存在
- [ ] **服务启动正常**:`systemctl status myapp` 显示 `active (running)`,无 ERROR
- [ ] **关键 API 可访问**:`curl http://<server>:<port>/health` 返回 `200 OK`(且 version 字段 = 本版本号)
- [ ] **关键页面可访问**:浏览器打开主页,无 5xx 错误
- [ ] **旧版本功能仍正常**:核心业务流程冒烟测试通过(如:登录 / 创建订单 / 搜索)
- [ ] **新版本功能可见**:新功能菜单 / 按钮 / 接口可访问
- [ ] **数据库无连接异常**:服务日志中无 "Connection refused" / "DB timeout" / "Migration failed" 等
- [ ] **日志路径可写**:`/var/log/myapp/` 目录可写
- [ ] **磁盘空间充足**:`df -h` 检查 / /var / 数据库目录,余量 > 20%
- [ ] **回滚方案仍可执行**(详 §8):回滚脚本 / 备份 / 决策点已就绪
- [ ] **日志无 ERROR**:`journalctl -u myapp --since "5 minutes ago" | grep ERROR` 为空
- [ ] **(若灰度)流量比例已记录**:开始时 X% → 1h 后 Y% → ...

---

## 8. 回滚方案(新增)

> **核心原则:任何升级都必须可回滚**;本节是 DEPLOY.md 没有的**专属**内容。
>
> **建议在升级开始前完成本节的所有准备**;否则可能面临"升级失败但无法回滚"的窘境。

### 8.1 回滚步骤

> 回滚的目标:将服务**从本版本切回源版本**,并尽量保留数据(若 §5.3 数据迁移不可逆,可能需要"接受数据丢失"的代价)。

**默认步骤(原地升级 → 原地回滚)**:

```bash
# 1. 停止当前服务(本版本)
sudo systemctl stop myapp

# 2. 恢复源版本二进制(用 §6 步骤 2 的备份)
sudo cp /opt/upgrade/myapp.v0.0.1.bak /opt/myapp/bin/myapp

# 3. 恢复源版本配置
sudo cp /opt/upgrade/config.yaml.bak /etc/myapp/config.yaml

# 4. (若 §5.2/5.3 不可逆)**决策点:数据是否回滚**
# - 情况 A:DB 变更**可逆**(如:只新增表/列)→ 跳过 DB 回滚
# - 情况 B:DB 变更**不可逆**(如:DROP COLUMN)→ 执行 DB 回滚(详 §8.2)

# 5. 启动源版本
sudo systemctl start myapp

# 6. 验证源版本正常工作(参考 §7 验证清单)
```

**蓝绿/灰度回滚**(若使用):

- **蓝绿**:切流量回蓝环境(秒级回滚;绿环境保留为"备份")
- **灰度**:将 100% 流量切回源版本(配置负载均衡)

### 8.2 数据回滚(若有)

> **仅当 §5.2 / §5.3 的 DB 变更不可逆时执行**;否则跳过(节省时间)。

```bash
# 默认示例:回滚 DB 到升级前的状态
mysql -u<user> -p<passwd> <dbname> < <rollback-db.sql>

# 验证
mysql -u<user> -p<passwd> -e "USE <dbname>; SELECT * FROM schema_migrations ORDER BY version DESC LIMIT 5;"
# 应显示源版本的最后一条 migration
```

**`<rollback-db.sql>` 应在升级前准备好**,内容通常包括:
- DROP 新增的表 / 列
- 数据回滚(若新结构与旧结构不完全兼容,如拆分字段)
- 重置 schema_migrations 表

### 8.3 触发回滚的条件

> **决策矩阵**:出现以下任一情况,应**立即**触发回滚,**不**等待"修复":

- [ ] 服务**无法启动**(`systemctl status myapp` 显示 `failed`),且 5 分钟内重启 3 次都失败
- [ ] 关键 API **返回 5xx** 超过 1 分钟(且确认非源版本遗留问题)
- [ ] **数据库迁移失败**(§5.2 / §5.3 报错)
- [ ] **新功能**上线后**关键业务数据丢失 / 错乱**
- [ ] **安全漏洞**:新版本引入安全漏洞,且无快速修复
- [ ] **监控告警**:CPU / 内存 / 错误率 / 延迟等核心指标**超过阈值**且无法快速定位
- [ ] **用户报告**:短时间内大量用户反馈严重问题(登录失败 / 数据看不到 / 支付失败等)

**回滚决策人**:<指定负责人,如 SRE oncall / Tech Lead / 发布者本人>

**回滚决策 SLA**:从"发现严重问题"到"启动回滚"应**不超过 15 分钟**。

### 8.4 回滚后的动作

- [ ] 立即通知相关方(内部 IM / 邮件群)
- [ ] 在**下一次发版**前,修复导致回滚的根因(代码 bug / 配置错 / DB 脚本错 / ...)
- [ ] 保留回滚时产生的所有日志与 artifacts,以便事后分析
- [ ] 更新本手册(若回滚流程本身有缺陷)
