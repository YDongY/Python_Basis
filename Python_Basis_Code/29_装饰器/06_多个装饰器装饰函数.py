def add_func(func):
    print("开始进行装饰权限1")
    def call_func(*args, **kwargs):
        print("-----权限1----")
        return func(*args, **kwargs)
    return call_func

def add_xx(func):
    print("装饰xxx的功能")
    def call_func(*args, **kwargs):
        print("-----xxx功能----")
        return func(*args, **kwargs)
    return call_func

@add_func
@add_xx  # 先装下面的，再装上面的，执行时，最后装的之最先执行
def test1():
    print("----test1----")


test1()
