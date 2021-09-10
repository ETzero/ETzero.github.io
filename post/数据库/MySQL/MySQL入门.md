# MySQL 入门

## 一、MySQL数据类型

### 数值类型

| 数据类型  | 字节数 | 带符号最小值         | 带符号最大值        | 不带符号最小值 | 不带符号最大值       |
| --------- | ------ | -------------------- | ------------------- | -------------- | -------------------- |
| TINYINT   | 1      | -128                 | 127                 | 0              | 255                  |
| SMALLINT  | 2      | -32768               | 32767               | 0              | 65535                |
| MEDIUMINT | 3      | -8388608             | 8388607             | 0              | 16777215             |
| INT       | 4      | -2147483648          | 2147483647          | 0              | 4294967295           |
| BIGINT    | 8      | -9223372036854775808 | 9223372036854775807 | 0              | 18446744073709551616 |

**MySQL中整型默认是带符号的**。

#### 关于 INT(N)

int(N)我们只需要记住两点：

- 无论N等于多少，int永远占4个字节
- **N表示的是显示宽度，不足的用0补足，超过的无视长度而直接显示整个数字，但这要整型设置了unsigned zerofill 才有效**

### **浮点型**

| 类型   | 大小    | 范围（有符号）                                               | 范围（无符号）                                               | 用途            |
| :----- | :------ | :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------- |
| FLOAT  | 4 bytes | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE | 8 bytes | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |

总结一下float(M,D)、double(M、D)的用法规则：

- D表示浮点型数据小数点之后的精度，假如超过D位则四舍五入，即1.233四舍五入为1.23，1.237四舍五入为1.24
- M表示浮点型数据总共的位数，D=2则表示总共支持五位，即小数点前只支持三位数，所以我们并没有看到1000.23、10000.233、100000.233这三条数据的插入，因为插入都报错了

### **decimal 型**

| 类型    | 大小                                     | 范围（有符号） | 范围（无符号） | 用途   |
| :------ | :--------------------------------------- | :------------- | :------------- | :----- |
| DECIMAL | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值 | 依赖于M和D的值 | 小数值 |

`decimal`和`float/double`的区别，个人总结主要体现在两点上：

- `float/double`在db中存储的是近似值，而`decimal`则是以字符串形式进行保存的
- `decimal(M,D)`的规则和float/double相同，但区别在`float/double`在不指定M、D时默认按照实际精度来处理而`decimal`在不指定M、D时默认为`decimal(10, 0)`

### **日期类型**

| 数据类型  | 字节数 | 格式                | 备注                      |
| --------- | ------ | ------------------- | ------------------------- |
| date      | 3      | yyyy-MM-dd          | 存储日期值                |
| time      | 3      | HH:mm:ss            | 存储时分秒                |
| year      | 1      | yyyy                | 存储年                    |
| datetime  | 8      | yyyy-MM-dd HH:mm:ss | 存储日期+时间             |
| timestamp | 4      | yyyy-MM-dd HH:mm:ss | 存储日期+时间，可作时间戳 |

datetime与timestamp两种类型的区别：

- 上面列了，`datetime`占8个字节，`timestamp`占4个字节
- 由于大小的区别，`datetime`与`timestamp`能存储的时间范围也不同，datetime的存储范围为`1000-01-01 00:00:00——9999-12-31 23:59:59`，`timestamp`存储的时间范围为`19700101080001——20380119111407`
- `datetime`默认值为空，当插入的值为`null`时，该列的值就是`null`；`timestamp`默认值不为空，当插入的值为`null`的时候，mysql会取当前时间
- `datetime`存储的时间与时区无关，`timestamp`存储的时间及显示的时间都依赖于当前时区

### 字符串类型

| 类型       | 大小                  | 用途                            |
| :--------- | :-------------------- | :------------------------------ |
| CHAR       | 0-255 bytes           | 定长字符串                      |
| VARCHAR    | 0-65535 bytes         | 变长字符串                      |
| TINYBLOB   | 0-255 bytes           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255 bytes           | 短文本字符串                    |
| BLOB       | 0-65 535 bytes        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535 bytes        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215 bytes    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215 bytes    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295 bytes | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295 bytes | 极大文本数据                    |

关于`char`和`varchar的`对比，我总结一下：

1. `char`是固定长度字符串，其长度范围为0-255且与编码方式无关，无论字符实际长度是多少，都会按照指定长度存储，不够的用空格补足；`varchar`为可变长度字符串，在`utf8`编码的数据库中其长度范围为0-21844
2. `char`实际占用的字节数即存储的字符所占用的字节数，`varchar`实际占用的字节数为存储的字符+1或+2或+3
3. MySQL处理`char`类型数据时会将结尾的所有空格处理掉而`varchar`类型数据则不会

> **varchar型数据占用空间大小及可容纳最大字符串限制**
>
> 在utf8编码下我们可以知道varchar(M)，M最大=21844；gbk的编码格式下，varchar(M)最大的M=32765。为什么会有这样的区别呢？因为：
>
> - MySQL要求一个行的定义长度不能超过65535即64K
> - 对于未指定varchar字段not null的表，会有1个字节专门表示该字段是否为null
> - varchar(M)，当M范围为0<=M<=255时会专门有一个字节记录varchar型字符串长度，当M>255时会专门有两个字节记录varchar型字符串的长度，把这一点和上一点结合，那么65535个字节实际可用的为65535-3=65532个字节
> - 所有英文无论其编码方式，都占用1个字节，但对于gbk编码，一个汉字占两个字节，因此最大M=65532/2=32766；对于utf8编码，一个汉字占3个字节，因此最大M=65532/3=21844，上面的结论都成立
> - 举一反三，对于utfmb4编码方式，1个字符最大可能占4个字节，那么varchar(M)，M最大为65532/4=16383，可以自己验证一下
>
> 同样的，上面是表中只有varchar型数据的情况，**如果表中同时存在int、double、char这些数据，需要把这些数据所占据的空间减去，才能计算varchar(M)型数据M最大等于多少**。

`text`和`varchar`是一组既有区别又有联系的数据类型，其联系在于**当varchar(M)的M大于某些数值时，varchar会自动转为text**：

- M>255时转为`tinytext`
- M>500时转为`text`
- M>20000时转为`mediumtext`

所以过大的内容`varchar`和`text`没有区别，同时`varchar(M)`和`text`的区别在于：

- 单行64K即65535字节的空间，`varchar`只能用63352/65533个字节，但是text可以65535个字节全部用起来
- `text`可以指定text(M)，但是M无论等于多少都没有影响
- `text`不允许有默认值，varchar允许有默认值

`varchar`和`text`两种数据类型，使用建议是**能用varchar就用varchar而不用text（存储效率高）**，`varchar(M)`的M有长度限制，之前说过，如果大于限制，可以使用`mediumtext（16M`）或者`longtext（4G）`。

至于`text`和`blob`，简单过一下就是**text存储的是字符串而blob存储的是二进制字符串**，简单说`blob`是用于存储例如图片、音视频这种文件的二进制数据的。

