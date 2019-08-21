import re


def main():
    names = [
        "name1", "_name", "2_name", "__name__", "name_1_", "name!!", "name#123", "______"
    ]
    for name in names:
        # ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name)
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)

        if ret:
            print("变量名：%s 符合要求" % name)
        else:
            print("变量名：%s 不符合要求" % name)


if __name__ == "__main__":
    main()
