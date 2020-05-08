-- 链接查询
-- 内连接 ： 交集
      +----+--------+------+--------+--------+--------+-----------+-------------+
      | id | name   | age  | height | gender | cls_id | is_delete | name        |
      +----+--------+------+--------+--------+--------+-----------+-------------+
      |  1 | 小明   |   18 | 180.00 | 女     |      1 |           | python_01期 |
      |  2 | 小月月 |   18 | 180.00 | 女     |      2 |          | python_02期 |
      |  3 | 彭于晏 |   29 | 185.00 | 男     |      1 |           | python_01期 |
      |  4 | 刘德华 |   59 | 175.00 | 男     |      2 |          | python_02期 |
      |  5 | 黄蓉   |   38 | 160.00 | 女     |      1 |           | python_01期 |
      |  6 | 凤姐   |   28 | 150.00 | 保密   |      2 |          | python_02期 |
      |  7 | 王祖贤 |   18 | 172.00 | 女     |      1 |          | python_01期 |
      |  8 | 周杰伦 |   36 |   NULL | 男     |      1 |           | python_01期 |
      |  9 | 程坤   |   27 | 181.00 | 男     |      2 |           | python_02期 |
      | 10 | 刘亦菲 |   25 | 166.00 | 女     |      2 |           | python_02期 |
      | 11 | 金星   |   33 | 162.00 | 中性   |      3 |          | python_04期 |
      +----+--------+------+--------+--------+--------+-----------+-------------+
      -- inner join ..on
      --select * from 表A inner join 表B
      select * from students inner join classes;

      -- 查询 又能够对应班级的学生以及班级信息
      select * from students inner join classes on students.cls_id=classes.id;

      -- 按要求显示名字，班级
      select students.*,classes.name from students inner join classes on students.cls_id=classes.id;

      -- 给表起名字
      select stu.*,cls.name from students as stu inner join classes as cls on stu.cls_id=cls.id;

      -- 以上查询班级名字放在第一列
      select cls.name,stu.* from students as stu inner join classes as cls on stu.cls_id=cls.id;

      --以上查询班级名字放在第一列,按班级进行排序之后再按学号排序
      select cls.name,stu.* from students as stu inner join classes as cls on
      stu.cls_id=cls.id order by cls.name asc,stu.id asc;

-- 外连接:左连接，右链接
      +----+--------+------+--------+--------+--------+-----------+------+-------------+
      | id | name   | age  | height | gender | cls_id | is_delete | id   | name        |
      +----+--------+------+--------+--------+--------+-----------+------+-------------+
      |  1 | 小明   |   18 | 180.00 | 女     |      1 |           |    1 | python_01期 |
      |  3 | 彭于晏 |   29 | 185.00 | 男     |      1 |           |    1 | python_01期 |
      |  5 | 黄蓉   |   38 | 160.00 | 女     |      1 |           |    1 | python_01期 |
      |  7 | 王祖贤 |   18 | 172.00 | 女     |      1 |          |    1 | python_01期 |
      |  8 | 周杰伦 |   36 |   NULL | 男     |      1 |           |    1 | python_01期 |
      |  2 | 小月月 |   18 | 180.00 | 女     |      2 |          |    2 | python_02期 |
      |  4 | 刘德华 |   59 | 175.00 | 男     |      2 |          |    2 | python_02期 |
      |  6 | 凤姐   |   28 | 150.00 | 保密   |      2 |          |    2 | python_02期 |
      |  9 | 程坤   |   27 | 181.00 | 男     |      2 |           |    2 | python_02期 |
      | 10 | 刘亦菲 |   25 | 166.00 | 女     |      2 |           |    2 | python_02期 |
      | 11 | 金星   |   33 | 162.00 | 中性   |      3 |          |    3 | python_04期 |
      | 12 | 静香   |   12 | 180.00 | 女     |      4 |           | NULL | NULL        |
      | 13 | 郭靖   |   12 | 170.00 | 男     |      4 |           | NULL | NULL        |
      | 14 | 周杰   |   34 | 176.00 | 女     |      5 |           | NULL | NULL        |
      +----+--------+------+--------+--------+--------+-----------+------+-------------+
      -- left join
      -- 查询每位学生对应的班级信息
      select * from students left join classes on students.cls_id=classes.id;
      -- right join
      -- 将表的名字对调，使用left join完成

      -- 查询班级为空的学生
      select * from students left join classes on students.cls_id=classes.id having classes.id is null ;
      select * from students left join classes on students.cls_id=classes.id where classes.id is null ;