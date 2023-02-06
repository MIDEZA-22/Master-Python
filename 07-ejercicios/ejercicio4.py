"""
Ejercicio 4. Pedir dos numero al usuario y hacer todas las
operaciones básicas de una calculadora y mostrarlo por pantalla.
"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print("\n***CALCULADORA ***")
print(f"\nLa suma es: {str(numero1+numero2)}")
print(f"La resta es: {str(numero1-numero2)}")
print(f"La multiplicación es: {str(numero1*numero2)}")
print(f"La división es: {str(numero1/numero2)}")