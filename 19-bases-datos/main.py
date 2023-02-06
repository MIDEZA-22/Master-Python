import mysql.connector #3 Importar mysql.connector para realizar la conexión con MYSQL

# CONEXION
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python" #3 Se pone database siempre en cuando ya esta creado la BD sino NO
)

# ¿LA CONEXION HA SIDO CORRECTA?
# print(database)

# CURSOR
cursor = database.cursor(buffered=True) #2 buffered permite usar varias veces el cursor y no salgue error

# CREAR BASE DE DATOS
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES") #3 Mostrar la BDs - SHOW DATABASES

for bd in cursor:
    print(bd)
"""

# CREAR TABLAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id) #3 Asignar llave principal
)
""")

"""
cursor.execute("SHOW TABLES") #3 Mostrar las tablas

for table in cursor:
    print(table)
"""

# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

#5 INSERTAR VARIOS REGISTROS A LA VES
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000), 
    ('Mercedes', 'Clase C', 35000)
]

# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)

database.commit()

# LISTAR
cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall() #3 fetchall muestra todas las filas del registro

print("----TODOS MIS COCHES----")
for coche in result:
    print(coche[1], coche[2], coche[3])

cursor.execute("SELECT * FROM vehiculos")
cursor.fetchone() #3 fetchone muestra solo la primera fila del registro
print(coche)

# BORRAR
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount, "borrados¡¡") #2 Mostrar registros borrados

# ACTUALIZAR
cursor.execute("UPDATE vehiculos SET modelo='León' WHERE marca='Seat'") #3 SET es para cambiar algo
database.commit()

print(cursor.rowcount, "actualizados¡¡")


#4 Cada ves que se hague modificación de la BD, guardar con database.commit()
