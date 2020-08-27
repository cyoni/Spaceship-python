import pygame as game

import LoadImages
from Screen import Screen
from GameBoard import GameBoard
from Keyboard import Keyboard

game.init()
screen = game.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
gameBoard = GameBoard(screen)
keyboard = Keyboard(game, gameBoard.get_player())
font = game.font.Font('SansBold.ttf', 32)

gameBoard.start_game()


def show_score():
    score = font.render("Score: " + str(gameBoard.player_score), True, (255, 255, 255))
    screen.blit(score, (10, 10))


def update_lives():
    num_of_lives = gameBoard.lives
    for i in range(num_of_lives):
        screen.blit(LoadImages.lives_image, (Screen.SCREEN_WIDTH - 70 - i * 40, 20))





def update_monsters():
    for i in range(len(gameBoard.monsters)):
        current_monster = gameBoard.monsters[i]
        x = current_monster.get_position().getx()
        y = current_monster.get_position().gety()
        screen.blit(current_monster.get_picture(), (x, y))


def update_bullets():
    for i in range(len(gameBoard.bullets)):
        current_bullet = gameBoard.bullets[i]
        x = current_bullet.get_position().getx()
        y = current_bullet.get_position().gety()
        screen.blit(current_bullet.get_picture(), (x, y))


def update_player():
    pos = gameBoard.player.get_position()
    x = pos.getx()
    y = pos.gety()
    screen.blit(gameBoard.player.get_picture(),
                (x, y))


while gameBoard.is_running():
    for event in game.event.get():
        if event.type == game.QUIT:
            gameBoard.stop_game()
        keyboard.fire_when_space_key_pressed(event, game)

    keyboard.manage_keyboard()
    screen.blit(LoadImages.background_image, [0, 0])  # has to be first
    gameBoard.determine_level()
    show_score()
    update_lives()
    update_monsters()
    update_player()
    update_bullets()
    screen.blit(gameBoard.player.get_picture(), (gameBoard.player.position.getx(), gameBoard.player.position.gety()))
    game.display.update()
