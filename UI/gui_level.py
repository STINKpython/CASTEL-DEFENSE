import pygame
from configuraciones import *
from UI.gui_form import Form

from UI.gui_frame_unity import FrameUnity
from UI.gui_time import Time
from UI.gui_gold import Gold


def create_pos_frame(increase):
    return pygame.math.Vector2(POS_FRAME_UNITY[0] + increase * SPACE_BETWEEN_FRAMES, POS_FRAME_UNITY[1])


class Level(Form):
    """
    Formulario que maneja el nivel, dependiendo de cual se cargue
    """

    def __init__(
        self,
        name,
        master_surface,
        imagen_bg=None,
        color_bg=None,
        color_border=None,
        active=False
    ):

        self.name = name
        self.pos = pygame.math.Vector2(0, 0)

        super().__init__(
            name,
            master_surface,
            self.pos,
            (ANCHO_VENTANA, ALTO_VENTANA),
            color_bg,
            imagen_bg,
            color_border,
            active
        )

        self.frames = [
            FrameUnity(self, create_pos_frame(i), SIZE_FRAME_UNITY) for i, frame in enumerate(range(AMOUNT_FRAMES_UNITIES))
        ]

        self.time = Time(self, POS_TIME, SIZE_TIME)
        self.gold = Gold(self, POS_GOLD, SIZE_GOLD)

        self.lista_widget = []
        self.lista_widget.extend(self.frames)
        self.lista_widget.extend([self.time, self.gold])

    def update(self, list_event):
        for aux_widget in self.lista_widget:
            aux_widget.update(list_event)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:
            aux_widget.draw()
