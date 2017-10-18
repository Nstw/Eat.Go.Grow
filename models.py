import arcade.key
from random import randint
from genfood import Food

MOVE_SPEED = 9

class Player:    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.MOVE_X = 0
        self.MOVE_Y = 0
        self.scale = 0.2

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
    
    def hit(self, other, hit_size):
        return (abs(self.x-other.center_x)<=hit_size) and (abs(self.y-other.center_y)<=hit_size)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Player(self, 200, 350)
        self.pig = Player(self, 1000, 350)

        self.food_list = arcade.SpriteList()
        self.food_list = Food().food_list

    def update(self, delta):
        self.bear.update(delta)
        self.pig.update(delta)

        for x in self.food_list:
            if self.bear.hit(x, 20+(20*self.bear.scale)): 
                x.center_x = randint(0, self.width-1)
                x.center_y = randint(0, self.height-1)
                self.bear.scale += 0.1
                
            elif self.pig.hit(x, 20+(20*self.pig.scale)):
                x.center_x = randint(0, self.width-1)
                x.center_y = randint(0, self.height-1)
                self.pig.scale += 0.1

    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.UP):            
            self.pig.MOVE_Y = MOVE_SPEED
        elif (key == arcade.key.DOWN):            
            self.pig.MOVE_Y = MOVE_SPEED*-1
        elif (key == arcade.key.LEFT):            
            self.pig.MOVE_X = MOVE_SPEED*-1
        elif (key == arcade.key.RIGHT):            
            self.pig.MOVE_X = MOVE_SPEED

        if (key == arcade.key.W):
            self.bear.MOVE_Y = MOVE_SPEED
        elif (key == arcade.key.S):
            self.bear.MOVE_Y = MOVE_SPEED*-1
        elif (key == arcade.key.A):
            self.bear.MOVE_X = MOVE_SPEED*-1
        elif (key == arcade.key.D):
            self.bear.MOVE_X = MOVE_SPEED

    def on_key_release(self, key, key_modifiers):
        if (key == arcade.key.UP or key == arcade.key.DOWN):
            self.pig.MOVE_Y  = 0
        elif (key == arcade.key.LEFT or key == arcade.key.RIGHT):
            self.pig.MOVE_X = 0
        if (key == arcade.key.W or key == arcade.key.S):
            self.bear.MOVE_Y = 0
        elif (key == arcade.key.A or key == arcade.key.D):
            self.bear.MOVE_X = 0