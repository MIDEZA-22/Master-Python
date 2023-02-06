"""
EJERCICIO 5.Crear una lista con el contenido de esta tabla:
ACCION      AVENTURA            DEPORTES
GTA         ASSINS              FIFA 21
COD         CRASH               PRO 21
PUGB        PRINCE OF PERSIA    MOTO GP 21

Mostrar esta información ordenada
"""
tabla =[
    {
        "categoria": "ACCIÓN",
        "juegos": ["GTA", "Call of Duty", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSAINS", "Crash Bandicoot", "Prinde of Persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PES 21", "MOTO GP 21"]        
    }
]

for categoria in tabla:
    print(f"--------{categoria['categoria']}--------")
    for juego in categoria['juegos']:
        print(juego)