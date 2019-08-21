from pymysql import *


def main():
    conn = connect(host='localhost',
                   port=3306,
                   user='root',
                   password='qq990110',
                   database='jing_dong',
                   charset='utf8')

    cs1 = conn.cursor()

    # count = cs1.execute('insert into goods_cates(name) values ("硬盘")')
    count = cs1.execute('select * from goods_cates')
    # print(count.fetch())7

    print(cs1.fetchall())

    # count = cs1.execute('insert into goods_cates(name) values ("光盘")')
    # print(count)

    conn.commit()
    cs1.close()
    conn.close()

if __name__ == "__main__":
    main()
