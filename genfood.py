import arcade
from random import randint, random

class Food:
    def __init__(self):
        self.food_list = arcade.SpriteList()
        self.add_to_list()
    def add_to_list(self):
        grapes = arcade.Sprite('images/grapes.png')
        grapes.center_x = 100
        grapes.center_y = 100
        self.food_list.append(grapes)