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
