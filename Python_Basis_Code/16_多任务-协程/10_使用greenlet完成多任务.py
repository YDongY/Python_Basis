import time
from greenlet import greenlet


def test1():
    while True:
        print("-----1----")
        gr2.switch()  # 切换到test2运行
        time.sleep(0.1)


def test2():
    while True:
        print("----2----")
        gr1.switch()  # 切换到test1运行
        time.sleep(0.1)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()  # 先切换到test1运行
