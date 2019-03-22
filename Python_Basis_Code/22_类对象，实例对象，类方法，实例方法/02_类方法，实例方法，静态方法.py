class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        print("实例方法")

    @classmethod
    def class_func(cls):
        print("类方法")

    @staticmethod
    def static_func():
        print("静态方法")


f = Foo("中国")

f.class_func()
f.ord_func()
f.static_func()
print("------------------")
Foo.static_func()
Foo.class_func()
