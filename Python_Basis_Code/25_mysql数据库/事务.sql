--事务四大特性(简称ACID)
        --原子性(Atomicity)   : 如果执行就执行完，要么就不执行
        --一致性(Consistency) : 数据在commit之前不会因为系统挂了而出错
        --隔离性(Isolation)  : 一个sql的执行不会影响另一个sql，只能等待别的执行完, 即上锁
        --持久性(Durability) : 永久性的存储

-- 开启事务
    begin
--或者
    start transaction

--提交事务
commit

--回滚事务
rollback