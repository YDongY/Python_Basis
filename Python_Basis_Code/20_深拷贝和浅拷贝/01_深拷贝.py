import copy

a = [11, 22]
b = copy.deepcopy(a)  # 深拷贝直接把所有的值复制一遍
print(id(a))
print(id(b))
