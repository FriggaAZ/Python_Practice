import time


def test1():
    while True:
        print("------1------")
        time.sleep(0.1)
        yield


def test2():
    while True:
        print("------2------")
        time.sleep(0.1)
        yield


def main():
    t1 = test1()
    t2 = test2()
    # 先让t1运行一会儿，当t1遇到yield的时候，返回26行，然后执行t2
    # 当遇到yield时，再次切换到t1中
    # 这样t1/t2/t1/t2交替运行，最终实现多任务 --- 协程

    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()
