from pyclassgame import Game, Scene, GameObject, Colors, Image

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
        elif key_name == 'z': self.game.camera.set_zoom(0.5)
        elif key_name == 'x': self.game.camera.set_zoom(1.0)
        elif key_name == 'c': self.game.camera.set_zoom(1.5)

class Player (GameObject):
    def __init__(self, color, x, y, z, width, height):
        super().__init__(x=x, y=y, z=z, width=width, height=height, color=color)
    def update(self):
        self.scene.game.camera.target(self.x, self.y)
        # cube = self.scene.get_game_object('cube')
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
    game.get_active_scene().add_game_object('player', Player(color=Colors['red'], x=100, y=100, z=1, width=75, height=100))
    game.get_active_scene().add_game_object('cube', GameObject(width = 30, height = 50, z=0, color=Colors['blue']))
    gui = game.get_active_scene().instant_game_object(GameObject(gui = True))
    gui = game.get_active_scene().instant_game_object(Image(image_path='img.png', image_alpha=255, image_width=32, image_height=32, image_offset_x=50, x=100))

    game.run()