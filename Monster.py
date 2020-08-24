from ObjectThatFires import ObjectThatFires
from Point2D import Point2D
from random import randrange


class Monster(ObjectThatFires):

    def __init__(self, gameboard, init_position, velocity):
        ObjectThatFires.__init__(self, self, gameboard, init_position, self.pick_picture(), velocity)

    def pick_picture(self):
        num = randrange(1, 3, 1)
        return "images/monster" + str(num) + ".png"

