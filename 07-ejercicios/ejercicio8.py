"""
Ejercicio 8. ¿Cuanto es el X por ciento de X número?.
"""

numero = int(input("Introduce un número: "))
porcentaje = int(input("Introduce un porcentaje"))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es: {operacion}")