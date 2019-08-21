from greenlet import greenlet
import time


# greenlet是直接在函数中切换，一个连一个，yield需要自己在while里面手动写

def test1():
    while True:
        print("-----A-----")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("-----B-----")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
