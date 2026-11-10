import game_framework
import game_world
import play_mode
from pico2d import *


image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    play_mode.update()


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_mode()
            elif event.key in (SDLK_0, SDLK_1, SDLK_2):
                select_ball(event.key - SDLK_0)


def select_ball(size):
    play_mode.ball_size = size
    play_mode.boy.ball_size = size
    game_framework.pop_mode()
