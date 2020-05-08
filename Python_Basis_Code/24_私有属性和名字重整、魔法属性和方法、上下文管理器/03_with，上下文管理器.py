# 普通版
def m1():
    f = open("xxx", "w")
    f.write("ahha")
    f.close()


# 进阶版
def m2():
    f = open("xxx", "w")
    try:
        f.write("fdadad")  # 可能产生异常的代码写在try中
    except IOError:
        print("error")
    finally:
        f.close()


# 高级版
def m3():
    with open("xxx", "w") as f:  # 不管是否出现异常都会自动关闭
        f.write("dadad")


# 上下文管理器
class File(object):
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with File("xxx", "w") as f:
    f.write("adadad")

# 另一种方式定义上下文管理器
from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    f = open(path, mode)  # 调用with执行
    yield f
    f.close()  # 执行完毕运行


# 调用
with my_open("xxx", "w") as f:
    f.write("sdadad")
