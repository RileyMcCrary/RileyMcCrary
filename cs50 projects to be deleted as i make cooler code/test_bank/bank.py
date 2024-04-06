def main():
    enter = value(input(''))
    print('$',enter,sep='')


def value(greeting):
    greeting = greeting.strip()
    greeting = greeting.lower()

    if greeting.startswith("hello") == True:
        amount = 0
        return amount
    elif greeting.startswith("h") == True:
        amount = 20
        return amount
    else:
        amount = 100
        return amount


if __name__ == '__main__':
    main()