import LoadImages
from Point2D import Point2D
from gameobject import GameObject


def choose_image(target):
    if target == "player": 
        return LoadImages.bullet_down_image
    else:
        return LoadImages.bullet_image


class Bullet(GameObject):
    def __init__(self, position, vector, target):
        super().__init__(position, choose_image(target))
        self.position = position
        self.velocity = 5
        self.target = target
        self.vector = vector

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = Point2D(x, y)

    def get_velocity(self):
        return self.velocity

    def get_vector(self):
        return self.vector

    def get_target(self):
        return self.target
