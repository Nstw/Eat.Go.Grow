import arcade
from random import randint, random

class Food(arcade.Sprite):
    def setup(self, width, height):
        self.center_x = randint(0, width)
        self.center_y = randint(0, height)

    ''''
    def __init__(self, width, height):        
        self.width = width
        self.height = height
        self.food_list = arcade.SpriteList()
        self.add_to_list()

    def random_location(self):
        self.x = randint(0, self.world.width-1)
        self.y = randint(0, self.world.height-1)

    def add_to_list(self):
        grapes = arcade.Sprite('images/grapes.png')
        grapes.center_x = randint(0, self.width-1)
        grapes.center_y = randint(0, self.height-1)

        #carrot = arcade.Sprite('images/carrot.png')
        #carrot.center_x = 300

        self.food_list.append(grapes)
    '''