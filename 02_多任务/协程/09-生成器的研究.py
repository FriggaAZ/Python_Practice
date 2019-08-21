def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    
    while current_num < all_num:
        print(a)
        a, b = b, a + b
        current_num += 1


def create_num_generator(all_num):
    print("------1-----")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("------2-----")
        
        # print(a)
        yield a  # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器模板,和类一样
        print("------3-----")
        a, b = b, a + b
        current_num += 1
        print("------4-----")



obj = create_num_generator(10)
obj2 = create_num_generator(2)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj2)
print("obj2:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)
