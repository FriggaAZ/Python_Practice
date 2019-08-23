# 1. 检查登录
## 1.1 登录错误：输出错误
## 1.2 登陆成功：进入系统

# 2. 选择操作：

from ProtectSQLInJect import JD


class Login(JD):
    def execute_sql(self, sql):
        self.cursor.execute(sql)

    def login_judge(self):
        user_id = input("输入手机号码：")
        user_passwd = input("输入密码：")

        try:
            sql_id = """select tel from customers where tel='%s'""" % user_id
            sql_passwd = """select passwd from customers where passwd='%s'""" % user_passwd
            self.execute_sql(sql_id)
            self.execute_sql(sql_passwd)
        except Exception as e:
            print(e)
            print("出现错误")
            return False
        else:
            print("登录成功")
            return True


def main():
    log = Login()
    if log.login_judge():
        jd = JD()
        jd.run()


if __name__ == "__main__":
    main()
