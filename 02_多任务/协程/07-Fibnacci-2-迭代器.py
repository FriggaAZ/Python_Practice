class Fibonacci(object):
    def __init__(self, all_nums):
        self.all_nums = all_nums
        self.names = list()
        self.current_num = 0
        self.a = 0
        self.b = 1

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_nums:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibo = Fibonacci(100)

for num in fibo:
    print(num)
