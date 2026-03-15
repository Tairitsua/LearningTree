# Configurations

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
