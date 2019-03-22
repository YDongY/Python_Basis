--条件查询
    --比较运算符
        -- >
        --查询大于18岁的信息
        select * from students where age>18;

        -- <
        --查询小于18岁的信息
        select * from students where age<18;

        -- <=
        -->=
        --查询小于等于或大于等于18岁的信息
        select * from students where age<=18;
        select * from students where age>=18;

        -- =
        select * from students where age=18;

        -- !=或者<>
        select * from students where age!=18;
        
    --逻辑运算符
        -- and
        -- 18到28之间所有信息
        select * from students where age>18 and age<28;

        -- 18岁以上的女性
        select * from students where age>18 and gender='女';
        select * from students where age>18 and gender=2;

        -- or
        -- 18 以上或者身高超过180（包含）以上
        select * from students where age>18 or height>=180;
        
        -- not
        -- 不在 18以上的女性这个范围的信息
        select * from students where not (age>18 and gender=2);

        -- 年龄不是小于或者等于18 并且是女性
        select * from students where not age <=18 and gender=2;

    --模糊查询
        -- like
        -- %替换1个或者多个
        -- _替换一个
        -- 查询姓名中 以“小”开头的名字
        select * from students where name like "小%";

        --查询有小的所有名字
        select name from students where name like "%小%";

        -- 查询有2个字的名字
        select name from students where name like "__";

        -- 查询至少2个字的名字
        select name from students where name like "__%";

        -- rlike 正则
        -- 查询以 周开始的名字
        select name from students where name rlike "^周.*";

        -- 查询以 周开始、伦结束的名字
        select name from students where name rlike "^周.*伦$";

    --范围查询

        -- in (1,3,8)表示一个非连续的范围
        -- 查询 年龄为18 ，34的姓名
--         select name,age from students where age=18 or age=34;
        select name,age from students where age in (18,34,12);

        -- not in
        -- 年龄不是 18 ，34 的姓名
        select age,name from students where age not in(18,34) ;
        
        -- between and
        --年龄在18-34之间的信息
        select * from students where age between 18 and 34;

        -- not between and
        select * from students where not age between 18 and 34;
        
    -- 空判断
        -- 判空 is null
        -- 查询升高为空的
        select * from students where height is null ;
        
        -- is not null
        select * from students where height is not null;
