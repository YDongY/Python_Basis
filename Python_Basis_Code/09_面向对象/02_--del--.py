class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 我来了" % self.name)

    def __del__(self):
        print("% s 我去了" % self.name)


tom = Cat("tom")
print(tom.name)

del tom
print("-" * 50)
