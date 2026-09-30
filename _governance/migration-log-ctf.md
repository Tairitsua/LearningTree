# CTF 域内容治理迁移日志（C2 批）

> 执行日期：2026-09-30。前置：C1 机械重组（目录改名 `CRYPTO→Crypto` 等）已完成。
> 原则：`git mv`/`git rm` 保留历史，不 commit（由协调方统一提交）；所有内容操作逐项留痕于本日志。
> 脚本：`_governance/scripts/c2_split_ctf.py`（拆分）、`c2_rework_encoding.py`（编码速查重排）、`c2_verify_ctf_entries.py`（词条核对）。

## T1 拆分 CTF/Crypto/CTF.md（45KB，84 个 H2）

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| git mv 归档 | `CTF/Crypto/CTF.md` | `_archive/CTF/CTF速查-原稿.md`（头部加已拆分说明） |
| 拆分新建 | `CTF/Crypto/古典密码速查.md` | 替换密码 26 词条（a1z26/asciiSum/atbash/affine/bacon24/bacon26/caesar/caesar box/qwe/rot5/rot13/rot18/rot47/rot8000/gronsfeld/vigenere/autoKey/beaufort/porta/oneTimePad/FenHam/hill/playFair/bifid/FracMorse/vowel）+ 棋盘坐标 11 词条（ADFGVX/ADFGX/baudot/morse/polybius/nihilist/fourSquare/trifid/TapCode/braille/handyCode）+ 置换 3 词条（curveCipher/railFence/railFenceW）+ 参考节 |
| 拆分新建 | `CTF/Crypto/趣味编码速查.md` | 程序语言混淆 6 词条（aaencode/jjencode/brain fuck/Ook/troll script/rabbit）+ 中文趣味 17 词条（与佛论禅/与佛论禅加密版/新佛曰/熊曰/兽音/阴阳怪气/六十四卦/天干地支/百家姓/01248/pawnShop/periodicTable/socialCoreValue/cetacean/zwBinary/zwBinary-morse/zwUnicode）+ 其他符号与通信编码 7 词条（DNA/emojiSubstitute/grayCode/Twin Hex/bubbleBabble/Manchester/Manchester-diff） |
| 词条分流 | `RSA-crack` 词条 | → `Crypto/RSA与数论.md`「工具与攻击」 |
| 词条分流 | `steg base32` / `steg base64` 词条 | → `Misc/图像隐写/图像隐写.md` 新增「编码隐写」节 |
| 词条分流 | `base64CaseCrack` 词条 | → `Crypto/编码速查.md` Base家族节（base64Url 之后） |
| 清理 | 9 个空 `## ` 标题 | 删除（脚本统计 84 = 75 实词条（含"参考"节）+ 9 空） |
| 清理 | `[vowel]()` 空链接标题 | 改为正常标题 `vowel` |
| 格式 | 160 条无语言围栏行（80 个代码块，开+关各 80 行） | 全部开栏补 `text`（测试数据性质；盘点口径"160"实为围栏行数） |
| 拼写修正 | `caeser`→`caesar`、`virgenene`→`vigenere` | 标题与正文统一修正；caesar/vigenere 条目内各注一句原拼写留痕 |

## T2 RSA 族合并

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 合并新建 | `CTF/Crypto/RSA与数论.md` | 唯一 H1，分节：数论基础（术语/逆元/模运算/GCD 与欧几里得/扩欧/定理速查表/补充式子/欧拉函数/欧拉定理/费马小定理/威尔逊/中国剩余/欧拉准则与二次剩余）→ RSA 原理 → 工具与攻击（RSA-crack/sagemath） |
| git rm | `CTF/Crypto/RSA.md`（0.1KB 空壳） | 内容（sagemath、`m^e mod n ≡ c`）并入新文件；其费马小定理公式与 RSA理论知识 重复，去重保留完整版 |
| git rm | `CTF/Crypto/RSA理论知识.md` | 主体并入「数论基础」；2 处已丢失图片嵌入（`Pasted image 20231106224355.png`、`Pasted image 20231201154721.png`，库中不存在）删除嵌入行，改为文字备注"[图片已丢失：…]" |
| git rm | `CTF/Crypto/算法性质.md` | 数论部分（术语/GCD/欧几里得/扩欧，含 gcd 代码）与 RSA理论知识 去重合并（取两者并集，英文解释更全的版本保留）；XOR/CBC 部分独立为下条 |
| 合并新建 | `CTF/Crypto/XOR与CBC攻击.md` | XOR 性质/已知明文攻击（含原 Web/Python.md 恢复密钥脚本）/CBC 翻转攻击/`from pwn import xor` 工具说明 |
| git rm | `CTF/Crypto/学习资料.md`（2 条链接） | → `Crypto/README.md`「学习资料」节（见 T6） |

