import time

def arm(players):
    p1 = players.getRandomPlayerName()
    p2 = p1
    while p1 == p2:
        p2 = players.getRandomPlayerName()
    print(p1 + " must arm wrestle " + p2)
    time.sleep(10)
    input()
