import time
import gevent


def test1():
    while True:
        print("-----1----")
        # time.sleep(0.5)
        gevent.sleep(0.5)  # 遇到耗时操作就切换


def test2():
    while True:
        print("----2----")
        # time.sleep(0.5)
        gevent.sleep(0.5)


g1 = gevent.spawn(test1)
g2 = gevent.spawn(test2)
g1.join()  # 等待g1执行完
g2.join()
