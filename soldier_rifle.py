from auxiliar import Auxiliar
import pygame

class Soldier_rifle:

    def __init__(self,x,y):

        # Animaciones
        self.run = Auxiliar.getSurfaceFromSpriteSheet("unidades/soldier/run and point.png",8,1,False,1,1)[:6]
        self.atack =  Auxiliar.getSurfaceFromSpriteSheet("unidades/soldier/run and point.png",8,1,False,1,1)[6:8]       
        self.frame = 0
        self.animation = self.run
        self.image = self.animation[self.frame]
        # Movimientos y rectangulos
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_radar =  pygame.Rect(self.rect.x,self.rect.y,100,10)
        #funciones
        self.live=True
        self.life=100
        self.tiempo_transcurrido = 0
        self.frame_rate_ms = 300

    def move_x(self):
        self.rect.x += 5

    def move_y(self):
        self.rect.y += 0

    def actions(self,delta_ms,lista_eventos):
        
        self.animation=self.run
        self.move_x()


    def update(self,delta_ms,lista_eventos):
        self.tiempo_transcurrido = 0

        if self.live:
            self.actions(delta_ms,lista_eventos)
            self.tiempo_transcurrido += delta_ms
        
            if self.tiempo_transcurrido > self.frame_rate_ms:  
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1               
                else: 
                    self.frame = 0 

    def draw(self,screen):

        if self.live:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
