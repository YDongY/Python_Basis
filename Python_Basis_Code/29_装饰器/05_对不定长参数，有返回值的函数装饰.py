def set_func(func):
    def call_func(*args, **kwargs):
        print("-----权限1----")
        print("-----权限2----")
        return func(*args, **kwargs)  # ok返回到这，在返回ret

    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("----test1----%s", num)
    print("----test1----%s", args)
    print("----test1----%s", kwargs)
    print("=" * 20)
    return "ok"


ret = test1(100)
print(ret)
# test1(200, 300)
# test1(100, 200, a=200, b=300)
