import multiprocessing

def deadLoop1():
    while True:
        pass

def deadLoop2():
    while True:
        pass

def deadLoop3():
    while True:
        pass

# 子进程死循环
p1 = multiprocessing.Process(target=deadLoop1)
p2 = multiprocessing.Process(target=deadLoop2)
p3 = multiprocessing.Process(target=deadLoop3)
p1.start()
p2.start()
p3.start()

# 主进程死循环
while True:
    pass
