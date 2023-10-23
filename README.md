# pyclassgame

# Index
- [Game](#game)
    - [Title](#title)
    - [Icon](#icon)
    - [Fullscreen](#Fulscreen)
    - [FPS](#fps)
    - [Cursor](#cursor-visibility)
- [Scenes](#scenes)
- [GameObject](#gameobject)

# Game

## Initializating game

```python
from pyclassgame import Game

game = Game()

game.run()
```

## Title
```python
print(self.title)
game.set_title('My Game Title')
```

## Icon
```python
game.set_icon('icon.png')
print(self.icon_path) # icon file path
print(self.icon_image) # icon pygame.image
```

## Fullscreen
```python
print(game.fullscreen)
game.set_fullscreen(False) #can be True or False, by default is True
game.toggle_fullscreen()
```

## FPS
```python
print(game.fps)
game.set_fps(30)
```

## Cursor visibility
```python
print(self.cursor)
game.set_cursor_visibility(False) #can be True or False, by default is True
game.toggle_cursor_visibility()
game.hidde_cursor()
game.show_cursor()
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