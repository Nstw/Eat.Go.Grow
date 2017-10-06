import arcade.key
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
        self.status_move = 0
    
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
        #self.grapes = Food(self, 300, 200)

        #self.food = Food(self, 100, 100)
        self.food_list = arcade.SpriteList()
        self.food_list = Food().food_list

        #self.food_list.append(self.grapes)

        #self.collision_list = arcade.geometry.check_for_collision(self.grapes, self.bear)

    def update(self, delta):
        self.bear.update(delta)
        self.pig.update(delta)
        for x in self.food_list:
            if self.bear.hit(x, 10):
                x.kill()


    #def checkCollide(self):
    #    if (self.collision_list == TRUE):
    #        self.food_list.remove(grapes)

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