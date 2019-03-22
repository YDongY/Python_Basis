from pymysql import *


def select_all(cs):
    cs.execute("select * from goods")
    for temp in cs.fetchall():
        print(temp)

def select_goods_cates(cs):
    cs.execute("select * from goods_cates")
    for temp in cs.fetchall():
        print(temp)

def select_goods_brands(cs):
    cs.execute("select * from goods_brands")
    for temp in cs.fetchall():
        print(temp)

def main():
    # 链接数据库
    conn = connect(host="localhost", port=3306,
                   database="jing_dong", user="root", password="root", charset="utf8")

    # 获得游标对象
    cs = conn.cursor()

    while True:
        print("==================")
        print("1. 查询所有信息")
        print("2. 查询所有商品的分类")
        print("3. 查询所有的品牌分类")
        print("4. 输入0退出")
        print("==================")
        type = int(input("输入查询的选项："))
        if type == 1:
            select_all(cs)
        elif type == 2:
            select_goods_cates(cs)
        elif type == 3:
            select_goods_brands(cs)
        elif type == 0:
            break
        else:
            pass

    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
