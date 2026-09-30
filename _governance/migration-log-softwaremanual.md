# 治理日志：SoftwareManual 批（C2）

> 执行日期：2026-09-30。范围：`SoftwareManual/` 域内容操作（拆分/合并/格式治理）。未 `git commit`。
> 原则：不丢信息、`git mv`/`git rm` 保留历史、内容改动留痕于本文件与文件内 blockquote。原稿归档均保留原文（含原有格式瑕疵），仅文首追加"已拆分归档"说明。
> 验收：`fixlinks.py` 0 处修正、`checklinks.py` `all links OK`（exit 0）。

## T1 `SoftwareManual/CMD.md`（40KB，3 个 H1）拆分

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 拆分 | `SoftwareManual/CMD.md` 的 `# CMD` 章（剔除其中 `## PowerShell` 整章） | → 新建 `SoftwareManual/CMD命令.md`（唯一 H1 `# CMD`；含 Windows/设置Alias/文件操作/网络 各 H2）。图片引用相对路径不变（同目录深度），全库扫描无其他文件链接到 `CMD.md`。 |
| 合并 | `SoftwareManual/CMD.md` 的 `## PowerShell` 整章 | 并入 `SoftwareManual/Powershell.md`（原 `###` 子节提升为 `##`），与原有 `从单行base64执行`/`通过VBS运行脚本` 无重复内容，去重后直接追加。 |
| 拆分 | `# 注册表` 章 | → 新建 `SoftwareManual/注册表.md`（唯一 H1）。 |
| 拆分 | `# 批处理基础` 章 | → 新建 `SoftwareManual/批处理.md`（唯一 H1，标题保留原文"批处理基础"）。 |
| 归档 | `SoftwareManual/CMD.md` | `git mv` → `_archive/SoftwareManual/CMD-原稿.md`，文首加"已拆分归档"说明（git 状态为纯 rename，历史保留）。 |
| 格式修正 | 5 处 ① 类标号 | `### 端口占用问题` 的 ①②③ 与"变量延迟"节的 ①② 均改为 Markdown 序号列表，文字未动。 |
| 格式修正 | 6 个无语言代码块 | 均位于批处理章：命令块补 `bat`（变量延迟 ×2、for /r 示例 ×2），输出块补 `text`（for /r 输出 ×2）；原误标 `sh`/`log`/`bash` 但实为批处理命令/输出的块一并改为 `bat`/`text`。 |
| 修正 | `doskey` 引用的 XP 版 technet 文档 | 链接文字加"[历史文档]"并注明"XP 时代 technet 版文档，仅作参考"。 |
| 事实修正 | `powercfg batteryreport` | 原稿 `powercfg batteryreport output "D:\\battery_report.html"` 缺 `/` 参数写法，按正确语法改为 `powercfg /batteryreport /output "D:\battery_report.html"`（该节随 PowerShell 章位于 Powershell.md，两处留痕）。 |
| 格式修正 | 其余 | 注册表/批处理/输入输出/IF/FOR 各节原 H1 下直接 `####` 的跳级标题提升；`### 调整网络优先级` 一处不成对反引号修正；CMD命令.md 内服务启动类型处补指向 `SoftwareManual/注册表.md` 的链接行。 |

## T2 `SoftwareManual/WSL.md`（32KB，3 个 H1）拆分

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 拆分 | `# WSL` 章 | 留在 `SoftwareManual/WSL.md`（保留文件名；外部引用 `ComputerScience/Linux.md` 的 `[WSL](../SoftwareManual/WSL.md)` 因此保持有效）。 |
| 拆分 | `# Kali` 章 | → 新建 `SoftwareManual/Kali.md`（唯一 H1）。 |
| 拆分 | `# MyLinux` 章 | → 新建 `SoftwareManual/MyLinux环境.md`（H1 保留原文 `# MyLinux`）。 |
| 抽取 | `### ~/.zshrc` 下 412 行 `.zshrc` 全文 | → `attachments/zshrc.conf`（内容一字未改）；笔记中保留说明句 + 链接 `[zshrc.conf](../attachments/zshrc.conf)`，文首留痕。 |
| 保留 | `## Linux命令手册` 节 | 对照 `ComputerScience/Linux.md`（命令速查大表）复核：该节内容是 jaywcjlove/linux-command 查询网站的 Docker 部署方法，与 Linux 命令表不构成重复，按任务规则"否则保留原文"整节保留。 |
| 加链 | cryptohack/bkcrack 等 CTF 工具安装段 | 任务原文写"保留在 Kali.md"，实际盘点发现这些安装段（`## 安装常用包`、`## 安装自编译软件`）位于 `# MyLinux` 章的 Docker 环境上下文中，移入 Kali.md 会脱离语境。故保留在 MyLinux环境.md 并在 `## 安装自编译软件` 末尾加指向 `CTF/Toolbox/工具清单.md` 的 blockquote 链接；同时在 Kali.md 文首导语加同一链接（Kali 为 CTF 发行版语境），两处均覆盖任务意图。 |
| 归档 | `SoftwareManual/WSL.md` | `git mv` → `_archive/SoftwareManual/WSL-原稿.md`（文首加说明，含 zshrc 抽取去向）；因原路径新建了同名 WSL.md，git 状态呈现为 M+A 而非 rename，原稿全文已在归档件中完整保留。 |
| 格式修正 | WSL.md | 裸外链 `<https://…>` ×3 与一处纯文本 URL 改为带标题链接；2 个无语言代码块补标（wsl 报错输出 `text`、`/etc/wsl.conf` 为 `ini`）；`## WSL连接宿主机代理` 下直接 `####` 的"新版配置/脚本"提升为 `###`。 |
| 格式修正 | Kali.md | 裸外链 ×2（CSDN 桌面版教程、debian 邮件列表）改为带标题链接；KeX 节 Bing 引文的两条来源 URL 改为 Markdown 链接（AI 回答正文按"尽量不改动内容"原则保留原样）。 |

