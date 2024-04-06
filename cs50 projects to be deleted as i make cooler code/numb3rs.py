import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
   if ad := re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        max = 255
        num1, num2, num3, num4 = int(ad.group(1)), int(ad.group(2)), int(ad.group(3)), int(ad.group(4))
        if num1 <= max and num2 <= max and num3 <= max and num4 <= max:
            return True
        else:
            return False

   else:
       return False




if __name__ == "__main__":
    main()