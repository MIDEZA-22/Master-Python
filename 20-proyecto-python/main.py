"""
Proyecto Python y MySQL:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la BD
- Si elegimos login, identificará al usuario y nos preguntará
- Crear nota, mostrar nota, borrar notas
"""
from usuarios import acciones

print("""
ACCIONES DISPONIBLES:

    - registro
    - login
""")

hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()