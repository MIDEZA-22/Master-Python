"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un único
nombre.
Para acceder a esos valores podemos usar un indice númerico.
"""

pelicula = "Batman"

# DEFINIR LISTA
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))
years = list(range(2020, 2050))
variada = ["Mijail", 30, 4.4, True, "Texto"]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# INDICES
pelicula = "otra cosa"
peliculas[1] = "Gran torino"
peliculas[2] = "El hobbit"
print(peliculas)

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])

# AÑADIR ELEMENTO A LISTA
cantantes.append("Kase O")
cantantes.append("Natos")
print(cantantes)

# RECORRER LISTA
"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n**PELICULAS**")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
"""

#LISTAS MULTIDIMENSIONALES
print("\n**********LISTADO DE CONTACTOS**********")
contactos = [
    [
        'Antonio',
        'antonio@gmail.com'
    ],
    [
        'Luis',
        'luis@gmail.com'
    ],
    [
        'Salvador',
        'salvador@gmail.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)  
        else:
            print("Email: " + elemento)
    print("\n") 
    
# print(contactos[1][1])


