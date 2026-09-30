# LearningTree 知识库治理总报告

> 治理周期：2026-09-30（单日完成）· 治理基线：`843554e`（治理前最后一次 vault backup）
> 执行：ZCode 主控 + 13 个子代理（盘点×6 / 内容操作×7 / 格式×4 / 事实核查×1）
> 本报告与全部审计材料位于 `_governance/`。

## 一、成果总览

| 维度 | 治理前 | 治理后 |
|---|---|---|
| 笔记数 | 222 篇 | 239 篇（拆分+64 新建 / 合并-15 / 归档 12 篇原稿移入 `_archive/`） |
| 顶级域 | 11 个（含拼写错误 `Fontend`、错位 `Koubot`/`Business`） | 10 个，全部命名规范 |
| 巨石文件（>30KB） | 15 个（最大 Linux.md 208KB） | 0 个（全部按章节拆分） |
| 笔记互链 | 3 条（孤岛状态） | 全域 README 索引 + 数十条织网互链 |
| 死链 | 16 处（含目录括号致断链） | **0**（251 篇全绿，含归档） |
| 孤儿图片 | 31 张混杂 | 隔离至 `attachments/_orphan/`（未删除） |
| 事实错误 | 15+ 处存疑 | 16 项联网核查全部落地（见 §五） |
| 格式违规 | H1 多/缺 60+ 文件、无语言代码块 300+、wikilink 残留 | lint 全绿（唯一 H1/无跳级/围栏闭合/有语言） |
| 隐私 | 明文密码、内网 IP、内部 Pod 名 | 全部 `<已脱敏>`（见 §七） |
| 长效机制 | 无 | 根 `AGENTS.md` 宪法 + 入库技能 + 模板体系 + 校验脚本 |

治理提交链：`bd083df`(A+B) → `10351b1`(C1) → `52ffd7d`(C2+C3) → `ac862c9`(C4) → `dccfb27`(D) → `b78fe56`(E) → 本次(F)。每步均过链接校验门禁。

## 二、架构重组（阶段 B/C1）

**目录级**：`Fontend→Frontend`、`Kubernetes(K8S)→Kubernetes`（括号是断链根因）、`CRYPTO/MISC/WEB/PWN→Crypto/Misc/Web/Pwn`、`应急响应→IncidentResponse`、`ToolManual→Toolbox`、`数据结构→Algorithms`、`网络安全→Security`、`NET→DotNet`、`C++→Cpp`、`Business→Finance`、`attachments/templates→_templates`（摆脱搜索忽略）。
**文件级**：132 处重命名/迁移（拼写修正 Andorid/MicosoftOffice/Burpsuite 等、去空格 `ASP.NET Core*.md→ASP.NET-Core*.md`、去括号 `绕过(Bypass)→绕过技巧`、语义归位 AICoding→DotNet、Aspire→DotNet、Harbor→Docker、提权→AWD、JWT→Web、正则→Programming、VMware→SoftwareManual 等）。
**配套**：`.obsidian/app.json` 忽略 `_archive/`、`_governance/`；110+ 相对链接脚本化重算。

## 三、拆分与合并（阶段 C2+C3，六域并行）

| 域 | 拆分 | 合并/归位 |
|---|---|---|
| ComputerScience | Linux.md(208KB)→`Linux/`8篇；Database.md→3篇；BigData.md→2篇；架构/扁平化 | 01-附录并入基本概念并重编号 01-07；WEB.md 并入计算机网络；Koubot/Linux命令 并入命令速查（Koubot 域撤销） |
| CTF | CTF.md(84词条)→古典密码+趣味编码速查（75/75 词条脚本核对）；ToolsList→CTF工具清单+软件清单 | RSA 族 3 文件→RSA与数论；算法性质→数论+XOR与CBC攻击；编码类/学习资料/BMP/WEB/Xdbg/漏洞 等空壳归并；README 杂烩 14 处分流后重写为域索引；Web/Python 三域分流 |
| SoftwareManual | CMD.md→4篇（PowerShell章归位）；WSL.md→3篇（420行 zshrc 抽取为 attachments/zshrc.conf） | Microsoft+PowerToys→Windows杂记；Acunetix→CTF工具清单 |
| Frontend | HTML&CSS.md(81KB)→HTML.md+CSS.md | npm/nvm/Express 三处收敛→Node与npm.md；IsolationCSS→Blazor |
| English | English.md→5 篇系列+索引 | 重复图片去重；失效锚点改跨文件链接 |
| Programming | ASP.NET-Core(40KB)家族重组；EFCore→2分册 | 错误排查并入故障排查（3处重复去重）；IOC/Swagger/SignalR 双写去重互链 |
| CloudNative | Kubernetes监控.md 拆节（Git→SoftwareManual、发布→CICD/发布策略、网络→Kubernetes/网络） | 概述+Node+命令合并；命名空间/消息中间件/K8S部署笔记并入对应文件 |

全部操作留痕：`_governance/migration-log-*.md`（7 份）；原稿 12 篇归档 `_archive/`（Obsidian 搜索已忽略，git 历史完整）。

