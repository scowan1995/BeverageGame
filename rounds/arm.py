import time

def arm(players):
    print(players.getRandomPlayerName() + " must arm wrestle " + players.getRandomPlayerName())
    time.sleep(10)
    input()
