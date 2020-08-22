import pygame as game
from Point2D import Point2D
from gameObject import gameObject 

class Player(gameObject):

    def __init__(self, screen):
        super().__init__(screen, Point2D(370, 400), game.image.load('Ariel.png'))

