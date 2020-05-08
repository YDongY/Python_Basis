from collections import abc


class DictDIY:
    def __init__(self):
        self.dic = dict()

    def __getitem__(self, key):
        return self.dic[key]

    def __setitem__(self, key, value):
        self.dic[key] = value
        return self.dic

    def __delitem__(self, key):
        del self.dic[key]


a = dict()
dic = DictDIY()
dic["a"] = 1
dic["b"] = 2
print(dic["a"])
