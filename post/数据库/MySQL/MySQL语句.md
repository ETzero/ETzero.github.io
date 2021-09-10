# MySQL 语句

## SQL语句组成

- DDL：数据定义语言，用于定义数据库、表、索引和触发器等，包括`create`、`alter`、`drop`等
- DML：数据操作语言，用于操作数据库数据，有`select`、`delete`、`update`、`insert`
- DCL：数据控制语言，用于控制用户的访问权限，包括`grant`、`revoke`等

### DDL 语句

- [ALTER DATABASE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-database.com.coder114.cn.html)：可以更改数据库的整体特征
- [ALTER EVENT](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-event.com.coder114.cn.html)：更改现有事件的一个或多个特性，而无需删除和重新创建它
- [ALTER FUNCTION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-function.com.coder114.cn.html)：改变存储函数的特性。`ALTER FUNCTION`声明中可能会指定多个更改 。但是，您不能使用此语句更改存储函数的参数或主体; 要进行这样的更改，必须使用`DROP FUNCTION`和删除并重新创建函数`CREATE FUNCTION`
- [ALTER INSTANCE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-instance.com.coder114.cn.html)：MySQL 5.7.11中引入，定义了适用于MySQL服务器实例的操作。
- [ALTER LOGFILE GROUP](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-logfile-group.com.coder114.cn.html)：
- [ALTER PROCEDURE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-procedure.com.coder114.cn.html)：用来改变存储过程的特性，不能使用此语句更改存储过程的参数或主体; 要进行这样的更改，您必须使用`DROP PROCEDURE`和删除并重新创建该过程`CREATE PROCEDURE`。
- [ALTER SERVER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-server.com.coder114.cn.html)：更改服务器信息 *server_name*，调整`CREATE SERVER`语句中允许的任何选项 。
- [ALTER TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-table.com.coder114.cn.html)：`ALTER TABLE`改变一个表的结构。例如，您可以添加或删除列，创建或销毁索引，更改现有列的类型或重命名列或表本身。您还可以更改特征，如用于表格或表格评论的存储引擎。
- [ALTER TABLESPACE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-tablespace.com.coder114.cn.html)：用来添加一个新的数据文件，或者从表空间中删除一个数据文件。
- [ALTER VIEW](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-view.com.coder114.cn.html)：改变了必须存在的视图的定义
- [CREATE DATABASE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-database.com.coder114.cn.html)：`CREATE DATABASE`用给定的名字创建一个数据库
- [CREATE EVENT](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-event.com.coder114.cn.html)：该声明创建并安排新的事件。除非事件计划程序已启用，否则该事件将不会运行
- [CREATE FUNCTION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-function.com.coder114.cn.html)：用于创建存储的函数和用户定义的函数
- [CREATE INDEX](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-index.com.coder114.cn.html)：创建数据库索引， CREATE INDEX不能用来创建一个PRIMARY KEY; 使用 ALTER TABLE来代替
- [CREATE LOGFILE GROUP](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-logfile-group.com.coder114.cn.html)：
- [CREATE PROCEDURE和CREATE FUNCTION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-procedure.com.coder114.cn.html)：创建存储过程或用户定义的函数
- [CREATE SERVER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-server.com.coder114.cn.html)：创建用于`FEDERATED`存储引擎的服务器的定义
- [CREATE TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-table.com.coder114.cn.html)：用给定的名字创建一个表，默认情况下，使用`InnoDB`存储引擎在默认数据库中创建表 
- [CREATE TABLESPACE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-tablespace.com.coder114.cn.html)：创建一个表空间。精确的和语义取决于所使用的存储引擎
- [CREATE TRIGGER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-trigger.com.coder114.cn.html)：这个声明创建一个新的触发器。触发器是一个与表关联的已命名数据库对象，当表发生特定事件时会激活该对象。
- [CREATE VIEW](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-view.com.coder114.cn.html)：创建一个新的视图，或者如果`OR REPLACE`给出该子句
- [DROP DATABASE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-database.com.coder114.cn.html)：删除数据库中的所有表并删除数据库
- [DROP EVENT](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-event.com.coder114.cn.html)：将删除名为 *`event_name`*的事件。该事件立即停止激活，并从服务器上完全删除。
- [DROP FUNCTION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-function.com.coder114.cn.html)：该语句用于删除存储的函数和用户定义的函数
- [DROP INDEX](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-index.com.coder114.cn.html)：删除*`index_name`*表中 指定的索引 *`tbl_name`*
- [DROP LOGFILE GROUP](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-logfile-group.com.coder114.cn.html)：该语句将删除名为的日志文件组 *`logfile_group`*
- [DROP PROCEDURE和DROP FUNCTION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-procedure.com.coder114.cn.html)：删除存储过程或用户定义的函数
- [DROP SERVER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-server.com.coder114.cn.html)：删除名为的服务器的服务器定义 `*`server_name`*`
- [DROP TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-table.com.coder114.cn.html)：删除表，删除表格定义和所有表格数据。对于分区表，它将永久删除表定义，其所有分区以及存储在这些分区中的所有数据。
- [DROP TABLESPACE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-tablespace.com.coder114.cn.html)：删除表空间
- [DROP TRIGGER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-trigger.com.coder114.cn.html)：删除触发器
- [DROP VIEW](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-view.com.coder114.cn.html)：删除试图
- [RENAME TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/rename-table.com.coder114.cn.html)：重命名一个或多个表
- [TRUNCATE TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/truncate-table.com.coder114.cn.html)：完全清空一张表，类似于DELETE，但不能被回滚，不会导致`ON DELETE`触发器触发。

