# 目标架构设计（v1，2026-09-30）

> 阶段 B 产出。依据：`_governance/inventory/*.md` 六份盘点。

## 0. 设计原则

1. **不丢信息**：重组/修格式/修错可以，删内容必须留痕（`_governance/migration-log.md`）。被拆分的原稿进 `_archive/`；被合并的文件内容并入目标后删除原件（git 历史保全）。
2. **链接完整性**：一切移动后重算相对链接（标准 Markdown 相对路径），收尾全库 0 死链。
3. **命名体系**（三层规则）：
   - **目录名**：英文 PascalCase，无空格、无括号、无 `+`（`Frontend`、`Kubernetes`、`Crypto`、`Cpp`）
   - **笔记文件名**：中文主题词（`语法.md`、`公钥密码密钥格式.md`）；英文专有名词保持英文（`Blazor.md`、`AsyncLocal.md`）；多词英文用连字符（`ASP.NET-Core.md`）
   - **系列课程文件**：`NN-` 两位序号前缀（`01-基本概念.md`）；速查/备忘单文件不加序号
4. **域级索引**：每个顶级域目录一个 `README.md`（MOC：一句话定位 + 子主题导航表 + 相关域互链）。已有索引模式的文件（`架构/架构.md`、`网络安全/网络安全.md`、`Python/README.md`）改造为该域 README。
5. **格式规范**：沿用用户原 README 的 10 条 AI 格式化规则（见 PLAN.md），全库统一执行。
6. **新旧并存治理**：原稿 → `_archive/`；整理稿转正。**写手痕迹（AI 对话粘贴、Word 转换残留）清理为正式笔记**，不删信息。
7. **隐私红线**：明文密码、内网 IP、内部命名空间/Pod 名一律脱敏（`<已脱敏>`），留痕。
8. **时效标注**：含版本时点论断的笔记，在文首加"> 记录于 YYYY-MM，XX 已 EOL/停更"式提示，不改正文原意。

## 1. 目标目录树

