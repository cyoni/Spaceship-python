import pygame as game
from Screen import Screen
from GameBoard import GameBoard

game.init()
screen = game.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
gameBoard = GameBoard(screen)
gameBoard.wait_for_user()

