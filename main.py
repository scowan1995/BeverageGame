import time
from random import randint as alan
from classes import Player, Players
import rounds.capitals as r
import rounds.random as ran
import rounds.arm as arm
from inspect import getmembers, isfunction
import os
import sys


DEBUG = len(sys.argv)>1 and sys.argv[1] == 'debug'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def mprint(s):
    height, width = os.popen('stty size', 'r').read().split()
    
    n_chars = int((int(width)-len(s))/2)

    for i in range(0,n_chars):
        s = ' ' + s + ' '
    
    print(s)
    return

def main():
    
    
    num = input("Enter number of players:\n")
    players = Players()
    num = int(num)
    while num>0:
        name = input("Enter a player name:")
        new_player = Player(name)
        players.addPlayer(new_player)
        num=num-1
   
    n=0
    rounds=[
        (r.capital_round, "Capitals"),
        (ran.random, "Random"),
        (arm.arm, "Arm Wrestle")
    ]
    
    #for item in things:
    #    funcs = [rd for rd in getmembers(things) if isfunction(rd[1])]
    #    for thing in funcs:
    #        rounds.append(thing)
    #for roun in rounds:
    #    print(roun)
    #n=0
    while True:
        curr_round_num=alan(0,len(rounds)-1)
        curr_round=rounds[curr_round_num]
        n=n+1
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        x=20
        y=20
        text='[Press Enter to Continue]'
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()
        s = "-------Round 3-------"
        mprint(s)
        time.sleep(1)
        mprint("------------ %s ------------" %curr_round[1])
        print("\n")
        time.sleep(1)
        curr_round[0](players)


if __name__=="__main__":
    main()




