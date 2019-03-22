# 函数只要有yield语句，这个就不再是函数，而是一个生成器的模板
def fibo(max_num):
    a, b = 0, 1
    current_num = 0
    while current_num < max_num:
        yield a
        a, b = b, a + b
        current_num += 1
    return "ok..."


# 调用函数时候，发现函数中有yield，此时不是调函数，而是创建一个生成器对象
obj = fibo(10)
while True:
    try:
        ret = next(obj)
        print(ret)
    except StopIteration as ret:
        print(ret.value)  # 产生异常是捕获，得到带有yield函数的返回值
        break
