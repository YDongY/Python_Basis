-- 聚合函数
    -- 总数 count
    -- 查询男性有多少人， 女性有多少
    select count(*) from students where gender=1;
    select count (*) from students where gender=1;

    -- 最大值 max
    -- 查询最大年龄
    select max(age) from students;


    -- 最小值 min
    -- 身高最矮的女性
    select min(height) from students where gender=2;

    -- 求和 sum
    -- 计算所有人的年龄总和
    select sum(age) from students ;

    -- 平均值 avg
    select avg(age) from students;
    select sum(age)/count(*) from students ;

    -- 四舍五入round(123.45,2) 保留两位小数
    select round(avg(age),2) from students;

    -- 计算男性的平均身高，保留两位
    select round(avg(height),2) from students where gender=1;

-- 分组

    -- group by
    -- 按照性别分组,查询所有的性别
    select gender from students group by gender;

    -- 计算每种性别的人数
    select gender,count(*) from students group by gender;

    -- group_concat()
    -- 查询同种性别中的姓名
    select gender,group_concat(name) from students group by gender;
    select gender,group_concat(name," ",age," ",id) from students group by gender;

    -- having,从查询的结果中获得东西
    -- 查询平均年龄超过30岁的性别，以及姓名
    select gender,group_concat(name," ",age),avg(age) from students group by gender having avg(age)>30;

    -- 查询每种性别中的人数多余2个的信息
    select gender,group_concat(name) from students group by gender having count(*)>2;
    select gender,group_concat(name) from students group by gender having count(*)<2;
