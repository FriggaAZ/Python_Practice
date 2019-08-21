import re


def main():
    mail = input("请输入邮箱：")
    ret = re.match(r"^[A-Z0-9a-z_-]{4,20}@163\.com$", mail)

    if ret:
        print("%s符合要求" % mail)
    else:
        print("%s不符合要求" % mail)


if __name__ == "__main__":
    main()
