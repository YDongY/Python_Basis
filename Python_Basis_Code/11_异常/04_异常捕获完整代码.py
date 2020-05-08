try:
    num = int(input("输入一个整数："))
    res = 8 / num
    print(res)
except ValueError:
    print("请输入正确的整数")
except ZeroDivisionError:
    print("除0错误")
except Exception as result:
    print(result)
else:
    print("没有异常执行")
finally:
    print("无论是否发生异常都会执行的代码")
print("-" * 50)
