# 治理日志：CloudNative 批

> 执行日期：2026-09-30。范围：`CloudNative/` 域内容操作（合并/拆节/去重/格式治理/隐私脱敏），另涉及域外 2 文件（`SoftwareManual/Git.md` 追加、`Programming/DotNet/Libraries/Aspire.md` 互链、`Frontend/README.md` 引用改指）。未 `git commit`，删除/更名一律 `git rm`/`git mv` 保留历史。
> 原则：不丢信息；内容改动（脱敏/事实修正/删空占位/AI 痕迹重写）均在各文件文首 blockquote 与本日志双重留痕。
> 验收：`fixlinks.py` → `DONE: 0 links fixed`；`checklinks.py` → `all links OK`（exit 0；31 张 orphan 图片为其他域历史存量，与本批无关，未动）。

## T1 Kubernetes 概念文件合并

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 合并 | `Kubernetes/概述.md` + `Kubernetes/Node.md` + `Kubernetes/命令.md` | → `Kubernetes/概述.md`（唯一 H1 `# Kubernetes 概述`；正文 = 原概述全文 + 新增 `## 节点架构`（原 Node.md 的 Work Node/Master Node 组件）+ `## Kubectl`（原 命令.md 的命令表））。`git rm` Node.md、命令.md。原 概述.md 两张空 alt 架构图顺手补 alt（"Kubernetes 集群架构图"/"Kubernetes 架构示意图"）。 |
| 事实修正 | `Node.md` 两处 | ① `Master Node` "实际上就是 `Control Panel`" → `Control Plane`；② `Kubelet` 职责"调度 `Pod`，以及提供接口" → "节点代理：确保容器按 `PodSpec` 运行（调度决策由 `Scheduler` 负责），以及提供接口"。修正后的文件文首 blockquote 留痕。 |
| 事实修正 | `Pod.md` "Service" 节 | "…`Service` 管理 `Pod` 的 `IP`，`Pod` 挂掉 `IP` 也不会变" → "…`Service` 管理 `Pod` 的 `IP`——`Pod` 重建后 `IP` 会变化，稳定访问靠 `Service`"。 |
| 删除 | `Pod.md` 文末待办残句 | "，下周准备继续跟进一下" 删除（前句语义完整保留）。 |

## T2 Kubernetes监控.md 拆节

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 拆出 | `## Git`（提交规范 1 条） | → `SoftwareManual/Git.md` 追加为 `## Git 提交规范` H2（编号列表转标准列表，文末留痕说明迁出来源）。 |
| 拆出 | `## 发布`（发布/部署辨析、数据库变更、A/B 测试、金丝雀、灰度） | → 新建 `CloudNative/CICD/发布策略.md`（唯一 H1 `# 发布策略`，标题层级整体上调一级）。灰度 vs 金丝雀的区分表述与业界常见用法（两者中文语境常同义，均指按比例放量）冲突，按任务要求加 `> [!question] 待事实核查` callout，原文未擅改。 |
| 拆出 | `## 网络`（CoreDNS host 解析外链） | → `Kubernetes/网络.md` `### 排查DNS问题` 节，以列表项并入（注明迁出来源）。 |
| 保留 | 监控对象分层 + ELK/Prometheus 对比 | 留在 `Kubernetes/Kubernetes监控.md`（唯一 H1；原文件首行空行致 H1 在第 2 行，已修复；文首加治理留痕）。 |

