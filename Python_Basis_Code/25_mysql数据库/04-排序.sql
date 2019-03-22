-- 排序
    -- order by 字段 ,默认asc
    -- asc 小->大
    -- desc 大->小

    -- 查询年龄18-34之间的男性,按照年龄由小到大
    select * from students where (age between 18 and 34) and gender=1 order by age;
    select * from students where (age between 18 and 34) and gender=1 order by age asc;
    
    -- 年龄在18-34之间女性，身高由高到低
    select * from students where (age between 18 and 34) and gender=2 order by height desc ;

    -- 年龄在18-34之间女性，身高由高到低 ,身高相同按照id由小到大
    select * from students where (age between 18 and 34) and gender=2 order by height desc,id desc ;
