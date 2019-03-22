class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地面积：%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f\n剩余面积：%.2f\n家具列表：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        if item.area > self.free_area:
            print("%s 面积太大，无法添加" % item.name)
            return
        self.item_list.append(item.name)
        self.free_area = self.free_area - item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

house = House("两室一厅", 7)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
# print(bed)
# print(chest)
# print(table)
