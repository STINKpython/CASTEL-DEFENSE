import pygame
from configuraciones import *

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas, flip=False, step=1, scale=1):

        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width() / columnas)
        fotograma_alto = int(surface_imagen.get_height() / filas)
        fotograma_ancho_scaled = int(fotograma_ancho * scale)
        fotograma_alto_scaled = int(fotograma_alto * scale)
        x = 0

        for fila in range(filas):
            for columna in range(0, columnas, step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
                if scale != 1:
                    surface_fotograma = pygame.transform.scale(surface_fotograma, (
                    fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha()
                if flip:
                    surface_fotograma = pygame.transform.flip(surface_fotograma, True, False).convert_alpha()
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format, quantity, flip=False, step=1, scale=1, w=0, h=0, repeat_frame=1):
        lista = []
        for i in range(1, quantity + 1):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if scale == 1 and w != 0 and h != 0:
                surface_fotograma = pygame.transform.scale(surface_fotograma, (w, h)).convert_alpha()
            if scale != 1:
                surface_fotograma = pygame.transform.scale(surface_fotograma, (
                fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha()
            if flip:
                surface_fotograma = pygame.transform.flip(surface_fotograma, True, False).convert_alpha()

            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def debuggerMod(screen, color_main, color_top, color_bottom, color_left, color_right, rect_main, rects):
        if DEBUG:
            pygame.draw.rect(screen, color_main, rect_main)
            pygame.draw.rect(screen, color_top, rects[TOP])
            pygame.draw.rect(screen, color_bottom, rects[GROUND])
            pygame.draw.rect(screen, color_left, rects[LEFT])
            pygame.draw.rect(screen, color_right, rects[RIGHT])
    
    @staticmethod
    def create_side_animation(data, path, side):
        return Auxiliar.getSurfaceFromSpriteSheet(path, data['cols'], data['rows'], data[side])

    @staticmethod
    def create_sides_animation(data, path):
        return {
            RIGHT: Auxiliar.create_side_animation(data, path, RIGHT),
            LEFT: Auxiliar.create_side_animation(data, path, LEFT)
        }
