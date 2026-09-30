# CTF 域格式治理日志（c4 批次 · 格式扫尾）

- 日期：2026-09-30
- 范围：`CTF/` 域全部 52 个 md（治理后 51 个，`Reverse/PE逆向.md` 并入删除）
- 门禁结果：
  - `python _governance/scripts/lint_ctf.py` → **52 PASS / 0 FAIL**（口径：唯一 H1、无跳级、围栏闭合、围栏有语言（text 也算）、无 `※` 前缀标题、无裸 URL）
  - `python _governance/scripts/fixlinks.py` → `DONE: 0 links fixed`
  - `python _governance/scripts/checklinks.py` → `all links OK`
- 中断恢复说明：上次会话中断时 `CTF/Misc/压缩包.md`、`CTF/Misc/图像隐写/PNG.md`、`CTF/Misc/文件头.md`、`CTF/Misc/解题思路.md` 已完成修改。本次逐一核查确认其已合规（唯一 H1、层级、待补充标注、`RIFF` 魔数修正、`html>` [文件尾] 标注均到位），**除解题思路.md 补一处错字（存粹→纯粹）外未重复改动**。

## 一、修复清单（文件 | 修复项）

### 中断恢复核查（未重复改动）

| 文件 | 说明 |
|---|---|
| Misc/压缩包.md | 上次会话已完成：唯一 H1、层级、待补充、锚点链接；本次核查跳过 |
| Misc/图像隐写/PNG.md | 上次会话已完成：`※` 标题规整、H6 压缩至 H4、例题 CRC 保留；核查跳过 |
| Misc/文件头.md | 上次会话已完成：唯一 H1、`#TODO`→待补充、WAVE→`RIFF` 修正、`html>`[文件尾] 标注；核查跳过 |
| Misc/解题思路.md | 上次会话已完成：唯一 H1「Misc 解题思路」；本次仅补错字 存粹→纯粹 |

### CTF/Misc

| 文件 | 修复项 |
|---|---|
| 流量分析.md | 补唯一 H1「流量分析」；`常见流程`→H2（网站渗透→H3）、`Web流量`/`USB流量` H1→H2 及子节降级、冰蝎/蚁剑 H4→H3；空「键盘流量」节加待补充 |
| 二维码.md | H1「结构」→「二维码」；`格式和版本信息` H1→H2（英文原文保留未译） |
| 数值类.md | H1「二值化」→「数值类」（原 H1 降为 H2）；`数组`/`数字隐写`降级；一维/二维数组及其子节层级归位 |
| 电子取证.md | 补唯一 H1「电子取证」；`内存取证`/`磁盘取证` H1→H2 及全部子节降级；空 VolProGui/MemProcFS 节加待补充；winvol 链接(404)与 CSDN Volatility3 文(521×2) 标注[链接已失效]；新增 `${@:2}` 待事实核查 callout（见说明） |
| 镜像分析.md | 补唯一 H1「镜像分析」；`VMDK转VHDX` H4→H3；theitbros 裸 URL 改 md 链接；MVMC 下载链接(502)标注[链接已失效] |
| 音频隐写.md | `## 音频隐写` 升为唯一 H1；WAV/SSTV H1→H2；SSTV 下 `##### 工具`→H3；空「工具」节加待补充；2 个裸 autolink 改 md 链接 |

### CTF/Web

