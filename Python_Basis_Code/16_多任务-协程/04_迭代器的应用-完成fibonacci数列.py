class Fibonacci(object):
    def __init__(self, max_num):
        self.max_num = max_num
        self.a = 0
        self.b = 1
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.max_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibo = Fibonacci(10)
for num in fibo:
    print(num)
