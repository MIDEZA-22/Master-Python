"""
#BUCLE WHILE
Estructura de control que itera o repite la ejecución de una
serie de instrucciones tantas veces como sea necesario,
hasta que deja de cumplirse la condición.

while condición:
    bloque de instrucciones
    actualización de contador

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1

print("--------------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

# Ejemplo

print("\n*** EJEMPLO ***")
numero_usuario = int(input("\n¿De que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n*** Tabla del {numero_usuario} ***")

contador = 1
while contador <= 12:
    print(f"{numero_usuario} X {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print("\nTabla finalizada...")