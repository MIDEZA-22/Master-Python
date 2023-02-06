""" 
FUNCION:
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la función tantas veces como sea necesario.

def nombre_funcion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombre_funcion(mi_parametro)
nombre_funcion(mi_parametro)

"""

# EJEMPLO 1: FUNCIONES
print("***** EJEMPLO 1 *****")

# DEFINIR FUNCION
def muestraNombre():
    print("Mijail")
    print("Juan")
    print("Carlos")
    print("Nestor")
    print("Ivan")
    print("Ronaldo")
    print("\n")

# INVOCAR FUNCION
muestraNombre()
muestraNombre()
muestraNombre()

# EJEMPLO 2: PARAMETROS
"""
print("***** EJEMPLO 2 *****")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Es mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)
"""

# EJEMPLO 3
print("***** EJEMPLO 3 *****")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(1, 11):
        operacion = numero*contador
        print(f"{numero} X {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(7)
tabla(12)

# EJEMPLO 3.1
print("***** EJEMPLO 3.1 *****")

for numero_tabla in range (1, 11):
    tabla(numero_tabla )

# EJEMPLO 4
print("***** EJEMPLO 4 *****")

# PARAMETROS OPCIONALES

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Mijail", 70179048)

# EJEMPLO 5: RETURN O DEVOLVER DATOS
print("\n***** EJEMPLO 5 *****")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Mijail"))

# EJEMPLO 6
print("\n***** EJEMPLO 6 *****")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)
    
    return cadena

print(calculadora(5, 5))

# EJEMPLO 7
print("\n***** EJEMPLO 7 *****")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Mijail", "Zavala Llanco"))

# EJEMPLO 8: FUNCION LAMBDA
print("\n***** EJEMPLO 8 *****")

dime_el_year = lambda year: f"El año es: {year}"
 
print(dime_el_year(2034))