| 文件 | 修复项 |
|---|---|
| PHP.md | 7 个 H1→唯一 H1「PHP」全文件层级重构（伪协议/绕过/参考资料各归其位）；协议列表代码块补 `text`；行内 `http://www.baidu.com` 加反引号；magic_quotes_gpc 表述按事实修正（PHP 5.3.0 弃用、5.4.0 移除）；rot13 代码注释「似乎/可能」个人推测改中性表述 |
| SSRF.md | 补唯一 H1「SSRF」；`协议`→H2（Gopher/File→H3）；`--wite-curlwrappers`→`--with-curlwrappers` |
| 文件包含.md | H1「术语」→「文件包含」；`(E_warinng)`→`(E_WARNING)`；RFI 节 H4→H3 |
| 代码与命令执行.md | H1「概念」→「代码与命令执行」；`pctnl_exec()`→`pcntl_exec()`；高危函数总览/动态代码执行降为 H3 |
| 解析漏洞.md | 补唯一 H1「解析漏洞」；XML/YAML/反序列化 H1→H2 及子节归位；空 YAML 节与 Pickle 节加待补充（保留参考链接） |
| HTTP请求头.md | `#### 请求头`→H2、全部 `#####` 请求头→H3；空「响应头」节补常用响应头简表（Content-Type/Server/Set-Cookie/Location/Access-Control-\* 共 7 行，通用常识） |
| 信息收集.md | H1「目录扫描」→「信息收集」；备份后缀列表去重（删重复的 `.svn`，保留 NBSP 原样）；`Linux服务器信息收集` H1→H2 及子节归位 |
| JWT.md | 补唯一 H1「JWT」（原 H2 链接标题改为文首普通引用行）；`css` 误标→`text`、`bash` 误标→`json`、4 个无语言块补 `text`/`json`；header/payload/signature H3→H2 |
| 绕过技巧.md | 空「双重编码绕过」节加待补充（H1「绕过方式」语义等同文件名，保留不改） |
| 前端审计.md / JavaScript原型链污染.md / SSTI-模板注入.md | 核查合规（唯一 H1、无跳级、围栏正常），未改动 |

### CTF/Crypto

| 文件 | 修复项 |
|---|---|
| 公钥密码密钥格式.md | 5 个「1./2.」编号 H1→唯一 H1「公钥密码密钥格式」；各节编号去除、层级归位；H4「例子」→H5 归位；`vbnet`/`ruby` 误标及无语言块共 10 处→`text`；文末后缀说明规整为标准有序列表；RFC 2347 处加待事实核查 callout（原文未改） |
| 密码攻击方式.md | 3 H1→唯一 H1「密码攻击方式」；空「# RSA具体攻击方式」节改为一句话+链接 [RSA与数论](RSA与数论.md)；`Ciphtext`→`Ciphertext`；「唯密文攻击(COA」补缺失右括号 |
| 密码种类与特征.md | H1「古典密码」→「密码种类与特征」全文件层级归位（Playfair 跳级、CBC 跳级修复）；空「单表代换加密」节加待补充；`Transposi-tionCipher`→`Transposition Cipher`（补全角括号）；`PCKS5`/`PCKS7`→`PKCS5`/`PKCS7` |
| PBE.md / 伪随机数.md | 核查合规（唯一 H1、种子条目两句话保留），未改动 |
| 古典密码速查 / 趣味编码速查 / 编码速查 / RSA与数论 / XOR与CBC攻击 / 哈希长度扩展攻击 | 快速核查合规（唯一 H1 + 围栏语言齐全），未改动 |

### CTF/AWD

| 文件 | 修复项 |
|---|---|
| AWD.md | 章节按语义归位：`防利用`、`防检测防删除`（含后门加密码/流量混淆/混淆/困难删除/时间变化）移入「防御」章；`不死马`（含内存马）移入「攻击」章为 H3；`上传`、`反弹Shell` 保留在攻击章 |
| 工具.md | `php:7.2-apache` 镜像加「历史镜像标签」时效注（代码注释形式）；Metasploit 节加待补充 |
| 提权.md | 3 H1→唯一 H1「提权」；空「# 环境变量」节删除（无内容无计划，留痕见下） |
| Linux要点.md | 核查合规未改动（唯一 H1「Linux 易忽略点」语义等同文件名；`${@:2}` 表述实际位于 Misc/电子取证.md，callout 已加在该处，见待核查清单） |

### CTF/IncidentResponse

