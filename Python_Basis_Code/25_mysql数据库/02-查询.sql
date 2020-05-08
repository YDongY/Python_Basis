--查询
    --查询所有字段
    select * from students;
    select * from classes;

    --查询指定字段
    select name,age from students;

    --使用as给字段起别名
    select name as 姓名, age as 年龄 from students;

    --通过as 给表起别名
    select students.name,students.age from students;
    select stu.name from students as stu;

    --消除重复行
    --distinct 字段
    select distinct gender from students;