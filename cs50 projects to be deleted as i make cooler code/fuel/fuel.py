def main():
    while True:
        ask = input("Fraction: ")
#so I can't just use if ask == False. I need to redefine the returned value
        ask = fraction(ask)
#any of the no-no's return false and continue the loop
        if ask == False:
            pass
#if a value that works is entered, it does it's job and stops looping
        else:
            break

def fraction(prompt):
#splits the input by the division slash and defines the numer x and denom y
    (x,y) = prompt.split("/")
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
                empty_check(percent)

def empty_check(percent):
    percent = round(percent)
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(percent, "%", sep="")



main()

