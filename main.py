import pygame as game
from Keyboard import Keyboard
from Player import Player
from Point2D import Point2D
from Screen import Screen

game.init()
screen = game.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
background_image = game.image.load("background.png").convert()
player = Player(screen)
keyboard = Keyboard(game, player)
running = True


def updatePlayer():
    x = keyboard.getxchange()
    y = keyboard.getychange()
    player.set_position(player.get_position().getx() + x, player.get_position().gety() + y)


def checkPlayerBounderies():
    playerx = player.get_position().getx()
    playery = player.get_position().gety()
    x_boundary = Screen.SCREEN_WIDTH-50
    y_boundary = Screen.SCREEN_HEIGHT-80

    if playerx <= 0:
        player.get_position().setx(0)
    if playery <= 0:
        player.get_position().sety(0)
    elif playerx >= x_boundary:
        player.get_position().setx(x_boundary)
    elif playery >= y_boundary:
        player.get_position().sety(y_boundary)


while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        keyboard.manage_keyboard(event, game)

    updatePlayer()
    checkPlayerBounderies()
    screen.blit(background_image, [0, 0])
    screen.blit(player.picture, (player.position.getx(), player.position.gety()))
    game.display.update()
