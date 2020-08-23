from Point2D import Point2D


class GameObject:

    def __init__(self, screen, position, picture):
        self.position = position
        self.picture = picture
        self.screen = screen

    def get_position(self):
        return self.position

    def get_picture(self):
        return self.picture

    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y


