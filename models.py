class BearPig:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = BearPig(self, width//2, height//2)