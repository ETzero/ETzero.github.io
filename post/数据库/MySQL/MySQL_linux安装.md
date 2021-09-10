# MySQL linux 安装

## MySQL client linux 安装

### 一、离线方式

#### 1、下载安装包

```bash
# MySQL-common
mysql-community-common-5.7.27-1.el7.x86_64.rpm
# MySQL-libs
mysql-community-libs-5.7.27-1.el7.x86_64.rpm
# MySQL-client
mysql-community-client-5.7.27-1.el7.x86_64.rpm
# MySQL-devel
mysql-community-devel-5.7.27-1.el7.x86_64.rpm
# MySQL-odbc
mysql-connector-odbc-8.0.17-1.el7.x86_64.rpm
# unixODBC
使用 yum 安装，不必下载
```

#### 2、安装

```bash
# yum install unixODBC.x86_64
# yum install unixODBC-devel.x86_64
# 安照如下顺序安装
# rpm -ivh mysql-community-common-5.7.27-1.el7.x86_64.rpm
# rpm -ivh mysql-community-libs-5.7.27-1.el7.x86_64.rpm
# rpm -ivh mysql-community-client-5.7.27-1.el7.x86_64.rpm
# rpm -ivh mysql-community-server-5.7.27-1.el7.x86_64.rpm(安装客户端不需要安装这个)
# rpm -ivh mysql-community-devel-5.7.27-1.el7.x86_64.rpm
# rpm -ivh mysql-connector-odbc-8.0.17-1.el7.x86_64.rpm
```

当你安装第二个rpm时，会报出下列错误：

```bash
# rpm -ivh mysql-community-libs-5.7.27-1.el7.x86_64.rpm  
error: Failed dependencies:
	mariadb-libs is obsoleted by mysql-community-libs-5.7.27-1.el7.x86_64
```

