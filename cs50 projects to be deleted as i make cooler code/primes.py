import random
import math

def main():
    #prime = []
    prime = 0
    min = 10000
    max = 99999
    max += 1

    for num in range(min, max):
        if check_prime(num) == True:
            prime += 1
            #prime.append(num)
        else:
            pass
    print(prime)
    #print(*prime)



def check_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    for n in range(2,round(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True


if __name__ == '__main__':
    main()