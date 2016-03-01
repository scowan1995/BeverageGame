import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Players:

    def __init__(self):
        self.players = []
    
    def addPlayer(self,player):
        self.players.append(player)

    def getRandomPlayerName(self):
        player = self.players[random.randint(0,len(self.players)-1)]
        return player.getName()
    
    def get(self,n):
        return self.players[n]

    def __iter__(self):
        return iter(self.players)

    def size(self):
        return len(self.players)

class Player:
    def __init__(self, name):
        self.name=name
            
    def getName(self):
        return self.name

