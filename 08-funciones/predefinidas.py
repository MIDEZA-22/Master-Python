nombre = "MIJAIL DENIS"

#FUNCIONES GENERALES
print(type(nombre))

#DETECTAR EL TIPADO
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

#LIMPIAR ESPACIOS

frase = "     mi contenido"
print(frase)
print(frase.strip())

#ELIMINAR VARIABLES
year = 2021
print(year)
del year
#print(year)

#COMPROBAR VARIABLES VACIA
texto = " ff "

if len(texto) <= 0:
    print("La variable esta vacia")
else: 
    print("La variable tiene contenido: ", len(texto))

#ENCONTRAR CARACTERES
frase = "La vida es bella"
print(frase.find("vida"))

#REEMPLAZAR PALABRAS EN UN STRING
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#MAYUSCULAR Y MINUSCULAS
print(nombre)
print(nombre.lower())
print(nombre.upper())