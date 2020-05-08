import threading
import time

G_NUMS = [11, 22]


def test(temp):
    temp.append(33)
    print("---test1---%s" % str(temp))  # ---test1---101


def test2(temp):
    print("-----test2----%s" % str(temp))  # -----test2----101


def main():
    t1 = threading.Thread(target=test, args=(G_NUMS,))
    t2 = threading.Thread(target=test2, args=(G_NUMS,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("---main---%s" % str(G_NUMS))  # ---main---101


if __name__ == '__main__':
    main()
