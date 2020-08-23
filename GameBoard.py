from FireBulletManager import FireBulletManager
from Player import Player


class GameBoard:

    def __init__(self):
        self.monsters = []
        self.running = False
        self.player = Player(self)
        self.firing = FireBulletManager(self)



    def startgame(self):
        self.running = True
        self.firing.startThread()


    def getplayer(self):
        return self.player

    def isRunning(self):
        return self.running

    def stopGame(self):
        self.running = False