### DML 语句

- [CALL](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/call.com.coder114.cn.html)：调用之前定义的存储过程

- [DELETE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/delete.com.coder114.cn.html)：删除表中的数据

- [DO](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/do.com.coder114.cn.html)：执行表达式但不返回任何结果

- [HANDLER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/handler.com.coder114.cn.html)：提供对表存储引擎接口的直接访问

- [INSERT](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/insert.com.coder114.cn.html)：新行插入到现有表中

- [LOAD DATA INFILE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/load-data.com.coder114.cn.html)：以非常高的速度从文本文件读取数据到表中

- [LOAD XML](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/load-xml.com.coder114.cn.html)：将数据从XML文件读取到表中

- [REPLACE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/replace.com.coder114.cn.html)：REPLACE工作原理与此类似 INSERT，只是如果表中的旧行与a PRIMARY KEY或UNIQUE 索引的新行具有相同的值， 则在插入新行之前删除旧行

- [SELECT](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/select.com.coder114.cn.html)：用于检索从一个或多个表中选择的行，并可以包含 UNION语句和子查询

- [子查询](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/subqueries.com.coder114.cn.html)：子查询是SELECT另一个语句中的一个语句。支持SQL标准所需的所有子查询表单和操作，以及一些特定于MySQL的功能。

- [UPDATE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/update.com.coder114.cn.html)：`UPDATE`是修改表中的行的DML语句。

### 数据库管理语句

#### 账号管理

- [ALTER USER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/alter-user.com.coder114.cn.html)：修改MySQL帐户。它可以为现有帐户修改身份验证，SSL / TLS，资源限制和密码管理属性，并启用帐户锁定和解锁
- [CREATE USER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-user.com.coder114.cn.html)：声明创建新的MySQL帐户。它可以为新帐户建立认证，SSL / TLS，资源限制和密码管理属性，并控制帐户是初始锁定还是解锁
- [DROP USER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-user.com.coder114.cn.html)：删除一个或多个MySQL帐户及其权限。它从所有授权表中删除帐户的权限行
- [GRANT](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/grant.com.coder114.cn.html)：授予MySQL用户帐户的权限
- [RENAME USER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/rename-user.com.coder114.cn.html)：重命名现有的MySQL帐户。旧帐户不存在或新帐户已存在时发生错误
- [REVOKE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/revoke.com.coder114.cn.html)：使系统管理员可以撤消MySQL帐户的权限
- [SET PASSWORD](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/set-password.com.coder114.cn.html)：设MySQL用户帐户密码

#### 表维护

- [ANALYZE TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/analyze-table.com.coder114.cn.html)：执行密钥分发分析并存储指定表的分布

- [CHECK TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/check-table.com.coder114.cn.html)：检查一个或多个表格是否有错误。对于`MyISAM`表格，关键统计信息也会更新

