import pygame as py
from configuraciones import *
from UI.gui_widget import Widget


class Gold(Widget):
    def __init__(self, master):
        self.__gold = '000000'
        self.master = master
        super().__init__(
            master_form=master,
            pos=POS_GOLD,
            size=SIZE_GOLD,
            text="{0}".format(self.__gold),
            font="IMPACT",
            font_size=SIZE_FONT_GOLD,
            font_color=WHITE
        )
        self.__image_coin = py.image.load(PATH_GOLD_COIN)        
        self.__image_coin = py.transform.rotozoom(self.__image_coin, 0, 1.5).convert_alpha()
        self.__pos_image_coin = POS_GOLD_ICON
        self._rect = self.__image_coin.get_rect(topleft=self.__pos_image_coin)

        
    def render(self):
        if DEBUG:
            py.draw.rect(self.master.imagen_bg, GOLD1, self._rect)
        self.master.imagen_bg.blit(self.__image_coin, self.__pos_image_coin)
        super().render()

        
        
    def update(self, lista_eventos):
        self.render()