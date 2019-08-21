def create_num_generator(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print(">>>ret>>>", ret)
        a, b = b, a + b
        current_num += 1

obj = create_num_generator(10)

# 不能传参数
ret = next(obj)
print(ret)

# 可以传参数
ret = obj.send("hi")
print(ret)