- [CHECKSUM TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/checksum-table.com.coder114.cn.html)：检查表的内容的[校验和](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/glossary.com.coder114.cn.html#glos_checksum)。您可以使用此语句来验证在备份，回滚或旨在将数据恢复到已知状态的其他操作之前和之后内容相同

- [OPTIMIZE TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/optimize-table.com.coder114.cn.html)：重新组织表数据和关联索引数据的物理存储，以减少存储空间，提高访问表时的I / O效率。对每个表进行的确切更改取决于该表使用的 [存储引擎](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/glossary.com.coder114.cn.html#glos_storage_engine)。

- [REPAIR TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/repair-table.com.coder114.cn.html)：修复可能损坏的表格，仅用于某些存储引擎

#### 插件和用户定义的功能

- [CREATE FUNCTION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/create-function-udf.com.coder114.cn.html)：创建用户自定义函数

- [DROP FUNCTION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/drop-function-udf.com.coder114.cn.html)：删除函数

- [安装PLUGIN](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/install-plugin.com.coder114.cn.html)：安装一个服务器插件

- [卸载PLUGIN](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/uninstall-plugin.com.coder114.cn.html)：卸载一个服务器插件

#### SET语句

- [变量赋值的SET](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/set-variable.com.coder114.cn.html)：变量赋值的使您可以将值分配给影响服务器或客户机操作的不同类型的变量

- [SET CHARACTER SET](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/set-character-set.com.coder114.cn.html)：该语句映射服务器和当前客户端之间发送的所有字符串

- [SET NAMES](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/set-names.com.coder114.cn.html)：该语句设置三届系统变量 [`character_set_client`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/server-system-variables.com.coder114.cn.html#sysvar_character_set_client)， [`character_set_connection`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/server-system-variables.com.coder114.cn.html#sysvar_character_set_connection)以及 [`character_set_results`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/server-system-variables.com.coder114.cn.html#sysvar_character_set_results)给定的字符集。设置 [`character_set_connection`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/server-system-variables.com.coder114.cn.html#sysvar_character_set_connection)为 `charset_name`也设置 [`collation_connection`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/server-system-variables.com.coder114.cn.html#sysvar_collation_connection)为默认的排序规则`charset_name`

#### SHOW语句

- [SHOW BINARY LOGS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-binary-logs.com.coder114.cn.html)

- [SHOW BINLOG EVENTS句法](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-binlog-events.com.coder114.cn.html)

- [SHOW CHARACTER SET](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-character-set.com.coder114.cn.html)

- [SHOW COLLATION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-collation.com.coder114.cn.html)

- [SHOW COLUMNS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-columns.com.coder114.cn.html)

- [SHOW CREATE DATABASE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-create-database.com.coder114.cn.html)

- [SHOW CREATE EVENT](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-create-event.com.coder114.cn.html)

- [SHOW CREATE FUNCTION](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-create-function.com.coder114.cn.html)

- [SHOW CREATE PROCEDURE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-create-procedure.com.coder114.cn.html)

- [SHOW CREATE TABLE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-create-table.com.coder114.cn.html)

- [SHOW CREATE TRIGGER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-create-trigger.com.coder114.cn.html)

- [SHOW CREATE USER](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-create-user.com.coder114.cn.html)

- [SHOW CREATE VIEW](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-create-view.com.coder114.cn.html)

- [SHOW DATABASES](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-databases.com.coder114.cn.html)

- [SHOW ENGINE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-engine.com.coder114.cn.html)

- [SHOW ENGINES](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-engines.com.coder114.cn.html)

- [SHOW ERRORS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-errors.com.coder114.cn.html)

- [SHOW EVENTS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-events.com.coder114.cn.html)

- [SHOW FUNCTION CODE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-function-code.com.coder114.cn.html)

- [SHOW FUNCTION STATUS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-function-status.com.coder114.cn.html)

- [SHOW GRANTS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-grants.com.coder114.cn.html)

- [SHOW INDEX](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-index.com.coder114.cn.html)

- [SHOW MASTER STATUS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-master-status.com.coder114.cn.html)

- [SHOW OPEN TABLES](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-open-tables.com.coder114.cn.html)

- [SHOW PLUGINS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-plugins.com.coder114.cn.html)

- [SHOW PRIVILEGES](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-privileges.com.coder114.cn.html)

- [SHOW PROCEDURE CODE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-procedure-code.com.coder114.cn.html)

- [SHOW PROCEDURE STATUS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-procedure-status.com.coder114.cn.html)

- [SHOW PROCESSLIST](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-processlist.com.coder114.cn.html)

- [SHOW PROFILE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-profile.com.coder114.cn.html)

- [SHOW PROFILES](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-profiles.com.coder114.cn.html)

- [SHOW RELAYLOG](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-relaylog-events.com.coder114.cn.html)

- [SHOW SLAVE HOSTS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-slave-hosts.com.coder114.cn.html)

- [SHOW SLAVE STATUS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-slave-status.com.coder114.cn.html)

- [SHOW STATUS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-status.com.coder114.cn.html)

- [SHOW TABLE STATUS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-table-status.com.coder114.cn.html)

- [SHOW TABLES](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-tables.com.coder114.cn.html)

- [SHOW TRIGGERS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-triggers.com.coder114.cn.html)

- [SHOW VARIABLES](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-variables.com.coder114.cn.html)

- [SHOW WARNINGS](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/show-warnings.com.coder114.cn.html)

### 实用语句

- [DESCRIBE](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/describe.com.coder114.cn.html)：该[`DESCRIBE`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/describe.com.coder114.cn.html)和 [`EXPLAIN`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/explain.com.coder114.cn.html)语句是同义词，或者用于获取有关表结构或查询执行计划的信息

- [EXPLAIN](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/explain.com.coder114.cn.html)：该[`DESCRIBE`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/describe.com.coder114.cn.html)和 [`EXPLAIN`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/explain.com.coder114.cn.html)语句是同义词。在实践中，[`DESCRIBE`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/describe.com.coder114.cn.html)关键字通常用于获取关于表结构的信息，而[`EXPLAIN`](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/explain.com.coder114.cn.html)用于获取查询执行计划（也就是说MySQL将如何执行查询）

- [帮助](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/help.com.coder114.cn.html)：句返回MySQL参考手册中的在线信息。其正确的操作要求`mysql` 使用帮助主题信息初始化数据库中的帮助表

- [USE语句](http://www.searchdoc.cn/rdbms/mysql/dev.mysql.com/doc/refman/5.7/en/use.com.coder114.cn.html)：该 语句告诉MySQL将 数据库用作后续语句的默认（当前）数据库。直到会话结束或另一个语句发布时，数据库仍然是默认值。

## 参阅

[MySQL Chapter 13 SQL Statements](https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html)