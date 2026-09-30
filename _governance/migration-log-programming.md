# Programming 域内容治理迁移日志

> 执行日期：2026-09-30。前置：C1 机械重组（`NET→DotNet`、`C++→Cpp`、`ASP.NET Core.md→ASP.NET-Core.md`、`C.md→C/指针.md`、`PHP.md→PHP/基础.md`、`TroubleShooting.md→故障排查.md`）已完成。
> 原则：`git mv`/`git rm` 保留历史，不 commit（由协调方统一提交）；所有内容操作逐项留痕于本日志。
> 验收：`fixlinks.py`（0 处需修）+ `checklinks.py`（`all links OK`）全绿；域内 47 个 md 无未闭合代码围栏、无标题跳级、每文件唯一 H1（脚本 `_governance/tmp/verify_prog.py`）。

## T1 ASP.NET Core 家族重组（DotNet/Libraries/）

### 主文件 `ASP.NET-Core.md` 内容去向（逐节核对，40KB→约26KB）

| 原章节 | 去向 |
|---|---|
| `# ASP.NET Core`（H1） | 保留为唯一 H1；文首新增「家族导航」callout（链接 接口/进阶/认证/DependencyInjection/Configurations/环境部署） |
| `## MVC架构`（URL结构/Model传值/Session/Token机制） | 留主文件；Session"现在过时"自注改明确表述（`> [!note]` 注明原文与修订后说法，改述为 token/JWT 机制取代传统 Session，并链接认证分册）；Token机制节补认证互链 |
| `## 控制台程序为什么变成了网站（原理）`（Kestrel/入口/Startup/管道） | 留主文件；`### Startup类` 加时效注「.NET 6 之前写法，此后用 minimal hosting」；顺手修正 `ApplicatinBuilder`→`ApplicationBuilder` 拼写 |
| `## 开发`（launchSettings/IIS托管/自托管） | 留主文件 |
| `### 使用Configuration` | 留主文件；补 Options 三兄弟↔`Configurations.md` 互链；裸 URL→[Configuration in ASP.NET Core \| Microsoft Learn] |
| `### 使用内置IOC`（含生命周期/Autofac/AOP 全部小节） | 瘦身为主文件「依赖注入（IoC）」简述+链接；完整内容并入 `DependencyInjection.md`（见下） |
| `## 构建RESTful API`（属性路由/映射/AutoMapper/返回类型/Swagger/使用配置文件） | 全部留主文件；Swagger 节 3 条裸 URL（cnblogs 版本控制/csdn token/避坑）转链接，其中「token设置」改指向 `ASP.NET-Core-认证.md`「Swagger认证」（原 csdn 链接降级为括注保留）；`<http://localhost:port/swagger/v1/swagger.json>` 占位 URL 改行内代码 |
| `# 部署`（第二个 H1：局域网/公网/WebAssembly/dll目录启动） | 并入 `DotNet/环境部署.md` 新章 `## ASP.NET Core 部署`（H1→H2，子节顺延）；主文件留「部署」stub 节+链接 |
| `## HTTPS部署`（本地开发/IIS Express 44300-44399） | 并入 `环境部署.md` `### HTTPS部署`；`dev-certs https --trust` 与既有「## 证书」节重复 → 去重为"与证书一节重复，详见该节"链接；主文件 stub 已覆盖 |
| `## 作为前端服务器`（wwwroot 静态资源） | 留主文件（部署相关但不在分流指令范围，保守保留；候选后续可随部署章迁移） |
| `## SignalR`（概览/强类型） | 留主文件；3 个进阶小节（`Handle events for a connection`/`Send messages from outside a hub`/`不同的Hub不同的连接？`）并入 `ASP.NET-Core-进阶.md`「补充>SignalR」下（H3→H4，无重复内容，去重后互链）；裸 URL（derpturkey/blazor 教程/github issue/hubs 文档）全部转标题链接 |
| `## gRPC`（四种调用/概念/最佳实践/Protobuf-net） | 全部留主文件；自引用式 `[https://…](https://…)` 链接（5 处）与裸 URL 全部改为标题链接 |
| `## Unit Test`（Moq）/`## Cookies` | 留主文件；裸 URL（stackoverflow）转链接 |
| `## 补充`（Blazor/Controller 与动态代理） | 留主文件；Blazor 代码块语言标注 `cs`→`csharp` |

### `DependencyInjection.md`（合并去重）

