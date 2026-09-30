# MySQL

要注意MySQL里面函数的index是从1开始的。

## Trouble Shotting

### Linux中提示表不存在但Windows环境又可以

mysql在linux中默认安装配置是不忽略大小写的而Windows又是忽略大小写的

EFCore默认是生成小写表名，不显式配置表名迁移到linux中会导致表不存在。

## 连接及配置

### 允许远程连接


```sql
GRANT ALL PRIVILEGES ON *.* TO 'USERNAME'@'IP' IDENTIFIED BY 'PASSWORD' with grant option; -- ip设置为%是允许所有来源IP

FLUSH PRIVILEGES;
-- 以上是mysql8以前
--mysql8.0后不能直接GRANT to现有的用户 需要先创建新的再赋予权限

-- Starting with MySQL 8 you no longer can (implicitly) create a user using the GRANT command. Use CREATE USER instead, followed by the GRANT statement:

USE mysql;

CREATE USER 'user'@'localhost' IDENTIFIED BY 'P@ssW0rd';

GRANT ALL ON *.* TO 'user'@'localhost';

FLUSH PRIVILEGES;

--检查设定用户连接允许的host来源

SELECT host,user FROM mysql.user;

-- 修改密码
ALTER USER '用户名'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码';
```


## 管理全局变量


```sql
SHOW GLOBAL VARIABLES LIKE 'local_infile';

SET GLOBAL local_infile = true;
```


## 表操作

### 修改字段名

ALTER TABLE 表名 CHANGE 旧字段名 新字段名 必须还得跟着新字段类型等;


```sql
alter table `songs` change `aaa` `bbb` VARCHAR(255);
```


#### 修改字段


```sql
ALTER TABLE t_user

ADD COLUMN user_age int(**11**) DEFAULT NULL COMMENT '年龄' AFTER user_email;

-- 删除列，COLUMN也可以不用写

DROP COLUMN column;

-- 添加自增ID

alter table calendar add id int not null auto_increment PRIMARY KEY;
```


## 临时表

```sql
CREATE TEMPORARY TABLE IF NOT EXISTS table2 AS (SELECT * FROM table1)

-- 直接用结果集创建为临时表，不需要写临时表结构。

DROP TABLE if EXISTS aliasTmpTable;

CREATE TEMPORARY TABLE if not EXISTS aliasTmpTable (

        titleTmp VARCHAR ( 255 ), aliasTmp VARCHAR ( 255 ));

-- 临时表不可以写进存储过程BEGAIN里面，必须在外面声明，不然会报错。
```

### 注释

![](../../attachments/7dc98a6eefb9e0f2514d0b470962f4b3.png)


## 函数

| 函数                                     | 作用           | 备注                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **字符串操作**                               |                |                                                                                                                                                                                                                                                                                                                                    |
|                                          | Start With     | MySQL似乎没有StartWith这种功能，但是可以通过下面这个实现： a.song_title like CONCAT(SUBSTR(j.title, 1, 1),'%')                                                                                                                                                                                                                     |
| CONCAT()                                 | 字符串拼接     | 最常用的字符串拼接方法，但遇到拼接中的字符串出现null的情况会返回null 插入换行符得用CHAR(10)                                                                                                                                                                                                                                        |
| CONCAT_WS()（concat with separator）     | 字符串拼接     | 比CONCAT多了个分隔符功能，且如果某个字符串为null，会忽略null，并返回其他字符串的值 语法：CONCAT_WS(separator,str1,str2,…) 第一个参数是其它参数的分隔符。分隔符的位置放在要连接的两个字符串之间。分隔符可以是一个字符串，也可以是其它参数                                                                                           |
| cast("23333.3333" as decimal)            | 字符串类型转换 |                                                                                                                                                                                                                                                                                                                                    |
| CONVERT("23333.3333", decimal(3,1))      | 字符串类型转换 | 不支持’’的，会报错Incorrect DECIMAL value: '0' for column '’ at row -1 decimal(3,1)，总3位，保留1位 如果只用decimal，则是四舍五入变成整数                                                                                                                                                                                          |
| substring_index                          |                | Return the substring before the first occurrence of the delimiter "-": SELECT SUBSTRING_INDEX('foo-bar-bar', '-', 1) as result; Outputs result = "foo" You can replace 1 with the numbers of occurrences you want before getting the substring SELECT SUBSTRING_INDEX('foo-bar-bar', '-', 2) as result; Outputs result = "foo-bar" |
| FROM_UNIXTIME(date,'%Y-%m-%d %H:%i:%S')  | 时间戳转换     |                                                                                                                                                                                                                                                                                                                                    |
| SUBSTRING(myfield, 1, LENGTH(myfield)-4) |                | 利用length函数，动态的检测需要保留的位数，因此曲线救国的实现了remove。 注意CHARACTER_LENGTH()与LENGTH()的区别！                                                                                                                                                                                                                    |
|                                          |                |                                                                                                                                                                                                                                                                                                                                    |
|                                          |                |                                                                                                                                                                                                                                                                                                                                    |
| **判断操作**                                 |                |                                                                                                                                                                                                                                                                                                                                    |
| IF(expr1,expr2,expr3)                    | IF             | 如果expr1=true，则返回expr2，否则expr3。                                                                                                                                                                                                                                                                                           |
| IFNULL(expr1,expr2)                      |                | 假如expr1 不为 NULL，则 IFNULL() 的返回值为 expr1; 否则其返回值为 expr2                                                                                                                                                                                                                                                            |
|                                          |                |                                                                                                                                                                                                                                                                                                                                    |
| **日期处理**                                 |                |                                                                                                                                                                                                                                                                                                                                    |
| YEAR(date)                               | 获取年         |                                                                                                                                                                                                                                                                                                                                    |
| MONTH(date)                              | 获取月         |                                                                                                                                                                                                                                                                                                                                    |
| DAY(date)                                | 获取日         |                                                                                                                                                                                                                                                                                                                                    |

