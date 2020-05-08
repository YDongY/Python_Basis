import threading
import time

G_NUM = 100


def test():
    global G_NUM
    G_NUM += 1
    print("---test1---%d" % G_NUM)  # ---test1---101


def test2():
    print("-----test2----%d" % G_NUM)  # -----test2----101


def main():
    t1 = threading.Thread(target=test)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("---main---%d" % G_NUM)  # ---main---101


if __name__ == '__main__':
    main()
