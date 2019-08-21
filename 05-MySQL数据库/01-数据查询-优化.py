from pymysql import connect


class JD(object):
    def __init__(self):
        pass

    def show_all_data(self):
        conn = connect(host='localhost',
                       port=3306,
                       user='root',
                       password='qq990110',
                       database='jing_dong',
                       charset='utf8')
        cursor = conn.cursor()
        sql = "select * from goods"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        cursor.close()
        conn.close()

    def show_all_cates(self):
        conn = connect(host='localhost',
                       port=3306,
                       user='root',
                       password='qq990110',
                       database='jing_dong',
                       charset='utf8')
        cursor = conn.cursor()
        sql = "select * from goods_cates"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        cursor.close()
        conn.close()

    def show_all_brands(self):
        conn = connect(host='localhost',
                       port=3306,
                       user='root',
                       password='qq990110',
                       database='jing_dong',
                       charset='utf8')
        cursor = conn.cursor()
        sql = "select * from goods_brands"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        cursor.close()
        conn.close()

    def run(self):
        while True:
            print("1.查询所有数据")
            print("2.查询所有分类")
            print("3.查询所有品牌")
            print("4.退出")
            choice = int(input("请输入选项"))

            if choice == 1:
                self.show_all_data()
            elif choice == 2:
                self.show_all_cates()
            elif choice == 3:
                self.show_all_brands()
            elif choice == 4:
                break
            else:
                print("输入内容有误")


def main():
    jd = JD()
    jd.run()


if __name__ == "__main__":
    main()
