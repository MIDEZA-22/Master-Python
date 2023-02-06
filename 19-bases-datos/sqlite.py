# IMPORTAR MODULO
import sqlite3

# CONEXION
conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

# CREAR CURSOR
cursor = conexion.cursor()

# CREAR TABLA
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT, 
    precio INT(255)
);
""")

# GUARDAR CAMBIOS
conexion.commit()

# INSERTAR DATOS
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Segundo producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

# BORRAR REGISTROS
cursor.execute("DELETE FROM productos")
conexion.commit()

# INSERTAR MUCHOS REGISTROS DE GOLPE
productos = [
    ("Ordenador portatil", "Buena PC", 700),
    ("Telefono movil", "Buena telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet 15", "Buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

# UPDATE
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

# LISTAR DATOS
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

# CERRAR CONEXION
conexion.close()