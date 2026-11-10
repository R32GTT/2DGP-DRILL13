from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    SMALL = 1
    LARGE = 2
    images = {}

    def __init__(self, x, y, velocity, size=SMALL):
        if size not in Ball.images:
            filename = 'ball41x41.png' if size == Ball.LARGE else 'ball21x21.png'
            Ball.images[size] = load_image(filename)
        self.x, self.y = x, y
        self.velocity = velocity
        self.image = Ball.images[size]

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
