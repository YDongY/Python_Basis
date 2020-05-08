import re

email = input("输入163邮箱地址：")
# 例如： . ?等,匹配前需要转义
# ()：分组，可以取值
ret = re.match(r"^[a-zA-Z0-9]{4,20}@(163|qq)\.com$", email)
if ret:
    print(ret.group())
else:
    print("错误")
