# 盘点：CTF/Crypto+Reverse+Pwn+Web（31 文件）

> 来源：治理阶段 A 探查子代理，2026-09-30。此后文件如有变动以 git 记录为准。

范围：`CTF/{CRYPTO,Reverse,PWN,WEB}`，共 31 个 .md（CRYPTO 13、Reverse 3、PWN 1、WEB 14）。

## 一、逐文件清单

格式：`相对路径 | KB | 语言 | 主题 | 问题标记 | 重叠提示`

### CRYPTO（13）

| 记录 |
|---|
| `CTF/CRYPTO/CTF.md` \| 45.3 \| zh(密码名en) \| 古典密码/趣味编码巨型速查表（84 个条目：特征+测试数据+参考链接） \| 无H1、标题层级乱(9 个空`## `标题、1 个空链接`[vowel]()`)、代码块无语言(160/160) \| 与 Encoding.md 同为编码速查；古典密码部分重叠 密码种类与特征.md；RSA-crack 节重叠 RSA*.md；steg base32/64 属 MISC 隐写 |
| `CTF/CRYPTO/Encoding.md` \| 17.8 \| zh(术语en) \| 编码速查表：Base 家族/进制表示/其他编码/字符编码(Unicode-UTF8-BOM) \| H1多个(4)、代码块无语言(98/98) \| 与 CTF.md 互补但主题同域（base 系在两文件均有）；字符编码部分偏计算机基础 |
| `CTF/CRYPTO/PBE.md` \| 1.1 \| zh \| 基于密码加密(PBE)的 openssl 密文特征与 CryptoJS 算法对应表 \| 无H1(纯文本开头) \| AES/DES 部分与 密码种类与特征.md 相邻 |
| `CTF/CRYPTO/Practice_Cryptograph.md` \| 1.6 \| zh \| JWT 三段结构(header/payload/signature)入门笔记 \| 无H1(直接H2)、代码块无语言(10/12，且示例误标 css/bash)、文件名拼写错误(Cryptograph→Cryptography) \| JWT 主题也常见于 WEB 域，存在归类歧义 |
| `CTF/CRYPTO/RSA.md` \| 0.1 \| zh \| RSA 工具(sagemath)+两条公式，近乎空壳 \| 空文件/极简、H1多个(2)、"理论"H1下仅有孤立### 费马小定理 \| 与 RSA理论知识.md 高度重叠（费马小定理重复），应合并 |
| `CTF/CRYPTO/RSA理论知识.md` \| 6.1 \| zh \| RSA 数论基础：逆元/模运算/定理汇总表/CRT 代码 \| 无H1、含wikilink(2 处图片嵌入且目标文件缺失)、代码块无语言(5/6) \| 与 算法性质.md 大面积重复（模运算、欧几里得、扩欧、费马小定理、威尔逊）；与 RSA.md 重复 |
| `CTF/CRYPTO/伪随机数.md` \| 0.4 \| zh \| MT19937 梅森旋转预测要点（2 句话+1 链接） \| 空文件/极简 | 无 |
| `CTF/CRYPTO/公钥密码密钥格式.md` \| 16.5 \| 混(大段en原文) \| ASN.1/PKCS/X.509/PEM 密钥格式教程+私钥 hex 逐字节解析 \| H1多个(5，标题自带"1./2."编号)、标题层级乱(H4"例子"嵌在公钥节内)、代码块无语言(16/24，其余误标 vbnet/ruby)、事实可疑：称"RFC 2347 中可得到 RSA 私钥 ASN.1 定义"——RFC 2347 实为 TFTP 选项扩展，RSA 私钥 ASN.1 应为 RFC 8017(PKCS#1)；且"### PKCS #1 RSA Public Key"小节内容实为私钥结构解析（题文错位）；作者自注"3082 应该指私钥(不确定)" | 无 |
| `CTF/CRYPTO/学习资料.md` \| 0.1 \| zh \| 仅 2 条 cryptohack 链接（1 条纯文本 URL） \| 空文件/极简、无H1 \| 链接与 算法性质.md 重复（同一 flipping_cookie 链接） |
| `CTF/CRYPTO/密码攻击方式.md` \| 2.2 \| zh \| 密码分析四种攻击模型(COA/KPA/CPA/CCA)与安全性 \| H1多个(3)、标题层级乱(H1→###)、"RSA具体攻击方式"H1 为空节、事实可疑("Ciphtext"→Ciphertext 拼写) \| "已知明文攻击"概念与 算法性质.md 重复 |
| `CTF/CRYPTO/密码种类与特征.md` \| 4.0 \| zh \| 古典密码分类(替换/置换)与 AES/CBC/ECB 特征 \| H1多个(2)、标题层级乱(### 多表代换→直接##### Playfair) \| Playfair/Vigenere/Polybius/Nihilist 条目与 CTF.md 重复；AES/CBC 与 PBE.md、算法性质.md 相邻 |
| `CTF/CRYPTO/算法性质.md` \| 3.2 \| zh(术语en) \| XOR 性质+CBC 翻转攻击(bit flip)+模运算/GCD/扩欧 \| H1多个(3)、标题层级乱(H1→###)、代码块无语言(2/4) \| 与 RSA理论知识.md 高度重复；cryptohack 链接与 学习资料.md 重复；XOR 已知明文攻击脚本思路与 WEB/Python.md 重复 |

### Reverse（3）

| 记录 |
|---|
| `CTF/Reverse/Reverse.md` \| 1.7 \| zh \| Unity(Il2CppDumper)/IDA/xdbg 逆向工具操作笔记 \| 4 处图片路径多一级 `../`（`../../../attachments/` 指向库外）；其中 65fd3bdb….png 在库根 attachments 也不存在（双重失效） \| 与 PE逆向.md 同为桌面逆向主题 |
| `CTF/Reverse/PE逆向.md` \| 0.9 \| 混(概念段zh+OEP行en) \| PE 文件格式概念两段+OEP 一句话 \| 空文件/极简 | 与 Reverse.md（IDA/xdbg 桌面逆向）相邻，可合并 |
| `CTF/Reverse/Andorid逆向.md` \| 6.1 \| zh \| Android 逆向：CPU 架构/Dalvik/Smali/ADB/Frida hook/Jadx/脱壳 \| 文件名拼写错误(Andorid→Android)、4 处图片路径多一级 `../`（图片本身在库根 attachments 存在）、代码块无语言(3/6) | 无 |

### PWN（1）

| 记录 |
|---|
| `CTF/PWN/基础.md` \| 1.5 \| zh \| pwntools 两个报错规避+checksec/NX//bin/sh 概念 \| 文件名"基础"过泛；目录仅此 1 文件 | 无（PWN 域近乎空置，ROP/堆等主题全缺） |

### WEB（14）

| 记录 |
|---|
| `CTF/WEB/HTTP请求头.md` \| 1.6 \| zh \| 常见请求头作用+CTF 篡改提示(UA/Referer/XFF/Cookie) \| 标题层级乱(H1→####→#####)、"#### 响应头"为空节 | 无 |
| `CTF/WEB/JavaScript.md` \| 0.1 \| zh \| 仅"原型链污染"标题+1 条 CSDN 链接 \| 空文件/极简(占位) | 无 |
| `CTF/WEB/PHP.md` \| 9.8 \| zh(配置段为en原文) \| PHP 语法/弱类型/哈希绕过/php.ini/伪协议(filter 链)/函数绕过教程 \| H1多个(7)、标题层级乱(H1→####)、代码块无语言(9/16)、疑似过期信息(magic_quotes_gpc 仅称 deprecated，实际 PHP 5.4 已移除)、rot13 实验结论为"似乎/可能"的个人推测 \| 伪协议/allow_url_include 与 文件包含.md 重复；高危函数与 代码与命令执行.md 重复；"绕过"节与 绕过(Bypass).md 重复 |
| `CTF/WEB/Python.md` \| 4.8 \| zh \| 混杂：WAF 绕过+Python 内置函数+字符串前缀/位运算+自制 XOR 脚本 \| H1多个(7)、代码块无语言(7/14)、主题错位(字符串前缀/位运算属 Python 语言基础，"from pwn import xor"属 PWN，XOR 脚本属 CRYPTO) \| XOR 密钥恢复脚本与 CRYPTO/算法性质.md 同源；"反序列化"与 解析漏洞.md 重复 |
| `CTF/WEB/SSRF.md` \| 2.3 \| zh(部分en原文) \| SSRF 概念+Gopher/File 协议格式与语言支持限制 \| 标题层级乱(## →####)、代码块无语言(1/2)、事实可疑("--wite-curlwrappers"→--with-curlwrappers 拼写；支持情况表为老版本经验，PHP/Java 版本信息过旧) | File 协议与 PHP.md file:// 伪协议相邻重叠 |
| `CTF/WEB/WEB.md` \| 0.4 \| zh \| 查看网页源码技巧(view-source:F12 展开快捷键) \| 空文件/极简、标题层级乱(H1"工具"→###) \| 命名与目录同名，作为 WEB 域入口却无索引内容 |
| `CTF/WEB/代码与命令执行.md` \| 1.2 \| zh \| RCE 概念+PHP 高危函数总览+动态调用 \| 标题层级乱(H2→####)、代码块无语言(2/4)、事实可疑("pctnl_exec"→pcntl_exec 拼写) \| 高危函数与 PHP.md 重复；RCE 术语与 Python.md 重复 |
| `CTF/WEB/信息收集.md` \| 0.5 \| zh \| 目录扫描(dirsearch)/robots.txt/备份文件后缀 \| 空文件/极简、"Linux服务器信息收集"H1 为空节、备份后缀列表 `.svn` 重复列两次 | 无 |
| `CTF/WEB/前端审计.md` \| 0.6 \| zh \| 浏览器内直接改 JS 并立即生效的调试技巧 \| 空文件/极简(核心是 1 条 CSDN 链接) | 无 |
| `CTF/WEB/提权.md` \| 1.1 \| zh \| Linux 虚拟机破解密码+find 按时间查文件 \| H1多个(3)、"环境变量"H1 为空节、位置可疑(Linux 后渗透/主机安全，非 WEB 漏洞主题) | 与 CTF/Hacker、CTF/应急响应 域主题更相关 |
| `CTF/WEB/文件包含.md` \| 1.1 \| zh \| LFI/RFI 术语+PHP include 四函数差异 \| H1多个(2)、标题层级乱(H1→####)、代码块无语言(1/2)、事实可疑("E_warinng"→E_WARNING 拼写) \| allow_url_include 与 PHP.md、RFI 与 代码与命令执行.md 的 LFI→RCE 相邻重叠 |
| `CTF/WEB/模板注入.md` \| 0.6 \| zh \| SSTI 概念+Flask-Jinja2+绕 WAF 工具(Fenjing) \| 空文件/极简(概念 1 段+2 链接) | "绕过"主题与 绕过(Bypass).md、Python.md 相邻 |
| `CTF/WEB/正则表达式.md` \| 7.7 \| 混(大段en解释) \| 正则"艰深写法"示例+语法/替换/环视速查表 \| H1多个(2)、标题层级乱(H1→####)、代码块无语言(1/2)、语法表约 2/3 为空单元格（未填完的骨架） \| 通用编程主题，与 MISC/CTF.md 数字隐写的正则示例相邻 |
| `CTF/WEB/绕过(Bypass).md` \| 0.4 \| zh \| 双写/双重编码/ROT13 响应绕过 \| 空文件/极简、"双重编码绕过"H2 为空节、命名风格不一致(唯一带英文括号注释的文件名) \| 与 PHP.md"绕过"节、Python.md WAF 绕过、模板注入.md 绕 WAF 主题交叉 |
| `CTF/WEB/解析漏洞.md` \| 1.2 \| 混(XML段为en原文) \| XML 实体攻击(billion laughs/XXE)+YAML/Pickle 反序列化占位 \| H1多个(3)、"YAML解析漏洞""Pickle反序列化漏洞"两节均空 | Pickle 与 Python.md"反序列化"、文件名"解析漏洞"与内容(实际是注入类漏洞)不完全对应 |

> 全域共性：裸URL 0 处；①类标号 0 处；无 writeup 类时间敏感内容，"疑似过期信息"仅 PHP/SSRF 版本相关两处。

## 二、目录画像与命名

| 目录 | 画像 | 命名 |
|---|---|---|
| CRYPTO | 速查表+理论笔记为主：两份大速查 + 数论/格式理论 + 多个近空占位。无 writeup | 中英混杂；`CTF.md` 与顶层目录同名易混淆；`Practice_Cryptograph` 拼写错误 |
| Reverse | 工具操作笔记+概念。教程性质，非 writeup | 纯主题名；`Andorid逆向.md` 拼写错误 |
| PWN | 仅 1 个入门文件，域近乎空置 | `基础.md` 过泛 |
| WEB | 漏洞类型词条笔记集合，多数 0.4–2KB，深度不足；PHP.md 为唯一较完整教程 | 纯主题名，中英混合；`绕过(Bypass).md` 唯一带括号注释；`WEB.md` 与目录同名 |

**结论：4 个目录均不遵循 `YYYYMMDD_分类_标签_时长_题目名` writeup 模板**——均为知识主题型笔记。

## 三、笔记→笔记内部链接

范围内 31 个文件之间：**0 条**。反向也无任何文件链接进来。整个四子域是"孤岛"：无 MOC、无互链、无反链。

## 四、图片引用异常（15 处引用，9 处异常）

正常 5 处（CTF.md×2、PWN/基础.md、WEB/PHP.md、密码种类与特征.md）。

异常 9 处：
1. 路径多一级 `../`（全部失效）：`Reverse/Reverse.md` 4 处、`Reverse/Andorid逆向.md` 4 处（`../../../attachments/`）。其中 7 张图修掉一层 `../` 即可恢复；`Reverse.md` 的 `65fd3bdf0ce8572a5cc835fc357c2c74.png` 彻底丢失。
2. wikilink 嵌入+目标缺失：`RSA理论知识.md` 2 处 `![[attachments/Pasted image ...]]`（20231106/20231201 前缀不存在），已失效。

## 五、>20KB 大文件：CTF.md（45.3KB，1266 行，84 个 H2）

按自然分组拆分建议：
- 替换密码：a1z26, affine, asciiSum, atbash, autoKey, bacon24/26, beaufort, bifid, caeser(拼写应为 caesar), gronsfeld, hill, playFair, porta, qwe, rot5/13/18/47/8000, virgenene(拼写应为 vigenere), vowel, oneTimePad, curveCipher/railFence(置换类)
- 棋盘/坐标类：ADFGVX, ADFGX, baudot, morse, polybius, nihilist, fourSquare, trifid, TapCode, braille, handyCode
- 程序语言混淆：aaencode, jjencode, brain fuck, Ook, troll script, rabbit
- 趣味/中文编码：与佛论禅系, 新佛曰, 熊曰, 兽音, 阴阳怪气, 六十四卦, 天干地支, 百家姓, socialCoreValue, cetacean, emojiSubstitute, DNA, 01248(云影), FenHam, pawnShop(当铺), periodicTable, grayCode, Twin Hex, bubbleBabble, 零宽系
- 错置条目：RSA-crack（属 RSA 主题）、steg base32/64（属 MISC 隐写）、base64CaseCrack（与 Encoding.md 同域）
- 结构垃圾：9 个空 `## ` 标题、`[vowel]()` 空链接标题

## 六、组织问题汇总

1. 互链为零/全域孤岛——治理首要项。
2. 命名拼写错误：Andorid、Practice_Cryptograph、caeser、virgenene、pctnl_exec、E_warinng、--wite-curlwrappers、Ciphtext 等。
3. 应合并：RSA.md→RSA理论知识.md；算法性质↔RSA理论知识；密码种类与特征↔CTF.md；PHP.md↔文件包含↔代码与命令执行↔绕过(Bypass) 四者交叉。
4. 放错位置：WEB/Python.md 一半是 Python 语言基础；WEB/提权.md 是 Linux 后渗透；CTF.md 的 steg 条目属 MISC；Encoding.md 字符编码章偏计算机基础。
5. 空节/占位文件多处（见逐文件标记）。
6. 标题规范差：6 文件无 H1、14 文件多 H1、普遍跳级。
7. 代码块几乎全部无语言标注（CTF.md 160/160）。
8. 图片路径系统性错误（Reverse 8 处 `../../../`）与 3 张彻底丢失图片。
9. CTF.md 体量与命名问题（45KB 平铺 84 条目 + 与顶层目录同名）。
10. PWN 域空置（覆盖缺口）。
11. AI/外部粘贴痕迹：正则表达式、PHP、SSRF、解析漏洞存在大段未消化英文原文，正则语法表 2/3 空白。
