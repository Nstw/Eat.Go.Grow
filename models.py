import arcade.key

DIR_UP = 1
DIR_DOWN = 2
DIR_RIGHT = 3
DIR_LEFT = 4

DIR_OFFSET = {DIR_UP:(0,1) , DIR_DOWN: (0,-1) , }

class BearPig:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_DOWN

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = BearPig(self, 200, 350)

        self.pig = BearPig(self, 1000, 350)

    def on_key_release(self, key, key_modifiers):
        if (key == arcade.key.UP):
            self.bear.direction = DIR_UP 