## T3 编码合并

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| git mv + 重排 | `CTF/Crypto/Encoding.md` → `CTF/Crypto/编码速查.md` | 4 个 H1（Base家族/进制表示/其他/字符编码）→ 唯一 H1 + H2 分组；词条 H2→H3；字符集教程小节顺延降级（最深 H5，无跳级） |
| 格式 | 无语言代码块（盘点口径 98，实为 50 个代码块的围栏行计数） | 全部补 `text`，重排后复核剩余 0 |
| 并入 | `Misc/编码类.md` 的 Base64 介绍 | 并入 `编码速查.md` base64 词条（取更完整长版介绍，短句为子集去重；保留对照表图片 `cb26322862eb1aa2f48b58f388ceea28.png`） |
| git rm | `CTF/Misc/编码类.md` | 内容已并入 |

## T4 ToolsList 分流与 README 杂烩分流

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 新建 | `CTF/Toolbox/工具清单.md` | 原 `CTF/ToolsList.md` MISC/WEB/PWN/逆向 四节按方向分节（Misc/Web/Reverse），空表格行清理，裸 URL（blasting）转链接 |
| 调整 | 原 PWN 节的 `VolatilityPro` | 实为内存取证工具（放错节），移入 Misc/内存取证，行内注明 |
| 并入+删除 | `CTF/Toolbox/Xdbg.md`（仅 1 条参考链接） | 链接补入工具清单逆向节 Xdbg 行，git rm |
| 移除链接 | BurpSuite 52pojie 破解版链接 | 备注改为"[破解版链接已移除，历史记录见 git]"，链接本体删除 |
| 并入 | `SoftwareManual/Acunetix.md` 一句话（Administrative Password 重置） | → 工具清单 Web/漏洞扫描节 Acunetix 行（"清单安全节"无现成同名节，按工具属性落位漏洞扫描节；`SoftwareManual/Acunetix.md` 文件本身留待 SoftwareManual 批处理） |
| 标注 | `Ciphey` | 加 **[已停更]** 标注并提示改用 `Ares`（Ciphey 位于 CTF 工具清单而非通用软件清单，标注落在 `Toolbox/工具清单.md`） |
| 新建 | `SoftwareManual/软件清单.md` | 原 ToolsList 学习资源/环境/Linux/笔记/Git/Windows（开发/硬件/其他/效率/Audio/Novel/Video/中间件管理/UI）/AI/Game/Browser Add-on/Android/Python环境 通用章节，按用途分节 |
| 删除留痕 | `# Linux环境` 空节（仅标题） | 删除 |
| 清理 | Python 环境包列表重复行 | `matplotlib`、`python-tk` 各出现两次，去重；列表转为 `text` 代码块 |
| git rm | `CTF/ToolsList.md` | 内容已分流 |
| git mv 归档 | `CTF/README.md`（旧杂烩速查） | `_archive/CTF/README-旧速查-原稿.md`（头部加分流说明；其中指向已删除 `Misc/编码类.md` 的链接改为文字留痕） |

### 旧 README 杂烩内容分流明细

| 原节 | 去向 |
|---|---|
| MISC>套路（开局/收尾/冷门链接） | → `CTF/Misc/解题思路.md` 新增「开局与收尾套路」节 |
| 隐写术>数字隐写（文件时间/正则提取） | → `CTF/Misc/数值类.md` 新增「数字隐写（文件时间）」节 |
| 隐写术>语言混淆（jsfuck/esolangs） | → `CTF/Crypto/趣味编码速查.md`「程序语言混淆」节尾「语言混淆资源」 |
| 隐写术>文本隐写（snow/stegsnow） | → `CTF/Misc/解题思路.md`「文本隐写（snow）」节 |
| 隐写术>文件隐写（NTFS 流） | → `CTF/Misc/压缩包.md` ZIP>隐写>NTFS流隐写（原空节填充，链接转正） |
| 图片隐写>基础/观察/具体格式(PNG)/工具(Stegsolve/UltraEdit) | → `CTF/Misc/图像隐写/图像隐写.md`：观察节 WAV 例图并入「附加隐写」；PNG 数据块图/CRC 校验说明为「PNG 结构速查」节；Stegsolve 功能列表为工具隐写小节；基础链接入「参考资料」节 |
| AWD 节（cnblogs 套路 + awd-cmd 链接） | → `CTF/AWD/AWD.md` 新增「参考」节 |
| CRYPTO>DES加密 | → `CTF/Crypto/密码种类与特征.md` 分组密码下新增 DES 节（任务未明示，按主题就近归位） |
| CRYPTO>PBE/U2FsdGVkX1/口令/密钥/加盐 | → `CTF/Crypto/PBE.md`（重写：补唯一 H1、原理与算法对应分节，与原有 `U2FsdGVkX1` 特征行去重） |
| CRYPTO>栅栏密码 | → `古典密码速查.md` railFence 词条（补加密/解密方法，与 railFenceW 互链） |
| CRYPTO>当铺密码 | → `趣味编码速查.md` pawnShop 词条（笔画出头算法+解码示例；按 T1 归类当铺属趣味编码，T4 所指"古典密码速查"以词条实际所在文件为准） |
| CRYPTO>QWE密码 | → `古典密码速查.md` qwe 词条（补键盘对照图） |
| WEB>string转可执行代码（eval/jsfuck） | → `CTF/Web/前端审计.md` 新增节 |
| 空节（`# WEB` 下空内容、CRYPTO>编码空节） | 丢弃留痕（无独有内容） |

