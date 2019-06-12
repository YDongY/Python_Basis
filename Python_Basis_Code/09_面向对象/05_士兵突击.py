class Gun(object):
    def __init__(self, type):
        self.type = type
        self.bullet = 0

    def add_bullet(self, count):
        self.bullet = count

    def shoot(self):
        # 1. 开枪前判断有没有子弹
        if self.bullet <= 0:
            print("枪没有子弹！")
            return
        self.bullet -= 1
        print("突突突。。。【剩余子弹：%d】" % self.bullet)


class Solider(object):
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fair(self):
        # 1. 判断有没有枪
        if self.gun is None:
            print("%s 没有枪" % self.name)
            return
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("AK47")

xusanduo = Solider("许三多")
xusanduo.gun = ak47

xusanduo.fair()
