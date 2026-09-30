# 迁移映射表（C1 机械重组清单）

> C1 只做"纯移动/重命名"（不改内容），内容操作（拆分/合并/重写）在 C2 各域批完成。
> 执行方式：`git mv` 保历史；移动后运行 `_governance/scripts/fixlinks.py` 重算相对链接；`checklinks.py` 校验 0 死链后才 commit。

## 目录级迁移

| 原路径 | 新路径 | 说明 |
|---|---|---|
| `Fontend/` | `Frontend/` | 拼写修正 |
| `CloudNative/Kubernetes(K8S)/` | `CloudNative/Kubernetes/` | 去括号（断链根因） |
| `CTF/CRYPTO/` | `CTF/Crypto/` | 命名统一 PascalCase |
| `CTF/MISC/` | `CTF/Misc/` | 同上 |
| `CTF/WEB/` | `CTF/Web/` | 同上 |
| `CTF/PWN/` | `CTF/Pwn/` | 同上 |
| `CTF/应急响应/` | `CTF/IncidentResponse/` | 同上 |
| `CTF/ToolManual/` | `CTF/Toolbox/` | 与"工具清单"定位统一 |
| `ComputerScience/数据结构/` | `ComputerScience/Algorithms/` | 与 Algorithm 合并统一 |
| `ComputerScience/网络安全/` | `ComputerScience/Security/` | 命名统一 |
| `ComputerScience/Architecture/架构/` | `ComputerScience/Architecture/`（扁平化） | 原稿另归档 |
| `Programming/NET/` | `Programming/DotNet/` | 命名统一 |
| `Programming/C++/` | `Programming/Cpp/` | 去 `+` |
| `Business/` | `Finance/` | 域名义与内容相符 |
| `attachments/templates/` | `_templates/` | 摆脱 attachments 忽略规则 |

## 文件级迁移/重命名

### ComputerScience
| 原路径 | 新路径 |
|---|---|
| `ComputerScience/Architecture/架构.md`（原稿） | `_archive/ComputerScience/架构-原稿.md` |
| `ComputerScience/Architecture/架构/架构.md`（索引） | `ComputerScience/Architecture/README.md` |
| `ComputerScience/网络安全/网络安全.md`（索引） | `ComputerScience/Security/README.md` |
| `ComputerScience/网络安全（旧）.md` | `_archive/ComputerScience/网络安全-旧稿.md` |
| `ComputerScience/网络安全（新）.md` | `_archive/ComputerScience/网络安全-新稿.md` |
| `ComputerScience/计算机网络.md` | `ComputerScience/Network/计算机网络.md` |
| `ComputerScience/操作系统.md` | `ComputerScience/OperatingSystem/操作系统.md` |
| `ComputerScience/Algorithm/代码优化.md` | `ComputerScience/Algorithms/代码优化.md`（C2 重编号 07-） |
| `ComputerScience/AI/ArtificialIntelligence.md` | `ComputerScience/AI/神经网络入门.md` |
| `ComputerScience/AI/Audio.md` | `ComputerScience/AI/人声分离UVR5.md` |
| `ComputerScience/AI/Drawing.md` | `ComputerScience/AI/Roop换脸环境.md` |
| `ComputerScience/AI/Security.md` | `ComputerScience/AI/LLM安全-提示注入与越狱.md` |
| `ComputerScience/AI/AICoding.md` | `Programming/DotNet/AI编码规则.md` |
| `ComputerScience/Linux/Docker环境安装.md` | `CloudNative/Docker/环境安装.md` |

### Programming
| 原路径 | 新路径 |
|---|---|
| `Programming/C.md` | `Programming/C/指针.md` |
| `Programming/PHP.md` | `Programming/PHP/基础.md` |
| `Programming/TroubleShooting.md` | `Programming/故障排查.md` |
| `Programming/NET/Authentication.md` | `Programming/DotNet/Libraries/ASP.NET-Core-认证.md` |
| `Programming/NET/数据库编程.md` | `Programming/DotNet/Libraries/ADO.NET.md` |
| `Programming/NET/Libraries/ASP.NET Core.md` | `Programming/DotNet/Libraries/ASP.NET-Core.md` |
| `Programming/NET/Libraries/ASP.NET Core接口.md` | `Programming/DotNet/Libraries/ASP.NET-Core-接口.md` |
| `Programming/NET/Libraries/ASP.NET Core进阶.md` | `Programming/DotNet/Libraries/ASP.NET-Core-进阶.md` |
| `Programming/C++/03-string类型.md` | `Programming/Cpp/03-string与vector.md` |
| `Programming/C++/04-其他.md` | `Programming/Cpp/04-杂项.md` |

### Frontend
| 原路径 | 新路径 |
|---|---|
| `Fontend/FrontendConcept.md` | `Frontend/CORS.md` |

