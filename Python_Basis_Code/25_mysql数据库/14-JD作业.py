from pymysql import *
import time


class JD(object):
    def __init__(self):
        self.conn = connect(host="localhost", port=3306,
                            database="jing_dong", user="root", password="root", charset="utf8")
        self.cs = self.conn.cursor()
        self.user = list()

    def __del__(self):
        self.cs.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cs.execute(sql)
        for temp in self.cs.fetchall():
            print(temp)

    # 查询所有信息
    def get_all_goods(self):
        sql = "select * from goods;"
        self.execute_sql(sql)

    # 查询所有商品的分类
    def get_goods_cates(self):
        sql = "select * from goods_cates;"
        self.execute_sql(sql)

    # 查询所有的品牌分类
    def get_goods_brands(self):
        sql = "select * from goods_brands;"
        self.execute_sql(sql)

    # 添加一个商品分类
    def add_brand(self):
        name = input("输入添加的分类名称：")
        sql = "insert into goods_cates (name) values ('%s')" % name
        self.cs.execute(sql)
        self.conn.commit()

    # 根据名字查询一个商品
    def get_info_by_name(self):
        find_name = input("输入查询的名称：")
        sql = "select * from goods where name=%s"
        ret = self.cs.execute(sql, [find_name])
        if ret:
            for temp in self.cs.fetchall():
                print(temp)
        else:
            print("抱歉！没找到。。。")

    # 添加订单
    def add_orders(self):
        # 通过名字获取用户id
        sql = "select id from customers where name = %s"
        self.cs.execute(sql, [self.user[0]])
        customer_id = self.cs.fetchone()[0]
        # 获取当前时间
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 添加到订单表
        self.cs.execute("insert into orders values(0,%s,%s) ;", [now_time, customer_id])
        self.conn.commit()
        # 获得订单id
        self.cs.execute("select id from orders where order_date_time = %s", [now_time])
        order_id = self.cs.fetchone()[0]
        return order_id

    # 添加详细订单
    def add_order_detail(self, order_id, good_id, good_num):
        # 添加到订单详情表
        self.cs.execute("insert into order_detail values (0,%s,%s,%s)", [order_id, good_id, good_num])
        self.conn.commit()

    # 显示订单信息
    def show_orders_info(self):
        self.cs.execute(
            "select order_detail.*,orders.order_date_time,orders.customer_id from order_detail inner join orders on order_detail.order_id=orders.id;")
        for temp in self.cs.fetchall():
            print(temp)

    # 下单
    def order_goods(self):
        while True:
            print("======下单=======")
            print("1. 查询所有信息")
            print("2. 选择购买的商品编号：")
            print("0. 0返回上一级")
            print("================")
            num = int(input("输入选择项:"))
            if num == 1:
                self.get_all_goods()
            elif num == 2:
                good_id = int(input("输入商品编号："))
                good_num = int(input("输入商品数量："))
                # sql = "select * from goods where id=%s;"
                # self.cs.execute(sql, [good_id])
                order_id = self.add_orders()
                self.add_order_detail(order_id, good_id, good_num)
            elif num == 0:
                break

    # 校验用户信息
    def check_info(self, username, password):
        sql = "select passwd from customers where name=%s"
        self.cs.execute(sql, [username])
        try:
            pwd = self.cs.fetchone()[0]
            if pwd == password:
                print("登录成功")
                self.user.append(username)
                return "登录成功"
            else:
                print("登录失败")
                return "登录失败"
        except TypeError:
            print("用户未注册")
            return "用户未注册"

    # 注册用户
    def add_user(self, username, address, tel, password):
        sql = "insert into customers values (0,%s,%s,%s,%s)"
        self.cs.execute(sql, [username, address, tel, password])
        self.conn.commit()

    @staticmethod
    def show_menu():
        print("==================")
        print("1. 查询所有信息")
        print("2. 查询所有商品的分类")
        print("3. 查询所有的品牌分类")
        print("4. 添加一个商品分类")
        print("5. 根据名字查询一个商品")
        print("6. 下单")
        print("7. 查询订单信息")
        print("   输入0退出       ")
        print("==================")
        return int(input("输入对应的编号："))

    # 显示登陆界面
    def show_load_menu(self):
        print("----------请登录JD网！！！-------------")
        username = input("输入用户名：")
        password = int(input("输入密码："))
        ret = self.check_info(username, password)
        return ret

    # 显示添加用户界面
    def show_add_user_menu(self):
        print("------------注册界面----------")
        username = input("输入用户名：")
        address = input("输入地址：")
        tel = int(input("输入电话号码："))
        password = int(input("输入密码："))
        self.add_user(username, address, tel, password)

    def main(self):
        while True:
            num = self.show_menu()
            if num == 1:
                self.get_all_goods()
            elif num == 2:
                self.get_goods_cates()
            elif num == 3:
                self.get_goods_brands()
            elif num == 4:
                self.add_brand()
            elif num == 5:
                self.get_info_by_name()
            elif num == 6:
                self.order_goods()
            elif num == 7:
                self.show_orders_info()
            elif num == 0:
                break

    def run(self):
        while True:
            ret = self.show_load_menu()
            if ret == "登录成功":
                self.main()
            elif ret == "用户未注册":
                self.show_add_user_menu()
            elif ret == "登录失败":
                pass


def main():
    # 创建对象
    jd = JD()
    # 启动
    jd.run()

    del jd


if __name__ == '__main__':
    main()
