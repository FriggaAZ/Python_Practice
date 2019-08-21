import threading
import time

g_num = 0

class MyThread1(threading.Thread):
    def run(self):
        global g_num
        # num=100
        # 当num很大就会出问题
        num = 1000000
        for i in range(num):
            g_num += 1
        print("num in test1 g_num = %d" % g_num)


class MyThread2(threading.Thread):
    def run(self):
        global g_num
        # num=100
        num = 1000000
        for i in range(num):
            g_num += 1
        print("num in test2 g_num = %d" % g_num)


def main():
    t1 = MyThread1()
    t2 = MyThread2()

    t1.start()
    t2.start()

    # 等待线程执行完毕
    time.sleep(5)
    
    print("g_num in main thread is %d" % g_num)


if __name__ == "__main__":
    main()
