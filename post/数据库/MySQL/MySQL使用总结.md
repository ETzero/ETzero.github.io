# MySQL 使用总结

## MySQL 命令

#### 连接MySQL

```bash
# mysql -uroot -p
Enter password:

# mysql -h host -u user -p
Enter password:

# menagerie 是数据名字
# mysql -h host -u user -p menagerie
Enter password:
```

#### MySQL 批处理命令

```bash
# mysql < batch-file
# mysql -h host -u user -p < batch-file
Enter password: ********
# mysql < batch-file | more
# mysql < batch-file > exec_result.log

# mysql -uroot -p
Enter password: ********

mysql> source batch-file;

```

#### 基本 MySQL 命令

```sql
mysql> SHOW ENGINES;											# 显示存储引擎
mysql> show databases;										# 显示数据库
mysql> show tables;												# 显示当前数据库下所有表
mysql> show variables;										# 显示当前使用的系统变量
mysql> show variables like '%something%';		# 查找显示指定系统变量
mysql> show status;										# 显示状态信息
mysql> SHOW WARNINGS;									# 显示告警信息
mysql> SHOW CREATE TABLE pet;					# 显示创建表的SQL语句
mysql> SHOW PROCESSLIST;							# 显示用户正在运行的线程

mysql> CREATE SCHEMA menagerie;				# 创建 menagerie 数据库
mysql> CREATE DATABASE menagerie;			# 创建 menagerie 数据库
mysql> USE menagerie;									# 使用 menagerie 数据库
mysql> SELECT DATABASE();							# 查看当前使用的数据库
mysql> DESCRIBE pet;									# 打印表结构
mysql> DESC pet;											# 打印表结构

mysql> FLUSH PRIVILEGES;							# 重新加载授权表
mysql> select VALIDATE_PASSWORD_STRENGTH('Q~123456');		# 测试密码强度

# 创建表
mysql> CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20),
       species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);

# NULL 的使用： is NULL 和 is not NULL
mysql> SELECT 1 IS NULL, 1 IS NOT NULL;

# 排序列
# DESC关键字仅适用于紧邻其前面的列名（birth）; 它不会影响species列排序顺序。
mysql> SELECT name, species, birth FROM pet
       ORDER BY species, birth DESC;

mysql> drop DATABASE menagerie;				# 删除数据库
mysql> alter table oldtablename rename to newtablename		# 修改表名
mysql> alter table tablename modify fieldname datatype		# 修改字段数据类型
# 修改字段名
mysql> alter table tablename change oldfieldname newfieldname newdatatype
# 新增字段
mysql> alter table tablename add fieldname datatype [约束条件] [first | after otherfieldname]
mysql> alter table pet add id INT(8) PRIMARY KEY first;
mysql> alter table pet add remarks VARCHAR(100) NOT NULL default "" after death;
# 删除字段
mysql> alter table tablename drop fieldname;
# 修改字段顺序
mysql> alter table tablename modify fieldname datatype first|after otherfield;
# 更改表使用的存储引擎
mysql> alter table tablename engine=enginename;
# 删除表外键
mysql> alter table tablename drop foreign key keyname;
# 删除表
mysql> drop table tablename;

# 创建索引
mysql> create [UNIQUE|FULLTEXT|SPATIAL] INDEX indexname on tablename (fieldname [(indexlen)] [ASC|DESC]);
mysql> alter table tablename add [UNIQUE|FULLTEXT|SPATIAL] INDEX indexname on tablename (fieldname [(indexlen)] [ASC|DESC]);

mysql> create INDEX index_id on pet (id ASC);								# 创建普通索引
mysql> create UNIQUE INDEX idx_id on pet (id);							# 创建唯一性索引
mysql> create FULLTEXT INDEX idx_name on pet (name (4));		# 创建全文索引
mysql> create SPATIAL INDEX idx_birth on pet (birth DESC);	# 创建空间索引

mysql> drop index indexname on tablename;		# 删除索引

```

#### 导入导出数据命令

```sql
# 加载数据的两种方式
# 第一种方式：创建一个文本文件pet.txt ，每行包含一个记录，其值由制表符分隔，并按照CREATE TABLE语句中列出的顺序给出 。对于缺失值，您可以使用NULL 值。要在文本文件中表示这些，请使用 \N（反斜杠，大写-N）
# 第二种方式：就是常见的 insert 语句

# cat pet.txt
Whistler        Gwen    bird    \N      1997-12-09      \N

mysql> LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet;
mysql> INSERT INTO pet
       VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);

# 导出表数据到文件中
mysql> select * into outfile 'root/pet.t' from pet;
ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
# 失败是因为 服务站在安全文件模式下，mysql没有对 root 目录有写的权限。
# 详细查看 secure_file_priv 的官网说明

mysql> show variables like '%secure_file_priv%';		# 显示安全目录
+------------------+-----------------------+
| Variable_name    | Value                 |
+------------------+-----------------------+
| secure_file_priv | /var/lib/mysql-files/ |
+------------------+-----------------------+
1 row in set (0.00 sec)

mysql> select * into outfile '/var/lib/mysql-files/pet.tt' from pet;
OK

```

### MySQL 函数

#### MySQL 日期时间函数

```sql
mysql> select CURDATE() from dual;				# 当前日期
mysql> select now() from dual;						# 当前日期时间
# 计算两个时间差 计算方式以第一个参数为准。YEAR 表示计算相差年数，其他以此类推
mysql> select TIMESTAMPDIFF(YEAR|MONTH|DAY|HOUR, time1, time2)
# 将整型表达式int_expr 添加到日期或日期时间表达式 datetime_expr中。第一个参数用于表示 int_expr 的单位，YEAR 表示 datetime_expr 加上 int_expr 年。
mysql> select TIMESTAMPADD(YEAR|MONTH|DAY|HOUR,int_expr,datetime_expr)
# 提取日期中的年数
mysql> select YEAR(now()) from dual;		# now is 2019-09-12 resutlt is 2019
# 提取日期中的月数
mysql> select MONTH(now()) from dual;		# now is 2019-09-12 resutlt is 09
# 提取日期中的天数
mysql> select DAYOFMONTH(now()) from dual;	# now is 2019-09-12 resutlt is 12
# 日期加上间隔
mysql> select DATE_ADD('2018-05-01',INTERVAL 1 DAY);	# 2018-05-02
# 日期减去间隔
mysql> select DATE_SUB('2018-05-01',INTERVAL 1 YEAR);	# 2017-05-01

# 日期加上间隔 now is [2019-09-13 06:17:30] and result is [2019-09-13 06:27:50]
mysql> select now() + INTERVAL '10:20' MINUTE_SECOND from dual

```

