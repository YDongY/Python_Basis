import time
import gevent
from gevent import monkey

monkey.patch_all()  # 打补丁：自动将所有代码中的耗时操作，更换成gevent中的耗时


def test1():
    while True:
        print("-----1----")
        time.sleep(0.5)


def test2():
    while True:
        print("----2----")
        time.sleep(0.5)


# g1 = gevent.spawn(test1)
# g2 = gevent.spawn(test2)
# g1.join()  # 等待g1执行完
# g2.join()

# 以上可以归为下面这种写法
gevent.joinall([
    gevent.spawn(test1),
    gevent.spawn(test2)
])
