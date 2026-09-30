# Configurations

> 相关：[ASP.NET-Core](ASP.NET-Core.md) 的「使用Configuration」一节（`Options` 三兄弟 `IOptions`/`IOptionsSnapshot`/`IOptionsMonitor` 的行为差异、按优先度读取配置等）。[DependencyInjection](DependencyInjection.md)（`IOptionsSnapshot` 为 `Scoped` 生命周期的注意事项）。

## Options 模式（三兄弟）

- `IOptions<T>`：只读取一次（启动时），可注入单例服务。
- `IOptionsSnapshot<T>`：请求级快照，下一次请求重新读取配置（`Scoped` 生命周期，无法注册到单例服务）。
- `IOptionsMonitor<T>`：即时读取配置变更。

## Configure 方法

该方法似乎可以不同地方执行然后叠加生效。

```csharp
services.Configure<MvcOptions>(p =>
{
    p.Filters.AddService(typeof(ProxyMvcFilter));
});
```

## TroubleShooting
### 对于ICollection的行为是添加
添加的行为对于`Option`类带默认值的，以及有多个来源的都是一样。
源码在`Microsoft.Extensions.Confgiuration.ConfigurationBinder #line 530` 中

## Monica / FIPS2022 补充

### 选项叠加规则

- Monica `MoMvcOptionsExtensions`：多处 `services.Configure<TOptions>` 或 `services.Configure<MvcOptions>` 会叠加执行，不是后一次覆盖前一次。
- Monica `ModuleConfiguration`：`List`、`Array` 这类集合选项在多个 configuration provider 合并时默认是追加，不是替换。
- 学习要点：如果业务要求“完全替换”，不要假设后加载配置会覆盖旧集合；应显式清空、改键结构，或改成标量配置。
