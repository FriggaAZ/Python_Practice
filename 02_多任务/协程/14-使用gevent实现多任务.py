import gevent
from gevent import monkey
import time

# gevent的特点是遇到了延时gevent.sleep()就立刻切换，没有遇到延时，就不切换
# 协程消耗的资源非常少，效率比较高
# from gevent import monkey，写上monkey.patch_all()打上补丁可以实现保留原来的
# 延时操作(例如time.sleep(1), recv_from())，而实现并发

monkey.patch_all()


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.3)
        # gevent.sleep(0.3)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.3)
        # gevent.sleep(0.3)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.3)
        # gevent.sleep(0.3)


# print("-----1-----")
# g1 = gevent.spawn(f1, 5)
# print("-----2-----")
# g2 = gevent.spawn(f2, 5)
# print("-----3-----")
# g3 = gevent.spawn(f3, 5)
# print("-----4-----")

# 一个一个写太麻烦了
# g1.join()  # 等待g1执行完，在等待g1的时候，就运行其他对象，gevent会自动切换。
# g2.join()
# g3.join()

# 可以使用joinall
gevent.joinall([
    gevent.spawn(f1, 5),
    gevent.spawn(f2, 5),
    gevent.spawn(f3, 5),
])
