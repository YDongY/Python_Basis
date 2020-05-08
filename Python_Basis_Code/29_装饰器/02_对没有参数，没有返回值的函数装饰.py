def set_func(func):
    def call_func():
        print("-----权限1----")
        print("-----权限2----")
        func()

    return call_func

@set_func
def test1():
    print("----test1----")

test1()
