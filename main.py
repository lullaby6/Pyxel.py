from pyclassgame import Game, Scene, GameObject

class MainScene (Scene):
    def __init__(self, name, game):
        super().__init__(name, game)
    def update(self):
        self.game.screen.fill((125,0,255))
    def key_down(self, event, key_name):
        print(event.key, key_name)

class Player (GameObject):
    def __init__(self, name, scene):
        super().__init__(name, scene)
    def update(self):
        pass

if __name__ == "__main__":
    game = Game(640, 480, 'Title')

    game.add_scene('main', MainScene)
    game.change_scene('main')
    game.get_active_scene().add_game_object('player', Player)

    game.run()