import time
import gevent
from gevent import monkey

monkey.patch_all()  # 将程序中用到的耗时操作的代码替换为gevent中自己实现的模块


def corroutine_work(continue_name):
    for i in range(10):
        print(continue_name, i)
        time.sleep(0.3)


gevent.joinall([
    gevent.spawn(corroutine_work, "work1"),
    gevent.spawn(corroutine_work, "work2")
])
