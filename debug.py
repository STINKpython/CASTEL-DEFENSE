import pygame as py
from configuraciones import *

py.init()
font = py.font.Font(None, 30)

def debug(info, y=10, x=10):
    display_suf = py.display.get_surface()
    debug_surf = font.render(str(info), True, WHITE)
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    py.draw.rect(display_suf, BLACK, debug_rect)
    display_suf.blit(debug_surf, debug_rect)