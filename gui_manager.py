from pygame.locals import *
from configuraciones import *
from gui_nivel import FormNivel


class FormManager():
    """
    Formulario manager que crea los demas formularios, los actualiza y dibuj, asi como tambien se fija cual mostrar en pantalla
    """
    def __init__(self,pantalla) -> None:
        self.pantalla = pantalla
        self.form_nivel_1 = self.crear_nivel("nivel_1",RUTA_IMAGEN + "fondo/MetalSlug-Mission2.jpg")
        self.niveles = [self.form_nivel_1]

    def crear_nivel(self,nivel,fondo):
        """
        Este metodo se encarga de crear el formulario nivel
        Parametros: recibe un str que representa la clave del nivel a crear
        Retorna: un objeto que representa al formulario del nivel
        """
        return FormNivel(name=nivel,master_surface = self.pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,imagen_background=fondo,color_background=BLACK,color_border=BLACK,active=True)


    def actualizar_forms(self,eventos):
        """
        Este metodo se encarga de actualizar y dibujar el formulario que este activo
        Parametros: una lista de eventos, teclas, sonidos, tambien un valor delta_ms, y un evento de usuario de tiempo
        """
        
        if(self.form_nivel_1.active):
            self.form_nivel_1.update(eventos)
            self.form_nivel_1.draw()