## 二、数据库基本操作

```sql
# 创建库
create database db_name;

# 显示数据库
show databases;

# 删除库
drop database db_name;

# 显示数据库支持的引擎
show engines;
show variables like 'have%';
```

### 存储引擎

#### InnoDB

- 提供事务、回滚、崩溃修复能力和并发控制的存储引擎。
- 提供外键约束的表引擎，支持外键。
- 支持自增长`AUTO_INCREMENT`，自增列必须主键。
- 创建的表结构存储在 `.frm` 文件中，数据存储在 `innodb_data_home_dir` 中，索引存储在 `innodb_data_file_path` 中
- 读写效率较低，占用空间较大

#### MyISAM

- MyISAM 存储引擎的表存储在三个文件中，文件名与表名同名，后缀分别为：`.frm`, `.MYD`, `.MYI`。
- MyISAM 的表支持三种方式的存储格式：静态型、动态型、压缩型。默认静态型（字段长度固定）。压缩型需要使用`myisampack` 工具压缩
- MyISAM 优势在于占用空间小，处理速度快；缺点是不支持事务的完整性和并发性

#### MEMORY

- 存储的所有表都在内存中，表结构存储在磁盘中，而表的数据内容存储在内存中
- 默认使用`HASH`索引而不是`B-tree`索引
- 表的大小是有限制的，取决于 `max_rows` 和 `max_heap_table_size`。 `max_rows` 在创建时可以指定， `max_heap_table_size` 默认为 16MB，可以扩大

## 三、表的基本操作

### 创建表

```sql
# 一般创建
create table 表名0(
	id INT,
    name VARCHAR(20),
    sex BOOLEAN
);

# 单字段主键
create table 表名1(
	id INT PRIMARY KEY,
    name VARCHAR(20),
    sex BOOLEAN
);

# 多字段主键
create table 表名2(
	stu_id INT,
    course_id INT,
    grade FLOAT,
    PRIMARY KEY(stu_id, course_id)
);

# 外键
create table 表名3(
	id INT PRIMARY KEY,
    stu_id INT,
    course_id INT,
    CONSTRAINT c_fk FOREIGN KEY(stu_id, course_id)
    	REFERENCES 表名2 (stu_id, course_id)
);

# 非空约束 & 唯一性约束
create table 表名4(
    id INT NOT NULL PRIMARY KEY
	stu_id INT UNIQUE,
    name VARCHAR(20) NOT NULL,
    course_id INT,
    grade FLOAT,
    PRIMARY KEY(stu_id, course_id)
);

# 自动自增列
create table 表名5(
    id INT PRIMARY KEY AUTO_INCREMENT,
	stu_id INT UNIQUE,
    name VARCHAR(20) NOT NULL,
);

#查看表结构
describe 表名;
```

### 修改表

```sql
# 重命名表
alter table old_name rename new_name;

# 修改字段的数据类型
alter table 表名 modify column_name VARCHAR(20);

# 修改字段名
alter table 表名 change old_column_name new_column_name column_type;

# 新增字段
alter table 表名 add new_column_name column_type;
alter table example_table add phone VARCHAR(20);
alter table example_table add age VARCHAR(20) NOT NULL;
alter table example_table add  num INT(8) PRIMARY KEY FIRST;	# 加到第一列的位置
alter table example_table add  address VARCHAR(30) NOT NULL AFTER phone;	# 加到指定列的后面

# 删除字段
alter table 表名 drop column_name;

# 修改字段的排列位置
alter table 表名 modify column_name column_type FIRST|AFTER other_column_name;
alter table example_table modify name VARCHAR(30) FIRST;
alter table example_table modify sex TINYINT(1) AFTER age;

# 更改存储引擎
alter table 表名 engine=InnoDB;
alter table 表名 engine=MyISAM;

# 删除表的外键约束
alter table 表名 drop foreign key 外键名;
```

### 删除表

```sql
# 删除表
drop table 表名;

#删除被其他表关联的父表
alter table sub_table drop foreign key 外键名;	 # 解除与被删除表之间的外键约束
drop table par_table;	# 再删除表
```

## 四、索引

索引是创建在表上的，是对数据库表的一列或多列的值进行排序的一种结构。作用是提高对表中数据的查询速度。

不同的存储引擎定义每个表的最大索引数和最大索引长度。所有存储引擎对每个表至少支持16个索引，总索引长度至少256字节。

索引有两种存储类型：

- B-tree 索引：MEMORT、InnoDB 和 MyISAM 都支持
- HASH 索引：只有MEMORY 支持

索引优缺点：

- 优点：提高检索速度
- 缺点：创建和维护索引会增加耗时；索引占用物理空间；插入、修改、删除表时，需要动态维护索引，造成数据维护速度降低。

索引的分类：

- 普通索引：可以创建在任何数据类型中，其值是否唯一和非空有字段本身的完整性约束条件决定
- 唯一性索引：使用 `UNIQUE` 参数可以设置索引为唯一性索引。创建唯一性索引时，限制该索引的值必须是唯一的。
- 全文索引：使用 `FULLTEXT` 参数可以设置索引为全文索引。全文索引只能创建在 CHAR，VARCHAR 和 TEXT 类型的字段上。当查询数据量较大的字符串的类型时，使用全文索引可以提高查询速度。
- 单列索引：在表中的单个字段上创建索引，单列索引只根据该字段进行索引。
- 多列索引：在表的多个字段上创建一个索引。多个字段中，只有当查询条件使用了第一个字段时，索引才会被使用
- 空间索引：使用 `SPATIAL` 参数可以设置索引为空间索引。空间索引只能建立在空间数据类型上，这样就可以提高系统获取空间数据的效率。

> MySQL 的空间类型包括 GEOMETRY、POINT、LINESTRING、POLYGON 等。MyISAM 存储引擎支持空间检索，且索引的字段不能为空值。

索引的设计原则：

- 选择唯一性索引
- 为经常需要排序、分组和联合操作的字段建立索引
- 为经常作为查询条件的字段建立索引
- 限制索引的数目
- 尽量使用数据量少的索引
- 尽量使用前缀来索引（如果索引字段的值很长，最好使用值的前缀来索引）
- 删除不再使用或者很少使用的索引

### 创建索引

