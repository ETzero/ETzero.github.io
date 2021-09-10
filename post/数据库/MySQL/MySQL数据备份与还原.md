# MySQL 数据备份与还原

## 一、数据备份

### 1、mysqldump 命令备份

mysqldump 是MySQL 自带的 备份命令。使用逻辑备份的方式对数据库和表进行备份。

```bash
# mysqldump -u username -p dbname table1 table2 ... > BackupName.sql				# 备份一个数据库下的多张表
# mysqldump -u username -p --databases dbname1 dbname2 ... > BackupName.sql			# 备份多个数据库
# mysqldump -u username -p --all-databases > BackupName.sql							# 备份所有数据库

# 命令常见的一些参数
--add-drop-database					# 创建数据库先执行删除操作 (DROP DATABASE IF EXISTS `...`;)
--add-drop-table					# 在建表之前先执行删表操作
--add-locks							# 备份表时，使用LOCK TABLES 和 UNLOCK TABLES。(这个参数不支持并行备份)
--bind-address						# 指定通过哪个网络接口来连接Mysql服务器
--complete-insert					# dump出包含所有列的完整insert语句。
--compress							# 压缩客户端和服务器传输的所有的数据
--default-character-set				# 指定备份的字符集
--routines							# 备份出来包含存储过程和函数，默认开启
--triggers							# 备份出来包含触发器，默认开启
--user								# 备份时候的用户名
--password							# 备份需要的密码

其他更多参数，请参考官方：https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html
```

### 2、mysqlpump 命令备份

mysqlpump 也是MySQL 官方自带的备份命令，也是逻辑备份。使用上与 mysqldump 类似。

mysqlpump 相比 mysqldump ，注意是：

- mysqlpump  可以**并行备份**数据库和数据库中的对象的，加快备份过程
- 更好的控制数据库和数据库对象（表，存储过程，用户帐户）的备份
- 备份用户账号作为帐户管理语句（CREATE USER，GRANT），而不是直接插入到MySQL的系统数据库
- 支持压缩，备份出来直接生成压缩后的备份文件
- 备份进度指示（估计值）
- 还原备份文件，先建表后插入数据最后建立索引，减少了索引维护开销，加快了还原速度
- 备份可以排除或则指定数据库

```bash
# mysqlpump 的参数选项与 mysqldump 大部分是一直，下面列出一些特有的选择
--default-parallelism=0 			# 关闭并行备份功能
--add-drop-user						# 在CREATE USER语句之前增加DROP USER。(这个参数需要和--users一起使用，否者不生效)
--compress-output					# 默认不压缩输出，目前可以使用的压缩算法有 LZ4 和 ZLIB
--default-parallelism				# 指定并行线程数，默认是2，如果设置成0，表示不使用并行备份
--defer-table-indexes				# 延迟创建索引，直到所有数据都加载完之后，再创建索引，默认开启。
# 若关闭则会和mysqldump一样：先创建一个表和所有索引，再导入数据，因为在加载还原数据的时候要维护二级索引的开销，导致效率比较低
--exclude-databases 				# 备份排除该参数指定的数据库，多个用逗号分隔。
# 类似的还有--exclude-events、--exclude-routines、--exclude-tables、--exclude-triggers、--exclude-users
--include-databases					# 指定备份数据库，多个用逗号分隔。
# 类似的还有--include-events、--include-routines、--include-tables、--include-triggers、--include-users
--skip-dump-rows					# 只备份表结构，不备份数据，-d。（mysqldump支持--no-data，mysqlpump不支持--no-data）
--users								# 备份数据库用户，备份的形式是CREATE USER...，GRANT...
# mysqlpump --exclude-databases=% --users    # 备份数据库用户，过滤掉所有数据库
--watch-progress					# 定期显示进度的完成，包括总数表、行和其他对象。该参数默认开启

其他更多参数，请参考官方：https://dev.mysql.com/doc/refman/5.7/en/mysqlpump.html
```

### 3、物理备份

最直接的方式，直接拷贝磁盘目录上的数据文件。为保证数据一致性，最好停止MySQL 服务再进行拷贝。且该方式对 InnoDB 存储引擎不适用。同时还原的数据库最好版本一致。

## 二、备份还原

```bash
# mysql -u root -p < backup.sql
# 将 hostname1 主机上的数据库 备份至 hostname2 主机上。
# mysqldump -h hostname1 -u root -p[password] --all-databases | mysql -h hostname2 -uroot -p
Enter Password:
 
```

## 三、表的导出和导入

### 1、使用 select into outfile 导出

select into outfile 语句可以将表的内容导出成一个文本文件。

```sql
mysql> select column1, column2, ... from tablename where condition into outfile 'filename' [option];
mysql> select column1, column2, ... into outfile 'filename' from tablename where condition [option];
```

OPTION 的选项值有：

- FIELDS TERMINATED BY  '字符串' ：设置字符串为字段的分隔符。默认 '\t'
- FIELDS ENCLOSED BY  '字符' ：设置字符来括上字段的值。默认不使用任何字符
- FIELDS ESCAPED BY  '字符' ：设置转义字符，默认 '\'
- FIELDS OPTIONALLY ENCLOSED BY  '字符' ：设置字符来括上 CHAR、VARCHAR、TEXT等字符型字段。默认不使用任何字符
- LINES STARTING BY  '字符串' ：设置每行开头的字符，默认情况下无任何字符
- LINES TERMINATED BY  '字符串' ：设置每行的结束符，默认 '\n'

下面一些例子：

```sql
mysql> select * from pet into outfile '.\t_pet.sql' LINES TERMINATED BY  '\r\n' 
```

### 2、使用 mysqldump 导出

