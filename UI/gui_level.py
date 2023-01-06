import pygame
from configuraciones import *
from UI.gui_form import Form

from UI.gui_unity import Unity
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

        self.unities = [
            Unity(self, create_pos_frame(i), i) for i, unity in enumerate(range(AMOUNT_UNITIES))
        ]
        self.imagen_b2 = self.imagen_bg

        self.time = Time(self)
        self.gold = Gold(self)

        self.lista_widget = []
        self.lista_widget.extend(self.unities)
        self.lista_widget.extend([self.time, self.gold])
        

    def update(self, list_event):
        for aux_widget in self.lista_widget:
            aux_widget.update(list_event)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:
            aux_widget.draw()
