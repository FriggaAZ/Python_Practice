from multiprocessing import Queue
q = Queue(3)
q.put("111")
q.put(222)
q.put([11, 22, 33])

for i in range(3):
    print(q.get())

print(q.empty())
