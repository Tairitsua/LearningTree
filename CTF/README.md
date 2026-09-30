# CTF

CTF（Capture The Flag）竞赛域：按方向组织的题型知识、解题套路、工具清单与攻防笔记。

> 本页为域索引。原 `CTF/README.md` 的杂烩速查内容已于 2026-09 治理分流至各子域文件，原稿归档于 `_archive/CTF/README-旧速查-原稿.md`。

## 子域导航

| 子域 | 定位 | 代表文件 |
|---|---|---|
| [Crypto](Crypto/README.md) | 密码学：古典密码/趣味编码/编码速查三大速查表，`RSA` 与数论、分组密码与攻击模型 | [古典密码速查](Crypto/古典密码速查.md)、[编码速查](Crypto/编码速查.md)、[RSA与数论](Crypto/RSA与数论.md) |
| [Misc](Misc/解题思路.md) | 杂项：解题思维、隐写（图像/音频）、压缩包、流量/取证、数值类 | [解题思路](Misc/解题思路.md)、[图像隐写](Misc/图像隐写/图像隐写.md)、[压缩包](Misc/压缩包.md)、[流量分析](Misc/流量分析.md) |
| [Web](Web/PHP.md) | Web 漏洞与利用：`PHP` 弱类型、`SSTI`/`SSRF`/文件包含/命令执行、绕过技巧 | [PHP](Web/PHP.md)、[SSTI-模板注入](Web/SSTI-模板注入.md)、[绕过技巧](Web/绕过技巧.md)、[JWT](Web/JWT.md) |
| [Reverse](Reverse/Reverse.md) | 逆向：桌面（`IDA`/`x64dbg`、`PE` 文件格式）与 Android（`Frida`/`Jadx`） | [Reverse](Reverse/Reverse.md)、[Android逆向](Reverse/Android逆向.md) |
| [Pwn](Pwn/基础.md) | 二进制利用：`pwntools` 基础与 `checksec`/`NX` 概念（域尚薄弱，待扩充） | [基础](Pwn/基础.md) |
| [AWD](AWD/AWD.md) | 攻防模式：环境与备份、信息收集、不死马/内存马、反弹 `shell`、提权 | [AWD](AWD/AWD.md)、[工具](AWD/工具.md)、[提权](AWD/提权.md)、[Linux要点](AWD/Linux要点.md) |
| [IncidentResponse](IncidentResponse/常见思路.md) | 应急响应：入侵排查流程、Linux 排查十步、Web/数据库日志分析 | [常见思路](IncidentResponse/常见思路.md) |
| [Toolbox](Toolbox/工具清单.md) | CTF 工具：按 Misc/Web/Reverse 方向分节的工具清单与工具专页 | [工具清单](Toolbox/工具清单.md)、[BurpSuite](Toolbox/BurpSuite.md)、[CyberChef](Toolbox/CyberChef.md)、[Wireshark](Toolbox/Wireshark.md)、[010Editor](Toolbox/010Editor.md) |
| [Hacker](Hacker/软件破解.md) | 逆向破解实践记录（非竞赛向） | [软件破解](Hacker/软件破解.md)、[视频号代理解密](Hacker/视频号代理解密.md) |

## 相邻域

- 原理向：Web 漏洞（`XSS`/`CSRF` 等）的原理性介绍见 [ComputerScience/Security](../ComputerScience/Security/README.md)；算法与数论基础见 `ComputerScience/Algorithms/`。
- 工具向：正则语法速查见 [Programming/正则表达式](../Programming/正则表达式.md)；Python 语言基础见 `Programming/Python/`；通用软件见 [SoftwareManual/软件清单](../SoftwareManual/软件清单.md)。
