import arcade
from random import randint, random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675

class Food:
    def __init__(self):
        self.food_list = arcade.SpriteList()
        self.add_food()

    def add_food(self):
        for i in range(0, 8):
            self.add_to_list()

    def add_to_list(self):
        self.sweets = ["grapes", "banana", "carrot", "salad", "donut", "hamburguer", "ice-cream"] #list of food
        random_sweets = randint(0, len(self.sweets)-1)
        food = arcade.Sprite("images/" + self.sweets[random_sweets] + ".png", 1)
        food.center_x = randint(0, SCREEN_WIDTH-10)
        food.center_y = randint(0,SCREEN_HEIGHT-10)
        self.food_list.append(food)