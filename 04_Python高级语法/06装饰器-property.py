class Goods(object):
    def __init__(self):
        # 原价：
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        # 改变原价
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


# ipython
obj = Goods()
obj.price
obj.price = 200
del obj.price
