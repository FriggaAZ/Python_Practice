import threading
import time

num = 100


def test1():
    global num
    num += 1
    print("num in testi %d" % num)

def test2():
    print("num in test2 %d" % num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()



