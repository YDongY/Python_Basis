class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃")


class Dog(Animal):
    pass


dog = Dog("旺财")
print(dog.name)
dog.eat()
