"""
Modulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje, 
modulos en internet, y tambien creaer nuestros modulos
"""

# Importar modulo propio

# import mimodulo
# from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("Mijail Denis"))
#print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Mijail Denis"))
print(calculadora(3, 5, True))

# MODULO FECHAS

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())

# MODULO MATEMATICAS
import math

print("La raiz cuadrada de 10: ", math.sqrt(10))

print("Numero pi: ", float(math.pi))

print("Redondear: ", math.floor(6.25314677)) # floor redondeo a la baja y ceil a la alta

# MODULO RANDOM

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))