## 四、格式治理（阶段 C4）

37+ 文件修复：多 H1/无 H1 归一（PHP 7 个 H1、乐理 5 个、公钥密码密钥格式 5 个等）；13 处空节"待补充"标注；300+ 代码块补语言（含 css/bash/vbnet 误标纠正）；①/全角序号/`※`/`•` 全部标准化；WPF 16 个 `**●**` 伪标题转正；284 个零宽字符清除；LLM安全、Proxifier 等 AI 对话粘贴重写为结构化笔记（技术内容零丢失）；cnblogs 外链图片本地化；3 条失效链接实测标注。

## 五、事实核查（阶段 D，全部联网验证，来源见 `_governance/fact-check/findings.md`）

**修正 8 项**：RFC 2347→RFC 8017（私钥 ASN.1，溯源 RFC 2313）；恒生科技个股权重上限 15%→**8%**（恒指公司编算细则）；.NET 实例化顺序按 ECMA-334 重排（C# 特有：派生类实例字段初始化器先于基类构造）；灰度/金丝雀术语按 Martin Fowler+中文主流用法澄清；bash `"${@:2}"` 展开为多参数；`tcp_tw_recycle` 内核 4.12 移除确认；SSRF 协议表加历史经验注（`--with-curlwrappers` PHP 5.5 移除）；Ciphey 状态更正（未停更，已迁 bee-san/Ciphey）。
**核实无误 5 项**（删疑点注）：`ip.src_host` 字段真实存在；`fc`="fix command"（POSIX）；machine.config v2.0.50727 路径正确；dockershim v1.24 移除；"hithub"系原文作者自造示例名（非 OCR 错字）。
**其他**：有序树/无序树定义（C2 修正）、Python 布尔/浅拷贝（C2 修正）、magic_quotes_gpc 5.4 移除（C4 修正）、wav 魔数 RIFF（C4 修正）等。

## 六、织网与索引

12 个域全部有 `README.md` MOC 索引（新建 8 个 + 改造 4 个）；根 `README.md` 重写为知识宫殿总导航；Math↔CTF/Crypto、Security↔CTF、Dapr↔K8s/Aspire、VisualStudio↔Rider 等数十条互链落地。

## 七、隐私脱敏

`Components/Redis.md` 明文密码、`Docker扩展.md` MSSQL 密码、`K8S集群部署要求.md` 内网 IP `188.22.94.120`、`Docker与K8S.md` 内部命名空间/Pod 名、`环境部署.md` 公网 Nexus IP —— 全部替换 `<已脱敏>`，原值仅存于治理日志与 git 历史。

## 八、长效机制（阶段 E）

1. **根 `AGENTS.md`**：域边界规则、命名/格式/链接/内容政策、**知识入库工作流**（判域→判粒度→写入→织网→核查→校验→提交）、治理工具说明。未来任何 agent 进本仓库的第一入口。
2. **入库技能 `learningtree-intake`**（`C:\Users\mo\.agents\skills\`）：把"扔一条知识点"场景固化为可复用技能，含幂等示例与红线清单。
3. **模板体系 `_templates/`**：新增通用知识条目模板；修正 LinuxShellPlugin 模板（条目 H2 化，根治多 H1 缺陷）；保留 CTF writeup 双模板。
4. **校验工具 `_governance/scripts/`**：`fixlinks.py`（幂等链接重算）、`checklinks.py`（死链+孤儿图）、`lint_ctf.py`（结构 lint 范例）。

## 九、遗留事项与建议

| # | 事项 | 建议 |
|---|---|---|
| 1 | `attachments/_orphan/` 31 张图 | 人工浏览确认后可删除（git 有历史）；若确认无用直接整目录删即可 |
| 2 | `ApacheAPISIX.md` 的"已删路由仍生效"环境假设 callout | 待现场验证 etcd/ingress-controller 缓存行为 |
| 3 | Pwn 域仅 1 篇入门（覆盖缺口） | 后续积累 ROP/堆等专题 |
| 4 | CTF writeup 模板自 2023 后未产生新 writeup | 入库技能会按模板承接 |
| 5 | obsidian-git 自动备份与治理提交交错 | 正常现象，无需处理 |
| 6 | `_archive/` 12 篇原稿 | 已退出搜索；确认整理稿无缺漏后可整体删除（建议保留 3 个月） |

## 十、方法论备注

- 子代理分工：盘点（Explore，并行 6 域）→ 内容操作（general-purpose，按域并行，互不触碰对方域）→ 格式（幂等扫尾）→ 事实核查（联网）。主控负责架构决策、脚本、提交与门禁。
- 门禁纪律：每次结构改动后 `fixlinks+checklinks` 全绿才 commit；拆分完整性用脚本核对（如 CTF 84 词条 75/75 命中、Linux/Database/BigData 标题全覆盖）。
- 两处盘点误报被校验脚本纠正（"7 张丢失图片"实际存在），一处事实疑点被核查反转（`ip.src_host` 真实存在）——体现"以工具与权威来源为准，不以代理断言为准"。
