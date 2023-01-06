import pygame
from configuraciones import *
from pygame.locals import *


class Form:
    forms_dict = {}

    def __init__(self, name, master_surface, pos, size, color_bg, imagen_bg, color_border, active):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.pos = pygame.math.Vector2(pos)
        self.size = size
        self.color_bg = color_bg
        self.color_border = color_border
        self.imagen_bg = imagen_bg

        self.surface = pygame.Surface(size)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect = self.surface.get_rect(topleft=pos)
        self.active = active

        if self.imagen_bg is not None:
            self.imagen_bg = pygame.image.load(imagen_bg)
            self.imagen_bg = pygame.transform.scale(
                self.imagen_bg, size).convert_alpha()
            self.surface = self.imagen_bg
        elif self.color_bg is not None:
            self.surface.fill(self.color_bg)

    def set_active(self, name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def render(self):
        pass

    def update(self, list_event):
        pass

    def draw(self):
        self.master_surface.blit(self.surface, self.slave_rect)