| 文件 | 修复项 |
|---|---|
| 常见思路.md | `chattr` 代码块补 `bash`；`.base_hittory`→`.bash_history`；正文（1）（2）/(1)(2) 类序号改 Markdown 有序列表共 5 处（Web应用三条、第 6 节两条、第 8 节两法、第 10 节三目录）；「一、二、三、四」H2 按要求保留；`hithut.v1/v2` 与 `hihub/hithub` 疑 OCR 错字加 2 个待事实核查 callout（原文不改）；cnblogs 外链图片本地化为 `attachments/cnblogs-2727822-20221130150433299-140184437.png`（`file` 验证为有效 PNG 548x176 RGBA，魔数 `89504e470d0a1a0a`）并补 alt 文本；「360星图/M1/VS Code 插件」加时效注；「**待补充。。。**」规范为斜体待补充标注 |

### CTF/Toolbox

| 文件 | 修复项 |
|---|---|
| BurpSuite.md | 127.0.0.1/::1/localhost 清单代码块补 `text` |
| Wireshark.md | `ip.src_host`/`ip.dst_host` 加待事实核查 callout（原文不改） |
| 010Editor.md / CyberChef.md / 工具清单.md | 核查合规，未改动 |

### CTF/Hacker

| 文件 | 修复项 |
|---|---|
| 软件破解.md | 3 个 Windows 批处理块 `bash`/`sh`→`bat`（任务点名第一个，另两处同性质一并修）；`##### navicate15/16`、`##### writage` 跳级修复→H2；拼写 `navicate`→`Navicat`、`writage`→`Writage` |
| 视频号代理解密.md | H1「视频号解密」→「视频号代理解密」（与文件名一致）；监听器 H3→H2、监听/解密/aardio H4→H3；wasm 版本 `1.2.50` 硬编码 URL 加时效注 |

### CTF/Reverse / Pwn

| 文件 | 修复项 |
|---|---|
| PE逆向.md | 0.9KB 全文（概念两段 + OEP 句）并入 `Reverse.md` 新增「## PE 文件格式」节（附来源注），`git rm` 原文件 |
| Reverse.md | 新增「## PE 文件格式」节；其余核查合规 |
| Android逆向.md | 核查合规（3 处代码块均已带 `sh` 标注），未改动 |
| Pwn/基础.md | 核查合规（唯一 H1「PWN基础」），未改动 |

### 索引与工具

| 文件 | 修复项 |
|---|---|
| CTF/README.md | Reverse 行移除已删除的 `PE逆向.md` 链接，定位描述补「PE 文件格式」 |
| _governance/scripts/lint_ctf.py | 新增「多 H1」错误检查（原版只查无 H1）；「H1≠文件名」降级为 note 不计 FAIL（对齐门禁口径「唯一 H1」；README/解题思路 等特例靠此放行） |

## 二、待事实核查 callout 清单（供阶段 D）

