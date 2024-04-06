import random




def main():
    level = get_level()
    for numbers in range(0,10):
        global tries
        tries = 3
        nums = generate_integer(level)
        add(nums)


def get_level():
    #will ask the user for a num btwn 1 and 3
    try:
        user = int(input('Level: '))
        if user <= 0 or user > 3:
            raise ValueError
        else:
            return user
    #refuse non-int inputs
    except ValueError:
        return get_level()
    #refuse inputs < 0 and > 3


def generate_integer(level):
    #gen 2 nums based on level (num denotes digits)
    if level == 1:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
    if level == 2:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
    if level == 3:
        num1 = random.randint(100,999)
        num2 = random.randint(100,999)
    #returns the randomized digits
    return num1, num2



def add(answer):
    num1, num2 = answer
    #asks user to add both nums and only accepts int inputs
    try:
        #prints question and keeps it on the same line
        print(num1, '+', num2, '= ', end ='')
        user = int(input())
        global num3
        num3 = num1 + num2
        #check if answer is correct
        if user == num3:
            return
        #if its incorrect, reprompts (check make reprompt no more than 3X)
        else:
            check(num3)
            raise ValueError
    except ValueError:
        print('EEE')
        return(add(answer))


'''def check(num3):
    global tries
    #(should subtract 1 each call from 3 until it reaches 0)
    tries = tries - 1
    #(upon 0 should return correct answer)
    if tries == 0:
        correct = num3
        return correct'''

if __name__ == "__main__":
    main()