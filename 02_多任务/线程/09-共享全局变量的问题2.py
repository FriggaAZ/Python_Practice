import threading
import time

g_num = 0
def test1(num):
    for i in range(num):
        global g_num
        g_num += 1
    print("g_num in test1 is %d" % g_num)

def test2(num):
    for i in range(num):
        global g_num
        g_num += 1
    print("g_num in test2 is %d" % g_num)


def main():
    t1 = threading.Thread(target = test1, args = (10000,))
    t2 = threading.Thread(target = test2, args = (10000,))

    t1.start()
    t2.start()
    time.sleep(3)
    print("g_num in Main Thread is %d" % g_num)

    
if __name__ == "__main__":
    main()
