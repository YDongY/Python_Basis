import collections

# python2.6以后可以通过以下方式构造一个没有方法的类

User = collections.namedtuple('User', ['name', 'age', 'gender'])
print(type(User))
user = User('ydy', 18, '男')
print(type(user))
print(user)  # User(name='ydy', age=18, gender='男')
print(user.name)
print(user.age)
print(user.gender)

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    """来自一摞Python风格的纸牌"""
    # 2-A
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 黑桃，方块，梅花，红心
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()
print(len(deck))
for d in deck:
    print(d)
