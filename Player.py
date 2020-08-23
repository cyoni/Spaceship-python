import pygame as game
from Point2D import Point2D
from gameobject import GameObject


class Player(GameObject):

    def __init__(self, screen):
        super().__init__(screen, Point2D(370, 400), game.image.load('player.png'))

