import sys
from PIL import Image
from PIL import ImageOps

def check():
    try:
        #checks if the extension names are the same case-insensitively
        _ , extension = sys.argv[1].lower().split(".")
        _ , extension2 = sys.argv[2].lower().split(".")
        if extension != extension2:
            sys.exit("Input and output have different extensions")
        else:
            pass
        #this tries to open the file so it's able to raise a FileNotFoundError
        with open(sys.argv[1]):
            pass
        #checks to make sure there is exactly one argument for the file and stops the code otherwise
        if len(sys.argv) > 3:
            sys.exit("Too many command-line argumets")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
            #checks to see if the argument is a jpg, jpeg, or png and exits otherwise
        if extensio2n == "jpg" or extension == "jpeg" or extension == "png":
            pass
        else:
            sys.exit("Invalid output")
            #if the file isn't found, the code exits
    except FileNotFoundError:
        sys.exit("Input does not exist")

def main():
    with Image.open("shirt.png") as shirt:
        size = shirt.size
        with Image.open(sys.argv[1]) as input:
            input = ImageOps.fit(input, size)
            #the first shirt is what pastes to image, the second is the mask, which makes it transparent. mask=shirt would have also worked
            input.paste(shirt, shirt)
            input.save(sys.argv[2])










if __name__ == "__main__":
    main()