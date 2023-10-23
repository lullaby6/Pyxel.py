# pyclassgame

# Index
- [Game](#game)
    - [Icon](##set-icon)
- [Scenes](#scenes)
- [GameObject](#gameobject)

# Game

## Initializating game

```python
from pyclassgame import Game

game = Game()

game.run()
```

## Set title
```python
game.set_title('My Game Title')
```

## Set icon
```python
game.set_icon('icon.png')
```

## Fullscreen Managment
```python
print(game.fullscreen)
game.set_fullscreen(False) #can be True or False, by default is True
game.toggle_fullscreen()
```

# Scenes

# Creating a scene

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

## Creating a simple GameObject

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