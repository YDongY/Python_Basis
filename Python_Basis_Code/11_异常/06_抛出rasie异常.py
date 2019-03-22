def input_password():
    pwd = input("输入密码：")
    if len(pwd) >= 8:
        return pwd
    print("主动抛出异常")
    # 1. 创建异常对象
    ex = Exception("密码长度不够")
    # 2. 主动抛出异常
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)
