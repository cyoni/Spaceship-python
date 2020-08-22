class gameObject:

    def __init__(self, screen, position, picture):
        self.position = position
        self.picture = picture
        self.screen =  screen

    def getPosition(self):
        return self.position

    def getPicture(self):
        return self.picture

    def setPosition(self, x, y):
         self.screen.blit(self.picture, (x, y))
         self.position.x = x
         self.position.y = y