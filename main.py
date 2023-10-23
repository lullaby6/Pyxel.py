from pyclassgame import Game, Scene, GameObject, Colors, Image

class MainScene (Scene):
    def __init__(self):
        super().__init__()

    def load(self):
        # self.ignore_pause = True

        self.game.camera.x = -50
        self.game.camera.y = -50

        self.add_game_object('player', Player(color=Colors['red'], x=100, y=100, z=1, width=75, height=100))
        self.add_game_object('cube', GameObject(width = 30, height = 50, z=0, color=Colors['blue']))
        gui = self.instant_game_object(GameObject(gui = True))
        self.instant_game_object(Image(image_path='img.png', image_alpha=255, image_width=32, image_height=32, x=100, y=250))

    def update(self):
        cube = self.get_game_object('cube')
        cube.x += 0.25

    def key_down(self, event, key_name):
        # print(event.key, key_name)
        if key_name == 'f': self.game.toggle_fullscreen()
        elif key_name == 'p': self.game.toggle_pause()
        elif key_name == 'o': self.game.screenshot()
        elif key_name == 'z': self.game.camera.set_zoom(0.5)
        elif key_name == 'x': self.game.camera.set_zoom(1.0)
        elif key_name == 'c': self.game.camera.set_zoom(1.5)
        elif key_name == 'r': self.reset()
        elif key_name == 'm':
            cube = self.get_game_object('cube')
            cube.active = False

class Player (GameObject):
    def __init__(self, color, x, y, z, width, height):
        super().__init__(x=x, y=y, z=z, width=width, height=height, color=color)
    def load(self):
        self.ignore_pause = True
        pass
    def update(self):
        self.scene.game.camera.target(self.x, self.y)
        # print('xd', self.x, self.y)
        pass
    def on_click(self, event):
        print('omg')
    def on_collide(self, other):
        print('collide!!!!!!!!!!!!')


    def key_down(self, event, keyname):
        if keyname == 'w': self.y -= 10
        if keyname == 'a': self.x -= 10
        if keyname == 's': self.y += 10
        if keyname == 'd': self.x += 10

if __name__ == "__main__":
    game = Game(width=640, height=480, bg_color=Colors['lightblue'], bg_alpha=60, title='Title', quit_on_escape=True)
    game.set_icon('icon.png')

    game.set_scene('main', MainScene())

    game.run()