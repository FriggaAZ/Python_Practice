class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print("parent的init开始调用")
        self.name = name
        print("parent的init调用结束")


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print("Son1的方法开始被调用")
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1的方法调用结束')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print("Son2的init开始被调用")
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print("Son2的init调用结束")


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson的init开始被调用")
        super(Son2,self).__init__(name, age, gender)
        print("Grandson的init结束调用")


gs = Grandson("张三", "12", "Male")
