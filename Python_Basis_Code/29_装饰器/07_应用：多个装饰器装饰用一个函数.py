def add_str(func):
    def call_func():
        # add_content = "<h1>%s</h1>"
        # return add_content % func()
        return "<h1>" + func() + "</h1>"

    return call_func


@add_str  # 相当于 get_str = add_str(get_str)
def get_str():
    return "haha"


print(get_str())