### CloudNative
| 原路径 | 新路径 |
|---|---|
| `CloudNative/Aspire.md` | `Programming/DotNet/Libraries/Aspire.md` |
| `CloudNative/消息中间件.md` | `CloudNative/Components/消息中间件.md`（C2 并入 RabbitMQ.md） |
| `CloudNative/Components/Apache APISIX.md` | `CloudNative/Components/ApacheAPISIX.md` |
| `CloudNative/Dapr/Actor.md` | `CloudNative/Dapr/BuildingBlocks/Actor.md` |
| `CloudNative/Docker/VisualStudio集成.md` | `CloudNative/Docker/Docker与VisualStudio.md` |
| `CloudNative/K8S/Harbor镜像仓库.md` | `CloudNative/Docker/Harbor.md` |
| `CloudNative/K8S/TroubleShooting.md` | `CloudNative/Kubernetes/故障排查.md` |

### CTF
| 原路径 | 新路径 |
|---|---|
| `CTF/Reverse/Andorid逆向.md` | `CTF/Reverse/Android逆向.md` |
| `CTF/CRYPTO/Practice_Cryptograph.md` | `CTF/Web/JWT.md` |
| `CTF/WEB/绕过(Bypass).md` | `CTF/Web/绕过技巧.md` |
| `CTF/WEB/模板注入.md` | `CTF/Web/SSTI-模板注入.md` |
| `CTF/WEB/JavaScript.md` | `CTF/Web/JavaScript原型链污染.md` |
| `CTF/WEB/提权.md` | `CTF/AWD/提权.md` |
| `CTF/WEB/正则表达式.md` | `Programming/正则表达式.md` |
| `CTF/思路打开.md` | `CTF/Misc/解题思路.md` |
| `CTF/AWD/Linux易忽略点.md` | `CTF/AWD/Linux要点.md` |
| `CTF/Hacker/代理解密.md` | `CTF/Hacker/视频号代理解密.md` |
| `CTF/ToolManual/Burpsuite.md` | `CTF/Toolbox/BurpSuite.md` |
| `CTF/ToolManual/VMware.md` | `SoftwareManual/VMware.md` |

### SoftwareManual / 其他
| 原路径 | 新路径 |
|---|---|
| `SoftwareManual/MicosoftOffice.md` | `SoftwareManual/MicrosoftOffice.md` |
| `Business/基础.md` | `Finance/恒生科技ETF联接基金.md` |

## C1 同步修改

1. `.obsidian/app.json`：`userIgnoreFilters` 增加 `"_archive/"`、`"_governance/"`。
2. 新建空目录：`ComputerScience/Network/`、`ComputerScience/OperatingSystem/`、`Programming/C/`、`Programming/PHP/`、`_archive/ComputerScience/`。
3. 链接重算后必须全库校验通过再 commit。
4. `Koubot/`、`CTF/README.md`、`CTF/ToolsList.md`、`CTF/WEB/Python.md`、`ComputerScience/Linux.md`、`Database.md`、`BigData.md`、`SoftwareManual/CMD.md`、`WSL.md`、`Fontend/HTML&CSS.md`、`English/English.md` 等内容操作对象保留原地，C2 处理。

## C2 内容操作清单（各域子代理的任务依据）

1. **ComputerScience 批**：Linux.md(208K) 拆 7 篇入 Linux/ + Koubot/Linux命令.md 并入命令速查；Database.md 拆 3 篇入 Database/；BigData.md 拆 2+索引；Algorithms 重编号（附录并入基本概念）；Architecture README 重写；WEB.md 并入 Network/计算机网络.md。
2. **CTF 批**：CTF.md(45K) 拆 2 速查+条目分流；RSA.md+RSA理论知识+算法性质→RSA与数论+XOR与CBC攻击；Encoding+编码类+base64CaseCrack 合并；ToolsList 分流（CTF→Toolbox/工具清单.md；通用→SoftwareManual/软件清单.md）；CTF/README.md 重写为索引；杂烩内容分流去重（PBE/栅栏/NTFS/图片隐写/思路 各归其位）；Web/Python.md 拆分（WAF→绕过技巧、语言基础→Programming/Python、XOR→Crypto）；Xdbg/学习资料/漏洞/BMP/WEB.md 空壳并入。
3. **SoftwareManual 批**：CMD.md 拆 3（PowerShell 章→Powershell.md）；WSL.md 拆 3（zshrc→attachments/zshrc.conf）；VisualStudio 6 H1 降级；Microsoft+PowerToys→Windows杂记.md；Acunetix→Toolbox 工具清单。
4. **Frontend 批**：HTML&CSS.md(81K)→HTML.md+CSS.md；TypeScript/JS/Vue 的 npm/nvm/Express→Node与npm.md；IsolationCSS→Blazor.md；WebComponent 离题节处置。
5. **English 批**：English.md 拆 5 篇。
6. **Programming 批**：ASP.NET-Core 家族重组（IOC→DependencyInjection、部署→环境部署、SignalR/gRPC→进阶、认证去重）；EFCore 拆"问题排查/模型配置"；故障排查.md 合并 NET/错误排查.md 去重；Python 锚点/代码块/事实修正；08-常用函数加 H2。
7. **CloudNative 批**：概述+Node 合并；Kubernetes监控 拆节（Git→SoftwareManual/Git.md、发布→CICD/发布策略.md、网络→Kubernetes/网络.md）；命名空间+组件配置 合并；消息中间件+RabbitMQ 合并；K8S部署笔记 并入部署要求；K8S/命令.md 并入概述；隐私脱敏（Redis 密码、内网 IP、Pod 名）。