```bash
# mysqldump -uroot -p -T targetfilename dbname tablename [option]
# mysqldump -uroot -p --xml | -X dbname tablename [option] > filename			# 导出 XML格式

# option 有：(需用双引号括起来)
--fields-terminated-by=字符串 ： 设置字符串为字段的分隔符
--fields-enclosed-by=字符 ： 设置字符来括上字段的值
--fields-optionally-enclosed-by=字符 ：设置字符来括上 CHAR、VARCHAR、TEXT等字符型字段。默认不使用任何字符
--fields-escaped-by=字符 ：设置转义字符
--lines-terminated-by=字符串 ： 设置每行的结束符

# mysqldump -uroot -p -T ".\t_pet.sql" menagerie pet "--lines-terminated-by=\r\n" "--fields-terminated-by=,"
```

### 3、使用 mysql 导出

使用 mysql 命令加 linux 的管道方式导出表数据到文件中。

```bash
# mysql -uroot -p -e "select * from tablename" dbname > filename						# -e 选项可以执行 SQL 语句
# mysql -uroot -p --xml | -X -e "select * from tablename" dbname > filename				# 导出XML格式
# mysql -uroot -p --html | -H -e "select * from tablename" dbname > filename			# 导出HTML格式
```

### 4、 用 LOAD DATA INFILE 导入

将文本文件中的数据，导入数据库中。使用 load data infile 方式导入。

```sql
mysql> LOAD DATA LOCAL INFILE filename INTO TABLE tablename [OPTION];

# OPTION 选项有：
# FIELDS TERMINATED BY  '字符串' ：设置字符串为字段的分隔符。默认 '\t'
# FIELDS ENCLOSED BY  '字符' ：设置字符来括上字段的值。默认不使用任何字符
# FIELDS ESCAPED BY  '字符' ：设置转义字符，默认 '\'
# FIELDS OPTIONALLY ENCLOSED BY  '字符' ：设置字符来括上 CHAR、VARCHAR、TEXT等字符型字段。默认不使用任何字符
# LINES STARTING BY  '字符串' ：设置每行开头的字符，默认情况下无任何字符
# LINES TERMINATED BY  '字符串' ：设置每行的结束符，默认 '\n'
# IGNORE n LINES ：忽略文件的前 n 行记录
# SET column=expr ：将指定的列 column 进行相应地转换后在加载，使用 expr 表达式进行转换

# 例子
mysql> LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet;
```

### 5、使用 mysqlimport 命令导入

将文本文件导入至数据库中，还可以使用 MySQL 自带的命令 mysqlimport 导入

```
# mysqlimport -uroot -p [--LOCAL] dbname file [OPTION]
```

mysqlimport 使用上与 mysqldump 类似， OPTION 选项也是一样。

## 四、实际操作

```bash
# mysqldump -uroot -p menagerie > Backup_menagerie.sql						# 只备份表，不备份库
Enter password: 

# mysqldump -uroot -p --databases menagerie > Backup_menagerie.sql			# 备份表也备份库
Enter password: 

# vim Backup_menagerie.sql
-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: menagerie
-- ------------------------------------------------------
-- Server version>--5.7.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `menagerie`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `menagerie` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `menagerie`;

...

# 查看备份的sql文件，以“--” 开头的都是SQL语言的注释。
# 以 “/*!40101” 等形式开头的是与MySQL有关的注释。 40101 表示数据库的版本 4.1.1。还原时，如果MySQL的版本高于 4.1.1，则 “/*!40101” 和 “*/” 之间的内容被当做SQL命令执行，如果低于这个版本，则内容被当做注释看待。 “/*!32312” 也是类似含义。

#############################

# mysqlpump 压缩备份 employees 数据库 三个并发线程备份，消耗时间：10707 ms
# mysqlpump -uroot -p -h192.168.19.130 --single-transaction --default-character-set=utf8 --compress-output=LZ4 --default-parallelism=3 -B employees > employees_db.sql.lz4
Enter password: 
Dump progress: 1/3 tables, 0/331603 rows
Dump progress: 2/6 tables, 140000/3900908 rows
Dump progress: 2/6 tables, 590000/3900908 rows
Dump progress: 4/6 tables, 1057377/3900908 rows
Dump progress: 4/6 tables, 1447877/3900908 rows
Dump progress: 4/6 tables, 1751627/3900908 rows
Dump progress: 5/6 tables, 2083185/3900908 rows
Dump progress: 5/6 tables, 2504185/3900908 rows
Dump progress: 5/6 tables, 2978435/3900908 rows
Dump progress: 5/6 tables, 3480435/3900908 rows
Dump completed in 10707 milliseconds

# mysqlpump 压缩备份 所有数据库 三个并发线程备份，消耗时间：4657 ms
# mysqlpump -uroot -p -h192.168.19.130 --single-transaction --default-character-set=utf8 --compress-output=LZ4 --default-parallelism=3 --all-databases > all_db.sql.lz4
Enter password: 
Dump progress: 1/1 tables, 0/9 rows
Dump progress: 24/26 tables, 1493543/3903756 rows
Dump progress: 29/30 tables, 2358414/3909297 rows
Dump progress: 29/30 tables, 3083664/3909297 rows
Dump progress: 29/30 tables, 3829414/3909297 rows
Dump completed in 4657 milliseconds

# mysqldump 压缩备份 所有数据库 单个线程备份，消耗时间：13s 。 mysqlpump 备份数量很多时优势明显！
# time mysqldump -uroot -p -h192.168.19.130 --default-character-set=utf8 -P3306 --skip-opt --add-drop-table --create-options  --quick --extended-insert --single-transaction --all-databases | gzip > all.sql.gz
Enter password: 

real	0m13.752s
user	0m11.360s
sys	0m3.600s


```

