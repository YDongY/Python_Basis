class Test(object):
    def __init__(self, name):
        self.__name = name


a = Test("ydy")
print(a.__dict__)  # {'_Test__name': 'ydy'}
print(a._Test__name)  # 私有属性实际是把变量名改了
print(Test.__dict__)
