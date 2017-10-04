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

    def draw(self):
        self.sync_with_model()
        super().draw()

class BearPigWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.bear_sprite = ModelSprite('images/bear2.png', model = self.world.bear)
        #self.bear_sprite.set_position(0,0)

        self.pig_sprite = ModelSprite('images/pig1.png', model = self.world.pig)
        #self.pig_sprite.set_position(0,0)

    def on_draw(self):
        arcade.start_render()
        
        self.bear_sprite.draw()
        self.pig_sprite.draw()

def main():
    window = BearPigWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()