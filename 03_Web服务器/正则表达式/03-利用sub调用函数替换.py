import re


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


def main():
    ret = re.sub(r"\d+", add, "python = 998")
    print(ret)

    ret = re.sub(r"\d+", add, "C = 99")
    print(ret)

if __name__ == "__main__":
    main()
