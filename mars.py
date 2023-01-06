import pygame
from auxiliar import Auxiliar


class Enemy_mars():

    def __init__(self, x, y):

        self.iddle = Auxiliar.getSurfaceFromSpriteSheet(
            r"recursos/unidades/mars people/mars_idle.png", 17, 3)[:16]

        self.frame = 0
        self.animation = self.iddle
        self.image = self.animation[self.frame]

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.tiempo_transcurrido = 0
        self.frame_rate_ms = 8.8889

    def draw(self, screen):

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
