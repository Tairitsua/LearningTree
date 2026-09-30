# 盘点：CloudNative 域（39 文件）

> 来源：治理阶段 A 探查子代理，2026-09-30。约 174KB。无 >20KB 文件。

## 一、逐文件记录（39/39）

| 文件 | KB | 语言 | 主题 | 问题标记 | 重叠提示 |
|---|---|---|---|---|---|
| CloudNative.md | 11.6 | 混 | 云原生总览：CNCF/路线图、概念、Dapr/Orleans、容器编排、CI/CD | 裸URL(4) | 与 Dapr/概念.md、K8S/概述.md、Docker/概念与引擎.md、消息中间件.md 重叠；作总览却未链接任何子笔记 |
| Aspire.md | 4.1 | 混 | .NET Aspire 两个问题排查（HTTP/2代理、dapr APIPA 调用失败） | 代码块无语言(1) | 与 Dapr/故障排除.md HTTP/2 错误同根因 |
| 消息中间件.md | 4.5 | zh | RabbitMQ 队列/交换机/主题概念科普+配置 | 标题层级乱；`•`/`◦`非标准列表符 | 与 Components/RabbitMQ.md、PublishSubscribe.md(L13重复解释Queue/Exchange) 三处同主题 |
| CICD/Jenkins.md | 0.4 | zh | Jenkins 两条 Pipeline 问题小记 | 空文件/极简 | CICD 目录仅此一文件 |
| Components/Apache APISIX.md | 0.7 | zh | APISIX 正则转发路由+两问题 | 事实可疑("幻觉问题"断言无依据，更可能是 etcd/ingress-controller 缓存) | 与 Components/Nginx.md 同为网关 |
| Components/Nginx.md | 0.2 | zh | Nginx location 不生效（前端缓存） | 空文件/极简 | Nginx 内容分散两处（K8S/TroubleShooting 也有） |
| Components/RabbitMQ.md | 2.5 | zh | rabbitmqctl 批量清除队列/交换机与节点重置 | `•`列表符 | 与 消息中间件.md 概念重叠 |
| Components/Redis.md | 0.1 | zh | Redis 主从查看单条命令 | 空文件/极简；**明文密码 `P@ssw0rd123` 安全隐患** | Dapr 多处以 Redis 为 statestore 未互链 |
| Dapr/Actor.md | 2.8 | 混 | Dapr Actor 状态管理/序列化/跨命名空间 | 疑似过期("现在1.14支持跨命名空间"时点论断) | 与 CloudNative.md Orleans/Actor 章节重叠；应归 BuildingBlocks |
| Dapr/仪表板.md | 0.2 | zh | Dashboard standalone 不支持 docker compose | 空文件/极简；快照截至 2022/9/29 | 无 |
| Dapr/命名空间.md | 0.8 | zh | Dapr 命名空间机制与组件全局访问 | 无 | 与 Dapr/组件配置.md"可访问性"同主题，未互链 |
| Dapr/故障排除.md | 4.7 | 混 | Dapr 13类常见错误排查汇编 | 代码块无语言(1) | GoAwayFrame 与 ServiceInvocation.md 重复；HTTP/2 与 Aspire.md 重复 |
| Dapr/服务列表.md | 1.9 | zh | Placement/Sentry 服务+SPIFFE ID 解析 | 标题嵌套至##### | 与 Dapr/部署.md"安全"章节相关 |
| Dapr/概念.md | 4.3 | 混 | Dapr 定位、边车模式、与 Service mesh 区别、BB 表 | 空alt图片(`![]()` x2) | BB 表与 CloudNative.md 章节重叠 |
| Dapr/组件配置.md | 1.5 | 混 | 组件可访问性/HTTPS/状态存储（大段英文摘自微软电子书） | 空alt(1)；docs.microsoft.com 旧链 | 与 Dapr/命名空间.md 重叠 |
| Dapr/调试.md | 4.0 | 混 | VS2022+PowerShell+Child Process Debugging 调试 dapr | 伪 wikilink(`[[Discussion]…](url)`)；docs.microsoft.com；同一链接文末重复两次 | 与 Docker/VisualStudio集成.md 同为 VS 工具链 |
| Dapr/部署.md | 1.6 | 混 | Self-Host 安装/边车端口/监听地址/证书刷新 | "50002 for Internal ?"存疑自注 | 端口表与 ServiceInvocation.md 开头重复 |
| Dapr/BuildingBlocks/Bindings.md | 1.6 | zh | 输入/输出绑定概念+两个未生效排查 | 无 | pubsub/binding 混淆条目与 PublishSubscribe.md 相关 |
| Dapr/BuildingBlocks/PublishSubscribe.md | 5.1 | zh | 发布订阅消费模式/批量推送+Kafka/RabbitMQ 6类问题 | 代码块无语言(1)；"问题N"命名随意；开头 L3-5 与"## 发布订阅"章节逐字重复 | 与 消息中间件.md、Components/RabbitMQ.md 三处消息主题 |
| Dapr/BuildingBlocks/ServiceInvocation.md | 3.2 | 混 | 服务调用端口模型+常见调用错误 | **断链：`[Kubernetes(K8S)](Kubernetes(K8S).md#DNS)` 相对本文件指向不存在的路径**；括号 URL 截断风险 | GoAwayFrame 与 故障排除.md 重复 |
| Deployments/K8S部署笔记.md | 0.6 | zh | K8S 部署外链资源+Ceph 一句 | 空文件/极简；KubeSphere v3.3 文档已过时 | 与 集群管理.md 重叠 |
| Deployments/K8S集群部署要求.md | 8.5 | zh | openEuler22.03 离线集群前置要求 | 代码块无语言(2)；全角（2）（3）编号重复错乱；**内网 IP 188.22.94.120 明文留痕**；`im`应为`vim`；`tcp_tw_recycle` 已随内核4.12移除仍列为可调；"出现下图则部署成功"缺图 | 与 集群管理.md 同属部署主题分散两目录 |
| Docker/Docker与K8S.md | 4.5 | 混 | docker ps 为何能看到 K8S 容器 | 代码块无语言(2)；**结论环境特定非通用事实**；AI 对话粘贴痕迹("你的环境架构")；Docker 20.10.8/dockershim 时代 | 与 概念与引擎/Node.md/Pod.md 四处讲容器运行时 |
| Docker/Docker命令.md | 4.9 | 混 | Docker CLI 命令速查表 | 无 | save/load 与 Harbor镜像仓库.md 重复；与 Docker扩展.md 分立两份命令表 |
| Docker/Docker扩展.md | 6.4 | 混 | Network/Storage/Volume/BindMount/Compose 扩展概念 | "## Docker File"空章节；末尾 Compose 命令表 5 行空占位 | VS 集成小节与 VisualStudio集成.md 重叠 |
| Docker/Docker概念与引擎.md | 5.6 | 混 | Docker 概念与 Engine 架构（官方文档翻译摘录） | 文末句子中途截断"…limited to that namespace" | 与 CloudNative.md"容器"章重叠 |
| Docker/Docker错误排查.md | 3.6 | zh | COPY找不到/D-Bus/DinD daemon 挂掉等6类 | 代码块无语言(1)；`/user/sbin/init` 疑为 `/usr/sbin/init` | COPY context 与 VisualStudio集成.md 同类 |
| Docker/VisualStudio集成.md | 4.8 | 混 | VS 容器工具集成+13条构建错误排查 | 疑似过期(docs.microsoft.com、Resharper 2022.2.3)；13个###平铺无分组；文件名缺 Docker 前缀 | 边车连不上 RabbitMQ 与 PublishSubscribe 问题二同模式 |
| K8S/Harbor镜像仓库.md | 0.6 | zh | docker save/load/tag/push 推送 Harbor | 无 | 内容实为 Docker 通用操作；文末链接到 集群管理.md |
| K8S/Kubernetes监控.md | 4.0 | zh | 监控对象分层+ELK/Prometheus 对比 | 标题层级乱/主题漂移("## Git"提交规范、"## 发布"灰度金丝雀、"## 网络"与监控无关)；灰度vs金丝雀定义区分不标准；首行空行致 H1 在第2行 | 发布章节与 CICD 域重叠 |
| K8S/Node.md | 1.0 | 混 | Worker/Master 节点组件速览 | 事实可疑(**"Control Panel"应为"Control Plane"；Kubelet 职责写成"调度 Pod"，调度是 Scheduler**) | 与 概述.md 高度重复可合并 |
| K8S/Pod.md | 5.3 | 混 | Pod/Service/ConfigMap/挂载/容器权限 | 事实可疑(**"Pod 挂掉 IP 也不会变"错误——Pod 重建 IP 会变，稳定的是 Service**)；文末"下周准备继续跟进"待办残句 | CRI/OCI 段与 Docker与K8S.md 重叠 |
| K8S/TroubleShooting.md | 1.8 | 混 | calico 网络性能/Nginx 截断/真实IP/命名空间限制4条 | 英文名与 故障排除/错误排查 命名不一致 | Nginx 两条与 Components/Nginx.md 重叠 |
| K8S/命令.md | 0.4 | zh | kubectl 单条命令表（仅 get pods 一行） | 空文件/极简；泛文件名 | 与 Docker命令.md 等构成三种命名风格 |
| K8S/故障恢复.md | 5.4 | zh | Ceph RBD 块恢复+PV/PVC 静态绑定恢复 | `•`/`◦` 列表符；AI 对话粘贴痕迹 | Ceph 与 集群管理.md 互补应互链 |
| K8S/概述.md | 0.7 | zh | K8s 一句话定位+架构图+kubectl | 无（泛文件名） | 与 Node.md 相邻重复；与 CloudNative.md 重叠 |
| K8S/网络.md | 1.4 | zh | 跨命名空间访问+Service/Pod DNS 格式+busybox 排查 | 无 | 是 ServiceInvocation.md 断链的本意目标；与 集群管理.md"跨命名空间"重复 |
| K8S/集群管理.md | 9.3 | 混 | KubeSphere/HAproxy/Keepalived/Ceph/Kuboard/Minikube 六工具合集 | 无（天然拆分候选） | 与 Deployments 两文件重叠；Kuboard 与 KubeSphere 两套 Dashboard 未对比 |

