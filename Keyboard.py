from Screen import Screen


class Keyboard:

    def __init__(self, game, player):
        self.player = player
        self.game = game
        self.x = 0
        self.y = 0
        self.change = 3

    def getxchange(self):
        return self.x

    def getychange(self):
        return self.y

    def manage_keyboard(self, event, game):

        self.checkPlayerBounderies()

        if event.type == game.KEYDOWN:
            if event.key == game.K_LEFT:
                self.x = -self.change
            if event.key == game.K_RIGHT:
                self.x = self.change
            if event.key == game.K_UP:
                self.y = -self.change
            if event.key == game.K_DOWN:
                self.y = self.change
            if event.key == game.K_SPACE:
                self.player.fire("up")

        if event.type == game.KEYUP:
            if event.key == game.K_DOWN or event.key == game.K_UP or event.key == game.K_RIGHT or event.key == game.K_LEFT:
                self.x = 0
                self.y = 0

    def checkPlayerBounderies(self):
        playerx = self.player.get_position().getx()
        playery = self.player.get_position().gety()
        x_boundary = Screen.SCREEN_WIDTH - 50
        y_boundary = Screen.SCREEN_HEIGHT - 80

        if playerx <= 0:
            self.player.get_position().setx(0)
        if playery <= 0:
            self.player.get_position().sety(0)
        elif playerx >= x_boundary:
            self.player.get_position().setx(x_boundary)
        elif playery >= y_boundary:
            self.player.get_position().sety(y_boundary)