import threading
import time

g_num = 0
def test1(num):
    global g_num

    # 上锁,如果之前没被上锁，那么此时上锁成功
    # 如果上锁之前已经被上锁，那么此时会堵塞在这里，知道这个锁被解开为止
    mutex.acquire()

    for i in range(num):
        g_num += 1

    # 解锁
    mutex.release()

    print("g_num in test1 is %d" % g_num)

def test2(num):
    global g_num
    mutex.acquire()

    for i in range(num):
        g_num += 1

    mutex.release()

    print("g_num in test2 is %d" % g_num)


# 创建一个互斥锁，默认，没有上锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target = test1, args = (1000000,))
    t2 = threading.Thread(target = test2, args = (1000000,))

    t1.start()
    t2.start()
    time.sleep(3)
    print("g_num in Main Thread is %d" % g_num)

    
if __name__ == "__main__":
    main()
