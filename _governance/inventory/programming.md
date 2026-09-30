# 盘点：Programming 域（42 文件）

> 来源：治理阶段 A 探查子代理，2026-09-30。约 8900 行、约 470KB。

## 一、逐文件清单

### 根（3）

| 记录 |
|---|
| C.md \| 4KB \| zh \| C 语言指针专题（&/*、多级指针、常量指针、数组名退化） \| 无（结构完整） \| 仅覆盖指针却以"C"命名 |
| PHP.md \| 12KB \| zh \| PHP 基础笔记（预定义变量/常量/类型转换/运算符/函数，源自 B 站视频课） \| 无H1、①类标号、裸URL(bilibili)、疑似过期(`●`项目符+`\$`转义为 Word 粘贴痕迹) \| 唯一 PHP 语言笔记 |
| TroubleShooting.md \| 16KB \| 混 \| 跨技术栈故障手册：VS、IIS、EFCore、C#、ASP.NET Core/gRPC、Docker、K8S、NPM、Dapr、Windows \| 无（结构好） \| 与 NET/错误排查.md、NET/环境部署.md 重复(NU1105 vs NU1302、NuGet 缓存、EFCore 追踪异常三处)；Docker/K8S/Dapr 部分超出 Programming 域 |

### C++/（4）

| 记录 |
|---|
| 01-基础语法.md \| 12KB \| zh \| namespace/iostream/引用/inline/重载/模板/动态内存入门语法 \| 末尾 cpp 代码块未闭合 \| 与 02 的"运算符重载"分界清晰 |
| 02-类Class.md \| 20KB \| zh \| struct→class、构造/析构、拷贝构造、继承、虚函数/多态、多重继承、类模板 \| 无（前 81 行无标题引言） \| — |
| 03-string类型.md \| 4KB \| zh \| std::string 构造/遍历 + vector 向量入门 \| 文件名只提 string 但近半内容是 vector \| string 内容散见 04-其他.md |
| 04-其他.md \| 8KB \| zh \| 杂项：string↔char*、fgets 换行、头文件规则、map、VS 快捷键、LNK2019、UTF-8-BOM \| 兜底文件；图片引用路径少一级 `../`(fe23f359…png 目标在库根存在) \| 与 03 的 string 主题相邻 |

### Python/（11）

| 记录 |
|---|
| README.md \| 4KB \| zh \| 目录页：Python 特性简介 + 01-10 文件结构说明 \| 自称"本书"（外部资料改写痕迹）；文件列表用行内代码而非链接 | — |
| 01-语法规则.md \| 4KB \| zh \| 缩进/PEP8/注释/docstring/语法糖 \| 锚点失效([*生成器](#生成器generator) 目标实际在 03-函数.md) \| 装饰器/生成器细节在 03 |
| 02-变量.md \| 8KB \| zh \| 变量即引用、可变/不可变、LEGB、魔法属性 \| 无 | 与 06 的元组/字典键话题呼应 |
| 03-函数.md \| 16KB \| zh \| 参数/*args/**kwargs/lambda/高阶函数/装饰器/生成器原理 \| 无 | 内置函数表与 08-常用函数.md 重叠 |
| 04-流程控制.md \| 4KB \| zh \| 条件表达式、for/while+else、try/except \| 最后一个代码块未闭合——"## 异常处理"标题落入未闭合代码块内渲染丢失 | with 语句在 01 也有 |
| 05-逻辑运算.md \| 4KB \| zh \| and/or/not、in、链式比较、==与is \| 空文件/极简(实质约 20 行) | is/None 判断在 04 也出现 |
| 06-数据类型.md \| 12KB \| zh \| 数字/布尔/字符串/列表/Numpy/元组/字典/集合 \| 事实可疑(L53"整数0为True，1为False"说反；L137 称 `li[:]` 是"深克隆"——实为浅拷贝) | 布尔/None 与 04、05 重叠 |
| 07-类.md \| 4KB \| zh \| class/实例方法/类方法/静态方法/MRO \| 空文件/极简(49 行) | — |
| 08-常用函数.md \| 36KB \| zh \| 内置/常用函数大表格（数学、IO、字符串、类型、队列、pathlib） \| 36KB 无任何 H2（表格以分组行分组） | 与 03 的内置函数表明显重叠 |
| 09-模块与包.md \| 8KB \| zh \| import 搜索顺序/原理、循环与覆盖导入、相对导入 \| 锚点失效([#内置变量all] 目标在 02-变量.md) | __all__ 定义在 02 |
| 10-环境搭建.md \| 4KB \| zh \| pip 源配置、requirements、VSCode 编码、Python2→3 迁移 \| 疑似过期(Python2 相关) | — |

### NET/ 根（11）

| 记录 |
|---|
| Authentication.md \| 16KB \| 混 \| OAuth2.0/OIDC/JWT 术语 + ASP.NET Core 认证实现 \| 图片 %20 编码(3 张，存在) \| 内容是 ASP.NET 主题却放 NET 根；与 ASP.NET Core.md 的 Token/Swagger 认证节重叠 |
| 内置类型.md \| 12KB \| 混 \| Dictionary/Record/Span/ArraySegment/String 等 BCL 类型要点 \| "## PadString"空标题 | 值类型/Equals 与 基础.md、概念.md 边界模糊 |
| 基础.md \| 12KB \| 混 \| C# 类型系统与语言基础 | 裸URL(3) | 与 语法.md 重叠(using/try-finally)；与 概念.md 重叠(接口、值/引用类型)；两个"接口"H2 重复 |
| 多线程编程.md \| 16KB \| 混 \| lock/Mutex/RWLock/SemaphoreSlim/volatile/async-await 原理/Task 工厂 | 裸URL(2) | UnobservedTaskException 与 异常处理.md 重复；与 AsyncLocal.md 边界尚清 |
| 异常处理.md \| 12KB \| 混 \| throw/throw ex、catch-finally 覆盖链、未捕获兜底、C++ 非托管异常 | H1多个(2)、裸URL(1)；后半篇为林德熙博客整段转载(含 CC 署名及外链徽章图) | Task 异常与 多线程编程.md 重叠 |
| 性能优化.md \| 4KB \| 混 \| 仅 WebApplicationBuilder 空模板的默认开关清单 \| 空文件/极简；含伪 wikilink(`[[标题]](url)` 混写) | 与 ASP.NET Core.md 的 Configuration 话题相邻 |
| 数据库编程.md \| 4KB \| zh \| ADO.NET 五大对象 | 无 | 命名过宽；与 EFCore 新旧两代数据访问分属两处 |
| 概念.md \| 20KB \| 混 \| 运行时/框架概念(AOT/JIT/CLR/版本史) + OOP(重载重写/实例化顺序/GC/泛型约束) + Linq | ①类标号、裸URL(4)、事实可疑("实例化类的执行顺序"与 .NET 实际不符；"WinForms/WPF 属 .NET Framework 独有"已过时)、"Lambada"拼写错 | 三合一杂烩：与 语法.md/基础.md/错误排查.md 多处重叠 |
| 环境部署.md \| 8KB \| 混 \| dotnet CLI、NuGet 还原与缓存、dev-certs、CRL 启动冻结 | 代码块无语言(1)、疑似过期(machine.config 示例路径为 .NET Fx 2.0)、图片 %20 编码(1 张，存在) | NuGet 还原与 TroubleShooting.md 重复；与 ASP.NET Core.md"# 部署"重叠 |
| 语法.md \| 28KB \| zh \| C# 关键字大全 + 语法糖 + XML 注释标签表 \| 裸URL(3) | using/try-finally 与 基础.md；override/new/virtual 与 概念.md |
| 错误排查.md \| 4KB \| zh \| DistinctBy 需 ToList、Release+Docker 中文乱码、外部程序集加载失败 | 代码块无语言(1) | 与 TroubleShooting.md 定位重复；命名无法区分 |

### NET/Libraries/（11）

| 记录 |
|---|
| ASP.NET Core.md \| 40KB \| 混 \| 全景：MVC/Kestrel/管道/Configuration/IOC/AOP/RESTful/Swagger/SignalR/gRPC/Blazor/部署 | H1多个(2)、裸URL(9)、Session"现在过时"自注、Startup 写法为 .NET 6 前旧范式、**7 张图片引用目标缺失**(a2e479…、dd66a8e…、af71973…、c9639c6…、bda55e…、a53559f…、ea175c1…) | 与 接口.md/进阶.md/DependencyInjection.md/Authentication.md/环境部署.md 五处交叉 |
| ASP.NET Core接口.md \| 8KB \| zh \| FromBody 限制、Minimal API 与 Swagger、中间件顺序 | 空 H2("## 问题"无内容；"## 待学"仅一链接) | 中间件与主文件"管道模型"节互补但切分未声明 |
| ASP.NET Core进阶.md \| 8KB \| zh \| ApplicationPartManager/Features、Application Model 与 Conventions、SignalR 补充 | 无 | SignalR 补充与主文件应合并 |
| AsyncLocal.md \| 16KB \| zh \| AsyncLocal 用法/ExecutionContext 原理/COW 之坑/ValueHolder/HttpContextAccessor 源码 | H1多个(5，应降级)；系博客园"黑洞视界"文章转载+个人批注 | 与 多线程编程.md 相邻主题 |
| Configurations.md \| 4KB \| zh \| Options Configure 叠加语义、集合选项追加 | 空文件/极简(25 行) | Options 三兄弟在 ASP.NET Core.md 讲过，未互链 |
| DependencyInjection.md \| 8KB \| zh \| 三种生命周期兼容矩阵、捕获依赖、ValidateScopes、TryAdd 差异 | 无 | 与 ASP.NET Core.md"内置IOC/Autofac"节明显重叠 |
| EntityFrameworkCore.md \| 40KB \| 混 \| 问题排查(并发/SQLite GUID/跟踪) + ABP 仓储 + 模型配置对照表 + 连接池 | H1多个(2)、代码块无语言(1)、标题层级乱(H2 下直跳 H4)、含"以下待测试"未验证内容 | 问题节与 TroubleShooting.md、错误排查.md 重复 |
| JsonSerializer.md \| 8KB \| 混 \| System.Text.Json：默认行为/Converter 顺序/元组与 fields/DateTime 时区坑 | 无 | 与 接口.md Minimal API 返回值呼应 |
| Mapster.md \| 4KB \| zh \| Mapster 映射配置与两类失败原因 | 空文件/极简(34 行)；"TroubleShotting"拼写错 | Mapster 案例 TroubleShooting.md 也提及 |
| Serilog.md \| 4KB \| zh \| Serilog 配置结构、死锁、二次构建、禁用日志 | 无 | — |
| Stream.md \| 8KB \| zh \| HttpContext Request/Response Body 重写中间件完整案例 | 无（正文以 Monica 框架代码为主，个人项目耦合度高） | 与 接口.md 中间件话题相邻 |

### NET/UI/（2）

| 记录 |
|---|
| WPF.md \| 24KB \| zh \| XAML 头部/partial/美化/资源 pack URI/生成操作表/Binding/MVVM | 代码块无语言(1)、标题带全角冒号、疑似过期(资源"生成操作"大表为 Silverlight/xap 时代内容) | MVC/MVVM 概念与 ASP.NET Core.md 重复讲 MVC |
| WinForm.md \| 4KB \| 混 \| UI 线程亲和/Invoke、控制台调试、透明、防闪烁、无边框拖动 | "双层窗体"等 2 节仅堆链接无内容(链接农场) | "启用控制台调试"同时写了 WPF |

## 二、子目录画像

- **C++/**：01-04 数字前缀+中文主题；无 README；`04-其他` 兜底。
- **Python/**：唯一有 README（目录页）的子目录；01-10 数字前缀；正文有 `*`/`**` 自创重点标记。
- **NET/**：无序号、无 README。根=中文命名+1 英文 Authentication.md；Libraries=英文帕斯卡；UI=WPF/WinForm。命名中英不统一；DependencyInjection.md 英文名中文标题。
- **根散文件**：C/PHP/TroubleShooting 三者无归属目录。

## 三、笔记→笔记内部链接

**0 条真实互链。** 仅 3 处疑似：Python/01 失效锚点(目标在 03)、Python/09 失效锚点(目标在 02)、性能优化.md 伪 wikilink 外链。Python/README 用行内代码列文件（不可点击）。全域孤岛。

## 四、图片引用异常

约 90 个引用中：
1. **目标缺失 7 处**（全部在 ASP.NET Core.md：a2e479ea…、dd66a8e1…、af71973…、c9639c64…、bda55ea…、a53559f…、ea175c1…，L48/106/108/241/261/267/340）
2. 相对深度错误 1 处（C++/04-其他.md L171 少一级 `../`，目标存在）
3. %20 编码 6 处（Authentication×3、AsyncLocal×2、环境部署×1，可用，风格不统一）
4. 外链图片 1 处（异常处理.md L199 CC 徽章）

## 五、>20KB 大文件

- **ASP.NET Core.md（40KB，692 行，2 H1）**：MVC架构/原理/开发(Configuration/IOC/Autofac/AOP)/RESTful(Swagger/AutoMapper)/HTTPS/前端服务器/SignalR/gRPC/Unit Test/补充(Blazor)；# 部署。拆分落点：IOC→DependencyInjection.md；部署+HTTPS→环境部署.md；SignalR/gRPC→进阶.md；认证→Authentication.md。
- **EntityFrameworkCore.md（40KB，580 行，2 H1）**：# Entity Framework Core(问题/ABP仓储/外键/继承/ChangeTracker) + # 基础知识(DI/配置/连接池待测试/Monica补充)。按"问题排查/ABP 实践/模型配置/连接池"四块拆，前两块与 TroubleShooting.md 去重。
- **语法.md（28KB）**：switch/关键字(18 H3)/语法糖/注释(XML 标签大表)。可拆"关键字"与"语法糖"两文。
- **WPF.md（24KB）**：代码层/美化/资源引入/xaml（Binding/MVVM 藏在"xaml"节内）。建议 XAML 基础/资源与 pack URI/Binding 与 MVVM 三分；Silverlight 表删除或标注。
- **概念.md（20KB）**：AOT/JIT/版本史/CLR/Mono/ECMA/Blazor + OOP(10 H3) + Linq。至少拆"运行时与框架"与"OOP/Linq"两文。
- **Python/08-常用函数.md（36KB，41 行）**：仅 1 个 H1 的超大表。需先把分组行升格为章节。
- **C++/02-类Class.md（20KB）**：结构良好可不拆。

## 六、组织问题清单

1. 三个文件名带空格（ASP.NET Core*.md×3）：CLI/git/脚本处理需引号，与库内风格不一致。
2. NET 根 vs Libraries 边界模糊：Authentication/数据库编程放错层；性能优化名不副实。
3. 三处"排查"文件并存（TroubleShooting/错误排查/环境部署），命名无法区分职责，内容互有重复。
4. 基础 vs 语法 vs 概念边界不清（using 三处、override/new 两处、值引用类型两处）。
5. IOC 生命周期两遍、Swagger 两遍、SignalR 两遍。
6. 转载内容未规范化：AsyncLocal（5 H1 博客园转载）、异常处理（林德熙博文含 CC 声明）、WPF（Silverlight 表）——统一"来源标注+降级标题"。
7. 命名：TroubleShooting 大写 S、TroubleShotting、Lambada、中英混名。
8. 事实/时效：Python/06 两处、概念.md 两处、环境部署 machine.config、Python/10 Python2、ASP.NET Core Startup 旧范式。
9. 格式：PHP.md 无 H1（Word 转换稿）；C++/01 与 Python/04 末尾代码块未闭吞标题；内置类型 PadString 空节；接口.md 空"问题"节。
10. C++/Python 有序号体系，NET 无；C/PHP/TroubleShooting 游离根目录；NET 无 README 导航。
