# MySQL 用户管理

## 一、权限表

Mysql 数据库安装后，会有四个系统数据库，其中一个 `mysql` 库，该数据库下存储的表，基本是权限相关的表。有31张表。

```sql
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> use mysql;
mysql> show tables;
.......（此处省略）
31 rows in set (0.00 sec)
```

用户登录Mysql后，系统会根据这些权限表的内容为每个用户赋予相应的权限。

这其中，经常使用的表有：

```bash
# 经常使用到的是 mysql 库下的表
# user						# 用户帐户，全局权限和其他非特权列。
# db							# 数据库级权限。
# tables_priv			# 表级权限。
# columns_priv		# 列级权限。
# procs_priv			# 存储过程和功能权限.
# proxies_priv		# 代理用户权限

# event				# 有关事件计划程序事件的信息
# func				# 有关用户定义函数（UDF）的信息
# plugin			# 有关服务器端插件的信息
# proc				# 有关存储过程和函数的信息

# general_log		# 常规查询日志表
# slow_log			# 慢查询日志表
```

### 1、user 表

user 表是MySQL 中最重要的表，其有45个字段，大致可以分为四类：**用户列、权限列、安全列、资源控制列**。

```sql
mysql> desc user;
.......（此处省略）
45 rows in set (0.00 sec)
```


#### 用户列

用户列 有：

```bash
Host								# 主机名
User								# 用户名
authentication_string				# 密码
password_expired						# 密码是否过期
password_last_changed				# 密码最后修改时间
password_lifetime						# 密码有效期
account_locked							# 账户是否锁定标识
```

#### 权限列

权限列，字段名的后缀带有 _priv 的为权限列。权限列限定了用户的各种权限。其取值为 'Y' 或者 'N'。比如 `Select_priv` 表示用户的查询权限。以下列出几个常见的：

```bash
Select_priv             # 查询数据权限
Insert_priv             # 插入数据权限
Update_priv             # 更新数据权限
Delete_priv             # 删除数据权限
Create_priv             # 创建表、数据库权限
Drop_priv               # 删除权限
Reload_priv             # 刷新和重新加载MySQL所用各种内部缓存的特定命令权限
Shutdown_priv           # 关闭MySQL 服务权限
Process_priv            # 通过SHOW PROCESSLIST命令查看其他用户的进程 权限
File_priv               # 执行SELECT INTO OUTFILE和LOAD DATA INFILE命令 权限
Grant_priv              # 确定用户是否可以将已经授予给该用户自己的权限再授予其他用户
References_priv         # 不知道
Index_priv              # 索引权限
Alter_priv              # alter 使用权限
Show_db_priv            # 访问所有数据权限
Super_priv              # 超级权限
Create_tmp_table_priv   # 创建临时表权限
Lock_tables_priv        # 使用LOCK TABLES命令阻止对表的访问/修改 权限
Execute_priv            # 可执行权限, 用户执行存储过程和函数
Repl_slave_priv         # 是否可以读取用于维护复制数据库环境的二进制日志文件。此用户位于主系统中，有利于主机和客户机之间的通信
Repl_client_priv        # 是否可以确定复制从服务器和主服务器的位置
Create_view_priv        # 创建视图权限
Show_view_priv          # 查询视图权限
Create_routine_priv     # 是否可以更改或放弃存储过程和函数
Alter_routine_priv      # 是否可以修改或删除存储函数及函数
Create_user_priv        # 创建用户权限
Event_priv              # 能否创建、修改和删除事件
Trigger_priv            # 触发器权限
Create_tablespace_priv  # 创建表空间权限
```

#### 安全列

安全列，有：

```bash
ssl_type       # SSL 类型
ssl_cipher     # SSL 使用的加密算法？
x509_issuer    # x509标准可以用来标识用户
x509_subject   # x509标准可以用来标识用户
```

#### 字段控制列

```bash
max_questions          # 每小时可以运行执行多少次查询
max_updates            # 每小时可以运行执行多少次更新
max_connections        # 每小时可以建立多少连接
max_user_connections   # 单个用户同时具有的连接数
plugin                 # 插件
```

### 2、db 表 

db 表存储了某个用户对一个数据库的权限。db 表有 22 个字段，字段可以分为两类：用户列和权限列。权限列限定了用户对于一个数据库所拥有的权限，如 Select_priv , 表示用户对该数据库下所有的表是否拥有查询权限。

```bash
Host                  # 主机名
Db                    # 数据库名
User                  # 用户名
Select_priv           # (对数据库的)查询权限
Insert_priv           # 插入权限
Update_priv           # 更新权限
Delete_priv           # 删除数据权限
Create_priv           # 新建表权限
Drop_priv             # 删除权限
Grant_priv            # 使用 grant 权限
...
```

### 3、tables_priv 表 和 columns_priv 表

- tables_priv 表 存储了某个用户对一张表的权限。
- columns_priv 表存储了某个用户对一张表中的单个数据列的权限。

