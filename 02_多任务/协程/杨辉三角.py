def triangles_1():
    # 层数
    n = 1
    # 上一层列表
    a = []
    while True:
        # 本层列表
        l = []
        for i in range(0, n):
            if i == 0:
                l.insert(i, 1)
            elif i == n - 1:
                l.insert(i, 1)
            else:
                l.insert(i, a[i - 1] + a[i])
        yield l
        a = l
        n = n + 1


# 打印层数控制
n = 0
ret = triangles_1()
for t in ret:
    print(t)
    n = n + 1
    if n == 10:
        break

def triangles_2():
	# 定义最初的数据 1 ，存到列表中
    lt = [1]
    # 进入循环
    while True:
	    # 使用yield语句产生一个生成器，返回当前列表
        yield lt
        # 列表后追加元素 0
        lt.append(0)
        # 列表生成式：原列表中前一项与后一项相加
        lt = [lt[i - 1] + lt[i] for i in range(len(lt))]


n = 0
for i in triangles_2():
    print(i)
    n += 1
    if n == 10:
        break
"""
###代码解析：

在方法中，先定义最初的数据1，存到列表中lt = [1]。
随后进入循环，使用yield语句产生一个生成器，返回列表lt。
此时，代码初次执行到此处，不会再向下执行。
在源代码下部循环中，第二次执行到triangles方法时，会从第一次的断点，也就是yield lt之后开始执行。
此时，在列表后追加一个元素0。
利用列表生成式，将原列表中前一项与后一项相加（其中第一项与最后一项相加），产生一个新列表命名为lt覆盖原列表。
再次进入循环时，代码执行到yield lt语句，将最新的列表返回。
n为循环控制条件。
###语言描述比较抽象，我们逐步分析数据变化。

首先方法的定义，不会执行。将0赋值给n后，直接进入循环，遍历triangles方法返回的生成器对象，此时lt = [1]，triangles方法中的代码执行到yield lt被阻塞，循环中接下来执行print语句打印[1]为第一行，n的值变为1。
再次进入循环，从yield lt后面开始执行，lt.append语句将lt从[1]变为[1, 0]。
列表生成式中，循环次数是len(lt)为2，i初始值为0，所以新列表的第一个值为lt[i - 1] + lt[i]即lt[-1] + lt[0]，为1；接下来i为1，新列表的第二个值为lt[0]+lt[1]，为1。至此列表生成式执行结束，新列表为[1, 1]。for循环中print语句将lt打印，n的值为2，不满足小于10的条件，继续循环。
此时进入循环，同样从yield lt后面开始执行，lt.append语句将lt从[1, 1]变为[1, 1, 0]。
列表生成式中，循环次数是len(lt)为3，i初始值为0，所以新列表的第一个值为lt[i - 1] + lt[i]即lt[-1] + lt[0]，为1；i为1时，新列表的第二个值为lt[0]+lt[1]，为2；i为2，新列表的第二个值为lt[1]+lt[2]，为1。至此列表生成式执行结束，新列表为[1, 2, 1]。for循环中print语句将lt打印，n的值为3，不满足小于10的条件，继续循环。

"""
