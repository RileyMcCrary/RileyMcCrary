def main(enter):
    enter = stand(enter)
#These check if the input times fall within the schedule
    if 7 <= enter <= 8:
        print("breakfast time")
    if 12 <= enter <= 13:
        print("lunch time")
    if 18 <= enter <= 19:
        print("dinner time")

def convert(time):
#splits the hours and minutes at the colon
    time = hrs, mins = time.split(":")
#converts the minutes to float then a decimal
    mins = float(mins)
    mins = mins / 60
#coverts hours to an integer and adds them to make a float
    hrs = int(hrs)
    val = hrs + mins
    return val

def stand(insert):
#This should standardizes
    insert = insert.strip().lower()
    insert = swap(insert)
#This takes the am off and convert it to float to be handled by main
    if insert.endswith("a.m.") == True:
        insert = insert.replace("a.m."," ")
        insert = convert(insert)
        return insert
#This takes the pm off, converts it, and adds 12 to the float
    if insert.endswith("p.m.") == True:
        insert = insert.replace("p.m.", " ")
        insert = convert(insert)
        insert = insert + 12
        return insert
    else:
        insert = convert(insert)
        return insert
#Since 12 am in 24 hour is 24, this swaps midnight and noon
def swap(noonight):
    if noonight.startswith("12") and noonight.endswith("a.m."):
        noonight = noonight.replace("a.m.", "p.m.")
        return noonight
    if noonight.startswith("12") and noonight.endswith("p.m."):
        noonight = noonight.replace("p.m.", "a.m.")
        return noonight
    else:
        return noonight

main(input("Please enter the time: "))
        