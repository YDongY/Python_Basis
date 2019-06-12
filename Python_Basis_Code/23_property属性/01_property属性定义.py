class Foo(object):
    def func(self):
        print("实例方法")

    # 第一种：定义property属性 ， 参数只能有一个self
    @property
    def prop(self):
        # 必须有个返回值
        return 100

    # 第二种
    @prop.setter
    def prop(self, value):
        print("@price.setter", value)

    @prop.deleter
    def prop(self):
        print("@prop.deleter")


f = Foo()
f.func()
ret = f.prop  # 调用property属性  相当于调用了一个属性
print(ret)
f.prop = 200  # 设置property属性
del f.prop  # 删除property属性

