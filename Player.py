

from ObjectThatFires import ObjectThatFires
from Point2D import Point2D


class Player(ObjectThatFires):

    def __init__(self, gameBoard):
        ObjectThatFires.__init__(self, gameBoard, Point2D(370, 400), 'player.png')

