import pygame as game

import LoadImages


class GameObject:

    def __init__(self, position, picture):
        self.position = position
        self.picture = picture

    def get_position(self):
        return self.position

    def get_picture(self):
        return self.picture

    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y
