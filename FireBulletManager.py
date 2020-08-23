from threading import Thread
import time


class FireBulletManager(Thread):

    def __init__(self, gameboard):
        self.gameBoard = gameboard
        self.bullets = []

    def add_bullet(self, bullet):
        self.bullets.append(bullet)
        print("bullet added")

    def firing(self):
        while self.gameBoard.isRunning():
            time.sleep(1)

    def run(self):
        while self.gameBoard.isRunning():
            time.sleep(0.1)

    def startThread(self):
        Thread.__init__(self)
        Thread.start(self)
