class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        # 判断某个值是什么类型
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整数")

    # 还可以使用装饰器的方式
    money = property(getMoney, setMoney)


a = Money()
print(a.money)
a.money = 100  # 调用setMoney
print(a.money)  # 调用getMoney
