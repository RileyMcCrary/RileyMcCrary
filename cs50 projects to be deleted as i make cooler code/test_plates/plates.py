def main():
    plate = is_valid(input('Plate: '))
    if plate == True:
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):

    #this checks if the length of the input is acceptable
    if len(s) < 2 or len(s) > 6:
        return False


#this makes sure the input doesn't start with two numbers
    if s[0].isnumeric() == True or s[1].isnumeric() == True:
        return False



#this checks if therer are any non-alphanumeric characters in the input
    if s.isalnum() == False:
        return False

#checks if 0 is 1st num to appear
    for n in range(2,len(s) +1):
        try:
            if s[n] == '0'and s[n-1].isnumeric() == False:
                return False
                break
        except IndexError:
            pass
        else:
            pass

    for n in range(2,len(s)+1):
        try:
            if s[n].isnumeric() and s[n+1].isalpha() == True:
                return False
        except IndexError:
            pass
        else:
            pass


    else:
        return True


if __name__ == '__main__':
    main()