注：①类圆圈标号经 grep 确认零出现；表中"①类标号风格"指全角（2）（3）或 `•`/`◦` 列表符变体。

## 二、子目录画像

| 目录 | 文件数 | 画像 | 命名 |
|---|---|---|---|
| 根 | 3 | 1 总览+2 散件 | 总览=域名同名 |
| CICD/ | 1 | 仅 Jenkins 排错 | 英文产品名 |
| Components/ | 4 | 中间件/网关排错碎片，三个 0.1~0.7KB | 英文产品名（空格分隔） |
| Dapr/ | 9+3 | 最成体系：概念→部署→调试→排错→配置；BB 子目录按构建块拆 | 主目录中文功能名，BB 英文名；Actor.md 未入 BB 属归类不一致 |
| Deployments/ | 2 | openEuler 离线内网装机手册 | "K8S+中文描述"式 |
| Docker/ | 6 | 概念/命令/扩展/排错/VS集成/与K8S关系 | "Docker+X"前缀式；VisualStudio集成.md 破例 |
| Kubernetes(K8S)/ | 10 | 概念+专题+排错+命令+Harbor | 中英混用；概述/命令/网络 为无前缀泛名 |

## 三、笔记→笔记内部链接（仅 2 条）

| 源 | 目标 | 状态 |
|---|---|---|
| Dapr/BuildingBlocks/ServiceInvocation.md | `Kubernetes(K8S).md#DNS` | **断链**：解析为 Dapr/BuildingBlocks/Kubernetes(K8S).md（不存在）；本意应为 `../../Kubernetes(K8S)/网络.md#DNS`；括号 URL 截断 |
| K8S/Harbor镜像仓库.md | `集群管理.md` | 有效 |