出现依赖冲突，因为CentOS的默认数据库已经不再是MySQL了，而是MariaDB，为什么呢？ 
MariaDB数据库管理系统是MySQL的一个分支，主要由开源社区在维护，采用GPL授权许可。开发这个分支的原因之一是：甲骨文公司收购了MySQL后，有将MySQL闭源的潜在风险，因此社区采用分支的方式来避开这个风险。MariaDB的目的是完全兼容MySQL，包括API和命令行，使之能轻松成为MySQL的代替品。 （摘自：[CentOS 7 rpm 安装MySQL 详解](<https://blog.csdn.net/yangjjuan/article/details/61615187>)）
查看当前安装的mariadb包：

```bash
# rpm -qa | grep mariadb
mariadb-libs-5.5.60-1.el7_5.x86_64

# 将其删除
# rpm -e --nodeps mariadb-libs-5.5.60-1.el7_5.x86_64

# 然后继续重新按顺序安装
```

#### 3、配置odbc

此处大家注意下5a 5s 5w之间的区别（根据数据库的不同编码格式选择动态库，否则会出现中文乱码）:

- libmyodbc5a.so 是ASCII编码格式  
- libmyodbc5w.so 是UNICODE编码格式  
- libmyodbc5s.so  是程序开发中配置数据源提供界面的动态链接库
  

```bash
# 查看odbc配置文件路径
# odbcinst -j
unixODBC 2.3.1
DRIVERS............: /etc/odbcinst.ini
SYSTEM DATA SOURCES: /etc/odbc.ini
FILE DATA SOURCES..: /etc/ODBCDataSources
USER DATA SOURCES..: /root/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8


# 查找 odbc 库路径
# find / -name "libmyodbc*"
/usr/lib64/libmyodbc8a.so
/usr/lib64/libmyodbc8w.so

```

##### odbcinst.ini 配置

```bash
#vim /etc/odbcinst.ini
# 新增 [MySQL8]
[PostgreSQL]
Description=ODBC for PostgreSQL
Driver=/usr/lib/psqlodbcw.so
Setup=/usr/lib/libodbcpsqlS.so
Driver64=/usr/lib64/psqlodbcw.so
Setup64=/usr/lib64/libodbcpsqlS.so
FileUsage=1

[MySQL]
Description=ODBC for MySQL
Driver=/usr/lib/libmyodbc5.so
Setup=/usr/lib/libodbcmyS.so
Driver64=/usr/lib64/libmyodbc5.so
Setup64=/usr/lib64/libodbcmyS.so
FileUsage=1

[MySQL8]		(新增)
Description=ODBC 8.0 for MySQL
Driver=/usr/lib64/libmyodbc8w.so
Setup=/usr/lib/libodbcmyS.so
Driver64=/usr/lib64/libmyodbc8w.so
Setup64=/usr/lib64/libodbcmyS.so
FileUsage=1

[MySQL ODBC 8.0 Unicode Driver]
Driver=/usr/lib64/libmyodbc8w.so
UsageCount=1

[MySQL ODBC 8.0 ANSI Driver]
Driver=/usr/lib64/libmyodbc8a.so
UsageCount=1
```

#####  odbc.ini 配置

- Driver 为 odbcinst.ini 中的配置 MySQL，也可以使用 /usr/lib/libmyodbc5.so 代替，即可以不配置 odbcinst.ini 

- Charset是字符集

- server是服务器主机名（可以解析）或IP

```bash
# vim /etc/odbc.ini
# 添加如下内容
[NEWDB]
Description = whatever
Trace = On
TraceFile = stderr
Driver = MySQL8				(odbcinst.ini 中的MySQL8)
SERVER = 172.26.1.180
USER = username
PASSWORD = passwd
PORT = 3306
DATABASE = db_sid
CHARSET= UTF8
OPTION = 3
```

#### 4、测试连接

```bash
# isql -v NEWDB
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+

# mysql -uroot -h172.26.1.180 -p
```

## MySQL server linux 安装

### 二、在线方式

#### 1、配置 yum 源

yum 源的 rpm包，可以从官方网站上下载再安装，也可以使用命令下载（下载对于版本）

```bash
# wget -c https://dev.mysql.com/get/mysql57-community-release-el7-{version-number}.noarch.rpm
```

安装命令将MySQL Yum存储库添加到系统的存储库列表中，并下载GnuPG密钥以检查软件包的完整性。

```bash
# yum localinstall mysql57-community-release-el7-{version-number}.noarch.rpm
# 检查MySQL Yum存储库是否已成功添加
# yum repolist enabled | grep "mysql.*-community.*"
```

#### 2、配置版本

使用MySQL Yum存储库时，默认情况下会选择安装最新的GA系列（当前为MySQL 5.7）
如果需要使用旧版本，则可以用如下命令：

```bash
# yum-config-manager --disable mysql57-community
# yum-config-manager --enable mysql56-community
```

也可以通过手动编辑`/etc/yum.repos.d/mysql-community.repo` 文件来选择发布系列 。

```bash
[mysql57-community]
name=MySQL 5.7 Community Server
baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql

# Enable to use MySQL 5.6
[mysql56-community]
name=MySQL 5.6 Community Server
baseurl=http://repo.mysql.com/yum/mysql-5.6-community/el/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
```

任何时候为一个发布系列启用子存储库。当启用多个版本系列的子存储库时，Yum将使用最新的系列。
以下命令检查其输出来验证是否已启用和禁用了正确的子存储库

```bash
# yum repolist enabled | grep mysql
```

#### 3、安装

这将安装MySQL server（`mysql-community-server`）的包以及运行服务器所需组件的包，包括client（`mysql-community-client`）的包，客户端和服务器的常见错误消息和字符集（`mysql-community-common`）以及共享客户端库（`mysql-community-libs`）

```bash
# yum install mysql-community-server
```

可以使用Yum来安装和管理MySQL的各个组件。其中一些组件托管在MySQL Yum存储库的子存储库

```bash
# yum install mysql-community-libs
# yum install mysql-workbench-community
```

#### 4、初始化数据目录

通用二进制和源代码发行版方式安装的mysql，需要初始化数据目录。
在数据目录中，服务器创建 `mysql`系统数据库及其表，包括授权表，时区表和服务器端帮助表。

yum源方式安装，会自动初始化数据目录，无须再手动初始化。

```sql
# 进入mysql命令行后，通过以下命令查看数据目录的位置
mysql> show variables like '%datadir%'
```

#### 5、启动MySQL服务器

```bash
# systemctl start mysqld
```

在服务器初始启动时，如果服务器的数据目录为空，则会发生以下情况：

- 服务器已初始化。
- SSL证书和密钥文件在数据目录中生成。
- [`validate_password`](https://dev.mysql.com/doc/refman/5.7/en/validate-password.html) 已安装并已启用。
- 将`'root'@'localhost`创建一个超级用户帐户。设置超级用户的密码并将其存储在错误日志文件中

> [`validate_password`](https://dev.mysql.com/doc/refman/5.7/en/validate-password.html) 默认安装。实现的默认密码策略`validate_password`要求密码包含至少一个大写字母，一个小写字母，一个数字和一个特殊字符，并且总密码长度至少为8个字符。

使用 root 用户登陆时，需要知道服务器为 root 创建的随机 密码。使用以下命令可以在错误日志中显示出来

```bash
# grep 'temporary password' /var/log/mysqld.log
# 登陆服务器, 不带 -h 默认使用 localhost
# mysql -uroot -p
```

登陆mysql服务器后，需要尽快修改密码，密码满足 `validate_password` 的要求即可。

```sql
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'YourPassword';
```

#### 6、测试服务器

使用[**mysqladmin**](https://dev.mysql.com/doc/refman/5.7/en/mysqladmin.html)验证服务器是否正在运行。以下命令提供简单的测试。

```bash
# mysqladmin -u root -p version
Enter password: 
mysqladmin  Ver 8.42 Distrib 5.7.27, for Linux on x86_64
Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Server version		5.7.27
Protocol version	10
Connection		Localhost via UNIX socket
UNIX socket		/var/lib/mysql/mysql.sock
Uptime:			1 hour 15 min 7 sec

Threads: 2  Questions: 46  Slow queries: 0  Opens: 137  Flush tables: 1  Open tables: 130  Queries per second avg: 0.010

# 测试关闭服务
# mysqladmin -u root -p shutdown
Enter password: (enter root password here)
```

### 三、安装包方式

#### 1. 准备

```bash
# Mysql目录安装位置：/usr/local/mysql
# 数据库保存位置：/data/mysql
# 日志保存位置：/data/log/mysql
$ mkdir -p /usr/local/mysql
$ mkdir -p /data/mysql
$ mkdir -p /data/log/mysql

# 检查是否已经安装过mysql
$ rpm -qa | grep mysql

# 删除旧版本
# 通过whereis mysql 和 find / -name mysql查找，删除相关
$ rpm -e --nodeps mysql-libs-版本

# 检查mysql用户组和用户，没有则创建
$ cat /etc/group | grep mysql
$ cat /etc/passwd |grep mysql
$ groupadd mysql
$ useradd -r -g mysql mysql
# 新建msyql用户禁止登录shell
$ useradd -r -s /sbin/nologin -g mysql mysql -d /usr/local/mysql
```

#### 2. 安装包下载、解压、存储

```bash
# 下载安装包
$ wget http://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.17-linux-glibc2.5-x86_64.tar.gz

# 解压并拷贝到指定目录
$ tar -xzvf /data/software/mysql-5.7.17-linux-glibc2.5-x86_64.tar.gz
# 移动并修改文件名
$ mv /data/software/mysql-5.7.17-linux-glibc2.5-x86_64 /usr/local/mysql

# 改变目录属有者
$ cd /usr/local/mysql
$ pwd
$ chown -R mysql .
$ chgrp -R mysql .
$ chown -R mysql /data/mysql
```

#### 3. 配置参数

```bash
# 配置参数
# 编译安装并初始化mysql,务必记住初始化输出日志末尾的密码（数据库管理员临时密码root@localhost:后的字符串）
$ cd /usr/local/mysql/
$ bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql --datadir=/data/mysql
#$ bin/mysql_ssl_rsa_setup  --datadir=/data/mysql
```

#### 4. 启动

```bash
# 启动mysql服务器
$ /usr/local/mysql/support-files/mysql.server start
# 如果出现如下提示信息
Starting MySQL.Logging to '/usr/local/mysql/data/iZge8dpnu9w2d6Z.err'.
# 查询服务
$ ps -ef|grep mysql
$ ps -ef|grep mysqld

# 结束进程
$ kill -9 PID

# 添加软连接，并重启mysql服务
$ ln -s /usr/local/mysql/support-files/mysql.server /etc/init.d/mysql 
$ ln -s /usr/local/mysql/bin/mysql /usr/bin/mysql
$ service mysql restart
```

#### 5. 登陆

```bash
# 如果出现：-bash: mysql: command not found
# 就执行：ln -s /usr/local/mysql/bin/mysql /usr/bin
# 没有出现就不用执行
$ mysql -hlocalhost -uroot -p
Enter password: 输入配置参数时生成的临时密码
mysqladmin  Ver 8.42 Distrib 5.7.27, for Linux on x86_64
Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
mysql> 
```

#### 6. 登陆后设置MySQL

```bash
# 修改密码
mysql> set password=password('root');

# 设置root账户的host地址（修改了才可以远程连接）
mysql> grant all privileges on *.* to 'root'@'%' identified by 'root';
mysql> flush privileges;

# 查看表
mysql> use mysql;
mysql> select host,user from user;

# 开放远程连接
>use mysql;
>update user set user.Host='%' where user.User='root';
>flush privileges;

#退出mysql命令窗口
mysql> exit

# 如提示不能成功连接，可能需要添加需要监听的端口
$ /sbin/iptables -I INPUT -p tcp --dport 3306 -j ACCEPT
```

#### 7. 设置开机自启

```bash
# 添加系统路径
$ vim /etc/profile
# 添加： export PATH=/usr/local/mysql/bin:$PATH
$ source /etc/profile

# 配置mysql自动启动
# 1. 将服务文件拷贝到init.d下，并重命名为mysqld
$ cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld
$ cp /usr/local/mysql/support-files/my-default.cnf /etc/my.cnf

# 2. 修改系统配置文件
$ vim /etc/init.d/mysqld
# 修改以下内容：
basedir=/usr/local/mysql
datadir=/data/mysql

# 3. 赋予可执行权限
$ chmod 755 /etc/init.d/mysqld
# 4. 添加服务
$ chkconfig --add mysqld
$ chkconfig --level 345 mysqld on


# 查看mysql状态
$ service mysqld status
$ systemctl status mysqld

# 停止mysql
$ service mysqld stop

# 启动mysql
$ service mysqld start

```
