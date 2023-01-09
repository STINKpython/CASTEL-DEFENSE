import pygame
from pygame.locals import *
import sys
from configuraciones import *
from UI.gui_manager import *
from soldier_bazuka import Soldier_rifle
from mars import Enemy_mars

flags = DOUBLEBUF 
PANTALLA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

juego = FormManager(PANTALLA)

timer_1s = pygame.USEREVENT + 0
pygame.time.set_timer(timer_1s,1000)

soldadito = Soldier_rifle()
enemy = Enemy_mars(300,330)

while True:     
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    delta_ms = clock.tick(FPS)

    juego.actualizar_forms(events)

    soldadito.update(delta_ms,events,enemy.rects["LEFT"])
    soldadito.draw(PANTALLA)
    #soldadito.detect_object()

    enemy.update(delta_ms)
    enemy.draw(PANTALLA)
    
    pygame.display.flip()