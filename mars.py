import pygame
from auxiliar import Auxiliar
from configuraciones import *

class Enemy_mars():

    def __init__(self, x, y):

        self.iddle = Auxiliar.getSurfaceFromSpriteSheet(
            r"recursos\unidades\mars people\mars_idle3.png",16, 3)[:16]

        self.frame = 0
        self.animation = self.iddle
        self.image = self.animation[self.frame]

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.rects = {
            "TOP": pygame.Rect((self.rect.left, self.rect.top), (self.rect.w - W_H_RECT * 2, W_H_RECT)),
            "GROUND": pygame.Rect((self.rect.left, self.rect.bottom - W_H_RECT), (self.rect.w - W_H_RECT * 2, W_H_RECT)),
            "LEFT": pygame.Rect((self.rect.left, self.rect.top), (W_H_RECT, self.rect.h - W_H_RECT * 2)),
            "RIGHT": pygame.Rect((self.rect.right - W_H_RECT, self.rect.top),
                           (W_H_RECT, self.rect.h - W_H_RECT * 2))
        } 

        self.tiempo_transcurrido = 0

        self.frame_rate_ms = 8.9



    def draw(self, screen):

        pygame.draw.rect(screen,RED1,self.rects["LEFT"])
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

    def update(self, delta_ms):

        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido += delta_ms

        if self.tiempo_transcurrido > self.frame_rate_ms:
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0

    def ataque(self):
        pass

    def detectar_objetos(self):
        pass

    def move_x(self):
        pass

    def move_y(self):
        pass

    