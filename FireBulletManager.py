from threading import Thread
import time

import Math
from Screen import Screen


class FireBulletManager(Thread):

    def __init__(self, game_board, screen):
        super().__init__()
        self.game_board = game_board
        self.screen = screen

    def add_bullet(self, bullet):
        self.game_board.bullets.append(bullet)

    def run(self):
        while self.game_board.is_running():
            time.sleep(0.01)
            self.bullets_flying()

    def start_thread(self):
        Thread.__init__(self)
        Thread.start(self)

    def bullets_flying(self):
        try:
            num_bullets = (len(self.game_board.bullets))
            if num_bullets > 0:
                for i in range(num_bullets):
                    current_bullet = self.game_board.bullets[i]
                    position = current_bullet.get_position()
                    vector = current_bullet.get_vector()
                    velocity = current_bullet.get_velocity()
                    x = position.getx()
                    y = position.gety()

                    if vector == "up":
                        y = y - velocity
                    else:
                        y = y + velocity

                    if position.gety() < 0 or position.gety() > Screen.SCREEN_HEIGHT-50:
                        del self.game_board.bullets[i]
                        break
                    else:
                        current_bullet.get_position().sety(y)
                        self.check_if_bullet_hits_player(current_bullet, i)
                        self.check_if_bullet_hits_monster(current_bullet, i)
        except:
            print("exeption 333")

    def check_if_bullet_hits_monster(self, current_bullet, bullet_index):
        for i in range(len(self.game_board.monsters)):
            bullet_position = current_bullet.get_position()
            dis = Math.distance(bullet_position, self.game_board.monsters[i].get_position())
            if dis < 30:
                del self.game_board.monsters[i]
                self.game_board.increase_score()
                # del self.game_board.bullets[bullet_index]
                break

    def check_if_bullet_hits_player(self, current_bullet, bullet_index):
        bullet_position = current_bullet.get_position()
        dis = Math.distance(bullet_position, self.game_board.player.get_position())
        if dis < 30:
            self.game_board.decrease_lives()
            del self.game_board.bullets[bullet_index]