| 操作 | 说明 |
|---|---|
| 并入 | 「IoC 概念与 ASP.NET Core 内置容器」（抽象/实现/注册/使用、三条好处、`ServiceCollection` 局限）；修正 `Microsoft.Externsions.DependencyInjection`→`Microsoft.Extensions.DependencyInjection` 拼写 |
| 生命周期去重 | 原 ASP.NET-Core.md 的三种生命周期文字与本文表格重复：保留本文完整版，`AddScoped` 请求级子容器原理解释+生命周期示意图（`fc35966….png`）补入「1. 三种生命周期的基础定义」，`AddSingleton` 用途句并入表格下方 |
| 并入 | 「手动获取依赖」（含 `52aaeffa….png`）、「使用第三方IOC容器（例 Autofac）」（注册/解析两小节）、「AOP面向切面编程」（含 5 张图，Filter 四种注入方式） |
| 互链 | 文首链接回 ASP.NET-Core.md；`CreateHostBuilder` 段落加 minimal hosting 时效注 |
| 格式 | `## 注意事项` 下的 `####` 小节（ActivatorUtilities/Scoped和Transient/部分注入/性能比较）降跳级为 `###`；`### 差异` 更名 `### TryAdd 系列："差异"`（消除与「性能比较」的层级错乱，内容不动） |

### 其他家族文件

| 文件 | 操作 |
|---|---|
| `环境部署.md` | 新增 `## ASP.NET Core 部署`（含 HTTPS）；`## 证书` 与 HTTPS 部署去重互链；`## 还原` 与 `Programming/故障排查.md` 的 NU1105 条目互链去重（NU1105=项目未加载，还原=源/缓存问题，二者互补不重复合并）；`## 构建` 代码块语言 `csharp`→`bash`（命令非代码）；文首加分流说明 |
| `ASP.NET-Core-进阶.md` | 「补充>SignalR」并入 3 个进阶小节；`Application Model` 下 3 个 `####` 跳级（H2→H4）修为 `###` |
| `ASP.NET-Core-认证.md` | 文首补与主笔记「Token机制」的互链说明（Swagger认证/Token 细节以本文件为准，主文件为概览） |
| `Configurations.md` | 新增「Options 模式（三兄弟）」节并与 `ASP.NET-Core.md` 互链 |

## T2 EFCore 拆分（Libraries/）

`EntityFrameworkCore.md`（40KB、2 个 H1）拆为：

| 新结构 | 内容 |
|---|---|
| `EntityFrameworkCore.md`（基础） | 唯一 H1；`# 基础知识` H1 降并为导语；依赖注入（`#### DbContext依赖注入` 跳级修为 `###`）/模型配置（fluentAPI/数据注释/跟踪修改）/日志排查/注意事项/反向工程/Migration/**数据库连接池(以下待测试)整节原文未动**/Monica-FIPS2022 补充；文首链接问题排查分册 |
| `EntityFrameworkCore-问题排查.md`（新建） | 原「问题」章全部（Update 行为/`DbUpdateConcurrencyException`/`AbpDbConcurrencyException`（修改令牌/多线程触发）/SQLite GUID 大小写问题/A second operation/Cannot access a disposed context/更新异常连续操作）+「ABP仓储层」+「外键问题」+「继承关系」+「更新（ChangeTracker）」；并合入 `Programming/故障排查.md` 的 4 条 EFCore 条目（见 T3）；标题整体上提一级、无跳级 |

| 清理项 | 说明 |
|---|---|
| `#### SQLlite相关问题` | 拼写修正为「SQLite相关问题」（正文 `SQLite` 原本就正确） |
| 「数据库更新操作异常catch后…」下的空 ```` ```cs ```` 代码块 | 删除（无内容的占位块） |
| 2 条 sourcegraph 裸 URL | 转标题链接 |
| 原「EFCore跟踪修改」等 H3 挂在「模型配置」下 | 层级保持，无跳级 |

## T3 故障排查合并

| 操作 | 对象 | 说明 |
|---|---|---|
| git rm | `DotNet/错误排查.md` | 3 个条目全部并入 `Programming/故障排查.md` 后删除（git 留史） |
| 并入 | `### Linq DistinctBy 似乎需要 ToList() 才有效` | → `故障排查.md`「C#」节 |
| 并入 | `## .NET > ### 加载外部程序集失败（deps.json 未包含）` | 新增「.NET」章（AsterixDecoder/deps.json 案例，错误日志代码块补 `text` 标注） |
| 并入 | `### Release 模式编译，Linux Docker 中文乱码` | → 「Docker」节首位（GB2312/CRLF 问题） |
| EFCore 去重 | 「EFCore」节 4 条（字段未算上/temporary value/同键重复追踪/枚举 0-1） | 细节移入 `EntityFrameworkCore-问题排查.md`「模型与映射异常」；本节改为"一句话+链接"索引（含 github issue 链接随细节迁移） |
| NuGet 互链 | NU1105 条目 ↔ `DotNet/环境部署.md`「还原」 | 两处互补不重复：NU1105=命令行 restore 解决项目未加载；还原=源配置/缓存/NU1302 |

