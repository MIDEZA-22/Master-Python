from flask import Flask, flash, request, url_for, redirect, render_template  #az Importar el módulo de flask | render_template sirve para trabajar con plantillas
from datetime import datetime #az Importar el módulo de fechas
from flask_mysqldb import MySQL #az Importar MySQL, para trabajar con la BD

#r Crear la app de flask

app = Flask(__name__) 

#r Crear clave secretas para las sesiones (PARA QUE FUNCIONE BIEN LOS MENSAJES FLASH)

app.secret_key = 'clave_secreta_flask' #az Puede ser cualquier mensaje

#R Conexión con la BD MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)

#r Context processor

@app.context_processor #az Decorador
def date_now():

    return{
        'date': datetime.utcnow() #az utcnow() es una función que va a devolver varias propiedades. Se podra acceder a la hora, al año, etc.
    }

#r Creación de rutas: EL NOMBRE DE LA RUTA ESTA VINCULADA A LA FUNCION

@app.route('/') #az '/' es la ruta inicial o por defecto cuando se abra el proyecto
def index():

    edad = 101
    personas = ['Victor', 'Paco', 'Francisco', 'David']

    return render_template('index.html', #az Redirigir a la plantilla 'index.html'
        dato1="Valor",
        dato2="Valor2",
        lista=["uno","dos","tres"],
        edad=edad,
        personas=personas
    ) 
 
#az Se puede crear varias rutas para una misma función
@app.route('/informacion') #az Ruta con parametro opcionales
@app.route('/informacion/<string:nombre>') #az Ruta con parametro obligatorios
@app.route('/informacion/<string:nombre>/<apellidos>') #az Ruta con parametro obligatorios
def informacion(nombre = None, apellidos = None): #az Nombre y apellidos por default
    
    texto = ""

    if nombre != None and apellidos != None:
        texto = f"Bienvenido, {nombre} {apellidos}"
    
    return render_template('informacion.html', texto = texto) #az Redirigir a la plantilla 'informacion.html'. Renderizando la plantilla con la informacióm de todas las variables que se les pasa 

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):

    if redireccion is not None:

        return redirect(url_for('lenguajes')) #az Redirigir a otra ruta: Primero importar el módulo de "redirect"
        
    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():

    #s return "<h1>Página de lenguajes</h1>"
    return render_template('lenguajes.html')

@app.route('/crear-coche', methods=['GET','POST']) #az Se puede usar dos métodos en una misma ruta
def crear_coche():

    if request.method == 'POST':

        #az Se recogen los datos que vienen por el método POST
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        #az Crear el cursor
        cursor = mysql.connection.cursor()

        #az Ejecutar consultas. Pasandole las variables que recogieron los datos del formulario (marca, modelo, precio, ciudad)
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)", (marca, modelo, precio, ciudad)) #az %s = marca, %s = modelo, %s = precio y %s = ciudad. Se pone %s porque ocuparan DIFERENTES datos que se le pasara por el formulario. EL %s NO SERA PARA UN CAMPO EN ESPECIFICO.
        #az Guardar los datos en la BD
        cursor.connection.commit()

        #az Mensaje flash
        flash('Has creado el coche correctamente')
      
        return redirect(url_for('index'))

    return render_template('crear_coche.html')

@app.route('/coches')
def coches():

    cursor = mysql.connection.cursor() #az Crear el cursor
    cursor.execute("SELECT * FROM coches ORDER BY id DESC") #az Consultar la tabla coches
    coches = cursor.fetchall() #az Sacar toda la informacón dentro de la tabla coches
    cursor.close() #az Cuando se saque información del cursor, siempre hay que cerrarlo

    return render_template('coches.html', coches=coches)

@app.route('/coche/<coche_id>')
def coche(coche_id):

    cursor = mysql.connection.cursor() #az Crear el cursor
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id)) #az Consultar la tabla coches
    coche = cursor.fetchall() #az Sacar toda la informacón dentro de la tabla coches
    cursor.close() #az Cuando se saque información del cursor, siempre hay que cerrarlo

    return render_template('coche.html', coche=coche[0]) #an VA A DEVOLVER UNA SOLA TUPLA. POR ESO SE PONE [0] PARA ACCEDER SIEMPRE AL PRIMERO ELEMENTO DE LA TUPLA Y PODER RENDERIZAR LA PLANTILLA 'coche.html' SIN PROBLEMAS

#r BOTON "ELIMINAR"
@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):

    cursor = mysql.connection.cursor() #az Crear el cursor
    cursor.execute(f"DELETE FROM coches WHERE id = {coche_id}") #az Consultar la tabla coches
    mysql.connection.commit()

    #az Mensaje flash
    flash('El coche ha sido eliminado')

    return redirect(url_for('coches'))

#r BOTON "EDITAR"
@app.route('/editar-coche/<coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):

    #r SEGUNDO ENTRA AQUI: CUANDO HAYA DATOS POR EL METODO 'POST', SE ACTUALIZARA LOS CAMPOS DE LA TABLA COCHES
    if request.method == 'POST':

        #az Se recogen los datos que vienen por el método POST
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        #az Crear el cursor
        cursor = mysql.connection.cursor()

        #az Ejecutar consultas. Pasandole las variables que recogieron los datos del formulario (marca, modelo, precio, ciudad)
        cursor.execute(
        """
            UPDATE coches
            SET marca = %s, modelo = %s, precio = %s, ciudad = %s
            WHERE id = %s
        """, (marca, modelo, precio, ciudad, coche_id))
        #az Guardar los datos en la BD
        cursor.connection.commit()

        #az Mensaje flash
        flash('Has editado el coche correctamente')
      
        return redirect(url_for('coches'))

    #r PRIMERO ENTRA AQUÍ: COMO RECIEN SE HIZO CLICK EN EL BOTON "EDITAR", NO HAY INFORMACIÓN QUE ACTUALIZAR. SOLO MANDAR POR EL METODO 'POST' LOS DATOS DEL COCHE QUE SE QUIERE EDITAR
    cursor = mysql.connection.cursor() #az Crear el cursor
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id)) #az Consultar la tabla coches
    coche = cursor.fetchall() #az Sacar toda la informacón dentro de la tabla coches
    cursor.close() #az Cuando se saque información del cursor, siempre hay que cerrarlo

    return render_template('crear_coche.html', coche=coche[0]) #an VA A DEVOLVER UNA SOLA TUPLA. POR ESO SE PONE [0] PARA ACCEDER SIEMPRE AL PRIMERO ELEMENTO DE LA TUPLA Y PODER RENDERIZAR LA PLANTILLA 'coche.html' SIN PROBLEMAS

if __name__ == '__main__': #az Identificar que el __main__ es el archivo principal. Si el nombre de la aplicación de flask es "main"(LO QUE HEMOS CREADO), significa que es un proyecto de flask
    app.run(debug=True) #az debug=True porque necesitamos que el servidor de flask cuando arranque el programa este funcionando perfectamente. Y cuando se hague un cambio en el código el servidor se recarge o reinicie automaticamente
