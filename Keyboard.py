class Keyboard:

    def __init__(self, game, player):
        self.player = player
        self.game = game
        self.x = 0
        self.y = 0
        self.change = 0.5

    def getxchange(self):
        return self.x

    def getychange(self):
        return self.y

    def manage_keyboard(self, event, game):

        if event.type == game.KEYDOWN:
            if event.key == game.K_LEFT:
                self.x = -self.change
            if event.key == game.K_RIGHT:
                self.x = self.change
            if event.key == game.K_UP:
                self.y = -self.change
            if event.key == game.K_DOWN:
                self.y = self.change

        if event.type == game.KEYUP:
            self.x = 0
            self.y = 0
