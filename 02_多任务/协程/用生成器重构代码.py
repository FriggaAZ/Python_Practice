"""
生成器在Python中是一个非常强大的编程结构，可以用更少地中间变量写流式代码，此外，相比其它容器对象它更能节省内存和CPU，当然它可以用更少的代码来实现相似的功能。现在就可以动手重构你的代码了，但凡看到类似：

def something():
    result = []
    for ... in ...:
        result.append(x)
    return result
    
都可以用生成器函数来替换：

def iter_something():
    for ... in ...:
        yield x


"""


def something():
    result = []
    for i in range(10):
        result.append(i)
    return result


odi_some = something()
print(odi_some)


def iter_something():
    for i in range(10):
        yield i


iter_some = iter_something()
result = list()
for x in iter_some:
    result.append(x)
print(result)
