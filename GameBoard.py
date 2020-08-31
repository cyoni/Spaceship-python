import LoadImages
from FireBulletManager import FireBulletManager
from GameAlgo import GameAlgo
from MonstersManager import MonstersManager
from Player import Player
import pygame as game
from Screen import Screen


class GameBoard:

    def __init__(self, screen):
        self.player_score = 0
        self.screen = screen
        self.bullets = []
        self.monsters = []
        self.running = False
        self.player = Player(self)
        self.firing = FireBulletManager(self, screen)
        self.monsters_manager = MonstersManager(self, screen)
        self.lives = 0

    def start_game(self):
        self.running = True
        self.firing.start()
        self.monsters_manager.start()
        self.lives = 3
        game_algo = GameAlgo(self)
        game_algo.playing()

    def get_player(self):
        return self.player

    def is_running(self):
        return self.running

    def stop_game(self):
        self.running = False

    def get_player_score(self):
        return self.player_score

    def decrease_lives(self):
        self.lives = self.lives - 1
        if self.lives <= 0:
            self.stop_game()

    def determine_level(self):
        if self.player_score < 3:
            self.monsters_manager.total_monsters = 1
        elif self.player_score < 10:
            self.monsters_manager.total_monsters = 2
        elif self.player_score < 30:
            self.monsters_manager.total_monsters = 4
        elif self.player_score < 60:
            self.monsters_manager.total_monsters = 6
        elif self.player_score < 90:
            self.monsters_manager.total_monsters = 10
        elif self.player_score < 120:
            self.monsters_manager.total_monsters = 20
        elif self.player_score < 150:
            self.monsters_manager.total_monsters = 30

    def increase_score(self):
        self.player_score = self.player_score + 1

    def wait_for_user(self):
        i = 0
        while True:
            for event in game.event.get():
                if event.type == game.QUIT:
                    break
                if event.type == game.KEYDOWN and event.key == game.K_SPACE:
                    self.start_game()
            self.screen.blit(LoadImages.background_image, [0, 0])  # this has to be first
            font = game.font.Font('SansBold.ttf', 32)
            score = font.render("Press Space To Start", True, (255, 255, 255))
            self.screen.blit(score, (Screen.SCREEN_WIDTH/2-150, Screen.SCREEN_HEIGHT/2))
            game.display.update()
