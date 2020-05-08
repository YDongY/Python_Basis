slots = []
slot_num = 32

# 初始化槽位
for _ in range(slot_num):
    slots.append([])


def put(slots, key, value):
    # 先计算索引值
    i = hash(key) % slot_num
    for index, (key, value) in enumerate(slots[i]):
        if key == key:
            break
    else:
        slots[i].append((key, value))



def get(slots, key):
    i = hash(key) % slot_num
    for k, v in slots[i]:
        if k == key:
            return v
    raise KeyError(key)


put(slots, 'a', '1')
put(slots, 'a', '2')
print(slots)
print(get(slots, 'a'))
# print(get(slots, 'b'))
