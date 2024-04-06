import random
import math
import sys
import inflect
p = inflect.engine()

#these set the upper and lower bound of acceptable values
MAX = 99991
MIN = 10007

#this allows the code to change with edits a bit better, but if you're operating on more than one order of magnitude at once I can't help you
LEN_NUM = len(str(MAX))
LEN_WORD = p.number_to_words(len(str(MAX)))

#this sets the number of entered primes before game over
TRIES = 5

#sets the number of non-primes you need to enter before it starts giving sequential primes above and below the entered number
HELP_0 = 3


counter = 0
non_prime_count = 0

def main():
    answer: int = get_prime()
    while True:
        user: int = get_user()
        colors = compare(answer, user)
        output(colors)

def get_user() -> int:
    try:
        user = int(input(f'Please input a {LEN_WORD}-digit prime number: '))
        test = check_prime(user)
        if test == False:
            print(f'Not a {LEN_WORD}-digit prime!\n')
            next_prime(user)


            return get_user()
        else:
            return user
    except ValueError:
        print('Please use numbers!\n')
        return get_user()
    except KeyboardInterrupt:
        sys.exit('\n Game Exited')

def check_prime(num: int) -> bool:
    if num < MIN or num > MAX:
        return False
    for n in range(2,round(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True

#this uses check_prime to spit out the closest prime number (increasing) if a non-prime is entered HELP_0 times
def next_prime(user: int): #prints from here, it was just easier, fix later
    global non_prime_count
    non_prime_count += 1
    if non_prime_count > HELP_0:
        if str(user).isdigit() == True:
            #this was added so that the calculation is shorter for massive numbers
            #before this if you typed in 15 sextillion, it'd crunch numbers until it was in range (10007-99991) though honestly one would deserve to wait
            #numbers changed to MAX and MIN for easier updating in the future
            if user > MAX + 1:
                user = MAX + 1
            if user < MIN - 1:
                user = MIN - 1

            for num in range(user, MAX):
                if check_prime(num) == True:
                    print(f'Next sequential prime is {num}\n')
                    break
                else:
                    pass

            for num in reversed(range(MIN, user)):
                if check_prime(num) == True:
                    print(f'Previous sequential prime is {num}\n')
                    break
                else:
                    pass
    else:
        pass

def get_prime() -> int:
    answer = random.randint(MIN,MAX)
    if check_prime(answer) == True:
        for digit in str(answer):
            if str(answer).count(digit) <= 2:
                return answer
            else:
                return get_prime()
    else:
        return get_prime()

def compare(answer: int, user: int) -> str:
    answer = str(answer)
    user = str(user)
    global answer_list
    global user_list
    answer_list = []
    user_list = []
    for digit in answer:
        answer_list.append(digit)
    for digit in user:
        user_list.append(digit)

    answer_enum = list(enumerate(answer_list))
    user_enum = list(enumerate(user_list))

    global colors
    colors = []
    for n in range(0,len(answer_list)):

        x, y = answer_enum[n]
        a, b = user_enum[n]



        if x == a and y == b:
            colors.append('🟩')
        elif b in answer_list:
            colors.append('🟨')
        else:
            colors.append('⬜')

    for n in range(0,len(answer_enum)):
        a, b = user_enum[n]
        if b in answer_list and user_list.count(b) > answer_list.count(b):
                #if it does, this should change the second instance of the value to a white unless it is in the right place
                user_list.reverse()
                colors.reverse()

                if colors[user_list.index(b)] != "🟩":
                    colors[user_list.index(b)] = "⬜"
                    #should reverse the list again, returning it to original state
                    user_list.reverse()
                    colors.reverse()
                else:
                    user_list.reverse()
                    colors.reverse()
                    colors[user_list.index(b)] = "⬜"
        else:
            return colors

def output(colors: str) -> str:
    global counter
    global user_list
    global answer_list
    if '🟨' not in colors and '⬜' not in colors:
        if counter + 1 == 1:
            print(f'ANSWERED IN {counter + 1} TRY!!!')
        else:
            print(f'Answered in {counter} tries!')
        for n in range(0, len(colors)):
            print(user_list[n], colors[n])
        sys.exit('You Win!!!')
    counter += 1
    if counter > TRIES:
        print('Answer:', sep='')
        print(*answer_list)
        sys.exit('Game Over')
    else:
        for n in range(0, len(colors)):
            print(user_list[n], colors[n])
        return True











if __name__ == '__main__':
    main()