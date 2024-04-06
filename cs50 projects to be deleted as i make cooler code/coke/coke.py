amount_due = 50

def left(amount_due):
    if amount_due <= 0:
        change =  - amount_due
        print("Change Owed:", change)
    else:
        print("Amount Due:", amount_due)

while amount_due > 0:
    coins = int(input("Insert coin: "))
    if coins == 5 or coins == 10 or coins == 25:
        amount_due = amount_due - coins
        left(amount_due)
    else:
        print("Amount Due:", amount_due)
x = 5