## T4 Python 系列修复

| 文件 | 操作 |
|---|---|
| `04-流程控制.md` | 文件末尾未闭合的 ```python 代码块补闭合围栏（原文件末行无换行，导致末块吞掉 EOF；`## 异常处理`标题位于块前，修复后整体渲染正常） |
| `01-语法规则.md` | `[*生成器](#生成器generator)` 失效锚点（目标在 03）→ `[生成器](03-函数.md#**生成器（Generator）)`（Obsidian 按标题字面匹配） |
| `09-模块与包.md` | `` [`__all__`](#内置变量all) `` 失效锚点（目标在 02）→ `` [`__all__`](02-变量.md#*内置变量/魔法属性) `` |
| `06-数据类型.md` | ①"整数`0`为`True`，`1`为`False`"→ 事实修正为 `bool` 是 `int` 子类型、`True/False` 对应 `1/0`、`bool(0)==False`/`bool(1)==True`（`> [!note]` 留痕）；②"`li[:]` 深克隆"→ 浅拷贝（等价 `li.copy()`，深层嵌套仍共享引用，行内留痕）；③ 顺手修正同类错误：`a = b.copy() # a深克隆b`（Set 节）→ 浅拷贝留痕；④ 修复 CTF 并入的 r-string 段落中 `` `␊`、`⇥` `` 破损行内代码（`\n`/`\t` 被转成了字面换行/制表符）→ `` `\n`、`\t` `` |
| `08-常用函数.md`（36KB 单表） | 表格分组行（数学类/输入输出/字符串类/类型/数据结构/文件和目录访问）升格为 H2 章节（命名按任务清单：数学类/输入输出/字符串/类型转换/数据结构/文件与目录），各章节保留原子表与备注；加文首目录；与 `03-函数.md` 去重：03 的「内置函数/魔法方法」表格+3 条参考链接移入 08 新章「内置函数与魔法方法」，03 保留文字说明+链接 |
| `Python/README.md` | 文件清单 10 项行内代码→真链接 |
| `10-环境搭建.md` | 「Python2转Python3的坑」加 `> [!note] 历史记录`（Python 2 已于 2020-01 EOL） |
| `05-逻辑运算.md` | 检查 CTF 并入段落（位运算节）：来源注齐全、无突兀，未改动 |

## T5 其他文件修复

| 文件 | 操作 |
|---|---|
| `Cpp/01-基础语法.md` | 末尾未闭合的 ```cpp 块补闭合（文件以 `}` 结尾无围栏） |
| `DotNet/概念.md` | ① `## Linq 与 Lambada表达式` 标题+正文 → "Lambda"（留痕注）；② GetHashCode 四条 ①②③④ 标号 → Markdown 序号（留痕注）；③ 裸 URL×4（GC 博客/MS 基础/unmanaged/stackoverflow Trim）转标题链接；④ `\<Costura …/\>`、`Packages-\>` Word 转义清理为行内代码；⑤ **两处存疑事实加 `> [!question] 待事实核查` callout 未改原文**：(a)「.NET Framework 独有特性」表把 `WinForms`/`WPF` 列为独有（.NET Core 3.0/.NET 5+ 已支持）；(b)「实例化类的执行顺序」清单排列与常见结论有出入（子类静态/父类静态/父类实例/子类实例的先后与"子类的实例字段"位置）——**留待主控阶段 D 处理** |
| `DotNet/内置类型.md` | `### PadString` 空标题删除（正文留痕注说明，无内容丢失）；`lambada`→`lambda`；裸 URL×4 转标题链接 |
| `DotNet/性能优化.md` | 伪 wikilink `[[探索 .NET 6]02 …](url)` → `【探索 .NET 6】02 …`（内层方括号改全角，避免嵌套括号破坏链接） |
| `DotNet/异常处理.md` | 林德熙转载段：第二个 H1 `# 来自C++等非托管库的异常Catch` 降为 H2，节首补 `> [!note] 转载说明`（文末 CC BY-NC-SA 署名原样保留）；`#### throw`/`#### throw ex`/`#### Json序列化问题` 跳级修为 `###`；裸 URL（github issue）转链接 |
| `DotNet/Libraries/AsyncLocal.md` | 5 个 H1 → 唯一 H1「AsyncLocal」+ 4 个 H2（实现原理/的坑/避坑指南/HttpContextAccessor 实现原理）；文首补全转载来源说明（整篇转载自博客园《.NET AsyncLocal 避坑指南》，原有单节来源注保留） |
| `DotNet/Libraries/Configurations.md` | 与 ASP.NET-Core.md Options 三兄弟互链（见 T1） |
| `DotNet/多线程编程.md` | 裸 URL×2（JetBrains DCL/cnblogs async）转标题链接 |
| `DotNet/基础.md` | 裸 URL×3（CS1612/ModuleInitializer/automatic-memory-management）转标题链接 |
| `DotNet/语法.md` | 注释节重复的裸 URL 与标题链接去重；ranges 裸 URL 转链接并入小节首；表格内 stackoverflow 裸 URL 转链接 |
| `DotNet/UI/WPF.md` | 全角冒号标题×3 规范化（`代码层：`→`代码层`、`美化：`、`资源引入：`）；裸 URL（多 Style 插件）转链接；`**●xxx**` Word 式小节标记保留（作者约定式排版，未动） |
| `DotNet/UI/WinForm.md` | 链接农场节×3（启用控制台调试/双层窗体/控件透明）改为"一句话+标题链接"；无内容的裸 URL 段落合并整理 |
| `Programming/PHP/基础.md` | 补 H1「PHP 基础」；Word 残留清理：`●` 项目符→标准 H2/H3 章节（嵌套小节按原层级映射）、`\$`/`\<`/`\>` 转义还原、`__DIR__` 等魔术常量还原、代码行收进 ```php 块、①②③④→Markdown 序号、弯引号代码→直引号、全角括号/分号→半角（代码处）；裸 bilibili URL 转链接；明显拼写修正（留行内痕）：`imlode`→`implode`、`triger_error`→`trigger_error`、`\</from\>`→`</form>`；内容未增删（`73P` 等作者标记原样保留） |
| `Programming/C/指针.md` | 体检：28 个围栏配对、唯一 H1、无跳级、代码块均有 `c` 标注——无需修改 |
| `Programming/正则表达式.md` | 2 个 H1（艱深写法/语法）→ 唯一 H1「正则表达式」，「语法」前置、「艱深写法」降 H2（其下 `####` 跳级修为 `###`）；2/3 空白语法表补齐常见正则语法（分组：字符与字符类/锚点/量词/或/替换/子组结构/内联标志，含 `.`、`[…]`、`\d\w\s`、`\b`、`\A\z`、`*+?{n,m}`、懒惰量词、`\|`、`(?i)(?s)(?m)(?x)` 等，标注"通用 PCRE/.NET，各引擎略有差异"）；内联标志组标"待补充：各引擎差异"——未伪造不确定内容，原有条目（字符串包含/`\0``\1``${foo}`/环视组等）原样保留 |

