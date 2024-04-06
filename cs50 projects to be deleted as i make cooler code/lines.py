import sys


def check():
    try:
        #checks to make sure there is exactly one argument for the file and stops the code otherwise
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
            #checks to see if the argument is a python file (code) and exits the code otherwise
        elif str(sys.argv[1]).endswith(".py") == False:
            sys.exit("Not a Python file")
            #if the file isn't found, the code exits
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    check()
    num = 0
    try:
        with open(sys.argv[1], "r") as file:
            #it seems to treat file as a list once readlines is used
            file = file.readlines()
            #iterates through items in file one by one
            for line in file:
                #remove leading and trailing spaces
                line = line.strip()
                #ignores commented code
                if line.startswith("#") == True:
                    pass
                #ignores completely empty lines or strings of all whitespace
                elif len(line) == 0 or line.isspace() == True:
                    pass
                else:
                    #add 1 if the code is meaningful
                    num = num + 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


    #prints the number given after going through every line in the file
    print(num)










if __name__ == "__main__":
    main()