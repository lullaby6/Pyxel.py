# pyclassgame

# Index
- [Game](#game)
- [Scenes](#installation)
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