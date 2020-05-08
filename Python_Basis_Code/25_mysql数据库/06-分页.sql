-- 分页

    -- limit start,count
    -- 限制查询出来的数据个数
    select * from students  where gender=1 limit 2;
    
    -- 查询前5个数据
    select * from students limit 0,5;
    
    -- 查询6-10
    select * from students limit 5,5;

    -- 每页显示两个，显示第六页信息，按照年龄从小到大排序
    select * from students order by age asc limit 10,2;