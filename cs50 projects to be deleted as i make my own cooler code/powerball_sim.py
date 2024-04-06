import random

play = []
lot= []





#There seem to be no repeats of the same number in one draw (two 7s in the lucky numbers)
#there are no more than one of every number
def lottery():
    for numbers in range(0,6):
        #Rolls a random number six times
        roll = random.randint(1,59)
        #adds the rolled nums to the lot list
        while roll in lot:
            roll = random.randint(1,59)
        lot.append(roll)
        #This puts the numbers in least to greatest
        lot.sort()
    return(lot)



def player():
    #This is the same for player
    for numbers in range(0,6):
        roll = random.randint(1,59)
        while roll in play:
            roll = random.randint(1,59)
        play.append(roll)
        play.sort()
    return(play)

tickets = 0

for numbers in range(0,100000000):
    lottery()
    player()
    tickets = tickets + 1
    if lot == play:
        print(lot)
        print(play)
        print('Win')
        print('Victory after', tickets, 'spins')
        break
    else:
        lot.clear()
        play.clear()