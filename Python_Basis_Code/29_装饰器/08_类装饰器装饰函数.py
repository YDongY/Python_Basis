class Test(object):
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这是装饰权限")
        return self.func()

@Test  # 相当于 get_str = Test(get_str)
def get_str():
    return "haha"

print(get_str()) # 相当于 对象名() ，直接调用__call__方法
