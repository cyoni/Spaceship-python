from Bullet import Bullet
from Point2D import Point2D
from gameobject import GameObject
import pygame as game


class ObjectThatFires(GameObject):

    def __init__(self, firing_object, game_board, position, picture, movement_velocity):
        super().__init__(position, picture)
        self.gameBoard = game_board
        self.movement_velocity = movement_velocity
        self.firing_object = firing_object
        self.imgBullet = game.image.load('images/bullet.png')

    def fire(self, where, target):  # up or down
        object_position = self.firing_object.get_position()
        delta = 0
        if where == "up":
            delta = -35
        else:
            delta = 50
        self.gameBoard.firing.add_bullet \
            (Bullet(Point2D(object_position.getx() + 20, object_position.gety() + delta), where, target))

    def get_velocity(self):
        return self.movement_velocity
