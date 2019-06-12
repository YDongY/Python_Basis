from collections import Iterable

# 列表 元组 字典 集合 字符串都是可迭代的
print(isinstance([11, 22, 33], Iterable))  # True

print(isinstance((11, 22, 33), Iterable))  # True

print(isinstance("abcd", Iterable))  # True

print(isinstance({'a': 10, 'b': 20}, Iterable))  # True
