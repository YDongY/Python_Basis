from pymysql import *


def main():
    # 创建Connection链接
    conn = connect(host="localhost", port=3306,
                   database="jing_dong", user="root", password="root", charset="utf8")

    # 获得Cursor对象
    cs = conn.cursor()

    count = cs.execute('select * from goods')
    # 打印受影响的行数
    print(count)
    print(cs.fetchall())

    # 增加
    # count2 = cs.execute('insert into goods_cates(name) values ("硬盘")')

    # 更新
    # cs.execute('update goods_cates set name="机械硬盘" where name="硬盘"')

    # 删除
    # cs.execute('delete from goods_cates where name="机械硬盘"')
    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    conn.commit()

    # 关闭Cursor对象
    cs.close()
    # 关闭Connection对象
    conn.close()


if __name__ == '__main__':
    main()
