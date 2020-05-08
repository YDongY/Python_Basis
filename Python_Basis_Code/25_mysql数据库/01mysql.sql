--数据库操作

      --链接数据库
      mysql -uroot -p

      --退出数据库
      exit/quit/ctrl+d

      --显示时间
      select now();

      --显示版本
      select version();

      --查看所有数据库
      show databases;

      --创建数据库,指定编码utf8
      create database python charset=utf8;

      --显示创建数据库
      show create datebase python;

      --查看当前数据库
      select database();

      --使用数据库
      use python;

      --删除数据库
      drop database python;


--数据表操作

      --查看当前数据库的所有表
      show tables;


      --创建表
      create table xxx(id int primary key ,name varchar (20));

      --desc:表结构
      desc stu;

      --显示创建表
      show create table stu;


      --创建一个学生表
      create table stu(
        id int unsigned not null auto_increment primary key ,
        name varchar (20),
        age tinyint unsigned,
        high decimal (5,2),
        gender enum("男","女","保密","中性") default "保密",
        cls_id int unsigned
      );

      --创建班级表
      create table class(
        id int unsigned not null primary key auto_increment,
        name varchar (30)
      );

      --插入数据
      insert into  stu values (0,"ydy",22,172.00,"男",0);

      --查看所有数据
      select * from stu;

      --添加字段
      alter table stu add birthday datetime;

      --修改字段-不重名
      alter table stu modify birthday date ;
      --修改字段-重命名
      alter table stu change birthday birth date default "2019-02-24";

      --删除字段
      alter table stu drop high;

      --删除表
      drop table stu;



--增删查改

            +--------+-------------------------------+------+-----+------------+----------------+
      | Field  | Type                          | Null | Key | Default    | Extra          |
      +--------+-------------------------------+------+-----+------------+----------------+
      | id     | int(10) unsigned              | NO   | PRI | NULL       | auto_increment |
      | name   | varchar(20)                   | YES  |     | NULL       |                |
      | age    | tinyint(3) unsigned           | YES  |     | NULL       |                |
      | gender | enum('男','女','保密','中性') | YES  |     | 保密       |                |
      | cls_id | int(10) unsigned              | YES  |     | NULL       |                |
      | birth  | date                          | YES  |     | 2019-02-24 |                |
      +--------+-------------------------------+------+-----+------------+----------------+

    --增加
        --全列插入
        insert into class  values (0,"软件1601");
        insert into stu values(0,"lbx",22,"男",1,"1997-01-01");
        insert into stu values(null,"lbx",22,"男",1,"1997-01-01");
        insert into stu values(default ,"lbx",22,"男",1,"1997-01-01");

        --部分插入
        insert into stu(name,age) values ("laowang",22);

        --多行插入
        insert into stu(name,age) values ("张三",23),("李四",25);

    --修改
        update stu set cls_id=1 where id=3;
        update stu set cls_id=2 where id=4 or id=5;
        update stu set gender = "男" where id>=3;

    --删除
        --物理删除
        delete from stu;

        --逻辑删除
        --添加一个字段标记是否删除
        --给stu表添加is_delete字段bit类型
        alter table stu add is_delete bit default 0;
        update stu set is_delete = 1 where id = 5;

    --查询
        --查询所有
        select * from stu;


        --指定条件查询
        select * from stu where id<3;

        --查询指定列
        select name,gender from stu;

        --字段顺序

        --可以使用as为列或表指定别名
        select name as "姓名",gender as "性别" from stu;


