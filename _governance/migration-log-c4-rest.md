# C4 残留治理日志 — CloudNative / Programming / SoftwareManual / Frontend / English

> 执行日期：2026-09-30。定位：查漏补缺轻扫——五域 118 个 md，前批已整理过的合规文件零改动跳过，只修仍有问题的文件。
> 方法：结构 lint 脚本（唯一 H1 / 无跳级 / 围栏闭合 / 围栏语言，fence 感知）`_governance/tmp/lint_c4.py` 全量扫描 + 修复清单逐项人工核查 + 全域裸外链 / ①②③ / `•`/`◦`/`●` 列表符 / 零宽空格专项扫描。
> 门禁：`fixlinks.py`（DONE: 0 links fixed）+ `checklinks.py`（`all links OK`）；lint 硬性项（围栏闭合、围栏语言、跳级、多 H1/无 H1）终扫 0 问题。
> 本批改动 19 个文件，未 git commit。

## 一、修复清单（19 文件）

| # | 文件 | 修复内容 |
|---|------|----------|
| 1 | `CloudNative/Components/Nginx.md` | 末尾新增 `### 相关条目` 互链 → `../../Kubernetes/故障排查.md`（Nginx 消息截断、获取用户真实 IP 两条，目标锚点 `## Nginx出现消息截断问题`/`## 获取用户真实IP` 已验证存在）。H1 前/*前批已补*，本批核查通过。 |
| 2 | `CloudNative/Components/ApacheAPISIX.md` | `### 幻觉问题` → `### 已删除路由仍生效问题（原记录名"幻觉问题"）`；断言改中性：补 `> [!question] 待事实核查：疑似 etcd / ingress-controller 配置缓存未同步导致已删除路由仍生效，待验证。` 原文现象记录与"可能是 `/*` 所致"猜测未动，文内留痕。 |
| 3 | `CloudNative/Dapr/仪表板.md` | 2022/9/29 快照补 `> [!info] 时效注`（现状以官方文档 / issue #38 为准）。H1 已存在且合规。 |
| 4 | `CloudNative/Dapr/故障排除.md` | L88 json 日志块补语言 ```` ```json ````。（另注：L86 `redis-claster` 疑为 `redis-cluster` 笔误，但可能是 compose 里实际服务名，**未改**。） |
| 5 | `CloudNative/Kubernetes/集群管理.md` | 文末补 `> [!note] 待补充：KubeSphere 与 Kuboard 两套 Dashboard 并存的对比（功能、部署方式、维护活跃度、适用场景）`。H1/层级核查通过（六工具 H2 并列，无跳级）。 |
| 6 | `Programming/Cpp/02-类Class.md` | H1 后插入 `## 概述`，网住原 L3–L180 无标题引言与示例（首个实义标题 `## 拷贝` 在 L181）。 |
| 7 | `Programming/DotNet/AI编码规则.md` | H1 `AI  Coding`（含双空格、与文件名不符、首行空行）→ `# AI 编码规则`，去首行空行。 |
| 8 | `Programming/DotNet/Libraries/Mapster.md` | `## TroubleShotting` → `## Troubleshooting`（拼写）。 |
| 9 | `Programming/DotNet/Libraries/ASP.NET-Core-接口.md` | 空 `## 问题` 节补 `> [!note] 待补充`（保留节名留痕）；`## 待学` 节含参考链接非空，原样保留。 |
| 10 | `Programming/DotNet/Libraries/ASP.NET-Core-进阶.md` | L66 ApplicationModel 树形图块补 `text`；全文清除 76 个零宽空格（U+200B，不可见垃圾字符，如 `### ​**​核心概念​**​`）。 |
| 11 | `Programming/DotNet/Libraries/Aspire.md` | L38 dapr 报错串块补 `text`。 |
| 12 | `Programming/DotNet/Libraries/EntityFrameworkCore.md` | L317 sequenceDiagram 块补 `mermaid`；清除 201 个零宽空格。 |
| 13 | `Programming/DotNet/Libraries/AsyncLocal.md` | 清除 4 个零宽空格。 |
| 14 | `Programming/DotNet/异常处理.md` | 清除 3 个零宽空格。 |
| 15 | `Programming/DotNet/环境部署.md` | L33 machine.config `<runtime>` 块补 `xml`。 |
| 16 | `Programming/DotNet/UI/WPF.md` | ① 16 个 `**●标签**` 伪标题 → `### 标签`（均位于 H2 之下，转后无跳级，`●` 列表符清除）；② L266 XAML 绑定串块补 `xml`。 |
| 17 | `Programming/Python/09-模块与包.md` | L84 包结构树块补 `text`。 |
| 18 | `SoftwareManual/CMD命令.md` | L202 链接文本含未转义嵌套方括号 `[Deprecated, work in progress alternative: https://github.com/M2Team/NanaRun]`（渲染即断链）→ 改写为标准 Markdown 链接，NanaRun 裸链一并转正 `[NanaRun](https://github.com/M2Team/NanaRun)`，英文原文未译。 |
| 19 | `Frontend/Node与npm.md` | 空节 `#### Middleware`（拆分自 Vue.md 时未携带内容）补 `> [!note] 待补充`。H1/层级核查通过。 |

## 二、待事实核查 callout 清单（本批新增 1 处）

| 文件 | 内容 |
|------|------|
| `CloudNative/Components/ApacheAPISIX.md` | 疑似 etcd / ingress-controller 配置缓存未同步导致已删除路由仍生效，待验证（原"幻觉问题"断言改中性）。 |

## 三、核查通过（重点项）

- `CICD/Jenkins.md`：H1 前批已补（`# Jenkins`）。两条 Pipeline 记录为作者经验：① `cat app.log` 无输出 → 日志缓冲未刷新、`sleep 5`，与 Jenkins `sh` 步骤输出缓冲现象相符；② 制品与本地不一致 → 条件编译未同步改，属合理排查思路。均为亲历记录，表述未含越界断言，不加 callout，内容未动。
- `Dapr/部署.md`：L17 `### 50002 DaprGrpcPort for Internal ?` 为作者存疑自注，按指示保留原样。
- `Dapr/BuildingBlocks/Bindings.md`、`Actor.md`、`ServiceInvocation.md`、`PublishSubscribe.md`：唯一 H1、无跳级、围栏带语言（H1 带空格如 "Publish & subscribe" 属命名口径差异，见第五节）。
- `Cpp/01-基础语法.md`：末尾围栏闭合验证——46 个 ``` 标记 = 23 块全配对，前批修复有效。
- `Cpp/03-string与vector.md`、`04-杂项.md`、`DotNet/Libraries/ADO.NET.md` 等 H1 与文件名非逐字一致（如 `# 数据库编程`、`# 其他`）：沿用前批"域前缀/原标题保留"口径（同 `基础.md`→`# C# 基础`、`概念.md`→`# .NET 概念`），未改。
- `DotNet/Libraries` 其余（JsonSerializer/Serilog/Stream/认证/EntityFrameworkCore-问题排查等）：结构核查通过。
- `Python/02-变量.md`、`07-类.md`（49 行种子条目）、`README.md`：唯一 H1、层级合规。
- `Programming/故障排查.md`、`正则表达式.md`、`PHP/基础.md`、`C/指针.md`：前批已修，复核通过。
- `SoftwareManual` 20 文件快查：结构全部合规（H1 命名差异见第五节）；`软件清单.md` 唯一 H1 + H2/H3 层级无跳级重点复核通过；`Proxifier.md` 的 TroubleShotting 修正（前批）已验证生效。
- `Frontend/HTML.md`、`CSS.md`（40KB 级新拆分）：全部代码块带语言（css/html），围栏全配对，无跳级；`TypeScript.md`、`Javascript.md`、`Vue.md`、`WebComponent.md`、`CORS.md`、`README.md`、`Blazor/Blazor.md` 核查通过。
- `English/README.md` + 01–05：唯一 H1（编号前缀去号口径）；例句块**全量**（非抽查）核对——118 个围栏开标记全部 `text`（01:46 / 02:12 / 03:54 / 04:6）；跨文件链接与 `03` 内锚点 `#动名词复合结构`（→ `### 动名词复合结构`）均有效；`README → _archive/English/English-原稿.md` 存在。

## 四、发现未改项（记录备查）

1. `Programming/DotNet/环境部署.md` L68：nexus 仓库地址含公网 IP `188.2.27.132`（行内代码内）。前批仅对 `Deployments/K8S集群部署要求.md` 做过内网 IP 脱敏，此处建议后续统一评估是否脱敏，本批按"尽量不改动内容"未动。
2. `CloudNative/Docker/Docker命令.md` L13：占位域名 `proxy.exaple.com`（`example` 拼写疑误）×2，占位符性质，未改。
3. `CloudNative/Dapr/调试.md` L77：`[https://…\#issuecomment-…](url)` URL 即标题的合法外链，保留。
4. `SoftwareManual/MyLinux环境.md` L68、`Git.md` L164：链接文本为来源页标题（含内嵌 URL），属合法链接，保留。
5. checklinks 报 31 张 `attachments/` 孤儿图：全库既有状态（多涉他域/前批归档），非本批引入，未处理。

## 五、Lint 结果（118 文件，脚本 `_governance/tmp/lint_c4.py`）

- **硬性项 0 FAIL**：无多 H1/无 H1、无跳级、无未闭合围栏、无缺语言围栏（首扫 8 处围栏语言 + 1 处伪标题组 + 零宽空格，已全部修复）。
- **52 文件全项 PASS**：CloudNative 24（Jenkins、发布策略、Nginx、RabbitMQ、Redis、Dapr 全部 8、K8S 5、Docker 4、K8S集群部署要求）、Programming 11（正则表达式、异常处理、环境部署、语法、Aspire、AsyncLocal、Configurations、Mapster、Serilog、Stream、WPF、WinForm）、SoftwareManual 13（AHK、Clash、Git、Kali、Proxifier、ReSharper、Rider、Typora、VMware、VSCode、WSL、注册表、软件清单）、Frontend 3（TypeScript、Vue、Blazor）。
- **66 文件仅 H1 文本 ≠ 文件名**（唯一 H1 均成立，差异为空格/编号前缀/域前缀/README 惯例，沿用前批口径判合规）：README×5、编号前缀文件（Cpp/Python/English 01–05 等）、带空格专有名（`Apache APISIX`、`Microsoft Office`、`Visual Studio`、`Node 与 npm`、`Web Component`）、原标题保留（`批处理基础`、`数据库编程`、`TroubleShooting`、`Harbor镜像仓库`、`Docker环境安装`、`C语言指针` 等）。完整名单见 `_governance/tmp/fail_list.txt`（66 行）/PASS 名单 `pass_list.txt`。
