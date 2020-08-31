import pygame as game
import LoadImages
from Screen import Screen
from Keyboard import Keyboard


class GameAlgo:

    def __init__(self, game_board):
        self.game_board = game_board
        self.screen = game.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
        self.keyboard = Keyboard(game, game_board.get_player())
        self.font = game.font.Font('SansBold.ttf', 32)

    def show_score(self):
        score = self.font.render("Score: " + str(self.game_board.player_score), True, (255, 255, 255))
        self.screen.blit(score, (10, 10))

    def update_lives(self):
        num_of_lives = self.game_board.lives
        for i in range(num_of_lives):
            self.screen.blit(LoadImages.lives_image, (Screen.SCREEN_WIDTH - 70 - i * 40, 20))

    def update_monsters(self):
        for i in range(len(self.game_board.monsters)):
            current_monster = self.game_board.monsters[i]
            x = current_monster.get_position().getx()
            y = current_monster.get_position().gety()
            self.screen.blit(current_monster.get_picture(), (x, y))

    def update_bullets(self):
        for i in range(len(self.game_board.bullets)):
            current_bullet = self.game_board.bullets[i]
            x = current_bullet.get_position().getx()
            y = current_bullet.get_position().gety()
            self.screen.blit(current_bullet.get_picture(), (x, y))

    def update_player(self):
        pos = self.game_board.player.get_position()
        x = pos.getx()
        y = pos.gety()
        self.screen.blit(self.game_board.player.get_picture(),
                    (x, y))

    def playing(self):
        while self.game_board.is_running():
            for event in game.event.get():
                if event.type == game.QUIT:
                    self.game_board.stop_game()
                self.keyboard.fire_when_space_key_pressed(event, game)
            self.keyboard.manage_keyboard()
            self.screen.blit(LoadImages.background_image, [0, 0])  # this has to be first
            self.game_board.determine_level()
            self.show_score()
            self.update_lives()
            self.update_monsters()
            self.update_player()
            self.update_bullets()
            self.screen.blit(self.game_board.player.get_picture(),
                        (self.game_board.player.position.getx(), self.game_board.player.position.gety()))
            game.display.update()