## T3 `SoftwareManual/VisualStudio.md` 标题降级

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 降级 | 6 个 H1 | `# Visual Studio` 保持唯一 H1；`# 项目配置`/`# 发布`/`# 模板`/`# 调试`/`# 快捷操作` 5 个 H1 降为 H2，其下 39 个子孙标题各下移一级（合计 44 处，脚本围栏感知，代码块内 `#` 注释未误伤），无跳级。 |
| 核查 | 盘点所称"10 个无语言代码块" | 复核实为 10 个代码块的**闭合围栏**被误计：`editorconfig`/`shell`/`csharp`×3/`xml`×5 全部已带语言标注，无需补标（留痕于文件内）。 |
| 互链 | SourceGenerator 调试 | `### 调试 SourceGenerator 或 EFCore 等非常规程序入口点` 末尾加"另见 [Rider](Rider.md)"；Rider.md 对应节加"另见 [Visual Studio](VisualStudio.md)"，双向成对。 |

## T4 合并与收尾

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 合并 | `SoftwareManual/Microsoft.md`（0.4KB）+ `SoftwareManual/PowerToys.md`（0.2KB） | → 新建 `SoftwareManual/Windows杂记.md`（唯一 H1，两个 H2：Microsoft Store 连接问题 / PowerToys 键位映射）；拼写"clsah"→`Clash` 修正并留痕；随后 `git rm` 两个源文件。 |
| 删除 | `SoftwareManual/Acunetix.md`（0.1KB） | 内容已由 CTF 域代理并入 `CTF/Toolbox/工具清单.md`（已核实第 69 行含 Acunetix 条目及出处说明），`git rm`。 |
| 加注 | `SoftwareManual/Clash.md` | 文首加时效提示："记录于 Clash for Windows 时期（2023-11 官方归档停更），配置思想仍适用于 Clash Verge 等续作"。 |
| 重写 | `SoftwareManual/Proxifier.md` | AI 回答粘贴痕迹（"Key evidence from your machine""I hope that helps"口吻）重写为中性笔记语气：现象→关键证据（假 DNS 的 127.170.10.x 记录、`fd00:696e:6974:6578::...` 解码 `initex` 等）→解决步骤→更合理配置；XML 证据（`<ViaProxy>`/Direct 规则）改为 `xml` 代码块但内容原样保留；H1 由 `# TroubleShotting` 改为 `# Proxifier`（题文相符+拼写修正），留痕。 |
| 格式 | `MicrosoftOffice.md` | "设置大纲级别"节末尾 AI 引文编号残留"标题级别3。"的"3"已删除，留痕。其余核查通过（唯一 H1、无跳级、无代码块）。 |
| 格式 | `VMware.md` | `## TroubleShooting` → `## Troubleshooting`，留痕。 |
| 格式 | `Rider.md` | `## Verison Control` → `## Version Control`，留痕；另见 T3 互链。 |
| 格式 | `Git.md` | 明显错误修正并留痕：`.gitingore` ×3 统一改为 `.gitignore`；命令笔误 `git add remote origin <url>` → `git remote add origin <url>`。代码块均已带语言（`bash`/`sh`/`shell`/`gitattributes`/`mailmap`）。 |
| 核查 | `VSCode.md`、`AHK.md`、`Typora.md`、`ReSharper.md` | 逐项核查（唯一 H1、标题不跳级、代码块语言、专名反引号）均通过，零改动。 |
| 不动 | CloudNative 域"Git 提交规范"节 | 按任务说明确认非本域职责，跳过（该节实际在 CloudNative 域）。 |

## T5 域索引

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 新建 | `SoftwareManual/README.md` | 软件速查总索引，分类：终端与 Shell（CMD命令/Powershell/批处理/WSL/Kali/MyLinux环境）、开发工具（VisualStudio/VSCode/Rider/ReSharper/Git）、办公与写作（MicrosoftOffice/Typora）、网络与代理（Clash/Proxifier）、系统工具（注册表/Windows杂记/VMware/AHK）、清单（软件清单）；每行"链接+一句话"。含 `软件清单.md`（另一代理创建，未改动其内容）与 CTF 工具清单、归档目录入口。 |

## 验收

- `python _governance/scripts/fixlinks.py` → `DONE: 0 links fixed`（拆分后所有新旧链接深度本就正确）。
- `python _governance/scripts/checklinks.py` → `all links OK`，exit 0（31 张 orphan 图片为其他域历史存量，与本批无关，未动）。
- 全库引用核查：除 `ComputerScience/Linux.md → SoftwareManual/WSL.md`（文件名保留，仍有效）外，无其他存活笔记链接到本批移动/删除的文件。
