import bisect

# 用来处理已排序的序列,用来维持已排序的序列，升序

# 二分查找
inter_list = []

bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 4)

print(bisect.bisect(inter_list, 3))  # 查找 3
print(bisect.bisect_left(inter_list, 3))  # 查找 2
print(inter_list)
