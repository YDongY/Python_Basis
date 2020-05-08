-- 子查询相对比较慢

-- 查询最高的男生信息
select * from students where height=(select max(height) from students);

select * from areas where pid=(select aid from areas where atitle="湖北省");
select * from areas where pid=(select aid from areas where atitle="襄阳市");

