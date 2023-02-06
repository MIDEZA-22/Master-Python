"""
EJERCICICO 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuleva un string
- Ordenar y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

#CREAR LA LISTA
numeros = [1, 5, 3, 7, 4, 6, 2, 8]

# CREAR FUNCION QUE RECORRA LISTA Y DEVUELVA STRING
def mostrar_lista(lista):
    resultado = ""
    
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado

# RECORRER Y MOSTRAR
print("***RECORRER Y MOSTRAR***")

"""
for numero in numeros:
    print(numero)
"""

print(mostrar_lista(numeros))
print(mostrar_lista(numeros))
print(mostrar_lista(["Mijail", "Diana", "Deysi"]))

# ORDENAR Y MOSTRAR
print("***ORDENAR Y MOSTRAR***")
numeros.sort()
print(mostrar_lista(numeros))

# MOSTRAR SU LONGITUD
print("***MOSTRAR SU LONGITUD***")
print(len(numeros))

# BUSQUEDA EN LA LISTA
try:
    print("***BUSQUEDA EN LA LISTA***")

    busqueda = int(input("Introduce el numero: "))

    comprobrar = isinstance(busqueda, int)
    while not comprobrar or busqueda <= 0:
        busqueda = int(input("Introduce el numero: "))
    else:
        print(f"Has introducido el {busqueda}")

    print(f"***Buscar en la lista el numero {busqueda}***")

    search = numeros.index(busqueda)
    print(f"El numero buscado existe en la lista, es el indice: {search}")
except:
    print("El numero no esta en la lista")