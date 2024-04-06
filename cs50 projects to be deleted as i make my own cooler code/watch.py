import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #checks for src= and takes in the youtube url accepting www 1/0 times as well as the s in https
    #used single quotes because doubles are searched for
    src = re.search(r'(src=")(https?:/{2})(www\.)?(youtube.com/)(embed/)(\w{11})"', s)
    try:
        s = src.group(2)+src.group(4)+src.group(6)
        UTUBE_URL = re.sub(r"(https?)", "https", s)
        UTUBE_URL = re.sub(r"(youtube\.com)", "youtu.be", UTUBE_URL)
        return UTUBE_URL
    except AttributeError:
        return None


if __name__ == "__main__":
    main()