```sql
# 创建表时创建
# 普通索引
create table 表名(
	id INT,
    name VARCHAR(20),
    sex BOOLEAN,
    INDEX(id)
);

# 创建唯一性索引
create table 表名(
	id INT UNIQUE,
    name VARCHAR(20),
    UNIQUE INDEX index2_id(id ASC)
);

# 创建全文索引
create table 表名(
	id INT,
    name VARCHAR(20),
    info VARCHAR(20),
    FULLTEXT INDEX index3_info(info)
) engine=MyISAM;

# 创建单列索引
create table 表名(
	id INT,
    subject VARCHAR(30),
    INDEX index4_sj( subject(10) )
);

# 创建多列索引
create table 表名(
	id INT,
    name VARCHAR(20),
    sex CHAR(4),
    INDEX index5_ns(name, sex)
);

# 创建空间索引
create table 表名(
	id INT,
    space GEOMETRY NOT NULL,
    SPATIAL INDEX index6_sp(space)
)engine=MyISAM;

###########################################
# 已存在表上创建
# 普通索引
create index index7_id on 表名(id);

# 创建唯一性索引
create unique index index8_id on 表名(course_id);

# 创建全文索引
create fulltext index index9_info on 表名(info);

# 创建单列索引
create index index10_addr on 表名(address(4));

# 创建多列索引
create index index11_na on 表名( name, address );

# 创建空间索引
create SPATIAL index index12_line on 表名(line);

###########################################
# alter table 创建索引
# 普通索引
alter table example0 add index index13_name (name(20));

# 创建唯一性索引
alter table example1 add unique index index14_id (curse_id);

# 创建全文索引
alter table example3 add fulltext index index15_info (info);

# 创建单列索引
alter table example4 add index index16_addr (address(4));

# 创建多列索引
alter table example5 add index index17_ns (name, address);

# 创建空间索引
alter table example5 add SPATIAL index index17_li(line);
```

### 删除索引

```sql
drop index index_name on TableName;
```

## 五、视图

视图是一种虚拟的表，是从数据库中一个或多个表中导出来的表。还可以从已经定义的视图基础上定义。数据库中只存放了视图的定义，而没有存放视图中的数据。

视图的作用：

- 使操作简单化：目的就是所见即所得
- 增加数据的安全性：通过视图，用户只能查询和修改指定的数据，未指定的其他数据接触不到
- 提高表的逻辑独立性：视图可以屏蔽原有表结构变化带来的影响

### 创建视图

```sql
# 语法
CREATE [ALGORITHM = {UNDEFINED|MERGE|TEMPTABLE}] 
VIEW  视图名 [字段名] AS SELECT 语句 
[WITH [cascaded|local] CHECK OPTION]
```

凡是有中括号的，都是可选参数。语法说明：

- `ALGORITHM` ： 可选参数表示视图选择的算法，有以下几个：
  - UNDEFINED : 表示MySQL 将自动选择所要使用的算法；
  - MERGE : 表示将使用视图 的语句与视图定义合并起来，使得视图定义的某一部分取代语句的对应部分。
  - TEMPTABLE : 表示将视图的结果存入临时表中，然后使用临时表执行语句
- `cascaded` ： 可选参数，表示更新视图时要满足所以相关视图和表的条件，该值为默认值
- `local`: 可选参数， 表示更新视图时，要满足该视图本身的定义的条件即可
- `WITH CHECK OPTION` : 可选参数，表示更新视图时要保证在该视图的权限范围之内。

> 创建视图时，建议使用 `WITH cascaded CHECK OPTION`，保证数据的安全性。

例子：

```sql
# 单表创建
create view department_view1 as select * from department;
create view department_view2 (name, function, location) as select d_name, function, address from department;

# 多表创建
create ALGORITHM=MERGE view worker_view1 (name, department, sex, address )
as select name, department.d_name, sex, birthday, address from worker, department
where worker.d_id = department.d_id
with local check option;
```

### 查看视图

```sql
# 查看视图基本信息
describe '视图名';
show table status like '视图名';

# 查看视图详细信息
show create view 视图名;

# 在视图表中查看详细信息
select * from information_schema.views;
```

### 修改视图

```sql
# replace 方式修改
CREATE OR REPLACE [ALGORITHM = {UNDEFINED|MERGE|TEMPTABLE}] 
VIEW  视图名 [字段名] AS SELECT 语句 
[WITH [cascaded|local] CHECK OPTION]

# alter 方式修改
alter [ALGORITHM = {UNDEFINED|MERGE|TEMPTABLE}] 
VIEW  视图名 [字段名] AS SELECT 语句 
[WITH [cascaded|local] CHECK OPTION]

# example
alter view department_view2 (department, name, sex, location)
as select d_name, worker.name, worker.sex, address
from woker, department where department.d_id = worker,d_id
with check option;
```

### 更新视图

更新视图，指的是通过视图来插入(insert)、更新(update)和删除(delete)表中的数据。有以下的情况是不能更新视图：

- 视图中包含`SUM()`，`COUNT()`，`MAX()`，`MIN()` 等函数
- 视图中包含 `union`, `union all`, `distinct`, `group by`, `having` 等关键字
- 常量视图：`create view view_name as select 'Lee' as name from dual` 这样的视图称为常量视图
- 视图中的 `SELECT` 中包含子查询
- 由不可更新的视图导出的视图
- 创建视图时，ALGORITHM 为 TEMLTABLE 类型的使用
- 视图对于的表上存在没有默认值的列，且该列没有包含在视图中

### 删除视图

```sql
drop view [if exists] 视图名列表(逗号分隔) [RESTRICT |CASCADE]
```

## 六、触发器

触发器是由`INSERT`、`UPDATE`和`DELETE` 等事件来触发某种特点操作。当满足触发器条件时，数据库系统会执行触发器定义的程序语句，以保证某些操作之间的一致性。

### 创建触发器

```sql
# 创建单个执行语句的触发器
create  trigger 触发器名 before|after 触发条件
on 表名 for each row 执行语句

# example 
create trigger dept_trig1 before insert
on department for each row insert into trigger_time values(now());

# 创建多个执行语句的触发器
create trigger 触发器名 before|after 触发条件
on 表名 for each row
begin
	执行语句列表
end

# example
delimiter &&
create trigger dept_trig2 after delete
on department for each row
begin
	insert into trigger_time values('21:01:01');
	insert into trigger_time values('22:01:01');
end
&&
delimiter ;
```

> 一般情况下，MySQL 默认是以分号 `;` 作为结束执行语句。在创建触发器过程中需要用到分号 `;` （多个执行语句要以分号分隔）。为了解决这个问题，可以使用 `delimiter &&` 语句定义结束符号为 `&&`，当触发器创建完成后，再用 `delimiter ;` 将结束符号定义回默认的分号。

### 查看触发器

```sql
show triggers;
select * from information_schema.triggers where trigger_name = '触发器名';
```

在激活触发器时，对触发器中的执行语句存在一些限制，如触发器中不能包含 START TRANSACTION、COMMIT 或 ROLLBACK 等关键字，也不能包含 CALL 语句。

### 删除触发器

```sql
drop trigger 触发器名;
```

## 七、查询数据

### 普通查询

