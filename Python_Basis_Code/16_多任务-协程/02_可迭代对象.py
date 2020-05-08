from collections.abc import Iterable, Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        '''如果想要一个对象称为一个 可以迭代的对象，
        即可以使用for 那么必须实现__iter__方法
        '''
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.num < len(self.obj.names):
            ret = self.obj.names[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老王")
classmate.add("张三")
classmate.add("李四")

# 当类中含有__iter__方法，则此类创建的对象就是可迭代对象
# print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))

# classmate_iterator = iter(classmate)  # 自动调用__iter__方法

# print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))

# for循环自动调用classmate对象的__iter__ 方法，返回值的对象自动调用__next__方法
for name in classmate:
    print(name)
    time.sleep(1)
