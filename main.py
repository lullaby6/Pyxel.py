from pyclassgame import Game, Scene, GameObject, Colors, is_collide

class MainScene (Scene):
    def __init__(self):
        super().__init__()

    def load(self):
        self.game.camera.x = -50
        self.game.camera.y = -50
        pass

    def key_down(self, event, key_name):
        # print(event.key, key_name)
        if key_name == 'f': self.game.toggle_fullscreen()
        elif key_name == 'p': self.game.toggle_pause()
        elif key_name == 'o': self.game.screenshot()

class Player (GameObject):
    def __init__(self, color, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = color
        self.alpha = 100

    def update(self):
        self.scene.game.camera.target(self.x, self.y)
        cube = self.scene.get_game_object('cube')
        print(is_collide(self, cube))
        pass

    def key_down(self, event, keyname):
        if keyname == 'w': self.y -= 10
        if keyname == 'a': self.x -= 10
        if keyname == 's': self.y += 10
        if keyname == 'd': self.x += 10

if __name__ == "__main__":
    game = Game(width=640, height=480, bg_color=Colors['lightblue'], bg_alpha=60, title='Title')

    game.set_scene('main', MainScene())
    game.get_active_scene().add_game_object('player', Player(color=Colors['red'], x=100, y=100, width=75, height=100))
    game.get_active_scene().add_game_object('cube', GameObject(width = 30, height = 50))
    game.get_active_scene().instant_game_object(GameObject(gui = True))

    game.run()