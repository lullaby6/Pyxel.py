import pygame, sys, json, uuid

Colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (255, 0, 255),
    'orange': (255, 165, 0),
    'cyan': (0, 255, 255),
    'brown': (165, 42, 42),
    'pink': (255, 192, 203),
    'lightgray': (211, 211, 211),
    'lightblue': (173, 216, 230),
    'lightgreen': (144, 238, 144),
}

class GameObject:
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color = Colors['white'], alpha = 255, tags = [], gui = False):
        self.name = None
        self.scene = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.alpha = alpha
        self.tags = tags
        self.gui = gui
    def drawing(self):
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.set_alpha(self.alpha)
        self.surface.fill(self.color)
        drawingX = self.x
        drawingY = self.y
        if self.gui == False:
            drawingX -= self.scene.game.camera.x
            drawingY -= self.scene.game.camera.y
        self.scene.game.screen.blit(self.surface, (drawingX, drawingY))
    def add_tag(self, tag):
        self.tags.append(tag)
        return tag
    def remove_tag(self, tag):
        self.tags.remove(tag)
        return tag
    def has_tag(self, tag):
        return tag in self.tags
    def get_tags(self):
        return self.tags

class Camera:
    def __init__(self, game, x = 0, y = 0, delay = 50):
        self.game = game
        self.x = x
        self.y = y
        self.delay = delay
    def target(self, x, y):
        # self.x = x - (self.game.width / 2)
        # self.y = y - (self.game.height / 2)
        self.x += ((x - self.game.width/2) - self.x) / self.delay
        self.y += ((y - self.game.height/2) - self.y) / self.delay

class Scene:
    def __init__(self):
        self.name = None
        self.game = None
        self.game_objects = {}
    def add_game_object(self, name, game_object):
        self.game_objects[name] = game_object
        self.game_objects[name].name = name
        self.game_objects[name].scene = self
        if hasattr(self.game_objects[name], 'load'): self.game_objects[name].load()
        return self.game_objects[name]
    def instant_game_object(self, game_object):
        random_uuid_name = str(uuid.uuid4())
        self.add_game_object(random_uuid_name, game_object)
    def remove_game_object(self, name):
        del self.game_objects[name]
    def get_game_object(self, name):
        return self.game_objects[name]
    def get_game_objects_by_tag(self, tag):
        objects = []
        for game_object_name in self.game_objects:
            game_object = self.game_objects[game_object_name]
            if game_object.has_tag(tag):
                objects.append(game_object)
        return objects

class Game:
    def __init__(self, width = 640, height = 480, bg_color = Colors['black'], bg_alpha = 255, title = 'Title', fps = 60, default_scene = Scene()):
        pygame.init()
        self.set_title(title)
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.bg_alpha = bg_alpha
        self.screen = pygame.display.set_mode((self.width, self.height))
        # self.screen.fill(self.bg_color)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.prev_time = pygame.time.get_ticks()

        self.scenes = {}
        self.active_scene = None
        self.set_scene('default', default_scene)

        self.quit_on_escape = False
        self.fullscreen = False

        self.camera = Camera(self, 0, 0)

        self.running = False
        self.pause = False
    def run(self):
        self.running = True
        while self.running:
            active_scene = self.get_active_scene()
            game_objects = active_scene.game_objects
            events = {
                'key_down': pygame.KEYDOWN,
                'key_up': pygame.KEYUP,
                'mouse_down': pygame.MOUSEBUTTONDOWN,
                'mouse_up': pygame.MOUSEBUTTONUP,
                'mouse_motion': pygame.MOUSEMOTION,
                'mouse_wheel': pygame.MOUSEWHEEL,
                'joy_axis_motion': pygame.JOYAXISMOTION,
                'joy_button_down': pygame.JOYBUTTONDOWN,
                'joy_button_up': pygame.JOYBUTTONUP,
                'quit': pygame.QUIT,
                'fullscreen': pygame.FULLSCREEN,
                'resize': pygame.VIDEORESIZE,
                'expose': pygame.VIDEOEXPOSE,
                'focus': pygame.ACTIVEEVENT,
            }

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.quit_on_escape:
                        self.running = False
                for eventName in events:
                    if event.type == events[eventName]:
                        key_name = None
                        if hasattr(event, 'key'): key_name = pygame.key.name(event.key)
                        if hasattr(active_scene, eventName):
                            getattr(active_scene, eventName)(event, key_name)
                        for game_object_name in game_objects:
                            game_object = game_objects[game_object_name]
                            if hasattr(game_object, eventName) and self.pause == False:
                                getattr(game_object, eventName)(event, key_name)

            current_time = pygame.time.get_ticks()
            self.delta_time = (current_time - self.prev_time) / 1000.0
            self.prev_time = current_time

            if(self.pause == False):
                self.bg_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                self.bg_surface.set_alpha(self.bg_alpha)
                self.bg_surface.fill(self.bg_color)
                self.screen.blit(self.bg_surface, (0, 0))

            if hasattr(active_scene, 'update') and self.pause == False:
                active_scene.update()
            if hasattr(active_scene, 'draw') and self.pause == False:
                active_scene.draw()

            for game_object_name in game_objects:
                game_object = game_objects[game_object_name]

                if hasattr(game_object, 'update') and self.pause == False:
                    game_object.update()

                if self.pause == False:
                    game_object.drawing()

                if hasattr(game_object, 'draw'):
                    game_object.draw()

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(self.fps)
    def set_title(self, title):
        self.title = title
        pygame.display.set_caption(title)
    def add_scene(self, name, scene):
        self.scenes[name] = scene
        self.scenes[name].name = name
        self.scenes[name].game = self
        if hasattr(self.scenes[name], 'load'): self.scenes[name].load()
        return self.scenes[name]
    def change_scene(self, name):
        self.active_scene = name
    def set_scene(self, name, scene):
        self.add_scene(name, scene)
        self.change_scene(name)
    def get_active_scene(self):
        return self.scenes[self.active_scene]
    def remove_scene(self, name):
        del self.scenes[name]
    def set_fullscreen(self, fullscreen = True):
        self.fullscreen = fullscreen
        if fullscreen == True:
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
    def toggle_fullscreen(self):
        self.set_fullscreen(not self.fullscreen)
    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
    def set_pause(self, pause):
        self.pause = pause
    def toggle_pause(self):
        self.set_pause(not self.pause)
    def set_fps(self, fps):
        self.fps = fps
        self.clock = pygame.time.Clock()
    def custom_event(self, eventName):
        active_scene = self.get_active_scene()
        game_objects = active_scene.game_objects

        if hasattr(active_scene, eventName) and self.pause == False:
            getattr(active_scene, eventName)()

        for game_object_name in game_objects:
            game_object = game_objects[game_object_name]
            if hasattr(game_object, eventName) and self.pause == False:
                getattr(game_object, eventName)()