```sql
select * from employee;
select name, sex, age from employee where d_id  = 10;
select name, sex, age from employee where d_id in (1,2,10);
select * from employee where age between 15 and 25;			# 15 <= age <= 25
select * from employee where age not between 15 and 25;
select * from employee where name like 'aric';
select * from employee where name like 'ar%';
select * from employee where name like '张__';			# 一个下划线 `_` 表示一个字符
select * from worker where info is null;
select * from worker where info is not null;
select * from employee where d_id = 10 and sex = 'man';
select * from employee where d_id = 10 or sex like 'man';
select distinct d_id from employee order by d_id desc;
select * from employee order by age asc;
select * from employee order by d_id asc, age desc;		# 先按 d_id 升序，再按 age 降序

# group by
select * from employee group by sex;
select sex, group_concat(name) from employee group by sex;		# 把 name 合并显示， 逗号分隔
select sex, count(sex) from employee group by sex;
select sex, count(sex) from employee group by sex having count(sex) > 3;
select sex, count(sex) from employee group by sex with rollup;		# 在所有记录的最后加上一条记录，显示所有记录的总和

# limit
select * from employee limit 2;
select * from employee limit 0,2;		# 初始位置, 记录数
```

### 集合函数

```sql
select count(0) from employee;						# 统计记录条数
select sum(score) from grade where num=100;			 # 求和
select avg(age) from employee;			 			# 求平均
select max(age) from employee;			 			# 求最大
select min(age) from employee;			 			# 求最小
```

### 连接查询

```sql
# 内连接查询 （ 交集 ）
select num, name, employee.d_id, sex, age, d_name, function
from employee, department
where employee.d_id = department.d_id;

# 外连接查询 
# 左连接
select num, name, employee.d_id, sex, age, d_name, function
from employee left join department
on employee.d_id = department.d_id;

# 右连接
select num, name, employee.d_id, sex, age, d_name, function
from employee right join department
on employee.d_id = department.d_id;

# 子查询
# IN 的子查询
select * from employee where d_id in (select d_id from department);
select * from employee where d_id not in (select d_id from department);

# 比较运算符的子查询
select name, score from computer_stu
where score >= (select score from scholarship where slevel=1);
select d_id, d_name from department 
where d_id <> (select d_id from employee where age = 24);

# EXISTS 的子查询
# 使用 EXISTS 关键字，内层查询语句不返回查询结果，而是返回一个真假值
select * from employee where exists (select d_name from department where d_id=1003);		# 内层查询到结果时返回true,外层执行
select * from employee where not exists (select d_name from department where d_id=1003);	# 内层查询到结果时返回true,外层不执行

# ANY 的子查询
# ANY 表示满足其中的任一条件
select * from computer_stu where score>=ANY(select score from scholarship);

# ALL 的子查询
# ANY 表示满足所有的条件
select * from computer_stu where  score>=ALL(select score from scholarship);

# 合并查询
select d_id from department union select d_id from employee;
select d_id from department union all select d_id from employee;		# union 会消除合并后相同的记录， union all 不会
```

### 使用正则表达式查询

| 模式字符串     | 含义                                       |
| -------------- | ------------------------------------------ |
| ^              | 匹配字符串开始的部分                       |
| $              | 匹配字符串结束的部分                       |
| .              | 代表字符串中的任意一个字符，包括回车和换行 |
| [字符集合]     | 匹配“字符集合”中的任何一个字符             |
| [^字符集合]    | 匹配除了“字符集合”以外的的任何一个字符     |
| S1 \| S2 \| S3 | 匹配 S1、S2和S3中的任意一个字符串          |
| *              | 代表0个或多个该符号之前的字符              |
| +              | 代表1个或多个该符号之前的字符              |
| 字符串{N}      | 字符串出现N次                              |
| 字符串{M,N}    | 字符串出现至少M次，至多N次                 |

```sql
select * from info where name regexp '^L';			# 名字以 L 开头的数据
select * from info where name regexp 'c$';			# 名字以 c 结尾的数据
select * from info where name regexp '^L..y&';		# 名字以 L 开头, y 结尾, 中间有两个字符的数据
select * from info where name regexp '[ceo]';		# 名字包含有 c、e、o 任意一个的数据
select * from info where name regexp '[0-9]';		# 名字包含有 0-9任意一个数字的数据
select * from info where name regexp '[a-z]';		# 名字包含有 a-z任意一个字母的数据
select * from info where name regexp '[^a-w0-9]';	# 名字包含 a-w 字母和数字以外的数据
select * from info where name regexp 'ic|uc|ab';	# 名字包含有 ic、uc、ab 中的任意一个的数据
select * from info where name regexp 'a+c';			# 名字包含有 c字母，且 c之前出现过 a 的数据
select * from info where name regexp 'a{3}';		# 名字包含连续出现3次字母 a 的数据
```

## 八、插入、更新、删除数据

### 插入

```sql
insert into 表名 values (value_1, value_2, value_3, value_4, value_5);
insert into 表名(column_1, column_2, column_3) values (value_1, value_2, value_3);

# 多条数据
insert into 表名 values
(value_1, value_2, value_3, value_4, value_5),
(value_1, value_2, value_3, value_4, value_5),
(value_1, value_2, value_3, value_4, value_5);

# 查询结果插入
insert into 表名 (value_1, value_2, value_3, value_4, value_5)
	select column_1, column_2, column_3, column_4, column_5 from 另一个表名 where 条件;
```

### 更新

```sql
update 表名
	set coulmn_1 = value_1, coulmn_2 = value_2, coulmn_3 = value_3
 where 条件;
```

### 删除

```sql
delete from 表名 where 条件;
```

## 九、MySQL 运算符

### 算术运算符

| 符号 | 表达式形式 | 作用   |
| ---- | ---------- | ------ |
| +    | `x+y+z`    | 加法   |
| -    | `x-y-z`    | 减法   |
| *    | `x*y*z`    | 乘法   |
| /    | `x/y/z`    | 除法   |
| DIV  | `x DIV y`  | 同除法 |
| %    | `x % y`    | 求余   |
| MOD  | `x  MOD y` | 求余   |

### 比较运算符

默认情况下，字符串比较不区分大小写，并使用当前字符集。默认值为 utf8mb4。

| 符号                          | 作用                                                       |
| ----------------------------- | ---------------------------------------------------------- |
| >                             | 大于运算符                                                 |
| >=                            | 大于等于运算符                                             |
| <                             | 小于运算符                                                 |
| <>, !=                        | 不等运算符                                                 |
| <=                            | 小于等于运算符                                             |
| <=>                           | NULL 安全等于运算符                                        |
| =                             | 等于运算符                                                 |
| BETWEEN ... AND ...           | 一个值是否在某些范围内                                     |
| COALESCE(*value*,...)         | 返回第一个非 NULL 参数                                     |
| GREATEST(*value1,value2*,...) | 返回最大参数                                               |
| IN()                          | 一个值是否在一组值内                                       |
| INTERVAL(*N,N1,N2,N3*,...)    | 返回小于第一个参数的参数索引                               |
| IS                            | 基于布尔值进行测试                                         |
| IS NOT                        | 基于布尔值进行测试                                         |
| IS NOT NULL                   | NOT NULL 值测试                                            |
| IS NULL                       | NULL 值测试                                                |
| ISNULL(expr)                  | 测试参数是否为 NULL,  *expr* 为 NULL则返回1，不为NULL返回0 |
| LEAST(*value1,value2,*...)    | 返回最小参数。                                             |
| LIKE                          | 简单模式匹配                                               |
| NOT BETWEEN ... AND ...       | 一个值是否不在某个范围内                                   |
| NOT IN()                      | 一个值是否不在一组值内                                     |
| NOT LIKE                      | 简单模式匹配的否定                                         |
| STRCMP()                      | 比较两个字符串                                             |

