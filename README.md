# pyclassgame

pyclassgame is a library that adds functionality and structure to pygame, you can still use all your pygame code but remove a lot of boilerplate code.

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
    - [Default Props](#scene-default-props)
    - [Methods](#scene-methods)
    - [Extend](#extend-scene-class)
    - [Reset](#reset-scene)
    - [Ignore Pause](#scene-ignore-pause)
- [GameObject](#gameobject)
    - [Default Props](#gameobject-default-props)
    - [Methods](#gameobject-methods)
    - [Extend](#extend-gameobject-class)
    - [Coords](#coordinates)
    - [Color](#color)
    - [Alpha Color](#aplha-color)
    - [Size](#gameobject-size)
    - [GUI](#gui)
    - [Reset](#gameobject-reset)
    - [Tags](#tags)
    - [Visible](#visible)
    - [Active](#active)
    - [Ignore Pause](#gameobject-ignore-pause)
    - [Z-Index](#z-index)
- [Image](#Image)
- [Text](#Text)
- [Sound](#Text)
- [Events](#Events)
    - [All Events](#all-events)
    - [Extra Events](#extra-events)
    - [GameObject Events](#gameobject-exclusive-events)
    - [Example](#event-example)
- [Camera](#camera)
- [Colors](#Colors)
- [Functions](#functions)

<br>

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

<br>

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

## Scene methods

```python
my_scene = Scene() # instancing a base scene

game.add_scene('scene_name', my_scene) # add scene to game.scenes
game.change_scene('scene_name') # change the active/current scene
game.set_scene('scene_name', my_scene) # a shortcut for add_scene and change_scene
game.get_active_scene()
game.remove_scene('scene_name') # delete a scene
game.reset_scene() # reset current scene
```

## Scene default props

```python
my_scene = Scene(ignore_pause = False)
```

## Extend Scene class

```python
class MainScene (Scene):
    def __init__(self):
        super().__init__()

    def load(self):
        print('main scene loaded!')

    def update(self)
        print('main scene loop.', self.game.delta_time)
```

## Reset scene

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

## Scene ignore pause

```python
my_scene = Scene(ignore_pause = True)
```

or

```python
class MyScene (Scene):
    def load(self):
        self.ignore_pause = True

my_scene = MyScene()
```

<br>

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

## GameObject default props

```python
MyObject = GameObject(x = 0, y = 0, z = 0, width = 10, height = 10, color = Colors['white'], alpha = 255, tags = [], gui = False, ignore_pause = False, active = True, visible = True)

game.get_active_scene().instant_game_object(MyObject)
```

## GameObject methods
```python
active_scene = game.get_active_scene()
player = GameObject()

active_scene.add_game_object('player', player) # create a GameObject with 'player' name
active_scene.instant_game_object(player) # create a GameObject without specifying a name
active_scene.remove_game_object('player') # remove GameObject by name
player = active_scene.get_game_object('player')
```

## Extend GameObject class

```python
class MyGameObject (GameObject):
    def __init__(self):
        super().__init__()

    def load(self):
        print(self.id, 'my-gameobject loaded!')

    def update(self)
        print(self.name, 'my-gameobject scene loop.', self.game.delta_time)
```

## Coordinates

```python
player = GameObject(x=0, y=0, z=0)
```

or

```python
player.x = 25
player.y = 25
player.set_z(1)
```

## Color

```python
player = GameObject(color=(255, 255, 255))
```

or

```python
player.color = Colors['red']
```

## Alpha color

```python
player = GameObject(aplha=128)
```

or

```python
player.alpha = 128
```

## GameObject size

```python
player = GameObject(width=25, height=25)
```

or

```python
player.set_size(25, 25) # width, height
```

or

```python
player.width = 50
player.height = 25
```

## GUI

GameObjects has 'gui' enabled will be fixed in the window.

```python
GUI = GameObject(width=200, height=50, gui=True)
```

## Game Object Reset

```python
player.reset()
```

## Tags

```python
active_scene.instant_game_object(GameObject(tags=['enemy']))

enemies = active_scene.get_game_objects_by_tag('enemy')
```

### Tags methods
```python
player.add_tag('player')
player.remove_tag('player')

if player.has_tag('player'):
    print(player, 'is a player!')

print(player.get_tags())
```

## Visible

```python
player.visible = False # by default is True
```

## Active

```python
player.active = False # by default is True
```

## GameObject ignore pause

```python
player.ignore_pause = True # by default is False
```

## Z-Index

```python
print(player.z)
player.set_z(10)
```

<br>

# Events

## All events

Events for Scenes and GameObjects.

- ```key_down```
- ```key_up```
- ```mouse_down```
- ```mouse_up```
- ```mouse_motion```
- ```mouse_wheel```
- ```joy_axis_motion```
- ```joy_button_down```
- ```joy_button_up```
- ```quit```
- ```fullscreen```
- ```resize```
- ```expose```
- ```focus```

## Extra events

- ```on_pause```

## GameObjects exclusive events
- ```on_collide```
- ```on_click```

## Event Example

```python
class MainScene (Scene):
    def key_down(self, event, key_name):
        if key_name == 'p': self.game.toggle_pause()
```