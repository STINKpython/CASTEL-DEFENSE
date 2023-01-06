from colors import *
# VENTANA
ANCHO_VENTANA = 900
ALTO_VENTANA = 500

# CORDENADA DEL PISO
NIVEL_PISO = 552
NIVEL_TECHO = 50

# FOTOGRAMAS POR SEGUNDO
FPS = 120

# RUTA DE IMAGENES
RUTA_IMAGEN = './recursos/'  # RUTA DE IMAGENES
PATH_FRAME_UNIT_IMAGE = 'recursos/interface/Marco.png'
PATH_GOLD_COIN = 'recursos/interface/Moneda.png'

PATHS_UNITIES = {
    0: 'recursos/unidades/soldiers/Rebel Soldier Bazooka ico.png',
    1: 'recursos/unidades/soldiers/Rebel Soldier Helicopter Ico.png',
    2: 'recursos/unidades/soldiers/Rebel Soldier Icon.png',
    3: 'recursos/unidades/soldiers/Rebel Soldier Mini-Gun Ico.png',
    4: 'recursos/unidades/soldiers/Rebel Soldier Rifle Ico.png',
    5: 'recursos/unidades/soldiers/Rebel Soldier Shield Ico.png',
    6: 'recursos/unidades/soldiers/Rebel Soldier Tank Ico.png'
}

# DIRECCION DONDE MIRA EL PERSONAJKE
IZQUIERDA = -1
DERECHA = 1

# SIZES
SIZE_FRAME_UNITY = (1/28*ANCHO_VENTANA, 1/16*ALTO_VENTANA)
SPACE_BETWEEN_FRAMES = 3 / 70 * ANCHO_VENTANA
SIZE_FONT_TIME = 30
SIZE_TIME = (100, 25)
SIZE_FONT_GOLD = 30
SIZE_GOLD = (100, 25)


# AMOUNTS

AMOUNT_UNITIES = 7

# POSITIONS
POS_FRAME_UNITY = (9/14*ANCHO_VENTANA, 9/80*ALTO_VENTANA)
POS_TIME = (1/3*ANCHO_VENTANA, 1/50*ALTO_VENTANA)
POS_GOLD = (7/9*ANCHO_VENTANA, 1/50*ALTO_VENTANA)
POS_GOLD_ICON = (2/3*ANCHO_VENTANA, 1/50*ALTO_VENTANA)



# TAMAÑO DE COLLIDERECT
ALTURA_PIES = 8  #  Aprox Gravedad/2 + 1

# MODO DEBUG // DIBUJAR RECTANGULOS
DEBUG = False

# ESTADOS
M_STATE_NORMAL = 1
M_STATE_HOVER = 2
M_STATE_CLICK = 3
M_BRIGHT_HOVER = 1
M_BRIGHT_CLICK = 2

# TILED
PLATAFORMA = "P"
PISO = "O"
MURO = "M"
LOOT = "B"
CAJA = "C"
PINCHO = "S"
FONDO_ACIDO = "A"
TOP_ACIDO = "T"
MOBILE = "U"

CORAZON = RUTA_IMAGEN + r"Menu/Button/Health_Dot.png"
BALA = RUTA_IMAGEN + r"Menu/Button/Armor_Bar_Dot.png"
