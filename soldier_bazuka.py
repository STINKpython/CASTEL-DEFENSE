import pygame
from configuraciones import *
from bazuka_shot import Bazuca_shot
from character import Character


class SoldierRifle(Character):
    def __init__(self):
        super().__init__('data.json')

        self.rect_radar = pygame.Rect(self.rect.x+170, self.rect.y, 20, 40)
        self.rect_gun_point = pygame.Rect(
            self.rect.right, self.rect.centery, 10, 10)
        # funciones
        self.tiempo_transcurrido_bullet = 0

        # acciones
        self.atacar = False
        self.shoot_list = []

    def move_x(self, speed=1):
        self.rect_radar.x += speed
        self.rect_gun_point.x += speed

    def move_y(self, speed=0):
        self.rect.y += speed

    def actions(self, delta_ms, lista_eventos, objeto):
        self.detect_object(objeto)
        self.ataque(delta_ms)

    def detect_object(self, objeto):
        if self.rect_radar.colliderect(objeto):
            self.atacar = True
            self.frame = 0
            self.move_x(0)
            self.speed = 0
            self.status = 'atack'
            self.frame_rate_ms = 250

        else:
            self.move_x()
            self.status = 'run'

    def ataque(self, delta_ms):
        self.tiempo_transcurrido_bullet += delta_ms
        if self.atacar:
            if self.tiempo_transcurrido_bullet > self.cd_shot:
                self.shoot_list.append(Bazuca_shot(
                    self.rect.right, self.rect_gun_point.y))
                self.tiempo_transcurrido_bullet = 0

    def update(self, delta_ms, lista_eventos, objeto):
        if self.live:
            self.actions(delta_ms, lista_eventos, objeto)
            super().update(delta_ms)

    def draw(self, screen):
        if self.live:
            super().draw(screen)
            if DEBUG:
                pygame.draw.rect(screen, GREEN, self.rect_radar)
                pygame.draw.rect(screen, GRAY, self.rect_gun_point)

            if len(self.shoot_list) > 0:
                for e in self.shoot_list:
                    e.update()
                    e.draw(screen)
                    if not (e.live):
                        self.shoot_list.remove(e)
