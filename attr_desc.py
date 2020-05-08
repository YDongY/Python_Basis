import numbers


class IntField(object):
    """数据属性描述符：实现get和set"""

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass


class NoDataField(object):
    """非数据属性描述法符：只实现一个get方法"""

    def __get__(self, instance, owner):
        pass


class UserModel:
    # 属性描述符的对象
    age = IntField()


if __name__ == '__main__':
    user = UserModel()
    user.age = 30  # 调用__set__,instance:user,value:30
    print(user.age)