## T3 Dapr/Components/Deployments 合并与去重

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 合并 | `Dapr/命名空间.md` → `Dapr/组件配置.md` | 并入"可访问性"一节（同主题去重：中文机制说明 + 英文原文 + 全局访问 YAML 示例共存，无重复句），`git rm` 源文件。 |
| 合并 | `Components/消息中间件.md` → `Components/RabbitMQ.md` | 重构为"概念（原消息中间件全文）/常见命令/问题"三节结构；`•`/`◦` 列表符全部转标准 Markdown 列表，原 H2 标题降为 H3，`git rm` 源文件。 |
| 合并 | `Deployments/K8S部署笔记.md` → `Deployments/K8S集群部署要求.md` | 三个外链迁入文末新增 `## 参考资料` 节（注明 KubeSphere v3.3 为时点文档），"存储方案：Ceph 使用 ceph-deploy 部署"一句一并保留于该节，`git rm` 源文件。 |
| 去重 | `Dapr/BuildingBlocks/PublishSubscribe.md` | 开头导语第 5 行与原 `## 发布订阅` 章节逐字重复：删除 `## 发布订阅` 章节，内容并入文件导语；`## 问题排查` 下"问题一/二/三/四/五/一直启动时失败"统一为"问题 N：一句话概括"格式（一句话为治理时概括，正文未动）；队列名示例代码块补 `text` 语言标注。 |
| 去重 | `ServiceInvocation.md` 与 `故障排除.md` 的 GoAwayFrame 条目 | 细节保留在 `Dapr/故障排除.md`（错误汇编），`ServiceInvocation.md` 改为一句结论 + 指向 `../故障排除.md` 的链接，两处均留痕。 |
| 互链 | HTTP/2 代理错误与 `Programming/DotNet/Libraries/Aspire.md` 的重复 | 按任务要求各保留（Dapr 边车 vs Aspire Dashboard 场景不同），双向互链：故障排除.md 与 Aspire.md 各加"另见"链接，Aspire.md 文首留痕。 |
| 去重+修复 | `Dapr/调试.md` | 文末"其他：…"处重复贴的同一 dapr#6097 issue 链接删除；`[[Discussion] Who is using…](url)` 伪 wikilink（链接文本含未转义方括号）改写为标准链接 `[Discussion · Who is using Visual Studio … · dapr/dapr #6097](url)`；第 4 步空 alt 截图补 alt"Child Process Debugging 设置界面"。 |
| 规整 | `Dapr/服务列表.md` 五级标题 | `Dapr Sentry` 原误挂 `## Placement` 之下（H3），独立为 H2；`##### 基本概念` 等四个五级标题上调为 H4，最深四级、无跳级。 |
| 补 alt | `Dapr/概念.md` ×2、`Dapr/组件配置.md` ×1 | 空alt `![](...)` 补中性描述：Dapr 架构图 / 边车模式示意图 / VS 新建项目对话框中的 Configure for HTTPS 选项（图片内容无法直接判断，按任务允许用中性描述）。 |
| 自查 | `Dapr/BuildingBlocks/Actor.md` | 已通读：文件内仅有 2 条外部 GitHub 链接，无指向旧路径的相对链接，零改动。 |

## T4 Docker 目录治理

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 删除 | `Docker/Docker扩展.md` `## Docker File` 空章节 | 删除留痕（文首 blockquote）。 |
| 删除 | `Docker扩展.md` 末尾 Compose 命令表 5 行空占位 | 删除留痕；因删除后仅剩表头的空表无意义，连同 `### 命令` 空小节一并清理。 |
| 补全 | `Docker/Docker概念与引擎.md` 文末截断句 | 选"补全"方案：原句止于 "…limited to that namespace"（缺句号）。经比对 Docker 官方文档 "The underlying technology" 一节，该句为官方原文完整句，仅补齐句号，未增删内容；文件内 blockquote 说明依据。 |
| 重写 | `Docker/Docker与K8S.md` | AI 问答粘贴痕迹（"你的环境架构""你会看到""运行你的 .NET API""这就是为什么你…"等）重写为中性笔记语气，mermaid 图/表格/命令/容器名分解图等技术内容全保留。文首加环境前提 callout："K8S 直连 containerd 时 `docker ps` 看不到 K8S 容器，非通用行为"。`dockershim` 时代表述（"已废弃"）加时效注：dockershim 已随 `Kubernetes 1.24`（2022-05）移除，本文为 Docker 20.10.8 / containerd v1.4.9 时点观察。两个原本无语言的代码块补 `text`。 |
| 修正 | `Docker/Docker错误排查.md` | `/user/sbin/init` → `/usr/sbin/init`（注释行内），留痕；文末 Docker-in-Docker 日志代码块补 `text` 语言标注。 |
| 加注 | `Docker/环境安装.md` | ① `registry.docker-cn.com` 两处出现均加"[已停服]"标注（JSON 块内无法注释，标注加在块外说明文字与"配置 Docker 镜像源"时效提示中，并连带注明 `docker.mirrors.ustc.edu.cn` 同样已停服）；② 第三方镜像清单节（15 个加速地址）加时效提示：此类镜像站变动/失效频繁，使用前先验证。 |

