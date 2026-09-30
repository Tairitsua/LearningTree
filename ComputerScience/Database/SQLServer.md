# SQL Server
## 配置管理器

管理SQLServer服务
不能直接找到，需要运行相应版本的`SQLServerManagerXX.msc`

| Version                | Path                                       |
| ---------------------- | ------------------------------------------ |
| SQL Server 2022        | C:\Windows\SysWOW64\SQLServerManager16.msc |
| SQL Server 2019        | C:\Windows\SysWOW64\SQLServerManager15.msc |
| SQL Server 2017        | C:\Windows\SysWOW64\SQLServerManager14.msc |
| SQL Server 2016        | C:\Windows\SysWOW64\SQLServerManager13.msc |
| SQL Server 2014 (12.x) | C:\Windows\SysWOW64\SQLServerManager12.msc |
| SQL Server 2012 (11.x) | C:\Windows\SysWOW64\SQLServerManager11.msc |

### Navicate 无法连接
检查是否开启了`TCP/IP`连接
![](../../attachments/Pasted%20image%2020231030084457.png)

## 语句

`RESTORE DATABASE FIPS with recovery` 使正在还原的数据库变为已还原可访问

### 嵌套子查询

```sql
select sum(c), d from
(
select count(*) c, DATEPART(HH, SOBT) as d from FlightPlan where … group by SOBT
) as tempTable group by d order by d.
```

嵌套语句都需要取列名、且临时表也要取名

## 坑
### 连接字符串失败

比如用 `Navicate` 连接 `127.0.0.1:33333` 端口的`docker`环境SQL Server，默认是会报错的。
而要使用 `127.0.0.1,33333`，逗号连接！

#### 无法信任的根证书SSL问题

在连接字符串中加入`TrustServerCertificate=true`

#### 自增ID列无法插入

`SET IDENTITY_INSERT FlightPlan ON`

#### TOP而不是LIMIT

而且写法是 `SELECT TOP 100 * FROM Table`

#### 字符串是用单引号而不是双引号

#### 在查询结果里面继续查询需要重命名结果

```sql
SELECT
    newStr,
    oldStr,
    LogID
FROM
    (
        SELECT
           SUBSTRING (
               MsgText,
               newStart,
               newEnd - newStart
           ) AS newStr,
           SUBSTRING (
               MsgText,
               oldStart,
               oldEnd - oldStart
           ) AS oldStr,
           LogID
        FROM
           (
               SELECT
                   CHARINDEX('"OLDFLT_NUM":', MsgText) AS flag1,
                   CHARINDEX('"OLDFLT_NUM":', MsgText) + len('"OLDFLT_NUM":') AS oldStart,
                   CHARINDEX(',"OLDSTART_CITY"', MsgText) AS oldEnd,
                   CHARINDEX('"NEWFLT_NUM":', MsgText) AS flag2,
                   CHARINDEX('"NEWFLT_NUM":', MsgText) + len('"NEWFLT_NUM":') AS newStart,
                   CHARINDEX(',"NEWSTART_CITY"', MsgText) AS newEnd,
                   MsgText,
                   LogID
               FROM
                   NAIPChangeLog
               WHERE
                   MsgVersion = '2021-13.V1'
           ) AS tmp
        WHERE
           flag1 > 0
        AND flag2 > 0
        AND SUBSTRING (
           MsgText,
           oldStart,
           oldEnd - oldStart
        ) != SUBSTRING (
           MsgText,
           newStart,
           newEnd - newStart
        )
    ) tmp2;

```

> 注意里面的tmp和tmp2

#### 在Select中命名的在Where中不能马上使用，这是因为Where比Select先执行，所以得使用嵌套查询才可用别名

## 函数

| 函数名                                       | 作用                                                                                                   | 备注                                                                                                                                                                                 |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DATEPART(datepart, date)                     | 函数用于返回日期/时间的单独部分                                                                        | Datepart:年yy,月mm,日dd Weekday/dw，一周的第几天（周日是第一天），所以这里用CASE DATEPART(WEEKDAY, @StartTime) WHEN 1 THEN 7 ELSE DATEPART(WEEKDAY, @StartTime) - 1 END) AS CHAR(1)  |
| CONVERT(date_type,expression[, style])       | 转换expression结果成特定类型                                                                           | Style一般在时间转字符串时使用。 CONVERT(varchar(100), GETDATE(), 120) 120是ODBC规范，yyyy-mm-dd hh:mi:ss（24小时制） 23是yyyy-mm-dd 24是hh:mi:ss                                     |
| CHARINDEX(str1, str2[, start_location])      | 从str2中查找str1，可以使用start_location指定从str2开始查找的位置（为1或0或负数，都是从第一位开始查找） | 查找到返回str1在str2出现的位置（index，从1开始，即第一个字符），反之返回0                                                                                                            |
| OBJECT_ID('tempdb..\#MatchPlan') IS NOT NULL | 判断MatchPlan临时表是否存在                                                                            |                                                                                                                                                                                      |
| GETDATE()                                    | 获取当前时间                                                                                           |                                                                                                                                                                                      |
|                                              |                                                                                                        |                                                                                                                                                                                      |
|                                              |                                                                                                        |                                                                                                                                                                                      |

## 数据库文件迁移

```sql
select name,physical_name from sys.master_files; -- 查看数据库定义的文件目录

USE master

GO

ALTER DATABASE ZGACFIPS MODIFY FILE (NAME= ZGACFIPS_data , FILENAME= 'D:\MSSQL\DATA\ZGACFIPS_data.mdf') -- 设定数据库定义位置
```

使用select后复制出来可以使用该正则快速生成

`^((.+?)_.+?)\s+.+\\(.+)`

`ALTER DATABASE $2 MODIFY FILE (NAME= $1, FILENAME= 'D:\\MSSQL\\DATA\\$3')`

然后关闭数据库，解除文件占用，移动ldf、log文件到指定目录，再启动数据库，把处于Recovery Pending的数据库删除，再Attach上指定目录上的数据库。
