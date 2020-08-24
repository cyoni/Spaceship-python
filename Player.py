from ObjectThatFires import ObjectThatFires
from Point2D import Point2D


class Player(ObjectThatFires):

    def __init__(self, gameboard):
        ObjectThatFires.__init__(self, self, gameboard, Point2D(370, 400), 'player.png', 5)


