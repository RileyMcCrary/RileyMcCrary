import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = " "+s+" "
    um_pattern = re.compile(r"\Wum\W", re.I)
    um_num = re.findall(um_pattern, s)
    um_num = len(um_num)
    return um_num




if __name__ == "__main__":
    main()