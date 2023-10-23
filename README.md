# pyclassgame

# Index
- [Game](#game)
- [Scenes](#scenes)
- [GameObject](#gameobject)

# Game

```python
from pyclassgame import Game

game = Game()

game.run()
```

# Scenes

```python
from pyclassgame import Game, Scene

class MainScene (Scene):
    def __init__(self):
        super().__init__()

    def load(self):
        print('main scene loaded!')

game = Game()

game.set_scene('main', MainScene())

game.run()
```

# GameObject

```python
from pyclassgame import Game, Scene, GameObject

class Player (GameObject):
    def __init__(self):
        super().__init__()
    def key_down(self, event, keyname):
        if keyname == 'w': self.y -= 10
        if keyname == 'a': self.x -= 10
        if keyname == 's': self.y += 10
        if keyname == 'd': self.x += 10

class MainScene (Scene):
    def __init__(self):
        super().__init__()

    def load(self):
        self.add_game_object('player', Player())

game = Game()

game.set_scene('main', MainScene())

game.run()
```