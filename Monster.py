import LoadImages
from ObjectThatFires import ObjectThatFires
from Point2D import Point2D
from random import randrange


def pick_picture():
    num = randrange(1, 3, 1)
    return LoadImages.monster_image


class Monster(ObjectThatFires):

    def __init__(self, gameboard, init_position, velocity):
        ObjectThatFires.__init__(self, self, gameboard, init_position, pick_picture(), velocity)
