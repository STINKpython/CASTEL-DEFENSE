from configuraciones import *
from auxiliar import Auxiliar
import pygame as py

class Bazuca_shot():

    def __init__(self, x, y):

        self.shot = Auxiliar.getSurfaceFromSpriteSheet(
            r"recursos/unidades/sodlado_bazuca/Shoot_bullet.png", 4, 1)
        self.boom = Auxiliar.getSurfaceFromSpriteSheet(
            r"recursos/unidades/sodlado_bazuca/Shoot_boom.png", 15, 5)

        self.frame = 0
        self.animation = self.shot
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 50
        self.live = True
        self.trayectoria = 0

    def move_x(self, speed=3):

        self.rect.x += speed
        self.trayectoria += speed

    def detecta_objeto(self, objeto):

        if self.rect.colliderect(objeto):
            self.animation = self.boom

    def state(self):

        if self.rect.x > ANCHO_VENTANA:
            self.live = False

    def update(self):

        if self.live:
            self.move_x()

            # self.detecta_objeto()
            self.state()

    def draw(self, screen):
        if self.live:
            screen.blit(self.image, self.rect)
        if DEBUG:
            py.draw.rect(screen, GREENYELLOW, self.rect)