```bash
# tables_priv 表 包含8个字段
Host        	# 主机名
Db          	# 数据库名
User        	# 用户名
Table_name  	# 表名
Grantor     	# 权限的设置者
Timestamp   	# 修改权限的时间
Table_priv  	# 对表进行操作的权限(Select,Insert,Update,Delete,Create,Drop,Grant,References,Index,Alter,Create View,Show view,Trigger)
Column_priv 	# 对表中的数据列进行操作的权限(Select,Insert,Update,References)

# columns_priv 表 包含7个字段
Host        	# 主机名
Db          	# 数据库名
User        	# 用户名
Table_name  	# 表名
Column_name  	# 表字段名
Timestamp   	# 修改权限的事件
Column_priv 	# 对表中的数据列进行操作的权限(Select,Insert,Update,References)
```
### 4、procs_priv 表

procs_priv 表存储了用户对存储过程和函数的权限。

```bash
# procs_priv  表 包含8个字段
Host        		# 主机名
Db          		# 数据库名
User        		# 用户名
Routine_name  	# 存储过程或函数的名称
Routine_type    # 类型(FUNCTION, PROCEDURE)
Grantor   			# 权限的设置者
Proc_priv  			# 权限(Execute, Alter Routine ,Grant)
Timestamp 			# 修改权限的时间
```

**MySQL权限分配是按照user表 ---》 db表 ---》 table_priv表 --》 columns_priv表 的顺序进行分配的。**

**在数据库系统中，先判断user表中的值是否为'Y'，如果user表中的值是'Y'，就不需要检查后面的表。如果user表为N，则一次检查后面的表。**

MySQL 系统通过上面的几张表，实现了一个用户的权限配置。

## 二、账户管理

 账户管理包括：创建用户、删除用户、密码管理、权限管理。

### 1、创建用户

#### 使用 create user 创建用户

```sql
mysql> create user 'username'@'host' IDENTIFIED BY [PASSWORD] 'yourpassword';
mysql> create user 'test1'@'localhost' IDENTIFIED BY '12345678';
mysql> create user 'test2'@'localhost' IDENTIFIED BY PASSWORD('test1'),  user 'test2'@'localhost';			# 可以创建多个用户
```

#### 使用 insert 创建用户

```sql
mysql> insert into mysql.user(Host,User,authentication_string, ssl_cipher,x509_issuer,x509_subject) VALUES('localhost','newuser1',PASSWORD('12345678'),'','','')		  # ssl_cipher,x509_issuer,x509_subject 必须设置
mysql> flush privileges;											  # 重新装载权限, 需要 reload 权限 
```

#### 使用 grant 创建用户

```sql
mysql> GRANT priv_type ON database.table TO 'username'@'host' IDENTIFIED BY [PASSWORD] 'yourpassword';	# priv_type为权限 
mysql> GRANT SELECT ON *.* TO 'test3'@'%' IDENTIFIED BY 'test3';		# *.*表示所有数据库所有表, % 表示任意主机
```

### 2、删除用户

#### 使用 drop user 删除用户

```sql
mysql> drop user 'username'@'host';
mysql> drop user 'test4'@'localhost';
```

#### 使用 delete 删除用户

```sql
mysql> delete from mysql.user where Host='hostname' and User = 'username';
mysql> flush privileges;											# 重新装载权限, 需要 reload 权限 
```

### 3、密码管理

#### root 修改自己密码

```bash
# 方式一：使用命令行工具 mysqladmin
# mysqladmin -u username -p password "new_password"

# 方式二: 修改 user表
mysql> UPDATE mysql.user set authentication_string=PASSWORD("new_password") where User='username' and Host = 'hostname';
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';

# 方式三：使用root登录后，使用 SET 命令
mysql> SET PASSWORD = PASSWORD("new_password");
```

#### root 修改其他用户密码

```sql
# 方式一：使用 grant 修改
mysql> GRANT priv_type ON database.table TO 'username'@'host' IDENTIFIED BY [PASSWORD] 'yourpassword';

# 方式二: 修改 user表
mysql> UPDATE mysql.user set authentication_string=PASSWORD("new_password") where User='username' and Host = 'hostname';
mysql> ALTER USER 'username'@'host' IDENTIFIED BY 'NewPassword';

# 方式三：使用root登录后，使用 SET 命令
mysql> SET PASSWORD FOR 'username'@'host' = PASSWORD("new_password");
```

#### 普通用户修改自己密码

```sql
# 使用用户登录后，使用 SET 命令
mysql> SET PASSWORD = PASSWORD("new_password");
```

#### 忘记 root 密码

```bash
# 忘记 root 密码，无法登陆
# 参考官网：https://dev.mysql.com/doc/refman/5.7/en/resetting-permissions.html

# vim /etc/my.conf
# 添加以下内容
[mysqld]
skip-grant-tables			# 以不检查权限表方式启动mysql server
:wq
# systemctl restart mysqld										# 重启mysql server
# mysql_safe --skip-grant-tables user=mysql		# 以参数方式启动, 这样就不用改 my.conf
# mysql -uroot																# 不使用密码登陆
mysql> FLUSH PRIVILEGES;											# 重新加载授权表
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';	# 修改新密码
```

