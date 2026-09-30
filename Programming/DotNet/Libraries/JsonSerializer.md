# System.Text.Json

By default, all public properties are serialized. You can specify properties to ignore.

The default encoder escapes non-ASCII characters, HTML-sensitive characters within the ASCII-range, and characters that must be escaped according to the RFC 8259 JSON spec.

By default, JSON is minified. You can pretty-print the JSON.

By default, casing of JSON names matches the .NET names. You can customize JSON name casing.

By default, circular references are detected and exceptions thrown. You can preserve references and handle circular references.

**By default, fields are ignored. You can include fields.**

## JsonConverter

不管是`JsonConverterFactory`还是`JsonConverter`，引擎按顺序遍历，每个类型只会选取第一次`CanConvert`返回`true`的`Converter`进行转换，所以注意顺序。


## TroubleShooting

### 未成功反序列化
`System.Text.Json`默认行为是只反序列化到`public`属性（或`init`？），对于非`public`的属性的需要加`JsonInclude`标签才会设置。
[c# - Use System.Text.Json to deserialize properties with private setters - Stack Overflow](https://stackoverflow.com/questions/62270834/use-system-text-json-to-deserialize-properties-with-private-setters/67206063#67206063)
默认是大小写敏感的，需要设置option insensitive
.NET 7后新增`JsonRequired`

#### 元组无法序列化

直至`.NET 8.0`，仍对元组序列化支持不够，目前仅有设置`IncludeFields=true`才会序列化成功，且序列化为`Items = xx`的形式，若有命名，反序列化时也为`(null, null)`


### 序列化值为{}

**默认情况下是序列化当前类型字段**，如果用`this`关键字要小心。如果传入的是个接口类型，也将序列化失败，可以使用 `(object)yourObjToSerialize`

```csharp
/// <summary>
/// 将当前状态提取为可追踪链信息
/// </summary>
/// <returns></returns>
public string GetCurTracingData()
{
    return JsonSerializer.Serialize(this, TracingDataJsonOptions); //应改为(object)this
}
```

### 序列化失败

默认情况下不会序列化`Field`，只会序列化`Properties`。而`Tuple`是两个public field，所以也不会序列化`Tuple`

#### 类型不一致

比如`labelId:100000` 就无法序列化到 `string labelId`上

### JsonConstructor 特性

Constructor上的参数必须与属性或字段一样，否则会报错：`Each parameter in the deserialization constructor on type xxx must bind to an object property`
似乎多了或少了都不行？

```csharp
public class Person
{
    public string  Name { get; init; }
    public string  Age { get; init; }
    public string TracingData { get; set; }
    public List<object> ChangingList { get; set; }
    [JsonConstructor]
    public Person(string name, string age, string tracingData, List<object> changingList)
    {
    }
}

var json2 = """
           {
           "tracingData": "123",
           "changingList": [
            "ddd"
           ],
           "name" : "",
           "age": ""
           }
           """;
```

## 补充

### ASP.NET Core 全局 JSON

- 来源：`Monica.Core`
- 如果项目同时用了 MVC 和 Minimal API，只配置 `Microsoft.AspNetCore.Mvc.JsonOptions` 不够，`Microsoft.AspNetCore.Http.Json.JsonOptions` 也要一起配置。
- 最稳的做法是维护一份统一的 `JsonSerializerOptions`，再分别克隆到 MVC 与 Minimal API；否则枚举序列化、空值忽略、引用循环等行为容易不一致。

### 带时区偏移的 `DateTime`

- 来源：`Monica.Core`
- 类似 `2024-08-08T03:27:05+08:00` 这种带时区偏移的输入，进入 MVC 反序列化或绑定后，得到的 `DateTime.Kind` 可能已经是 `Utc`。
- 如果业务语义依赖“本地时间”而不是“绝对时刻”，不要想当然地把反序列化结果继续当本地时间使用，最好统一做一次归一化处理。

### 自定义 `DateTime?` Converter 与 `null`

- 来源：`Monica.Core`
- 自定义 `JsonConverter<DateTime?>` 时，如果希望 `null` 也走进自己的转换逻辑，需要显式重写 `HandleNull => true`。
- 不加这个设置时，`null` token 可能直接被框架短路，你的 converter 根本不会进入。
