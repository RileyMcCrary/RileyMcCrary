import csv
from tabulate import tabulate
import sys

def check():
    try:
        #checks to make sure there is exactly one argument for the file and stops the code otherwise
        if len(sys.argv) > 2:
            sys.exit("Too many command-line argumets")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
            #checks to see if the argument is a CSV file and exits the code otherwise
        elif str(sys.argv[1]).endswith(".csv") == False:
            sys.exit("Not a CSV file")
            #if the file isn't found, the code exits
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    check()
    with open(sys.argv[1], newline="") as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))




if __name__ == "__main__":
    main()
