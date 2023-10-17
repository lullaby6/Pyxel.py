from pyclassgame import Game, Scene, GameObject, Colors

class MainScene (Scene):
    def __init__(self):
        super().__init__()

    def key_down(self, event, key_name):
        # print(event.key, key_name)
        if key_name == 'f': self.game.toggle_fullscreen()
        elif key_name == 'p': self.game.toggle_pause()

class Player (GameObject):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.alpha = 100

    def update(self):
        self.scene.game.camera.target(self.x, self.y)
        pass
        # print('xd')

    def key_down(self, event, keyname):
        if keyname == 'w': self.y -= 10
        if keyname == 'a': self.x -= 10
        if keyname == 's': self.y += 10
        if keyname == 'd': self.x += 10

if __name__ == "__main__":
    game = Game(640, 480, Colors['lightblue'], 'Title')

    game.set_scene('main', MainScene())
    game.get_active_scene().add_game_object('player', Player(color=Colors['red']))
    game.get_active_scene().instant_game_object(GameObject())

    game.run()