| # | 文件 | 问题 |
|---|---|---|
| 1 | CTF/Crypto/公钥密码密钥格式.md | 「在 RFC 2347 中，我们可以得到 RSA 私钥的 ASN.1 定义」——RFC 编号疑应为 **RFC 8017 (PKCS#1)**；RFC 2347 是 TFTP Option Extension。原文未改。 |
| 2 | CTF/Misc/电子取证.md | 「`"${@:2}"` ... treats them as a single string」——bash 中 `"${@:2}"` 展开为**多个独立参数**，并非单个字符串。（注：任务清单将此条列于 AWD/Linux要点.md，该表述实际位于本文件 Volatility3 节，callout 已按实际位置添加） |
| 3 | CTF/Toolbox/Wireshark.md | `ip.src_host`/`ip.dst_host` 疑非标准显示过滤器写法，标准写法为 `ip.src`/`ip.dst`。原文未改。 |
| 4 | CTF/IncidentResponse/常见思路.md | `hithut.v1`/`hithut.v2` 疑 OCR 错字（示例输出文件名，内部引用一致，语义不受影响）。 |
| 5 | CTF/IncidentResponse/常见思路.md | `hihub`/`hithub` 同一示例文件名三处拼写不一致，疑原文转录错字，原文件名不可考。 |

## 三、失效链接实测标注

| 文件 | 链接 | 实测 |
|---|---|---|
| Misc/电子取证.md | `https://www.forensics-wiki.com/volatility/winvol.html` | 404 |
| Misc/电子取证.md | `https://blog.csdn.net/Aluxian_/article/details/127064750` | 521（间隔复测两次） |
| Misc/镜像分析.md | `http://download.microsoft.com/.../mvmc_setup.msi` | 502 |

其余链接实测 200；`book.hacktricks.xyz` 403 为反爬（站点存活），未标失效；aliyundrive 200 未标。

## 四、拼写修正留痕（逐条）

| 原文 | 修正 | 文件 |
|---|---|---|
| `E_warinng` | `E_WARNING` | Web/文件包含.md |
| `pctnl_exec()` | `pcntl_exec()` | Web/代码与命令执行.md |
| `--wite-curlwrappers` | `--with-curlwrappers` | Web/SSRF.md |
| `Ciphtext` | `Ciphertext` | Crypto/密码攻击方式.md |
| 唯密文攻击(COA【缺右括号】 | 补 `)` | Crypto/密码攻击方式.md |
| `Transposi-tionCipher)` | `Transposition Cipher` | Crypto/密码种类与特征.md |
| `PCKS7` / `PCKS5` | `PKCS7` / `PKCS5` | Crypto/密码种类与特征.md |
| `.base_hittory` | `.bash_history` | IncidentResponse/常见思路.md |
| `navicate15/16` | `Navicat15/16` | Hacker/软件破解.md |
| `writage` | `Writage` | Hacker/软件破解.md |
| `存粹` | `纯粹` | Misc/解题思路.md |

## 五、删除留痕

| 对象 | 理由 |
|---|---|
| AWD/提权.md「# 环境变量」空节 | 无内容、无明确计划，属无意义空节，删除 |
| CTF/Reverse/PE逆向.md | 0.9KB 小文件，内容并入 `Reverse.md`「## PE 文件格式」后 `git rm`（README 索引同步更新） |

## 六、事实性表述修正留痕（非拼写，按任务授权）

| 文件 | 修正 |
|---|---|
| Web/PHP.md | magic_quotes_gpc：由「now deprecated」改为「deprecated in PHP 5.3.0 and removed in PHP 5.4.0」（任务指定口径） |
| Web/PHP.md | rot13 代码注释「似乎只对…？」「可能这就是因为」→ 中性陈述「只对…」「这是因为」 |
| Misc/文件头.md | （上次会话）wav 魔数 WAVE→`RIFF`、`html>` 标注[文件尾] |

## 七、lint 结果

`python _governance/scripts/lint_ctf.py`（更新版：多 H1 检查 + 门禁对齐）：

```text
TOTAL 52 files, 0 FAIL, 52 PASS
```

全部 PASS。H1 与文件名不完全一致但语义等同而保留的文件（lint note，不计 FAIL，共 13 个）：`CTF/README.md`（CTF）、`CTF/Crypto/README.md`（Crypto）、`AWD/Linux要点.md`（Linux 易忽略点）、`Hacker/软件破解.md`（试用类）、`IncidentResponse/常见思路.md`（应急响应）、`Misc/解题思路.md`（Misc 解题思路，任务指定）、`Pwn/基础.md`（PWN基础）、`Reverse/Android逆向.md`（Android 逆向）、`Toolbox/BurpSuite.md`（Burpsuite）、`Toolbox/工具清单.md`（CTF 工具清单）、`Web/JavaScript原型链污染.md`（原型链污染）、`Web/SSTI-模板注入.md`（SSTI(Server-Side Template Injection)）、`Web/绕过技巧.md`（绕过方式）。
