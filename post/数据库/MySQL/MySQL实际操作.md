# Mysql 实际操作

### 加载 Mysql 官方 World 数据

mysql 官方提供了几个样本数据，用于测试使用mysql。详细地址在官网： [Other MySQL Documentation](<https://dev.mysql.com/doc/index-other.html>) 。

```bash
# wget -c https://downloads.mysql.com/docs/world_x-db.tar.gz
# tar -zxvf world_x-db.tar.gz
# cd world_x-db
# ls -al
-rwxr-xr-x. 1  500  500   1432 Jun 15  2018 README.txt
-rwxr-xr-x. 1  500  500 389282 Jun 15  2018 world_x.sql
# 方式一，mysql 批处理方式
# mysqlsh -u root --sql --recreate-schema world_x < /path/world_x.sql

# 方式二，登陆 mysql 后载入数据
# mysql -uroot -p
Enter password:
mysql> SOURCE /path/world_x.sql;

mysql> show databases;
| world_x            |

mysql> use world_x;
mysql> show tables;
+-------------------+
| Tables_in_world_x |
+-------------------+
| city              |
| country           |
| countryinfo       |
| countrylanguage   |
+-------------------+

```

### 加载 Mysql 官方 employee 数据

```bash
# git clone https://github.com/datacharmer/test_db.git
# mysql -uroot -p -t < employees.sql
Enter password:

# mysql -uroot -p -t < test_employees_md5.sql		校验数据
# mysql -uroot -p -t < test_employees_sha.sql		校验数据
```

### 修改 mysql root 密码

```bash
# 忘记 root 密码，无法登陆
# 参考官网：https://dev.mysql.com/doc/refman/5.7/en/resetting-permissions.html

# vim /etc/my.conf
# 添加以下内容
[mysqld]
skip-grant-tables			# 以不检查权限表方式启动mysql server
:wq
# systemctl restart mysqld	# 重启mysql server
# mysql -uroot				# 不使用密码登陆
> FLUSH PRIVILEGES;			# 重新加载授权表
> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';	# 修改新密码

```

### 密码策略问题异常信息

```sql
mysql> create user 'test1'@'localhost' IDENTIFIED BY 'test1';
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements

# 报上述异常，是因为密码的规范，不符合当前设置的密码安全策略。
# 首先查看当前的密码策略
mysql> SHOW VARIABLES LIKE 'validate_password%';
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password_check_user_name    | OFF    |
| validate_password_dictionary_file    |        |
| validate_password_length             | 8      |
| validate_password_mixed_case_count   | 1      |
| validate_password_number_count       | 1      |
| validate_password_policy             | MEDIUM |
| validate_password_special_char_count | 1      |
+--------------------------------------+--------+

# validate_password_check_user_name			表示是否能将密码设置成当前用户名; ON 表示能
# validate_password_dictionary_file			指定密码验证的文件路径
# validate_password_length					固定密码的总长度（默认密码的长度最小值为 4）
# validate_password_mixed_case_count		整个密码中至少要包含大/小写字母的总个数
# validate_password_number_count			整个密码中至少要包含阿拉伯数字的个数
# validate_password_policy					指定密码的强度验证等级，默认为 MEDIUM。（0/LOW；1/MEDIUM；2/STRONG）
# validate_password_special_char_count		整个密码中至少要包含特殊字符的个数

# 使用如下命令修改相应的策略即可
mysql> set global validate_password_policy=LOW;
mysql> set global validate_password_length=6;
```

### 远程连接 mysql 失败

```sql
# mysql -h host -u username -p
Enter password:
ERROR 1130 (HY000): Host '192.168.0.1' is not allowed to connect tothis MySQLserver

# 因为系统数据库mysql中user表中，该username限定了连接的host 是localhost的原因

# 方式一：修改 user表中的 Host字段为 '%' 表示任意主机
# mysql -u root -p
Enter password:
mysql> use mysql;
mysql> update user set Host = '%' where User = 'root';
mysql> flush privileges;

# 方式二：授权用户权限
# mysql -u root -p
Enter password:
mysql> GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%';				# 授权用户可以从任何主机上远程连接
mysql> GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'192.168.0.1';	# 授权用户可以从192.168.1.3 的主机上远程连接

# 方式三：修改系统变量（不建议修改系统变量）
# mysql -u root -p
Enter password:
mysql> use mysql；
mysql> update user sethost='123.456.789.254';		# IP为你想要远程连接数据库的本地机器的IP
```



