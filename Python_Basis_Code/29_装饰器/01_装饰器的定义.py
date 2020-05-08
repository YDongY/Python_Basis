def set_func(func):
    def call_func():
        print("-----权限1----")
        print("-----权限2----")
        func()

    return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1():
    print("----test1----")


# ret = set_func(test1)
# ret()

# 装饰器的是实现过程
# test1 = set_func(test1)
test1()

from functools import wraps


def auth(func):
    @wraps(func)
    def wrapper(username, password):
        if username == 1 and password == 1:
            ret = func(username, password)
            return ret
        else:
            return "登录失败"

    return wrapper


@auth
def login(username, password):
    """
    登录函数
    :param username:用户名
    :param password: 密码
    :return:
    """
    return "登录成功"


# login = auth(login)
print(login(1, 1))
print(help(login))


# login()

def single(cls):
    instances = dict()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@single
class Person(object):
    def __init__(self):
        print("创建一个对象")


# single = single(Person)
person = Person()
person2 = Person()
print(person)  # <__main__.Person object at 0x7fc366f61d30>
print(person2)  # <__main__.Person object at 0x7fc366f61d30>
