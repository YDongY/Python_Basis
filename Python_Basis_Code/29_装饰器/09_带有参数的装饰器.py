def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("---权限级别1，验证---")
            elif level_num == 2:
                print("---权限级别2，验证---")
            return func()

        return call_func

    return set_func


@set_level(1)
# 1.调用set_level将参数做实参传递 相当于 调用set_level(1) 返回值 set_func
# 2.用上一步的返回值当作装饰器对test1函数进行装饰 test1 = set_func(test1)

def test1():
    print("-----test1----")
    return "ok"


@set_level(2)
def test2():
    print("-----test1----")
    return "ok"


test1()
test2()