```
LearningTree/
├── AGENTS.md                    # 【新】知识库总规范（agent 入库宪法）
├── README.md                    # 【重写】知识宫殿总导航
├── attachments/                 # 图片附件（平铺，保持现状）+ _orphan/ 孤儿隔离
├── _templates/                  # 【迁入】模板（原 attachments/templates，7+ 个）
├── _archive/                    # 【新】被取代原稿归档（按来源域分子目录）
├── _governance/                 # 治理工作区（本目录，审计留痕）
│
├── ComputerScience/             # 计算机科学（原理与理论）
│   ├── README.md                # 【新】域索引
│   ├── Algorithms/              # 数据结构与算法（原 数据结构/ + Algorithm/）
│   │   ├── 01-基本概念.md       # 原 02-基本概念 + 01-附录 并入
│   │   ├── 02-线性表.md … 06-排序.md
│   │   └── 07-代码优化.md       # 原 Algorithm/代码优化.md
│   ├── Linux/                   # Linux 系统（原 Linux.md 拆分 + Koubot/Linux命令.md 并入）
│   │   ├── 01-命令速查.md       # 原 # 命令 章（巨型表格）
│   │   ├── 02-Vim.md / 03-Shell脚本.md / 04-用户与权限.md
│   │   ├── 05-磁盘管理.md / 06-SSH.md / 07-网络配置.md
│   │   └── README.md            # 拆分索引（原稿→_archive）
│   ├── OperatingSystem/         # 操作系统（种子：原 操作系统.md）
│   ├── Network/                 # 计算机网络.md（+ 原 WEB.md 3 条概念并入）
│   ├── Database/                # 原 Database.md 按 H1 拆分
│   │   ├── 数据库基础.md / SQLServer.md / MySQL.md / README.md
│   ├── Architecture/            # 原 Architecture/扁平化（架构/ 子目录提升）
│   │   ├── README.md            # 原 架构/架构.md 索引改造
│   │   ├── 架构基础与设计原则.md … 交付流程与软件工程.md（7 篇）
│   │   └── ABP.md
│   ├── Security/                # Web 安全原理与防御（原 网络安全/）
│   │   └── README.md（原 网络安全.md）+ 6 篇内容文件
│   ├── AI/                      # AI 理论与 AI 工具
│   │   ├── 神经网络入门.md      # 原 ArtificialIntelligence.md
│   │   ├── 人声分离UVR5.md / Roop换脸环境.md
│   │   └── LLM安全-提示注入与越狱.md  # 原 Security.md 重写去对话痕迹
│   ├── BigData/                 # 原 BigData.md 拆分：Hadoop生态.md / 云数据中心.md / README.md
│   └── IoT.md / SoftwareTest.md / Unity.md   # 零散主题笔记（域 README 收纳导航）
│
├── Programming/
│   ├── README.md                # 【新】
│   ├── DotNet/                  # 原 NET/
│   │   ├── 语法.md / 基础.md / 概念.md / 内置类型.md / 多线程编程.md
│   │   ├── 异常处理.md / 环境部署.md / 性能优化.md / AI编码规则.md  # 后者原 CS/AI/AICoding.md
│   │   ├── Libraries/           # ASP.NET-Core.md（去空格）/ ASP.NET-Core-接口.md / ASP.NET-Core-进阶.md
│   │   │   │                    # ASP.NET-Core-认证.md（原 Authentication.md）/ ADO.NET.md（原 数据库编程.md）
│   │   │   │                    # EntityFrameworkCore.md / AsyncLocal.md / DependencyInjection.md
│   │   │   │                    # Configurations.md / JsonSerializer.md / Mapster.md / Serilog.md / Stream.md / Aspire.md（原 CloudNative/）
│   │   └── UI/                  # WPF.md / WinForm.md
│   ├── Cpp/                     # 原 C++/（01-基础语法 / 02-类 / 03-string与vector / 04-杂项）
│   ├── Python/                  # 保持 01-10 体系（修锚点/代码块/事实错误；08 常用函数加 H2 分节）
│   ├── C/指针.md                # 原 C.md
│   ├── PHP/基础.md              # 原 PHP.md（修 Word 转换格式）
│   └── 故障排查.md              # 原 TroubleShooting.md（并入 NET/错误排查.md 去重）
│
├── Frontend/                    # 原 Fontend/（拼写修正，含 Blazor.md 内 MyFontend 等扩散修正）
│   ├── README.md                # 【新】
│   ├── HTML.md / CSS.md         # 原 HTML&CSS.md 81KB 拆分（原稿→_archive）
│   ├── Javascript.md / TypeScript.md / Vue.md / WebComponent.md / CORS.md（原 FrontendConcept.md）
│   ├── Node与npm.md             # 【新】从 TypeScript.md/Javascript.md/Vue.md 收敛 npm/nvm/Express 杂项
│   └── Blazor/                  # Blazor.md（IsolationCSS.md 并入"问题"节）
│
├── CloudNative/
│   ├── README.md                # 域索引【新】
│   ├── 总览.md                  # 原 CloudNative.md（Orleans 章节保留）
│   ├── Docker/                  # 概念与引擎/命令/扩展/错误排查/Docker与K8S/Docker与VisualStudio/Harbor/环境安装（原 CS/Linux/Docker环境安装.md 迁入）
│   ├── Kubernetes/              # 原 Kubernetes(K8S)/（去括号；概述+Node 合并；监控拆出 Git/发布/网络节）
│   │   ├── 概述.md / Pod.md / 网络.md / 监控.md / 集群管理.md / 故障恢复.md / 故障排查.md / 命令.md
│   ├── Dapr/                    # 概念/部署/调试/故障排除/服务列表/组件配置（命名空间.md 并入）
│   │   └── BuildingBlocks/      # ServiceInvocation / PublishSubscribe / Bindings / Actor.md（自上级迁入）
│   ├── Components/              # Nginx / Redis / ApacheAPISIX（去空格）/ RabbitMQ（消息中间件.md 并入）
│   ├── CICD/                    # Jenkins.md / 发布策略.md（自 K8S监控"发布"节拆出）
│   └── Deployments/             # K8S集群部署要求.md（K8S部署笔记.md 并入）
│
├── CTF/
│   ├── README.md                # 【重写】纯域索引（原杂烩速查内容分流，原稿→_archive）
│   ├── Crypto/                  # 原 CRYPTO/
│   │   ├── README.md            # 【新】+ 原 学习资料.md 并入
│   │   ├── 古典密码速查.md      # 原 CTF.md 拆分①（替换/棋盘坐标类，原稿→_archive）
│   │   ├── 趣味编码速查.md      # 原 CTF.md 拆分②（程序混淆/中文趣味类）
│   │   ├── 编码速查.md          # 原 Encoding.md（base64CaseCrack、Misc/编码类.md 并入）
│   │   ├── RSA与数论.md         # RSA.md + RSA理论知识.md + 算法性质.md(数论部分) + CTF.md RSA-crack 合并
│   │   ├── XOR与CBC攻击.md      # 算法性质.md(XOR/bit-flip 部分)
│   │   ├── 哈希长度扩展攻击.md  # 原 AWD/工具.md 拆出
│   │   ├── PBE.md / 密码攻击方式.md / 密码种类与特征.md / 公钥密码密钥格式.md / 伪随机数.md
│   ├── Misc/                    # 原 MISC/
│   │   ├── 解题思路.md          # 原 思路打开.md
│   │   ├── 图像隐写/（图像隐写.md + PNG/JPG；BMP.md 并入；CTF.md steg 条目并入）
│   │   ├── 压缩包.md / 流量分析.md / 电子取证.md / 文件头.md / 数值类.md / 音频隐写.md / 镜像分析.md / 二维码.md
│   ├── Web/                     # 原 WEB/
│   │   ├── PHP.md / SSRF.md / SSTI-模板注入.md / 文件包含.md / 代码与命令执行.md / 解析漏洞.md
│   │   ├── 绕过技巧.md          # 原 绕过(Bypass).md + Web/Python.md 的 WAF 绕过部分
│   │   ├── HTTP请求头.md / 信息收集.md（WEB.md view-source 并入）/ 前端审计.md / JavaScript原型链污染.md / JWT.md（原 Practice_Cryptograph.md）
│   ├── Reverse/                 # Reverse.md（PE逆向.md 并入）/ Android逆向.md（拼写修正）
│   ├── Pwn/基础.md
│   ├── AWD/                     # AWD.md / Linux要点.md（原 Linux易忽略点.md）/ 工具.md / 提权.md（自 Web/ 迁入）
│   ├── IncidentResponse/        # 原 应急响应/常见思路.md
│   ├── Toolbox/                 # 原 ToolManual/（BurpSuite 拼写修正）+ 工具清单.md（ToolsList.md CTF 部分）
│   │                            # Xdbg.md 并入工具清单；VMware.md → SoftwareManual/
│   └── Hacker/                  # 软件破解.md / 视频号代理解密.md（原名 代理解密.md，H1 归位）
│
├── SoftwareManual/
│   ├── README.md                # 【新】
│   ├── CMD命令.md / 注册表.md / 批处理.md   # 原 CMD.md 拆分（原稿→_archive）
│   ├── Powershell.md            # + 原 CMD.md"## PowerShell"章并入
│   ├── WSL.md / Kali.md / MyLinux环境.md   # 原 WSL.md 拆分（zshrc 420 行抽出至 attachments/zshrc.conf，原稿→_archive）
│   ├── VisualStudio.md（6 H1 降级）/ Rider.md（SourceGenerator 去重）/ ReSharper.md / VSCode.md
│   ├── Git.md（+ K8S监控"Git提交规范"节并入）/ AHK.md / Typora.md / MicrosoftOffice.md（拼写修正）
│   ├── Clash.md / Proxifier.md / VMware.md（自 CTF/ToolManual 迁入）/ Windows杂记.md（Microsoft+PowerToys 合并）
│   └── 软件清单.md              # 原 ToolsList.md 非 CTF 部分（9 个 H1 迁出重组成文）
│
├── English/                     # README.md + 原 English.md 拆 5 篇（01-长难句解析/02-从句/03-短语与非谓语/04-句子成分/05-词性）
├── Finance/                     # 原 Business/（域名义修正）；恒生科技ETF联接基金.md（原 基础.md，事实修正）
├── Math/                        # README.md + 数论.md / 形式幂级数.md（与 CTF/Crypto 互链）
└── Music/                       # README.md + MusicTheory.md / 和弦.md（调式音阶去重互链）/ FLStudio.md
```

