import pygame
from pygame.locals import *
from configuraciones import *
from gui_form import Form
from gui_progressbar import ProgressBar
from gui_widget import Widget

class FormNivel(Form):
    """
    Formulario que maneja el nivel, dependiendo de cual se cargue
    """
    def __init__(self, name, master_surface, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, imagen_background=None, color_background=None, color_border=None, active=False):
        self.name = name
        self.tiempo_juego = 0
        self.puntuacion = 0
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.text1 = Widget(master=self,x=450,y=45,w=25,h=25,color_background=None,color_border=DORADO,image_background=RUTA_IMAGEN + "interface\Marco.png",text=None,font=None,font_size=None,font_color=None)
        self.text2 = Widget(master=self,x=480,y=45,w=25,h=25,color_background=None,color_border=DORADO,image_background=RUTA_IMAGEN + "interface\Marco.png",text=None,font=None,font_size=None,font_color=None)
        self.text3 = Widget(master=self,x=510,y=45,w=25,h=25,color_background=None,color_border=DORADO,image_background=RUTA_IMAGEN + "interface\Marco.png",text=None,font=None,font_size=None,font_color=None)
        self.text4 = Widget(master=self,x=540,y=45,w=25,h=25,color_background=None,color_border=DORADO,image_background=RUTA_IMAGEN + "interface\Marco.png",text=None,font=None,font_size=None,font_color=None)
        self.text5 = Widget(master=self,x=570,y=45,w=25,h=25,color_background=None,color_border=DORADO,image_background=RUTA_IMAGEN + "interface\Marco.png",text=None,font=None,font_size=None,font_color=None)
        self.text6 = Widget(master=self,x=600,y=45,w=25,h=25,color_background=None,color_border=DORADO,image_background=RUTA_IMAGEN + "interface\Marco.png",text=None,font=None,font_size=None,font_color=None)
        self.text7 = Widget(master=self,x=630,y=45,w=25,h=25,color_background=None,color_border=DORADO,image_background=RUTA_IMAGEN + "interface\Marco.png",text=None,font=None,font_size=None,font_color=None)
        self.text8 = Widget(master=self,x=660,y=45,w=25,h=25,color_background=None,color_border=DORADO,image_background=RUTA_IMAGEN + "interface\Marco.png",text=None,font=None,font_size=None,font_color=None)
        self.text9 = Widget(master=self,x=600,y=10,w=100,h=25,color_background=None,color_border=None,image_background=None,text="{0}".format(self.tiempo_juego),font="IMPACT",font_size=30,font_color=WHITE)
        self.text10 = Widget(master=self,x=300,y=10,w=100,h=25,color_background=None,color_border=None,image_background=None,text="{0}".format(self.puntuacion),font="IMPACT",font_size=30,font_color=WHITE)

        self.lista_widget = [self.text1,self.text2,self.text3,self.text4,self.text5,self.text6,self.text7,self.text8,self.text9,self.text10]


    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)    
        

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
        


        