# 函数只要有yield语句，这个就不再是函数，而是一个生成器的模板
def fibo(max_num):
    a, b = 0, 1
    current_num = 0
    while current_num < max_num:
        yield a
        a, b = b, a + b
        current_num += 1


# 调用函数时候，发现函数中有yield，此时不是调函数，而是创建一个生成器对象
obj = fibo(10)
for i in obj:
    print(i)
