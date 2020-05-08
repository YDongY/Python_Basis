string = "hello python"

print(string.count("o"))
print(string.count("abc"))  # 子串不存在，0

print(string.index("o"))
print(string.index("abc"))  # 子串不存在，报错
