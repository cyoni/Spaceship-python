import pygame as game


def load(address):
    return game.image.load(address)


bullet_image = load("images/bullet.png")
bullet_down_image = load("images/bullet_down.png")
lives_image = load("images/heart.png")
player_image = load("images/player.png")
monster_image = load("images/monster2.png")
background_image = load("images/background.png")