### AWD 域调整

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 并入+git rm | `CTF/AWD/漏洞.md`（仅 vulhub 链接） | → `AWD/工具.md`「镜像」列表（注明来源） |
| 拆出新建 | `CTF/Crypto/哈希长度扩展攻击.md` | 原 `AWD/工具.md` 的 `Hash_extender` 章节整体拆出（哈希长度扩展攻击属密码学主题），分「原理」「工具」两节 |

## T5 拆分 CTF/Web/Python.md

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 并入 | WAF 绕过节（Unicode/十六进制字符） | → `CTF/Web/绕过技巧.md` 新增「WAF 绕过」节 |
| 并入 | 字符串前缀（r/b/u/f） | → `Programming/Python/06-数据类型.md` 新增「字符串前缀」节，注明来源 |
| 并入 | 位运算（二进制 AND/OR/XOR/NOT） | → `Programming/Python/05-逻辑运算.md` 新增「位运算」节，注明来源 |
| 并入 | 常用内置函数 + 常用库函数（base64/Crypto.Util.number） | → `Programming/Python/08-常用函数.md` 新增「CTF 常用函数速记」节，注明来源 |
| 并入 | `from pwn import xor` 占位节 + 已知明文恢复密钥脚本 | → `CTF/Crypto/XOR与CBC攻击.md`（T2 已含） |
| 并入 | 反序列化节（pickle 知乎链接） | → `CTF/Web/解析漏洞.md`「Pickle反序列化漏洞」空节填充（任务未明示，就近填充既有空节） |
| 丢弃留痕 | `# RCE (Remote Code Execution)` 空标题 | 无内容，删除 |
| git rm | `CTF/Web/Python.md` | 内容已全部分流 |

## T6 空壳与占位处理

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 并入+git rm | `CTF/Web/WEB.md`（view-source 技巧 0.4KB） | → `CTF/Web/信息收集.md` 新增「页面信息获取」节 |
| 并入+git rm | `CTF/Misc/图像隐写/BMP.md`（3 行） | → `图像隐写.md` 通用类型下「BMP」节 |
| 修复 | `CTF/Crypto/伪随机数.md` | 补唯一 H1「伪随机数」，原 H1「梅森旋转算法MT19937」降为 H2 并规范反引号 |
| 新建 | `CTF/Crypto/README.md` | 域内索引（11 文件一句话定位+阅读建议）+ `学习资料.md` 2 条链接并入「学习资料」节 |

## T7 重写 CTF/README.md

| 操作 | 对象 | 去向/说明 |
|---|---|---|
| 重写 | `CTF/README.md` | 域总述一句 → 9 子域导航表（Crypto/Misc/Web/Reverse/Pwn/AWD/IncidentResponse/Toolbox/Hacker，定位+代表文件链接）→ 相邻域互链（`ComputerScience/Security`、`Programming/正则表达式`、`SoftwareManual/软件清单`）。唯一 H1 "CTF" |

## 事实性内容改动清单（除格式/结构外）

1. 拼写修正：`caeser`→`caesar`、`virgenene`→`vigenere`（密码名统一，条目内注原拼写）。
2. `RSA理论知识.md` 2 处丢失图片改为"[图片已丢失：Pasted image 20231106224355]"、"[图片已丢失：Pasted image 20231201154721]"。
3. `PBE.md` 口令定义"一串单词、汉子、数字字符"→"汉字"（错字）；RC4 段多余"常"字删除。
4. `ToolsList.md` BurpSuite 52pojie 破解版链接移除（历史见 git）；`Ciphey` 标注 [已停更]（事实：Ciphey 已归档停更，建议其继任者 Ares）；`VolatilityPro` 从 PWN 节移至内存取证节（工具属性纠偏）。
5. Python 环境包列表去重（matplotlib/python-tk 重复行）。
6. 新增少量一句级说明（均为结构性注解，非知识内容）：`sagemath` 一句定位、`from pwn import xor` 一句用法、`哈希长度扩展攻击` 原理补一句 Merkle–Damgård 特性说明。
7. 去重合并：DES/栅栏/当铺/QWE/PBE/U2FsdGVkX1/Base64 介绍/NTFS/GCD/扩欧/费马小定理等重复段落按"保留完整版"合并，无信息丢弃。

## 门禁结果

1. `python _governance/scripts/fixlinks.py` → `DONE: 0 links fixed`（首轮修复归档件 6 处图片相对深度）；`python _governance/scripts/checklinks.py` → **all links OK**（另报 31 张孤儿图片，均为治理前遗留或其他批次文件所致，与本批无关）。
2. `python _governance/scripts/c2_verify_ctf_entries.py` → 原稿 84 个 H2 = 75 实词条 + 9 空标题；产物命中 **75/75**，空标题 9 个全部删除留痕。
