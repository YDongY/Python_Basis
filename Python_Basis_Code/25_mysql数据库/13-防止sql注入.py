from pymysql import *


def main():
    # 创建Connection链接
    conn = connect(host="localhost", port=3306,
                   database="jing_dong", user="root", password="root", charset="utf8")

    # 获得Cursor对象
    cs = conn.cursor()

    # goods_name = input("输入品牌名称：")
    # sql 注入：
    # goods_name = ' or 1=1 or 1 '
    # sql = """select * from goods_brands where name='%s'""" % goods_name
    # print("---->%s<----" % sql)


    # 安全的方式
    params = ["ibm"]
    cs.execute("select * from goods_brands where name=%s",params)
    for temp in cs.fetchall():
        print(temp)

    # 关闭Cursor对象
    cs.close()
    # 关闭Connection对象
    conn.close()


if __name__ == '__main__':
    main()
