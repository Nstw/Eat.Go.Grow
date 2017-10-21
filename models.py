import arcade
import arcade.key
from random import randint
from genfood import Food

class Player:    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.MOVE_X = 0
        self.MOVE_Y = 0
        self.scale = 0.2
        self.Move_Speed = 5
        self.win = False

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
    
        for x in self.world.food_list:
            if self.hit(x, 20+(20*self.scale)): 
                x.center_x = randint(0, self.world.width-1)
                x.center_y = randint(0, self.world.height-1)
                self.scale += 0.05
        '''
        self.world.check_gift = False
        if self.hit(self.world.gift, 10+(10*self.scale)):
            self.Move_Speed += self.Move_Speed*0.1
            self.world.check_gift = True
        '''
    def hit(self, other, hit_size):
        return (abs(self.x-other.center_x)<=hit_size) and (abs(self.y-other.center_y)<=hit_size)

    def hit_player(self, other, hit_size):
        return (abs(self.x-other.x)<=hit_size) and (abs(self.y-other.y)<=hit_size)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.food_list = arcade.SpriteList()
        self.food_list = Food().food_list

        self.gift = arcade.Sprite()
        self.gift = Food().gift

        self.bear = Player(self, 200, 350)
        self.pig = Player(self, 1000, 350)

        self.check_gift = False

    def update(self, delta):
        if not(self.pig.win):
            self.bear.update(delta)
        if not(self.bear.win):
            self.pig.update(delta)

        self.check_gift = False
        if self.bear.hit(self.gift, 10+(10*self.bear.scale)):
            self.bear.Move_Speed += self.bear.Move_Speed*0.1
            self.check_gift = True
        elif self.pig.hit(self.gift, 10+(10*self.pig.scale)):
            self.pig.Move_Speed += self.pig.Move_Speed*0.1
            self.check_gift = True
       
        if self.check_gift :
            self.gift.center_x = randint(0,self.width-10)
            self.gift.center_y = randint(0,self.height-10)
            self.check_gift = False

        if self.bear.hit_player(self.pig, 15+(15*self.pig.scale)):
            if (self.bear.scale > self.pig.scale):
                self.bear.win = True
        if self.pig.hit_player(self.bear, 15+(15*self.bear.scale)):
            if (self.pig.scale > self.bear.scale):
                self.pig.win = True    

    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.UP):            
            self.pig.MOVE_Y = self.pig.Move_Speed
        elif (key == arcade.key.DOWN):            
            self.pig.MOVE_Y = self.pig.Move_Speed*-1
        elif (key == arcade.key.LEFT):            
            self.pig.MOVE_X = self.pig.Move_Speed*-1
        elif (key == arcade.key.RIGHT):            
            self.pig.MOVE_X = self.pig.Move_Speed

        if (key == arcade.key.W):
            self.bear.MOVE_Y = self.bear.Move_Speed
        elif (key == arcade.key.S):
            self.bear.MOVE_Y = self.bear.Move_Speed*-1
        elif (key == arcade.key.A):
            self.bear.MOVE_X = self.bear.Move_Speed*-1
        elif (key == arcade.key.D):
            self.bear.MOVE_X = self.bear.Move_Speed

    def on_key_release(self, key, key_modifiers):
        if (key == arcade.key.UP or key == arcade.key.DOWN):
            self.pig.MOVE_Y  = 0
        elif (key == arcade.key.LEFT or key == arcade.key.RIGHT):
            self.pig.MOVE_X = 0
        if (key == arcade.key.W or key == arcade.key.S):
            self.bear.MOVE_Y = 0
        elif (key == arcade.key.A or key == arcade.key.D):
            self.bear.MOVE_X = 0