class Sample(object):
    def __enter__(self):
        print("enter")
        # 获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_something(self):
        print("doing something")


with Sample() as sample:
    sample.do_something()

# enter
# doing something
# exit

