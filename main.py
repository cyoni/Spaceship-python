import pygame as game
from Point2D import Point2D
from Player import Player

game.init()
screen = game.display.set_mode((800, 600))

player = Player(screen)



running = True
while running:
    screen.fill((100, 0, 0))
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    player.setPosition(500, 500)
    game.display.update()
