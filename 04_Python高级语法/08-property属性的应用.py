class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("Error: 不是整数")

    money = property(getMoney, setMoney)

a = Money()

print(a.money)
a.money = 1000000000000
print(a.money)
