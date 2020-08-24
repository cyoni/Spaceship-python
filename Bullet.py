from Point2D import Point2D
from gameobject import GameObject


class Bullet(GameObject):

    def __init__(self, position, vector):
        super().__init__(position, 'bullet.png')
        self.position = position
        self.velocity = 5
        self.vector = vector

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = Point2D(x, y)

    def get_velocity(self):
        return self.velocity

    def get_vector(self):
        return self.vector
