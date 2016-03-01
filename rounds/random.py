import time
from random import randint
import classes
from classes import bcolors as b
def random(players):
    i=10
    while i>0:
        
        print(players.get(randint(0, players.size() - 1)).getName() + " drink!\n")
        time.sleep(1)
        i=i-1

