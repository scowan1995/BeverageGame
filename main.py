from time import sleep as shlep
from random import randint as alan

class Player:
    def __init__(self, name):
        self.name=name


    def getName(self):
        return self.name
capitals = []
    

def capital_round(n, players):
    print("\n\n -------------ROUND %d----------\n %s:\n" %(n, "Random"))
    # import capitals
    with open('capitals.txt', 'r') as f:
        p = f.read().splitlines()
        capitals = [x.split(',') for x in p]

    for player in players:
        print(player.getName() + " YOUR TURN")
        capital = capitals[alan(0, len(capitals)-1)]
        answer = input("What is the capital of " +  capital[0])
        if answer==capital[1]:
            print("Correct! Pick a person to drink!")
        else:
            print("WRONG! Drink!")

def random(n, players):
    print("\n\n -------------ROUND %d----------\n %s:\n" %(n, "Random"))
    i=10
    while i>0:
        print(players[alan(0, len(players) - 1)].getName())
        shlep(1)
        i=i-1


def main():
    num = input("Enter number of players:\n")
    players = []
    num = int(num)
    while num>0:
        name = input("Enter a player name:")
        new_player = Player(name)
        players.append(new_player)
        num=num-1

    rounds = [capital_round, random]
    n=0
    while True:
        curr_round_num=alan(0,len(rounds)-1)
        curr_round=rounds[curr_round_num]
        n=n+1
        curr_round(n,players)


if __name__=="__main__":
    main()




