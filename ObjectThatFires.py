from Bullet import Bullet
from Point2D import Point2D
from gameobject import GameObject
import pygame as game


class ObjectThatFires(GameObject):

    def __init__(self, gameBoard, position, picture):
        super().__init__(position, picture)
        self.gameBoard = gameBoard
        self.imgBullet = game.image.load('bullet.png')

    def fire(self):
        playerPosition = self.gameBoard.getplayer().get_position()
        self.gameBoard.firing.add_bullet(Bullet(Point2D(playerPosition.getx(), playerPosition.gety()), 1))
