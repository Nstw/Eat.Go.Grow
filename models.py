import arcade.key
from random import randint
from genfood import Food

DIR_UP = 1
DIR_DOWN = 2
DIR_RIGHT = 3
DIR_LEFT = 4

DIR_OFFSET = {DIR_UP:(0,1), DIR_RIGHT:(1,0), DIR_DOWN:(0,-1), DIR_LEFT:(-1,0)}

MOVE_SPEED = 10

class Player:    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.MOVE_X = 0
        self.MOVE_Y = 0
        self.status_move = 0
        self.scale = 0.2
'''
    def update(self, delta):
        self.x += self.MOVE_X
        self.y += self.MOVE_Y

        if self.x > self.world.width:
            self.x = 0
        elif self.x < 0:
            self.x = self.world.width
        
        if self.y > self.world.height:
            self.y = 0        
        elif self.y < 0:
            self.y = self.world.height
'''    
    def hit(self, other, hit_size):
        return (abs(self.x-other.center_x)<=hit_size) and (abs(self.y-other.center_y)<=hit_size)

class Bear(Player):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def update(self, delta): 
        if self.status_move == DIR_UP:
            self.y += MOVE_SPEED
        elif self.status_move == DIR_DOWN:
            self.y -= MOVE_SPEED
        elif self.status_move == DIR_RIGHT:
            self.x += MOVE_SPEED
        elif self.status_move == DIR_LEFT:
            self.x -= MOVE_SPEED
        
        if self.x > self.world.width:
            self.x = 0
        elif self.x < 0:
            self.x = self.world.width
        
        if self.y > self.world.height:
            self.y = 0        
        elif self.y < 0:
            self.y = self.world.height

class Pig(Player):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.status_move == DIR_UP:
            self.y += MOVE_SPEED
        elif self.status_move == DIR_DOWN:
            self.y -= MOVE_SPEED
        elif self.status_move == DIR_RIGHT:
            self.x += MOVE_SPEED
        elif self.status_move == DIR_LEFT:
            self.x -= MOVE_SPEED

        if self.x > self.world.width:
            self.x = 0
        elif self.x < 0:
            self.x = self.world.width
        
        if self.y > self.world.height:
            self.y = 0        
        elif self.y < 0:
            self.y = self.world.height

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Bear(self, 200, 350)
        self.pig = Pig(self, 1000, 350)
        self.food_list = arcade.SpriteList()
        '''
        self.sweets = ["grapes", "banana", "carrot", "salad", "donut", "hamburguer", "ice-cream"] #list of food
        random_sweets = randint(0, len(self.sweets)-1)
        food = Food("images/" + self.sweets[random_sweets] + ".png", 1)
        food.setup(self.width, self.height)
        self.food_list.append(food)
        '''
        self.food_list = Food().food_list

    def update(self, delta):
        self.bear.update(delta)
        self.pig.update(delta)
        for x in self.food_list:
            if self.bear.hit(x, 20+(20*self.bear.scale)): 
                x.kill()
                self.bear.scale += 0.1
            elif self.pig.hit(x, 20+(20*self.pig.scale)):
                x.kill()
                self.pig.scale += 0.1

    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.UP):            
            self.pig.status_move = DIR_UP
        elif (key == arcade.key.DOWN):            
            self.pig.status_move = DIR_DOWN
        elif (key == arcade.key.LEFT):            
            self.pig.status_move = DIR_LEFT
        elif (key == arcade.key.RIGHT):            
            self.pig.status_move = DIR_RIGHT

        if (key == arcade.key.W):
            self.bear.status_move = DIR_UP
        elif (key == arcade.key.S):
            self.bear.status_move = DIR_DOWN
        elif (key == arcade.key.A):
            self.bear.status_move = DIR_LEFT
        elif (key == arcade.key.D):
            self.bear.status_move = DIR_RIGHT

    def on_key_release(self, key, key_modifiers):
        if (key == arcade.key.UP or key == arcade.key.DOWN or
            key == arcade.key.LEFT or key == arcade.key.RIGHT):
            self.pig.status_move = 0
        elif (key == arcade.key.W or key == arcade.key.S or
            key == arcade.key.A or key == arcade.key.D):
            self.bear.status_move = 0