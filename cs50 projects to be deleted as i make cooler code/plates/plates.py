def main():
    plate = is_valid(input('Plate: '))
    print(plate)


def is_valid(s):

    #this checks if the length of the input is acceptable
    if len(s) < 2 or len(s) > 6:
        return 'Invalid'


#this makes sure the input doesn't start with two numbers
    if s[0].isnumeric and s[1].isnumeric() == True:
        return 'Invalid'



#this checks if therer are any non-alphanumeric characters in the input
    if s.isalnum() == False:
        return 'Invalid'

#checks if 0 is 1st num to appear
    for n in range(2,len(s) +1):
        try:
            if s[n] == '0'and s[n-1].isnumeric() == False:
                return 'Invalid'
                break
        except IndexError:
            pass
        else:
            pass

    for n in range(2,len(s)+1):
        try:
            if s[n].isnumeric() and s[n+1].isalpha() == True:
                return 'Invalid'
        except IndexError:
            pass
        else:
            pass


    else:
        return 'Valid'


    #for char in is_valid:




if __name__ == '__main__':
    main()