`LEAST` 的比较规则：

- 如果任何参数为 NULL，则结果为 NULL。不需要比较
- 如果所有参数都是整数值，则将它们作为整数进行比较
- 如果至少有一个参数是双精度值，则将它们作为双精度值进行比较。否则，如果至少有一个参数是 DECIMAL 值，则将它们作为 DECIMAL 值进行比较
- 如果参数由数字和字符串组成，则将它们作为字符串进行比较
- 如果任何参数是非二进制（字符）字符串，则这些参数将作为非二进制字符串进行比较
- 在所有其他情况下，参数作为二进制字符串进行比较

### 逻辑运算符

| 符号     | 含义 |
| -------- | ---- |
| &&, AND  | 与   |
| \|\|, OR | 或   |
| !, NOT   | 非   |
| XOR      | 异或 |

### 位运算符

| 符号 | 含义     |
| ---- | -------- |
| &    | 按位与   |
| ^    | 按位异或 |
| \|   | 按位或   |
| <<   | 按位左移 |
| >>   | 按位右移 |
| ~    | 按位取反 |

### 运算符优先级

相同优先级的，表达式从左往右运算 。

| 优先级由低到高排列 | 运算符                                                       |
| ------------------ | ------------------------------------------------------------ |
| 1                  | =(赋值运算）、:=                                             |
| 2                  | II、OR                                                       |
| 3                  | XOR                                                          |
| 4                  | &&、AND                                                      |
| 5                  | NOT                                                          |
| 6                  | BETWEEN、CASE、WHEN、THEN、ELSE                              |
| 7                  | =(比较运算）、<=>、>=、>、<=、<、<>、!=、 IS、LIKE、REGEXP、IN |
| 8                  | \|                                                           |
| 9                  | &                                                            |
| 10                 | <<、>>                                                       |
| 11                 | -(减号）、+                                                  |
| 12                 | *、/、%                                                      |
| 13                 | ^                                                            |
| 14                 | -(负号）、〜（位反转）                                       |
| 15                 | !                                                            |

## 十、MySQL 函数

### 数学函数

| 函数 | 作用 |
| ---- | ---- |
| ABS(x)		| 返回给定值的绝对值 |
| ACOS(x)	| 返回数字的反余弦值 |
| ASIN(x)	| 返回数字的反正弦值 |
| ATAN(x)	| 返回一个或多个值的反正切值 |
| ATAN2(x,y)	| 返回两个参数的反正切 |
| CEIL(x)	| 同义词是CEILING() |
| CEILING(x)	| 将一个数字四舍五入到最近的整数(返回不小于其参数的最小整数) |
| CONV()		| 转换不同数字基数之间的数字 |
| COS()			| 返回数字的余弦值 |
| COT(x)		| 返回数字的余切 |
| CRC32()		| 计算循环冗余校验值 |
| DEGREES()		| 从弧度转换为度数 |
| EXP()			| 返回e到x的幂 |
| FLOOR()		| 将数字向下舍入到最接近的整数（返回不大于参数的最大整数值） |
| LN()			| 返回数字的自然对数 |
| LOG()			| 返回数字的自然对数。还允许您指定基数 |
| LOG10()		| 返回参数的以10为底的对数 |
| LOG2()		| 返回参数的以2为底的对数 |
| MOD()			| 执行模运算。返回N除以M的余数 |
| PI()			| 返回π（pi）的值 |
| POW(x,y)	| 将引发的参数返回到指定的幂 |
| POWER(x,y)	| 同义词POW() |
| RADIANS()		| 将值从度转换为弧度，并返回结果 |
| RAND()		| 返回随机浮点值 |
| ROUND()		| 将数字向上或向下舍入到给定的小数位数 |
| SIGN()		| 返回参数的符号（这样你就可以知道数字是正数还是负数） |
| SIN()			| 返回参数的正弦值 |
| SQRT()		| 返回参数的平方根 |
| TAN()			| 返回参数的正切值 |
| TRUNCATE()	| 将值截断为指定的小数位数 |

### 字符串函数

| 函数 | 作用 |
| ---- | ---- |
| CHAR_LENGTH(S)						| 返回字符串 s 的字符数 |
| LENGTH(S)							    | 返回字符串 s 的长度 |
| CONCAT(s1,s2,....)					| 将字符串s1,s2等多个字符串合并为一个字符串 |
| CONCAT_WS(s1,s2,...)					| 同CONCAT 函数，但是每个字符中直接要加上 x |
| INSERT(s1,x,len,s2)					| 将字将串 s2 替换 s1 的 x 位置开始长度为len的字符串 |
| UPPER(s), UCASE(s)                    | 将字符串 s 的所有字母都变成大写字母 |
| LOWER(s), LCASE(s)                    | 将字符串 s 的所有字母都变成小写字母 |
| LEFT(s,n)                             | 返回字符串 s 的前n个字符 |
| RIGHT(s,n)                            | 返回字符串 s 的后n个字符 |
| LPAD(s1, len, s2)                     | 字符串 s2 来填充s1的开始处，使字符串长度达到len |
| RPAD(s1, len, s2)                     | 字符串 s2 来填充s1的结尾处，使字符串长度达到len |
| LTRIM(s)                              | 去掉字符串s开始处的空格 |
| RTRIM(s)                              | 去掉字符串S结尾处的空格 |
| TRIM(s)                               | 去掉字符串s开始处和结尾处的空格 |
| TRIM(s1 FROM s)                       | 去掉字符中s中开始处和结尾处的字符申s1 |
| REPEAT(s,n)                           | 将字符串s重复n次 |
| SPACE(n)                              | 返回n个空格 |
| REPLACE(s,s1,s2)                      | 用字符串s2替代字符串s中的字符串s1 |
| STRCMP(s1,s2)                         | 比较字符串s1和s2 |
| SUBSTRING(s,n,len)                    | 获取从字符串s中的第n个位置开始长度为len的字符串 |
| MID(s,n,len)                          | 同 SUBSTRING(s,n,len) |
| LOCATE(s1,s), POSITION(s1 IN s)       | 从字符串 s 中获取s1的开始位置 |
| INSTR(s,s1)                           | 从字符串 s 中获取s1的开始位置 |
| REVERSE(s)                            | 将字符串 s 的顺序反过来 |
| ELT(n, s1, s2, ...)                   | 返回第n个字符串 |
| EXPORT_SET(x,s1,s2)                   |  |
| FIELD(s, s1, s2, ...)                 | 返回第一个与字符串 s 匹配的字符串的位置 |
| FIND_IN_SET(s1,s2)					| 回在字符串 s2 中与 s1 匹配的字符串的位置 |
| MAKE_SET(x, s1, s2,...)				| 按x的二进制从s1, s2, s3,...sn 中选取字符串 |

### 日期和时间函数

| 函数 | 作用 |
| ---- | ---- |
| CURDATE(),CURRENT_DATE()			| 返回当前日期 |
| CURTIMEO,CURRENT_TIME()			| 返回当前时间 |
| NOW(), CURRENT_TIMESTAMP(), LOCALTIME(), SYSDATE(), LOCALTIMESTAMP()	| 返回当前日期和时间 |
| UNIX TIMESTAMP()					| 以 UNIX 时间戳的形式返回当前时间 |
| UNIX_TIMESTAMP(d)					| 将时间 d 以UNIX 时间戳的形式返回 |
| FROM_UNIXTIME(d)					| 把 UNIX 时间戳的时间转换为普通格式的时间 |
| UTC_DATE()						| 返回UTC（Universal Coordinated Time，国际协调时间）日期 |
| UTC_TIME()						| 返回 UTC 时间 |
| MONTH(d)							| 返回日期d中的月份值,范围是1~12 |
| MONTHNAME(d)						| 返回日期 d 中的月份名称，如 January,February |
| DAYNAME(d)						| 返回日期 d 是星期几，如 Monday,Tuesday 等 |
| DAYOFWEEK(d)						| 返回日期d是星期几，1表示星期日，2表示星期一等 |
| WEEKDAY(d)						| 返回日期d是星期几,0表示星期一,，1表示星期二等 |
| WEEK(d)							| 计算日期d是本年的第几个星期，范围是0~53 |
| WEEKOFYEAR(d)						| 计算日期d是本年的第几个星期，范围是1~53 |
| DAYOFYEAR(d)						| 计算日期d是本年的第几天 |
| DAYOFMONTH(d)						| 计算日期d是本月的第几天 |
| YEAR(d)							| 返回日期d中的年份值 |
| QUARTER(d)						| 返回日期d是第几季度,范围是1~4 |
| HOUR(t)							| 返回时间 t 中的小时值 |
| MINUTE(t)							| 返回时间 t 中的分钟值 |
| SECOND(t)							| 返回时间 t 中的秒钟值 |
| EXTRACT(type FROM d)				| 从日期d中获取指定的值，type 指定返回的值，如 YEAR,HOUR 等 |
| TIME_TO_SEC(t)					| 将时间 t转换为秒 |
| SEC_TO_TIME(s)					| 将以秒为单位的时间 s 转换为时分秒的格式 |
| TO DAYS(d)						| 计算日期 d~0000年Ⅰ月1日的天数 |
| FROM_DAYS(n)						| 计算从 0000年1月1日开始 n 天后的日期 |
| DATEDIFF(d1,d2)					| 计算日期 dl~d2 之间相隔的天数 |
| ADDDATE(d,n)						| 计算起始日期d加上n天的日期 |
| ADDDATE(d,INTERVAL expr type)		| 计算起始日期 d 加上一个时间段后的日期 |
| DATE_ADD(d,INTERVAL expr type)	| 同 ADDDATE(d,INTERVAL n type) |
| SUBDATE(d,n)						| 计算起始日期 d 减去 n 天的日期 |
| SUBDATE(d,INTERVAL expr type)		| 计算起始日期 d 减去一个时间段后的日期 |
| ADDTIME(t,n)						| 计算起始时间 t 加上n 杪的时间 |
| SUBTIME(t,n)						| 计算起始时间 t 减去 n 秒的时间 |
| DATE_FORMAT(d,f)					| 按照表达式 f 的要求显示日期 d |
| TIME_FORMAT(t, f)					| 按照表达式 f 的要求显示时间 t |
| GET_FORMAT(type,s)				| 根据字符串 s 获取 type 类型数据的显示格式 |

#### MySQL的日期隔离类型

| 类型 | 含义 | expr 表达式的形式 |
| ---- | ---- | ----------------- |
| YEAR				| 年			| YY |
| MONTH				| 月			| MM |
| DAY				| 日			| DD |
| HOUR				| 时			| hh |
| MINUTE			| 分			| Inm |
| SECOND			| 秒			| SS |
| YEAR_MONTH	| 年和月		| YY 和MM之间用任意符号隔开 |
| DAY_HOUR		| 日和小时		| DD 和 hh 之间用任意符号隔开 |
| DAY_MINUTE	| 日和分钟		| DD 和 mm之间用任意符号隔开 |
| DAY_SECOND	| 日和秒钟		| DD 和 ss 之间用任意符号隔开 |
| HOUR_MINUTE	| 时和分		| hh 和 mm 之间用任意符号隔开 |
| HOUR_SECOND	| 时和秒		| hh 和 ss 之间用任意符号隔开 |
| MINUTE_SECOND	| 分和秒		| mm 和 ss 之间用任意符号隔开 |

```sql
select dt, ADDDATE(dt, INTERVAL '-1 -1'  YEAR_MONTH) from t4;		# 计算一年零一个月前的日期和时间
```

#### MySQL的日期时间格式

| 符号 | 含义 | 取值示例 |
| ---- | ---- | -------- |
| %Y	| 以4位数字表示年份		| 2008,2009 等 |
| %y	| 以2位数字表示年份		| 98,99等 |
| %m	| 以2位数字表示月份		| 01,02,...,12 |
| %c	| 以数字表示月份		| 1,2,...,12 |
| %M	| 月份的英文名			| January,February,...,December |
| %b	| 月份的英文缩写		| Jan,Feb,...,Dec |
| %U	| 表示星期数，其中 Sunday 是星期的第一天	| 00~52 |
| %u	| 表示星期数，其中 Monday 是星期的第一天	| 00~52 |
| %j		| 以3位数字表示年中的天数		| 001~366 |
| %d		| 以2位数字表示月中的几号		| 01,02,...31 |
| %e		| 以数字表示月中的几号			| 1,2,...31 |
| %D		| 以英文后缀表示月中的几号		| lst,2nd,... |
| %W		| 以数字的形式表示星期几		| 0 表示 Sunday，1 表示 Monday,.... |
| %W		| 星期几的英文名				| Monday, ..., Sunday |
| %a		| 星期几的英文缩写				| Mon,... , Sun |
| %T		| 24小时制的时间形式			| 00：00：00~23：59：59 |
| %r		| 12 小时制的时间形式			| 12:00:00AM~11:59:59PM |
| %p		| 上午（AM）或下午（PM）		| AM 或PM |
| %k		| 以数字表示 24 小时			| 0,1,…,23 |
| %l		| 以数字表示 12 小时			| 1,2,...,12 |
| %H		| 以2位数表示24小时				| 00,01,...,23 |
| %h,%I		| 以2位数表示12小时				| 01,02,...,12 |
| %i		| 以2位数表示分					| 00,01,...,59 |
| %S,%s		| 以2位数表示时					| 00,01,...,59 |
| %%		| 标识符%						| % |

#### GET_FORMAT函数返回的格式字符串

| 函数 | 返回的格式字符串 | 日期与时间的示例 |
| ---- | ---------------- | ---------------- |
| GET_FORMAT(DATE, 'EURT')				| %d.%m.%Y			| 30.02.2010 |
| GET_FORMAT(DATE, 'USA')				| %m.%d.%Y			| 02.30.2010 |
| GET_FORMAT(DATE, 'JIS')				| %Y-%m-%d			| 2010-02-30 |
| GET_FORMAT(DATE, 'ISO')				| %Y-%m-%d			| 2010-02-30 |
| GET_FORMAT(DATE, 'TINTERNAL')			| %Y%m%d			| 20100230 |
| GET_FORMAT(DATETIME, 'EUR')			| %Y-%m-%d-%H.%i.%s	| 2010-02-30-15.20.04 |
| GET_FORMAT(DATETIME, 'USA')			| %Y-%m-%d-%H.%i,%s	| 2010-02-30-15,20.04 |
| GET FORMAT(DATETIME, 'JIS')			| %Y-%m-%d %H:%i:%s	| 2010-02-30 15:20:04 |
| GET_FORMAT(DATETIME, 'ISO')			| %Y-%m-%d %H:%i:%s	| 2010-02-30 15:20:04 |
| GET_FORMAT(DATETIME, 'TNTERNAL')		| %Y%m%d%H%i%s		| 20100230152004 |
| GET_FORMAT(TIME, 'EUR')				| %H.%i.%S			| 15.20.04 |
| GET_FORMAT(TIME, 'USA')				| %h:%i:%s %p		| 03.20.04 PM |
| GET_FORMAT(TIME, 'JIS')				| %H:%i:%s			| 15：20：04 |
| GET_FORMAT(TIME, 'ISO')				| %H:%i:%s			| 15：20：04 |
| GET_FORMAT(TIME, 'TNTERNAL')			| %H%i%s			| 15：20：04 |

```sql
select get_format(datetime, 'ISO') from dual;
```

### 条件判断函数

```sql
# IF 函数
select id, grade, IF(grade>=60, 'PASS','FAIL') from stu_table;		# 大于 60 显示 PASS； 小于60 显示 FAIL

# IFNULL 函数
select id, IFNULL(grade, 'NO GRADE') from stu_table;			   # grade 值不为 NULL 显示 grade 值， 为 NULL 显示 NO GRADE

# CASE 函数
select id, grade,
case 
	when grade>60 then 'GOOD' 
	when grade=60 then 'PASS' 
	else 'FAIL' end grade_level
from stu_table;

# 另一种写法
select id, grade,
case grade 
	when 90 then 'GOOD' 
	when 60 then 'PASS' 
	when 50 then 'FAIL'
	else 'NO GRADE' end grade_level
from stu_table;
```

### 系统信息函数

```sql
# 获取数据版本
select version() from dual;

# 获取连接数
select connection_id() from dual;

# 获取数据库名
select database() from dual;
select scheme() from dual;

# 获取用户名
select user() from dual;
select system_user() from dual;
select session_user() from dual;
select current_user() from dual;
select current_user from dual;

# 获取字符串的字符集
select charset('aa') from dual;
# 获取字符串的 排序方式
select collation('aa') from dual;

# 获取最后一个自动生成的ID 值
select last_insert_id() from dual;

# 加密函数
select password(str) from dual;

# MD5
select MD5('abcd') from dual;

# ENCODE 加密
select encode('abcd', 'aa') from dual;		# 用 'aa' 来给 'abcd' 加密

# DECODE 加密
select decode(encode('abcd', 'aa'), 'aa')	# 用 'aa' 来给 encode('abcd', 'aa')的结果 解密
```

### 其他函数

```sql
# 格式化函数
select format(234.35677, 3) from dual;			# 234.357 , 四舍五入

# 不同进制的转换
select ASCII('ABC') from dual;				 # 65, 转换第一个字符的 ASCII 码
select BIN(28) from dual;					# 11100 二进制
select HEX(28) from dual;					# 1C 十六进制
select OCT(28) from dual;					# 34 八进制

select conv(28, 10, 2) from dual;			# 11100 指定 28 为十进制， 转换为二进制
select conv(28, 16, 2) from dual;			# 101000 指定 28 为十六进制， 转换为二进制
select conv(28, 16, 8) from dual;			# 50 指定 28 为十六进制， 转换为八进制

# IP地址与数字相互转换
select INET_ATON('59.65.226.15');			# 994173455
select INET_NTOA('994173455');				# 59.65.226.15

# 加解锁函数
select get_lock('MYSQL', 10);			# 返回 1， 说明加上了一个名为 MYSQL 的锁，时间为 10 秒
select if_free_lock('MYSQL');
select release_lock('MYSQL');			# 返回 1, 说明解锁成功

# 重复执行指定操作的函数
select benchmark(10000, NOW());

# 改变字符集
select charset('abc'), charset(convert('abc' USING gbk)) from dual;

# 改变字段数据类型
select d, case(d as DATE), convert(d, TIME) from some_table;
```

## 十一、存储过程和函数

存储过程和函数，是指将经常使用的一组SQL语句的组合在一起，并将这些SQL语句当做一个整体存储在MySQL服务器中。

### 存储过程

```sql
create procedure sp_name ([proc_parameter[...]])
	[characteristic...] routine_body
```

- sp_name : 存储过程的名称
- proc_parameter : 存储过程的参数列表
- characteristic : 指定存储过程的特性
- routine_body : SQL 代码的内容

#### 参数类型

proc_parameter 中的每个参数由三部分组成：输入输出类型、参数名和参数类型。形式为： `[IN | OUT | INOUT] param_name type`。

其中，`IN` 表示输入参数，`OUT` 表示输出参数。`type` 表示参数类型，可以是MySQL中的任意数据类型。

#### 存储过程特性

characteristic  参数可以有多个取值，每个取值及其含义如下：

- LANGUAGE SQL ：说明 routine_body 部分是由 SQL 语言的语句组成，数据库默认语言
- [NOT] DETERMINISTIC : 指明存储过程的执行结果是否是确定的。DETERMINISTIC 表示结果是确定的，每次执行存储过程，相同的输入会得到相同的输出。
- {CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA} : 指明子程序使用SQL语句的限制。默认为 CONTAINS SQL 

  - CONTAINS SQL : 表示子程序包含SQL语句，但是不包含读或写数据的语句
  - NO SQL ： 子程序不包含SQL语句
  - READS SQL DATA ：表示子程序包含读数据的SQL语句
  - MODIFIES SQL DATA：表示子程序包含写数据的SQL语句
- SQL SECURITY { DEFINER | INVOKER } : 指明谁有权限来执行。DEFINER 表示只有定义者自己才能执行；INVOKER 表示调用者可以执行。默认   DEFINER 。
- COMMENT 'msg string' ： 注释信息

> 创建存储过程时，系统默认 CONTAINS SQL ，但是如果确实没有使用 SQL语句，应该设置为 NO SQL。并且添加注释说明是一个良好的习惯。

例子：

```sql
# 创建一个包含读数据的SQL语句的存储过程
create procedure num_from_employee (IN emp_id INT, OUT count_num INT)
READS SQL DATA
BEGIN
	select count(0) into count_num from employee where d_id = emp_id;
END
```

### 函数

```sql
create function sp_name ([func_parameter[...]])
returns type
[characteristic...] routine_body
```

- sp_name : 函数的名称
- func_parameter ：函数参数
- type：函数返回的数据类型
- characteristic：指定函数的特性，与存储过程的取值一样
- routine_body：函数体

func_parameter 中的每个参数由两部分组成：参数名和参数类型。形式为： `param_name type`。其中，`type` 表示参数类型，可以是MySQL中的任意数据类型。

例子

```sql
# 
create function name_from_employee(emp_id INT)
returns varchar(20)
begin
	return (select name from employee where num=emp_id);
end
```

### 存储过程和函数内部SQL

#### 变量

```sql
# 定义变量
DECLARE var_name[...] type [DEFAULT value]
DECLARE my_id INT DEFAULT 1;

# 为变量赋值
SET var_name = expr [, var_name = expr] ...
SET my_id = 30;

SELECT col_name[...] INTO var_name[...] FROM tableName WHERE conditions;
SELECT d_id, name INTO my_id, my_name FROM employee WHERE d_id = 2;
```

#### 条件

```sql
DECLARE condition_name CONDITION FOR condition_value
condition_value:
	SQLSTATE [VALUE] sqlstate_value | mysql_error_code
	
# 方法一 ： 使用 sqlstate_value
DECLARE can_not_find CONDITION FOR SQLSTATE '42S02';
# 方法二 ：使用 mysql_error_code
DECLARE can_not_find CONDITION FOR 1146;
```

`sqlstate_value` 和 `mysql_error_code` 都可以表示 MySQL 的错误，比如 ERROR 1146（42S02）错误中，`sqlstate_value` 的值是 `42S42`，`mysql_error_code` 的值是 `1146`。

#### 定义处理程序

```sql
DECLARE handler_type HANDLER FOR condition_value[...] sp_statement
handler_type:
	CONTINUE | EXIT | UNDO
condition_value:
	SQLSTATE [VALUE] sqlstate_value | condition_name | SQLWARNING | NOT FOUND | SQLEXCEPTION | my_error_code
```

- handler_type : 指明遇到错误的处理方式，有3个取值，CONTINUE 表示继续；EXIT 表示退出；UNDO 表示撤回之前的操作。
- condition_value : 指明错误的类型。有6个取值。
  - sqlstate_value ：与条件中的定义同一个意思
  - my_error_code ：与条件中的定义同一个意思
  - condition_name : 是自定义的条件名称，比如上面的 `can_not_find`
  - SQLWARNING ：表示以 `01` 开头的 sqlstate_value 值。
  -  NOT FOUND ： 表示所有以 `02` 开头的 sqlstate_value 值。
  -  SQLEXCEPTION ： 表示所有没有被 SQLWARNING  和 NOT FOUND 捕获的 sqlstate_value 值。
- sp_statement ： 表示一些存储过程和函数的执行语句

```sql
# 方式一： 捕获 sqlstate_value
DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02' SET @info='CAN NOT FIND';
# 方式二：捕获 mysql_error_code
DECLARE CONTINUE HANDLER FOR 146 SET @info='CAN NOT FIND';
# 方式三： 先定义条件，再调用
DECLARE can_not_find CONDITION FOR 1146;
DECLARE CONTINUE HANDLER FOR can_not_find SET @info='CAN NOT FIND';
# 方式四： 使用 SQLWARNING
DECLARE EXIT HANDLER FOR SQLWARNING SET @info='ERROR';
# 方式五： 使用 NOT FOUND
DECLARE EXIT HANDLER FOR NOT FOUND SET @info='CAN NOT FIND';
# 方式六： 使用 SQLEXCEPTION 
DECLARE EXIT HANDLER FOR SQLEXCEPTION  SET @info='ERROR';
```

#### 光标（游标）

使用光标来逐条读取查询结果集中的记录。

```sql
DECLARE cursor_name CURSOR FOR select_statement;
```

- cursor_name : 光标的名称
- select_statement ： SQL查询语句的内容

```sql
DECLARE cur_employee CURSOR FOR select name, age from employee;

# 打开光标
OPEN cur_employee

# 使用光标
FETCH cur_employee INTO var_name[, var_name...];
FETCH cur_employee INTO emp_name, emp_age;

# 关闭光标
CLOSE cur_employee;
```

#### 流程控制

```sql
# IF 语句
IF age>20 THEN SET @count_num=@count_num+1;
ELSEIF age=20 THEN @count_fp=@count_fp+1;
ELSE @count_qq=@count_qq+1;
END IF;

# CASE 语句
CASE WHEN age=20 THEN SET @count_num=@count_num+1;
ELSE SET @count_fp=@count_fp+1;
END CASE;

# LOOP 循环语句
# begin_label 和 end_label 表示循环开始和结束的标志，标志必须相同，且都可以省略
[begin_label:] LOOP
	statement_list
END LOOP [end_label]
# 例子，该例子没有跳出循环，谨慎执行
add_num: LOOP
	SET @count_fp=@count_fp+1;
END LOOP add_num;

# LEAVE 语句
add_num: LOOP
	SET @count_fp=@count_fp+1;
	IF @count_fp=100 THEN
		LEAVE add_num;		# 跳出循环
	END IF;
END LOOP add_num;

# ITERATE 语句
# 类似 continue
add_num: LOOP
	SET @count_fp=@count_fp+1;
	IF @count_fp=100 THEN
		LEAVE add_num;		# break
	ELSEIF MOD(@count_fp,3)=0 THEN
		ITERATE add_num;	# continue
	END IF;
END LOOP add_num;

# REPEAT 语句
# 有条件的控制循环
REPEAT
	SET @count=@count+1;
	UNTIL @count=10
END REPEAT;

# WHILE 语句
WHILE @count<100 DO
	SET @count=@count+1;
END WHILE;
```

### 存储过程和函数的操作

```sql
# 调用存储过程
> CALL num_from_employee(1002, @n);
> select @n;
1

# 调用函数
> select name_from_employee(3);
张三

# 查看存储过程和函数
# 查看状态
SHOW {PROCEDURE | FUNCTION} STATUS [LIKE 'pattern'];
show PROCEDURE STATUS LIKE '%from_employee%';
# 查看具体定义
SHOW CREATE {PROCEDURE | FUNCTION} sp_name;
SHOW CREATE FUNCTION name_from_employee;
# 查看详细信息
SELECT * FROM information_schema.Routines WHERE ROUTINE_NAME = 'sp_name';
SELECT * FROM information_schema.Routines WHERE ROUTINE_NAME = 'num_from_employee';

# 修改存储过程和函数
ALTER {PROCEDURE | FUNCTION} sp_name [characteristic...]
characteristic：
	{CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA}
	| SQL SECURITY {DEFINER | INVOKER}
	| COMMENT 'msg string'
	
# 删除存储过程和函数
DROP {PROCEDURE | FUNCTION} sp_name;
```
