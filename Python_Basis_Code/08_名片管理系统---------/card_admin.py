def main_frame():
    print("=" * 100)
    print("欢迎使用【名片管理系统】v1.0")
    print()
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print()
    print("0. 退出系统")
    print("=" * 100)


def add_card():
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    phone = input("请输入电话号码：")
    email = input("请输入邮箱地址：")

    info_dic = {}
    info_dic['name'] = name
    info_dic['age'] = age
    info_dic['phone'] = phone
    info_dic['email'] = email

    INFO_LIST.append(info_dic)


def show_card():
    print("*" * 100)
    print("编号\t\t姓名\t\t年龄\t\t电话号码\t\t邮箱地址")
    print("*" * 100)
    for each_info in INFO_LIST:
        print("%d\t\t%s\t\t%s\t\t%s\t\t\t\t%s" % (INFO_LIST.index(each_info) + 1,
                                                  each_info['name'], each_info['age'], each_info['phone'],
                                                  each_info['email']))
    print("*" * 100)


def select_card():
    name = input("输入查找的姓名：")
    for each in INFO_LIST:
        if name == each['name']:
            print("*" * 100)
            print("编号\t\t姓名\t\t年龄\t\t电话号码\t\t\t\t邮箱地址")
            print("*" * 100)
            print("%d\t\t%s\t\t%s\t\t%s\t\t\t\t%s" % (INFO_LIST.index(each) + 1,
                                                      each['name'], each['age'],
                                                      each['phone'],
                                                      each['email']))
            print("*" * 100)
            deal_one_info(each)
            break

    else:
        print("----------------对不起没有找到！----------------")


def deal_one_info(each):
    option = int(input("功能选择【1.修改】【2.删除】【0.返回上一级】"))
    if option == 1:
        each['name'] = input_card_info(each['name'], "请输入姓名【回车不修改】：")
        each['age'] = input_card_info(each['age'], "请输入年龄【回车不修改】：")
        each['phone'] = input_card_info(each['phone'], "请输入电话号码【回车不修改】：")
        each['email'] = input_card_info(each['email'], "请输入邮箱地址【回车不修改】：")
        print("---------修改成功------")
    elif option == 2:
        INFO_LIST.remove(each)
        print("---------删除成功------")


def input_card_info(value, message):
    str_mess = input(message)
    if len(str_mess) > 0:
        return str_mess
    else:
        return value


def main():
    while True:
        main_frame()
        number = int(input("功能选择："))
        if number == 1:
            add_card()
        elif number == 2:
            show_card()
        elif number == 3:
            select_card()
        elif number == 0:
            break


INFO_LIST = []

if __name__ == '__main__':
    main()
