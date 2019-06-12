class Province(object):
    # 类属性
    country = "中国"

    def __init__(self, name):
        self.name = name


# 创建一个实例对象
obj = Province("陕西")
print(obj.__class__)  # 用于查找对象有哪个类创建的
