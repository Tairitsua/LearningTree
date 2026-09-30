# PHP基础

## 文件包含

常见文件包含语句：

1. `require`
2. `include`
3. `require_once`
4. `include_once`

区别说明：

1. `require` 和 `include` 的主要区别在于失败时的处理方式。
2. `require` 出错时会产生更严重的错误并终止脚本。
3. `include` 出错时通常只产生警告，脚本可继续执行。
4. `*_once` 表示同一个文件只加载一次，常用于避免重复包含。

## 预定义变量

这些变量由系统预先定义，通常也被称为超级全局变量：

1. `$_GET`：获取所有以 `GET` 方式提交的数据
2. `$_POST`：获取所有以 `POST` 方式提交的数据
3. `$_REQUEST`：合并 `GET` 和 `POST` 数据；若重名，通常后者覆盖前者
4. `$GLOBALS`：所有全局变量组成的数组
5. `$_SERVER`：服务器信息
6. `$_SESSION`：`session` 会话数据
7. `$_COOKIE`：`cookie` 会话数据
8. `$_ENV`：环境变量
9. `$_FILES`：上传文件信息

### `session`

使用 `session` 前需要先启动：

```php
session_start();

$_SESSION["name"] = "King";
unset($_SESSION["name"]);
session_destroy();
unset($_SESSION);
```

### `cookie`

```php
setcookie("user", "value", time() + 3600, "/");
$user = $_COOKIE["user"];
setcookie("user", "", time() - 3600);
```

## 可变变量与引用传递

可变变量示例：

```php
$a = "b";
$b = "hello";

echo $$a;
```

引用传递示例：

```php
$a = &$b;
```

## 常量

定义方式：

```php
define("APP_NAME", "demo");
const VERSION = "1.0.0";
```

说明：

1. 常量名通常不带 `$`。
2. 常量名一般使用大写。
3. 使用特殊字符定义时，通常只能通过 `define()` + `constant()` 访问。

### 系统常量与魔术常量

常见系统常量：

1. `PHP_VERSION`
2. `PHP_INT_SIZE`
3. `PHP_INT_MAX`

常见魔术常量：

1. `__DIR__`
2. `__FILE__`
3. `__LINE__`
4. `__NAMESPACE__`
5. `__CLASS__`
6. `__METHOD__`
7. `__FUNCTION__`

## 数据类型

`PHP` 是弱类型语言，变量本身没有固定数据类型。

常见类型可分为三类：

1. 基本数据类型：`int`、`float`、`string`、`bool`
2. 复合数据类型：`object`、`array`
3. 特殊数据类型：`resource`、`NULL`

## 类型转换与判断

### 类型转换

有两种常见方式：

1. 自动转换：系统根据上下文自动处理
2. 强制转换：手动指定类型

示例：

```php
$value = "123";
$number = (int)$value;
```

其他说明：

1. `true` 转数值通常为 `1`，`false` 通常为 `0`。
2. 以字母开头的字符串转数值时，结果通常为 `0`。
3. 以数字开头的字符串会从开头解析到无法继续为止。

### 常用判断函数

```php
empty($value);
isset($value);
var_dump($value);
gettype($value);
settype($value, "integer");
```

说明：

1. `empty()` 用于判断值是否为空。
2. `isset()` 用于判断变量是否已声明且不为 `null`。
3. `var_dump()` 用于查看变量的值、结构与类型。
4. `gettype()` 返回变量类型名。
5. `settype()` 会直接修改变量本身的类型。

## 运算符

常见特殊运算符：

1. `===`：全等于，值与类型都相同
2. `!==`：不全等于
3. `.`：字符串连接
4. `.=`：拼接并重新赋值
5. `@`：错误抑制符

`@` 常用于你预期某些表达式可能报错、但又不希望直接把错误暴露给用户的场景。生产环境中通常也会结合统一错误处理，而不是只依赖 `@`。

## 文件加载路径

相对路径常见写法：

```txt
./   当前目录
../  上级目录
```

说明：

1. 绝对路径通常更稳定，但灵活性稍差。
2. 文件嵌套包含时，相对路径更容易出错。

## 函数

函数定义示例：

```php
function display($name)
{
    return $name;
}
```

补充说明：

1. `PHP` 通常先编译再执行，所以函数定义可以放在调用后面。
2. `return` 也可以直接在被包含文件中使用，把结果返回给 `include` / `require` 的调用方。

### 作用域

1. 局部变量：函数内部定义的变量
2. 全局变量：函数外部定义的变量
3. 超全局变量：如 `$_SERVER`、`$_POST`

在函数内部访问全局变量的两种常见方式：

```php
global $name;
echo $GLOBALS["name"];
```

### 静态变量

函数内部可以使用 `static` 关键字定义静态变量，使其在多次调用之间保留状态。

### 可变函数

```php
$fn = "display";

function display()
{
    echo "hello";
}

$fn();
```

### 匿名函数

```php
$handler = function () {
    // 函数体
};
```

匿名函数本质上会生成一个 `Closure` 对象。

### 错误处理

可以人为触发错误：

```php
trigger_error("manual error");
```

## 数组

常用函数：

```php
implode(",", $array);
```

## 表单传值

### `GET` 传值

常见方式：

1. `form` 表单
2. `a` 标签
3. `location.href`
4. `location.assign()`

示例：

```html
<form method="GET">表单元素</form>
<a href="https://www.xx.cn/index.php?data=xx"></a>
```

```javascript
location.href = "https://www.xx.cn/index.php?data=xx";
location.assign("https://www.xx.cn/index.php?data=xx");
```

### `POST` 传值

```html
<form method="POST">表单元素</form>
```

接收方式通常包括：

1. `$_GET`
2. `$_POST`
3. `$_REQUEST`

这些都是预定义数组，表单元素的 `name` 属性会作为数组下标，对应的 `value` 会作为数组值。

补充：

如果用户没有勾选复选框，后端可能根本接收不到对应字段。此时应先使用 `isset()` 判断是否存在，再做后续处理。

参考链接：

[PHP 常用系统函数参考 - Bilibili](https://www.bilibili.com/video/av12863134/?p=54)

## 修订说明

1. 将原文中的 `imlode` 更正为 `implode`。
2. 将原文中的 `triger_error()` 更正为 `trigger_error()`。
