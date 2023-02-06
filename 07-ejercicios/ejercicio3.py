"""
Ejercicio 3. Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros numeros
naturales. Resolviendo con for y con while
"""
print("\nFOR")
print("-----")

for numero in range (0, 61):
    cuadrado = numero * numero
    print(cuadrado)

print("\n*****")

print("\nWHILE")
print("-----")

contador = 0

while contador <= 60:
    cuadrado = contador * contador
    print(cuadrado) 

    contador += 1