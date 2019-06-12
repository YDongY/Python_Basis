class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 我来了" % self.name)

    def __del__(self):
        print("% s 我去了" % self.name)

    def __str__(self):
        return "我是 %s" % self.name


tom = Cat("tom")
print(tom)  # 默认打印：<__main__.Cat object at 0x000002B475CAC160>

