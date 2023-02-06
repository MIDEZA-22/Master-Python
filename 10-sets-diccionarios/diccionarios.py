"""
DICCIONARIO:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json
"""

persona = {
    "nombre": "Mijail",
    "apellidos": "Zavala",
    "web": "mijailzavala.com"
}

print(persona["apellidos"])

# LISTA CON DICCIONARIOS

contactos = [
    {
        'nombre': 'mijail',
        'email': 'mijail@gmail.com'
    },
    {
        'nombre': 'luis',
        'email': 'luis@gmail.com'
    },
    {
        'nombre': 'salvador',
        'email': 'salvador@gmail'
    }

]

contactos[0]['nombre'] = "Miky"
print(contactos[0]['nombre'])

print("\nListado de contactos: ")
print("***************************************")

for contacto in contactos:
    print(f"\nNombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("***************************************")