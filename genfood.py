import arcade
from random import randint, random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675

class Food:
    def __init__(self):
        self.food_list = arcade.SpriteList()
        #for i in range (0, random.randrange(0,10)):
        self.random_food()
        
        #self.add_to_list()
    '''
    def setup(self, width, height):
        self.center_x = randint(0, width)
        self.center_y = randint(0, height)
    '''
    def check_amountOf_sprite(self, i):
        len_foodlist = len(self.food_list)
        if len_foodlist < i:
            return True
        else:
            return False

    def random_food(self):
        for i in range(0, 10):
            if (self.check_amountOf_sprite(i)):
                self.add_to_list()
            else:
                for x in self.food_list:
                    x.kill()
    #def del_sprite_randomly(self):
    #    self.kill()            

    #def make_food(self):
    #    self.size = random.randrange(10,30)
    def add_to_list(self):
        self.sweets = ["grapes", "banana", "carrot", "salad", "donut", "hamburguer", "ice-cream"] #list of food
        random_sweets = randint(0, len(self.sweets)-1)
        food = arcade.Sprite("images/" + self.sweets[random_sweets] + ".png", 1)
        food.center_x = randint(0, SCREEN_WIDTH-10)
        food.center_y = randint(0,SCREEN_HEIGHT-10)
        self.food_list.append(food)

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

        self.food_list.append(grapes)
    '''