## T6 域索引

| 文件 | 内容 |
|---|---|
| `Programming/README.md`（新建） | 语言域导航：DotNet 家族树/Cpp/Python/C/PHP/正则/故障排查，每行链接+一句话 |
| `Programming/DotNet/README.md`（新建） | 语言层 vs Libraries vs UI 三层结构说明 + 全部文件导航（含 ASP.NET Core 家族与 EFCore 两分册） |

## 验收记录

1. `python _governance/scripts/fixlinks.py` → `DONE: 0 links fixed`；`python _governance/scripts/checklinks.py` → `all links OK`（245 md）。
2. ASP.NET-Core.md 原全部 H1/H2/H3 去向见 T1 表格（每节"留主文件/移入目标文件"逐一核对，无丢失）；EFCore 原两 H1 结构去向见 T2。
3. 结构自检脚本 `_governance/tmp/verify_prog.py`：Programming 域 47 md，无未闭合围栏、无标题跳级、均唯一 H1。
4. git 状态：`DotNet/错误排查.md` 经 `git rm` 删除（历史保留）；新增 3 文件（EntityFrameworkCore-问题排查.md、Programming/README.md、DotNet/README.md）；未执行 commit。
5. 备注：`DotNet/Libraries/Aspire.md` 的改动来自并行域代理（与 CloudNative/Dapr 互链），非本批操作。
