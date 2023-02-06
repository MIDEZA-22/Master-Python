"""
Ejercicio 7. Hacer un programa que muestre todos los numeros impares
entre dos numeros que decida el usuario.
"""

numero1 = int(input("\nIngrese el primero número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 < numero2:

    for contador in range(numero1+1, numero2):
        
        if contador % 2 != 0:

            print(contador)

else:
    
    print("\nEl primer número tiene que ser menor")