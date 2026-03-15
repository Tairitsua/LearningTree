# Mapster

```csharp
TypeAdapterConfig<TSource, TDestination>
    .NewConfig()
    .Map(dest => dest.Id, src => src.Id)
    .Map(dest => dest.Name, src => src.Name)
    .IgnoreNonMapped(true) //这里的意思是除了显式配置的Map，其他都忽略
```

## TroubleShotting

### Cannot convert immutable type
映射的是不同的类型，比如`DateTime`和`DateOnly` 除非写了两种类型的映射？

### 没有映射上
映射的类型可能无法访问。比如属性没有`set`方法或不是`public`的`set`方法。

## Monica / FIPS2022 补充

### 查询投影

- Monica `MoAbstractKeyCrudAppService`：`ProjectToType` 遇到 DTO 中声明的子表字段时，可能已经把关联数据一并投影出来，额外 `Include` 往往只是增加查询成本。

### 类型匹配

- FIPS2022 `UnifiedAppRunner`：无默认构造函数的类型，通常需要额外映射配置，例如 `ConstructUsing` 或显式构造规则。
- FIPS2022 `UnifiedAppRunner`：值类型的可空与非可空是两组不同映射，`int -> TimeSpan`、`int? -> TimeSpan?` 这类要分别配置。
- FIPS2022 `UnifiedAppRunner`：引用类型可空大多只是元数据；如果真的要读取空标注，应该使用 `NullabilityInfoContext` 这类运行时 API。

### 配置叠加与空值

- FIPS2022 `FlightService.Infrastructure/AppBaseRunner`：`ForType` 是增强现有映射，不是清空并重建；后续规则会继续叠加在已有配置上。
- FIPS2022 `AlarmService.Infrastructure/AppBaseRunner` 与 `FlightService.Infrastructure/AppBaseRunner`：`IgnoreNullValues(true)` 只是不把 `null` 赋给目标，不会保护 `src.SomeNullable.Value`；`Map` 表达式里仍要显式判空。
