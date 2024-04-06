menu = {
      "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    tab = 0
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            print("\n")
            break
        else:
            #I wanted all of this to be in bill, but tab doesn't make its way into the function properly (local vs global variables)
            price = bill(item)
            if bill(item) == False:
                pass
            else:
                total = price + tab
                tab = total
                total = format(total, ".2f")

                print("Total: " ,"$", total, sep="")


def bill(item):
    try:
        cost = menu[item]
    except KeyError:
        return False
    else:
        return cost





main()