![](../../attachments/70b817be1ab289c47449a61414f74a50.png)

### 其他

#### 自增ID重置


```sql
-- 从第一条开始重置（注意不可以用于有外键关系的）

SET @rownum = 0;
UPDATE table_name SET id = @rownum := @rownum +1;

-- 从最后一条开始重置

ALTER TABLE table_name AUTO_INCREMENT = 1;

-- 注意自增id重置后仍然会往现有表中id最大一个往后加
```

#### 一行变多行

```sql
Drop table if EXISTS numbers;
CREATE TEMPORARY TABLE numbers (
  n INT PRIMARY KEY);
-- 这意思是是拆分结果最多可能的数量
INSERT INTO numbers VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13);
select
  aliases.title,
  SUBSTRING_INDEX(SUBSTRING_INDEX(aliases.alias, '|', n), '|', -1) as a
from
  numbers inner join aliases
  on CHAR_LENGTH(aliases.alias)
     -CHAR_LENGTH(REPLACE(aliases.alias, '|', ''))>=n-1

```



## 数据库中的字符编码

utf8mb4_general_ci是针对utf8mb4编码的collation(n.校对，核对；整理; (对书卷号码、编页等的) 核实，配页; 牧师职务的授予;)

collation即用于指定数据集如何排序，以及字符串的比对规则。

mb4就是most bytes 4 （一个字符最多4字节）的意思，专门用来兼容四字节的Unicode

ci是case insensitive的缩写，cs是case sensitive的缩写。即，指定大小写是否敏感。

**在ci的collation下，如何在比对时区分大小写？**


```sql
select * from pet where name = binary 'whistler'; -- 推荐，这不会使索引失效
```


或


```sql
select * from pet where binary name = 'whistler';
```

**mysql中的对utf8支持有缺点**（因为早期规定只支持最大utf8的字符长度为 3 字节 或称为utf8mb3）

三个字节的 UTF-8 最大能编码的 Unicode 字符是 0xffff，也就是 Unicode 中的基本多文种平面(BMP Basic Multilingual Plane 或称第零平面 Plane 0)（是Unicode中的一个编码区段。编码从U+0000至U+FFFF）。也就是说，任何不在基本多文种平面的 Unicode字符，都无法使用 Mysql 的 utf8 字符集存储。包括 Emoji 表情(Emoji 是一种特殊的 Unicode 编码，常见于 ios 和 android 手机上)，和很多不常用的汉字，以及任何新增的 Unicode 字符等等(utf8的缺点)

### utf8mb4_0900_ai_ci

MySQL 8.0之后，默认collation不再像之前版本一样是是utf8mb4_general_ci，而是统一更新成了utf8mb4_0900_ai_ci。

中间的0900，它对应的是Unicode 9.0的规范。要知道，Unicode规范是在不断更新的，每次更新既包括扩充，也包括修正。比如6.0版新加入了222个中日韩统一表义字符（CJK Unified Ideographs），7.0版加入了俄国货币卢布的符号等等。

