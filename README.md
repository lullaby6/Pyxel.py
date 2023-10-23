# pyclassgame

# Index
- [Game](#game)
    - [Default Props](#default-props)
    - [Title](#title)
    - [Icon](#icon)
    - [Size](#size)
    - [Background Color](#background-color)
    - [Background Color Alpha](#background-color-alpha)
    - [Pause](#pause)
    - [Fullscreen](#Fulscreen)
    - [FPS](#fps)
    - [Cursor](#cursor-visibility)
    - [Delta Time](#delta-time)
    - [Screenshot](#screenshot)
    - [Quit on Escape](#quit-on-escape)
    - [Custom Event](#custom-event)
- [Scenes](#scenes)
    - [Default Props](#default-props-2)
    - [Methods](#scene-methods)
    - [Reset](#reset-scene)
    - [Ignore Pause](#scene-ignore-pause)
- [GameObject](#gameobject)
    - [Default Props](#default-props-3)
- [Image](#Image)
- [Text](#Text)
- [Camera](#camera)
- [Colors](#Colors)
- [Functions](#functions)

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
game.bg_color = (123, 255, 100) # default is (0, 0, 0) (black)
```

## Background Color Alpha

```python
game.bg_alpha = 128 # default is 255
```

## Pause

All update, drawing and event functions will be paused, except Scene events.

```python
print(game.pause)
game.set_pause(True) # can be True or False, by default is False
game.toggle_pause()
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

## Custom Event

### Example

The 'print_name' function is executed for the current scene and all game objects actives.

```python
game.custom_event('print_name', 'Lullaby')

class Player (GameObject):
    def print_name(self, name):
        print(f'My name is: {name}')
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

## Scene Methods

```python
my_scene = Scene() # instancing a base scene
game.add_scene('scene_name', my_scene) # add scene to game.scenes
game.change_scene('scene_name') # change the active/current scene
game.set_scene('scene_name', my_scene) # a shortcut for add_scene and change_scene
game.get_active_scene()
game.remove_scene('scene_name') # delete a scene
game.reset_scene() # reset current scene
```

## Default Props 2

```python
my_scene = Scene(ignore_pause = False)
```

## Reset Scene

```python
active_scene = game.get_active_scene()
active_scene.reset()
```

## Sort Game Objects by Z-Index

This function will be executed automatically when a GameObject is created.

```python
active_scene = game.get_active_scene()
active_scene.sort_game_objects_by_z()
```

## Scene Ignore Pause

```python
my_scene = Scene(ignore_pause = True)
```

or

```python
class MainScene (Scene):
    def load(self):
        self.ignore_pause = True
```

# GameObject

## Creating a GameObject

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

## Default props <span style="color: transparent; opacity: 0; display: none;">3</span>

```python
MyObject = GameObject(x = 0, y = 0, z = 0, width = 10, height = 10, color = Colors['white'], alpha = 255, tags = [], gui = False, ignore_pause = False, active = True, visible = True)

game.get_active_scene().instant_game_object(MyObject)
```