## 2. 配置与基础设施变更

| 项 | 变更 |
|---|---|
| `.obsidian/app.json` | `userIgnoreFilters` 增加 `"_archive/"`、`"_governance/"`（避免归档/治理文件污染搜索） |
| `attachments/templates/` | 迁至 `_templates/`（原位置被 `attachments/` 忽略规则隐藏，搜索不可见） |
| `_templates/LinuxShellPlugin.md` | 修正模板结构：条目用 H2 而非 H1（消除"多条目堆叠=多 H1"缺陷） |
| 根 `README.md` | 重写为总导航（Markdown/Obsidian 使用笔记并入 SoftwareManual，AI 提示词升格进 AGENTS.md） |
| 根 `AGENTS.md` | 【新】知识库规范 + agent 入库流程（阶段 E 产出） |
| `.claude/settings.local.json` | 保留（本地工具配置） |
| Koubot/ | 删除（唯一文件迁至 ComputerScience/Linux/01-命令速查.md） |

## 3. 事实核查清单（阶段 D 输入，来自盘点标记）

| # | 文件 | 存疑点 | 预判 |
|---|---|---|---|
| 1 | 数据结构/04-树 | 有序树/无序树定义写反 | 待证实后修正 |
| 2 | Python/06-数据类型 | "0为True，1为False"说反；`li[:]`称深克隆 | 均为错误，修正 |
| 3 | CRYPTO/公钥密码密钥格式 | "RFC 2347"应为 RFC 8017(PKCS#1) | 待证实后修正 |
| 4 | K8S/Node.md | "Control Panel"应为 Control Plane；Kubelet 职责≠调度 | 错误，修正 |
| 5 | K8S/Pod.md | "Pod 挂掉 IP 也不会变"错误 | 修正（Service 稳定） |
| 6 | Business/基础.md | 恒生科技指数个股权重上限 8% vs 15% | 联网核实 |
| 7 | CloudNative/Deployments | tcp_tw_recycle 内核 4.12 已移除 | 核实 |
| 8 | WEB/PHP.md 等 | magic_quotes_gpc PHP 5.4 移除 | 核实 |
| 9 | Business、应急响应等 | 多处 OCR/拼写错字 | 修正 |
| 10 | AI/ArtificialIntelligence | tf.random.unifrom→uniform | 修正 |
| 11 | NET/概念.md | 实例化顺序；WPF 属 Fx 独有（已过时） | 核实+修正 |
| 12 | ToolsList/Wireshark 等 | ip.src_host 字段、Ciphey 停更等 | 核实 |
| 13 | Music/MusicTheory | BPM=beats per minute 单数 | 修正 |
| 14 | Koubot/Linux命令 | "fc = fix command"词典式伪词源 | 核实 |
| 15 | MISC/文件头 | wav 魔数（RIFF）、html 尾 | 修正 |

## 4. 执行批次（阶段 C 计划）

| 批 | 内容 | 执行者 |
|---|---|---|
| C1 机械重组 | 建目录、git mv/重命名（含去空格/拼写/括号）、链接重算、全库校验、配置变更、模板迁移 | 主 agent（脚本） |
| C2 拆分与合并-域批 | ① ComputerScience（Linux 巨石/Database/BigData/架构扁平化/Algorithms）② CTF（CTF.md 45K 拆分、RSA 族合并、ToolsList 分流、README 重写）③ SoftwareManual（CMD/WSL 拆分）④ Frontend（HTML&CSS 81K 拆分）⑤ English 拆分 ⑥ Programming（ASP.NET Core 家族重组、EFCore、故障排查合并）⑦ CloudNative（概述+Node 合并、监控拆节、命名空间合并） | 每批 1 个 general-purpose 子代理，输出治理记录 |
| C3 归位与去重 | 放错域内容迁移（Hacker/AICoding/Koubot/Web-Python/Aspire 等）、重叠去重互链、空壳合并 | 随 C2 各域批一并做（同域就近），跨域的由主 agent 协调 |
| C4 全库格式治理 | 按 10 条格式规则全量扫描修复（wikilink→md 链接、裸 URL、无语言代码块、H1 规范、①→序号、拼写） | 2-3 个 general-purpose 子代理分域并行 |
| C5 域级 README | 12 个域索引页 + 根 README 重写 | 主 agent |
