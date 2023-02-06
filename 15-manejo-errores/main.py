# CAPTURAR EXCEPCIONES Y MANEJO DE ERRORES EN CODIGO
# SUSCEPTIBLE A FALLOS/ERRORES

"""
try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, ingrese un nombre correcto...")
else: 
    print("TODO ESTA CORRECTO!!!...")
finally:
    print("FIN")
"""

# MANEJAR MULTIPLES EXCEPCIONES
"""
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el codigo")
#except ValueError:
#   print("Introduce un numero correcto")
except Exception as error: # MULTIPLES EXCEPSIONES
    print(type(error))
    print("Ha ocurrido un error: ", type(error).__name__)
"""

# EXCEPCIONES PERSONALIZADAS O LANZAR EXCEPCION

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real") # raise GENERA UN ERROR
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta incompleto")
    else:
        print(f"Bienvenido {nombre}")
except ValueError: #2 Si se pone un tipo de error solo captura ese error nada mas
    print("Introduce los datos correctamente")
except Exception as error: #2 Exception coge los errores en general
    print("Existe un error", error)
