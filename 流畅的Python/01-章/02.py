from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # def __bool__(self):
    #     return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# __add__ 类具有加法运算
print(Vector(1, 2) + Vector(2, 3))  # Vector(3, 5)
# __mul__ 类具有乘法运算
print(Vector(1, 2) * 2)  # Vector(2,4)

# 如果没有实现 __repr__，
# 当我们在控制台里打印一个向量的实例时，
# 得到的字符串可能会是 <Vector object at 0x10e100070>。
print(Vector(0, 1))

# __abs__
print(abs(Vector(3, 4)))  # 5.0

# __bool__
print(bool(Vector(0, 0)))  # false
