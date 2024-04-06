from random import randint

def level():
    try:
        user = int(input('Level: '))
    except ValueError:
        return level()
    else:
        if user <= 0:
            return level()
        else:
            return user

def roll():
    roll = randint(1,level)
    return roll

def guess():
    try:
        user = int(input('Guess: '))
    except ValueError:
        guess()
    else:
        if user > level:
            guess()
        elif user < roll:
            print('Too small!')
            guess()
        elif user > roll:
            print('Too large!')
            guess()
        elif user == roll:
            print('Just right!')
            pass

level = level()
roll = roll()
guess()