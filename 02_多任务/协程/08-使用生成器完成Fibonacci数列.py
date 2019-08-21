def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print(a)
        a, b = b, a + b
        current_num += 1


def create_num_generator(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        yield a  # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器模板,和类一样
        a, b = b, a + b
        current_num += 1
    return "OK..."

# create_num(10)

# 如果在调用函数的时候发现有yield，那么此时不是调用函数而是创建一个生成器对象

# obj = create_num_generator(10)
# for num in obj: # 把yield后面的值（a）返回给num，下一次从上一次停止的位置继续执行，而不会执行完整个函数
#     print(num)

# obj = create_num_generator(10)
# while True:
#     try:
#         ret = next(obj)
#         print(ret)

#     except Exception as ret:
#         print(ret.value)
#         break

obj = create_num_generator(10)
ret = next(obj)
print(ret)

ret = next(obj)
print(ret)
