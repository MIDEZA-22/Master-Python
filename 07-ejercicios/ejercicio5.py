"""
Ejercicio 5. Hacer un programa que muestre todos los numeros entre
dos numeros que diga el usuario.
"""

numero1 = int(input("\nIngrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 < numero2:
    
    for contador in range(numero1+1, numero2):
        print (contador)

else:
    print("\nEl primer numero tiene que ser menor")
