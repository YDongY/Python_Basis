import contextlib

from collections import abc
@contextlib.contextmanager
# 装饰的必须是一个生成器
def file_open(filename):
    print("file open")  # 相当于类中的__enter__
    yield {}
    print("file end")  # 相当于类中的__exit__


with file_open("test.txt") as f:
    print("file")

# file open
# file
# file end
