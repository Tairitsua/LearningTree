# DotNet

`.NET`/`C#` 学习笔记，按"语言层 → Libraries → UI"三层组织。

## 结构说明

- **语言层**（本目录根）：`C#` 与 `.NET` 平台本身的语法、概念与通用实践——不依赖特定框架类库就能理解的内容。
- **[Libraries](Libraries/)**：具体类库与框架的笔记，其中 `ASP.NET Core` 是一个家族（主笔记 + 接口/进阶/认证分册 + `DependencyInjection`/`Configurations` 等专题）。
- **[UI](UI/)**：桌面/客户端 UI 框架（`WPF`、`WinForm`）。

## 语言层

- [基础](基础.md) - 访问性、值/引用类型、属性、特性、索引器、枚举、事件、接口、非托管代码
- [语法](语法.md) - 关键字（`override`/`virtual`/`static`/`ref`/`yield`…）、语法糖、模式匹配、XML 注释
- [概念](概念.md) - `AOT`/`JIT`、`.NET` 版本史、`CLR`/`BCL`、面向对象、`GC`、泛型约束、`Linq`
- [内置类型](内置类型.md) - `Dictionary`/`Record`/`IEnumerable`/`Span<T>`/`String` 等内置类型要点
- [异常处理](异常处理.md) - `throw`/`finally`/`using` 异常流、未捕获异常、`C++` 非托管异常
- [多线程编程](多线程编程.md) - 锁、`volatile`、`async`/`await`、`Task`、线程问题排查
- [性能优化](性能优化.md) - `WebApplicationBuilder` 默认行为等
- [环境部署](环境部署.md) - 启动、NuGet 还原、构建/发布命令、`ASP.NET Core` 部署与 HTTPS
- [AI编码规则](AI编码规则.md) - AI 辅助编码约定

## Libraries

- [ASP.NET Core](Libraries/ASP.NET-Core.md) - 主笔记（架构/管道/`Configuration`/RESTful/`Swagger`/`gRPC`/`Blazor` 概览），家族导航见其文首
  - [ASP.NET-Core-接口](Libraries/ASP.NET-Core-接口.md)、[ASP.NET-Core-进阶](Libraries/ASP.NET-Core-进阶.md)、[ASP.NET-Core-认证](Libraries/ASP.NET-Core-认证.md)
- [EntityFrameworkCore](Libraries/EntityFrameworkCore.md) - 基础（DI/模型配置/`Migration`/连接池）
  - [EntityFrameworkCore-问题排查](Libraries/EntityFrameworkCore-问题排查.md) - 并发/跟踪/ABP 仓储实践等
- [DependencyInjection](Libraries/DependencyInjection.md) - DI 生命周期矩阵、`Autofac`、AOP（`Filter`）
- [Configurations](Libraries/Configurations.md) - `Options` 模式与配置绑定
- [AsyncLocal](Libraries/AsyncLocal.md)、[ADO.NET](Libraries/ADO.NET.md)、[JsonSerializer](Libraries/JsonSerializer.md)、[Mapster](Libraries/Mapster.md)、[Serilog](Libraries/Serilog.md)、[Stream](Libraries/Stream.md)、[Aspire](Libraries/Aspire.md)

## UI

- [WPF](UI/WPF.md) - `XAML`、资源、`Binding`、`MVVM`
- [WinForm](UI/WinForm.md) - 线程安全、透明、拖动等界面实践

> 跨栈故障排查见上级目录的 [Programming/故障排查](../故障排查.md)。
