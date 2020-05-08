xiaoming = {'name': '小明',
            'age': 18,
            'gender': True,
            'height': 1.75
            }
# # 1. 取值
# print(xiaoming['name'])
#
# # 2. 增加
# xiaoming['comment'] = 'student'
# print(xiaoming)
#
# # 3. 修改
# xiaoming['name'] = '小小明'
# print(xiaoming)
#
# # 4. 删除
# xiaoming.pop('name')
# print(xiaoming)


# 5. 统计键值对的数量
print(len(xiaoming))

# 6. 合并字典
temp = {
    "class":'软件1601'
}
# 如果被合并的字典中包含已经存在的键值对，会替换以前的字典
xiaoming.update(temp)
print(xiaoming)

# 7. 清空
xiaoming.clear()
print(xiaoming)