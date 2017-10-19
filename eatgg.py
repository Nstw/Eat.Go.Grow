import arcade
from models import World

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.set_scale(self.model.scale)

    def set_scale(self, scale):
        self.width = self.texture.width * scale
        self.height = self.texture.height * scale

    def draw(self):
        self.sync_with_model()
        super().draw()

class PlayerWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMARANTH_PURPLE)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background = arcade.load_texture("images/bg12.png")

        self.bear_sprite = ModelSprite('images/bear3.png', model = self.world.bear)
        self.pig_sprite = ModelSprite('images/pig3.png', model = self.world.pig)
        self.food = self.world.food_list   

        self.gifts = self.world.gift

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.gifts.draw()

        self.food.draw()    
        if not(self.world.pig.win):  
            self.bear_sprite.draw()
        if not(self.world.bear.win):
            self.pig_sprite.draw()

        #self.end_game()        

    #def end_game(self):
    #    arcade.draw_text("bear wins", self.width-30, self.height-30, arcade.color.BLACK, 400)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    
    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

def main():
    window = PlayerWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()