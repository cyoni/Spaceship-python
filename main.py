import pygame as game
from ScreenManager import ScreenManager
from GameBoard import GameBoard
from Keyboard import Keyboard

game.init()


gameBoard = GameBoard()
keyboard = Keyboard(game, gameBoard.getplayer())
screen = ScreenManager(gameBoard, keyboard)


def updatePlayer():
    x = keyboard.getxchange()
    y = keyboard.getychange()
    gameBoard.player.set_position(gameBoard.player.get_position().getx() + x, gameBoard.player.get_position().gety() + y)


gameBoard.startgame()

