def main():
    while True:
        user = input("Fraction: ")
#so I can't just use if ask == False. I need to redefine the returned value
        ask = convert(user)
#any of the no-no's return false and continue the loop
        if ask == False:
            pass
#if a value that works is entered, it does it's job and stops looping
        else:
            print(ask)
            break

def convert(fraction):
#splits the input by the division slash and defines the numer x and denom y
    try:
        (x,y) = fraction.split("/")
    except ValueError:
        return False
#it tries to set them as integers and if it fails returns False
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return False
    else:
#this is a fuel gauge so you can't have <100% fuel
        if x > y:
            return False
        else:
            try:
                percent = (x/y) * 100
#if you divide by zero, it returns False
            except ZeroDivisionError:
                return False
            else:
                return gauge(percent)

def gauge(percentage):
    percentage = round(percentage)
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return str(str(percentage) + '%')


if __name__ == '__main__':
    main()

