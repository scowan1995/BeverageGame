import time
from random import randint

def random(players):
    i=10
    while i>0:
        print(players.get(randint(0, players.size() - 1)).getName())
        time.sleep(1)
        i=i-1