## 三、权限管理

### 1、权限列表

下面列出了MySQL的各种权限。Grant 命令中的 `priv_type` 就是对应列表的第一列。（参考官方：[Privileges Provided by MySQL](<https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_alter-routine>)）

| 权限名称 |对应user表中的列      |权限的范围      |
| :--- | :--- | :--- |
| ALL [PRIVILEGES] |Synonym for “all privileges” |服务器管理 |
| USAGE |Synonym for “no privileges” |服务器管理 |
| EVENT |Event_priv |数据库 |
| PROXY |See `proxies_priv` table |服务器管理 |
|	CREATE						|	Create_priv				|	数据库、表或索引			  |
|	DROP						|	Drop_priv				|	数据库或表                    |
|	GRANT OPTION				|	Grant_priv				|	数据库、表、存储过程或函数    |
|	REFERENCES					|	References_priv			|	数据库或表                    |
|	ALTER						|	Alter_priv				|	修改表                        |
|	DELETE						|	Delete_priv				|	删除表                        |
|	INDEX						|	Index_priv				|	用索引查询表                  |
|	INSERT						|	Insert_priv				|	插入表                        |
|	SELECT						|	Select_priv				|	查询表                        |
|	UPDATE						|	Update_priv				|	更新表                        |
|	CREATE TABLESPACE	|	Create_tablespace_priv	|	服务器管理 |
|	CREATE VIEW					|	Create_view_priv		|	创建视图                      |
|	SHOW VIEW					|	Show_view_priv			|	查看视图                      |
|	ALTER ROUTINE				|	Alter_routine			|	修改存储过程或存储函数        |
|	CREATE ROUTINE				|	Create_routine_priv		|	创建存储过程或存储函数        |
|	EXECUTE						|	Execute_priv			|	执行存储过程或存储函数        |
|	FILE						|	File_priv				|	加载服务器主机上的文件        |
|	CREATE TEMPORARY TABLES		|	Create_temp_table_priv	|	创建临时表                    |
|	LOCK TABLES					|	Lock_tables_priv		|	锁定表                        |
|	CREATE USER					|	Create_user_priv		|	创建用户                      |
|	PROCESS						|	Process_priv			|	服务器管理                    |
|	TRIGGER	|	Trigger_priv	|	表 |
|	RELOAD						|	Reload_priv				|	重新加载权限表                |
|	REPLICATION CLIENT			|	Repl_client_priv		|	服务器管理                    |
|	REPLICATION SLAVE			|	Repl_slave_priv			|	服务器管理                    |
|	SHOW DATABASES				|	Show_db_priv			|	查看数据库                    |
|	SHUTDOWN					|	Shutdown_priv			|	关闭服务器                    |
|	SUPER						|	Super_priv				|	超级权限                      |

### 2、授权

授权就是给某个用户赋予某些权限。可以给多个用户同时授权。授权操作必须拥有 GRANT 权限的用户才可以执行 grant 语句。

```sql
mysql> GRANT priv_type [(column_list)] ON database.table TO user [IDENTIFIED BY [PASSWORD] 'password']
[,user [IDENTIFIED BY [PASSWORD] 'password']]... WITH with_option[with_option]				# column_list 表示权限作用于哪些列上
```

with_option 有以下选项：

- GRANT OPTION ：被授权的用户可以将这些权限赋予给别的用户
- MAX_QUERIES_PER_HOUR count ：设置每小时可以允许执行count次查询
- MAX_UPDATES_PER_HOUR count ：设置每小时可以允许执行count次更新
- MAX_CONNECTIONS_PER_HOUR count ：设置每小时可以建立count个连接
- MAX_USER_CONNECTIONS count ：设置单个用户可以同时具有的count个连接数

下面看一些例子

```sql
mysql> GRANT SELECT, UPDATE ON *.* TO 'test5'@'localhost' WITH GRANT OPTION;
mysql> GRANT SELECT, UPDATE ON menagerie.pet TO 'test6'@'localhost' WITH GRANT OPTION MAX_QUERIES_PER_HOUR 100 MAX_UPDATES_PER_HOUR 100;
mysql> GRANT SELECT (owner, death) ON menagerie.pet TO 'test6'@'localhost' WITH MAX_QUERIES_PER_HOUR 100;
```

### 3、回收权限

回收权限，就是取消某个用户的某些权限。可以同时回收多个用户的权限。

```sql
mysql> REVOKE priv_type [(column_list)] ON database.table FROM user [,user]
mysql> REVOKE ALL PRIVILEGES, GRANT OPTION FROM user [,user]			# 回收全部权限

mysql> REVOKE UPDATE, INSERT ON *.* FROM 'test7'@'localhost', 'test8'@'localhost';
```

### 4、查看权限

```sql
mysql> select * from mysql.user;
mysql> SHOW GRANTS FOR 'username'@'host';
```

