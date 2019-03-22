import threading
import time

G_NUMS = 0
# 创建一个互斥锁，默认没有上锁
mutex = threading.Lock()


def test(temp):
    global G_NUMS
    # 上锁,如果之前没有上锁，此时上锁
    # 如果之前已经上锁，此时等待解锁之后才能上锁
    for i in range(temp):
        mutex.acquire()
        G_NUMS += 1
        mutex.release()
    print("---test1---%d" % G_NUMS)  # ---test1---101


def test2(temp):
    global G_NUMS
    for i in range(temp):
        mutex.acquire()
        G_NUMS += 1
        mutex.release()
    print("-----test2----%s" % G_NUMS)  # -----test2----101


def main():
    t1 = threading.Thread(target=test, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()

    time.sleep(3)
    print("---main---%d" % G_NUMS)  # ---main---101


if __name__ == '__main__':
    main()
