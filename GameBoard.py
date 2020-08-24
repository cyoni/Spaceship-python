from FireBulletManager import FireBulletManager
from MonstersManager import MonstersManager
from Player import Player


class GameBoard:

    def __init__(self, screen):
        self.player_score = 0
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
