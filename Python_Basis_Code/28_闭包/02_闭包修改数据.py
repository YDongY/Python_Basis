x = 300


def test1():
    x = 200

    def test2():
        nonlocal x # 想要修改外部函数的值必须添加此关键字
        print("-----1-----%d" % x) # 调用外部函数的数据
        x = 100
        print("-----2-----%d" % x) # 修改了外部函数的数据
    return test2
t = test1()
t()