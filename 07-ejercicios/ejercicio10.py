"""
Ejercicio 10.El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han desaprobado.
"""

contador = 1    
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno {contador}\"?: "))

    if nota >= 11:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1

print(f"\nAlumndos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")
