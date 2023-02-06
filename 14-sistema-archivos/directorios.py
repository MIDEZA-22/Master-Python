import os
import shutil

# CREAR CARPETA
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# COPIAR
"""
ruta_original = "./mi_carpeta"
ruta_nueva =  "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""

# ELIMINAR
"""
os.rmdir('./mi_carpeta_COPIADA')
"""

print("CONTENIDO DE MI CARPETA")
contenido = os.listdir("./mi_carpeta")

for fichero in contenido:
    print("Fichero: " + fichero)