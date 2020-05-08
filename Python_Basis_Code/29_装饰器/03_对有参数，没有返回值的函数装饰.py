def set_func(func):
    def call_func(a):
        print("-----权限1----")
        print("-----权限2----")
        func(a)

    return call_func


@set_func
def test1(num):
    print("----test1----%s" % num)


test1(100)
