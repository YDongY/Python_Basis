def print_line(char, num):
    print(char * num)


def print_lines(char, times):
    """打印多行分隔线

    :param char: 分隔线使用的分隔符
    :param times:分隔线重复的次数
    """
    i = 0
    while i < 5:
        print_line(char, times)
        i += 1


print_lines('-', 50)
