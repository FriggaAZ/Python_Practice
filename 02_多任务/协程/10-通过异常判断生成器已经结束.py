def create_nums(all_nums):
    current_nums = 0
    a, b = 0, 1
    while current_nums < all_nums:
        yield a
        a, b = b, a + b
        current_nums += 1
    return "OK....."


obj = create_nums(10)
while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break
