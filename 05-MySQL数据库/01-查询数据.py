# 1. 查询所有数据
# 2. 查询所有分类
# 3. 查询所有品牌
from pymysql import *


conn = connect(host='localhost',
                port=3306,
                user='root',
                password='qq990110',
                database='jing_dong',
                charset='utf8')
cs = conn.cursor()


def show_all_data():
    datas = cs.execute('select * from goods;')
    print(cs.fetchall())


def show_all_cates():
    cates = cs.execute('select * from goods_cates')
    print(cs.fetchall())


def show_all_brands():
    brands = cs.execute('select * from goods_brands')
    print(cs.fetchall())


def main():
    while True:
        print("1.查询所有数据")
        print("2.查询所有分类")
        print("3.查询所有品牌")
        print("4.退出")
        choice = int(input("请输入选项"))

        if choice == 1:
            show_all_data()
        elif choice == 2:
            show_all_cates()
        elif choice == 3:
            show_all_brands()
        elif choice == 4:
            break
        else:
            print("输入内容有误")    


if __name__ == "__main__":
    main()
