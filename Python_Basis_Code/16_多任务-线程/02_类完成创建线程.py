import threading
import time


class Mythread(threading.Thread):
    def run(self):
        self.test()

    def test(self):
        for i in range(5):
            print("-----test----")
            time.sleep(1)


if __name__ == '__main__':
    t = Mythread()
    # 自动调用run方法
    t.start()
