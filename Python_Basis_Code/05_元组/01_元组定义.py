info_tuple = (1, 2, 3, ('zhangsan', '1.78', '20'))
info_tuple2 = (1,)

print(type(info_tuple))
print(info_tuple)
print("=" * 20)
print(type(info_tuple2))
print(info_tuple2)

print("=" * 20)

for info in info_tuple:
    print(info)