## 四、图片引用

42 个引用全部有效；空alt 4 处（Dapr/概念×2、组件配置×1、调试×1）；Pasted image %20 编码 7 处；K8S集群部署要求.md 文末缺图；唯一 .jpg 在 K8S/TroubleShooting.md；CloudNative.md 单文件 15 张图最密。

## 五、最大三文件（拆分参考）

- CloudNative.md（11.6KB）H2：学习/概念/微服务框架Dapr(含Orleans)/容器/容器编排/支持服务/自动化——Orleans 可独立成篇。
- K8S/集群管理.md（9.3KB）H2：KubeSphere/HAproxy/Keepalived(VRRP)/Ceph/Kuboard/Minikube——六个独立工具。
- Deployments/K8S集群部署要求.md（8.5KB）H2：节点要求/防火墙/时钟/DNS/系统资源限制/openEuler软件源。

## 六、组织问题汇总

1. **`Kubernetes(K8S)` 目录名带括号**：markdown URL 截断（已致 1 处实际断链）、URL/git 不友好——改名并修复断链。
2. 排查类笔记四处分散、命名不一（故障排除/TroubleShooting/错误排查）；两处实打实重复（GoAwayFrame、HTTP/2 代理）。
3. 主题重复/分散：消息三处、Nginx 两处、容器运行时四处、K8S 部署横跨两目录、命令速查三种风格。
4. 边界：Aspire.md 属 .NET 编排工具；消息中间件.md 应归 Components/；Harbor 主体是 Docker 命令；Kubernetes监控.md 含 Git/发布/网络三个离题章；命名空间.md 与 组件配置.md 应合并；概述.md 与 Node.md 可合并；CloudNative.md 中 Orleans 篇幅大。
5. Dapr BuildingBlocks 只收 3/8 构建块，Actor.md 悬在上级；服务列表.md 嵌套五级；调试.md 伪 wikilink 与重复链接。
6. 时点性论断未标注（仪表板 2022/9/29、Actor 1.14、Resharper 2022.2.3、KubeSphere 3.3、Docker 20.10.8/dockershim）。
7. **安全/隐私**：Redis.md 明文密码；Docker扩展.md MSSQL 示例密码；K8S集群部署要求.md 内网 IP；Docker与K8S.md 命名空间/Pod 名（zgyg-fips-dev）。
8. AI 对话粘贴痕迹三处（Docker与K8S/故障恢复/K8S集群部署要求），含未清理口语和编号错乱。
9. 极简文件 6 个：Redis/Nginx/仪表板/Jenkins/命令/K8S部署笔记。
