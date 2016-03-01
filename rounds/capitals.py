from random import randint as alan

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def capital_round(players):
    # import capitals
    with open('capitals.txt', 'r') as f:
        p = f.read().splitlines()
        capitals = [x.split(',') for x in p]

    for player in players:
        print(player.getName() + " YOUR TURN")
        capital = capitals[alan(0, len(capitals)-1)]
        answer = input("What is the capital of " +  capital[0] + "\n")
        if answer.lower()==capital[1].lower():
            print(bcolors.OKGREEN + "Correct! Pick a person to drink!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "WRONG! Drink! The answer is: " + bcolors.ENDC  + capital[1])

