from collections.abc import Iterable, Iterator


class MyIterator(Iterator):
    def __init__(self, li):
        self.list = li
        self.index = 0

    def __next__(self):
        try:
            item = self.list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return item


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)


com = Company(["bobby", "join", "jack"])
for c in com:
    print(c)
