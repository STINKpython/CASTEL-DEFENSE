from auxiliar import Auxiliar
import pygame
from configuraciones import *
from bazuka_shot import Bazuca_shot
import json

DEBUG=True

class Soldier_rifle:

    def __init__(self, x, y):

        # Animaciones
        data = self.call_json()
        
        
        self.run = Auxiliar.getSurfaceFromSpriteSheet(
            data['UNIDADES']["soldado_bazuca"]["path_run"], 11, 1, True, 1, 1)[:6]
        self.atack = Auxiliar.getSurfaceFromSpriteSheet(
            data["UNIDADES"]["soldado_bazuca"]["path_atack"],8,1, True,1,1)
        
        self.frame = 0
        self.animation = self.run
        self.image = self.animation[self.frame]
        # Movimientos y rectangulos
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


        self.rect_radar = pygame.Rect(self.rect.x+170, self.rect.y, 20, 40)
        self.rect_gun_point = pygame.Rect(self.rect.x+40,self.rect.y+40,10,10)
        # funciones
        self.live = True
        self.life = data["UNIDADES"]["soldado_bazuca"]["life"]
        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_bullet = 0
        self.frame_rate_ms =data["UNIDADES"]["soldado_bazuca"]["frame_rate_ms"]
        self.cd_shot =data["UNIDADES"]["soldado_bazuca"]["cd_shot"]

        # acciones
        self.atacar = False
        self.shoot_list = []

    def call_json(self):

        with open("configutaciones(unidades).json","r") as archivo:
            diccionario = json.load(archivo)
            return diccionario

    def move_x(self,speed=1):

        self.rect.x += speed
        self.rect_radar.x += speed
        self.rect_gun_point.x +=speed

    def move_y(self,speed=0):

        self.rect.y += speed

    def actions(self, delta_ms, lista_eventos,objeto):

        
        self.detect_object(objeto)
        self.ataque(delta_ms)

    def detect_object(self, objeto):

        if self.rect_radar.colliderect(objeto):
            self.atacar = True
            self.frame=0
            self.animation = self.atack
            self.move_x(0)
            self.rect.y +40
            self.frame_rate_ms=7
        else:
            self.move_x()
            self.animation = self.run
        
    def ataque(self,delta_ms):

        self.tiempo_transcurrido_bullet+=delta_ms
        if self.atacar:    
            if self.tiempo_transcurrido_bullet>self.cd_shot:

                self.animation = self.atack           
                self.shoot_list.append(Bazuca_shot(self.rect_gun_point.x,self.rect_gun_point.y-10))
                self.tiempo_transcurrido_bullet=0
          

    def update(self, delta_ms, lista_eventos,objeto):

        self.tiempo_transcurrido = 0
        
        if self.live:
            self.actions(delta_ms, lista_eventos,objeto)
          
            self.tiempo_transcurrido += delta_ms
            if self.tiempo_transcurrido > self.frame_rate_ms:
                if (self.frame < len(self.animation) - 1):
                    self.frame += 1
                else:
                    self.frame = 0
        
    def draw(self, screen):

        if self.live:

            if DEBUG:
                pygame.draw.rect(screen,BLUE2,self.rect_radar)
                pygame.draw.rect(screen,GREEN2,self.rect_gun_point)

            self.image = self.animation[self.frame]
            screen.blit(self.image, self.rect)

            if len(self.shoot_list)>0:
                for e in self.shoot_list:
                    
                    e.update()
                    e.draw(screen)
                    if not(e.live):
                        self.shoot_list.remove(e)
        

