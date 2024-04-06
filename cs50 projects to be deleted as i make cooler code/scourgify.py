import csv
import sys
num = 0

def check():
    try:
        #sys.exit only takes one argument, so the text and the file are grouped into the exit variable
        exit = "Could not read " + sys.argv[1]
        #this tries to open the file so it's able to raise a FileNotFoundError
        with open(sys.argv[1]):
            pass
        #checks to make sure there is exactly one argument for the file and stops the code otherwise
        if len(sys.argv) > 3:
            sys.exit("Too many command-line argumets")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
            #checks to see if the argument is a CSV file and exits the code otherwise
        elif str(sys.argv[1]).endswith(".csv") == False:
            sys.exit("Not a CSV file")
            #if the file isn't found, the code exits
    except FileNotFoundError:
        sys.exit(exit)

def get():
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        #you cannot understand how important this line is
        #this line makes the code ignore the header so that you can write your own header because headers can't be changed
        #this realization took no less than six hours
        next(reader, None)
        for row in reader:
            #breaks rows into names and house
            name , house = row
            #splits the last and first name into two and assigns the first name to "first" and last name to "last"
            name = name.split(",")
            last, first = name[0], name[-1]
            #removes the leading space from first
            first = first.replace(" ", "")
            #puts first, last, and house function to add
            add(first, last, house)


def add(first ,last, house):
    with open(sys.argv[2], "a") as file:
        #prepares the dictionary and writes the three headers
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        #writes the three headers a single time
        global num
        if num >= 1:
            pass
        else:
            writer.writeheader()
            num = num + 1
        #writes the names and houses for each row
        writer.writerow({"first":first, "last":last, "house":house})
with open(sys.argv[2], "w") as file:
    pass

def main():
    check()
    get()




if __name__ == "__main__":
    main()
