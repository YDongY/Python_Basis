class Foo(object):
    def get_bar(self):
        return "哈哈"

    def set_bar(self, value):
        # 必须两个参数
        print("set_bar")
        return value

    def del_bar(self):
        print("del_bar")
        return "del_bar"

    BAR = property(get_bar, set_bar, del_bar, "dadadada")


f = Foo()
print(f.BAR)  # 调用get_bar
f.BAR = 200  # 调用set_bar
print(Foo.BAR.__doc__)  # 调用"dadadad"
del f.BAR  # 调用 del_bar
