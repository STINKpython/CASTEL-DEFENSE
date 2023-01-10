from random import choice
import pygame as py
from configuraciones import *
from auxiliar import Auxiliar
import json

def data(file_path):
    with open(file_path, 'r') as archivo:
        data = json.load(archivo)
    return data

class Character:
    def __init__(self, file_path):
        self.data = data(file_path)
        self.animations = None
        self.animations = {
            key: Auxiliar.create_sides_animation(animation, self.data['type'] + animation['path']) for (key, animation) in self.data['animations'].items()
        }
        self.frame_index = 0
        self.status = self.data['status']
        self.orientation = self.data['orientation']

        self.image = self.animations[self.status][self.orientation][self.frame_index]
        self._rect = self.image.get_rect(topleft=(self.data['x'], self.data['y']))
        self.rects = {
            TOP: py.Rect((self._rect.left, self._rect.top), (self._rect.w - W_H_RECT * 2, W_H_RECT)),
            GROUND: py.Rect((self._rect.left, self._rect.bottom - W_H_RECT), (self._rect.w - W_H_RECT * 2, W_H_RECT)),
            LEFT: py.Rect((self._rect.left, self._rect.top), (W_H_RECT, self._rect.h - W_H_RECT * 2)),
            RIGHT: py.Rect((self._rect.right - W_H_RECT, self._rect.top),
                           (W_H_RECT, self._rect.h - W_H_RECT * 2))
        }

        self.direction = py.math.Vector2(0, 0)
        self.speed = self.data["speed"]
        self.life = True
        self.cd_shot =self.data["cd_shot"]

        self.live = True

        self.time_accumulation_animation = 0
        self.frame_rate_ms = self.data['frame_rate_ms']


    @property
    def rect(self):
        return self._rect
    
    def do_moving(self, delta_ms):
        self.time_accumulation_animation += delta_ms
        if self.time_accumulation_animation >= self.frame_rate_ms:
            self.time_accumulation_animation = 0
            if self.orientation == RIGHT:
                self.direction.x = 1
            elif self.orientation == LEFT:
                self.direction.x = -1
            self.update_position((self.direction.x * self.speed, 0))

    def update(self, delta_ms):
        self.do_animation(delta_ms)
        self.do_moving(delta_ms)


    def do_animation(self, delta_ms):
        self.time_accumulation_animation += delta_ms
        
        if self.time_accumulation_animation >= self.frame_rate_ms:
            self.time_accumulation_animation = 0
            if self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
                self.frame_index = 0
            else:
                self.frame_index += 1
        elif self.frame_index >= len(self.animations[self.status][self.orientation]) - 1:
            self.frame_index = 0

    def update_position(self, pos):
        self._rect = py.Rect.move(self._rect, pos)
        self.rects[TOP].midtop = self._rect.midtop
        self.rects[GROUND].midbottom = self._rect.midbottom
        self.rects[RIGHT].midright = self._rect.midright
        self.rects[LEFT].midleft = self._rect.midleft

    def draw(self, screen):
        try:
            self.image = self.animations[self.status][self.orientation][self.frame_index]
        except IndexError:
            print("ERROR: ", self.status, self.orientation, self.frame_index)
        else:
            screen.blit(self.image, self._rect)
        Auxiliar.debuggerMod(
            screen=screen,
            color_main=RED1,
            color_top=WHITE, 
            color_bottom=WHITE,
            color_left=WHITE,
            color_right=WHITE,
            rect_main=self._rect,
            rects=self.rects
        )