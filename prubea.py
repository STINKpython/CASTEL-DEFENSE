import json

with open("configutaciones(unidades).json","r") as archivo:
    diccionario = json.load(archivo)
# diccionario["UNIDADES"]

    print(diccionario["UNIDADES"]["soldado_bazuca"]["path_run"])
    print(diccionario['UNIDADES']["soldado_bazuca"]["path_run"])