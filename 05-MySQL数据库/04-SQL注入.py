from pymysql import connect


class JD(object):
    def __init__(self):
        self.conn = connect(host='localhost',
                            port=3306,
                            user='root',
                            password='qq990110',
                            database='jing_dong',
                            charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_data(self):

        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_all_cates(self):

        sql = "select * from goods_cates;"
        self.execute_sql(sql)

    def show_all_brands(self):

        sql = "select * from goods_brands;"
        self.execute_sql(sql)

    def add_new_cate(self):
        cate_name = input("输入商品分类名称：")
        sql = """insert into goods_cates (name) values ("%s")""" % cate_name
        self.cursor.execute(sql)
        self.conn.commit()

    def del_cate(self):
        self.show_all_cates()
        cate_name = input("请输入要删除的类别id:")
        sql = """delete from goods_cates where name='%s' """ % cate_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        find_name = input("请输入要查询的商品名字")
        sql = """select * from goods where name='%s'""" % find_name
        print("--->%s<---" % find_name)
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("1.查询所有数据")
        print("2.查询所有分类")
        print("3.查询所有品牌")
        print("4.添加商品分类")
        print("5.删除商品分类")
        print("6.根据名字查询商品")
        print("x.退出")
        return input("请输入选项")

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == '1':
                self.show_all_data()
            elif choice == '2':
                self.show_all_cates()
            elif choice == '3':
                self.show_all_brands()
            elif choice == '4':
                self.add_new_cate()
            elif choice == '5':
                self.del_cate()
            elif choice == '6':
                self.get_info_by_name()
            elif choice == 'x' or 'X':
                break
            else:
                print("输入内容有误")


def main():
    jd = JD()
    jd.run()


if __name__ == "__main__":
    main()
