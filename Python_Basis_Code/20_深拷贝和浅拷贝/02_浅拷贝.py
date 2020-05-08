import copy

a = [11, 22]
b = [33, 44]

c = [a, b]
# a的引用指向[11,22]
# b的引用指向[33,44]
e = copy.copy(c)  # 只拷贝c, c里面的东西都不变
print(c)
