def line(k, b):
    def create_y(x):
        print(k * x + b)

    return create_y



line_1 = line(1, 2)
line_1(0)
line_1(1)
line_1(2)
print("="*10)
line(1,2)(0)
line(1,2)(1)
line(1,2)(2)
