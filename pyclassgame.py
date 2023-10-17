import pygame, sys, json, uuid

class GameObject:
    def __init__(self, name = None, scene = None):
        self.name = name
        self.scene = scene
        self.tags = []
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

class Scene:
    def __init__(self, name = None, game = None):
        self.name = name
        self.game = game
        self.game_objects = {}
    def add_game_object(self, name, game_object):
        self.game_objects[name] = game_object(name, self)
        return self.game_objects[name]
    def instant_game_object(self, game_object):
        name = str(uuid.uuid4())
        self.game_objects[name] = game_object(name, self)
        return self.game_objects[name]
    def remove_game_object(self, name):
        del self.game_objects[name]
    def get_game_object(self, name):
        return self.game_objects[name]

class Game:
    def __init__(self, width = 640, height = 480, title = 'Title', fps = 60, default_scene = Scene):
        pygame.init()
        self.set_title(title)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.prev_time = pygame.time.get_ticks()

        self.scenes = {}
        self.active_scene = None
        self.add_scene('default', default_scene)
        self.change_scene('default')

        self.quit_on_escape = False
    def run(self):
        while True:
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
                'joy_button_up': pygame.JOYBUTTONUP
            }

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.quit_on_escape:
                        return
                for eventName in events:
                    if event.type == events[eventName]:
                        key_name = None
                        if hasattr(event, 'key'): key_name = pygame.key.name(event.key)
                        if hasattr(active_scene, eventName):
                            getattr(active_scene, eventName)(event, key_name)
                        for game_object in game_objects:
                            if hasattr(game_object, eventName):
                                getattr(game_object, eventName)(event, key_name)

            current_time = pygame.time.get_ticks()
            self.delta_time = (current_time - self.prev_time) / 1000.0
            self.prev_time = current_time

            if hasattr(active_scene, 'update'): active_scene.update()
            for game_object in game_objects:
                if hasattr(game_object, 'update'): game_object.update()

            pygame.display.update()
            self.clock.tick(self.fps)
    def set_title(self, title):
        self.title = title
        pygame.display.set_caption(title)
    def add_scene(self, name, scene):
        self.scenes[name] = scene(name, self)
        return self.scenes[name]
    def change_scene(self, name):
        self.active_scene = name
    def get_active_scene(self):
        return self.scenes[self.active_scene]
    def remove_scene(self, name):
        del self.scenes[name]