import time
from threading import Thread
from random import randrange

import Math
from Bullet import Bullet
from Monster import Monster
from Point2D import Point2D
from Screen import Screen


class MonstersManager(Thread):
    def __init__(self, game_board, screen):
        super().__init__()
        self.screen = screen
        self.game_board = game_board
        self.total_monsters = 0

    def run(self):
        while self.game_board.is_running():
            time.sleep(0.001)
            self.control_monsters()
            self.manage_monsters()

    def start_thread(self):
        Thread.__init__(self)
        Thread.start(self)

    def kill_monster(self):
        pass

    def manage_monsters(self):
        try:
            total_monsters = (len(self.game_board.monsters))
            if total_monsters > 0:
                for i in range(total_monsters):
                    current_monster = self.game_board.monsters[i]
                    monster_position = current_monster.get_position()
                    velocity = current_monster.get_velocity()
                    y = monster_position.gety()
                    y = y + velocity
                    current_monster.get_position().sety(y)

                    # check if a monster is at the bottom of the screen
                    if current_monster.get_position().gety() > Screen.SCREEN_HEIGHT - 100:
                        self.game_board.decrease_lives()
                        self.remove_monster(i)
                        break

                    # check if a monster is close enough to the player
                    if Math.distance(monster_position, self.game_board.player.get_position()) < 30:
                        self.game_board.decrease_lives()
                        self.remove_monster(i)
                        break

                    if self.game_board.player_score > 1:
                        choose_a_number = randrange(0, 500, 1)
                        if choose_a_number == 2:
                            current_monster.fire("down")
        except:
            print("exception 3425367")

    def control_monsters(self):
        if len(self.game_board.monsters) < self.total_monsters:
            x = randrange(50, Screen.SCREEN_WIDTH-100, 1)
            init_position = Point2D(x, 10)
            velocity = 1
            self.game_board.monsters.append(Monster(self.game_board, init_position, velocity))

    def remove_monster(self, index):
        del self.game_board.monsters[index]

    def is_monster_bellow_screen(self, current_monster):
        if current_monster.get_position().gety() > Screen.SCREEN_HEIGHT - 100:
            print(current_monster.get_position().print())
            self.game_board.decrease_lives()




