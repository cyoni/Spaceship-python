import pygame as game


class GameObject:

    def __init__(self, position, picture):
        self.position = position
        self.picture = game.image.load(picture)

    def get_position(self):
        return self.position

    def get_picture(self):
        return self.picture

    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y


