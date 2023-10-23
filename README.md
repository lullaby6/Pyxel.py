# pyclassgame

# Index
- [Game](#game)
    - [Default Props](#default-props)
    - [Title](#title)
    - [Icon](#icon)
    - [Size](#size)
    - [Background Color](#background-color)
    - [Background Color Alpha](#background-color-alpha)
    - [Fullscreen](#Fulscreen)
    - [FPS](#fps)
    - [Cursor](#cursor-visibility)
    - [Delta Time](#delta-time)
    - [Screenshot](#screenshot)
    - [Quit on Escape](#quit-on-escape)
- [Scenes](#scenes)
- [GameObject](#gameobject)

# Game

## Initializating game

```python
from pyclassgame import Game

game = Game()

game.run()
```

## Default props

```python
game = Game(width = 640, height = 480, bg_color = Colors['black'], bg_alpha = 255, title = 'Title', cursor = True, fps = 60, quit_on_escape = False, default_scene = Scene())
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

## Size
```python
print(game.width, game.height)
game.set_size(1280, 720)
```

## Background Color
```python
game.bg_color = (123, 255, 100) # default is (255, 255, 255) (white)
```

## Background Color Alpha
```python
game.bg_alpha = 128 # default is 255
```

## Fullscreen
```python
print(game.fullscreen)
game.set_fullscreen(False) # can be True or False, by default is True
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
game.set_cursor_visibility(False) # can be True or False, by default is True
game.toggle_cursor_visibility()
game.hidde_cursor()
game.show_cursor()
```

## Delta Time
```python
print(game.delta_time)
```

## Screenshot
```python
game.screenshot() # default screenshots directory is 'screenshots/'
game.screenshot('my_screenshots')
game.screenshot(os.path.join(__file__, 'my_screenshots'))
```

## Quit on Escape
```python
game.quit_on_escape = True # can be True or False, by default is False
```

# Scenes

## Creating a scene

```python
from pyclassgame import Game, Scene

class MainScene (Scene):
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
    def key_down(self, event, keyname):
        if keyname == 'w': self.y -= 10
        if keyname == 'a': self.x -= 10
        if keyname == 's': self.y += 10
        if keyname == 'd': self.x += 10

class MainScene (Scene):
    def load(self):
        self.add_game_object('player', Player())

game = Game()

game.set_scene('main', MainScene())

game.run()
```