## T5 隐私脱敏（逐项留痕）

| 文件 | 脱敏项 | 处理 |
|---|---|---|
| `Components/Redis.md` | 明文密码 `P@ssw0rd123` | → `<已脱敏>`（`redis-cli -a` 命令内）。 |
| `Docker/Docker扩展.md` | MSSQL 示例密码 `SA_PASSWORD=passw0rd1!` | → `SA_PASSWORD=<已脱敏>`。 |
| `Deployments/K8S集群部署要求.md` | 时钟服务器内网 IP `188.22.94.120` | → `192.168.x.x`；其余非公网占位（`188.xxx.xxx.xxx`、`xxx.xx.xx.xx`）保留。 |
| `Docker/Docker与K8S.md` | 命名空间 `zgyg-fips-dev`、Pod 名 `zgyg-dev-component-redis-node-0`/`zgyg-dev-service-flight-route-api-5696ffd9d7-nlc79` | 命名空间 → `<内网命名空间>`，Pod 名 → `<内网Pod名>`（同一 `zgyg` 内网标识族一并脱敏；随机性容器 ID / Pod UID / 镜像名非组织标识，保留）。 |
| `Kubernetes/故障恢复.md` | AI 教学腔（"以下是具体操作步骤和注意事项""确保以下字段正确"等口吻） | 重写为中性笔记语气，命令/YAML/匹配规则/排查点全部保留；`•`/`◦` 列表符转标准列表；原首行空行修复。 |

另：`K8S集群部署要求.md` 的非脱敏治理项（编号错乱修复、`im`→`vim`、`tcp_tw_recycle` 加注、资源限制节 AI 痕迹重排、chrony 配置块补 `ini` 标注）见 T3/文件文首留痕——`tcp_tw_recycle` 处按任务原文加注"[内核 4.12 起已移除，待事实核查确认]"。

## T6 域索引

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 更名 | `CloudNative/CloudNative.md` → `CloudNative/README.md` | `git mv`，总览内容保留。 |
| 新增 | 文首 `## 域导航` | Docker/Kubernetes/Dapr/Components/CICD/Deployments 六条"链接 + 一句话"，关键子页（Harbor、网络、监控、故障恢复、集群管理、Building Blocks、发布策略）一并挂链。 |
| 加链 | 正文 5 个相关小节 | `## 容器`、`## 容器编排`、`## 微服务框架Dapr`、`## 支持服务`、`## 自动化` 各加"域内笔记见…"跳转。 |
| 转链 | 裸 URL ×4 | Ocelot / YARP（microsoft/reverse-proxy）/ Dapr for .NET developers / Orleans 官方文档 → 带标题 Markdown 链接。 |
| 联动 | `Frontend/README.md` 跨域互链 | 原指向 `../CloudNative/CloudNative.md` 改为 `../CloudNative/README.md`（避免更名后断链）。 |

## 事实核查待办（`_governance/fact-check/` 候选）

1. `CICD/发布策略.md`：灰度发布 vs 金丝雀发布的区分表述（已加 `[!question]` callout，未擅改）。
2. `Deployments/K8S集群部署要求.md`：`tcp_tw_recycle` 内核 4.12 移除（已按任务原文加注，建议正式确认后转正）。

## 验收

- `python _governance/scripts/fixlinks.py` → `DONE: 0 links fixed`（所有新写链接相对深度本就正确）。
- `python _governance/scripts/checklinks.py` → `all links OK`，exit 0（31 张 orphan 图片为其他域历史存量，与本批无关，未动）。
- 全库引用核查：合并/删除/更名的 7 个文件（Node.md、命令.md、命名空间.md、消息中间件.md、K8S部署笔记.md、CloudNative.md、K8S/TroubleShooting 更名前的旧路径）在存活笔记中已无任何指向；唯一外部引用 `Frontend/README.md → CloudNative.md` 已同步更新。
- 结构核查：本批涉及的全部 24 个文件唯一 H1、标题不跳级、无首行空行（fence 感知校验通过）。
- git 状态：5 个 `git rm`（Node/命令/命名空间/消息中间件/K8S部署笔记）、1 个 `git mv`（CloudNative.md→README.md），未执行任何 `git commit`。
