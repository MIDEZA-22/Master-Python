from io import open
import pathlib
import shutil

# ABRIR ARCHIVO
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt" #RUTA ABSOLUTA str(pathlib.Path().absolute()) es el lugar donde estan se esta trabajando los scripts
archivo = open(ruta, "a+")

# ESCRIBIR
archivo.write("****Mijail Denis Zavala Llanco****\n")

#CERRAR ARCHIVO
archivo.close()

# ABRIR ARCHIVO
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r+")

# LEER CONTENIDO
#contenido = archivo_lectura.read()
#print(contenido)

# LEER CONTENIDO Y GUARDAR EN LISTA
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for frase in lista:
   #lista_frase = frase.split()
   #print(lista_frase)
    print("- "+frase.center(50))

# COPIAR
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado88.txt"

shutil.copyfile(ruta_original, ruta_alternativa)
"""

# MOVER/RENOMBRAR
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

# ELIMINAR
import os
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""

# COMPROBAR SI EXISTE DIRECTORIO
import os.path

#print(os.path.abspath("../"))  RUTA ABSOLUTA QUE NO NECESITA CONVERTIR A STR
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt" #RUTA ABSOLUTA
ruta_comprobar = "./ficheros.py" #RUTA RELATIVA

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")