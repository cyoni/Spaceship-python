from Screen import Screen


class Keyboard:

    def __init__(self, game, player):
        self.player = player
        self.game = game
        self.change = 3

    def manage_keyboard(self):

        player_pos = self.player.get_position()
        x = player_pos.getx()
        y = player_pos.gety()

        keys = self.game.key.get_pressed()

        if keys[self.game.K_LEFT]:
            x = x - 3
        if keys[self.game.K_RIGHT]:
            x = x + 3
        if keys[self.game.K_UP]:
            y = y - 3
        if keys[self.game.K_DOWN]:
            y = y + 3

        self.player.set_position(x, y)
        self.is_player_boundaries_ok(x, y)

    def is_player_boundaries_ok(self, playerx, playery):
        x_boundary = Screen.SCREEN_WIDTH - 70
        y_boundary = Screen.SCREEN_HEIGHT - 80

        if playerx <= 0:
            self.player.get_position().setx(0)
        if playery <= 0:
            self.player.get_position().sety(0)
        elif playerx >= x_boundary:
            self.player.get_position().setx(x_boundary)
        elif playery >= y_boundary:
            self.player.get_position().sety(y_boundary)

    def fire_when_space_key_pressed(self, event, game):
        if event.type == game.KEYDOWN and event.key == game.K_SPACE:
            self.player.fire("up", "monster")
