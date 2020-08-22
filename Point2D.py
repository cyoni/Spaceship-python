class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    

    def printpoint(self):
        print("[", self.x, ",", self.y, "]")

