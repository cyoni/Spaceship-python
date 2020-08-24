from ObjectThatFires import ObjectThatFires
from Point2D import Point2D
from Screen import Screen


class Player(ObjectThatFires):

    def __init__(self, gameboard):
        ObjectThatFires.__init__(self, self, gameboard, Point2D(Screen.SCREEN_WIDTH / 2, Screen.SCREEN_HEIGHT),
                                 'images/player.png', 5)
