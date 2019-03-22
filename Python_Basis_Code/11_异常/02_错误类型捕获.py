try:
    num = int(input("输入一个整数："))
    result = 8 / num
    print(result)
except (ZeroDivisionError, ValueError):
    print("除0错误")
# except ValueError:
#     print("输入正确整数")
