import random

teams = int(input("How many teams are needed?\n"))

players = []

def TeamRandomizer():
    with open('Volleyball.txt', 'r') as f:
        
        for line in f:
            players.append(line.replace("\n",""))
        random.shuffle(players)

def TeamGenerator():

    if (teams < 2):
            exit("Invalid Input: Amount of Teams must be greater than or equal to 2")

    elif (teams == 2):
        with open('Volleyball.txt', 'r') as f:
        
            for line in f:
                players.append(line.replace("\n",""))
            random.shuffle(players)
            print(players[0:6],"\n")
            print(players[7:13],"\n")

    elif (teams == 3):
        with open('Volleyball.txt', 'r') as f:
        
            for line in f:
                players.append(line.replace("\n",""))
            random.shuffle(players)
            print(players[0:6],"\n")
            print(players[7:13],"\n")
            print(players[14:20],"\n")

    elif (teams == 4):
        with open('Volleyball.txt', 'r') as f:
            for line in f:
                players.append(line.replace("\n",""))
            random.shuffle(players)
            print(players[0:6],"\n")
            print(players[6:12],"\n")
            print(players[13:19],"\n")
            print(players[19:], "\n")

    elif (teams > 4):
        exit("Invalid Input: Amount of Teams must be less than or equal to 3")

        
TeamGenerator()
print("\nHere is a list of teams:\n")

redo = input("Are you happy with these teams? Enter y or n\n")
if (redo == 'y'):
    print("Have fun!")
else:
    while(redo == 'n'):
        players = []
        TeamGenerator()
        rerun = input("Rerun again? Enter y or n\n")
        if (rerun == 'y'):
            continue
        else:
            print("Have fun!")
            break











