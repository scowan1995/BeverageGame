import random

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

