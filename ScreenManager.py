import pygame as game


class ScreenManager:
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800

    def __init__(self, gameBoard, keyboard):
        self.gameBoard = gameBoard
        self.keyboard = keyboard
        self.background_image = game.image.load("background.png").convert()
        self.screen = game.display.set_mode((ScreenManager.SCREEN_WIDTH, ScreenManager.SCREEN_HEIGHT))

    def ScreenManager(self):
        while self.gameBoard.isRunning():
            for event in game.event.get():
                if event.type == game.QUIT:
                    self.gameBoard.stopGame()
                self.keyboard.manage_keyboard(event, game)

            self.gameBoard.updatePlayer()
            ScreenManager.checkPlayerBounderies(self.gameBoard.player)
            self.screen.blit(self.background_image, [0, 0])
            self.screen.blit(self.gameBoard.player.picture, (self.gameBoard.player.position.getx(), self.gameBoard.player.position.gety()))
            game.display.update()

    def checkPlayerBounderies(self, player):
        playerx = player.get_position().getx()
        playery = player.get_position().gety()
        x_boundary = ScreenManager.SCREEN_WIDTH - 50
        y_boundary = ScreenManager.SCREEN_HEIGHT - 80

        if playerx <= 0:
            player.get_position().setx(0)
        if playery <= 0:
            player.get_position().sety(0)
        elif playerx >= x_boundary:
            player.get_position().setx(x_boundary)
        elif playery >= y_boundary:
            player.get_position().sety(y_boundary)
