import numbers


class Cards:
    # 不可变序列 支持切片操作,重写特定的魔法函数
    def __init__(self, card):
        self.card = card

    def __reversed__(self):
        self.card.reverse()

    def __getitem__(self, item):
        # item为slice对象
        cls = type(self)
        # 切片的关键函数，是吧当前对象的切片作用到list
        if isinstance(item, slice):
            return cls(card=self.card[item])
        elif isinstance(item, numbers.Integral):
            return cls(card=[self.card[item]])

    def __len__(self):
        return len(self.card)

    def __iter__(self):
        return iter(self.card)

    def __contains__(self, item):
        if item in self.card:
            return True
        else:
            return False


# 实现的切片类似于Django的queryset，切片完成仍然是一个对象
card = Cards([i for i in range(10)])
print(card[:2])
print(card[0])
print(len(card))  # 对应len
if 0 in card:  # 对应__contains__
    print("yes")
reversed(card)  # 对应__reversed__
for c in card:
    print(c)
