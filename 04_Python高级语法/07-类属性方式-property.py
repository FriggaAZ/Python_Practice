class Foo(object):
    def __init__(self):
        self.name = "laowang"

    def get_bar(self):
        print("getter...")
        return self.name

    def set_bar(self, value):
        print("setter...")
        self.name = value

    def del_bar(self):
        print("deleter...")
        del self.name

    BAR = property(get_bar, set_bar, del_bar, "This is Description...")

obj = Foo()

obj.BAR
# print(obj.BAR)
obj.BAR = "Alexander"
print(obj.BAR)
desc = Foo.BAR.__doc__
print(desc)
