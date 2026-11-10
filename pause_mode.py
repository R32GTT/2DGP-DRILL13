import game_framework
import game_world
from pico2d import *


font = None


def init():
    global font
    font = load_font('../LEC16_Time/ENCR10B.TTF', 50)


def finish():
    global font
    del font


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    draw_rectangle(0, 0, 800, 600)
    font.draw(310, 320, 'PAUSED')
    font.draw(240, 260, 'PRESS P TO RESUME')
    update_canvas()
