# 盘点：CTF/AWD+MISC+Hacker+ToolManual+应急响应+根散文件（29 文件）

> 来源：治理阶段 A 探查子代理，2026-09-30。

范围共 29 个 .md（AWD 4、MISC 13 含图像隐写 4、Hacker 2、ToolManual 6、应急响应 1、ToolsList 1、CTF 根散文件 3）。

## 一、逐文件记录

### AWD（4）

| 文件 | 记录 |
|---|---|
| AWD/AWD.md | 6.5KB \| zh \| AWD 攻防总纲：环境搭建、备份、信息收集、不死马/内存马、反弹shell \| 标题层级乱(####主机发现/####目录发现挂##防御下，攻防章混排) \| 与 应急响应/常见思路.md(进程查杀/启动项)、AWD/Linux易忽略点.md(/dev/tcp、反弹shell原理重复) |
| AWD/Linux易忽略点.md | 8.1KB \| 混 \| Linux基础语法/重定向/文件描述符笔记 \| 事实可疑("${@:2} treats as a single string"表述不准,实为展开为多个参数) \| 与 AWD/AWD.md 反弹shell一节重复 |
| AWD/工具.md | 6.7KB \| zh \| AWD工具:docker镜像、PHP靶机构建、Weevely、Hash_extender、MSF \| 疑似过期(php:7.2镜像、aliyun源、Metasploit空节) \| 与 ToolManual/*、ToolsList.md 三处并存工具清单；Hash_extender(哈希扩展攻击)属CRYPTO放错位置 |
| AWD/漏洞.md | 0.1KB \| zh \| 仅一个vulhub链接的占位 \| 空文件/极简 \| 与 ToolsList.md 同质(纯链接清单) |

### MISC（13）

| 文件 | 记录 |
|---|---|
| MISC/二维码.md | 1.6KB \| 混 \| 二维码结构与格式版本信息 \| H1多个(#结构/#格式和版本信息)、英文段未消化 \| 无 |
| MISC/压缩包.md | 6.8KB \| zh \| ZIP/RAR结构、伪加密、CRC爆破、明文攻击(bkcrack/ARCHPR)、NTFS流隐写 \| H1多个、标题层级乱、疑似过期(banzip等工具名) \| NTFS流隐写与 README.md 文件隐写节重复(grep证实)；文件头hex与 文件头.md 重复 |
| MISC/图像隐写/BMP.md | 0.2KB \| zh \| BMP隐写特征极简卡 \| 空文件/极简 \| 宽高隐写内容被 图像隐写.md 覆盖 |
| MISC/图像隐写/JPG.md | 2.0KB \| 混 \| JPG标记段结构表+隐写工具(stegdetect/jphs/silenteye) \| 无 \| silenteye 与 图像隐写.md 工具节重复；JPG文件头与 文件头.md 重复 |
| MISC/图像隐写/PNG.md | 9.1KB \| zh \| PNG数据块结构详解+宽高/IDAT/附加三类隐写与CRC爆破 \| ①类标号(※标记)、层级深达H6、脚本硬编码例题CRC值 \| PNG文件头与 文件头.md 重复；※宽高/※附加隐写与 图像隐写.md 通用类型节重叠 |
| MISC/图像隐写/图像隐写.md | 8.7KB \| zh \| 图像隐写总览:通用套路+工具隐写(F5/steghide/outguess/盲水印)+LSB全家桶 \| ①类标号(※标记)、疑似过期(cloacked-pixel为python2、频域盲水印脚本是py2语法无法运行) \| 与 README.md 图片隐写节明显重复；与 JPG/PNG/BMP.md 为"总-分"但互有交叉 |
| MISC/数值类.md | 2.6KB \| zh \| 二值化/ASCII还原、一二维数组找规律 \| H1多个(#二值化/#数组)、H1与文件名不符 \| 与 思路打开.md 图片类节主题相近 |
| MISC/文件头.md | 2.9KB \| zh \| 常见文件头magic表+修复文件头思路 \| 无H1、#TODO未完成、事实可疑(wav列"WAVE"而非RIFF头、html列"html>"是文件尾) \| 文件头表与 PNG/JPG/压缩包/思路打开 四处重复 |
| MISC/流量分析.md | 2.2KB \| zh \| Web流量(冰蝎/蚁剑特征)、USB鼠标键盘数位板流量还原 \| H1多个、标题层级乱、空节(##键盘流量无内容) \| 与 ToolManual/Wireshark.md、AWD/AWD.md(webshell/蚁剑)重叠；"网站渗透"3条更像WEB/应急内容 |
| MISC/电子取证.md | 3.6KB \| 混 \| 内存取证Volatility2/3 docker封装、磁盘取证VeraCrypt \| 无H1、空节(VolProGui/MemProcFS)、疑似过期(阿里云盘分享链接已失效) \| 工具与 ToolsList.md 内存取证表完全重复 |
| MISC/编码类.md | 0.7KB \| zh \| 仅Base64一段介绍的占位 \| 空文件/极简、H1与文件名部分不符 | README.md 有链接指向此文件但内容远少于 README/思路打开 的编码节；与 CRYPTO/Encoding.md 主题重叠 |
| MISC/镜像分析.md | 0.8KB \| zh \| WinHex文件恢复+VMDK转VHDX \| 无H1、疑似过期(Microsoft Virtual Machine Converter已停役,下载链接失效) \| 与 ToolManual/VMware.md 同属虚拟化主题 |
| MISC/音频隐写.md | 0.9KB \| zh \| 音频隐写套路/private bit/WAV/SSTV提纲 \| 无H1、H1多个、标题层级乱、裸URL(2处)、空节(###工具) \| SSTV/套路与 思路打开.md 部分思路相近 |

### Hacker（2）

| 文件 | 记录 |
|---|---|
| Hacker/代理解密.md | 6.3KB \| zh \| 微信视频号抓流+Isaac64/wasm解密+aardio实现(个人逆向项目记录) \| H1与文件名不符(#视频号解密)、疑似过期(硬编码wasm版本号1.2.50,接口改版即失效)、非CTF内容放错域 \| 无；主题孤立 |
| Hacker/软件破解.md | 1.3KB \| zh \| Navicat15/16试用重置与Writage注册表脚本 \| 标题层级乱、第一个bat块误标```bash、非CTF内容放错域 \| 无 |

### ToolManual（6）

| 文件 | 记录 |
|---|---|
| ToolManual/010Editor.md | 1.4KB \| zh \| 010Editor模板改值/校验和/文件大小用法与排错 \| 无 \| 与 思路打开.md(010粘贴hex)、ToolsList.md(winhex/ImHex替代行)互补 |
| ToolManual/Burpsuite.md | 0.4KB \| zh \| Burp抓本地回环/证书/代理排错 \| 代码块无语言、空文件/极简 \| ToolsList.md WEB>抓包 有BurpSuite破解链接,两处未互链 |
| ToolManual/CyberChef.md | 1.0KB \| 混 \| CyberChef ASCII互转/Fork/XOR与凯撒爆破 \| 无 \| 与 ToolsList.md 编码/加密表、思路打开.md(Cyberchef magic)功能重叠 |
| ToolManual/VMware.md | 0.5KB \| zh \| VMware三种网络模式与嵌套虚拟化排错 \| 空文件/极简、非CTF专用工具 \| 与 MISC/镜像分析.md 虚拟化主题相邻 |
| ToolManual/Wireshark.md | 4.0KB \| zh \| Wireshark过滤器/tshark提取/ARP/统计与流追踪 \| 事实可疑("ip.src_host"疑非标准显示过滤器字段,通用写法为ip.src) \| 与 MISC/流量分析.md 主题互补但pcap提取两处讲 |
| ToolManual/Xdbg.md | 0.2KB \| zh \| 仅一条52pojie参考链接的占位 \| 空文件/极简 \| 与 ToolsList.md 逆向>反汇编 Xdbg 行重复(仅链接vs表行) |

### 应急响应（1）

| 文件 | 记录 |
|---|---|
| 应急响应/常见思路.md | 9.3KB \| zh \| 应急响应流程+Linux入侵排查10步+Web/数据库日志分析 \| ①类标号(中文序号)、代码块无语言、标题层级乱、外链图片(见§3)、事实可疑(".base_hittory"应为.bash_history、"hithut.v1"等疑为转载OCR错字)、疑似过期(360星图/M1环境旧文表述) \| 与 AWD/AWD.md 防御章高度重叠 |

### CTF 根散文件（3）

| 文件 | 记录 |
|---|---|
| README.md | 10.0KB \| 混 \| 名为README实为MISC/AWD/CRYPTO/WEB杂烩速查 \| H1多个(4)、裸URL(8处)、标题层级乱、文件名与内容定位不符 \| 重灾区:PBE/U2FsdGVkX1与CRYPTO/PBE.md重复、栅栏/当铺与CRYPTO/CTF.md重复、NTFS/图片隐写与MISC/压缩包.md、MISC/图像隐写.md重复(grep证实) |
| ToolsList.md | 29.1KB \| 混 \| 全域软件清单:CTF工具+Linux/Windows/效率/AI等通用软件 \| H1多个(16)、疑似过期(52pojie破解版Burp链接、Ciphey已停更、Python环境清单陈旧)、空尾节(#Linux环境无内容)、标题层级乱(Audio/Novel/Video等挂在#Windows下) \| 与 ToolManual/* 定位重叠；PWN节放的VolatilityPro实为MISC内存取证工具放错节 |
| 思路打开.md | 3.8KB \| zh \| MISC解题思维:特征识别、base换表、文件修复、暴力搜索关键字 \| H1多个(6个)、H1与文件名不符(#思维活跃)、标题层级乱 \| 与 README.md 套路节、MISC/数值类.md、MISC/文件头.md、MISC/编码类.md 多处主题交叉 |

## 二、目录画像

| 目录 | 画像 | 命名 |
|---|---|---|
| AWD | 教程+cheatsheet 混合；"Linux易忽略点"实为通用Linux笔记 | 主题词命名；无模板痕迹 |
| MISC | 主题cheatsheet按题型切分；图像隐写子目录"总-分"结构；大量半成品提纲 | 主题词+格式缩写；无writeup |
| Hacker | 个人逆向/破解项目记录，均与CTF无关 | 中文主题词 |
| ToolManual | 工具使用手册，质量参差 | 工具名；Burpsuite/Xdbg拼写与官方不一致 |
| 应急响应 | 单文件教程/排查清单（整合自外部转载文章） | 主题词 |
| CTF根 | README=杂烩速查、ToolsList=全域软件清单、思路打开=MISC思维笔记——三者均非"索引"职能 | 无模板 |

**范围内 29 个文件 0 个符合 writeup 模板；全部为知识/工具笔记形态。**

## 三、笔记→笔记内部链接

仅 1 条：`CTF/README.md` → `CTF/MISC/编码类.md`（有效）。其余互链为零；总览未链分文件、分文件无反链。

## 四、图片引用异常

- 全部本地图片为相对路径 `../attachments`、`../../attachments`，无绝对路径，**引用均能找到文件**。
- 异常 1 处：`应急响应/常见思路.md` L360 外链图片 `https://img2023.cnblogs.com/...png`（离线失效风险）。
- attachments 内两种命名风格并存：`Pasted image YYYYMMDD...` 与 `hash名.png`。

## 五、>20KB 大文件：ToolsList.md（29.1KB，16 个 H1）

H1：学习资源/环境/MISC/WEB/PWN/逆向(Reverse)/Linux/笔记/Git/Windows/AI/Game/Browser Add-on/Android/Python环境/Linux环境。

H2 结构（按所属 H1 归组）：
- MISC：压缩包、图片、文件、编码/加密、内存取证
- WEB：目录扫描、漏洞扫描、抓包、其他、SSH/SFTP/FTP
- 逆向(Reverse)：反汇编、反编译
- Windows：开发、硬件、其他、效率、Audio、Novel、Video、中间件管理、UI

拆分建议：CTF 相关的 MISC/WEB/逆向三节留 CTF 域并按 H2 拆为独立清单；Linux/笔记/Git/Windows/AI/Game/Browser Add-on/Android/Python环境 共 9 个 H1 与 CTF 无关，应整体迁出至 SoftwareManual 类区域。

## 六、组织问题汇总

1. README.md 定位失守（索引名/杂烩内容，与多文件重复）——应改为纯目录索引。
2. 工具信息三处并存：ToolsList.md（清单）、ToolManual/*（手册）、AWD/工具.md——边界未定义。
3. 放错位置：Hacker/ 整目录非 CTF；AWD/Linux易忽略点.md 是通用 Linux 笔记；MISC/流量分析.md"网站渗透"节；ToolsList.md PWN 节下的 VolatilityPro。
4. 命名不一致：文件名与 H1 不符 5 处；Burpsuite/Xdbg 与官方名不一致；中文目录与英文目录混用。
5. 极简/占位文件 6 个：漏洞.md(119B)、Xdbg.md(186B)、BMP.md(255B)、Burpsuite.md(440B)、VMware.md(472B)、编码类.md(685B)。
6. 重叠三组（去重优先级）：① README.md ↔ 各分类子目录；② 应急响应 ↔ AWD 防御章；③ 文件头 magic 表 4 处重复。
7. 自制标记体系两套：`※` 前缀与"一、二、三、四"中文序号；`文件头.md` 遗留 `#TODO`；`思路打开.md` 文件名口语化。