ai表示accent insensitivity，也就是"不区分音调"

### 修改数据库的字符集及字符编码

修改数据库的


```sql
ALTER DATABASE db_name CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
```


生成修改表的语句


```sql
SELECT
CONCAT("ALTER TABLE `", TABLE_NAME,"` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;")
AS target_tables
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA="db_name"
AND TABLE_TYPE="BASE TABLE"
```

注意，这里使用 `CONVERT TO` 而非 `DEFAULT`，是因为后者不会修改表中字段的编码和字符集。

### 使用Mysql数据库函数解码Unicode字段内容到UTF-8


```sql
CREATE FUNCTION STRINGDECODE(str TEXT CHARSET utf8)
RETURNS text CHARSET utf8 DETERMINISTIC
BEGIN
declare pos int;
declare escape char(6) charset utf8;
declare unescape char(3) charset utf8;
set pos = locate('\\u', str);
while pos > 0 do
    set escape = substring(str, pos, 6);
    set unescape = char(conv(substring(escape,3),16,10) using ucs2);
    set str = replace(str, escape, unescape);
    set pos = locate('\\u', str, pos+1);
end while;
return str;
END
```

#### Collation与Character Set分开的好处

我们可以多想想，把character set和collation分开，到底有什么好处？其实好处很多。如果把字符看作个人，character set就相当于验明正身，给每个字符发张身份证，而collation相当于告诉大家，排队的时候谁在前谁在后。collation有多套，就相当于可以灵活按身高、体重、年龄、出身地等等因素来排序，却完全不会受到身份证号的干扰。

这个问题本来不麻烦，为什么会难住人呢？原因不复杂，你去看关于MySQL和Unicode的中文资料，绝大部分都是告诉你，utf8或者utf8mb4就可以解决问题了。因此，不少程序员完全意识不到还有collation这种东西。

所以，这些程序员理解的"字符集"就只有一堆孤零零的字符，根本没想到还需要定义字符之间的等价和排序关系。而这恰恰是最可惜的，因为他们完全错过了"举一反三"的启发，许多类似问题也就缺乏解决思路。要知道，哪怕你做的不是国际化的业务，也可以从collation中受益的。

我们都知道，电商系统的订单处理是一个流程，其中涉及许多状态，比如"已下单，未支付"、"已支付"、"已确认"、"已拣货"、"已发货"等等。

有程序员看到这个需求，想当然就按照先后顺序，用1、2、3、4、5来表示对应状态，确实简单不会出错，也方便先后对比，比如要查找所有"已确认"之前的订单，就查查"已确认"的状态码是4，那么找状态码\<4的订单就可以。

然后，有一天，忽然要在两个状态之间加入某个中间状态，比如"已确认"之后需要新的风险评估，通过了才可以去拣货，怎么办？总不可能在3和4之间加一个3.5吧？因为这个数据字段本来就是整数型啊。

所以"有经验"一点的程序员会改改，一开始就不按照1、2、3、4、5这样来分配状态码，而是按100、200、300、400、500，留足空隙，这样就避免了3.5的尴尬，直接给"风控系统已通过"分配350就可以了。

但这仍然不够。如果业务忽然要求既有顺序要变，比如之前"已确认"在前，"风控系统已通过"在后，现在要求"风控系统已通过"在前，"已确认"在后，该怎么办？350总不可能大于400呀。

如果你了解了collation就会发现，这是同样的问题。数据的标识和数据的有序性应当隔离开来。标识是一套规范，有序性是另一套规范，两者可以随意组合。你看，Unicode字符的排序可以按照字符的编码值来，也可以按照其它规范来——加载不同collation就是了嘛。

所以，"已下单，未支付"的代码就可以是OUPD，"已支付"的代码就可以是PDED，"已确认"的代码就可以是CFMD…… 它们只用来做唯一标识，没有任何其它意义。然后在外面定义一套顺序规则，比如OUPD \< PDED \< CFMD，然后提供一个查询接口，做任何比较的时候都查询这个接口就好——实际上许多语言可以自定义compare函数来做排序，道理就在这里。万一将来要改业务流程，比如加入新状态，或者更改状态的先后顺序，也只需要做一点点更改，规则查询接口保持不变，其它地方更是保持原封不动。

## 问题

### MySQL Error 1153 - Got a packet bigger than 'max_allowed_packet' bytes

```sql
set global net_buffer_length=1000000;

set global max_allowed_packet=1000000000;

-- Use a very large value for the packet size.
```
