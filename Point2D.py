class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def printpoint(self):
        print("[", self.x, ",", self.y, "]")

